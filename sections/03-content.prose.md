# The checkpoint workflow

## Prepare a disposable lab

Follow this path: baseline, useful proposal, broken proposal and recovery, then branch and merge. Use Git 2.28+ and Python 3.9+; substitute `python3` if needed. From this tutorial's repository root:

```sh
python examples/create_demo.py ../git-safety-demo
cd ../git-safety-demo
git init -b main
```

The helper refuses a nonempty destination. It creates the function, checks, and simulated edits. Commands work in PowerShell, Bash, or zsh; no model service or PySR is required.

## Git identity and terminal navigation

After initialization, configure your own local identity if it is not already set. Substitute your values:

```sh
git config user.name "Your Name"
git config user.email "you@example.com"
```

Git may display a long diff in a scrollable **pager**. Press Space to advance and `q` to return to the terminal. This is especially useful when reviewing the initial helper scripts.

## Establish a known-good baseline

```sh
python check.py
git add fitness.py check.py propose.py .gitignore
git diff --staged
git commit -m "Record tested MSE baseline"
git status --short
```

Expect `PASS: 3 baseline checks`, then no status output. Inputs are nonempty, equal-length lists of finite numbers. Clean status means recorded, not necessarily correct.

## Review a useful proposal

The simulated agent rejects empty or unequal-length inputs without changing MSE for valid inputs:

```sh
python propose.py good
git status --short
git diff -- fitness.py
python check.py --contract
```

Expected status (blank staging column; `M` working-file column):

```text
 M fitness.py
```

Expect `PASS: 5 contract checks`. Read the two added guards; the diff shows the edit, and tests check its intended behavior.

## Stage only the reviewed change

```sh
git add fitness.py
git diff --staged -- fitness.py
git commit -m "Reject invalid fitness inputs"
git log --oneline -2
```

Both commits appear, newest first. Your IDs will differ. If you edit after staging, rerun both diffs and stage the intended version again. To unstage without losing edits, use `git restore --staged fitness.py`.

## Detect a misleading improvement

```sh
python propose.py bad
git diff -- fitness.py
python check.py --contract
```

The diff replaces `(p - y) ** 2` with `(p - y)`. For predictions `[0, 2]` and observations `[1, 1]`, signed errors cancel to zero; MSE must be one. Expect `FAIL: opposite errors` and a nonzero exit code. Stop: do not stage this proposal.

## Discard the bad uncommitted edit

In this lab, the only uncommitted change is the intentional broken proposal. Inspect status and the diff first, then:

```sh
git restore --source=HEAD --worktree fitness.py
python check.py --contract
git status --short
```

Expect five passing checks and empty status. The explicit `HEAD` source restores the committed file. Plain `git restore fitness.py` copies from staging, which could already contain the mistake. [@gitrestore]

## Recovery reference: choose the scope

These are alternatives to consult, not the next steps to run.

- **Wrongly staged:** `git restore --staged fitness.py` keeps working edits.
- **Bad published commit:** `git revert COMMIT_ID` adds an inverse commit, preserving history. It can require conflict resolution. [@gitrevert]
- **Disposable uncommitted experiment:** `git reset --hard HEAD` resets tracked files and staging. It destroys uncommitted edits; inspect both diffs first. [@gitreset]

`reset --hard HEAD` does not undo the current commit. It is not a general untracked-file cleaner and may overwrite obstructing untracked paths.

## Isolate the next experiment

Start clean. We record a plan on `try-pysr`; installing PySR is a later task.

```sh
git switch -c try-pysr
python propose.py plan
git add experiment.md
git commit -m "Plan isolated PySR baseline"
git switch main
git diff main..try-pysr -- experiment.md
```

`experiment.md` exists on the experiment branch and is absent on `main`. Switching changes this working directory's tracked files.

## Merge only the reviewed result

```sh
git switch try-pysr
python check.py --contract
git switch main
git merge --ff-only try-pysr
git log --oneline --graph --all
```

Here `main` has not advanced, so the merge moves its label forward. If it has diverged, `--ff-only` stops; review the histories rather than forcing. Only a plan is merged, not a tested PySR implementation.

## See what the fast-forward changed

The same three commits exist before and after integration:

```text
Before: A --- B --- C
             main  try-pysr

After:  A --- B --- C
                   main, try-pysr
```

A is the baseline; B adds input guards; C adds the experiment plan. `git merge --ff-only try-pysr` moves only `main` from B to C. It creates no new commit.

## Keep outputs out; share reviewed commits

The lab's `.gitignore` excludes `.env`, Python caches, `data/`, and `runs/`. Keep source, checks, and a data manifest in Git; store large datasets elsewhere.

To share, create an empty remote you own. Substitute its actual URL for `REMOTE_URL`:

```sh
git remote add origin REMOTE_URL
git push -u origin main
```

This optional step needs network and authentication. In a team repository, push a feature branch for review before merging. A local commit has not yet been uploaded.
