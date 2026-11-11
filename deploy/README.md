# CPD deployment

Live course: <https://icg-cpd-cluster.port.ac.uk/python-phd/>.
[Validation](../VALIDATION.md) records versions, image digests and observed tests.
The existing UKSA book remains at `/jupyterbook/`.

## Student workflow

Read without signing in. Choose Connect to JupyterHub or the compute button and
use the existing GitHub sign-in. The bridge starts the CPU `python-phd` named
server and synchronises the course into `~/jupyter_data_languages`. Start compute
on a notebook page and run cells from the top. Open this notebook in CPD
JupyterHub opens the editable source; use its terminal for the Git practical.
Stop the named server from Hub Home when finished. Disconnect clears the book's
connection; it does not stop the server or remove files.

## Build and promote

Use the validation/build commands in the repository README, with Node 22 and
`BASE_URL=/python-phd`. The build applies the documented Thebe compatibility
patch and injects the user-scoped Hub controls. The static container serves
checked HTML on port 8080 with `/healthz`; it does not contain a kernel.

`myst.yml` pins book-theme v1.4.1 at commit `23f2df5493e23dfb1d9433c8aa64c87beb4232a3`.
The floating `book-theme` name began fetching v2.0.0 on 10 November 2026; its
HTML format differs from the tested Hub integration. Upgrade the theme as a
separate integration change, with cold-start and notebook tests, rather than
changing it implicitly during a content rebuild.

For content-only changes, rebuild the static book and publish the course branch
for nbgitpuller. Rebuild the notebook image when its Dockerfile or locked runtime
dependencies change; otherwise retain the verified runtime digest.

`Dockerfile.notebook` installs `requirements-hub.lock` with hashes. It supplies
the course's Python kernel, JupyterHub client and nbgitpuller, using UID/GID 1011.
The login-shell profile keeps terminal Python aligned with the kernel. Source
and data are pulled into the student's persistent home, rather than installed
as a hidden copy in the image.

GitOps resources live in `icg-innovation/space-k8s-gitops`:

- `apps/{base,overlays/prod-cluster}/phd-python-jupyterbook`
- `apps/overlays/prod-cluster/jupyterhub/jupyterhub-values.yaml`
- `docs/python-phd-jupyterbook.md` and `docs/registry-policy.md`

The book runs in `jupyterhub`, reusing its registry pull secret. The package
permissions inherit the GitOps repository's pull identity; no public package
exception or new credentials were needed. Promote immutable image digests and
update the registry inventory in the same approved GitOps change. The user's
approval is required before opening PRs in this organisation repository.

After promotion verify Flux's applied revision, Hub Helm readiness, pod image and
CPU resources, ingress, storage, login, clone, in-page execution, JupyterLab,
terminal commands and search. Preserve student PVCs during any rollback; revert
the relevant GitOps promotions rather than changing live workloads by hand.
