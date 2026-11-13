"""Layer editable, numbered SVG callouts over unchanged VS Code captures."""

import argparse
import base64
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image


def render(root: Path, item: dict) -> str:
    source = root / f"{item['name']}.jpg"
    raw = source.read_bytes()
    with Image.open(source) as capture:
        if capture.format != "JPEG":
            raise ValueError(f"Not a JPEG: {source.name}")
        width, height = capture.size
    description = " ".join(
        f"{i}: {callout['label']}." for i, callout in enumerate(item["callouts"], 1)
    )
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(item["title"])}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        f'<!-- Original JPEG SHA-256: {hashlib.sha256(raw).hexdigest()} -->',
        '<image id="original-capture" width="100%" height="100%" '
        f'href="data:image/jpeg;base64,{base64.b64encode(raw).decode()}"/>',
        '<g id="editable-callouts" font-family="Arial, Helvetica, sans-serif" '
        'font-size="42" font-weight="700" text-anchor="middle">',
    ]
    for i, callout in enumerate(item["callouts"], 1):
        x, y = callout["bubble"]
        tx, ty = callout["target"]
        if not (36 <= x <= width - 36 and 36 <= y <= height - 36
                and 0 <= tx <= width and 0 <= ty <= height):
            raise ValueError(f"Callout outside capture: {item['name']} #{i}")
        parts.extend([
            f'<g id="callout-{i}" aria-label="{escape(callout["label"], {chr(34): "&quot;"})}">',
            f'<path d="M{x},{y} L{tx},{ty}" stroke="white" stroke-width="12"/>',
            f'<path d="M{x},{y} L{tx},{ty}" stroke="#075985" stroke-width="6"/>',
            f'<circle cx="{tx}" cy="{ty}" r="7" fill="#075985" stroke="white" stroke-width="2"/>',
            f'<circle cx="{x}" cy="{y}" r="36" fill="#075985" stroke="white" stroke-width="4"/>',
            f'<text x="{x}" y="{y + 14}" fill="white">{i}</text>',
            '</g>',
        ])
    return "\n".join(parts + ["</g>", "</svg>", ""])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1] / "book" / "screenshots"
    items = json.loads((root / "callouts.json").read_text())
    for item in items:
        path = root / f"{item['name']}.svg"
        expected = render(root, item)
        if args.check:
            if not path.exists() or path.read_text() != expected:
                raise SystemExit(f"Regenerate {path.name}")
        else:
            path.write_text(expected)
    print(f"{'Checked' if args.check else 'Rendered'} {len(items)} annotated screenshots")


if __name__ == "__main__":
    main()
