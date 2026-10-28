"""Build a portable, static gallery from the public poster catalog."""
from pathlib import Path
from html import escape as e
import hashlib
import json
import os
import shutil
import zipfile
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
BASE = os.environ.get('SITE_URL', 'https://posters.afraim.me').rstrip('/')
REPO = 'https://github.com/Afraim10/protein-universe'
ITEMS = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
DETAILS = {
 'egfr-signal-translator': ('Signaling', 'A signal outside the cell becomes a molecular conversation within. Explore the architecture of a full-length epidermal growth factor receptor.'),
 'molecular-recycler': ('Molecular machines', 'Recognition, unfolding, threading and cleavage: a journey through the human proteasome and the machinery of protein turnover.'),
 'photon-switch': ('Protein chemistry', 'Follow the meeting of light and matter inside rhodopsin, where retinal photoisomerization initiates a biological signal.'),
 'one-protein-many-views': ('Ways of seeing', 'One molecule, multiple representations. Explore carbonic anhydrase II through surfaces, ribbons, atoms and illustrative property maps.'),
 'protein-universe': ('Ways of seeing', 'An invitation into protein biology: from the folding of a chain to the structures and interactions that make cellular life possible.'),
 'molecular-motor': ('Molecular machines', 'Explore ATP synthase, the molecular machine coupling an ion gradient to ATP synthesis.'),
 'molecular-walker': ('Molecular machines', 'Meet kinesin: a molecular motor whose coordinated steps carry cargo along the cell’s microtubule tracks.'),
 'molecular-weave': ('Protein chemistry', 'From intertwined chains to structural fibers, explore the molecular architecture of collagen.'),
 'viral-machine': ('Molecular machines', 'A portrait of bacteriophage T4 and its intricate molecular architecture for interacting with a bacterial host.'),
 'nuclear-gateway': ('Molecular machines', 'Explore the nuclear pore complex, the enormous protein assembly organizing selective transport between nucleus and cytoplasm.'),
 'genome-duplicator': ('Molecular machines', 'Follow the coordinated molecular machinery at a human DNA replication fork.')
}

def write(path, content):
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8')

def image(item, prefix='', hero=False, detail=False):
    slug = item['id']
    sizes = '(min-width: 1100px) 560px, (min-width: 700px) 48vw, 92vw' if hero else '(min-width: 1000px) 30vw, (min-width: 640px) 46vw, 92vw'
    if detail: sizes = '(min-width: 1000px) 62vw, 94vw'
    return (f'<img src="{prefix}media/{slug}-960.webp" srcset="{prefix}media/{slug}-480.webp 480w, '
            f'{prefix}media/{slug}-960.webp 960w, {prefix}media/{slug}-1600.webp 1600w" sizes="{sizes}" '
            f'width="{item["file"]["width"]}" height="{item["file"]["height"]}" alt="{e(item["title"])} — illustrated scientific poster" '
            f'loading="{"eager" if hero or detail else "lazy"}" decoding="async" '
            f'{"fetchpriority=\"high\"" if hero else ""}>')

