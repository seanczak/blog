# Blog

The docs below define how to work here. Each is listed with an `@` so it's loaded at the start of every session: Claude Code pulls `@` files in automatically, through this file and `CLAUDE.md`. Any other agent should read all of them before its first action.

Token counts were measured 2026-09-26 (Claude Code 2.1.283) as the extra startup context each import adds on its own. All six together add ~9.8K tokens on top of a ~29K baseline (~39K total). Re-measure with the method in `docs/agent_guidelines.md` after editing a doc.

- @docs/agent_guidelines.md (1.1K tokens): your role, reading context documents, numbers, figures, tools, git.
- @docs/writing_style.md (1.4K tokens): register, structure, and voice for notes, outlines, posts, docs, and chat.
- @docs/coding_style.md (2.4K tokens): Python and SQL conventions for code in `src/`.
- @docs/repo_structure.md (0.8K tokens): the repo root and keeping it clean.
- @docs/content_curation.md (2.1K tokens): idea directories in `content/`, notes → outline → post, naming, what gets tracked or kept in `notshared/`.
- @docs/publishing_with_jekyll.md (2.4K tokens): post front matter, publishing, `_config.yml` and `jekyll/`, local preview, design.

## Skills

Skills live in `.claude/skills/<name>/SKILL.md`. Claude Code discovers them automatically; other agents should open the matching `SKILL.md` when a request fits. There is one so far:

| Skill | Use when |
|---|---|
| `make-figure` | a chart, plot or figure is needed from a data file. It saves a rerunnable plot script in the idea's `src/` and a compressed PNG in its `img/` |
