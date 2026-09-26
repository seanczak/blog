# Content Structure

## Purpose

The repo serves as both a lab bench and a publishing source. The bulk of it is in-progress thinking; only what sits in a `_posts/` folder is finished and meant to be taken at face value. The rest (drafts, scratch work, supporting evidence) shows how a post came to be, not what it concludes.

This doc is about `content/`, where ideas are kept and refined. The repo root is covered in [repo_structure.md](repo_structure.md). Site building and serving (`_config.yml`, `jekyll/`, post front matter, GitHub Pages) is covered in [publishing.md](../site/publishing.md).

## Levels of refinement

An idea's material passes through three tracked stages. A fourth, private stage stays on the local machine:

| Level | File | Written by | Refinement |
|---|---|---|---|
| Private | `notshared/` | anyone | Gitignored scratch space. Never committed, never published. |
| Notes | `notes.md` | mostly the agent | Long-form log of the exploration: methods, results, abandoned paths, supporting evidence. |
| Outline | `outline.md` | mostly the human | What makes the cut and in what order: the post's argument and the evidence behind each step. |
| Post | `_posts/YYYY-MM-DD-slug.md` | human and agent | Finished prose, published through GitHub Pages. |

Precedence follows refinement: post over outline, outline over notes. Notes are a snapshot of the exploration as it happened. Once an outline or post has absorbed them, they can go out of date without anyone updating them.

## Directory layout

```text
content/
├── <area>/                    # broad grouping, e.g. ai, statistics
│   ├── <idea>/                # one directory per idea, e.g. file_structure
│   │   ├── notes.md           # exploration log
│   │   ├── outline.md         # skeleton of the eventual post
│   │   ├── _posts/            # the post itself (Jekyll requires this exact name)
│   │   │   └── YYYY-MM-DD-slug.md
│   │   ├── src/               # scripts behind the figures and numbers in the markdown
│   │   ├── img/               # figures written by src/ and embedded in the post
│   │   └── notshared/         # gitignored; data and private drafts
│   └── <idea>/
│       └── ...                # most ideas only have some of these
└── <area>/
    └── ...
```

## Conventions

### Naming

- **Area and idea directories:** brief `snake_case` names describing the subject, so the contents are guessable from the name. No date in the name; the post's filename holds the date.
- **Ordered ideas:** when the ideas in a directory are meant to be read in sequence, prefix each idea directory with a two-digit index (`00_production_code_for_ds`, `01_dry`) so the file tree lists them in order. Display order on the site still comes from `jekyll/_data/tree.yml`.
- **Post files:** `YYYY-MM-DD-short-title.md`. Front matter is described in [publishing.md](../site/publishing.md#writing-a-post).

### Inside an idea directory

Most ideas begin as a single `notes.md`; other files appear as they're needed, not in advance. When it's unclear where something belongs, the agent asks a quick yes/no question, e.g. "Draft an `outline.md` from the notes?" or "Commit this CSV, or keep it in `notshared/`?"

- **`notes.md`**: the working memory of the idea. It exists so that:
    - findings survive a fresh session, and the context window can be reset freely
    - another agent can audit or argue with choices made earlier
    - the outline and the post have something to draw from
- **`outline.md`**: where exploration turns into an argument. It records the claim, the section order and what evidence supports each section. Since it's where anyone resuming the idea should start, it links to the relevant parts of `notes.md`, `src/` and `img/`.
- **`_posts/`**: the finished article, kept alongside the notes and outline it grew from.
- **Other markdown**: add it when it helps (a comparison table, a reading list), and link it from the outline.
- **`src/`**: the code that really produced each figure or quoted number. A clean checkout must be able to rerun it, and every generated figure has its script committed.
- **`img/`**: what `src/` writes, embedded in the post and other markdown.

Together, the markdown, `src/` and `img/` do the job a notebook would. They produce readable git diffs, and an agent moves through plain files more easily than through notebook JSON.

To resume an idea in a new session, point the agent at its directory and have it read `outline.md` first, opening `notes.md` only where needed.

### What isn't tracked

- **Everything committed is public.** Notes and outlines don't appear on the blog, but anyone can read them on GitHub. Keep private material in `notshared/`.
- `notshared/` is ignored at any depth (repo root, area or idea). It holds data files (CSV, pickle, JSON extracts), private drafts, and anything copied in from elsewhere that can't be public.
- `data/` is ignored at any depth too, as a backstop. `notshared/` is still the place for data.
- New data files go to `notshared/`. Writing one to a tracked path requires the human's explicit approval.
- The ignore rules are themselves a convention. Changes to them are agreed with the human and made together, in one change, across [`.gitignore`](../../.gitignore), the `exclude` list in [`_config.yml`](../../_config.yml), this doc and [publishing.md](../site/publishing.md).
