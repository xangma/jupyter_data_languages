# Validation — pedagogical revamp and GUI walkthroughs

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
- **Deployment status**: Local branch commit only; live CPD remains at the
  13 November 2026 image below pending instructor confirmation to push and open a
  GitOps promotion PR in `icg-innovation/space-k8s-gitops`.

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
