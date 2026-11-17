# Validation — pedagogical revamp and GUI walkthroughs

## Session 2 restructure, software licensing & 17 concise diagrams — 17 November 2026 (`agy/pedagogy-revamp-20261114`)

Verified in `/Users/xangma/.gemini/antigravity/scratch/phd-python-2026-revamp`:

- **Prose smoothing & hover hygiene**: Removed shoehorned subfield roll-calls (`k-modes`, `inflation spectrum`, `SNR triggers`, `Fisher-information additivity`) and standalone single-symbol KaTeX (`k k`, `h(t) h(t)`) across all 5 notebooks, scoped `view` → `array view` in `myst.yml` so `review`/`overview` never get false `<abbr>` hover underlines, and added 11 Git/licensing hover definitions (`48` total keys in `myst.yml`).
- **Session 2 restructure & software licensing**: Restructured `book/02-git-and-tests.ipynb` into a 5-part progression (**1. Snapshots, staging & commits → 2. Branches & merges → 3. Remotes, clones & safe recovery → 4. Forks, pull requests & etiquette → 5. Unit tests, software licensing & handoff**), adding explicit **Branch vs Clone vs Fork (`upstream` / `origin`) vs Pull Request** coverage, **PR etiquette** (author, reviewer, and AI-assisted PR accountability), and **Software licensing & citation** ([choosealicense.com](https://choosealicense.com/) default-copyright trap, permissive `MIT`/`BSD-3-Clause`/`Apache-2.0` vs copyleft `GPL-3.0` vs `CC-BY-4.0` for data/docs, `CITATION.cff` + Zenodo DOIs, and supervisor/funder IP checks).
- **17 concise diagrams & natural SVG scale cap**: Added `git-zones-lifecycle`, `git-merge-types`, and `git-clone-fork-pr`, trimmed prose boxes and long banners across all **17 editable DOT/SVG diagrams** (`render_diagrams.py --check`, capping export scale at `1.0` so compact diagrams stay crisp), and verified all **52 annotated screenshots** (`render_screenshot_callouts.py --check`), **28 unit tests** (`pytest`), **5 executed notebooks** (`validate_course.py`), and **10 strict HTML pages** (`BASE_URL=/python-phd npm run build:docs`, `0` warnings).
- **Live CPD deployment — 17 November 2026**:
  - Course source published on `codex/phd-python-2026` at `7890f2b0966e47a35021ae041f5f3583adf7812a` (expanding Session 2 Part 1 into a complete visual Git & GitHub concept guide and command cheat sheet, following `922a291` / [PR 454](https://github.com/icg-innovation/space-k8s-gitops/pull/454)).
  - [PR 455](https://github.com/icg-innovation/space-k8s-gitops/pull/455) passed all 4 required checks (`Private registry source`, `Registry policy checks`, `Storage policy checks`, `Traefik migration checks`) and merged as `7d395278c0a42b704e8fe1a726437c128cf06498`.
  - Flux `gitrepository/flux-system` and `kustomization/{flux-system,apps,infrastructure}` reconciled `Ready=True` at `main@sha1:7d395278c0a42b704e8fe1a726437c128cf06498`.
  - `deploy/phd-python-jupyterbook` rolled out cleanly to `pod/phd-python-jupyterbook-64ff6dd966-rwt6w` (`1/1 Running` on `node3`) at `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:564c97c31aac417e43776e5895cc89ee5a8729f514ec166a75990a94d81ed6b9`, while `helmrelease/jupyterhub` (`True`) remained undisturbed.
  - Live `https://icg-cpd-cluster.port.ac.uk/python-phd/` returned `HTTP 200` across all 10 student routes (including the live Session 2 Part 1 Git & GitHub cheat sheet, PR etiquette, `choosealicense.com` licensing, and all 17 concise SVG diagrams), `HTTP 404` on `/python-phd/instructor/`, and `HTTP 200` on `/jupyterbook/` (`CPD Training`).

---

## Session 1 cross-model review & dependency-solving refinement — 16 November 2026 (`agy/pedagogy-revamp-20261114`)

Verified in `/Users/xangma/.gemini/antigravity/scratch/phd-python-2026-revamp` following independent external reviews by **Gemini Pro**, **OpenAI Codex (`gpt-6-astra`)**, and **Anthropic Claude (`claude-opus-5-5`)**:

- **Unit, diagram and overlay checks**: `pytest` (**28 passed**), `render_diagrams.py --check` (**14 editable DOT/SVG diagrams**, refining `python-environments`, `broadcasting`, `fits-vs-ecsv`, and `catalogue-selection` with native `viewBox` widths $\le 813\text{ pt}$), and `render_screenshot_callouts.py --check` (**52 annotated screenshots**).
- **Primer & Session 1 layout, CPD-independent prose, hover explainers and self-contained flow**: Moved `Environments and kernels: pip, conda and uv` into `book/00-primer.ipynb` so `book/01-catalogue.ipynb` starts immediately with the synthetic table, added **36 native MyST hover-over explainers** (`project.abbreviations` in `myst.yml` rendering `<abbr class="hover-text">` popover tooltips on `QTable`, `ECSV`, `FITS`, `HDU`, `WCS`, `apparent magnitude`, `boolean mask`, `broadcasting`, `lockfile`, `dependency solver`, etc.), cut unnecessary jargon (`IEEE-754`, `SAT solver`, `cryptographic hashes`, `CODATA/IAU`) while welcoming inflation/GW/simulation theorists (`-45` words in Primer, `-54` words in Session 1), removed `book/instructor.md` and all inline workshop/break/partner cues, generalised Setup, Session 2 (`JupyterLab` + `VS Code`) and Session 3 (`Claude Code`, `Codex` and `Cline` tabs) with zero `CPD` tutorial references, and retained the optional `myst.yml` JupyterHub/Thebe toolbar launch hooks.
- **Notebook execution, FITS provenance and output hygiene**: `validate_course.py` executed all **5 course notebooks** cleanly (`00-primer` through `04-signal-extension`) with zero errors or warnings, verified preserved `<=8`-character FITS header cards (`SYNTH`, `SEED=20261109`, `H0_INJ=70.0`) and persistent `outputs/catalogue_summary.{pdf,png}` export, while keeping all source `.ipynb` cells clean (`outputs: []`, `execution_count: null`).
- **Strict MyST HTML build and hydrated browser check**: `BASE_URL=/python-phd npm run build:docs` built all **10 student pages** strictly with zero warnings (`404` on `/python-phd/instructor`), injected all 5 CPD notebook launch routes, replaced the default top-left `"Made with MyST"` navbar label with **`Python for ICG Research`** (`site.options.logo_text` + `site.title`) while naming the root sidebar TOC item **`Course overview`** (`project.short_title`), and rendered `/python-phd/primer` and `/python-phd/catalogue` cleanly in headless Chrome (`HTTP 200`, `0` broken images).
- **Live CPD deployment — 16 November 2026**:
  - Course source published on `codex/phd-python-2026` at `afae73d54add45d9f7c68ca5b1fdd0471578bff2` (following `93eaeee` / [PR 451](https://github.com/icg-innovation/space-k8s-gitops/pull/451)).
  - [PR 453](https://github.com/icg-innovation/space-k8s-gitops/pull/453) passed all 4 required checks (`Private registry source`, `Registry policy checks`, `Storage policy checks`, `Traefik migration checks`) and merged as `d97f734c28a313c7103db4b17a1cfd55e377ea33`.
  - Flux `gitrepository/flux-system` and `kustomization/{flux-system,apps,infrastructure}` reconciled `Ready=True` at `main@sha1:d97f734c28a313c7103db4b17a1cfd55e377ea33`.
  - `deploy/phd-python-jupyterbook` rolled out cleanly to `pod/phd-python-jupyterbook-fd95cc46c-8mbww` (`1/1 Running` on `node3`) at `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:c4d93256bce47a93411b2a05482c8d30a0c30ca0cd2b78ba8d98076f5ec1681b`, while `helmrelease/jupyterhub` (`True`) remained undisturbed.
  - Live `https://icg-cpd-cluster.port.ac.uk/python-phd/` returned `HTTP 200` across all 10 student routes with top-left navbar **`Python for ICG Research`** and first sidebar link **`Course overview`**, `HTTP 404` on `/python-phd/instructor/`, and `HTTP 200` on `/jupyterbook/` (`CPD Training`).

---

## Session 1 & Primer expansion — 15 November 2026 (`agy/pedagogy-revamp-20261114`)

Verified in `/Users/xangma/.gemini/antigravity/scratch/phd-python-2026-revamp` on top of `4cabba9` (legacy `CKrawczyk` / 2025 files untouched):

- **Unit, diagram and overlay checks**: `pytest` (**28 passed**), `render_diagrams.py --check` (**14 editable DOT/SVG diagrams**, adding `python-environments` and `array-axes-slicing`), and `render_screenshot_callouts.py --check` (**52 annotated screenshots**).
- **Notebook execution and output hygiene**: `validate_course.py` executed all **5 course notebooks** cleanly (`00-primer`, `01-catalogue`, `02-git-and-tests`, `03-agents-and-inference`, `04-signal-extension`) with zero errors or `FITSFixedWarning`s; all source `.ipynb` code cells retain `outputs: []` and `execution_count: null`.
- **Strict MyST HTML build and hydrated browser check**: `BASE_URL=/python-phd npm run build:docs` built all **11 pages** strictly with zero warnings, injected all 5 CPD notebook launch routes, and passed headless Chrome checks (`HTTP 200`, `0` broken images, `0px` horizontal overflow across `/python-phd/primer` and `/python-phd/catalogue`).

---

## Local verification — 14 November 2026 (`agy/pedagogy-revamp-20261114`)

Verified in an isolated worktree branched from `ac96bd8` (`codex/phd-python-2026`):

- **Unit and overlay suite**: `uv run --frozen --extra teaching python -m pytest -q`
  passed **28 tests** (including 4 new SVG crop and callout-bounds checks in
  `tests/test_screenshot_callouts.py`).
- **Environment and data check**: `uv run --frozen --extra teaching python scripts/check_setup.py`
  passed (`Setup OK`, 395/400 usable synthetic survey rows).
- **Diagrams and screenshot overlays**:
  - `uv run --frozen python scripts/render_diagrams.py --check` passed across all
    **12 editable DOT/SVG diagrams** (`array-views`, `fits-vs-ecsv`,
    `git-undo-vs-revert` and `nyquist-aliasing` added; `shared-mask`,
    `agent-architecture` and `agent-review-loop` updated).
  - `uv run --frozen python scripts/render_screenshot_callouts.py --check` passed
    across all **52 annotated screenshot overlays**, preserving embedded raster
    bytes while enforcing lossless `viewBox` + `<clipPath>` crops and callout bounds.
- **Notebook execution and hygiene**: `uv run --frozen --extra teaching python scripts/validate_course.py`
  executed all **5 course notebooks** cleanly (`00-primer`, `01-catalogue`,
  `02-git-and-tests`, `03-agents-and-inference`, `04-signal-extension`); source
  `.ipynb` files retain empty outputs (`outputs: []`, `execution_count: null`).
- **Strict MyST HTML build and headless browser checks**: `BASE_URL=/python-phd npm run build:docs`
  built all **11 pages** strictly with zero warnings, injected all 5 CPD notebook
  launch links and verified cold-start config. Headless Chrome verified `HTTP 200`,
  `0px` horizontal overflow, zero broken images, and synchronized 3-tab switching
  (`Jupyter AI on CPD`, `Cline + CPD Qwen`, `Claude Code`) across the rendered site.
- **Live CPD deployment — 14 November 2026**:
  - Course source published on `codex/phd-python-2026` at `9a67ad96108102eedb871ba32e15ff3496264301`.
  - [PR 449](https://github.com/icg-innovation/space-k8s-gitops/pull/449) passed all 4 required checks (`Private registry source`, `Registry policy checks`, `Storage policy checks`, `Traefik migration checks`) and merged as `3c1719aa6cc6a7ecc27fa896fb605a239f983b24`.
  - Flux `gitrepository/flux-system` and `kustomization/{flux-system,apps,infrastructure}` reconciled `Ready=True` at `main@sha1:3c1719aa6cc6a7ecc27fa896fb605a239f983b24`.
  - `deploy/phd-python-jupyterbook` rolled out cleanly to `pod/phd-python-jupyterbook-676f86798b-gqxsh` (`1/1 Running`, `ready=true`) at `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:86b58865595e1372eb47f48b94a4405b51fb4c856c74197536c26f10623da843`, while `helmrelease/jupyterhub` (`True`) and running student pod `jupyter-xangma` (`uid=031025c9-8042-41c8-a6b4-0bdca62a6453`, runtime digest `sha256:cac45236652a82697f001f805b9667b1d2541cc66e059a0a1a1d2c307b747428`) remained undisturbed.
  - Headless Chrome against live `https://icg-cpd-cluster.port.ac.uk/python-phd/` verified `HTTP 200`, `0` broken images (60 rendered SVG/PNG assets across the 11 pages), `0px` horizontal overflow, live synchronized 3-tab switching (`Jupyter AI on CPD`, `Cline + CPD Qwen`, `Claude Code`), and `HTTP 200` on `/jupyterbook/` (`CPD Training`).

---

## Previous live deployment validation — 13 November 2026

Checked 13 November 2026 on `codex/phd-python-2026`. Published teaching/build
source: `f0039d29fa11b5f64d692d12dd3f9886e4543428`.
[Previous deployment validation](https://github.com/xangma/jupyter_data_languages/blob/a670592/VALIDATION.md)
is retained in history.

## Implementation

All eighteen agent slots (plan, independent tests and final review for six tools)
now contain real GUI screenshots, editable SVG callouts, captions, alt text and
full-size links. Claude uses the Claude Code editor GUI with returned results
and one-time approvals. Cline uses CPD Qwen with Plan/Act, explicit edit approval,
the working-tree diff and an explicit successful test exit status.

The Git lesson adds remote controls, actual rejected pushes and recovery in both
editors, plus GitHub PR creation, review and merge. JupyterLab Pull leaves a
staged merge that students must inspect and commit before pushing. Four older
VS Code captures now have editable callouts. Setup covers sign-in, workspace
choice and the locked kernel; every tool-guide tab has a GUI illustration.

Only Markdown cells changed in the two lecture notebooks. All eighteen IDs per
notebook, metadata, code cells and empty source outputs remain unchanged. The
three-session, six-hour structure and existing runtime are preserved.

## Focused checks and build

- Five native agents completed the same isolated repair; independent reruns
  passed all twelve tests with both test files unchanged. The exact saved
  Jupyter AI repair bundle also passed twelve tests on CPD. Its screenshot is
  labelled as saved chat, rather than a fresh model response.
- All five course notebooks executed successfully in the locked environment.
- All 52 annotated screenshot overlays regenerate exactly; source embedding,
  truthful MIME types and callout bounds passed validation.
- Strict eleven-page build passed, including five notebook launch routes and
  Hub cold-start checks. Build assets: `build-phd-f2ff20ceb93e`.
- Local browser checks passed for all eighteen agent images across synchronized
  tabs (about 701 pixels wide), all twelve VS Code and thirteen JupyterLab Git
  images, all three setup images and all six tool-guide images.

## Deployment

[PR 448](https://github.com/icg-innovation/space-k8s-gitops/pull/448) merged as
`e25aa2566b1d28ca21345a185c3f7539cd5bb84b`. All four checks passed: validate,
storage-policy, registry-policy and private-llama-source. The book base and all
three production Kustomize entrypoints rendered successfully.

Flux's GitRepository and apps Kustomization both report Ready=True at that merge
revision. The single running book pod is ready at:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:00acb94b237ee8846359f47367bfb11fe43155a4a757dda8d9b567e084a8e752`

Only the static image and registry inventory changed. Student server UID
`031025c9-8042-41c8-a6b4-0bdca62a6453` remains Running with the existing notebook
runtime digest `sha256:cac45236652a82697f001f805b9667b1d2541cc66e059a0a1a1d2c307b747428`.

## Observed student workflow

- The live book loaded all eighteen agent screenshots across synchronized tabs,
  all 25 Git GUI images, the three GitHub PR images, three setup images and all
  six tool-guide illustrations. Captions and full-size links are present.
- Start compute connected to the existing Hub server. Clearing and running the
  first Session 3 cell produced the fresh expected result, `Candidate: 1.5`,
  against the independent expectation of 1.2.
- The book's notebook button opened the editable Session 3 notebook. The course
  refresh merged the published source and retained the existing 22-cell notebook,
  including its extra cells. Every pre-launch notebook's exact bytes remain
  recoverable in the checkout's Git history.
- Fresh task-owned copies of Sessions 2 and 3 ran all three and six code cells
  respectively with Python PhD (locked), without errors. JupyterLab loaded all
  eighteen agent screenshots and all 25 Git GUI images at readable width.
- A fresh collaborator clone of the JupyterLab sharing example contained the
  completed merge and passed its test. A fresh clone of the merged GitHub PR's
  main branch passed both tests.

## Evidence

`evidence/screenshot-completion-20261113/` in the task workspace contains build
logs, browser image inventories, independent test records and capture provenance.
Raw captures and editable manifests remain in `book/screenshots/`.

The temporary notebook and book kernels were shut down; the four original
kernels and all three existing terminals remain. The saved chat, executed test
notebooks and Git histories were archived before removing the remote test
folder. The local preview stopped cleanly. Temporary environments, dependencies,
executed copies, build outputs, kernel registration and local image tag were
removed; shared caches were preserved. Unique local practice source/history,
verified bundles and patches are retained as evidence. `cleanup.json` and
`remote-cleanup.json` record measured available space before and after cleanup.
