"""Layer editable, numbered SVG callouts over unchanged interface captures."""

import argparse
import base64
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image


def filename(value: str) -> str:
    if (not isinstance(value, str) or not value or value in {".", ".."}
            or Path(value).name != value or "\\" in value):
        raise ValueError(f"Expected a filename: {value!r}")
    return value


def render(root: Path, item: dict) -> str:
    name = filename(item["name"])
    source = root / filename(item.get("source", f"{name}.jpg"))
    if source.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        raise ValueError(f"Unsupported capture format: {source.name}")
    raw = source.read_bytes()
    with Image.open(source) as capture:
        # Some older .png captures contain JPEG bytes: trust the image header.
        capture_format = capture.format
        mime_type = {"JPEG": "image/jpeg", "PNG": "image/png"}.get(capture_format)
        if mime_type is None:
            raise ValueError(f"Unsupported capture format: {source.name}")
        width, height = capture.size
    if item.get("mime_type", mime_type) != mime_type:
        raise ValueError(f"MIME type does not match capture: {source.name}")
    crop = item.get("crop")
    if crop is None:
        cx, cy, cw, ch = 0, 0, width, height
    else:
        if len(crop) != 4 or not all(isinstance(v, int) for v in crop):
            raise ValueError(f"Expected integer [x, y, w, h] crop: {item['name']}")
        cx, cy, cw, ch = crop
        if not (0 <= cx < width and 0 <= cy < height and cw > 0 and ch > 0
                and cx + cw <= width and cy + ch <= height):
            raise ValueError(f"Crop outside capture: {item['name']}")
    description = " ".join(
        f"{i}: {callout['label']}." for i, callout in enumerate(item["callouts"], 1)
    )
    scale = item.get("callout_scale", 1)
    if not 0 < scale <= 2:
        raise ValueError(f"Invalid callout scale: {item['name']}")
    def size(value: int) -> int:
        return max(1, round(value * scale))
    radius = size(36)
    overflow_attr = ' overflow="hidden"' if crop is not None else ''
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{cw}" height="{ch}" '
        f'viewBox="{cx} {cy} {cw} {ch}"{overflow_attr} role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(item["title"])}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        f'<!-- Original {capture_format} SHA-256: {hashlib.sha256(raw).hexdigest()} -->',
    ]
    if crop is not None:
        parts.extend([
            f'<defs><clipPath id="crop-box"><rect x="{cx}" y="{cy}" width="{cw}" height="{ch}"/></clipPath></defs>',
            '<g clip-path="url(#crop-box)">',
            f'<image id="original-capture" x="0" y="0" width="{width}" height="{height}" '
            f'href="data:{mime_type};base64,{base64.b64encode(raw).decode()}"/>',
        ])
    else:
        parts.append(
            '<image id="original-capture" width="100%" height="100%" '
            f'href="data:{mime_type};base64,{base64.b64encode(raw).decode()}"/>'
        )
    parts.append(
        '<g id="editable-callouts" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size(42)}" font-weight="700" text-anchor="middle">'
    )
    for i, callout in enumerate(item["callouts"], 1):
        x, y = callout["bubble"]
        tx, ty = callout["target"]
        if not (cx + radius <= x <= cx + cw - radius
                and cy + radius <= y <= cy + ch - radius
                and cx <= tx <= cx + cw and cy <= ty <= cy + ch):
            raise ValueError(f"Callout outside capture/crop: {item['name']} #{i}")
        parts.extend([
            f'<g id="callout-{i}" aria-label="{escape(callout["label"], {chr(34): "&quot;"})}">',
            f'<path d="M{x},{y} L{tx},{ty}" stroke="white" stroke-width="{size(12)}"/>',
            f'<path d="M{x},{y} L{tx},{ty}" stroke="#075985" stroke-width="{size(6)}"/>',
            f'<circle cx="{tx}" cy="{ty}" r="{size(7)}" fill="#075985" stroke="white" stroke-width="{size(2)}"/>',
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="#075985" stroke="white" stroke-width="{size(4)}"/>',
            f'<text x="{x}" y="{y + size(14)}" fill="white">{i}</text>',
            '</g>',
        ])
    closing = ["</g>", "</g>", "</svg>", ""] if crop is not None else ["</g>", "</svg>", ""]
    return "\n".join(parts + closing)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1] / "book" / "screenshots"
    items = json.loads((root / "callouts.json").read_text())
    for extra in ("legacy-callouts.json", "completion-callouts.json"):
        manifest = root / extra
        if manifest.exists():
            items.extend(json.loads(manifest.read_text()))
    names = set()
    for item in items:
        name = filename(item["name"]).casefold()
        if name in names:
            raise SystemExit(f"Duplicate screenshot name: {item['name']}")
        names.add(name)
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
