# Clarity & Exposition — Round 1

**Recommendation:** minor polish
The worked sequence is clear, with two small gaps in reader orientation.

## Strengths
- The three-state diagram introduces staging before the reader needs it, and the later staged-versus-working transfer question tests exactly that distinction.
- The good and bad proposals give review an observable purpose: expected status output, check counts, and the signed-error cancellation example let a beginner interpret each result.
- Recovery instructions name their scope and explain why the explicit HEAD source matters. The branch exercise also clearly distinguishes a recorded PySR plan from an implemented result.
- The spines have a coherent order and their central intentions are realized in the prose; they do not accumulate deferred explanations.

## Weaknesses
- `sections/04-conclusion.prose.md` — “For C1” and “For C2/C4,” followed by “the evaluation-to-fitness spine,” assume course terminology that the shipped sections never introduce. The final transfer advice becomes less concrete precisely where it should connect the lesson to the reader's next work.
- `sections/03-content.prose.md` — The prose never announces the live exercise's overall sequence or clearly labels “Choose the right recovery scope” as supplementary reference. The distinction between the 15-minute live path and supplementary recovery commands exists in `topic.md`, but a novice following the shipped tutorial must infer which commands to execute in sequence.

## Actionable
1. `sections/04-conclusion.prose.md` § Apply the same loop to the course — Expand C1 and C2/C4 with their course activity names, and replace “evaluation-to-fitness spine” with a plain description of the evaluation workflow. (*why:* Readers can apply the closing advice without decoding internal course labels.)
2. `sections/03-content.prose.md` § Prepare a disposable lab — Add one short roadmap naming baseline, reviewed proposal, broken proposal and recovery, then branch and merge; label “Choose the right recovery scope” as reference commands rather than a step to execute. (*why:* Beginners can follow the live path and recognize the recovery alternatives without interrupting the lab sequence.)
