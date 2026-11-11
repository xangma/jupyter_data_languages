"""Protect student work when the classroom setup command is repeated."""
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/create_agent_practice.py"


def run_setup(destination):
    return subprocess.run([sys.executable, str(SCRIPT), str(destination)],
                          capture_output=True, text=True)


def test_fresh_sandbox_preserves_course_starter(tmp_path):
    target = tmp_path / "nested" / "agent-practice"
    result = run_setup(target)
    assert result.returncode == 0, result.stderr
    for name in ("weighted_mean.py", "test_weighted_mean.py"):
        assert (target / name).read_bytes() == (ROOT / "exercises" / name).read_bytes()
    assert "__pycache__/" in (target / ".gitignore").read_text()
    (target / "weighted_mean.py").write_text("# Student's reviewed correction\n")
    (target / "my-notes.txt").write_text("Keep this work\n")
    before = {p.name: p.read_bytes() for p in target.iterdir()}
    result = run_setup(target)
    assert result.returncode != 0
    assert "Nothing was overwritten" in result.stderr
    assert {p.name: p.read_bytes() for p in target.iterdir()} == before


@pytest.mark.parametrize("kind", ["file", "directory"])
def test_refuses_an_existing_destination(tmp_path, kind):
    target = tmp_path / "already-used"
    if kind == "file":
        target.write_text("Keep this file\n")
    else:
        target.mkdir()
    assert run_setup(target).returncode != 0
    if kind == "file":
        assert target.read_text() == "Keep this file\n"
    else:
        assert list(target.iterdir()) == []