def shell(title, description, body, prefix='', path='', script=False, og='media/egfr-signal-translator-1600.webp'):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} | Protein Universe</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#080a0f"><link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | Protein Universe">
<meta property="og:description" content="{e(description)}"><meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{BASE}/{og}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}style.css"><link rel="stylesheet" href="{prefix}identity.css"><link rel="preload" href="{prefix}fonts/instrument-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
{'<script defer src="app.js"></script>' if script else ''}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header wrap"><a class="brand" href="{prefix or './'}" aria-label="Protein Universe home"><span class="brand-mark" aria-hidden="true">a<span>f</span></span><span class="brand-label">The Fold<span class="brand-second">Protein Universe / Art collection</span></span></a>
<nav aria-label="Main navigation"><a href="{prefix}index.html#collection">The collection</a><a href="{prefix}index.html#create">Create your own</a><a class="portfolio" href="https://afraim.me">Afraim’s portfolio ↗</a></nav></header>
{body}
<footer class="wrap"><div><a class="footer-title" href="{prefix or './'}">PROTEIN UNIVERSE</a><p>A molecular art collection by Afraim Mario.</p></div>
<div><a href="{REPO}">GitHub ↗</a> · <a href="{REPO}/blob/main/LICENSE.md">CC BY 4.0</a><p>AI-assisted illustrations. Independently created; not affiliated with Kurzgesagt.</p></div></footer>
</body></html>'''

OUT.mkdir(exist_ok=True)
(OUT/'media').mkdir(exist_ok=True)
(OUT/'downloads').mkdir(exist_ok=True)
for item in ITEMS:
    src = ROOT/item['image']
    assert hashlib.sha256(src.read_bytes()).hexdigest() == item['file']['sha256'], f'Checksum mismatch: {src}'
    with Image.open(src) as original:
        original = ImageOps.exif_transpose(original).convert('RGB')
        for width in (480, 960, 1600):
            resized = original.resize((width, round(original.height*width/original.width)), Image.Resampling.LANCZOS)
            resized.save(OUT/'media'/f'{item["id"]}-{width}.webp', 'WEBP', quality=83, method=6)
    shutil.copyfile(src, OUT/'downloads'/src.name)

skill = ROOT/'.agents/skills/artifact-template-protein-universe-posters'
with zipfile.ZipFile(OUT/'downloads/protein-universe-skill.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(skill.rglob('*')):
        if p.is_file(): z.write(p, 'artifact-template-protein-universe-posters/'+p.relative_to(skill).as_posix())
    z.write(ROOT/'LICENSE.md', 'LICENSE.md')
    z.write(ROOT/'docs/GETTING_STARTED.md', 'GETTING_STARTED.md')

cards = ''
for i, item in enumerate(ITEMS):
    category, description = DETAILS[item['id']]
    cards += f'''<article class="poster-card" data-category="{e(category)}"><a class="poster-frame" href="{item['id']}/">{image(item)}<span class="view-label">Explore poster ↗</span></a>
<div class="card-meta"><span>{i+1:02d} / {category}</span><span>{'Portrait' if item['file']['height'] > item['file']['width'] else 'Landscape'}</span></div>
<h3><a href="{item['id']}/">{e(item['title'])}</a></h3><p>{e(description)}</p></article>'''

body = f'''<main id="main">
<section class="hero wrap"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> THE FOLD / A MOLECULAR ART COLLECTION</p>
<h1>Life is molecular.<br><em>Look closer.</em></h1><p class="intro">The folds, machines and quiet wonders of protein biology, reimagined as scientific art.</p>
<div class="actions"><a class="button primary" href="#collection">Explore the collection <span>↓</span></a><a class="text-link" href="#create">Make something of your own ↗</a></div>
<p class="hero-foot">11 posters <span>·</span> Free to download <span>·</span> Openly shared</p></div>
<a class="hero-art" href="egfr-signal-translator/"><div class="frame-heading"><span>Featured / Human EGFR</span><span aria-hidden="true">+</span></div>{image(ITEMS[0], hero=True)}<div class="art-caption"><span>01 / EGFR</span><span>The Signal Translator ↗</span></div></a></section>
<div class="principles wrap"><span>FROM MOLECULAR MACHINES TO WAYS OF SEEING</span><p>Made for curious minds. Shared for the next idea.</p></div>
<section class="collection wrap" id="collection"><div class="section-heading"><div><p class="eyebrow"><span class="section-index">01</span> The collection</p><h2>A closer look at life.</h2></div><p>Explore a poster, read its scientific notes,<br>or take the full-resolution artwork with you.</p></div>
<div class="filters" aria-label="Filter posters" hidden><button type="button" aria-pressed="true" data-filter="All">All posters <small>11</small></button>'''
for category in ('Molecular machines','Signaling','Protein chemistry','Ways of seeing'):
    body += f'<button type="button" aria-pressed="false" data-filter="{category}">{category}</button>'
body += f'''</div><p class="sr-only" id="result-count" aria-live="polite">11 posters</p><div class="poster-grid">{cards}</div></section>
<section class="create wrap" id="create"><div><p class="eyebrow"><span class="section-index">02</span> Behind the collection</p><h2>Curiosity is<br>the starting point.</h2><p>I’m Afraim, an undergraduate in Egypt fascinated by proteins. A hardcover copy of <em>Immune</em> by Philipp Dettmer, brought from the US by a friend, and the motion graphics in Kurzgesagt’s videos made me fall in love with their visual storytelling. I wanted to explore that sense of wonder through my own subject: molecular biology.</p><p>These posters grew from that curiosity, using Codex and image generation. Their visual language is inspired by Kurzgesagt; this independent project doesn’t replace the craft of the studio’s designers.</p></div>
<div class="skill-panel"><span class="eyebrow">THE REUSABLE SKILL</span><h3>Your protein.<br>Your next poster.</h3><p>A shared workflow for choosing a molecular story, developing a composition and reviewing the result. Start with the guide, then adapt it to your own curiosity.</p><a class="button primary" href="downloads/protein-universe-skill.zip" download>Download the skill <span>↓</span></a><a class="text-link" href="{REPO}/blob/main/docs/GETTING_STARTED.md">Read the getting-started guide ↗</a><small>Requires access to compatible AI tools. The skill does not include a model or generation credits.</small></div></section>
<section class="reuse wrap"><div><p class="eyebrow"><span class="section-index">03</span> Open to your next idea</p><h2>Download. Adapt. Give credit.</h2><p>Share and adapt the original material, including commercially, under CC BY 4.0 to the extent applicable rights are held. Credit Afraim Mario, link the license and indicate your changes.</p><a class="text-link" href="{REPO}/blob/main/LICENSE.md">License & attribution ↗</a></div><div><h3>Art with scientific context.</h3><p>These are AI-assisted schematics, not experimentally validated figures or exact molecular renders. Read each poster’s notes before educational reuse. Known issues are listed alongside the artwork.</p><a class="text-link" href="{REPO}/blob/main/docs/SCIENTIFIC_REVIEW.md">Scientific review notes ↗</a></div></section></main>'''
write('index.html', shell('Molecular biology, illustrated', 'Explore and download 11 protein biology posters by Afraim Mario, plus a reusable AI-assisted scientific illustration skill.',body,script=True))

for index, item in enumerate(ITEMS):
    category, description = DETAILS[item['id']]
    f = item['file']
    issues = ''.join(f'<p>{e(issue)}</p>' for issue in item.get('knownIssues',[]))
    next_item = ITEMS[(index+1)%len(ITEMS)]
    body = f'''<main id="main" class="wrap detail"><a class="back-link" href="../index.html#collection">← Back to the collection</a><div class="detail-grid"><div class="detail-art">{image(item,'../',detail=True)}</div>
