---
name: pages-build-check
description: Waits for the GitHub Pages build of a pushed commit in this blog repo and reports its outcome. Start it in the background after a push to main that changes the built site (not only docs, notes, outlines, src/ or .claude/), passing the pushed commit SHA.
tools: Bash
model: haiku
---

Reports whether GitHub Pages built a commit just pushed to `seanczak/blog`. The prompt supplies the commit SHA, short or full.

## Procedure

1. In a single Bash loop, poll the latest build every 10 s for at most 5 min:

   ```bash
   /home/sfronczak/.local/bin/gh api repos/seanczak/blog/pages/builds/latest --jq '.status+" "+.commit'
   ```

   Stop when the status is `built` or `errored` and the commit begins with the given SHA. A build for an earlier commit means the pushed one hasn't started; continue polling.

2. Return one of the following, with the short SHA filled in:

   | Outcome | Report |
   |---|---|
   | Built | `Pages built <sha>. Reload the page (F5, or pull to refresh on a phone) if it still shows the old version.` |
   | Errored | `Pages build errored on <sha>:` followed by `error.message` from `gh api repos/seanczak/blog/pages/builds/latest`. |
   | Timed out | `Pages build for <sha> not finished after 5 min; last status: <status> <commit>.` |

## Scope

Read-only: no file edits, commits or commands other than the `gh api` calls above.
