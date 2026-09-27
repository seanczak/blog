# Writing Style

These rules cover every piece of text produced here: notes, outlines, posts, the docs in `docs/`, and replies in chat. They hold for the whole session; only the human can relax them.

## blog document specific styles

[Agentic Coding for ML Model Pipelines - Part 1](../../content/ai/ai_code_workflow/00_production_code_for_ds/_posts/2026-09-19-agentic-coding-for-ml-pipelines-part-1.md) is an example of how a post should look. It's the reference for the author's current voice; the posts imported from Medium (2020–2021) are older and aren't a model for new writing.

*Note for Sean:* observations on the blog voice, drawn from all the posts so far, are saved in `content/infra/writing_styles/notes.md`. We can revisit them if and when we decide to expand the agent's default blog voice in this section. Agents: don't apply them until then.

## Audience and density

- The reader is a technically trained peer. Now and then it's someone without that background, so a term that needs a definition gets one.
- Quantities and claims do the work. Sentences exist to connect them, not to pad them.
- The human often phrases a request informally. The written result should be tighter and more exact than the request was.
- Brevity is the default everywhere. Depth is added when the human asks for it, not in anticipation.

## Shape of a `notes.md` document

- Measurements and comparisons go in tables.
- Alternatives, procedures and conclusions go in bulleted or numbered lists, nested where grouping helps.
- Reasoning that has to flow can be a short paragraph of a few sentences at most.
- Every number carries its unit, percentages included, and so does every chart axis.
- A variable is defined in the text at the point it first appears.
- Long unbroken prose is out.
- Each claim is labeled by how it's known: checked against data, or reasoned toward. Weak confidence is said out loud.

## Tone for exploratory findings in `notes.md` documents

Most of the writing here comes out of work in progress: hypotheses being tested, checks still running, answers not yet settled. The prose should read that way. The repo is public, so the people behind a dataset, system or tool being discussed may well read what's written about it. Write as a guest looking at someone else's work with interest.

- **Describe first, explain later.** Early in an investigation, and before hearing from whoever built the system, report what the data shows. Leave the cause as an open question.
- **Keep verdicts out of the vocabulary.** Words that pass judgment on a system, or guess at hidden motives, stay out even when a result looks striking. State the measurement, list the candidate explanations, and note who could confirm. For example: *"about 12% of upstream rows have no downstream match; candidates include a filter, a late-arriving batch or a key mismatch; the pipeline's maintainers would know."*
- **Section titles name the question being asked.** *"Where do the unmatched rows go?"* works. A title announcing the answer, or labeling a component as faulty, does not.
- **Keep the evidence status attached.** A join or mechanism that was tested says so. One that was assumed says that instead. Plausibility doesn't promote a guess to a finding.
- **A tone correction applies to the whole file.** When the human softens one passage, bring every similar passage in the document to the same register, including sections of personal opinion.

## Markdown documents

### Paths

Paths are given from the repo root, beginning at the shortest prefix that identifies the file without ambiguity, e.g. `content/statistics/2020_election_series/01_virginia/img/statewide-totals.png`. Machine-specific prefixes such as a home directory never appear.

### Currency

In prose, a dollar sign is written `\$` (as in `\$4.2K`). Several renderers, GitHub and VS Code among them, treat a pair of bare `$` as inline math and hide the text between them. Inside backticks no escape is needed. Genuine math keeps plain delimiters: `$x$`, `$$…$$`.

### Table of Contents

Posts get a generated table of contents (see [publishing.md](../site/publishing.md)). A `notes.md` built from repeating blocks (say, one block per experiment, each with setup, run and outcome) gets a hand-written one at the top.

- List headings through h3:`###` unless a section's own layout needs finer entries.
- Switch depth without asking when the human requests it, or when this file or a related one read earlier in the session already uses another depth. Consistency wins.
- Anchor slugs mangle some characters (escaped `\$`, em dashes, `§`, apostrophes). Guess the slug, point out the doubtful ones, and fix whichever links fail after rendering.
