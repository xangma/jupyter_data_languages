# Git session screenshots

These are actual captures of the built-in Git interface in Microsoft Visual
Studio Code 1.141.0 on macOS, made on 13 November 2026. They show a disposable
copy of the Session 2 bearing exercise, with synthetic author identity
`PhD Student <student@example.org>` and no credentials or research data.
Third-party extensions were temporarily disabled in the capture window.
Window layout and font size were adjusted for reading in the book; no controls,
code or history were fabricated or composited.

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
