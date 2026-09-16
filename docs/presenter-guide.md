# Presenter guide: 7 minutes + 3 minutes

For the complete two-speaker English script with Chinese cues, see [speaker-script.md](speaker-script.md).

The public `slides.pdf` contains 9 pages: a title, seven teaching slides, and one live-demo command card. No section-divider or bibliography slides interrupt the talk. Full explanations and references remain in the handout and website.

## Seven-minute talk

| Page | Time | Focus |
| --- | --- | --- |
| 1 | 0:00-0:20 | Introduce Git as the safety net for agent edits. |
| 2 | 0:20-1:15 | Show how signed errors cancel and falsely improve the score. |
| 3 | 1:15-2:25 | Explain working files, staging, HEAD, and the two diffs. |
| 4 | 2:25-3:30 | Describe the acceptance loop; do not type commands yet. |
| 5 | 3:30-4:35 | Select restore, unstage, or revert; name reset's destructive scope. |
| 6 | 4:35-5:30 | Trace main moving in a fast-forward. |
| 7 | 5:30-6:15 | State what Git does not protect; note reproducibility inputs. |
| 8 | 6:15-7:00 | Summarize the habit and introduce the live demonstration. |

## Prepare before the clock starts

From the tutorial repository root, choose an unused sibling folder. Git 2.28+ and Python 3.9+ are required; use `python3` in place of `python` where needed.

```sh
python examples/create_demo.py ../git-safety-demo-live
cd ../git-safety-demo-live
git init -b main
```

Configure your own local `user.name` and `user.email` if needed, then:

```sh
python check.py
git add fitness.py check.py propose.py .gitignore
git commit -m "Record tested MSE baseline"
python propose.py good
python check.py --contract
git add fitness.py
git commit -m "Reject invalid fitness inputs"
git status --short
```

The final output is empty; the checks have printed `PASS: 5 contract checks`.
Leave this terminal open beside slide 9. Do not spend the three-minute demo installing software, creating the repository, or logging into GitHub.

## Three-minute live demonstration

| Time | Command/action | What to say |
| --- | --- | --- |
| 7:00-7:30 | `python propose.py bad` | This deterministic helper simulates an agent edit. |
| 7:30-8:10 | `git --no-pager diff -- fitness.py` | Point to removal of `** 2`: the metric's meaning changed. |
| 8:10-8:45 | `python check.py --contract` | Expected failure: opposite errors gave zero, but MSE must be one. |
| 8:45-9:20 | `git restore --source=HEAD --worktree fitness.py` | Recover only the broken working file from our checkpoint. |
| 9:20-9:45 | `python check.py --contract` | Five checks pass again. |
| 9:45-10:00 | `git status --short` | Empty output confirms the working tree is clean. Close with the habit. |

This is a presenter demonstration, not simultaneous audience typing. If the terminal fails, explain the expected FAIL → PASS → clean sequence on the command card and finish on time.

## Rehearsal and boundaries

Run `python examples/verify_demo.py` from the tutorial root before class. It checks the full acceptance/recovery/branch exercise in a temporary directory.

The toy fitness contract is nonempty, equal-length lists of finite numbers. Its five checks are teaching fixtures, not production numerical validation. No PySR installation or result is claimed. Recovery extensions, remote commands, and official references remain in the full handout.
