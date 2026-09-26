# Repo Structure

```text
blog/
├── content/      # ideas: notes, outlines, and posts (content_curation.md)
├── docs/         # repo conventions (this file and the docs below)
├── jekyll/       # how the site is built and served (publishing_with_jekyll.md, site_design.md)
├── notshared/    # gitignored private scratch space
├── _config.yml   # Jekyll config; GitHub Pages reads it only from the root
├── .gitignore
├── README.md
├── AGENTS.md     # agent entry point; indexes these docs
└── CLAUDE.md     # imports AGENTS.md for Claude Code
```

## Keep the top level clean

The root holds only what's listed above. Everything else goes one level down: the Jekyll `Gemfile` and preview script live in `jekyll/`, and figure scripts live in their idea's `src/`. Before adding a file or directory at the root, check whether it fits in an existing directory, and ask the human if it doesn't.

## Where the details are

| Doc | Covers |
|---|---|
| [agent_guidelines.md](agent_guidelines.md) | how agents work here: role, context documents, numbers, figures, keeping docs current, tools, git |
| [content_curation.md](content_curation.md) | `content/`: idea directories, notes → outline → post, naming, what isn't tracked |
| [publishing_with_jekyll.md](publishing_with_jekyll.md) | `jekyll/` and `_config.yml`: GitHub Pages, local preview, post front matter |
| [site_design.md](site_design.md) | how the site looks and its pages behave: style, header, landing-page tree, archive, articles |
| [writing_style.md](writing_style.md) | how to write notes, outlines, posts, docs, and chat replies |
| [coding_style.md](coding_style.md) | Python and SQL conventions |

The repo is public. `notshared/` is gitignored at every depth, so anything private goes in the nearest `notshared/`.
