"""Generate the SVG figures used by the Power Analysis post.

Uses only Python's standard library so an agent can regenerate the figures with:
python3 scripts/generate_power_figures.py
"""

from pathlib import Path
from statistics import NormalDist

NORMAL = NormalDist()
OUT = Path(__file__).parents[1] / "img"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#24282b"
MUTED = "#6b767b"
GRID = "#cbd1d4"
GOLD = "#c6a34b"
TURQUOISE = "#087f86"
SLATE = "#63747a"


def power(n_per_group: int, effect_size: float, alpha: float = 0.05) -> float:
    """Normal-approximation power for an equal-sized, two-sided two-sample test."""
    critical = NORMAL.inv_cdf(1 - alpha / 2)
    signal = effect_size * (n_per_group / 2) ** 0.5
    return NORMAL.cdf(-critical - signal) + 1 - NORMAL.cdf(critical - signal)


def required_n(effect_size: float, target_power: float, alpha: float = 0.05) -> int:
    critical = NORMAL.inv_cdf(1 - alpha / 2)
    return round(2 * (critical + NORMAL.inv_cdf(target_power)) ** 2 / effect_size**2)


def write_svg(path: Path, width: int, height: int, body: str) -> None:
    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">
<style>text{{font-family:system-ui,sans-serif;fill:{INK}}}.muted{{fill:{MUTED};font-size:13px}}.label{{font-size:14px;font-weight:650}}.grid{{stroke:{GRID};stroke-width:1}}.axis{{stroke:{INK};stroke-width:1.5}}</style>
<rect width="100%" height="100%" fill="#f1f3f4" rx="8"/>{body}</svg>''',
        encoding="utf-8",
    )


def power_curves() -> None:
    width, height = 760, 430
    left, right, top, bottom = 74, 34, 40, 66
    plot_w, plot_h = width - left - right, height - top - bottom
    x = lambda n: left + (n - 10) / 290 * plot_w
    y = lambda p: top + (1 - p) * plot_h
    pieces = [f'<text x="{left}" y="24" class="label">Power grows with sample size</text>']
    for fraction in (0, .2, .4, .6, .8, 1):
        ypos = y(fraction)
        pieces.append(f'<line x1="{left}" y1="{ypos:.1f}" x2="{width-right}" y2="{ypos:.1f}" class="grid"/>')
        pieces.append(f'<text x="{left-12}" y="{ypos+5:.1f}" text-anchor="end" class="muted">{fraction:.0%}</text>')
    for n in (10, 50, 100, 150, 200, 250, 300):
        xpos = x(n)
        pieces.append(f'<text x="{xpos:.1f}" y="{height-bottom+27}" text-anchor="middle" class="muted">{n}</text>')
    pieces.extend([
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" class="axis"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" class="axis"/>',
        f'<text x="{left+plot_w/2:.1f}" y="{height-14}" text-anchor="middle" class="muted">observations per group</text>',
    ])
    for effect, color, label in ((.2, SLATE, "d = 0.20"), (.35, TURQUOISE, "d = 0.35"), (.5, GOLD, "d = 0.50")):
        points = " ".join(f"{x(n):.1f},{y(power(n, effect)):.1f}" for n in range(10, 301, 5))
        pieces.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
        pieces.append(f'<circle cx="{x(300):.1f}" cy="{y(power(300, effect)):.1f}" r="4" fill="{color}"/>')
        pieces.append(f'<text x="{x(300)-8:.1f}" y="{y(power(300, effect))-9:.1f}" text-anchor="end" class="muted">{label}</text>')
    write_svg(OUT / "power-analysis-power-curves.svg", width, height, "".join(pieces))


def sample_size_chart() -> None:
    targets = (.7, .8, .9, .95)
    values = [required_n(.35, target) for target in targets]
    width, height = 760, 330
    left, right, top, bottom = 74, 34, 40, 58
    plot_w, plot_h = width - left - right, height - top - bottom
    maximum = 220
    y = lambda n: top + (1 - n / maximum) * plot_h
    pieces = [f'<text x="{left}" y="24" class="label">More certainty requires more data</text>']
    for n in (0, 50, 100, 150, 200):
        ypos = y(n)
        pieces.append(f'<line x1="{left}" y1="{ypos:.1f}" x2="{width-right}" y2="{ypos:.1f}" class="grid"/>')
        pieces.append(f'<text x="{left-12}" y="{ypos+5:.1f}" text-anchor="end" class="muted">{n}</text>')
    bar_w, gap = 92, 56
    start = left + 58
    for index, (target, value) in enumerate(zip(targets, values)):
        xpos = start + index * (bar_w + gap)
        bar_y = y(value)
        color = TURQUOISE if target == .8 else GOLD if target == .9 else SLATE
        pieces.append(f'<rect x="{xpos}" y="{bar_y:.1f}" width="{bar_w}" height="{top+plot_h-bar_y:.1f}" rx="4" fill="{color}"/>')
        pieces.append(f'<text x="{xpos+bar_w/2}" y="{bar_y-10:.1f}" text-anchor="middle" class="label">{value}</text>')
        pieces.append(f'<text x="{xpos+bar_w/2}" y="{height-bottom+26}" text-anchor="middle" class="muted">{target:.0%} power</text>')
    pieces.extend([
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" class="axis"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" class="axis"/>',
        f'<text x="{left+plot_w/2:.1f}" y="{height-12}" text-anchor="middle" class="muted">required observations per group for d = 0.35</text>',
    ])
    write_svg(OUT / "power-analysis-sample-size.svg", width, height, "".join(pieces))


if __name__ == "__main__":
    power_curves()
    sample_size_chart()
    print("Generated power-analysis-power-curves.svg and power-analysis-sample-size.svg")
