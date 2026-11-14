# Instructor guide

Notebooks `01`–`03` form the six-hour taught core; `00-primer` is pre-course
preparation and `04-signal-extension` is an optional post-course extension.
Protect hands-on task blocks and breaks when discussion runs long, and direct
students to the visible hints in [Hints and worked answers](solutions.md) before
opening full dropdown solutions.

## Before class

- **Environment & CPD readiness:** Distribute the locked 2026 checkout and
  `uv.lock` (the upstream default branch is legacy material). Confirm CPD
  JupyterHub enrolment (**Python PhD (locked)** kernel; standard CPU server
  suffices) and remind students to run `source /opt/course/.venv/bin/activate` in
  every new CPD terminal. Avoid live survey downloads or installing GW/ML stacks
  during class.
- **Coding-agent routes:** Confirm one graphical route per student or pair before
  Session 3 using [Choose your coding agent](agent-tools.md):
  1. **Jupyter AI on CPD** — recommended zero-install default (browser UI +
     OpenCode + `cpd/qwen3.8` hosted together on CPD).
  2. **Cline + CPD Qwen** — free local VS Code route (`https://icg-cpd-cluster.port.ac.uk/v1`,
     model `qwen3-8-27b-mtp-ud-q4-k-xl`, distinct from `cpd/qwen3.8`; file and
     terminal tools run on the laptop).
  3. **Claude Code** — commercial editor/desktop route (`Plan` $\rightarrow$
     `Manual` modes with pre-configured accounts).
  Students bringing Codex, Antigravity or OpenCode Desktop map controls via the
  reference table in [Choose your coding agent](agent-tools.md); pairs without
  agent access use the first-class manual pair route. Running
  `python scripts/create_agent_practice.py outputs/agent-practice` copies the
  starter files, writes the active course Python interpreter path into `TASK.md`,
  commits `main` and switches to `agent-repair`.

## Session 1 — 120 minutes

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–10 | Inspect the catalogue | Identify units and error columns |
| 10–40 | Arrays, masks, broadcasting; Task A | Explain a shared mask and 395 usable rows |
| 40–60 | Quantities and FITS round-trip; Task B | Distinguish metadata from numbers |
| 60–70 | Break | |
| 70–95 | Error-bar plot | Label units and define uncertainty |
| 95–115 | Survey selection; Task C | Compare distributions with common bins |
| 115–120 | Exit check | Explain one claim the figure cannot support |

### Key Pitfalls

- Filtering columns separately instead of applying one shared `valid` mask (five
  disjoint bad rows—three missing velocities, one zero error, one missing
  magnitude—leave 395 usable rows).
- Stripping units blindly with `.value` instead of `.to_value(u.Mpc)`, or
  forgetting `[:, None]` when broadcasting a 1-D per-object scale `(N,)` across
  `(N, 3)`.
- Claiming every survey cut biases every fit: here `apparent_magnitude < 16.5`
  (262 objects) alters the distance distribution without selecting on velocity
  noise at fixed distance.

### 3-Command Terminal/Repo Triage

```bash
pwd
git rev-parse --show-toplevel
python -c "import sys; print(sys.executable)"
```

Confirm `pwd` and the Git top-level directory match the 2026 course checkout
containing `data/mock_galaxies.ecsv`, and `sys.executable` points to
`/opt/course/.venv/bin/python` on CPD (or the local `.venv`).

### Novice Minimum Path

Pair on array indexing; complete the shared `valid` mask (395 rows), the FITS
round-trip `.to_value(u.Mpc)` check, the subsampled error-bar figure, and a
three-sentence caption for the `16.5` magnitude cut.

### Fast-Finisher Stretch

Compare selected counts across `15.5` (161), `16.5` (262) and `17.5` (357), add
finite-range and header assertions to the FITS check, and specify which physical
effects (distance errors, Malmquist bias, correlated peculiar velocities) would
bias a real Hubble-flow slope.

## Session 2 — 120 minutes

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–15 | Why Git; Git/GitHub/VS Code; working tree, index, commit | Distinguish saving, staging, committing and sharing |
| 15–40 | First commit; GUI mapping; branch and Task A | Explain one file appearing in both change lists |
| 40–60 | Resolve a same-line merge conflict | Retain both intended meanings |
| 60–70 | Break | |
| 70–95 | Bare practice remote; private reset; shared revert and clone | Retain work after reset; collaborator receives a revert |
| 95–110 | Function interface; known-answer tests; Task B and handoff | See an introduced bug fail and restore only that implementation edit |
| 110–120 | Partner review and exit check | Show diff, tests and commit |

