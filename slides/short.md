## A lower score can be wrong

Predictions: `[0, 2]` · Observations: `[1, 1]`

```text
Squared errors:  (1 + 1) / 2 = 1   correct MSE
Signed errors:  (-1 + 1) / 2 = 0   broken evaluator
```

An agent can improve the number by breaking the measurement.

**Save a working checkpoint before the agent edits.**

## Three states, two diffs

```text
Working files --git add--> Staging --git commit--> HEAD

       git diff                  git diff --staged
   working vs staging             staging vs HEAD
```

`git add` snapshots the file now; later edits are not staged.

A commit records selected files. A branch names a commit.

## Accept only a reviewed change

Before the run: test, commit, and confirm a clean status.

After the agent edits:

```sh
git diff -- fitness.py
python check.py --contract
git add fitness.py
git diff --staged
git commit -m "Reject invalid inputs"
```

The diff explains the edit. Fixed tests check its behavior.

## Match recovery to the mistake

- **Uncommitted file:** restore the recorded version.
  `git restore --source=HEAD --worktree fitness.py`
- **Staged by mistake:** keep the working edit, unstage it.
  `git restore --staged fitness.py`
- **Already shared:** add an inverse commit.
  `git revert COMMIT_ID`

`git reset --hard HEAD` destroys uncommitted tracked edits.
Use it only for a deliberately disposable experiment.

## Branches keep experiments separate

```text
Before: A --- B --- C
             main  try-pysr
After:  A --- B --- C
                   main, try-pysr
```

Create: `git switch -c try-pysr`

After reviewing and testing, on main:
`git merge --ff-only try-pysr`

Only a label moves in this fast-forward; no new commit is created.

## Know the boundary

Git protects **recorded files**, not API charges, database writes,
or messages an agent has already sent.

A branch is history separation, not a security sandbox.

Ignore credentials and generated data. Record the data version,
environment, and seed alongside the code commit.

## The habit to keep

**Checkpoint → inspect the diff → test → accept or recover**

For an evaluator, a better score is evidence only if the measurement
still means the same thing.

Next, a three-minute demonstration: break the MSE function,
catch the failure, and restore the checkpoint.

## Live demo: break, detect, recover

Start in the prepared demo directory with a clean, tested checkpoint.

```sh
python propose.py bad
git --no-pager diff -- fitness.py
python check.py --contract
git restore --source=HEAD --worktree fitness.py
python check.py --contract
git status --short
```

Expect **FAIL → PASS → clean status**. The original commit survives.
