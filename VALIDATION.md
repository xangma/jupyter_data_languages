# Observed validation — student-facing timings, 12 November 2026

Live book: <https://icg-cpd-cluster.port.ac.uk/python-phd/>.
Teaching/build revision: `5f691dba6e663beb9ade34bbb1a240ed55d1d00a` on
`xangma/jupyter_data_languages`, branch `codex/phd-python-2026`.
Later validation-only commits do not change the teaching/build inputs.

## Implementation

Removed section time ranges, task durations and minute-based session/break
labels from all five current notebooks. The overview also omits pacing details.
Breaks and the learning sequence remain. All notebook code and cell IDs are
unchanged. The instructor guide is byte-for-byte unchanged, retaining its full
three-session/six-hour pacing tables.

## Validation

- Source and staged notebook comparisons confirmed unchanged code and IDs.
  Generated notebook Markdown contains no minute timings.
- All five notebooks executed successfully in fresh kernels and empty working
  directories. The strict 11-page book build and five Hub launch routes passed.
- All three production Kustomize entrypoints rendered. The deployment PR passed
  all four required checks.
- Live browser checks confirmed untimed section/task headings in Sessions 1–3.
  The instructor page still showed its Minutes column and 60–70 break rows.
  The final student view was visually checked and captured.

## Deployment

[PR 428](https://github.com/icg-innovation/space-k8s-gitops/pull/428) merged as
`7cd4cdf86be525c109d3e2c475215618ce7a4b40`. Flux `apps` applied that exact revision
and reported Ready. The book Deployment reached one updated, ready, available
replica and completed its rollout.

Static image:
`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:64df446ff35586c3aa00b678fdcbe76bdb977b9543995eb867bf04335c50282c`.

This promotion changes the static book only. The locked runtime and Hub
configuration retain their existing settings. Restore the previous static image
through GitOps for rollback; preserve student PVCs.

The [prior validation](https://github.com/xangma/jupyter_data_languages/blob/85421300a573385a355e717d55aeda6e0db59e5f/VALIDATION.md)
records the agent-focused lesson revision and its broader classroom checks.
