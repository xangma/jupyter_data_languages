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
