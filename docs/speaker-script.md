# Speaker script — 7-minute talk + 3-minute live demo

英文正文可直接讲；中文括号是操作提示，不朗读。时间是排练目标，包含翻页、指图和停顿，并非语速保证。建议分工：A（Chengjia）讲第 1–4 页，B（Yiyang）讲第 5–8 页；演示时 B 操作、A 讲解。名字和角色可互换。前 7 分钟约 760 个英文词，请计时排练一次。

## Slide 1 · Title · A · 0:00–0:20

Hi everyone. We’re Chengjia and Yiyang. Today, we’ll show how Git helps us work safely with coding agents. Our goal is simple: save a working version, inspect an agent’s changes, and recover when those changes are wrong.

（停一下，翻页。）

## Slide 2 · A lower score can be wrong · A · 0:20–1:15

Let’s start with a small evaluation function. Our predictions are zero and two, and our observations are one and one. The errors are minus one and plus one.

For mean squared error, we square those errors first. Both become one, so the average is one.

Now imagine an agent removes the square. The two signed errors cancel, and the score becomes zero. That looks better, but the predictions have not improved. The evaluator is broken.

This is why a lower number is not enough. We need to check what changed, and save a working checkpoint before the agent starts.

（指上、下两行计算，让观众看清“1 变成 0”的原因。）

## Slide 3 · Three states, two diffs · A · 1:15–2:25

To do that, we need three Git states.

First, the working files: the code we are editing. Second, the staging area: the version of each file selected for the next commit. Third, HEAD: the current commit, our recorded checkpoint.

Git add copies the current file content into staging. It does not permanently connect the file to staging. If we edit again afterward, that later edit is not staged automatically.

That explains the two diff commands. Git diff compares working files with staging. Git diff staged compares staging with HEAD: it shows what the next commit will contain.

A commit records a snapshot. A branch gives a name to a commit. Keeping those ideas separate helps us avoid committing changes we have not actually reviewed.

（沿图从左指向右，再分别指两个 diff；不现场输入命令。）

## Slide 4 · Accept only a reviewed change · A · 2:25–3:30

Here is the workflow we want to repeat.

Before an agent edits anything, run the tests, commit the working version, and confirm that the working tree is clean. That gives us a known starting point.

After the edit, first inspect the diff. Then run fixed checks against the behavior we expect. In this example, those checks protect the meaning of mean squared error.

If the change is acceptable, stage the specific file, inspect the staged diff, and commit it with a clear message.

The diff and the tests answer different questions: what changed, and does it behave correctly? Passing tests is useful evidence, but we still need to review the change. Yiyang will now explain what to do when we reject it.

（在 3:30 左右交接；B 接着翻到第 5 页。）

## Slide 5 · Match recovery to the mistake · B · 3:30–4:35

Thanks. The recovery command depends on where the mistake is.

If the file has uncommitted changes we want to discard, restore its recorded version from HEAD. This replaces the working file, so we should check that we do not need those edits.

If we only staged something by mistake, use restore staged. That removes it from the next commit while keeping our working edits.

If the bad commit has already been shared, use revert. It creates a new commit that reverses the earlier change, preserving the shared history.

Finally, reset hard can destroy uncommitted tracked changes. It is not our default recovery tool. For today’s demo, we will restore just one broken file from a known checkpoint.

（按三种情况依次指命令，不逐字读长命令。）

## Slide 6 · Branches keep experiments separate · B · 4:35–5:30

A branch lets us keep an experiment separate from main.

In this diagram, main points to commit B. Our experiment branch, called try-pysr, has moved ahead to commit C. The name is only an example; we do not install or run PySR today.

After reviewing and testing the experiment, we switch back to main and use merge with fast-forward only.

Because main has not diverged, Git can simply move its label from B to C. It creates no new commit in this case. If the branches have diverged, this command refuses, giving us a chance to inspect the situation.

（指 Before 的 main，再指 After 的两个分支名。）

## Slide 7 · Know the boundary · B · 5:30–6:15

Git also has limits. It helps us recover recorded files. It cannot undo an API charge, a database write, or a message an agent has already sent.

A branch separates history; it is not a security sandbox.

And a code commit alone does not guarantee reproducibility. We should also record the data version, environment, and random seed. Credentials should stay out of the repository. These practices make our checkpoint more useful, without pretending that Git can reverse every action.

## Slide 8 · The habit to keep · B · 6:15–7:00

The habit we want you to remember is: checkpoint, inspect the diff, test, then accept or recover.

For an evaluation function, a better score is meaningful only if the measurement still means the same thing.

Now we’ll demonstrate that in three minutes. We already have a clean, tested checkpoint. We’ll simulate a bad agent edit, catch it with a fixed test, and restore the original file. Watch for three results: a failed check, passing checks after recovery, and finally a clean working tree.

（切到第 9 页和提前准备好的终端。若超时，直接用最后三句进入演示。）

## Slide 9 · Live demo · A narrates, B types · 7:00–10:00

必须提前按 [presenter-guide.md](presenter-guide.md) 完成准备；下面命令在准备好的演示目录执行，不是在教程仓库执行。B 等 A 解释完当前输出再输入下一条。

### 7:00–7:30 · Introduce the edit

B:
```sh
python propose.py bad
```

A: “This helper makes a deterministic edit that simulates a coding agent. We use it so the demonstration is repeatable. It has now changed our evaluation function.”

### 7:30–8:10 · Inspect the change

B:
```sh
git --no-pager diff -- fitness.py
```

A: “Look at the removed and added lines. The square has disappeared. We are averaging signed errors instead of squared errors. This small edit changes what the score means.”

（B 用光标指删除的 `** 2`，留几秒看输出。）

### 8:10–8:45 · Detect the failure

B:
```sh
python check.py --contract
```

A: “This failure is expected. For our example, mean squared error should be one. The modified function gives zero because opposite errors cancel. Our fixed check catches the broken measurement.”

（失败是演示成功的一部分，不尝试修改测试。）

### 8:45–9:20 · Recover the file

B:
```sh
git restore --source=HEAD --worktree fitness.py
```

A: “We reject this edit. This command replaces only the working copy of fitness.py with its version from HEAD. We deliberately discard the broken edit; the saved commit remains unchanged.”

### 9:20–9:45 · Verify recovery

B:
```sh
python check.py --contract
```

A: “All five checks pass again. We have verified the restored behavior, rather than assuming recovery worked.”

### 9:45–10:00 · Close

B:
```sh
git status --short
```

A: “No output means the working tree is clean. Checkpoint, inspect, test, then accept or recover. That is our Git safety net. Thank you.”

## Fallback if the terminal fails

不要临时安装依赖或登录账号。切回第 9 页，A 说：

“The expected sequence is visible here: the bad edit fails the check; restoring the saved file makes all five checks pass; and status becomes clean. The key is to save the checkpoint before the agent edits, then verify both the change and the recovery.”

随后用上面的收尾句结束。若已经临近 10 分钟，跳过这段解释，直接收尾。
