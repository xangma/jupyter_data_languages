# Instructor guide

The six-hour core consists of notebooks 01–03. Notebook 00 is prework; notebook
04 is an extension. Preserve the hands-on tasks and breaks if discussion runs
long. Open solutions after students attempt an exercise.

## Before class

Distribute the exact 2026 checkout and lockfile; the GitHub default branch is
older. Ask students to run the setup check and primer before Session 1.
Bring an installed environment, local data and a working preview. Avoid survey
downloads or installing a GW/ML stack in class.

Confirm one institution-approved coding agent per student/pair in advance:
Codex, Claude Code, Antigravity/agy or Cline with the CPD Qwen 3.8 27B route.
Use [tool setup](agent-tools.md) to prepare the practice workspace in one command;
the helper creates its files, committed starter and branch automatically. Verify
the client can edit that workspace and use its existing Python environment.
Confirm the effective permissions/sandbox and demonstrate pause, diff and undo.
Do not spend the session constructing a container or repeating Git initialisation.
Without an agent, use the saved incorrect proposal and a partner's review/repair.
The outcomes do not depend on a vendor or paid account. CPD provides a locked,
CPU-only course workspace through JupyterHub. Confirm student enrolment before
class and rehearse both in-page execution and opening the notebook in JupyterLab.

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

Expected issues: three missing velocities, one zero velocity error and one
missing magnitude, without overlap. A magnitude cut favours nearby objects.
This changes the distance distribution but need not bias the toy slope:
conditional on distance, selection is independent of velocity noise here.
Do not imply that every selection biases every estimator.

## Session 2 — 120 minutes

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–10 | Move a calculation to a function | Explain its input/output contract |
| 10–40 | Sandbox, status, diff, staging, commit; Task A | Passing test change on a branch |
| 40–60 | Resolve a same-line merge conflict | Retain both intended meanings |
| 60–70 | Break | |
| 70–95 | Known-answer tests; Task B | See an introduced bug fail |
| 95–110 | Environment, README, ignore rules; remote/PR demo | Explain reproducibility and review |
| 110–120 | Partner review and exit check | Show diff, tests and commit |

`scripts/create_practice_repo.py` refuses to overwrite an existing sandbox.
The angle helper starts correct. Students add independent tests, temporarily
introduce a bug, observe failures, restore the implementation and rerun.
The later equal/opposite-bearing tests belong to a fresh `edge-case-tests`
branch, committed before partner review. For optional hosting, use an empty
classroom repository and push `main` before that branch. A nonempty classroom
repository needs a clone with shared history. Offline review uses the same diff
and explanation. Research upstreams are reading examples.

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

Make the agent interaction the organising thread. Students inspect and critique
a plan, provide independently derived expectations, delegate test syntax, then
authorise a bounded repair. They should use their tool, not just watch a demo.
Keep prompts short enough for the CPD model route. A fresh chat needs the current
contract, diff and test evidence. Avoid suggesting that another model's agreement
establishes correctness. Reject unexplained edits to truth, data, errors or tests.
The starter returns only a mean; the reference helper also returns its standard
error. Preserving that interface is part of the exercise. Students derive their
own unequal-error, equal-error and 2-D rejection cases, review the agent's
`test_student_checks.py`, then checkpoint those tests before requesting a repair.
The agent edits only `weighted_mean.py` during repair. Both tests retain the agreed
expectations. The setup helper refuses an existing destination and leaves the
original intentionally wrong exercise unchanged. It uses a synthetic Git identity
local to the exercise, with no remotes. The same criteria apply to partner-only work.

An agent's scope prompt is not enforced isolation. Explain the tool's sandbox,
approval settings and recovery checkpoints separately. Some in-scope commands
run automatically: accept a truthful account of that rather than require a
fabricated permission prompt. Cline's inference on CPD does not relocate its
client's file/terminal tools. The approved model connection is still needed
even when agent shell downloads and extra services are out of scope.

The fitting/residual/error-rescaling cells remain as a worked optional scientific
verification example after the core activity. They no longer consume the opening
20 minutes. Sessions 1 and 2 and the overall three two-hour structure are unchanged.

## Assessment and adaptations

Each student/pair submits a rerunnable analysis with a caption and selection,
an independently justified test, a reviewed commit and an AI-use record.
Ask: what are the units, why is the expected answer correct, what did the agent
change, and which scientific assumption is still untested? Passing-test
screenshots alone are insufficient.

Pair novices on arrays and omit optional remote pushing if needed. Experienced
students can vary the cut or run multiple-seed recovery simulations; distinguish
one successful recovery from a coverage study. The FFT extension supports GW
interests. Keep HPC infrastructure in its separate teaching.
