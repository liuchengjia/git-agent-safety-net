# Round 1 — Synthesis

**Panel recommendation:** minor polish
**Seats:** clarity minor polish · pedagogy minor polish · visual minor polish

## Since last round
First round — no prior docket.

## Consensus
All three seats consider the worked workflow usable and identify polish rather than a correctness or readiness blocker. No actionable defect was independently duplicated across seats; agreement on the overall tier must not be presented as agreement on each finding.

## Conflicts
- none

## Docket
1. **Explain how to exit Git's pager** — `sections/03-content.prose.md` § Establish a known-good baseline
   *Raised by:* pedagogy · *Effort:* small
   Before the first diff, state that Space advances and q returns to the terminal, or use --no-pager consistently.
2. **Preserve the two status columns** — `sections/03-content.prose.md` § Review a useful proposal
   *Raised by:* visual · *Effort:* small
   Use a fenced text block for the leading blank in ` M fitness.py`; explain the blank staging column and M working-file column. Check PDF and HTML output.
3. **Keep document headings with their content** — `sections/03-content.prose.md` § The checkpoint workflow; `sections/04-conclusion.prose.md` § Git manuals
   *Raised by:* visual · *Effort:* small
   Prevent stranded section headings at page bottoms and mark Git manuals unnumbered. Inspect the document after repagination.
4. **Show the branch labels moving** — `sections/03-content.prose.md` § Merge only the reviewed result
   *Raised by:* visual · *Effort:* medium
   Add a compact before/after graph of baseline, guarded evaluator, and plan. main points at the guarded evaluator before the fast-forward and joins try-pysr at the plan afterward; no new commit is created. Use a separate concise heading if needed for slide fit.
5. **Signpost the live path and recovery reference** — `sections/03-content.prose.md` § Prepare a disposable lab
   *Raised by:* clarity · *Effort:* small
   Name baseline, useful proposal, broken proposal and recovery, and branch/merge in a short roadmap. Label the recovery-scope unit as alternative reference commands rather than the next sequential step.
6. **Expand course-specific labels** — `sections/04-conclusion.prose.md` § Apply the same loop to the course
   *Raised by:* clarity · *Effort:* small
   Expand C1 and C2/C4 with their activities and replace evaluation-to-fitness spine with a plain description of evaluator provenance.

## Deferred
- none

## Do next
1. Remove the pager obstacle.
2. Preserve the status field's leading blank.
3. Fix the document's heading attachment and reference numbering.

## Panel health
- Every persona filed independently. The visual seat could inspect actual rendered pages, so it explicitly separates rendered evidence from source estimates.
- The build gate used the existing just recipes with the supported engine override `engine=tectonic`; all three outputs built successfully. Fontconfig discovery warnings remained, but no overfull boxes were reported in the corrected build.
- This docket records the reviewed snapshot. Any subsequent revisions belong outside this round; do not rewrite the reports or this synthesis to imply the revisions were re-reviewed.
