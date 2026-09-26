---
name: make-figure
description: Puts an image into an idea in this blog repo, compressed, in content/<area>/<idea>/img/. Covers charts made from a data file (plus a rerunnable plot script in the idea's src/) and any other image - a photo, diagram or figure brought in from elsewhere, or one edited or converted in Python. Use for any request to chart, plot or visualize data ("plot X from this CSV", "chart Z for the post") and whenever an image is added to or changed in img/.
---

# Make a figure

Applies to every image that lands in an idea's `img/`.

- **Location:** `<idea_dir>/img/<figure_name>.<ext>`, committed. Names are lowercase with hyphens.
- **Compression:** everything goes through [`compress_images.py`](compress_images.py), never an improvised PIL call.
    - Charts, diagrams, screenshots of text: PNG, palette-compressed.
    - Photos: JPEG at quality 82 (a palette would band them). A photo that arrives as PNG gets `--photo`.
    - Run `python3 .claude/skills/make-figure/compress_images.py [--photo] <files>` and quote the before/after sizes it logs.
- **Size:** keep images under about 150 KB. If one comes out larger, tell the human rather than cutting resolution or content.
- **Embed:** `![<alt text>]({{ '/content/<area>/<idea>/img/<figure_name>.<ext>' | relative_url }})`. Alt text describes what the image shows, including the numbers on a chart's axes.

## Chart specifics

For a chart drawn from data.

- **Files:** the script goes to `<idea_dir>/src/plot_<figure_name>.py` and the image to `<idea_dir>/img/<figure_name>.png`; both are committed. Data normally sits in the idea's `notshared/`. If it's unclear which data file to use, ask.
- **Script:** start from [`plot_script_template.py`](plot_script_template.py) and keep its `save_png` call, which saves at 100 dpi and palette-compresses the PNG.
- **Chart:** units on both axis labels; a title naming what's plotted, not a conclusion; a legend only for two or more series; currency written `\$`, since matplotlib reads a bare `$` as math.
- **Caption numbers:** only ones the script prints.

## Image specifics

For an image that isn't drawn from data: a photo, a diagram, or a figure brought in from elsewhere (a web page, an old post).

- **Source:** download the largest version available, then compress it as above.
- **Provenance:** an image that wasn't made here gets a caption naming its source and author (e.g. *Source: Unsplash. Photographer: Eivarain.*). Check that its license allows reuse; if unsure, ask.
- **Script:** none is needed for an image used as-is. If Python edits or converts it (crop, resize, annotate), that edit is a script in `<idea_dir>/src/` like a chart's.
