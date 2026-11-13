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
