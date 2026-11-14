"""Verify editable screenshot SVG rendering and lossless crop bounds."""
import importlib.util
import io
from pathlib import Path

from PIL import Image
import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "screenshot_callouts", ROOT / "scripts/render_screenshot_callouts.py"
)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def _make_jpeg(path: Path, size: tuple[int, int] = (400, 300)) -> None:
    buf = io.BytesIO()
    Image.new("RGB", size, color=(240, 244, 248)).save(buf, format="JPEG")
    path.write_bytes(buf.getvalue())


def test_cropped_svg_sets_viewbox_clip_and_preserves_source_bytes(tmp_path: Path) -> None:
    src = tmp_path / "sample.jpg"
    _make_jpeg(src, (400, 300))
    before = src.read_bytes()
    svg = MOD.render(
        tmp_path,
        {
            "name": "sample",
            "title": "Cropped panel",
            "crop": [50, 40, 300, 200],
            "callout_scale": 0.5,
            "callouts": [
                {"bubble": [100, 90], "target": [180, 120], "label": "Inspect plan"}
            ],
        },
    )
    assert src.read_bytes() == before
    assert 'width="300" height="200" viewBox="50 40 300 200" overflow="hidden"' in svg
    assert '<rect x="50" y="40" width="300" height="200"/>' in svg
    assert '<image id="original-capture" x="0" y="0" width="400" height="300"' in svg


@pytest.mark.parametrize(
    "crop,bubble,target",
    [
        ([50, 40, 400, 200], [100, 90], [180, 120]),   # crop exceeds width
        ([50, 40, 300, 200], [55, 90], [180, 120]),    # bubble clips left crop edge
        ([50, 40, 300, 200], [100, 90], [20, 120]),    # target outside crop box
    ],
)
def test_invalid_crop_or_out_of_crop_callout_is_rejected(
    tmp_path: Path, crop: list[int], bubble: list[int], target: list[int]
) -> None:
    _make_jpeg(tmp_path / "sample.jpg", (400, 300))
    with pytest.raises(ValueError):
        MOD.render(
            tmp_path,
            {
                "name": "sample",
                "title": "Invalid crop",
                "crop": crop,
                "callout_scale": 0.5,
                "callouts": [{"bubble": bubble, "target": target, "label": "Bad"}],
            },
        )
