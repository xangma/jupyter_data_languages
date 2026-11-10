import importlib.util
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("hub_links", ROOT / "scripts/inject_jupyterhub_launch_links.py")
links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(links)


def test_launch_targets_editable_source_not_generated_copy():
    url = urlsplit(links.launch_url("_executed/01-catalogue.ipynb"))
    assert url.path == "/jupyterhub/services/phd-python-thebe/bootstrap"
    assert parse_qs(url.query)["open"] == ["book/01-catalogue.ipynb"]


def test_book_root_may_live_in_a_subdirectory():
    project = {"toc": [{"file": "book/index.md"}, {"file": "book/setup.md"},
                       {"file": "_executed/01-catalogue.ipynb"}],
               "pages": [{"slug": "setup"}, {"slug": "catalogue"}]}
    assert list(links.notebook_routes(project)) == ["catalogue"]


def test_connect_returns_to_current_chapter_and_injection_is_idempotent(tmp_path):
    chapter = tmp_path / "catalogue/index.html"
    chapter.parent.mkdir()
    chapter.write_text('<html><body><a href="/jupyterhub/services/phd-python-thebe/bootstrap">JupyterHub</a></body></html>')
    script = links.injected_script({"catalogue": links.launch_url("book/01-catalogue.ipynb")})
    assert links.inject(tmp_path, chapter, script)
    assert not links.inject(tmp_path, chapter, script)
    assert chapter.read_text().count(links.MARKER_START) == 1
    assert 'return=%2Fpython-phd%2Fcatalogue%2F' in chapter.read_text()
