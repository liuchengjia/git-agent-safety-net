"""Exercise acceptance, failure, staged recovery, reset, revert, and branching."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).with_name("create_demo.py")


def main():
    with tempfile.TemporaryDirectory(prefix="git-safety-verification-") as tmp:
        root = Path(tmp) / "lab"
        subprocess.run([sys.executable, str(SOURCE), str(root)], check=True)
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0")

        def run(*args, expected=0):
            p = subprocess.run(args, cwd=root, env=env, text=True, capture_output=True)
            if p.returncode != expected:
                raise AssertionError(f"{args}: {p.returncode}\n{p.stdout}\n{p.stderr}")
            return p.stdout

        def git(*args):
            return run("git", *args)

        def py(*args, **kwargs):
            return run(sys.executable, *args, **kwargs)

        git("init", "-b", "main")
        git("config", "user.name", "Tutorial verification")
        git("config", "user.email", "verification@example.invalid")
        git("config", "commit.gpgsign", "false")
        git("config", "core.autocrlf", "false")
        assert "3 baseline checks" in py("check.py")
        git("add", "fitness.py", "check.py", "propose.py", ".gitignore")
        git("commit", "-m", "Record tested MSE baseline")
        assert not git("status", "--porcelain")
        py("propose.py", "good")
        assert "5 contract checks" in py("check.py", "--contract")
        assert "raise ValueError" in git("diff", "--", "fitness.py")
        git("add", "fitness.py")
        git("commit", "-m", "Reject invalid fitness inputs")
        good = git("rev-parse", "HEAD").strip()
        py("propose.py", "bad")
        assert "FAIL: opposite errors" in py("check.py", "--contract", expected=1)
        git("restore", "--source=HEAD", "--worktree", "fitness.py")
        py("check.py", "--contract")
        assert not git("status", "--porcelain")
        # Plain restore copies a staged mistake: demonstrate the distinction.
        py("propose.py", "bad")
        git("add", "fitness.py")
        git("restore", "fitness.py")
        py("check.py", "--contract", expected=1)
        git("restore", "--staged", "fitness.py")
        git("restore", "--source=HEAD", "--worktree", "fitness.py")
        # Destructive reset is confined to this generated temporary repository.
        py("propose.py", "bad")
        git("add", "fitness.py")
        git("reset", "--hard", "HEAD")
        assert git("rev-parse", "HEAD").strip() == good
        py("check.py", "--contract")
        # Revert adds a commit and preserves the bad commit in history.
        py("propose.py", "bad")
        git("add", "fitness.py")
        git("commit", "-m", "Demonstrate a committed evaluator error")
        bad = git("rev-parse", "HEAD").strip()
        git("revert", "--no-edit", bad)
        assert bad in git("rev-list", "HEAD")
        py("check.py", "--contract")
        git("switch", "-c", "try-pysr")
        py("propose.py", "plan")
        git("add", "experiment.md")
        git("commit", "-m", "Plan isolated PySR baseline")
        git("switch", "main")
        assert not (root / "experiment.md").exists()
        assert "PySR" in git("diff", "main..try-pysr", "--", "experiment.md")
        git("switch", "try-pysr")
        py("check.py", "--contract")
        git("switch", "main")
        git("merge", "--ff-only", "try-pysr")
        assert (root / "experiment.md").is_file()
        assert not git("status", "--porcelain")
        py(str(SOURCE), str(root), expected=1)
        # Refuse a fast-forward merge after independent commits on both branches.
        git("switch", "-c", "divergent-experiment")
        (root / "experiment-note.txt").write_text("experiment\n")
        git("add", "experiment-note.txt")
        git("commit", "-m", "Independent experiment")
        git("switch", "main")
        (root / "main-note.txt").write_text("main\n")
        git("add", "main-note.txt")
        git("commit", "-m", "Independent main change")
        run("git", "merge", "--ff-only", "divergent-experiment", expected=128)
        print("PASS: baseline, good/bad edits, restore, staging, reset, revert, branch, merge, divergence, overwrite guard")


if __name__ == "__main__":
    main()
