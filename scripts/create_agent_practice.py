"""Prepare the agent practical, including its local Git checkpoints."""
import argparse
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
target = args.destination.resolve()
if target.exists():
    parser.error("Destination already exists; choose a fresh directory. Nothing was overwritten.")
if shutil.which("git") is None:
    parser.error("Git is required. Install it using the course setup before preparing this workspace.")
try:
    target.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    parser.error("Destination already exists; choose a fresh directory. Nothing was overwritten.")

root = Path(__file__).resolve().parents[1]
for name in ("weighted_mean.py", "test_weighted_mean.py"):
    shutil.copy2(root / "exercises" / name, target / name)
(target / ".gitignore").write_text("__pycache__/\n.pytest_cache/\n.venv/\n")
(target / "TASK.md").write_text("""# Weighted-mean agent practical

The intentionally wrong `weighted_mean(values, errors)` must return one scalar
inverse-variance weighted mean. Inputs are matching, nonempty, finite 1-D arrays
of repeated measurements and independent one-sigma errors; errors must be positive.
Reject invalid inputs with ValueError. The reference course helper has a different
return interface: do not substitute its (mean, uncertainty) tuple here.

First inspect and propose a plan without edits. Then draft only student checks
from the student's independently calculated expectations. After those checks
are reviewed and checkpointed, repair only weighted_mean.py. Keep both test files
fixed during the repair. Use the existing Python environment; no installations,
downloads or remote pushes. Ask the student before changing phase or scope.

This is a practice workspace, not an enforced security sandbox. Use the agent's
configured permissions/sandbox or the instructor's prepared environment.
""")
subprocess.run(["git", "init", "-b", "main", str(target)], check=True, capture_output=True)
# A synthetic identity is local to this disposable exercise, never global.
for key, value in (("user.name", "PhD practical"),
                   ("user.email", "classroom@example.invalid"),
                   ("commit.gpgsign", "false")):
    subprocess.run(["git", "config", "--local", key, value], cwd=target, check=True)
subprocess.run(["git", "add", "--", "weighted_mean.py", "test_weighted_mean.py",
                "TASK.md", ".gitignore"], cwd=target, check=True)
subprocess.run(["git", "commit", "-m", "Record intentionally failing course starter"],
               cwd=target, check=True, capture_output=True)
subprocess.run(["git", "switch", "-c", "agent-repair"], cwd=target,
               check=True, capture_output=True)
print(f"Prepared {target}\nBranch: agent-repair; starter committed; no remotes.\n"
      "Open this directory in your agent. The course originals are unchanged.\n"
      "This practice directory is not an enforced security sandbox.")