<div class="detail-copy"><p class="eyebrow">{index+1:02d} / {category.upper()}</p><h1>{e(item['title'])}</h1><p class="intro">{e(description)}</p>
<dl><div><dt>Resolution</dt><dd>{f['width']:,} × {f['height']:,} px</dd></div><div><dt>Original download</dt><dd>PNG · {f['bytes']/1000000:.1f} MB</dd></div><div><dt>Creator</dt><dd>Afraim Mario</dd></div><div><dt>Reuse</dt><dd><a href="{REPO}/blob/main/LICENSE.md">CC BY 4.0</a></dd></div></dl>
<a class="button primary" href="../downloads/{Path(item['image']).name}" download>Download full-resolution PNG <span>↓</span></a>
<a class="text-link" href="{REPO}/blob/main/{item['notes']}">Read the sources & process ↗</a>
<div class="science-note"><h2>Before you use this poster</h2><p>AI-assisted schematic illustration. Not independently validated. The enhanced original is preserved without further changes.</p>{'<h3>Known label issue</h3>'+issues if issues else ''}<p>Credit Afraim Mario / Protein Universe, link <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, and indicate any changes.</p></div>
</div></div><a class="next-poster" href="../{next_item['id']}/"><span>KEEP EXPLORING</span><strong>{e(next_item['title'])} →</strong></a></main>'''
    write(item['id']+'/index.html', shell(item['title'],description,body,'../',item['id']+'/',og=f'media/{item["id"]}-1600.webp'))

for name in ('style.css','identity.css','app.js','favicon.svg'):
    shutil.copyfile(ROOT/'gallery'/name, OUT/name)
shutil.copytree(ROOT/'gallery/fonts', OUT/'fonts', dirs_exist_ok=True)
write('.nojekyll','')
write('404.html',shell('Page not found','This page could not be found.',f'<main id="main" class="wrap detail"><p class="eyebrow">404</p><h1>This molecule wandered off.</h1><p><a href="{BASE}/">Return to the collection →</a></p></main>', prefix=BASE+'/'))
write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}/{p}</loc></url>' for p in ['']+[i['id']+'/' for i in ITEMS])+'</urlset>')
print(f'Built {len(ITEMS)} poster pages, responsive previews and exact original downloads in {OUT}')
