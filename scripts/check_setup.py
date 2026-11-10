"""Run from the repository root before class: python scripts/check_setup.py."""
import importlib.metadata
from pathlib import Path
import shutil
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from astropy.table import QTable
from course2026.analysis import usable_rows, weighted_mean

root = Path(__file__).resolve().parents[1]
for name in ("numpy", "scipy", "astropy", "matplotlib", "pytest", "nbclient", "jupyterlab"):
    print(f"{name}: {importlib.metadata.version(name)}")
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
if shutil.which("git") is None:
    raise SystemExit("Install Git before Session 2; ask the instructor for help")
catalogue = QTable.read(root / "data/mock_galaxies.ecsv")
assert usable_rows(catalogue).sum() == 395
assert np.isclose(weighted_mean([1, 3], [1, 3])[0], 1.2)
print("Setup OK: local data, imports, Git and known-answer calculation")
