# Why an agent needs a checkpoint

## A better score can hide a broken evaluator

Our example scores predictions against observations using mean squared error (MSE). Lower is better. An agent replacing squared errors with signed errors can make mistakes cancel: the score improves while the evaluator becomes wrong.

**Commit before the agent edits. Inspect the diff and run fixed checks before accepting the result.** Record the code commit, data version, environment, and seed in an experiment log; a commit alone does not reproduce a run.

## What Git cannot undo

A commit protects recorded files. It cannot reverse sent messages, API charges, database writes, or changes outside the repository. A branch separates history; it is not a security sandbox or a second working directory.

Keep credentials and generated data out of commits. `.gitignore` affects untracked files; it does not erase an already tracked secret. Rotate exposed credentials and follow the host's removal procedure. [@gitignore]
