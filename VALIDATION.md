# Observed validation — editable diagrams, 12 November 2026

Live book: <https://icg-cpd-cluster.port.ac.uk/python-phd/>.
Teaching/build revision: `805c416478b7922204f721ae19f7b611abe1c0cf` on
`xangma/jupyter_data_languages`, branch `codex/phd-python-2026`.
Later validation-only commits do not change those teaching/build inputs.

## Implementation

Eight explanatory diagrams accompany the agreed teaching points:

- Session 1: a shared row mask; row-wise broadcasting; validity filtering and
  magnitude selection as separate decisions.
- Session 2: staged snapshots versus working edits; the actual two-branch README
  conflict; local commits, remote branches, fetching and hosted review.
- Session 3: client/model/tool execution and permission boundaries, using the
  Cline/CPD example; the human-led plan, authorise, repair and review loop.

Each has an editable DOT source, native SVG export, accessible title/description,
caption and editable-source link. `book/diagrams/README.md` documents editing;
`python scripts/render_diagrams.py` regenerates the exports and `--check` checks
freshness. Graphviz 13.1.2 was used for maintenance. Viewing requires only the
checked-in SVGs, with no extra student package or diagram service. SVG exports
fit within 720 by 640 CSS pixels while retaining scalable vector content.

Two bounded delegates authored the science/Git sources. The primary agent
reviewed the examples and every diagram in the actual book. A Graphviz nested
cluster/rank interaction was isolated before applying explicit global ranking;
all final sources render without warnings. Scientific notebook code, existing
cell IDs and empty source outputs are preserved. The instructor pacing file is
byte-for-byte unchanged, and student minute timings remain absent.

## Validation

- All eight DOT sources rendered; the export freshness check passed, including
  after the final book build. SVGs parse as native vector/text content with
  accessibility descriptions and no embedded raster images, scripts or
  foreignObject elements.
- All eight image paths resolve from both source and executed notebook locations.
  All five notebooks passed in fresh kernels/empty working directories. The
  strict 11-page build and five Hub notebook launch routes passed.
- All eight diagrams were visually reviewed at normal book reading width.
  Matrix indices and the agent boundary layout were refined from that review.
- On the deployed CPD pages, all eight images completed loading with positive
  natural/rendered dimensions, all eight editable-source links were present,
  and the three session pages had no horizontal overflow. The browser console
  query returned no errors. Live screenshots cover catalogue, Git and agent views.
- All eight deployed assets returned 200 with image/svg+xml. Their SHA-256 hashes
  matched the exact locally validated build assets.
- All three production Kustomize entrypoints rendered. The deployment PR passed
  all four required checks after incorporating current main.

This pass focused on diagram rendering and portability. It did not start or
restart student compute; the prior validation records the broader Hub workflow.

## Deployment

[PR 431](https://github.com/icg-innovation/space-k8s-gitops/pull/431) merged as
`8a6574bfb23a16a1132aee2131208a8cdea5bf85`. Flux `apps` applied that exact revision
and reported Ready. The book Deployment completed its rollout.

Static image:
`ghcr.io/icg-innovation/phd-python-jupyterbook@sha256:942e706ad94b87a91a05eb8894c7516c7932b96045f30a798c6c20c3a89d962e`.

This promotion changes the static book, retaining the existing notebook runtime
and Hub integration. Rollback restores the previous static image through GitOps;
preserve student PVCs.

The [previous validation](https://github.com/xangma/jupyter_data_languages/blob/ffd26f3/VALIDATION.md)
records student-facing timing removal and links the earlier authenticated
classroom checks.
