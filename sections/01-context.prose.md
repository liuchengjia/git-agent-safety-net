# What Git records

## Snapshots you can return to

Git is a local version-control system. A **commit** records a snapshot of selected files, a message, and links to its parent commit(s). Its ID identifies that state; **HEAD** normally names the current branch tip.

A **branch** is a movable name for a commit. GitHub hosts a remote copy; you can commit and recover locally without GitHub or a network. [@progit]

## The three states

```text
Working files --git add--> Staging area
Staging area --git commit--> Commit (HEAD)

git diff         : working files vs staging
git diff --staged: staging vs HEAD
```

`git add` copies the file's current content into staging. Later edits are not staged automatically. `git status --short` uses two columns: staging first, working files second. `??` means untracked.
