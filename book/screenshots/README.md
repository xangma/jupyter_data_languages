# Teaching screenshots and editable callouts

The original Git captures show the built-in interface in Microsoft Visual
Studio Code 1.141.0 on macOS, made on 13 November 2026. They show a disposable
copy of the Session 2 bearing exercise, with synthetic author identity
`PhD Student <student@example.org>` and no credentials or research data.
Third-party extensions were temporarily disabled in the capture window.
Window layout and font size were adjusted for reading in the book; no controls,
code or history were fabricated or composited. Every displayed figure now has numbered vector annotations over its unchanged
capture. Later additions use the installed editor/desktop apps and CPD browser
interfaces, as documented below.

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

Edit labels and pixel coordinates in [callouts.json](callouts.json),
[legacy-callouts.json](legacy-callouts.json) or
[completion-callouts.json](completion-callouts.json), then run
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
JupyterLab notebooks. The book synchronizes across its interface tab sets; JupyterLab's
renderer synchronizes within a Markdown cell, so select the interface again in
the next cell. Students perform each action once in their chosen
interface; common setup and test commands sit outside the alternatives.


## Completed sharing and setup walkthroughs

These additional captures were made on 13 November 2026. The VS Code examples
use VS Code Insiders; JupyterLab uses the existing CPD Standard server and its
installed Git extension. New Git practice repositories use synthetic identities
`Classroom Researcher <classroom@example.invalid>` and
`Classroom Collaborator <partner@example.invalid>`.

| Capture stem | Actual state |
| --- | --- |
| `vscode-remote-controls` | Pull, Push and Fetch menu; Pull has created a merge, with zero incoming and two outgoing commits before Push |
| `vscode-push-rejected` | Real non-fast-forward rejection dialog; Show Command Output reveals Git's error |
| `jupyterlab-remote-controls` | Current repository/main branch and ordinary Pull/Push menu actions; no Fetch button is claimed |
| `jupyterlab-push-rejected` | Real rejected push and integration hint from the classroom bare remote |
| `jupyterlab-pull-merge` | Pull succeeded but left `MERGE_HEAD` and the collaborator file staged; review/test/Commit was still required |
| `github-pr-create` | Prepared title, purpose and local validation, `main` as base and `add-wraparound-test` as comparison |
| `github-pr-review` | Actual Files changed view of the new wraparound assertion; no review was requested from another person |
| `github-pr-merged` | The synthetic pull request merged into main; a local clone still needs fetching/pulling |
| `jupyterhub-signin` | Real unauthenticated GitHub sign-in page |
| `jupyterhub-workspaces` | Standard and Python PhD book entry points, plus separate-workspace/resource-change guidance |
| `jupyterlab-kernel-choice` | Python PhD (locked) selected for an isolated notebook; preferred-kernel setting unchecked |
| `cline-cpd-settings` | OpenAI Compatible, the CPD endpoint and the advertised Qwen model; access field masked by the app |

Both Git interfaces reproduced a rejected push. After integration, the bearing
checks passed and GUI Push updated the classroom remote. The JupyterLab case
required completing the staged merge before pushing; “Successfully pulled” did
not mean the merge commit had been recorded. A fresh collaborator check verified
the shared history. The GitHub screenshots use the private synthetic
`xangma/python-phd-git-example` repository, pull request 1, with two local tests
passing. Its Checks count of zero is not CI evidence or a correctness guarantee.

The kernel choice was applied only to the isolated capture notebook. A real cell
reported `/opt/course/.venv/bin/python` and computed `1 + 1 == 2`. The existing
Standard server was retained. The CPU/GPU launch form is conditional on a stopped
server; the workspace capture shows the actual entry points without stopping
Standard merely for a screenshot.

The four older `.png` sources contain JPEG bytes. Their names and bytes are
retained; their new SVG wrappers use the encoding detected from the image header.
The renderer also accepts genuine PNG captures and validates bounds, filenames,
MIME type and duplicate names. The overlay never replaces or invents UI content.

