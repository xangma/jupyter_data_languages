# Observed validation — 11 November 2026

## Implementation and deployment

The course is published at <https://icg-cpd-cluster.port.ac.uk/python-phd/>.
Its source is `xangma/jupyter_data_languages`, branch `codex/phd-python-2026`.
The original local 2025 drafts remain preserved in baseline commit `f9c3ee3`;
`COURSE_REVIEW.md` records provenance and the assessment recommendations adopted.

CPD deployment and fixes were promoted through `space-k8s-gitops` PRs
[416](https://github.com/icg-innovation/space-k8s-gitops/pull/416),
[417](https://github.com/icg-innovation/space-k8s-gitops/pull/417),
[418](https://github.com/icg-innovation/space-k8s-gitops/pull/418),
[419](https://github.com/icg-innovation/space-k8s-gitops/pull/419),
[420](https://github.com/icg-innovation/space-k8s-gitops/pull/420) and
[421](https://github.com/icg-innovation/space-k8s-gitops/pull/421).
The final application revision is `38ae7f547de86155afe80b7d5f02189ac2d6bb73`.
The Hub reached Helm release v55 (chart 4.3.5).

The PhD bridge reuses the UKSA implementation with separate user-scoped OAuth
and a named `python-phd` server. The observed pod uses the default scheduler,
requests 1 CPU / 1 GiB, limits 4 CPU / 8 GiB, and requests no GPU. Its home is a
separate Bound 20 GiB `longhorn-retain` PVC. Existing Hub admission rules apply.

Pinned images:

- Book: `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:e1c7d14379509bbb41f9c6223b1d4635ee5ca91ad1a7ed8fda06945cdd6943b1`
- Runtime: `ghcr.io/icg-innovation/phd-python-notebook@sha256:b703527a678c9ef7d2be931c7f500fe1c8c76f091a217235448a383c6fa6e3ca`

## Tests and student execution

- 20 course tests passed inside the actual Hub environment: Python 3.13.18,
  NumPy 2.5.4, SciPy 1.18.1, Astropy 8.0.2, Matplotlib 3.11.2, pytest 9.2.0.
- All five notebooks passed in fresh Hub kernels with empty working directories.
  This includes catalogue/FITS/plots, Git reference tests, inference/agent
  acceptance checks and the optional signal exercise.
- GitHub sign-in and the book's OAuth connection were exercised as `xangma`.
  This verifies the normal user-scoped bridge flow using the operator's admitted
  account; a newly enrolled student's account was not available for this test.
- In-page computation was activated from a stopped named server. After clearing
  the saved outputs, Run All produced 400 rows, 395 usable, 262 selected, and a
  395-row FITS round trip. The selection means were 110.7 and 87.5 Mpc.
- Open Notebook targeted the editable `book/` source on the named server.
  JupyterLab Restart and Run All passed, and its saved outputs survived a server
  restart. A Session 2 notebook also opened before starting in-page computation.
- A new JupyterLab terminal resolved `/opt/course/.venv/bin/python`; setup,
  pytest and the five-notebook check passed using the lecture's ordinary commands.
- The Git practical passed on CPD: branch, independent wraparound tests,
  deliberate conflict, resolution, commit and revert. The sandbox finished with
  a clean tree and no remote; no student-practice changes were pushed upstream.
- Anonymous book access returned 200; the anonymous kernel proxy returned 401.
  The existing UKSA book continued to return 200.

## Build and integration repairs

MyST 1.12.0 / Node 22.23.2 strict builds passed for ten pages and five notebook
routes. The Hub/service/profile suite passed 114 tests; the registry-policy suite
passed 29 tests. All three production Kustomize entrypoints and the complete
pinned private-source registry validation passed, as did required GitHub checks.

Live testing identified and repaired failures that local notebook execution alone
could not detect: the bridge now calls nbgitpuller's sync API and waits for its
finished event; compute startup retains a request made while Thebe loads;
readiness includes the notebook's own cells and session; login shells preserve
the locked Python PATH; Hub controls leave React-owned nodes in place.

`scripts/fix_thebe_cold_start.py` is a bounded compatibility patch for the pinned
theme. It fails the build if its vendor fragments change. Review it and rerun the
student workflow when upgrading MyST/Thebe rather than assuming compatibility.

The build also runs `scripts/check_hub_autostart.cjs`, which executes the actual
injected script before and after page hydration. It verifies that the launch
intent survives parsing and reaches the compute handler exactly once afterward.
Launch return URLs carry a build identifier to avoid cached preview HTML.

Final live UI checks passed on release `4cb54844dce4`: search returned the
weighted-mean material and navigated to Session 3; a fresh tab then navigated to
Session 1, launched compute once, cleared outputs and reran all cells without
console errors. The resulting error-bar plot was visually verified. The source
notebook opened in a fresh JupyterLab workspace. Disconnect/reconnect also passed.

The test named server was stopped through Hub Home. Its pod is gone and its
20 GiB home PVC remains Bound. The local preview was stopped too. The book tab
was left open; its status correctly shows the server stopped.
