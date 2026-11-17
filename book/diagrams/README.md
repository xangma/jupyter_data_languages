# Editable teaching diagrams

Each `.dot` file is the editable text source for the matching `.svg` diagram.
Edit labels, examples, nodes and connections there, then regenerate from the
course root:

```bash
uv run --frozen python scripts/render_diagrams.py
uv run --frozen python scripts/render_diagrams.py --check
```

Rendering requires [Graphviz](https://graphviz.org/download/), tested with
13.1.2. The notebooks and published book use the checked-in SVGs, so students
do not need Graphviz or a live diagram service. The SVGs also remain editable
vector graphics, with selectable text, accessible titles and descriptions.
Exports fit within 720 by 640 CSS pixels while retaining their scalable viewBox.
`diagrams.json` holds those descriptions. The native
[SVG output](https://graphviz.org/docs/outputs/svg/) preserves text and shapes.

| Source | Placement |
| --- | --- |
| `python-environments.dot` | Primer: Dependency solvers (`uv`, `pip + venv`, `conda / mamba`) and aligned kernel/shell execution |
| `array-axes-slicing.dot` | Primer: 0-based and negative indexing, half-open slices and 2D `axis` reductions |
| `array-views.dot` | Primer: Slice views versus independent `.copy()` buffers |
| `shared-mask.dot` | Session 1: Arrays, shapes and masks (including separate-mask misalignment trap) |
| `broadcasting.dot` | Session 1: 2D broadcasting `(M, 1) * (1, N)` and `axis=1` reduction for $\chi^2(H_0)$ |
| `catalogue-selection.dot` | Session 1: Investigate a survey selection |
| `fits-vs-ecsv.dot` | Session 1: Saving tables with units and metadata (ECSV vs FITS HDUs) |
| `nyquist-aliasing.dot` | Optional extension: Spectral analysis and Nyquist folding / aliasing |
| `git-zones-lifecycle.dot` | Session 2: Four places work lives (Working tree, Staging index, Local `.git` history, Remote) |
| `git-states.dot` | Session 2: Staging captures a point-in-time snapshot (`git diff` vs `git diff --staged`) |
| `git-merge-types.dot` | Session 2: Fast-forward pointer move versus three-way merge commit |
| `git-branches.dot` | Session 2: Merge conflict pause and scientific resolution |
| `git-remotes.dot` | Session 2: Synchronising via `clone`, `fetch`, `pull` and `push` (and rejected pushes) |
| `git-undo-vs-revert.dot` | Session 2: Private `git reset --soft` vs shared `git revert` |
| `git-clone-fork-pr.dot` | Session 2: Team repository versus open-source Fork and Pull Request workflow |
| `agent-architecture.dot` | Session 3: Know what your agent can do |
| `agent-review-loop.dot` | Session 3: Supply context, commit the tests checkpoint and review repairs |

Keep labels short enough to read in a notebook/book column. Use labels and
shapes as well as colour. Match the actual file, branch, array-shape and catalogue
examples in the lesson. After an edit, check the rendered diagram at reading
size and the SVG's notebook link. The shared palette uses dark ink on a white
canvas, blue for human/input context, purple for stored state/client mediation,
amber for proposals/decisions, green for checked results, and soft red for
errors or rejected items.
