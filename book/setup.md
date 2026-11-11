# Before the first session

Allow 20–30 minutes for installation. You need Python 3.11 or later and Git;
the locked course environment uses Python 3.13. A working notebook and a terminal
are enough. VS Code is optional.

## Use CPD without local installation

Open [the Python PhD book](https://icg-cpd-cluster.port.ac.uk/python-phd/) and
choose **Connect to JupyterHub**. Sign in with your enrolled GitHub account.
Preparing the course workspace can take a few minutes on the first visit.
On a notebook page, start the compute environment and run cells from the top.
For Git, a terminal or editing files, open the connection menu and choose
**Open this notebook in JupyterHub**. Your workspace contains the course checkout.

If access is denied, ask the instructor to check your existing CPD enrolment;
creating a GitHub account alone does not grant access. Disconnecting the book
does not stop your server: use JupyterHub's control panel to stop the `python-phd`
server when finished. Your files remain in your workspace.

## Install locally instead

Use the [`codex/phd-python-2026` course branch](https://github.com/xangma/jupyter_data_languages/tree/codex/phd-python-2026).
The older default `master` branch is not this course. Install Git, then clone
the course branch explicitly and enter its root (containing `pyproject.toml`):

```bash
git clone --branch codex/phd-python-2026 https://github.com/xangma/jupyter_data_languages.git
cd jupyter_data_languages
```

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
For the terminal practicals, activate this environment in each new terminal:
`source .venv/bin/activate` on macOS/Linux, or `source .venv/Scripts/activate`
in Windows Git Bash. Run that from the course root before entering a sandbox.
In Windows PowerShell, use `.venv\Scripts\Activate.ps1`.

uv does not install pip in this environment. Use `uv pip freeze` to inspect its
packages; installing pip during class is unnecessary. Inside CPD JupyterLab the
course interpreter is already on the terminal's PATH; use `python -m pip freeze`.

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
you repair a **sandbox copy** of its starter in Session 3. Leave the originals
in `exercises/` unchanged: the notebook uses them to demonstrate the failing baseline.

For Windows, use Git Bash for the shell blocks in Sessions 2 and 3 and activate
the environment there first, as above. For VS Code, install Microsoft's Python and Jupyter
extensions and choose this environment in **Select Kernel**.

If installation is blocked, tell the instructor before class. Pairing or an
instructor-provided JupyterHub environment is a fallback; an account with a paid
AI service is never required. Keep a local copy of the repository and data.
