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

## Pedagogical, visual and 3-route agent revamp — 14 November 2026

Reviewed all eleven pages, five notebooks, diagrams and screenshot overlays for
incoming first-year astrophysics PhD students spanning both observational and
theoretical projects and mixed computing backgrounds.

- **Concept → visual → example → scaffolded task flow**: Restructured `setup.md`
  into browser-first CPD (`Option A`, including `source /opt/course/.venv/bin/activate`
  and cropped Hub/kernel guides) versus local `uv`/`venv` (`Option B`). Added
  theorist and observer bridges, `pprint_all()` inspection, explicit 3-band flux
  broadcasting, scaffolded student task cells, progressive `{dropdown}` hints and
  worked answers in `solutions.md`, balanced theoretical/observational tracks in
  `further-reading.md`, and scannable session tables in `instructor.md`.
- **Twelve editable concept diagrams**: Added `array-views`, `fits-vs-ecsv`,
  `git-undo-vs-revert` and `nyquist-aliasing` (plus two-panel time/FFT figure in
  `04-signal-extension.ipynb`), and refined `shared-mask`, `agent-architecture`
  and `agent-review-loop`.
- **Sleeker lossless screenshot crops**: Extended `scripts/render_screenshot_callouts.py`
  with optional `"crop": [cx, cy, cw, ch]` SVG `viewBox` + `<clipPath>` framing
  and bounds checks (`tests/test_screenshot_callouts.py`), zooming key UI regions
  and stripping personal IDE chrome while keeping embedded `.jpg`/`.png` bytes
  untouched across all 52 annotated overlays.
- **Session 2 rebalance (`02-git-and-tests.ipynb`)**: Reduced total Markdown prose
  by ~36% (~40% along a single editor route) by trimming triple-repeated screenshot
  captions, folding troubleshooting and the optional GitHub PR walkthrough into
  `{dropdown}` blocks, moving `git-remotes.svg` into the Remotes section, adding
  `git-undo-vs-revert.svg`, and expanding uninterrupted `pytest` coverage
  (`pytest.approx`, `pytest.raises`, failure tracebacks, and 1D wraparound versus
  2D spherical separation).
- **Focused 3-tab Session 3 (`agent-tools.md`, `03-agents-and-inference.ipynb`)**:
  Placed `agent-tools.md` immediately before Session 3 in `myst.yml`, streamlined
  the six-tool tab sets to three synchronized GUI routes (`Jupyter AI on CPD`,
  `Cline + CPD Qwen`, `Claude Code`) with a compact control-mapping table for
  Codex, Antigravity and OpenCode Desktop, recorded `sys.executable` in generated
  `TASK.md`, added `claude-repair-approval.svg` and a concrete steering contrast,
  and removed raw internal CI harness cells from student view.

## Session 1 & Primer audit against `CKrawczyk` — 15 November 2026

Audited the Jupyter Book's Python lessons (`01-catalogue.ipynb` and `00-primer.ipynb`)
against Coleman Krawczyk's (`CKrawczyk`) original `master` notebooks
(`General_Python.ipynb`, `General_plotting.ipynb`, `Uncertainty_plotting.ipynb`,
`Fits_images.ipynb`, `mpl_style.py`) and 2025's `1.1 - Environments_and_Conda.ipynb`,
leaving all legacy notebooks untouched:

- **`pip`, `conda` and `uv` opening section in Session 1 (`01-catalogue.ipynb`)**:
  Added a concise opening section, comparison table, `sys.executable` check,
  scientific-stack overview (`QTable` vs `pandas.DataFrame`), and editable diagram
  `python-environments.svg` contrasting `pip + venv`, hash-locked `uv` (`uv.lock`),
  and `conda`/`mamba` (`conda-forge` C/Fortran/CUDA astronomy libraries) alongside
  the Jupyter kernel vs unactivated terminal shell boundary.
- **Essential scientific Python, Astropy, FITS & Matplotlib additions (`01-catalogue.ipynb`)**:
  Added `astropy.constants` ($R_s = 2 G M_\odot / c^2$) and spectral/Doppler
  `equivalencies` (`u.spectral()`, `u.doppler_optical`), 2D `axis=0` vs `axis=1`
  reductions, a 2-panel 2D FITS `WCS` cutout + residual figure (`origin='lower'`,
  `AsinhStretch` sequential `magma` vs zero-centred `RdBu_r` `CenteredNorm`),
  inward journal ticks, a 2-panel `errorbar` + `fill_between` and inverted-magnitude
  selection-plane figure (`ax.invert_yaxis()`), `fig.savefig` (`.pdf` vs `.png`,
  noting `rasterized=True` / `hexbin` for $\ge 10^5$ points), and a velocity-residual
  diagnostic task.
