"""Compatibility fixes for the lazy compute startup in the pinned book theme.

The toolbar requests a connection before its lazy-loaded server exists. Retain
that request in the provider's existing `connect` state so its effect connects
once the server mounts. Fail closed if a template update changes the vendor
fragment. Notebook readiness must include the page's own cells and session,
including notebooks with no external dependencies. Version all build asset
URLs to avoid cached modules hiding the fixes.
"""
from hashlib import sha256
from pathlib import Path
import shutil

OLD = "let q=()=>{if(b)return y(!0),i?i(b):n?"
NEW = "let q=()=>{if(!b){g(!0);return}return y(!0),i?i(b):n?"
PATCHES = [
    (OLD, NEW),
    ("function S9(t,e){let r=t.pages[e];return r==null?void 0:r.dependencies.every(",
     "function S9(t,e){let r=t.pages[e];return r==null?void 0:(r.kind!==Tr.Notebook||!!r.scopes[e])&&r.dependencies.every("),
    ("function E9(t,e){let r=t.pages[e];return r==null?void 0:r.dependencies.every(",
     "function E9(t,e){let r=t.pages[e];return r==null?void 0:(r.kind!==Tr.Notebook||!!r.scopes[e]?.session)&&r.dependencies.every("),
]


def patch(build_dir: Path) -> None:
    assets = build_dir / "build"
    if not assets.is_dir():
        if list(build_dir.glob("build-phd-*")):
            return
        raise ValueError("Missing MyST build assets")
    matches = [p for p in assets.rglob("*.js") if OLD in p.read_text()]
    if len(matches) != 1 or matches[0].read_text().count(OLD) != 1:
        raise ValueError("Thebe 0.5.0 compatibility fragment changed; review cold-start behavior")
    target = matches[0]
    source = target.read_text()
    for old, new in PATCHES:
        if source.count(old) != 1:
            raise ValueError("Compute compatibility fragment changed; review notebook readiness")
        source = source.replace(old, new)
    target.write_text(source)
    version = "build-phd-" + sha256(source.encode()).hexdigest()[:12]
    for previous in build_dir.glob("build-phd-*"):
        if previous.is_dir():
            shutil.rmtree(previous)
    assets.rename(build_dir / version)
    for path in build_dir.rglob("*"):
        if path.is_file() and path.suffix in {".html", ".js", ".json", ".css"}:
            text = path.read_text()
            updated = text.replace("/python-phd/build/", f"/python-phd/{version}/")
            if updated != text:
                path.write_text(updated)
    print(f"Fixed Thebe cold start; versioned assets at {version}")


if __name__ == "__main__":
    patch(Path("_build/html"))
