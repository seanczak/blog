# Site Design

How the site looks and how its pages behave. How it's built and published, and what a post file needs, is in [publishing.md](publishing.md).

## Style

- Quiet editorial style: grey base, turquoise (`#087f86`) for content links and interaction, opaque gold (`#c6a34b`) for 2px structural dividers and the portrait trim.
- Fonts: one font across the whole site (Georgia, falling back to a system serif), headings, titles, navigation and labels included.
- Header: portrait, name, then Topics / Archive / About, then LinkedIn and GitHub (this repo) icons. On phone-width screens (below `$phone`) the text links fold into a three-line menu button beside the icons, a native `<details>` dropdown with no script. Header links, icons included, are charcoal, and turquoise only on hover.

## Pages

- Landing page (`/`): a topic tree of sections, groups and posts, with a sticky right-hand list of sections and their groups. Groups are native `<details>` elements, collapsed by default, with only one open at a time, and a group with no posts shows "Posts to come."; clicking a group title, or its link in the right-hand list, expands it. Structure, order and blurbs come from `jekyll/_data/tree.yml`, not from folders. Posts are referenced by `slug` (file name minus date); a `blurb` there overrides the post's `description`. A slug that matches no post is skipped and leaves an HTML comment in the page.
- Archive (`/archive/`): chronological post list with a sticky right-hand Categories filter. No hero, no "Writing" heading, no card-heavy design.
- 404 (`jekyll/404.md`): a short "Page not found" note linking to the topics and the archive.
- Articles: categories appear beneath the title. The table of contents hides below a `56rem` viewport width.

## Implementation

- The font is set once, as `$font` in `jekyll/_sass/_base.scss`, applied to `body` and inherited everywhere else (form controls are told to inherit it). Component rules never set `font-family`.
- Colors come only from the tokens in `jekyll/_sass/_tokens.scss`. Dark mode redefines the tokens; component rules never repeat a color.
- One Sass partial per component (header, sidebar, categories, archive, post, topic tree), each with its own responsive rules.
- Page behavior lives in `jekyll/assets/js/<name>.js`, one file per interactive page. A page or layout opts in with `script: <name>` in its front matter; templates carry no inline scripts.
- Header links are data (`jekyll/_data/navigation.yml`), not markup. A link with `icon: <name>` shows the inline SVG `jekyll/_includes/icons/<name>.svg` (filled with `currentColor`) and keeps its title as the `aria-label`.
- Implement dynamic state programmatically and deterministically. Don't use DOM-position selectors (for example `:first-child`) for filtered or sorted state. Derive it from visible data and apply explicit classes.
