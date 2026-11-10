"""Serve the checked static book locally at /python-phd/; Ctrl+C stops it."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--port", type=int, default=8765)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1] / "_build/html"
if not (root / "index.html").exists():
    parser.error("Build the book first; see README.md")
with tempfile.TemporaryDirectory(prefix="icg-preview-") as folder:
    (Path(folder) / "python-phd").symlink_to(root, target_is_directory=True)
    server = ThreadingHTTPServer(("127.0.0.1", args.port),
        partial(SimpleHTTPRequestHandler, directory=folder))
    print(f"Serving http://127.0.0.1:{args.port}/python-phd/ — Ctrl+C to stop", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