### Key Pitfalls

- Running `git init`, commits or resets inside the parent course checkout rather
  than `outputs/git-practice`, or assuming CPD JupyterLab files sync with a
  laptop VS Code folder.
- Expecting plain `git diff` to display untracked files, or forgetting that VS
  Code **Complete Merge** and JupyterLab **Mark as resolved** stage the file
  without creating the final merge commit.
- Using VS Code **Undo Last Commit** (`reset --soft`) on a commit already pushed
  to `practice`; demonstrate the pushed mistake on the remote *before* running
  `git revert` and inspecting `partner-practice`.

### 3-Command Terminal/Repo Triage

```bash
pwd
git rev-parse --show-toplevel
python -c "import sys; print(sys.executable)"
```

Verify `git rev-parse --show-toplevel` ends in `outputs/git-practice` (never the
parent course repository) and `sys.executable` uses the active course
environment before running `python -m pytest -q`.

### Novice Minimum Path

Complete `git init -b main`, the initial commit, Task A staging comparison,
instructor-led conflict resolution, account-free `practice` remote recovery
(`reset --soft` vs `revert`), and Task B equal/opposite bearing tests with local
diff review—omitting optional GitHub remote setup.

### Fast-Finisher Stretch

Add floating-point wraparound checks using `pytest.approx(0.2)`, work through
the rejected-push merge recovery, and push `main` + `edge-case-tests` to an
empty personal classroom repository on GitHub for a hosted pull-request review.

## Session 3 — 120 minutes

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–15 | Locate model, client, workspace and controls | Distinguish sandbox, approval and checkpoint |
| 15–35 | Agent inspection and plan; failing baseline | Review its diagnosis, contract and proposed scope |
| 35–60 | Derive expectations; delegate and review test syntax | Explain 1.2, 2.8 and a student-chosen case; checkpoint tests |
| 60–70 | Break | |
| 70–95 | Authorise repair; observe tools and steer | Explain one real edit, command or permission decision |
| 95–110 | Independently rerun and review the diff | Tests unchanged; known-answer evidence; reject a false fix |
| 110–120 | Accept repair and write AI-use record | Reviewed commit and scientific explanation |

### Key Pitfalls

- Agent subprocesses invoking system Python instead of the course interpreter
  recorded in `TASK.md` (`/opt/course/.venv/bin/python` on CPD).
- Treating a Git branch, `.venv`, Plan mode or prompt instruction as an enforced
  OS sandbox, or forgetting that Cline's CPD Qwen route still edits files and
  runs commands on the laptop.
- Accepting weakened or edited tests (`1.2` $\rightarrow$ `1.5`), relying on
  equal-error checks that cannot distinguish $1/\sigma$ from $1/\sigma^2$, or
  substituting the `(mean, uncertainty)` tuple from `course2026.analysis`.

### 3-Command Terminal/Repo Triage

```bash
pwd
git rev-parse --show-toplevel
python -c "import sys; print(sys.executable)"
```

Confirm `git rev-parse --show-toplevel` resolves to `outputs/agent-practice` on
branch `agent-repair`, and `sys.executable` matches the `Course Python
interpreter:` line recorded in `TASK.md`.

### Novice Minimum Path

Use **Jupyter AI on CPD** (or the manual pair route) through the four core
gates: inspect & critique the plan, derive one unequal-error test and commit
`TESTS_COMMIT`, authorise and steer a single-file repair of `weighted_mean.py`
(restoring tests with `git checkout "$TESTS_COMMIT" -- test_weighted_mean.py test_student_checks.py`
if touched), verify with `pytest -q` and `git diff`, and record the 5-line
`AI_USE.md`.

### Fast-Finisher Stretch

Run the optional `mock_galaxies.ecsv` weighted `curve_fit` cells, verify the
$2\sigma$ uncertainty doubling and $\chi^2/4$ scaling, test how Session 1's
`apparent_magnitude < 16.5` cut narrows the distance lever arm and widens
$\sigma_a$, or explore FFT resolution, leakage and aliasing in `04-signal-extension.ipynb`.

## Assessment and sign-off

Each student or pair finishes with a rerunnable Session 1 plot and caption, a
committed Session 2 test branch, and a verified Session 3 repair with
`AI_USE.md`. Ask four check questions rather than accepting passing-test
screenshots alone: **What are the units? Why is your expected answer right? What
did the diff actually change? Which physical assumption remains untested?**
