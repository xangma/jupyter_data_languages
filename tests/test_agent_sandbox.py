"""Protect student work when the classroom setup command is repeated."""
from pathlib import Path
import os
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/create_agent_practice.py"


def run_setup(destination, **kwargs):
    return subprocess.run([sys.executable, str(SCRIPT), str(destination)],
                          capture_output=True, text=True, **kwargs)


def test_fresh_sandbox_preserves_course_starter(tmp_path):
    target = tmp_path / "nested" / "agent-practice"
    result = run_setup(target)
    assert result.returncode == 0, result.stderr
    for name in ("weighted_mean.py", "test_weighted_mean.py"):
        assert (target / name).read_bytes() == (ROOT / "exercises" / name).read_bytes()
    assert "__pycache__/" in (target / ".gitignore").read_text()
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=target, text=True).strip()
    assert Path(git("rev-parse", "--show-toplevel")) == target
    assert git("branch", "--show-current") == "agent-repair"
    assert git("status", "--short") == ""
    assert git("remote") == ""
    assert git("show", "main:weighted_mean.py") == (ROOT / "exercises/weighted_mean.py").read_text().strip()
    (target / "weighted_mean.py").write_text("# Student's reviewed correction\n")
    (target / "my-notes.txt").write_text("Keep this work\n")
    def snapshot():
        return {str(p.relative_to(target)): p.read_bytes()
                for p in target.rglob("*") if p.is_file()}
    before = snapshot()
    result = run_setup(target)
    assert result.returncode != 0
    assert "Nothing was overwritten" in result.stderr
    assert snapshot() == before


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


def test_missing_git_leaves_no_partial_workspace(tmp_path):
    target = tmp_path / "agent-practice"
    result = run_setup(target, env={**os.environ, "PATH": ""})
    assert result.returncode != 0
    assert "Git is required" in result.stderr
    assert not target.exists()
