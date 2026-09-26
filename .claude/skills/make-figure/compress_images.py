"""Shrink images before they are committed.

Every revision of a committed image stays in the repository history, so the
reduction has to be applied up front. Two cases:

- Flat-colour images (charts, diagrams, screenshots of text) are PNGs
  re-encoded with an adaptive palette of at most 256 colours. They look the
  same and typically lose half their bytes or more.
- Photos have too many colours for a palette, which would band them, so they
  are JPEGs at quality 82.

In a plot script, call ``save_png(fig, target)`` in place of ``fig.savefig``.
From a shell, shrink existing PNGs in place, or convert a photo saved as PNG
to JPEG with ``--photo``. An existing JPEG is left alone, since re-encoding
one loses quality every time:

    python3 .claude/skills/make-figure/compress_images.py content/<area>/<idea>/img/*.png
    python3 .claude/skills/make-figure/compress_images.py --photo content/<area>/<idea>/img/header.png
"""

import argparse
import logging
import pathlib

import PIL.Image

MAX_COLOURS = 256
SAVE_DPI = 100
JPEG_QUALITY = 82
PNG_SUFFIXES = {".png"}
JPEG_SUFFIXES = {".jpg", ".jpeg"}

logger = logging.getLogger(__name__)


def shrink_png(target: pathlib.Path, max_colours: int = MAX_COLOURS) -> int:
    """Quantize the PNG at ``target`` in place and return bytes saved."""
    size_before = target.stat().st_size
    with PIL.Image.open(target) as original:
        reduced = original.convert("RGB").quantize(colors=max_colours)
    reduced.save(target, format="PNG", optimize=True)
    return size_before - target.stat().st_size


def save_jpeg(source: pathlib.Path, target: pathlib.Path) -> None:
    """Write the photo at ``source`` to ``target`` as a progressive JPEG."""
    with PIL.Image.open(source) as original:
        photo = original.convert("RGB")
    photo.save(
        target, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True
    )


def save_png(fig, target: pathlib.Path, dpi: int = SAVE_DPI) -> None:
    """Write a matplotlib figure to ``target`` and shrink it."""
    fig.savefig(target, dpi=dpi)
    shrink_png(pathlib.Path(target))


def compress_path(image_path: pathlib.Path, is_photo: bool) -> pathlib.Path:
    """Shrink ``image_path`` by its type and return where the result is.

    With ``is_photo``, a PNG is converted to a JPEG beside it and the PNG is
    deleted. A JPEG is returned untouched. Raises ValueError for a suffix
    that isn't PNG or JPEG.
    """
    suffix = image_path.suffix.lower()
    if is_photo and suffix in PNG_SUFFIXES:
        jpeg_path = image_path.with_suffix(".jpg")
        save_jpeg(image_path, jpeg_path)
        image_path.unlink()
        return jpeg_path
    if suffix in PNG_SUFFIXES:
        shrink_png(image_path)
        return image_path
    if suffix in JPEG_SUFFIXES:
        logger.info(f"{image_path}: already JPEG, left as is")
        return image_path
    raise ValueError(f"{image_path}: expected .png, .jpg or .jpeg")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description="Shrink PNG files in place.")
    parser.add_argument(
        "images", nargs="+", type=pathlib.Path, help="image files to shrink"
    )
    parser.add_argument(
        "--photo",
        action="store_true",
        help="treat PNG inputs as photos: convert each to a .jpg and delete the .png",
    )
    args = parser.parse_args()
    for image_path in args.images:
        size_before_kb = image_path.stat().st_size / 1024
        try:
            result_path = compress_path(image_path, args.photo)
        except ValueError as error:
            logger.error(error)
            continue
        size_after_kb = result_path.stat().st_size / 1024
        logger.info(f"{result_path}: {size_before_kb:.1f} KB -> {size_after_kb:.1f} KB")
