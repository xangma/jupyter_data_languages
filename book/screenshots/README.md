# Git session screenshots

These are actual captures of the built-in Git interface in Microsoft Visual
Studio Code 1.141.0 on macOS, made on 13 November 2026. They show a disposable
copy of the Session 2 bearing exercise, with synthetic author identity
`PhD Student <student@example.org>` and no credentials or research data.
Third-party extensions were temporarily disabled in the capture window.
Window layout and font size were adjusted for reading in the book; no controls,
code or history were fabricated or composited. The six beginner figures add
numbered vector annotations over the unchanged captures, as described below.

| File | Captured state |
| --- | --- |
| `vscode-staging.png` | `test_wraparound` staged, then `test_full_turns` added without restaging; staged diff selected |
| `vscode-conflict.png` | README descriptions from `description-a` and `description-b` conflict; actual merge editor before resolution |
| `vscode-undo.png` | Git: Undo Last Commit applied to the latest unpublished ordinary commit; README work remains staged |
| `vscode-revert.png` | Mistake and revert both in history; `practice/recovery-lab` updated to the revert |

Recreate these states by following the notebook in order. Use a separate
practice folder: its creator refuses an existing destination. The `practice`
remote is a separate bare repository on disk, so screenshots and the remote
recovery exercise need no hosted account. Commit IDs and dates will differ.

For an updated capture, use the current built-in Source Control view and check
its named actions against [the official guide](https://code.visualstudio.com/docs/sourcecontrol/overview).
Keep meaningful alt text and a nearby explanation when replacing a screenshot.
The lesson's conceptual diagrams remain editable in [../diagrams](../diagrams/README.md).

## Beginner walkthrough and editable callouts

The six `vscode-basics-*.jpg` files are additional, unchanged native captures
from the same VS Code version, platform and date above. The capture API supplied
JPEG bytes at 2366 × 1676 pixels. Their names retain the actual encoding.
The matching `.svg` files embed those exact bytes and add editable numbered
circles and leader lines; these are the versions displayed in the lesson.

| Capture and annotated figure (same stem) | State and lesson placement |
| --- | --- |
| `vscode-basics-workspace` | Explorer, editor, Source Control icon, integrated terminal and branch indicator; VS Code introduction |
| `vscode-basics-untracked` | Four saved, untracked starter files and Stage Changes; first-commit visual recap |
| `vscode-basics-staged` | Four staged files, Unstage Changes, message and Commit; first-commit visual recap |
| `vscode-basics-committed` | Empty pending Changes, first commit with its recorded files, and real clean `git status`; first-commit visual recap |
| `vscode-basics-branch` | Actual branch picker after creating `test-wraparound`; both names at the same commit; immediately after the branch commands |
| `vscode-basics-diff` | Saved, unstaged wraparound test, M marker, added lines and Stage Changes; immediately before testing and staging in Task A |

The branch was created and the first commit recorded through the built-in Git
UI. The wraparound test was added and saved in the editor. State was checked
against Git directly. Graph's historical A markers describe files in the
selected commit; they are separate from pending Changes.

Edit labels and pixel coordinates in [callouts.json](callouts.json), then run
from the course root using its locked environment (Pillow comes with Matplotlib):

```bash
uv run --frozen python scripts/render_screenshot_callouts.py
uv run --frozen python scripts/render_screenshot_callouts.py --check
```

Alternatively edit the numbered groups in an SVG editor; update the manifest to
retain those edits when regenerating. The `original-capture` image is unchanged;
`editable-callouts` contains the overlay. Each SVG has a title and text description,
and each lesson figure has meaningful alt text and a nearby numbered caption.
Use short leaders that leave the demonstrated controls and text visible. Replace
both capture and coordinates when changing interface layout or screenshot size.

## JupyterLab on CPD and synchronized interface tabs

The ten `jupyterlab-git-*.jpg` files are real browser captures from CPD's
standard CPU workspace on 13 November 2026: JupyterLab 4.5.11,
`jupyterlab-git` 0.51.1, nbdime 4.0.2 and `jupyterlab-myst` 2.7.0.
They use an independent copy of the same bearing exercise and the same
synthetic author identity. No extension installation is needed on CPD.
The viewport was unchanged. Seven captures omit unused space on the right
(1100 × 860); the two diffs and merge editor retain both/all panes
(1682 × 860). No interface elements were fabricated or composited.

| Capture and annotated figure (same stem) | State |
| --- | --- |
| `jupyterlab-git-workspace` | File Browser, editor, Git sidebar, Git menu and current branch |
| `jupyterlab-git-untracked` | Four new files under Untracked, U markers and Track all untracked files |
| `jupyterlab-git-staged` | Four files selected in Staged, Unstage, Summary and Commit |
| `jupyterlab-git-committed` | First locally recorded commit in History |
| `jupyterlab-git-branch` | New Branch and two branch names at the same initial commit |
| `jupyterlab-git-diff` | HEAD versus WORKING; saved wraparound edit before staging |
| `jupyterlab-git-staging` | HEAD versus INDEX; one file in Staged and Changed, only wraparound staged |
| `jupyterlab-git-conflict` | Actual three-pane README merge editor before resolution |
| `jupyterlab-git-undo` | Soft reset in JupyterLab Terminal; original work retained staged |
| `jupyterlab-git-revert` | Revert, original mistake, updated practice remote and passing tests |

The first commits, branch creation, staging/unstaging, merge resolution and
merge commit were exercised through the Git UI. Recovery commands ran in the
JupyterLab Terminal; **Git → Push to Remote** sent the tested revert to the
account-free bare remote. A fresh collaborator clone confirmed both the
corrected README and preserved history. **Mark as resolved** saves and stages
the merge result; it does not create the repository's merge commit.

The matching SVGs embed the exact JPEGs with editable vector annotations.
`callout_scale` in the manifest adjusts annotation size for the capture;
coordinates remain in source pixels. The rendering commands above cover both
interfaces.

Edit each walkthrough directly in the notebook's Markdown cells. Each native
MyST `tab-set` has `Git commands`, `VS Code` and `JupyterLab on CPD` items with
matching `:sync:` keys (`git-command`, `vscode`, `jupyterlab`). Keep a complete
set in one cell. [MyST's tab documentation](https://mystmd.org/guide/dropdowns-cards-and-tabs#tabs)
describes synchronization. These tabs also render inside CPD's MyST-enabled
JupyterLab notebooks. The book synchronizes across all ten sets; JupyterLab's
renderer synchronizes within a Markdown cell, so select the interface again in
the next cell. Students perform each action once in their chosen
interface; common setup and test commands sit outside the alternatives.


## Lecture 3: Jupyter AI review

`jupyter-ai-review.jpg` is a real 1682 × 908 CPD browser capture made on
13 November 2026, with Jupyter AI 3.2.0 and OpenCode 1.18.34 using the prepared
`cpd/qwen3.8` model. It shows the proposed new `test_student_checks.py` in the
isolated weighted-mean exercise, before one-time approval. The numbers were
independently derived and supplied in the prompt; the agent drafted test syntax.
No controls, file contents or model output were fabricated or composited.
The SVG embeds the unchanged JPEG and adds the manifest's editable callouts.
The viewport was unchanged. No credentials or private research data are shown.

The named-file read, new test-file write, focused tests and subsequent repair
are real tool actions with one-time decisions in the classroom validation.
The lesson keeps the scientific acceptance criteria common to all six routes.