- **Core Python & 2D array idioms (`00-primer.ipynb`)**: Added `array-axes-slicing.svg`
  (bringing the course total to **fourteen** editable diagrams), `tuple` unpacking,
  stride/reverse slicing (`[::2]`, `[::-1]`), formatted `f-strings`, attributes vs
  methods, 2D indexing and `axis=0`/`axis=1` reductions, `enumerate`/`zip`/list
  comprehensions, `with` cleanup, and a starter `fig, ax = plt.subplots()` plot.

## Three-model review & dependency-solving refinement of Session 1 — 16 November 2026

Refined `book/01-catalogue.ipynb`, `book/solutions.md`, `book/instructor.md` and
`book/setup.md` following independent pedagogical and technical reviews across
three models (`Gemini Pro`, `Codex gpt-6-astra`, `Claude Opus 5.5`) plus explicit
coverage of dependency solving:

- **Dependency solving & scannable opening (`env-kernels`)**: Explained how
  package constraint graphs are solved by full-graph lockfile resolvers (`uv` +
  `uv.lock` and `conda`/`mamba`'s `libmamba` SAT solver across Python + compiled
  C/Fortran/CUDA libraries) versus ad-hoc `pip install`, noted `%pip` and `uv`'s
  `pip`-free default `.venv` alongside hidden out-of-order notebook state, and
  moved the 4-column tool reference table into a `{dropdown}`.
- **Cohesive catalogue thread & protected 120-minute pacing**: Added explicit
  units and uniform-baseline caveats on the mock Hubble relation, 4 learning
  objectives, `clean = table[valid]` `QTable` slicing alongside sentinel-value
  warnings, a 5-line $\chi^2(H_0)$ parameter-grid broadcast `(201, 1) * (395,)`
  replacing the disconnected 3-band toy array, `1 / H0` unit algebra with
  `u.allclose`, preserved `<=8`-character FITS provenance cards (`SYNTH`, `SEED`,
  `H0_INJ`) before Task B, and badged the constants/equivalencies and 2D FITS WCS
  cells as optional pre-break spotlights (`layout='constrained'`, sparse asinh
  colorbar ticks).
- **Honest uncertainty & unspoiled Task C discovery**: Added faint background
  scatter of all 395 valid rows behind `[::8]` error bars, labelled the shaded
  band explicitly as $\pm\text{median }\sigma_v$ data scatter, wrote persistent
  `.pdf`/`.png` exports to `outputs/`, placed legends on both selection-histogram
  panels, removed pre-answered Task C numbers from preceding prose and Task A's
  worked answer, and aligned `solutions.md`, `instructor.md` and `setup.md`.
- **Self-contained book cleanup**: Moved *Environments and kernels: pip, conda and
  uv* (including dependency solving and `python-environments.svg`) into the
  opening of `book/00-primer.ipynb` so Session 1 (`01-catalogue.ipynb`) starts
  directly on the galaxy catalogue, removed `book/instructor.md` from the book
  and TOC, and stripped inline workshop-pacing, break and partner/manual-pair cues
  across all sessions and reference pages so every page reads as self-contained
  material.
- **Cluster-independent general tutorial**: Removed CPD-specific setup, paths and
  model references across `book/` and `README.md`, restructured `setup.md` around
  reproducible local `uv` and standard `venv`/`conda` workflows, generalised
  Session 2's JupyterLab tabs to `JupyterLab`, and replaced CPD-bound Session 3
  tabs with general `Claude Code`, `Codex`, and `Cline` (any OpenAI-compatible or
  local Ollama/`llama.cpp` model) routes while keeping optional JupyterHub build
  and deployment scripts intact.
- **Hover-over glossary & gentler beginner/theorist framing (`myst.yml`, `00-primer`, `01-catalogue`)**:
  Added 36 interactive `project.abbreviations` hover-card explainers in `myst.yml`
  for Python, packaging, NumPy, Astropy, and astronomy terms; replaced dense
  packaging/survey jargon in `00-primer.ipynb` and `01-catalogue.ipynb` with
  plain-English 1-line bullets and explicit bridges for inflation, gravitational-wave,
  and numerical-simulation PhD students while reducing markdown word count in
  both notebooks.