## Lecture 3: six graphical agent workflows

All captures use synthetic copies of the weighted-mean exercise. The agent
interface is a desktop app or editor panel. Commands visible in tool cards or
integrated terminals prepare/check the work; they are not agent CLI sessions.
Native window and browser capture sizes are retained.

| Route | Inspection/plan | Independent test file | Repair and result |
| --- | --- | --- | --- |
| Codex editor integration | `codex-editor-plan` | `codex-tests` | `codex-review` |
| Claude Code editor integration | `claude-editor-plan` | `claude-tests` | `claude-review` |
| Antigravity desktop | `antigravity-desktop-plan` | `antigravity-tests` | `antigravity-review` |
| Cline with CPD Qwen | `cline-editor-plan` | `cline-tests` | `cline-review` |
| OpenCode Desktop | `opencode-desktop-plan` | `opencode-tests` | `opencode-review` |
| CPD Jupyter AI/OpenCode | `jupyter-ai-plan` | `jupyter-ai-review` | `jupyter-ai-final-review` |

The numbers were independently derived and supplied in the prompts; agents
translated those criteria into test syntax. Each of the five native-agent
workspaces extended the original nine checks with three student checks:
11 failures/one pass against the broken starter, then 12 passing checks after
the bounded repair. Both test files were independently compared with their Git
tests checkpoint. Only `weighted_mean.py` changed during repair. Local captures
use a prepared `.venv` link to the existing course interpreter; that link is
capture preparation, not a step required in students' practice folders.

The Claude test-file and `claude-repair-approval` images show genuine pending
one-time write decisions. Cline's test-file preview likewise precedes Save.
Codex and OpenCode applied in-scope workspace edits before review; no imaginary
pre-edit approval gate is claimed. Antigravity's test capture is mid-task; its
later repair capture includes the actual result and Request Review preset.

Claude's first GUI attempt encountered an HTTPS connection failure; after the
user restored connectivity, the editor GUI completed the plan, test-file and
repair sequence. `claude-desktop-modes` is retained as an earlier setup-draft
capture, but the current lesson uses the completed editor workflow instead.

Cline's current captures use the real CPD public endpoint and
`qwen3-8-27b-mtp-ud-q4-k-xl`. Its earlier non-CPD planning capture was replaced.
The returned plan suggested a wrong test path; the lesson shows how to catch
and correct that before allowing execution. Plan-to-Act session rebuilding also
required a fresh task and a single explicit Send during capture. The final test capture includes an explicit `PYTEST_EXIT=0` after a tool-status
ambiguity; an independent subprocess also returned zero with 12 passing tests.
The original provider URL/model were restored after capture; no credential was
replaced. Automatic approvals remain None.
OpenCode Desktop's Big Pickle selection is an installed example, not an
inheritance of CPD's hosted settings.

Jupyter AI captures use JupyterLab 4.5.11, Jupyter AI 3.2.0 and OpenCode 1.18.34
with the prepared `cpd/qwen3.8` route. The test-file preview shows actual
Allow once/Reject controls. The final figure reopens the original saved
classroom conversation beside the native Git diff from tests checkpoint
`ac15c0debf947dd333e388753a3e63c94f341d59` to accepted repair
`f4970163fc39869c2a3c3aa95b7023832597699b`. It is a saved report, not a newly
executed chat turn. The exact Git bundle was restored in an isolated CPD folder
and independently rerun with 12 passing tests before publication. No model
response, tool result or file diff was fabricated or composited.

Each SVG embeds the exact original capture and exposes editable numbered groups
with an accessible title/description. Keep blank lines before Markdown images
so MyST renders them as block figures, and preserve the numbered caption and
full-size link. Lecture 3 uses `agent-codex`, `agent-claude`, `agent-agy`,
`agent-cline`, `agent-opencode` and `agent-jupyterai` synchronization keys. The
book synchronizes the three phases; JupyterLab may require selecting a tab
again in the next Markdown cell.
