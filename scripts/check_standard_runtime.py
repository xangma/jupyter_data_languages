"""Check both standard kernels and run every course notebook in its named kernel."""
import json
from pathlib import Path
import tempfile

import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager

root = Path(__file__).resolve().parents[1]
kernels = KernelSpecManager().find_kernel_specs()
assert {"python3", "python-phd", "ml-env", "c", "ir"}.issubset(kernels), kernels
checks = {
    "python3": "import sys, numpy, torch; assert sys.version_info[:2] == (3, 12); assert numpy.__version__ == '1.26.4'; print(sys.executable, torch.__version__)",
    "python-phd": "import sys, numpy, scipy, astropy; assert sys.version_info[:2] == (3, 13); assert sys.executable == '/opt/course/.venv/bin/python'; assert numpy.__version__.startswith('2.'); print(sys.version, numpy.__version__, scipy.__version__, astropy.__version__)",
}
for kernel, code in checks.items():
    nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(code)])
    NotebookClient(nb, kernel_name=kernel, timeout=120).execute()
    print("PASS", kernel, flush=True)

for source in sorted((root / "book").glob("*.ipynb")):
    nb = nbformat.read(source, as_version=4)
    with tempfile.TemporaryDirectory(prefix="cpd-standard-notebook-") as cwd:
        NotebookClient(nb, kernel_name="python-phd", timeout=120,
                       resources={"metadata": {"path": cwd}}, allow_errors=False).execute()
    print("PASS", source.name, flush=True)

print(json.dumps({"kernels": sorted(kernels), "course_notebooks": 5, "result": "passed"}))
