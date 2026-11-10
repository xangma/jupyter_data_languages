"""Create an independent local Git exercise without changing the course clone."""
import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
target = args.destination.resolve()
if target.exists():
    parser.error("Destination already exists; choose a fresh directory")
target.mkdir(parents=True)
(target / "angle.py").write_text('''def angle_distance(a, b):
    """Smallest separation of two bearings in degrees."""
    difference = abs((b % 360) - (a % 360))
    return min(difference, 360 - difference)
''')
(target / "test_angle.py").write_text('''from angle import angle_distance


def test_small_angles():
    assert angle_distance(10, 90) == 80
''')
(target / "README.md").write_text("# Bearing separation practical\n\nAngles are inputs to a small helper.\n")
(target / ".gitignore").write_text("__pycache__/\n.pytest_cache/\n.venv/\n")
subprocess.run(["git", "init", "-b", "main", str(target)], check=True)
print(f"Created {target}\nNo commits, remotes or identity settings were added. Follow Session 2.")
