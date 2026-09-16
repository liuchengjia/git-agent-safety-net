# Initial local delivery: post-review revisions and validation

This document records the first local delivery. The later 7+3-minute presentation and GitHub Pages publication are described in README.md and docs/presenter-guide.md; the historical statements below are not current deployment status.

## Round 001

All three independent seats recommended **minor polish**. Their reports and synthesis in `rounds/round-001/` are immutable records of the reviewed snapshot. The changes below were made afterward as ordinary editing; no second independent review is claimed.

| Docket item | Disposition | Evidence |
| --- | --- | --- |
| Pager navigation | Done | New identity/navigation unit explains Space and q before the first diff. |
| Status whitespace | Done | Expected status is a fenced literal block with a leading blank and both columns explained. |
| Document headings | Done | Document-only header reserves space for sections; Git manuals is unnumbered. |
| Branch visual | Done | A before/after graph identifies baseline, guarded evaluator, and plan, and shows main moving. |
| Live-path signposting | Done | Preparation names the sequence; recovery reference is explicitly alternatives. |
| Course labels | Done | Conclusion expands C1 and describes the C2/C4 generate-evaluate-select loop. |

## Validation

- `python examples/verify_demo.py`: passed the baseline, useful edit, expected bad-edit failure, explicit restoration, staged-mistake behavior, unstage, hard reset, revert, branch isolation, fast-forward merge, divergence refusal, and overwrite guard. All recovery operations ran inside an automatically generated temporary lab.
- `just engine=tectonic build`: built both PDFs and the website from the same Markdown. Exact local tools: Git 2.53.0.windows.3, Pandoc 3.11, just 1.58.0, Tectonic 0.17.0. The default XeLaTeX route and remote Actions workflow were not executed locally.
- PDF page images were inspected, including the title, dense command/recovery units, branch graph, and bibliography. Text bounds and internal website anchors/PDF links were checked.
- The website was opened in a local browser for a desktop layout check. No mobile browser run or remote deployment is claimed.
- Tectonic emitted Fontconfig discovery/system-font warnings on this Windows machine. They did not prevent a successful build or readable output; exact font rendering can vary on another machine.

## Delivery scope

This is a local source-and-output delivery. No repository commit, push, pull request, or Pages deployment was performed. The source checkout retains the upstream history at `343592935cb95ac7f47b18a6425a79bce29665ef`. Generated PDFs and `_site/` remain ignored by Git. The PySR item is an experiment plan, not an installed or evaluated baseline.
