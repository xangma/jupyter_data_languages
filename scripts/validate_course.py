"""Execute every 2026 notebook in a new kernel and an empty working directory.

Write executed copies to the ignored build directory, leaving source clean.
The publication build reads these copies, so rendered plots match the check.
"""
from pathlib import Path
import tempfile
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parents[1]
destination = root / "_executed"
destination.mkdir(exist_ok=True)
for source in sorted((root / "book").glob("*.ipynb")):
    notebook = nbformat.read(source, as_version=4)
    nbformat.validate(notebook)
    with tempfile.TemporaryDirectory(prefix="icg-notebook-") as cwd:
        NotebookClient(notebook, timeout=120, kernel_name="python3",
            resources={"metadata": {"path": cwd}}, allow_errors=False).execute()
    nbformat.write(notebook, destination / source.name)
    print(f"PASS {source.name}", flush=True)
