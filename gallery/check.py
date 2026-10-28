"""Check generated links, accessibility basics, downloads and size budgets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'dist'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.h1=0; self.lang=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='html': self.lang=bool(a.get('lang'))
        if tag=='h1': self.h1+=1
        if tag=='img':
            assert a.get('alt') and a.get('width') and a.get('height'), a
            assert a['src'].endswith('.webp'), 'Original PNG loaded as preview'
        for key in ('href','src'):
            if key in a: self.links.append(a[key])
pages={}
for path in OUT.rglob('*.html'):
    p=Page();p.feed(path.read_text(encoding='utf-8'));pages[path.resolve()]=p
    assert p.lang and p.h1==1, path
for path,page in pages.items():
    for href in page.links:
        u=urlparse(href)
        if u.scheme or u.netloc: continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.exists(), (path,href)
        if u.fragment and target in pages: assert unquote(u.fragment) in pages[target].ids,(path,href)
items=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
for item in items:
    download=OUT/'downloads'/Path(item['image']).name
    assert hashlib.sha256(download.read_bytes()).hexdigest()==item['file']['sha256']
assert (OUT/'app.js').stat().st_size<3000
assert (OUT/'style.css').stat().st_size<16000
assert max(p.stat().st_size for p in (OUT/'media').glob('*-960.webp'))<350000
print(f'PASS: {len(pages)} HTML pages; local links and fragments; image accessibility; 11 download checksums; JS/CSS/preview budgets.')
