# Visual & Multi-Register Exposition — Round 1

**Recommendation:** minor polish
Readable rendered slides and a coherent workflow, with a missing branch visual and small cross-register presentation defects.

## Slide overflow
- none

## Strengths
- `sections/01-context.prose.md` — The three-state text diagram earns its place: labeled transitions distinguish copying into staging from committing, and the two comparison lines identify what each diff compares. It remains legible in the inspected document page 2 and rendered slide image 04.
- `sections/03-content.prose.md` — Action-oriented headings, short command blocks, and explicit expected results work well in all three registers. Rendered slide images 10 and 15–18 show the dense baseline, recovery, branching, merge, and sharing units fitting without clipping; this is rendered evidence, not a length estimate. Source-based estimates for the remaining units do not indicate overflow.
- `sections/04-conclusion.prose.md` — The staged-versus-working prediction question tests the state model rather than repeating commands. Rendered reference slides 23–24 retain readable text and links across two frames.
- `_site/index.html` — Nested navigation and specific, anchored workflow headings make the web document scannable. The CSS provides responsive single-column layout and internal code scrolling; these are source observations, not a browser-render verification.

## Weaknesses
- `sections/03-content.prose.md` — Branches and fast-forward integration are the single idea most in need of a missing diagram. Commands and prose explain that labels move, but neither the graph output nor a before/after commit graph is shown. A beginner must mentally reconstruct the relationship between `main`, `try-pysr`, and the same commit chain.
- `sections/03-content.prose.md`, `sections/04-conclusion.prose.md` — The rendered document strands “The checkpoint workflow” at the bottom of page 2 and “References” at the bottom of page 5, with their first content on the following page. “Git manuals” then appears as 4.3 under an unnumbered References heading, visually suggesting it belongs to the preceding course-application section.
- `sections/03-content.prose.md` — Inline formatting does not reliably preserve the leading blank in the expected ` M fitness.py` status. The generated HTML contains `<code>M fitness.py</code>`, and document page 3 presents the same ambiguous string. Since the lesson explicitly teaches two status columns, this loses meaningful visual information.

## Actionable
1. `sections/03-content.prose.md` § Merge only the reviewed result — Add a compact before/after graph using the same three commit nodes, baseline → guarded evaluator → experiment plan. Before integration, point `main` at the guarded evaluator and `try-pysr` at the plan; afterward, point both names at the plan. Label only the `main` movement with `merge --ff-only`, and caption that no new commit is created. Introduce the figure in the adjacent prose and place it in its own concise `##` unit if needed to preserve the current slide fit.
   (*why:* makes branch references and fast-forward movement visible in all three registers, especially projection.)
2. `sections/03-content.prose.md` § The checkpoint workflow; `sections/04-conclusion.prose.md` § Git manuals — Keep document section headings with their following subsection and first content; mark Git manuals unnumbered so it does not inherit section 4 numbering. Verify document pages 2, 5, and 6 after repagination.
   (*why:* repairs document hierarchy without lengthening projected content.)
3. `sections/03-content.prose.md` § Review a useful proposal — Show the expected status in a fenced text block that preserves its initial blank, and explain “blank staging column; M working-file column.” Verify that both PDF and HTML retain the two-character status field.
   (*why:* preserves a semantically significant space across document, presentation, and website.)
