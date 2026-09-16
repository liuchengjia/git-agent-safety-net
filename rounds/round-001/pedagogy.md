# Pedagogical Readiness — Round 1

**Recommendation:** minor polish
The complete offline workflow is ready for instruction, with one small terminal-navigation gap in the novice follow-along path.

**Audience read against:** Students who can edit and run a small Python program and navigate a terminal, but need reliable habits for saving, reviewing, accepting, and undoing an agent's changes to an evaluator.

## Strengths
- The declared audience, proposal, concept spines, and finished prose agree. The lesson delivers a tested baseline, both diff comparisons, acceptance and rejection, recovery choices, branch review, and optional sharing without claiming to implement PySR.
- The signed-error example gives students a concrete reason to inspect evaluator changes: the numerical counterexample explains why a lower score can be wrong, and the unchanged checks make that failure observable.
- The disposable lab supplies the actual files and deterministic edits required to follow along. Commands are ordered, expected test and status results are provided, and the presenter guide honestly distinguishes a 15-minute demonstration from slower first-time typing.
- Explicit HEAD-based restoration, the staged-versus-working transfer question, and the explanation that branches do not isolate processes address mistakes this audience is likely to make. Recovery and sharing limitations are stated at the point where they matter.

## Weaknesses
- `sections/03-content.prose.md` — The first `git diff --staged` displays all four newly staged files, including the substantial helper and check scripts. On a normal interactive Git installation this can open a pager, but the lesson never explains scrolling or pressing `q` to return to the prompt. A student who knows ordinary terminal commands but is new to Git can get stuck before the first commit, despite executing the supplied instructions correctly.

## Actionable
1. `sections/03-content.prose.md` § Establish a known-good baseline — Before the first diff, add a short note that Git may open a scrollable pager, Space advances, and `q` returns to the terminal; alternatively use `git --no-pager diff --staged` consistently for the demonstration. (*why:* removes the remaining small follow-along obstacle and moves minor polish to ready as-is.)
