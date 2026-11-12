"""Render the editable DOT teaching diagrams as portable, accessible SVGs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "book" / "diagrams"
SVG = "http://www.w3.org/2000/svg"


def render(entry: dict[str, str], dot: str) -> bytes:
    source = DIRECTORY / (entry["name"] + ".dot")
    result = subprocess.run([dot, "-Tsvg", str(source)], capture_output=True)
    if result.returncode:
        raise RuntimeError(f"dot failed for {source.name} ({result.returncode}): "
                           + result.stderr.decode())
    if result.stderr:
        raise RuntimeError(result.stderr.decode())
    root = ET.fromstring(result.stdout)
    # Keep intrinsic reading dimensions bounded without rasterising or changing
    # the viewBox: tall figures should not fill several notebook screens.
    _, _, width, height = map(float, root.attrib["viewBox"].split())
    scale = min(720 / width, 640 / height)
    root.set("width", str(round(width * scale)))
    root.set("height", str(round(height * scale)))
    root.set("role", "img")
    root.set("aria-labelledby", entry["name"] + "-title " + entry["name"] + "-desc")
    title = ET.Element("{" + SVG + "}title", id=entry["name"] + "-title")
    title.text = entry["title"]
    description = ET.Element("{" + SVG + "}desc", id=entry["name"] + "-desc")
    description.text = entry["description"]
    root.insert(0, title)
    root.insert(1, description)
    ET.register_namespace("", SVG)
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True) + b"\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if a checked-in SVG differs from its editable source")
    args = parser.parse_args()
    dot = shutil.which("dot")
    if dot is None:
        parser.error("Install Graphviz for diagram maintenance; students use the checked-in SVGs.")
    entries = json.loads((DIRECTORY / "diagrams.json").read_text())
    stale = []
    for entry in entries:
        output = render(entry, dot)
        target = DIRECTORY / (entry["name"] + ".svg")
        if args.check:
            if not target.exists() or target.read_bytes() != output:
                stale.append(target.name)
        else:
            target.write_bytes(output)
    if stale:
        parser.error("Regenerate stale diagrams: " + ", ".join(stale))
    print(f"{'Checked' if args.check else 'Rendered'} {len(entries)} editable diagrams.")


if __name__ == "__main__":
    main()
