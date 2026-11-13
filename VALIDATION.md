# Validation — graphical coding-agent walkthroughs

Checked 13 November 2026. Published teaching/build source:
`8a00ba9a34ddb37197412932bed14d7df711f008` on `codex/phd-python-2026`.
[Previous Git walkthrough validation](https://github.com/xangma/jupyter_data_languages/blob/9e40c754a3f37a347920132c6e0d118fb09be557/VALIDATION.md)
is retained in history.

## Implementation

Lecture 3 has three native, synchronized six-choice tab groups for Codex,
Claude Code, Antigravity, Cline + Qwen, OpenCode and Jupyter AI. Matching setup
tabs use graphical desktop/editor controls. Shared terminals prepare the
workspace, run pytest and inspect Git; agent startup and interaction use GUIs.
The scientific contract, independent expectations, test checkpoint, bounded
repair and six-hour course structure remain unchanged.

Six real GUI captures have editable numbered SVG callouts, captions, alt text
and full-size links. Five new desktop/editor captures accompany the CPD Jupyter
AI edit-approval capture. The SVGs embed unchanged JPEG bytes. Provenance and
editing instructions are in `book/screenshots/README.md` and `callouts.json`.
All eighteen cell IDs, six code cells and source notebook metadata are preserved;
source outputs remain empty.

The public CPD provider advertises `qwen3-8-27b-mtp-ud-q4-k-xl`; the prepared
hosted Jupyter AI/OpenCode configuration uses `cpd/qwen3.8`. Model inference and
client file/command execution locations are explained separately.

## Tests and build

- Strict eleven-page build passed with Node 22.23.2 and pinned MyST 1.12.0,
  including the Hub cold-start checks and all five notebook launch routes.
- All 22 annotated screenshot overlays regenerate exactly with valid bounds.
- All six choices synchronized across all three live lesson groups without
  horizontal overflow. All six setup choices rendered.
- All six GUI screenshots loaded successfully both in the live book and in
  CPD JupyterLab. A visual check confirmed the annotated book layout.
- The actual Downloads link returned a notebook matching all eighteen published
  cell IDs and source strings.
- The preceding validation of the same scientific code passed all 24 reference
  tests and executed all five notebooks in fresh local kernels. This GUI
  follow-up changed prose and media only.
- A fresh copy of the final published notebook executed all six code cells on
  CPD's **Python PhD (locked)** kernel as `[1, 2, 3, 4, 5, 6]`, with zero error
  outputs. Its intentional starter check observed nine failing tests as designed.
- All three production Kustomize entrypoints and the book base rendered. All
  four PR checks passed: validate, storage-policy, registry-policy and
  private-llama-source.

## Deployment

[PR 446](https://github.com/icg-innovation/space-k8s-gitops/pull/446) merged as
`02337b39aeb2ad432833f8fe7a33ee63a1e7b500`. Flux's source and apps Kustomization
applied that revision with Ready=True; apps also reported Healthy=True. The
static book has one available replica at:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:72166c8fd309c7004fa212e4abc4d39e2708dd0f8e5e3a4b63e8bf884210844e`

The live page serves the graphical lesson and all six images. Only the static
book digest and registry inventory changed. The JupyterHub integration and
standard runtime remain at:

`ghcr.io/icg-innovation/phd-python-notebook:standard-387e9ee@sha256:cac45236652a82697f001f805b9667b1d2541cc66e059a0a1a1d2c307b747428`

## Observed student workflow and limits

The actual book's **Open this notebook in CPD JupyterHub** action reused the
running standard server and pulled the new source, preserving existing student
changes. The source commit is present in the resulting checkout. The fresh
published-copy check above avoided replacing the user's modified notebook.
JupyterLab displays all three tab sets and six screenshots. Its MyST renderer
synchronizes within each Markdown cell; the book synchronizes across groups.

The CPD Jupyter AI/OpenCode practical completed actual scoped file reads,
reviewed student test creation and one-time tool approvals. The agreed tests
were committed before the implementation repair. The initial combined suite
reported 11 failures/1 pass. The bounded repair then passed all 12 checks;
an independent rerun confirmed both test file hashes unchanged. The accepted
repair and AI-use record were committed in the disposable practice repository.

Desktop captures illustrate controls rather than claiming six complete client
runs. Codex, Antigravity and OpenCode returned plans. Claude's local trial did
not start responding and was stopped: its image documents pre-send setup.
Cline's existing Qwen provider was preserved; its image does not demonstrate
CPD inference. It shows Plan, Auto-approve None and an unapproved command
request. The pending task was stopped. Automatic Cline actions remain disabled.
OpenCode Desktop's installed Big Pickle selection is an interface example,
not a claim that it inherited the hosted CPD configuration.

## Evidence and cleanup

Concise build/deployment records, browser results, the live book capture,
CPD notebook execution result and archived agent chat/Git bundle are in
`evidence/lecture3-tabs-20261113/` in the task workspace.

The two task-owned notebook kernels were shut down. Task check copies,
checkpoints, practice files and chat were removed after preserving their
unique evidence. The student server UID remained unchanged and Running;
other notebooks, kernels, terminals and personal files were preserved.

The preview stopped and temporary local environments, build outputs, executed
copies, fixture directories and task image tags were removed. Shared caches
were preserved. `cleanup-gui.json` records actual available space before and
after cleanup; retained evidence is below 1 MiB.
