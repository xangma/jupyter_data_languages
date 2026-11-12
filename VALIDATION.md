# Observed validation — agent-focused Session 3, 12 November 2026

Live [Session 3](https://icg-cpd-cluster.port.ac.uk/python-phd/agents-and-inference/)
and [tool setup](https://icg-cpd-cluster.port.ac.uk/python-phd/agent-tools/).
Teaching/build revision: `6a824076f96f331959b08a92208e761195c7ef58`, on
`xangma/jupyter_data_languages`, branch `codex/phd-python-2026`.
Later validation-only commits do not change those teaching/build inputs.

## Implementation

The 120-minute lesson now centres on using an agent: identify client/model and
execution location; inspect built-in controls; supply context and review a plan;
derive expectations and delegate test syntax; authorise a bounded repair;
steer from evidence; independently rerun/review; accept and account for the work.
The ten-minute break remains at 60–70 minutes. The course still has three two-hour
sessions. The other four notebooks are unchanged; fitting is retained as an
optional worked verification example after the agent practical.

One preparation command creates the practice files, committed starter and
`agent-repair` branch. Its synthetic identity is local to that repository, with
no remotes. Existing destinations are refused. The lesson explains enforced
sandboxing, approvals and Git recovery separately, using existing tool controls
rather than manual sandbox construction.

The tool guide covers Codex, Claude Code, Antigravity/agy and Cline with CPD Qwen
3.8 27B. Two bounded subagents advised on curriculum and verified official tool
documentation. Codex/Claude/agy command flags were also checked against local CLI
help. The CPD endpoint/model alias was checked against the serving configuration;
Flux subsequently reported applied source `640e02e5c096f8357cb783700889344881214387`
Ready. No model-generation request or live four-vendor account comparison was
performed in this pass. The guide links primary documentation and notes that
client versions and institutional policies affect effective controls.

## Tests and observed practice

- **24 course tests passed**, including four preparation cases: independent Git
  root/branch/clean starter/no remotes; refusal preserving student edits; existing
  file/directory protection; and missing Git leaving no partial workspace.
- **All five notebooks passed in fresh kernels and empty working directories**.
  Session 3 retains six executable code cells. Source outputs remain empty and
  all original cell IDs are preserved. The retained fitting plot was inspected
  with its explicit assumed-exact distance label.
- The strict MyST build passed with the immutable compatible theme: 11 pages,
  five CPD notebook launch routes, and the existing hydration/cold-start checks.
  The rendered lesson opening, timetable and tool table were reviewed.
- The prepared-workspace practical was rehearsed locally and using
  `/opt/course/.venv/bin/python` in the actual existing Python PhD Hub server.
  The starter produced **nine failures**; independently derived student checks
  produced **11 failures and one pass**; the published scalar repair produced
  **12 passes**. Both test files and the course starter retained their hashes.
  Repeating preparation refused the used directory, preserving the repair.
  The practice repository ended clean on `agent-repair`, with no remotes.
- This rehearsal used the documented partner/saved-solution route, explicitly
  recorded as such. The chosen additional example was `[0, 10]` with errors
  `[1, 2]`, deriving `(10/4)/(1 + 1/4) = 2.0` independently.

The Hub rehearsal retained its practice repository, AI-use record and summary in
`~/jupyter_data_languages/outputs/agent-lesson-20261112-6a824076`, alongside
`agent-lesson-20261112-6a824076-summary.json` and its workflow log. The temporary
course clone and transferred script were removed. The server was already active
when used; this run issued no start, stop or restart commands. At the final
snapshot there were no single-user pods and its 20 GiB home PVC remained Bound.
No inference call, fresh enrolment/sign-in flow or Windows run was tested here;
the prior deployment record contains the broader authenticated workflow and
persistence checks.

## Deployment and live checks

[PR 426](https://github.com/icg-innovation/space-k8s-gitops/pull/426) incorporated
current main, passed all four required checks and merged as
`7846bd86d101160d57232756fc5d6669d1def367`. All three production Kustomize
entrypoints rendered. Flux `apps` applied that exact revision and reported Ready;
the book Deployment successfully rolled out.

- Static image: `ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:c943aec060911d6ad1d145483042684995ca9af76888ddeb8167933fe6d793fe`
- Notebook runtime retained: `ghcr.io/icg-innovation/phd-python-notebook@sha256:b703527a678c9ef7d2be931c7f500fe1c8c76f091a217235448a383c6fa6e3ca`

The live lesson displayed the new timed agent sequence. Its tool-guide link
opened the deployed page with all four routes and the CPD endpoint; the browser
console query returned no errors. Anonymous lesson, guide and UKSA-book access
returned 200; anonymous kernel-proxy access returned 401. The Hub integration
and runtime configuration were unchanged by this content promotion.

Rollback restores the prior static image digest through GitOps while preserving
student PVCs. The [11 November validation](https://github.com/xangma/jupyter_data_languages/blob/4e3dd0fb6885bd45ae57b7947f52aae294f7f433/VALIDATION.md)
records the previous independent-review changes and authenticated end-to-end
workflow. `COURSE_REVIEW.md` records the rationale for this teaching revision.
