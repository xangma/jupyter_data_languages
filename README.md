# Python for ICG Research — 2026

Three two-hour practicals for incoming ICG PhD students: scientific arrays and
astronomy data; Git and tests; coding agents and independent verification.
Open [the live CPD book](https://icg-cpd-cluster.port.ac.uk/python-phd/), or start
locally with [the course overview](book/index.md) and [setup](book/setup.md).

```bash
uv sync --frozen --python 3.13 --extra teaching
uv run --frozen --extra teaching python scripts/check_setup.py
uv run --frozen --extra teaching jupyter lab
```

Open the notebooks in `book/`. All examples use small local synthetic data.
No paid AI account or HPC access is required. See the [instructor guide](book/instructor.md)
for pacing, solutions, prerequisites and the account-free agent fallback.

## Validate and build the Jupyter Book

Python 3.13 and Node.js 22 are the tested runtimes. Commands below run from this
directory; the first installation needs the network.
Check `node --version` reports 22 or later (`nvm use` if using nvm). Older Node
releases can fail inside MyST even if its installation succeeds.

```bash
uv run --frozen --extra teaching python -m pytest -q
uv run --frozen --extra teaching python scripts/validate_course.py
npm ci --ignore-scripts
BASE_URL=/python-phd npm run build:docs
```

`validate_course.py` executes all five notebooks in fresh kernels and empty
working directories, writing `_executed/`. The book builds from those checked
copies, including the plots. Source notebooks retain empty outputs. Preview at
the intended CPD subpath:

```bash
python scripts/serve_book.py --port 8765
```

Open `http://127.0.0.1:8765/python-phd/`. Stop the foreground server with Ctrl+C.
The local preview serves static pages. The deployed CPD edition connects to
JupyterHub for live kernels; [deployment notes](deploy/README.md) describe it.

The CPD edition uses the existing authenticated bridge with a separate
`python-phd` named server and locked CPU environment. Book links open editable
source notebooks rather than generated build copies.

The course retains its MIT licence. The reused bridge UI in
`scripts/inject_jupyterhub_launch_links.py` is adapted from the GPL-3.0 UKSA
integration and is distributed under GPL-3.0-or-later; see `LICENSES/GPL-3.0.txt`.

## Provenance and earlier lectures

Adapted from [Coleman Krawczyk's lectures](https://github.com/CKrawczyk/jupyter_data_languages)
through [Xan's fork](https://github.com/xangma/jupyter_data_languages).
The latest published teaching branch found was `update_2025` at `2e4201b`,
newer than the default `master` at `8a8c246`. The local 2025 drafts, including
unpublished class 3 material, are preserved in a separate baseline commit.
The original checkout was not edited.

The earlier `classes/`, root plotting notebooks, scripts/configuration and
`Previous_notebooks/` are historical references outside the validated 2026 path;
they may need extra dependencies or repairs. [Review notes](COURSE_REVIEW.md)
record adopted recommendations. The original MIT licence is retained.
