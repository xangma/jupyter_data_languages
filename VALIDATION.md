# Observed validation — reviewed course, 11 November 2026

## Implementation and deployment

Live book: <https://icg-cpd-cluster.port.ac.uk/python-phd/>.
Course branch: `xangma/jupyter_data_languages`, `codex/phd-python-2026`.
Reviewed content/build revision: `b7b5f096afe4dc337640e0b427c8a0d04fcc248a`.
Later validation-only commits do not change those teaching/build inputs.

The five agreed revisions are implemented: the Git branch/commit and optional
remote sequence; setup and environment commands; a non-overwriting agent
sandbox with independently authored tests; clearer scientific assumptions and
recomputed error-rescaling checks; and an executable FFT aliasing task. Small
primer, instructor and solution clarifications support those changes.
All three 120-minute sessions and ten-minute breaks retain their original times.
The selected-only refit remains optional; untested timetable changes were not adopted.

GitOps [PR 422](https://github.com/icg-innovation/space-k8s-gitops/pull/422)
passed all four required checks and was merged as
`70ebf461d52520b99146080101834d080c1b7d17`. Flux `apps` applied that exact
revision and reported Ready; the book Deployment reached one updated, ready replica.

Pinned images:

- Book: `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:33c21b0d7e1060b0505f652803b3346cd4b5eb6d96738482393e6473fd370e71`
- Runtime: `ghcr.io/icg-innovation/phd-python-notebook@sha256:b703527a678c9ef7d2be931c7f500fe1c8c76f091a217235448a383c6fa6e3ca`

The runtime, bridge and Hub configuration are unchanged. A fresh build exposed
an implicit book-theme v2.0.0 upgrade from its floating download. `myst.yml` now
pins compatible v1.4.1 commit `23f2df5493e23dfb1d9433c8aa64c87beb4232a3`.
The strict build, existing bounded Thebe patch and actual auto-start script
regression all pass with that immutable template.

## Tests and student workflow observed on CPD

The flow was exercised as the admitted user `xangma`, with a fresh book-service
connection using the existing Hub sign-in session. A newly enrolled student's
account was not available. No paid coding-agent account is needed for the tested
classroom route.

- The stopped named server started through one compute-button action. Its
  runtime was the pinned image above, using the default scheduler, requesting
  1 CPU / 1 GiB and limiting 4 CPU / 8 GiB, with no GPU resources. The separate
  20 GiB `longhorn-retain` home PVC stayed Bound.
- nbgitpuller incorporated the reviewed content while preserving the existing
  notebook outputs through a local merge. The reviewed content commit was
  verified as an ancestor of the student checkout; no hard reset was used.
- In-page outputs were cleared and recomputed. Session 3 recovered slope/intercept
  70.05/303.77, recomputed reduced chi-squared as 0.24 after doubling errors,
  and observed the expected nine starter-test failures. Session 1 reproduced
  400 rows, 395 usable, 262 selected, a 395-row FITS round trip and mean distances
  110.7/87.5 Mpc. Its error-bar and selection plots were visually inspected.
- Open Notebook opened editable `book/03-agents-and-inference.ipynb` in the
  named server's JupyterLab. Restart and Run All executed all six code cells
  with zero errors; the saved notebook reopened with those outputs after restart.
- A new JupyterLab terminal selected `/opt/course/.venv/bin/python` (Python
  3.13.18). Setup printed 395 usable rows out of 400. The documented pip
  inspection command, **23 course tests**, and **all five notebooks** in fresh
  kernels/empty working directories passed inside that actual workspace.
- The Git practical completed branch creation, independent tests, deliberate
  conflict/resolution, the new `edge-case-tests` commit, review and noninteractive
  revert. Five sandbox tests passed. Optional hosting was checked with an empty
  local bare remote, both branches pushed and a nonempty review diff; no hosted
  practice PR or upstream push was made.
- The offline agent exercise observed failure before repair, committed the
  independently derived student checks, applied the published scalar solution,
  passed **12 tests**, and confirmed both test files unchanged during repair.
  Repeating setup refused the existing sandbox and preserved the student's edits.
  Both practice repositories finished clean; the source starter remained wrong.
- A further fresh Hub kernel ran the 300 Hz FFT variation and produced a visible
  **212 Hz** peak on the full 0–256 Hz plot, with its sampling-theory check passing.
- The server was stopped through Hub Home, its pod disappeared and its PVC
  remained Bound. Starting through the book produced a different pod UID. Three
  persisted evidence files retained their SHA-256 checksums, and the saved
  six-cell notebook still had no errors. The test server was stopped again after
  this check; student files and evidence remain in its retained home.
- Anonymous book access returned **200**; the anonymous kernel proxy returned
  **401**; the existing UKSA book returned **200**.

The book console recorded no errors during computation. Two transient reconnect
warnings were observed during bootstrap/navigation; subsequent fresh cell runs
completed successfully. Windows shell guidance was reviewed but not executed on
Windows in this pass.

## Local and promotion checks

Local macOS validation also passed 23 course tests, all five fresh-kernel
notebooks, both practicals (including the nested course-directory layout), and
FFT 40/40.3/300 Hz variants. Notebook cell IDs, empty source outputs, timed
headings and the instructor timetable were checked and preserved.

93 targeted Hub/registry tests passed against the pinned Hub chart. All three
production Kustomize entrypoints rendered. The full registry policy passed with
36 workloads, 48 images, 25 private images, 19 pull-secret references and ten
sealed registry Secrets, including the exact pinned private Llama source.

Detailed live logs, the executed 300 Hz notebook/figure, practical repositories,
AI-use record and persistence marker are retained in the student's workspace:
`~/jupyter_data_languages/outputs/review-deploy-20261111-b7b5f09/`.

The [initial deployment record](https://github.com/xangma/jupyter_data_languages/blob/90ef6d55c2c0b23a61a9ca4eaf8b178c158717f2/VALIDATION.md)
records PRs 416–421 and the earlier integration repairs. `COURSE_REVIEW.md`
records provenance and the independent reviews; `deploy/README.md` describes
builds, promotion and rollback. Revert the GitOps image promotion for rollback;
preserve student PVCs.
