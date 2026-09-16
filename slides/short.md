## A lower score can be wrong

Predictions: `[0, 2]` · Observations: `[1, 1]`

```text
Squared errors:  (1 + 1) / 2 = 1   correct MSE
Signed errors:  (-1 + 1) / 2 = 0   broken evaluator
```

An agent can improve the number by breaking the measurement.

**Save a working checkpoint before the agent edits.**

## Three states, two diffs

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \definecolor{workingblue}{HTML}{24658A}
  \definecolor{stagingorange}{HTML}{A65B12}
  \definecolor{commitgreen}{HTML}{287363}
  \node[draw=workingblue,fill=workingblue!5,line width=1pt,
    minimum width=3.6cm,minimum height=1.85cm,align=center] (work) at (0,0)
    {\textcolor{workingblue}{\textbf{1. Working files}}\\[7pt]
     \small What you edit\\\small and run};
  \node[draw=stagingorange,fill=stagingorange!5,line width=1pt,
    minimum width=3.6cm,minimum height=1.85cm,align=center] (stage) at (4.9,0)
    {\textcolor{stagingorange}{\textbf{2. Staging area}}\\[7pt]
     \small Selected content\\\small for the next commit};
  \node[draw=commitgreen,fill=commitgreen!5,line width=1pt,
    minimum width=3.6cm,minimum height=1.85cm,align=center] (head) at (9.8,0)
    {\textcolor{commitgreen}{\textbf{3. Commit (HEAD)}}\\[7pt]
     \small Your recorded\\\small checkpoint};
  \draw[->,thick] (work.east) -- (stage.west);
  \node[font=\footnotesize,align=center] at (2.45,1.25) {\texttt{git add}};
  \draw[->,thick] (stage.east) -- (head.west);
  \node[font=\footnotesize,align=center] at (7.35,1.25) {\texttt{git commit}};
  \draw[workingblue,thick,<->] (0,-1.35) -- (4.75,-1.35);
  \draw[stagingorange,thick,<->] (5.05,-1.35) -- (9.8,-1.35);
  \node[align=center,anchor=north] at (2.4,-1.5)
    {\texttt{git diff}\\[3pt]\small Working files vs staging};
  \node[align=center,anchor=north] at (7.4,-1.5)
    {\texttt{git diff --staged}\\[3pt]\small Staging vs HEAD};
\end{tikzpicture}
\end{center}
\vspace{0.15cm}
\textbf{Remember:} \texttt{git add} snapshots the file now.\\
Later edits stay in working files until you stage them again.
```

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
