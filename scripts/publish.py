import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DATA = SITE / "data" / "posts.json"
TEMPLATES = SITE / "templates"
POSTS_DIR = SITE / "posts"

BASE = (TEMPLATES / "base.html").read_text(encoding="utf-8-sig")

def update_index():
    posts = json.loads(DATA.read_text(encoding="utf-8-sig"))
    # Ensure URLs are relative without leading slash for GitHub Pages project subpath
    for p in posts:
        date = p.get("date", "")
        slug = p.get("slug", "")
        p["url"] = f"posts/{date}-{slug}/"  # no leading slash
    DATA.write_text(json.dumps(posts, indent=2), encoding="utf-8")


def build_posts():
    posts = json.loads(DATA.read_text(encoding="utf-8-sig"))
    for p in posts:
        title = p["title"]
        url = p["url"].rstrip("/")
        out_dir = SITE / url
        out_dir.mkdir(parents=True, exist_ok=True)
        html = BASE.replace("{{ title }}", title).replace("{{ content }}", f"<p>Post: {title}</p>")
        (out_dir / "index.html").write_text(html, encoding="utf-8")

if __name__ == "__main__":
    update_index()
    build_posts()


