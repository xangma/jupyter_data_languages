# Before the first session

Allow 20–30 minutes for installation. You need Python 3.11 or later and Git;
the locked course environment uses Python 3.13. A working notebook and a terminal
are enough. VS Code is optional.

Obtain the **2026 course checkout supplied by the instructor**. On GitHub, the
older default `master` branch is not this course. Until the 2026 branch is
published, use the instructor's source archive. Open a terminal in its root
(the directory containing `pyproject.toml`).

## Reproducible setup with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and
[Git](https://git-scm.com/downloads), then run:

```bash
uv sync --frozen --python 3.13 --extra teaching
uv run --frozen --extra teaching python scripts/check_setup.py
uv run --frozen --extra teaching jupyter lab
```

The first command needs the network. Once installed, add `--offline` to `uv run`
for classroom use. Open `book/00-primer.ipynb` or `book/01-catalogue.ipynb`.

## Standard Python alternative

```bash
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux, or
`.venv\Scripts\Activate.ps1` in Windows PowerShell. Then:

```bash
python -m pip install -e ".[teaching]"
python scripts/check_setup.py
python -m jupyter lab
```

This alternative resolves compatible package versions; `uv.lock` records the
exact tested set. Select the same interpreter as the notebook kernel. If a cell
cannot import `course2026`, run the editable install in the kernel's environment
and restart the kernel. Check `sys.executable` in a cell to see which Python it uses.

## Readiness check

You should see `Setup OK`, 395 usable rows out of 400 and no import errors.
Run `python -m pytest -q` in the active environment; all reference tests should
pass. The separate `exercises/test_weighted_mean.py` intentionally fails until
you repair its starter function in Session 3.

For Windows, use PowerShell for Python commands and Git Bash for the shell
blocks in the Git practical. For VS Code, install Microsoft's Python and Jupyter
extensions and choose this environment in **Select Kernel**.

If installation is blocked, tell the instructor before class. Pairing or an
instructor-provided JupyterHub environment is a fallback; an account with a paid
AI service is never required. Keep a local copy of the repository and data.
