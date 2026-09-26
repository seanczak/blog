"""Reduce chart PNGs to an indexed palette before they are committed.

A chart contains only a handful of colours, so re-encoding it with an adaptive
palette (256 entries at most) leaves it looking the same while typically
cutting the byte count by half or more. Every revision of a committed image
stays in the repository history, so the reduction has to be applied up front.

In a plot script, call ``save_png(fig, target)`` in place of ``fig.savefig``.
From a shell, shrink existing files in place:

    python3 .claude/skills/make-figure/compress_pngs.py content/<area>/<idea>/img/*.png
"""

import argparse
import pathlib

import PIL.Image

MAX_COLOURS = 256
SAVE_DPI = 100


def shrink(target: pathlib.Path, max_colours: int = MAX_COLOURS) -> int:
    """Quantize the PNG at ``target`` in place and return bytes saved."""
    size_before = target.stat().st_size
    with PIL.Image.open(target) as original:
        reduced = original.convert("RGB").quantize(colors=max_colours)
    reduced.save(target, format="PNG", optimize=True)
    return size_before - target.stat().st_size


def save_png(fig, target: pathlib.Path, dpi: int = SAVE_DPI) -> None:
    """Write a matplotlib figure to ``target`` and shrink it."""
    fig.savefig(target, dpi=dpi)
    shrink(pathlib.Path(target))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shrink PNG files in place.")
    parser.add_argument("pngs", nargs="+", type=pathlib.Path, help="PNG files to shrink")
    for png in parser.parse_args().pngs:
        saved_bytes = shrink(png)
        print(f"{png}: saved {saved_bytes / 1024:.1f} KB, now {png.stat().st_size / 1024:.1f} KB")
