#!/usr/bin/env python3
"""Utilities for capturing the current git commit hash."""
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional


def _repo_root(start: Optional[Path] = None) -> Path:
    """Return the git repo root or current directory if git is unavailable."""
    start = start or Path(__file__).resolve().parent
    try:
        output = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            stderr=subprocess.DEVNULL,
        )
        return Path(output.decode().strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return start


def get_git_hash(short: bool = True) -> str:
    """Return the current git commit hash.

    Parameters
    ----------
    short
        When True return the short hash, otherwise return the full hash.
    """
    args = ["git", "rev-parse", "--short" if short else "", "HEAD"]
    # Remove empty string produced when short is False
    args = [arg for arg in args if arg]
    try:
        output = subprocess.check_output(
            args,
            cwd=_repo_root(),
            stderr=subprocess.DEVNULL,
        )
        return output.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


if __name__ == "__main__":
    print(get_git_hash())
