# Validation — Git foundations and VS Code

Checked on 13 November 2026. Teaching/build source:
`53a7c3836309844fdd2197464a049f64630db8f3` on `codex/phd-python-2026`.
The current standard-workspace integration at `19866ee` is included.
[Earlier diagram validation](https://github.com/xangma/jupyter_data_languages/blob/afee1c11c78897fa030c1b1369f2eb8c068001f6/VALIDATION.md)
remains available in history.

## Teaching content

Session 2 introduces Git from the working tree/index/commit model, distinguishes
Git, GitHub and VS Code, and includes explicit initialisation, branches, conflicts,
private undo and shared recovery. Four real VS Code 1.141.0 captures show the
actual exercise states. Their provenance is in `book/screenshots/README.md`.
Two bounded subagent reviews informed the revision; the parent verified the
material command and UI behaviours. The sources and adopted ideas are recorded
in `COURSE_REVIEW.md` and the further-reading page.

The core remains three two-hour sessions, with breaks and instructor-only pacing.
Existing notebook code cells and their original IDs are preserved. Student source
notebooks have empty outputs. The four other notebooks match the current
standard-workspace source. A scoped Git attribute prevents local nbstripout
filters from renumbering the validated book's cell IDs.

## Local validation

- 24 reference tests passed.
- All five notebooks executed in fresh kernels and empty working directories
  using their declared `python-phd` kernel and the locked local environment.
  Temporary kernel registration was removed afterward.
- Both practice-constructor routes passed: manual Git initialisation through
  `--files-only`, and the compatible default. Both refuse an existing target
  without changing its files.
- The Git practical passed through staging, the deliberate same-line conflict,
  private recovery, shared revert/push and an independent collaborator clone.
  Actual VS Code Undo Last Commit retained the work staged. Complete Merge
  staged the resolved file without creating the repository's merge commit.
- The introduced angle bug produced two failures; restoring only `angle.py`
  left the student tests intact and produced five passing tests.
- Rejected-push recovery retained both contributors' work; fetch left working
  files untouched; reflog-based branch rescue retained the current checkout.
- Node 22.23.2 built all 11 pages strictly. The five Hub launch routes and
  cold-return/hydration checks passed with the current standard-server bridge.
- All four screenshots were inspected in the rendered book in Edge at normal
  article width. All seven Git media assets loaded without page overflow.
- All three production Kustomize entrypoints and registry policy passed. The
  policy used a task-owned clone containing the exact serving-source pin.

## CPD deployment

[GitOps PR 438](https://github.com/icg-innovation/space-k8s-gitops/pull/438) merged as
`840133f859c1cb2d84eed7f629e07d3ba3cd8dc4` after all four CI checks passed.
Flux applied that exact revision with Ready=True. The book Deployment became
available at the expected immutable image:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:e53852b6671049d523f6cdf1593b5d6c5edae1ba7400bfc0dbda1a8d4c870ece`

The existing standard notebook runtime remains
`sha256:cac45236652a82697f001f805b9667b1d2541cc66e059a0a1a1d2c307b747428`.
The Hub HelmRelease is Ready. Both the PhD and CPD Training book routes returned
HTTP 200. Each of the seven published Git media assets returned its expected
MIME type and exactly matched the locally validated build bytes.

## Observed student workflow

The live book's Open Notebook action started the standard CPU server, completed
course synchronisation and opened the editable Session 2 notebook in JupyterLab
with **Python PhD (locked)** selected. Run All executed all three code cells
without errors; the notebook's reference checks reported 17 passed.

A fresh JupyterLab terminal activated `/opt/course/.venv/bin/python`
(Python 3.13.18). The new constructor option, manual Git init,
first commit, soft reset retaining staged work, bare remote, shared mistake,
revert, normal push and fresh partner clone all passed. The clone retained the
private work, omitted the reversed mistake and kept both shared-history commits.
The nbgitpuller workspace HEAD was `8a6a4f300d90bbdb33fe5ab5e8280a1028d1460c`;
the published source commit was verified as its ancestor.

The CPU pod requested one CPU and had no GPU request. Generated test repositories
were removed after retaining concise evidence. The test server was stopped via
Hub Home; saved course files and notebook outputs were preserved. This live pass
covered book → JupyterLab → notebook execution → terminal Git → server stop.
The optional hosted classroom PR exercise was not repeated; sharing and recovery
were exercised against a separate bare Git remote.

Detailed logs, UI/asset checks and deployment provenance are retained outside the
source checkout in `evidence/git-session-20261113/` in the task workspace. The
four requested source screenshots and the live book screenshot are retained;
reproducible local build/install outputs are removed after validation.
