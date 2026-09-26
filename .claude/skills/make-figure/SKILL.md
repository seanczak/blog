---
name: make-figure
description: Turns a data file into one chart for an idea in this blog repo: a rerunnable plot script in content/<area>/<idea>/src/ plus a compressed PNG in its img/. Use for any request to chart, plot or visualize data, e.g. "plot X from this CSV", "make a figure showing Y", "chart Z for the post".
---

# Make a figure

- **Files:** the script goes to `<idea_dir>/src/plot_<figure_name>.py` and the image to `<idea_dir>/img/<figure_name>.png`; both are committed. Data normally sits in the idea's `notshared/`. If it's unclear which data file to use, ask.
- **Script:** start from [`plot_script_template.py`](plot_script_template.py) and keep its `save_png` call (from [`compress_pngs.py`](compress_pngs.py)), which saves at 100 dpi and palette-compresses the PNG.
- **Chart:** units on both axis labels; a title naming what's plotted, not a conclusion; a legend only for two or more series; currency written `\$`, since matplotlib reads a bare `$` as math.
- **Size:** keep images under about 150 KB. If one comes out larger, tell the human rather than cutting resolution or content.
- **Caption numbers:** only ones the script prints.
- **Embed:** `![<alt text>]({{ '/content/<area>/<idea>/img/<figure_name>.png' | relative_url }})`
