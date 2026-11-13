# Validation — Jupyter AI in the first planning tab

Checked 13 November 2026. Published teaching/build source:
`3efe280539466ba976e6c936237c72f3e0e95ea1` on `codex/phd-python-2026`.
[Previous complete GUI workflow validation](https://github.com/xangma/jupyter_data_languages/blob/f486b4b/VALIDATION.md)
is retained in history.

## Implementation

The first **Jupyter AI** tab under **Supply context and review a plan** now has
its own planning screenshot, three editable callouts, caption, alt text and
full-size link. The later test-file review screenshot remains in its exercise.
All six tools therefore have an image in the first tab group.

`jupyter-ai-plan.jpg` is a real CPD capture of the practice files, three
one-time file-read approvals, returned diagnosis/plan, and OpenCode/CPD Qwen
**plan** controls. The SVG embeds the unchanged JPEG. The planning trial changed
none of the three practice files; only their reads were authorised.

Only the first tab group's Markdown cell changed. All eighteen cell IDs,
six code cells, notebook metadata and empty source outputs remain unchanged.
The three-session, six-hour structure and runtime are preserved.

## Focused checks and build

- All five notebooks executed in fresh local kernels in the locked environment.
- All 23 annotated screenshot overlays regenerate exactly with valid bounds.
- Strict eleven-page build passed, including Hub cold-start checks and five
  notebook launch routes.
- In the preview and live book, the **first** tab group's selected Jupyter AI
  item contains the new loaded image at 700.7 pixels wide, its full-size link
  and caption, with no horizontal overflow. The later review image is retained.
- The actual book notebook launch pulled the new source and image into the
  existing CPD workspace. A fresh, task-owned notebook copy showed the loaded
  planning image in its first Jupyter AI tab at 1182 pixels wide.
- The book base and all three production Kustomize entrypoints rendered.
  All four PR checks passed: validate, storage-policy, registry-policy and
  private-llama-source.

## Deployment

[PR 447](https://github.com/icg-innovation/space-k8s-gitops/pull/447) merged as
`1703f3fe5fd56725c2f173afd5e83ce76170501c`. Flux's GitRepository and apps
Kustomization applied that revision with Ready=True. The static book has one
available replica at:

`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:ced2e02a8e2e19f23b816105d32695708e5439f219da65b400d04c8dbaa4198b`

Only the static image and registry inventory changed. The existing student
server UID remained `031025c9-8042-41c8-a6b4-0bdca62a6453`, Running. No shared
server restart or runtime/provider change was needed.

## Evidence and cleanup

`evidence/jupyter-ai-first-tab-20261113/` in the task workspace contains concise
build and deployment records, the archived planning chat, first-tab browser
checks, unchanged-file check, JupyterLab image check and live-page screenshot.

The task-owned notebook kernel was shut down. Its copy/checkpoint, planning
chat and disposable practice folder were removed after preserving evidence.
Other notebooks, kernels, terminals and student files remain intact.
The local preview stopped; temporary environments, executed copies, build
outputs, kernel registration and task image tag were removed. Shared caches
were preserved. `cleanup.json` records measured available space before and
after cleanup. Source captures and editable callouts remain in the repository.
