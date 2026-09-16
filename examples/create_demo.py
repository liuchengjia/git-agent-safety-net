"""Create an offline, disposable Git teaching lab; never overwrite existing work."""
import argparse
from pathlib import Path
import textwrap

BASELINE = '''\
"""Mean squared error for a tiny symbolic-regression evaluation."""


def fitness(predicted, observed):
    return sum((p - y) ** 2 for p, y in zip(predicted, observed)) / len(observed)
'''

CHECKS = '''\
"""Fixed checks: simulated proposals never change this file."""
import argparse
import math
import sys
sys.dont_write_bytecode = True
from fitness import fitness

parser = argparse.ArgumentParser()
parser.add_argument("--contract", action="store_true")
args = parser.parse_args()
cases = [
    ("perfect fit", [1, 2], [1, 2], 0.0),
    ("opposite errors", [0, 2], [1, 1], 1.0),
    ("mean not sum", [0, 0], [2, 4], 10.0),
]
failed = []
for name, predicted, observed, expected in cases:
    actual = fitness(predicted, observed)
    if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12):
        failed.append(name)
        print(f"FAIL: {name}: expected {expected}, got {actual}")
if args.contract:
    for name, predicted, observed in [
        ("empty inputs", [], []),
        ("unequal lengths", [1], [1, 2]),
    ]:
        try:
            fitness(predicted, observed)
        except ValueError:
            pass
        except Exception as exc:
            failed.append(name)
            print(f"FAIL: {name}: expected ValueError, got {type(exc).__name__}")
        else:
            failed.append(name)
            print(f"FAIL: {name}: expected ValueError")
if failed:
    raise SystemExit(1)
print("PASS: 5 contract checks" if args.contract else "PASS: 3 baseline checks")
'''

PROPOSE = '''\
"""Deterministic stand-in for an agent edit, limited to this generated lab."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("proposal", choices=["good", "bad", "plan"])
args = parser.parse_args()
root = Path(__file__).resolve().parent
path = root / "fitness.py"
if args.proposal == "plan":
    target = root / "experiment.md"
    with target.open("x", encoding="utf-8") as stream:
        stream.write("# PySR experiment plan\\n\\n"
                     "- Fix the dataset, train/test split, and random seed.\\n"
                     "- Preserve the MSE evaluator and input checks.\\n"
                     "- Record PySR and Python versions with each result.\\n"
                     "- Compare held-out error before proposing a merge.\\n\\n"
                     "No PySR implementation or result is included yet.\\n")
else:
    text = path.read_text(encoding="utf-8")
    signature = "def fitness(predicted, observed):\\n"
    if args.proposal == "good":
        if "raise ValueError" in text or signature not in text:
            raise SystemExit("Expected the unchanged baseline; refusing this edit.")
        guards = ('    if len(predicted) != len(observed):\\n'
                  '        raise ValueError("inputs must have equal lengths")\\n'
                  '    if not observed:\\n'
                  '        raise ValueError("inputs must not be empty")\\n')
        text = text.replace(signature, signature + guards, 1)
    else:
        if "(p - y) ** 2" not in text:
            raise SystemExit("Expected squared errors; refusing this edit.")
        text = text.replace("(p - y) ** 2", "(p - y)", 1)
    path.write_text(text, encoding="utf-8")
print(f"Applied simulated proposal: {args.proposal}")
'''


def create(destination):
    destination = Path(destination).resolve()
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise SystemExit(f"Refusing nonempty destination: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    files = {
        "fitness.py": BASELINE,
        "check.py": CHECKS,
        "propose.py": PROPOSE,
        ".gitignore": "__pycache__/\n*.pyc\n.env\ndata/\nruns/\n",
    }
    for name, source in files.items():
        with (destination / name).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(textwrap.dedent(source))
    print(f"Created lab: {destination}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    create(parser.parse_args().destination)
