"""Check published local links and required artifacts using only the stdlib."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])


root = Path(__file__).resolve().parents[1] / "_site"
parser = Links()
parser.feed((root / "index.html").read_text(encoding="utf-8"))
for href in parser.links:
    url = urlsplit(href)
    if url.scheme or url.netloc:
        continue
    if not url.path:
        assert not url.fragment or unquote(url.fragment) in parser.ids, href
    else:
        target = (root / unquote(url.path)).resolve()
        assert target.is_relative_to(root.resolve()) and target.is_file(), href
for name in ("document.pdf", "slides.pdf"):
    data = (root / name).read_bytes()
    assert data.startswith(b"%PDF-") and len(data) > 1000, name
print(f"PASS: {len(parser.links)} links inspected; local anchors and PDFs are valid")
