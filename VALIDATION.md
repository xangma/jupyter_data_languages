# Validation — Git commands, VS Code and CPD JupyterLab

Checked on 13 November 2026. Published teaching/build source:
`e4e97e91e7debbe0808c3eef0d6b58a207391b35` on `codex/phd-python-2026`.
[Previous VS Code capture validation](https://github.com/xangma/jupyter_data_languages/blob/ab0ab1af78ad79d7366701e59682c458bd0f3d58/VALIDATION.md)
is retained in history.

## Implementation

Ten native MyST tab groups pair Git commands with VS Code and CPD JupyterLab
instructions: workspace, untracked files, staging, first commit, branches,
unstaged diff, partial staging, merge conflict, private undo and shared revert.
Ten real CPD captures add editable numbered SVG callouts, captions and alt text.
All twenty screenshots have full-size links. The screenshot README and
`callouts.json` document capture provenance and editing.

The book synchronizes the chosen interface across all ten groups. CPD's native
MyST notebook renderer synchronizes within a Markdown cell; the introduction
explains selecting the interface again in the next cell. This uses existing
JupyterLab extensions and native tabs, without build wrappers or added runtime
packages. Shared setup and tests remain outside the interface alternatives.

The practice helper now ignores JupyterLab's `.ipynb_checkpoints/`, so opening
files leaves the intended four starter files visible. All eighteen notebook
cell IDs, three code cells and runtime metadata are preserved, with empty
source outputs. The three-session, six-hour structure remains unchanged.

## Tests and build

- All 24 reference tests passed in the locked Python 3.13 environment.
- All five notebooks executed in fresh kernels and empty working directories.
  The final clarification changes Markdown only; code remains identical.
- Both practice-helper modes produced four starter files, refused overwrites
  and ignored an actual checkpoint file.
- All sixteen annotated SVGs regenerate exactly, embed the original JPEG bytes
  unchanged and have valid annotation bounds. The older four PNGs are retained.
- Node 22.23.2 built all eleven pages strictly, including five notebook launch
  routes and the existing Hub cold-start/hydration checks.
- All three production Kustomize entrypoints rendered. All four CI checks
  passed for each promotion: validate, storage-policy, registry-policy and
  private-llama-source.

## Deployment

[PR443](https://github.com/icg-innovation/space-k8s-gitops/pull/443) deployed the
walkthrough. [PR444](https://github.com/icg-innovation/space-k8s-gitops/pull/444)
then deployed the notebook synchronization clarification, merging as
`1b25a2b03a8e25843f3ee8f4b4f04f5a20fc01c4`.
Flux's source and apps Kustomization applied that exact revision with Ready=True.
The book rolled out successfully with one updated, available replica at:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:e700b18e4f82c6dd35c8fef61ce028468841733b7fa7f4bc24b6a1906142f6f2`

Only the static book image and registry inventory changed. The standard
notebook runtime and JupyterHub integration are retained.

## Observed student workflow

- On the live CPD book, choosing any of the three interfaces selects it in all
  ten groups. All screenshots and captions are present, with no horizontal
  page overflow. All 23 Git media assets returned HTTP 200, the expected MIME
  type and exactly the validated build bytes.
- The actual book's **Open this notebook in CPD JupyterHub** action reused the
  standard CPU workspace and pulled the final source. Its cell IDs, code and
  clarified introduction match the publication source. All ten JupyterLab
  screenshots render in the notebook, and the observed per-cell tab behavior
  matches the instructions.
- **Run All Cells** on **Python PhD (locked)** completed the three code cells
  as `[1]`, `[2]`, `[3]`, including all 17 scientific reference checks in 0.55s.
- An independent practice repository exercised real JupyterLab GUI staging,
  unstaging, branch creation and commits. The partial snapshot showed only
  wraparound staged while a later full-turn edit remained outside the index.
- The actual **Git → Merge Branch…** action produced the intended README
  conflict. Editing Result and **Mark as resolved** saved and staged both facts;
  three angle tests passed before the GUI merge commit. Git confirmed two parents.
- A terminal soft reset retained the private work staged and on a rescue branch.
  A shared revert preserved both commits; **Git → Push to Remote** updated the
  practice remote. A fresh collaborator clone received the corrected README.
- A fresh four-file repository also passed its initial test, displayed the
  staged diff before its first commit, and recorded the first commit through
  the GUI. Task B then passed five angle checks, exposed the deliberate bad
  formula with two failures, and passed all five again after restoring only
  the implementation. Its test branch reached the practice remote.

## Evidence and cleanup

Concise logs, the Git history bundle, image/build metadata, live browser and
asset checks, deployment records and the live-book capture are in
`evidence/jupyterlab-git-tabs-20261113/` in the task workspace.

The task-created terminal exited, practice repositories were removed after
preserving their history, and capture/preview tabs closed. The existing shared
student server, other terminals/kernels and unrelated files are preserved.
Temporary local build/install outputs and kernel registrations are removed
once validation ends; `cleanup.json` records actual available disk space before
and after removal. Source captures and editable figures remain in the course.
