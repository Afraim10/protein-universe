# Gallery maintenance

This standalone static gallery is hosted by GitHub Pages. It does not depend on or modify the portfolio application.

## Local build

Use Python 3.12 or newer:

```sh
pip install -r gallery/requirements.txt
python gallery/build.py
python gallery/check.py
python -m http.server 4173 --directory dist
```

Open http://localhost:4173. `dist/` is generated and ignored by Git. `SITE_URL` controls canonical URLs and the sitemap. GitHub Actions obtains it from the Pages configuration.

## Updating posters

Keep the original PNG in `posters/`, update its entry and SHA-256 checksum in `catalog.json`, and update its scientific notes. Add a category and short description in `gallery/build.py` for new subjects. The build creates three WebP preview sizes and copies original downloads without alteration. Review known issues beside the relevant poster.

Push to `main` to rebuild and deploy. The workflow checks internal links, image dimensions, original file checksums and asset budgets before deployment.

## Domain

The intended address is `posters.afraim.me`. Configure this custom domain in this repository’s GitHub Pages settings, then add only this record at Namecheap:

| Type | Host | Target | TTL |
| --- | --- | --- | --- |
| CNAME | posters | afraim10.github.io | Automatic |

Preserve all existing apex, www, mail and verification records. Enable Enforce HTTPS once GitHub issues the certificate. The initial GitHub Pages address remains useful until the custom domain is connected. With Actions publishing, the domain is stored in Pages settings, not in a generated CNAME file.
