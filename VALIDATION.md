# Validation — VS Code beginner screenshots

Checked on 13 November 2026. Published teaching/build source:
`e5b7bd10dbc8f6396ed04d79953cecbfdf073ac0` on `codex/phd-python-2026`.
[Previous Git foundations and complete student-workflow validation](https://github.com/xangma/jupyter_data_languages/blob/7e3b79a0a39fadeb909ab8a0bc10f6c1308beea5/VALIDATION.md)
remains available in history.

## Implemented content

Six additional real VS Code 1.141.0 captures illustrate the project workspace,
untracked files, staged contents and commit message, the completed first commit,
branch selection, and the first unstaged test diff. Numbered callouts, captions
and alt text connect each view to the lesson's existing Git exercise. The first
four form a visual recap in the VS Code introduction; the branch and diff figures
appear at the relevant Task A steps. The original four recovery/staging captures
and eight conceptual diagrams remain in the book.

The JPEG originals are unchanged. The SVG figures embed those exact bytes and
add editable vector annotations; `book/screenshots/callouts.json` and
`scripts/render_screenshot_callouts.py` regenerate them. The screenshot README
records provenance and editing instructions. Notebook code, cell IDs and runtime
metadata are unchanged; student source outputs are empty. The course retains
three two-hour sessions with instructor-only pacing.

## Local validation

- All 24 reference tests passed.
- All five notebooks executed in fresh kernels and empty working directories
  using the declared `python-phd` kernel and locked course environment.
- Both tests in the actual screenshot exercise passed. Git confirmed the real
  first commit, the two branches at the same initial commit and the saved,
  unstaged wraparound edit. The commit and branch were created through VS Code.
- SVG regeneration/check passed for all six figures; embedded capture bytes,
  annotation counts and coordinate bounds were checked.
- Node 22.23.2 built all 11 pages strictly; all five Hub launch routes and
  cold-start/hydration checks passed. Each figure was inspected at normal article
  width. Final leaders leave the demonstrated text and controls visible.
- All three production Kustomize entrypoints rendered. All four deployment CI
  checks passed: validate, storage-policy, registry-policy and private-llama-source.

## Deployment and observed result

[GitOps PR 441](https://github.com/icg-innovation/space-k8s-gitops/pull/441) merged as
`5dde9636fd7ff18a6b683c75117d140d6653b70a`. Flux applied that exact revision with Ready=True.
The book Deployment has one updated, available replica and a ready pod at:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:d4f681f77459327b7fd684788fe94290e449052f759ceea43f068beb162cd907`

The promotion changes only the static book image and its registry inventory.
The existing JupyterHub integration and standard notebook runtime are retained.

All six figures were inspected individually on the live CPD Git lesson at normal
article width (about 749 pixels). Every image and numbered caption was present,
with no horizontal page overflow. All 13 Git media assets returned HTTP 200,
the expected image MIME type and exactly the locally validated build bytes.
The PhD home, Git lesson and CPD Training book routes returned HTTP 200.

This update's live check covers the published book and its figures. The complete
book-to-JupyterLab/notebook/terminal/server-stop workflow was validated in the
preceding revision linked above; no student server was started for these static
image changes.

Evidence, six live-page captures and job provenance are retained in
`evidence/vscode-basics-20261113/` in the task workspace. The local preview,
temporary kernel registration, exercise copy and reproducible build/install
outputs are removed after validation. Source captures, editable figures, concise
logs and the capture history bundle are preserved.
