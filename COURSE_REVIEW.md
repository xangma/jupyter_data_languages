# Lecture review and 2026 update

## Source found

Checked GitHub on 9 November 2026. The remembered user is `CKrawczyk`
(Coleman Krawczyk), source `jupyter_data_languages`. Upstream and Xan's default
`master` point to `8a8c2469bf54af664d4e5ab656419e2328d8be92`. Xan's newer
`update_2025` points to `2e4201b3f2e596b351f3178f94ec480ed9dc35f6`.
The local checkout also had edited plotting notebooks and unpublished class 3,
scripts, configuration and utilities. These are preserved in baseline commit
`f9c3ee3` in an isolated worktree; the original checkout was not edited.

The [shared assessment](https://chatgpt.com/share/6af1b459-121c-83ed-ad3b-cd0e3beb5cd5?ogimg=plain)
was read in the browser. Its research examples are a purposive sample, not a
census. This update adopts its pedagogical ideas without presenting its
student-by-student claims as a newly verified literature review. Portsmouth's
October 2026 handbook AI guidance was checked directly.

## Adopted ideas

| Assessment idea or gap | Change |
| --- | --- |
| Shared research workflow | One small catalogue for selection, plotting, tests and parameter recovery |
| Explicit array teaching | Shapes, aligned masks, broadcasting, NaNs and views/copies |
| Astronomy data and units | Quantities, ECSV metadata and an offline FITS round-trip |
| Independent scientific validation | Known answers, exact-line/unit checks, injection recovery, residuals and error rescaling |
| Hands-on Git | Local sandbox, staging, branches, conflict, review, revert and optional classroom PR |
| Coding agents with scientific control | Failing weighted mean, hand-derived 1.2/2.8 tests, bounded edits and diff review |
| Mixed student experience | Primer, tasks, hints, answers and a no-account agent fallback |
| Reproducibility | Installable package, lockfile, setup check, reference tests and fresh kernels |
| Six-hour limit | Three 120-minute sessions with breaks; advanced material/HPC outside core |
| JupyterBook destination | MyST/Jupyter Book 2, checked executed content, subpath build and container preparation |

## Corrections and limits

The old README referenced moved files; the new entry point is explicit. The old
requirements file's Python docstring is corrected to a comment. Historical
environments remain separate from the minimal 2026 core.

The local debugging draft imported a nonexistent `utils.logging_helpers` and
guessed units from numeric ranges before scaling/interpolating missing values.
The new core uses declared units, a reported mask and explicit assumptions.
Historical drafts remain outside the validated book and are labelled accordingly.

The weighted-mean starter returns a scalar; the reference returns mean and standard
error. The contracts and invalid inputs are explicit. A changed sample distribution
is not automatically a biased estimator; one recovery does not establish coverage.
We do not repeat the assessment's research-example claims without new evidence.

The 2026 package, five notebooks, Git workflow and static book are the verification
targets. Historical notebooks and the live CPD cluster are outside that boundary.
No live resource, GitOps source, remote branch or PR is changed. See
`VALIDATION.md` for observed checks and `deploy/README.md` for the publishing handoff.

## Independent content reviews — 11 November 2026

Three independent CLI reviews used GPT-6 Astra/Max, Claude Fable 5.2/Max and
Gemini 4 Carbon High. Each received the same 19-file course snapshot, mixed
incoming-PhD audience, learning outcomes and six-hour constraint. Their findings
were checked against the source; workflow issues were reproduced before editing.

The resulting revision completes the Git branch/commit and optional remote
sequence, corrects setup/environment commands, protects the agent sandbox and
student-owned acceptance tests, clarifies distance/noise assumptions and checks
error rescaling directly, and repairs the FFT aliasing task. The primer and
worked answers received small supporting clarifications. All session timings
and breaks are preserved. Timing reallocations require a classroom rehearsal;
the selected-only refit remains an optional teaching idea.

A fresh build also exposed an implicit upgrade to book-theme v2.0.0. The site now
pins the compatible v1.4.1 template commit; its CPD integration remains explicit.
See `VALIDATION.md` for the revision's build, deployment and student-workflow evidence.
## Session 3 refocus — 12 November 2026

Following the instructor's feedback, Session 3 now centres on operating coding
agents: locating client/model/tool execution, inspecting built-in permissions
and sandboxing, supplying context, reviewing a plan, delegating test syntax from
independently derived expectations, authorising a bounded repair, steering from
evidence and accepting a reviewed change. It supports Codex, Claude Code,
Antigravity/agy and Cline with CPD Qwen 3.8 27B; a partner/saved-proposal route
remains available. Two bounded Codex subagents advised on the teaching sequence
and verified vendor controls; they did not modify the repository or deploy.

Preparation is one command. The helper creates the practice files, local Git
starter commit and repair branch without global identity changes or remotes,
and continues to refuse an existing destination. The lesson distinguishes this
practice workspace and recovery history from an enforced security sandbox.
Students inspect their existing tool/instructor-provided boundary rather than
constructing one manually. The agent can draft tests, but students derive and
agree the expected answers before a checkpoint and keep the tests fixed during
repair. A CPD model connection does not relocate a local Cline client's tools.

The timed agent lesson remains 120 minutes with the 60–70 minute break. Its
previous opening fitting example is retained after the core as optional worked
scientific verification. Sessions 1 and 2 are unchanged. The new tool reference
links official documentation checked on 12 November; actual controls may vary
by client version and institutional policy. CPD base URL/model alias were checked
against the applied serving-source configuration, not inferred from a model name.

## Session 2 foundations and recovery — 13 November 2026

Reviewed the current session against Coleman Krawczyk's original `Git.ipynb`,
the instructor's Medium example and GeeksforGeeks topic index, and current Git
and VS Code primary documentation. Two bounded read-only subagents advised on
beginner sequencing and the built-in VS Code interface; the parent checked
material behaviours in a real exercise repository before writing the lesson.

The session now introduces Git, GitHub and VS Code separately, then builds the
working tree/index/commit/branch model before the first commands. First-commit
blocks have expected observations. Task A makes the two versions of a partially
staged file visible. Four authentic VS Code screenshots show staging, a merge
conflict, a private soft-reset undo and a pushed revert. Core Git support does
not depend on a third-party editor extension or a hosted account.

An account-free bare remote supports a shared mistake, revert, normal push and
independent collaborator clone. Private recovery retains a rescue branch and
staged work. Restore, reset and revert are distinguished, including restore's
default index source and the ordinary-commit restriction of the examples.
Troubleshooting covers directory/identity/staging mistakes, blocked switches,
rejected pushes, conflicts, ignore rules and reflog recovery. Hosted PR setup
remains optional; force-push and merge-revert recipes remain advanced references.

The earlier lecture's explicit setup/help and research motivation were useful.
The Medium article's `git push master` is not adopted as shorthand for
`git push origin master`: the first positional argument is a repository.
The topic index informed coverage, rather than expanding the core to every
advanced command. Technical behaviours are checked against the primary manuals.

The six-hour structure and breaks remain. Session 2's instructor pacing now
allocates time to foundations and recovery; function/test demonstrations are
shorter and later. Student content contains no minute-by-minute timings. The
angle-helper tests, independent expectations and reproducible handoff remain.
