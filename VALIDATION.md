# Observed validation — 10 November 2026

## Implementation

The isolated branch `codex/phd-python-2026` preserves the latest local drafts in
baseline commit `f9c3ee3`, followed by the 2026 course. The original checkout and
both GitHub repositories remain unchanged. `COURSE_REVIEW.md` records provenance
and the assessment recommendations adopted.

## Tests and execution

- Locked Python 3.13.7 environment: setup check passed. NumPy 2.5.4, SciPy 1.18.1,
  Astropy 8.0.2, Matplotlib 3.11.2 and pytest 9.2.0.
- Reference suite: **17 passed**. Checks include independent weighted-mean
  answers, invalid inputs, exact-line recovery, compatible/incompatible units,
  catalogue selection and injected-parameter recovery.
- All **five notebooks** executed in separate fresh Python 3.13.7 kernels with
  empty working directories; no unexpected cell errors. Source outputs are empty;
  checked executed copies feed the book.
- The catalogue has 400 rows, 395 usable, 262 passing the magnitude-16.5 cut.
  Fitted slope/intercept: about 70.05 and 303.77, compared with injected 70 and 300;
  formal standard errors about 0.36 and 45.36 under the declared mock assumptions.
- Git practical rehearsed in a temporary local repository: baseline, branch,
  test addition, deliberate same-line merge conflict, resolution and revert.
  Existing-sandbox overwrite refusal also checked.
- Agent exercise: unmodified starter failed; the published scalar solution
  passed the unchanged acceptance tests. This is exercise validation, not a
  claim to have tested any particular external coding agent.

## Book and container

- MyST 1.12.0 with Node 22.23.2: strict HTML build passed for ten pages.
  An initial Node 20.10.0 build failed because MyST uses `Dirent.parentPath`;
  selecting the documented Node 22 runtime resolved it. `.nvmrc` and package
  engine requirements make the runtime explicit.
- Static HTML check: 370 local prefixed references, none missing.
- Executed selection, fit/residual and FFT figure PNGs were visually inspected;
  axes, labels and plotted results were readable.
- Local Docker image built successfully from the checked HTML and pinned Nginx
  base. HTTP 200 observed for `/healthz`, `/python-phd/` and all three core chapter
  URLs under `/python-phd/`. The temporary review container was stopped afterward.
- Browser visual/navigation/search QA was **not completed**: local browser use
  is disabled in Work settings. Perform it before publication. The figure PNGs
  from execution are available separately in the workspace evidence directory.

## Deployment

No CPD deployment, live-kernel integration, GitOps change, remote push or PR was
performed. `/python-phd/` is the prepared route, not a verified live CPD endpoint.
The deployment handoff includes the required live and browser checks and rollback
procedure. Historical notebooks are retained outside the validated 2026 path.
