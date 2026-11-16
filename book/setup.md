# Before the first session

Allow 15–25 minutes to set up your environment. You need Python 3.11+ and [Git](https://git-scm.com/downloads) 2.28+ (the locked course environment targets Python 3.13); [VS Code](https://code.visualstudio.com/) is optional. Everyone should also read *Environments and kernels: pip, conda and uv* at the start of [the Primer](00-primer.ipynb#environments-and-kernels-pip-conda-and-uv) for how dependency solvers, `uv`, `pip` and `conda` relate.

Clone the [`codex/phd-python-2026` course branch](https://github.com/xangma/jupyter_data_languages/tree/codex/phd-python-2026) explicitly (the default `master` branch is an older archive) and enter the repository root:

```bash
git clone --branch codex/phd-python-2026 https://github.com/xangma/jupyter_data_languages.git
cd jupyter_data_languages
```

## Option A: Reproducible setup with uv (recommended)

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run from the repository root:

```bash
uv sync --frozen --python 3.13 --extra teaching
uv run --frozen --extra teaching python -m ipykernel install --user --name python-phd --display-name "Python PhD (locked)"
uv run --frozen --extra teaching python scripts/check_setup.py
uv run --frozen --extra teaching jupyter lab
```

`uv sync` creates a local `.venv/` with the exact package versions and hashes pinned in `uv.lock`, while `ipykernel install` registers that `.venv` interpreter in Jupyter as **Python PhD (locked)**. After installation you can pass `--offline` to `uv run`, and in **each new terminal** for Sessions 2 and 3 activate `.venv` from the course root (`source .venv/bin/activate` on macOS/Linux, `source .venv/Scripts/activate` in Windows Git Bash, or `.venv\Scripts\Activate.ps1` in PowerShell).

## Option B: Standard venv or conda

Create and activate an isolated environment using standard `venv` (`python -m venv .venv`, followed by `source .venv/bin/activate` on macOS/Linux, `source .venv/Scripts/activate` in Windows Git Bash, or `.venv\Scripts\Activate.ps1` in PowerShell) or `conda` (`conda create -n python-phd python=3.13` followed by `conda activate python-phd`), then install the editable package and kernel:

```bash
python -m pip install -e ".[teaching]"
python -m ipykernel install --user --name python-phd --display-name "Python PhD (locked)"
python scripts/check_setup.py
python -m jupyter lab
```

In JupyterLab, click the kernel indicator at a notebook's top right, choose **Python PhD (locked)** under **Start python Kernel**, and click **Select** (start a fresh kernel rather than attaching to another notebook's session; in VS Code, choose `.venv` or `python-phd` in **Select Kernel** with the Python and Jupyter extensions). Note that `pip install -e ".[teaching]"` resolves unconstrained version ranges from `pyproject.toml` while registering the same `python-phd` kernel name (`Option A` pins exact versions from `uv.lock`). On Windows, use **Git Bash** for shell commands in Sessions 2 and 3.

![JupyterLab Select Kernel dialog with Python PhD locked selected](../book/screenshots/jupyterlab-kernel-choice.svg)

**Select kernel:** Pick **Python PhD (locked)** (**1**) and click **Select** (**2**), leaving **Always start the preferred kernel** (**3**) unchecked. [Open full-size screenshot](../book/screenshots/jupyterlab-kernel-choice.svg)

## Readiness check

1. **Python and Git:** Run `python scripts/check_setup.py` and `python -m pytest -q` in your active course terminal. Confirm `395 usable rows out of 400`, `Setup OK`, and passing reference tests (`exercises/test_weighted_mean.py` intentionally fails until you repair a separate practice copy in Session 3 — leave `exercises/` untouched). In a notebook cell, check that `import sys; print(sys.executable)` points to your `.venv` or `python-phd` environment.
2. **Coding agent (before Session 3):** Complete [Choose your coding agent](agent-tools.md) to configure `Claude Code`, `Codex`, `Cline`, or the manual option and create your practice folder.
