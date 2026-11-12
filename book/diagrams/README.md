# Editable teaching diagrams

Each `.dot` file is the editable text source for the matching `.svg` diagram.
Edit labels, examples, nodes and connections there, then regenerate from the
course root:

```bash
python scripts/render_diagrams.py
python scripts/render_diagrams.py --check
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
| `shared-mask.dot` | Session 1: Arrays, shapes and masks |
| `broadcasting.dot` | Session 1: beside the row-scaling example |
| `catalogue-selection.dot` | Session 1: Investigate a survey selection |
| `git-states.dot` | Session 2: before staging and committing |
| `git-branches.dot` | Session 2: Merge and resolve a conflict |
| `git-remotes.dot` | Session 2: Optional hosting exercise |
| `agent-architecture.dot` | Session 3: Know what your agent can do |
| `agent-review-loop.dot` | Session 3: Supply context and review a plan |

Keep labels short enough to read in a notebook/book column. Use labels and
shapes as well as colour. Match the actual file, branch, array-shape and catalogue
examples in the lesson. After an edit, check the rendered diagram at reading
size and the SVG's notebook link. The shared palette uses dark ink on a white
canvas, blue for human/input context, purple for stored state/client mediation,
amber for proposals/decisions, and green for checked results.
