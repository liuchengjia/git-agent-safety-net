# Carry the habit into agentic work

## Predict before you run

You stage a correct edit, then the agent breaks the same file again. `git diff --staged` looks correct. Is the working file ready to commit and run?

**No.** The commit would contain the staged version, while execution uses the later working file. Inspect `git diff`, restore or fix the working edit, and rerun checks before accepting it.

You can now create a checkpoint, review both diffs, accept or discard a proposal, and keep an experiment on its own branch.

## Apply the same loop to the course

For C1 (agentic coding and a reproducible repository), preserve a runnable baseline. For the C2/C4 capstone's generate-evaluate-select loop, start each agent run from a recorded state and finish with a reviewed diff and evaluation. Tie every fitness result to the commit that defines its evaluator.

Next: implement a real PySR baseline on `try-pysr`, with a fixed dataset and a held-out check. Commit only after its behavior earns acceptance. Revisit the Git manuals below when recovery scope is unclear.

# References {.unnumbered}

## Git manuals {.unnumbered .allowframebreaks}

::: {#refs}
:::
