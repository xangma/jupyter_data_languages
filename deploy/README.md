# CPD deployment preparation

The proposed new endpoint is `https://icg-cpd-cluster.port.ac.uk/python-phd/`.
It is not an observed live endpoint. No cluster resource has changed; the
existing UKSA book at `/jupyterbook/` is a separate application.

## Build and local container check

Run the validation/build commands in the repository README, then from its root:

```bash
docker build -f deploy/Dockerfile -t icg-phd-python:2026-review .
docker run --rm --name icg-phd-python-preview -p 127.0.0.1:8085:8080 icg-phd-python:2026-review
```

Open `http://127.0.0.1:8085/python-phd/`. Check a deep chapter, figures, search,
navigation and `/healthz`. Stop with Ctrl+C or `docker stop icg-phd-python-preview`.
The container serves prebuilt checked HTML; it supplies no notebook kernel.
Nginx preserves `/python-phd` rather than depending on an ingress prefix rewrite.
The runtime base is pinned. For release, pin the published course image too. Retain
the source revision, both lockfiles, check logs and image digest together.
Rebuild HTML if the base path changes.

## Later GitOps change

Verify GlobalProtect and the CPD route, consult activity records, then do
read-only cluster checks. Reinspect current `space-k8s-gitops` default-branch
manifests and instructions in an isolated worktree. Its UKSA JupyterBook pattern
is a starting point; do not copy its JupyterHub identity, token or auth settings.

Proposed resources: namespace `python-phd`, CPU-only Deployment using a pinned
image, ClusterIP Service and Ingress for `/python-phd` on the existing hostname.
Use port 8080 and `/healthz` probes. A static book needs no GPU or persistent
volume. Decide public versus authenticated course access before configuring
ingress, and add the app to the current Kustomization and Flux health checks.

Validate affected GitOps entrypoints locally and prepare a concrete diff. The
GitOps repository belongs to `icg-innovation`; the user's AGENTS.md requires
explicit prior approval before opening/submitting/modifying a PR there. This
preparation creates none. Before live changes, state the exact commands, impact,
verification and rollback.

After an approved release, verify Flux's source/applied revision, readiness,
pods, endpoints and Ingress. Check the live home page, deep chapters, assets,
search, plots and intended auth in a browser. Roll back by reverting to the
previous working Git/image revision and repeating those checks. A local build
or pushed image alone is not evidence of deployment.

## Optional live notebooks

Separately verify CPD JupyterHub's current image, environment, users and loading
route. Provide the exact course revision and install it in that kernel. Static
publication can proceed independently. No live-kernel integration is declared
ready, and the UKSA service identity must not be reused blindly.
