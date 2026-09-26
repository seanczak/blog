"""Schematic: how a Claude Code conversation grows turn by turn and which blocks are cache read, cache write, or output."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle

TICKET_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = next(p for p in TICKET_DIR.parents if (p / ".git").exists())
sys.path.insert(0, str(REPO_ROOT / "src"))
from compress_pngs import save_plot  # noqa: E402

OUT_PATH = TICKET_DIR / "img" / "prompt_cache_growth.png"

# Okabe-Ito based, colourblind-friendly.
COLOURS = {
    "read": "#A9B8C8",    # muted grey-blue
    "write": "#E69F00",   # orange
    "output": "#009E73",  # bluish green
}
LEGEND_LABELS = {
    "read": "cache read (already cached from an earlier turn)",
    "write": "cache write (new input this turn)",
    "output": "output (reply generated this turn)",
}

# Conversation chunks in order: (label, number of blocks).
CHUNKS = [
    ("system + tools", 4),
    ("msg 1", 1),
    ("reply 1", 2),
    ("msg 2", 1),
    ("reply 2", 2),
    ("msg 3", 1),
    ("reply 3", 2),
]
N_TURNS = 3
BLOCK_W = 1.0
BLOCK_H = 0.8
GAP = 0.12
ROW_STEP = 1.9


def load_plot_df() -> list[list[tuple[str, int, str]]]:
    """Build the hardcoded layout: per turn, a list of (label, n_blocks, role)."""
    turns = []
    for t in range(1, N_TURNS + 1):
        n_chunks = 1 + 2 * t  # system + (msg, reply) per turn so far
        rows = []
        for i, (label, n) in enumerate(CHUNKS[:n_chunks]):
            if i == n_chunks - 1:
                role = "output"  # the reply being generated now
            elif i >= n_chunks - 3 and t > 1:
                role = "write"   # previous reply + new message
            elif t == 1:
                role = "write"   # first turn: everything input is new
            else:
                role = "read"
            rows.append((label, n, role))
        turns.append(rows)
    return turns


def build_figure(turns: list[list[tuple[str, int, str]]]) -> plt.Figure:
    """Draw the stacked block rows, labels, arrow, and legend."""
    fig, ax = plt.subplots(figsize=(11, 5.2))
    total_blocks = sum(n for _, n in CHUNKS)

    for t_idx, rows in enumerate(turns):
        y = -t_idx * ROW_STEP
        ax.text(-0.4, y + BLOCK_H / 2, f"Turn {t_idx + 1}", ha="right",
                va="center", fontsize=12, fontweight="bold")
        x = 0.0
        for label, n, role in rows:
            start = x
            for _ in range(n):
                ax.add_patch(Rectangle((x + GAP / 2, y), BLOCK_W - GAP, BLOCK_H,
                                       facecolor=COLOURS[role], edgecolor="white",
                                       linewidth=0))
                x += BLOCK_W
            ax.text((start + x) / 2, y - 0.12, label, ha="center", va="top",
                    fontsize=9, color="#333333")
        print(f"Turn {t_idx + 1}: {int(x)} blocks "
              f"({', '.join(f'{l}={r}' for l, _, r in rows)})")

    # Leftward arrow above the top bar.
    top = BLOCK_H + 0.45
    ax.annotate("", xy=(0.2, top), xytext=(total_blocks - 0.2, top),
                arrowprops=dict(arrowstyle="-|>", color="#444444", lw=1.6,
                                mutation_scale=18))
    ax.text(total_blocks / 2, top + 0.15,
            "the LLM only looks left (backward): earlier blocks never change, "
            "so they can be reused",
            ha="center", va="bottom", fontsize=10, style="italic",
            color="#444444")

    handles = [Patch(facecolor=COLOURS[k], label=LEGEND_LABELS[k])
               for k in ("read", "write", "output")]
    ax.legend(handles=handles, loc="upper center", ncol=3, frameon=False,
              bbox_to_anchor=(0.5, -0.02), fontsize=10)

    ax.set_xlim(-2.0, total_blocks + 0.3)
    ax.set_ylim(-(N_TURNS - 1) * ROW_STEP - 0.8, top + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Each turn re-sends the whole conversation; "
                 "only the new part is computed", fontsize=13)
    fig.tight_layout()
    return fig


def main() -> None:
    turns = load_plot_df()
    fig = build_figure(turns)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    save_plot(fig, OUT_PATH)
    print(f"{OUT_PATH}: {OUT_PATH.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
