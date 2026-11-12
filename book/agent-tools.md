# Choose your coding agent

Prepare **one** approved tool before Session 3; pairs can share. Use an existing
account or the CPD model route. Installation, accounts and model downloads belong
before class. Without access, use the saved proposal in the lesson and work with
a partner; record that route honestly.

## Prepare the practice workspace

In the active course environment, from the course root, run:

```bash
python scripts/create_agent_practice.py outputs/agent-practice
```

This prepares the files, a committed starter and an `agent-repair` branch, using
a synthetic Git identity local to this exercise. It adds no remote and refuses
an existing destination. For a repeat attempt choose a new name. Open the
**printed directory** as the agent's workspace, rather than the whole course
or your home directory. Use your existing environment in its terminal; do not
install another one during the task.

The preparation command saves classroom time. The resulting directory and Git
branch are recovery aids, not a security boundary. Choose the tool's existing
permissions and, where available, enforced sandbox. If that is unavailable,
use the instructor's prepared environment with reviewed actions.

## Controls for your tool

Labels vary with version and institutional policy. Check the effective settings
in your installation; planning and action approval are distinct from OS isolation.
Use the same prompts and acceptance criteria with every tool.

| Tool | Inspect and plan first | Authorise the bounded edit |
| --- | --- | --- |
| **Codex** | Open the practice directory. In CLI use `codex --sandbox read-only --ask-for-approval on-request`; inspect `/permissions`. | After agreeing the plan, choose workspace write in `/permissions` (CLI launch: `codex --sandbox workspace-write --ask-for-approval on-request`). Commands inside that boundary can run automatically; review requests to expand access. [Official permissions guide](https://learn.chatgpt.com/docs/agent-approvals-security). |
| **Claude Code** | Open the practice directory; CLI: `claude --permission-mode plan`. Check `/permissions`. | Choose manual edit approval when leaving Plan (CLI launch: `claude --permission-mode default`). Existing allow rules affect prompts; its shell sandbox is a separate control. [Permission modes](https://code.claude.com/docs/en/permission-modes), [permissions](https://code.claude.com/docs/en/permissions). |
| **Antigravity / agy** | CLI: `agy --mode=plan`; inspect `/permissions` and the active workspace. | Use the CLI's `default` execution mode for reviewed edits/commands. Its terminal sandbox is separate (`--sandbox` or the sandbox setting). Desktop permission presets have different names: inspect the actual controls. [CLI modes](https://antigravity.google/docs/cli/modes), [agent settings](https://antigravity.google/docs/agent-settings). |
| **Cline**, including CPD Qwen | Open the practice folder in VS Code. Begin in **Plan**. | Switch to **Act** after reviewing the plan. Keep **Auto Approve** and **YOLO** off for this exercise. Checkpoints help compare/restore files; they do not enforce process isolation. [Plan/Act](https://docs.cline.bot/core-workflows/plan-and-act), [approvals](https://docs.cline.bot/features/auto-approve), [checkpoints](https://docs.cline.bot/core-workflows/checkpoints). |

For each route, inspect the sandbox supplied by the tool or instructor and keep
extra filesystem/network access subject to review. A prompt such as “edit only
one file” communicates scope; it does not itself enforce a filesystem boundary.

## Cline with Qwen 3.8 27B on CPD

In Cline's settings choose **OpenAI Compatible**. The course route uses:

| Setting | Value |
| --- | --- |
| Base URL | `https://icg-cpd-cluster.port.ac.uk/v1` |
| Model ID | `qwen3.8` (the CPD Qwen 3.8 27B route) |
| API key / access | Use the instructor's current access instructions; keep credentials in the provider settings. |

Confirm access before class; the shared service may need time to start. Use the
instructor's model capability settings rather than guessing context limits.
See Cline's [provider fields](https://docs.cline.bot/provider-config/openai-compatible).

**Locate both machines:** the model's inference runs on CPD; Cline's file edits
and terminal tools run where its VS Code workspace/client runs. A laptop Cline
session with a CPD model can still change laptop files. Connecting to the model
does not move the workspace into JupyterHub or create a local sandbox.

If your agent runs locally, use a local course checkout. If you use an approved
remote editor, check which host owns its terminal and files. JupyterHub notebook
compute alone does not supply all four agent clients. The exercise forbids
agent-initiated downloads and extra services; the approved model connection
still needs network access.
