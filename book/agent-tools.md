# Choose your coding agent

Prepare **one** approved route before Session 3; pairs can share. Installation,
accounts, provider access and model downloads belong **before class**. Use an
already available model. Without access, use the lesson's saved proposal with a
partner and record that route honestly.

## Prepare the practice workspace

In a CPD JupyterLab **Terminal**, activate the prepared environment:

```bash
source /opt/course/.venv/bin/activate
```

Locally, activate your existing course environment. From the **course root**, run
the same preparation command for every tool:

```bash
python scripts/create_agent_practice.py outputs/agent-practice
```

This prepares `TASK.md`, `weighted_mean.py` and `test_weighted_mean.py`, commits the
starter and creates `agent-repair`, with a synthetic Git identity local to this
exercise. It adds no remote and refuses an existing destination; choose a fresh
name for a repeat. Open the **printed directory** as the workspace. Keep the
existing Python environment; install nothing during the lesson.

## Controls for your tool

Checked **13 November 2026**. Labels and institutional settings vary; inspect your
actual controls. CPD's prepared image has OpenCode **1.18.34** and Jupyter AI
**3.2.0**; it does not supply Codex, Claude Code or agy. Those routes need a
client prepared elsewhere before class. OpenCode **V1** and **V2** have different
commands; use the linked V1 documentation for this CPD image. Sidebar labels can
also vary with the installed Jupyter extensions.

`````{tab-set}
````{tab-item} Codex
:sync: agent-codex

Open the printed directory in your prepared Codex client. For CLI, change to that
directory and start:

```bash
codex --sandbox read-only --ask-for-approval on-request
```

Use an existing available model. Inspect `/permissions`; send the lesson's
inspection prompt. After agreeing the plan, select workspace write there, or
relaunch with `--sandbox workspace-write --ask-for-approval on-request`.
Workspace edits and commands can then run automatically; inspect requests for
extra access. `/diff` shows changes. Use the session's interrupt control before
correcting scope. Read-only/workspace-write are enforced sandbox settings;
on-request controls approvals. [Official permissions guide](https://learn.chatgpt.com/docs/agent-approvals-security).
````

````{tab-item} Claude Code
:sync: agent-claude

In Desktop's **Code** tab choose a local environment and the practice folder;
select **Plan** below the prompt. Or change to that folder in a terminal:

```bash
claude --permission-mode plan
```

Inspect `/permissions`. At plan approval choose **Yes, manually approve edits**;
Desktop's execution mode is **Manual** (CLI: `--permission-mode manual`). Review
each requested edit/command and its scope. Existing allow rules affect prompts.
Review `/diff` and `Ctrl+O` tool details, or Desktop's **Changes** pane. `Esc`
interrupts CLI; Desktop has a stop button. `/resume` recovers a session. The
separate `/sandbox` control contains shell commands where supported; Plan and
Manual alone do not. [Modes](https://code.claude.com/docs/en/permission-modes),
[sandbox](https://code.claude.com/docs/en/sandboxing),
[Desktop](https://code.claude.com/docs/en/desktop).
````

````{tab-item} agy
:sync: agent-agy

In the practice directory, start `agy --mode=plan`; add `--sandbox` only where
the prepared installation supports its terminal sandbox. Inspect `/permissions`.
After plan review, use `/config` → **Agent Mode** → **default** for individual
edit review; do not assume the startup default. Inspect the inline diff before
**Yes, accept this change**; `f` expands it. `/diff` reviews changes and `Ctrl+O`
expands tool details. `Esc` interrupts work; explicitly reject a pending edit.
`agy --continue` resumes.

Desktop: **New Project** → **Add Folder** → practice folder → **Create**;
choose **Local mode**. Submit `/plan …`, review, then **Proceed**; **Review**
opens diffs. Desktop presets differ from CLI modes: **Request Review** asks
about commands with sandbox off; **Default** uses its sandbox.
[CLI modes](https://antigravity.google/docs/cli/modes),
[Desktop settings](https://antigravity.google/docs/agent-settings).
````

````{tab-item} Cline + Qwen
:sync: agent-cline

Open the practice folder in VS Code. In Cline settings select **OpenAI Compatible**:

| Setting | Course value |
| --- | --- |
| Base URL | `https://icg-cpd-cluster.port.ac.uk/v1` |
| Model ID | `qwen3.8` (CPD Qwen 3.8 27B) |
| Access | Instructor's current credentials, kept in provider settings |

Confirm access and capability settings before class. Start in **Plan**; switch
to **Act** only after review. Keep **Auto Approve** and **YOLO** off. Inspect
proposed diffs and terminal results before approving the next action; checkpoints
help recover edits. Inference runs on CPD, but files and terminal commands belong
to the machine hosting your VS Code workspace. A laptop client can edit laptop
files. Approvals/checkpoints do not create an OS sandbox.
[Provider](https://docs.cline.bot/provider-config/openai-compatible),
[Plan/Act](https://docs.cline.bot/core-workflows/plan-and-act),
[approvals](https://docs.cline.bot/features/auto-approve).
````

````{tab-item} OpenCode
:sync: agent-opencode

In the prepared CPD Terminal, activate the course environment, change to the
printed practice directory and run:

```bash
opencode --agent plan
```

Reuse the prepared **cpd/qwen3.8** provider/model; no public-provider account or
new API key is needed. Check the active directory, model and **Plan** indicator.
After reviewing the plan, press **Tab** to select **Build**. Keep the prepared
tool permissions on **ask**; approve individual bounded edits/commands after
reading their diffs/results. Plan/Build and permission prompts are not an OS
shell sandbox. Inspect the resulting files and `git diff` in the practice
terminal. [V1 agents](https://opencode.ai/v1/docs/agents/),
[V1 permissions](https://opencode.ai/v1/docs/permissions/).
````

````{tab-item} Jupyter AI
:sync: agent-jupyterai

In CPD JupyterLab, open the **Jupyter Chat** sidebar and choose **New chat**. Select the prepared **OpenCode**
persona in the input toolbar. After it connects, the toolbar shows the CPD Qwen
model and session mode (for example **build**); expand **More controls** if needed. This is a front end to the same OpenCode agent
and **cpd/qwen3.8** model, connected through ACP; it is not a separate model.

Attach `TASK.md`, `weighted_mean.py` and `test_weighted_mean.py` from the practice
directory, or give their paths relative to the Jupyter server root. Check the
agent's working directory and available mode/permission controls before sending
the inspection prompt. Keep tool requests subject to review; use **Allow once** for a bounded request
or **Reject** when scope is unclear. Read each edit diff and command result; verify files and tests in the practice terminal. Reopen the
saved chat to resume. If only chat is available, request a proposed patch, review
and apply it yourself, and record that fallback.
[Jupyter AI agent chat](https://jupyter-ai.readthedocs.io/en/latest/users/chat/index.html).
````
`````

Use the same lesson prompts, phase checkpoints and acceptance criteria whichever
tab you choose. The Git branch and practice folder aid recovery; they are not a
security boundary. A request to “edit only one file” communicates scope without
enforcing it. Keep extra filesystem/network access subject to review; the
approved model connection still needs network access. Run the final tests yourself
in the practice directory using the active course environment.
