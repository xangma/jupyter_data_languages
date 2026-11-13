# Validation — complete GUI screenshot walkthroughs

Checked 13 November 2026 on `codex/phd-python-2026`.
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

Static-image promotion and live CPD/JupyterLab validation are in progress.
The notebook runtime and existing student server will be retained.

## Evidence

`evidence/screenshot-completion-20261113/` in the task workspace contains build
logs, browser image inventories, independent test records and capture provenance.
Raw captures and editable manifests remain in `book/screenshots/`.
