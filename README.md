# Track A  Autonomous Business (Static Site)

This is a minimal static site scaffold ready for GitHub Pages (project subpath).

- Site root: `/site`
- Posts listing: `/site/data/posts.json`
- Post template: `/site/templates/base.html`
- Publish script: `/scripts/publish.py`
- Pages workflow: `.github/workflows/pages.yml`

Local build:
- Optional: `python scripts/publish.py` to generate sample post under `site/posts/...`.

GitHub Pages:
- Push to `main`; Actions will deploy `./site`.
- Expected URL: `https://<USERNAME>.github.io/<REPO>/`
