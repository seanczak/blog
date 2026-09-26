# Site Design

How the site looks and how its pages behave. How it's built and published, and what a post file needs, is in [publishing.md](publishing.md).

## Style

- Quiet editorial style: grey base, turquoise (`#087f86`) for content links and interaction, opaque gold (`#c6a34b`) for 2px structural dividers and the portrait trim.
- Header: portrait, name, then Topics / Archive / About / LinkedIn. Header links are charcoal, and turquoise only on hover.

## Pages

- Landing page (`/`): a topic tree of sections, groups and posts, with a sticky right-hand list of sections and their groups. Groups are native `<details>` elements, collapsed by default, and a group with no posts shows "Posts to come."; clicking a group title, or its link in the right-hand list, expands it. Structure, order and blurbs come from `jekyll/_data/tree.yml`, not from folders. Posts are referenced by `slug` (file name minus date); a `blurb` there overrides the post's `description`. A slug that matches no post is skipped and leaves an HTML comment in the page.
- Archive (`/archive/`): chronological post list with a sticky right-hand Categories filter. No hero, no "Writing" heading, no card-heavy design.
- Articles: categories appear beneath the title. The table of contents hides below a `56rem` viewport width.

## Implementation

- Implement dynamic state programmatically and deterministically. Don't use DOM-position selectors (for example `:first-child`) for filtered or sorted state. Derive it from visible data and apply explicit classes.
