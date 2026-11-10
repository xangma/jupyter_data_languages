# Instructor guide

The six-hour core consists of notebooks 01–03. Notebook 00 is prework; notebook
04 is an extension. Preserve the hands-on tasks and breaks if discussion runs
long. Open solutions after students attempt an exercise.

## Before class

Distribute the exact 2026 checkout and lockfile; the GitHub default branch is
older. Ask students to run the setup check and primer before Session 1.
Bring an installed environment, local data and a working preview. Avoid survey
downloads or installing a GW/ML stack in class.

Confirm an institution-approved coding agent in advance. Otherwise use the
incorrect candidate in notebook 03 and let students review/fix it themselves.
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
Keep hosted PRs in classroom repositories or students' own forks. Offline review
uses the same diff and explanation. Research upstreams are reading examples.

## Session 3 — 120 minutes

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–20 | Recover injected parameters; Task A | Discuss residuals and error rescaling |
| 20–40 | Agent inspection/test proposal demo | Bound files, commands and task |
| 40–60 | Derive weighted-mean tests; Task B | Calculate 1.2 and 2.8 independently |
| 60–70 | Break | |
| 70–105 | Repair a deliberately wrong function | Tests fail before, pass after |
| 105–120 | Review, rerun, commit, AI-use record | Explain assumptions without quoting the agent |

Do not generate the entire analysis before students understand the acceptance
tests. Reject unexplained edits to truth values, data, error bars or tests.
The starter returns only a mean; the reference helper also returns its standard
error. Preserving the requested interface is part of the exercise. Ask for an
equal-error test in addition to supplied unequal-error and invalid-input tests.

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
