"""Copy the intentionally failing exercise into a fresh student sandbox."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
target = args.destination.resolve()
try:
    target.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    parser.error("Destination already exists; choose a fresh directory. Nothing was overwritten.")

root = Path(__file__).resolve().parents[1]
for name in ("weighted_mean.py", "test_weighted_mean.py"):
    shutil.copy2(root / "exercises" / name, target / name)
(target / ".gitignore").write_text("__pycache__/\n.pytest_cache/\n.venv/\n")
print(f"Created {target}\nThe course originals are unchanged. Follow Session 3 to initialise Git.")
