"""Plots <quantity shown> as evidence for <claim in the idea's notes or post>."""

import importlib.util
import pathlib

import matplotlib.pyplot as plt
import pandas as pd

SCRIPT_PATH = pathlib.Path(__file__).resolve()
IDEA_DIR = SCRIPT_PATH.parent.parent  # content/<area>/<idea>/
REPO_ROOT = IDEA_DIR.parent.parent.parent  # repository root

_helper_spec = importlib.util.spec_from_file_location(
    "compress_pngs", REPO_ROOT / ".claude/skills/make-figure/compress_pngs.py"
)
compress_pngs = importlib.util.module_from_spec(_helper_spec)
_helper_spec.loader.exec_module(compress_pngs)

DATA_PATH = IDEA_DIR / "notshared/<data_file>"
FIGURE_PATH = IDEA_DIR / "img/<figure_name>.png"


def read_source(data_path: pathlib.Path) -> pd.DataFrame:
    """Return the rows and columns the chart needs, tidied for plotting."""
    frame_df = pd.read_csv(data_path)
    return frame_df


def draw(frame_df: pd.DataFrame) -> plt.Figure:
    """Render the chart. Units go in axis labels; currency is written `\\$`."""
    fig = plt.figure(figsize=(7.5, 4.2), layout="constrained")
    ax = fig.add_subplot()
    ax.set(
        title="<quantity plotted>",
        xlabel="<x quantity [unit]>",
        ylabel="<y quantity [unit]>",
    )
    return fig


if __name__ == "__main__":
    fig = draw(read_source(DATA_PATH))
    FIGURE_PATH.parent.mkdir(exist_ok=True)
    compress_pngs.save_png(fig, FIGURE_PATH)
    # Print every number the caption will quote, then the file size.
    size_kb = FIGURE_PATH.stat().st_size / 1024
    print(f"wrote {FIGURE_PATH.relative_to(REPO_ROOT)} ({size_kb:.1f} KB)")
