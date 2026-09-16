# Topic

## In one sentence
Use Git checkpoints, diffs, and branches to make an agent's edits reviewable and recoverable.

## What it is
Git records snapshots of selected project files and connects them into a history. A staging area selects the next snapshot; branches name lines of development. This tutorial uses a small symbolic-regression fitness function to make those operations observable.

## Why it belongs in this course
An agent can change an evaluation function faster than a human can inspect it. A lower reported error can mean a broken evaluator rather than a better model. A committed baseline, fixed tests, and a reviewed diff let the developer distinguish improvement from invalid evaluation and recover the code.

## What the reader will be able to do
- Initialize a disposable demo repository and commit a tested baseline.
- Distinguish unstaged and staged changes and review both.
- Accept a validated change and discard a broken uncommitted edit.
- Select restore, revert, or reset according to what must be undone.
- Create an experimental branch, review its diff, and fast-forward it after validation.
- Explain what a commit does not protect and prepare reviewed commits for pushing.

## Scope
**In scope:** Git 2.28+, Python 3.9+, snapshots, staging, diffs, recovery, branches, ignore rules, and a remote workflow.

**Out of scope:** installing or running PySR, symbolic-regression search, rebasing, history surgery, merge-conflict resolution, and GitHub account setup. They exceed the ten-minute live slot. `try-pysr` is a named experiment plan; no PySR result is claimed.

## Shape
Four paired sections follow WHAT / WHY / HOW / WHAT ELSE in the full handout and website. The nine-page short deck uses seven minutes for the concepts and three minutes for a prepared break/detect/recover demonstration. Setup, the good-proposal commit, branch execution, remote commands, and references remain available for self-paced reading. An offline Python helper applies deterministic simulated agent edits so the lesson needs no model service. The timed-deck exception is documented in CLAUDE.md.

## Open questions
- None blocking local delivery. A class-specific dataset and a real PySR baseline can replace the tiny fixture in a later lesson.
