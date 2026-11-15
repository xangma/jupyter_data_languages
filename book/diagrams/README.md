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
| `array-axes-slicing.dot` | Primer: 0-based and negative indexing, half-open slices and 2D `axis` reductions |
| `array-views.dot` | Primer: Slice views versus independent `.copy()` buffers |
| `python-environments.dot` | Session 1: Python environment tools (`uv`, `pip + venv`, `conda / mamba`) and aligned kernel/terminal execution |
| `shared-mask.dot` | Session 1: Arrays, shapes and masks (including separate-mask misalignment trap) |
| `broadcasting.dot` | Session 1: beside the row-scaling example |
| `catalogue-selection.dot` | Session 1: Investigate a survey selection |
| `fits-vs-ecsv.dot` | Session 1: Saving tables with units and metadata (ECSV vs FITS HDUs) |
| `nyquist-aliasing.dot` | Optional extension: Spectral analysis and Nyquist folding / aliasing |
| `git-states.dot` | Session 2: before staging and committing |
| `git-branches.dot` | Session 2: Merge and resolve a conflict |
| `git-undo-vs-revert.dot` | Session 2: Private `git reset --soft` vs shared `git revert` |
| `git-remotes.dot` | Session 2: Optional hosting exercise |
| `agent-architecture.dot` | Session 3: Know what your agent can do |
| `agent-review-loop.dot` | Session 3: Supply context, commit the tests checkpoint and review repairs |

Keep labels short enough to read in a notebook/book column. Use labels and
shapes as well as colour. Match the actual file, branch, array-shape and catalogue
examples in the lesson. After an edit, check the rendered diagram at reading
size and the SVG's notebook link. The shared palette uses dark ink on a white
canvas, blue for human/input context, purple for stored state/client mediation,
amber for proposals/decisions, green for checked results, and soft red for
errors or rejected items.
