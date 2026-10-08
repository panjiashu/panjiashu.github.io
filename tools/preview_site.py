"""Preview current website sources, using the deployed Jekyll head/assets.

This is an integration preview, not a replacement for a full Jekyll build.
Run with --serve to build and serve all reviewed pages on port 8768.
"""
from pathlib import Path
import argparse
import http.server
import re
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "_site" / "review-preview"


def render(text, title="", title_zh=""):
    text = re.sub(
        r"\{%\s*include ([\w-]+\.liquid)\s*%\}",
        lambda m: render((ROOT / "_includes" / m[1]).read_text(encoding="utf-8"), title, title_zh),
        text,
    )
    text = text.replace("{{ page.title }}", title).replace(
        "{{ page.title_zh | default: page.title }}", title_zh
    )
    text = re.sub(
        r"\{\{\s*[\"']([^\"']+)[\"']\s*\|\s*relative_url\s*\}\}",
        lambda m: m[1], text,
    )
    page_path = {"Home": "/", "Projects": "/projects/", "Publications": "/publications/"}.get(title)
    text = re.sub(
        r"\{% if page.permalink == '([^']+)' %\}(.*?)\{% endif %\}",
        lambda m: m[2] if m[1] == page_path else "", text,
    )
    return text


def build():
    DEST.mkdir(parents=True, exist_ok=True)
    cache = DEST / "deployed-home.html"
    try:
        shell = urllib.request.urlopen("https://panjiashu.github.io/", timeout=20).read().decode()
        cache.write_text(shell, encoding="utf-8")
    except OSError:
        shell = cache.read_text(encoding="utf-8")
    # Current controls/scripts/styles override the deployed shell.
    shell = re.sub(
        r'<button id="light-toggle"[\s\S]*?</button>',
        (ROOT / "_includes/theme-toggle.liquid").read_text(encoding="utf-8"), shell, count=1,
    )
    css = re.sub(r"//[^\n]*", "", (ROOT / "_sass/_homepage.scss").read_text(encoding="utf-8"))
    shell = shell.replace("</head>", "<style>" + css + "</style></head>")
    shell = re.sub(r'<script src="[^"]*/assets/js/theme\.js[^\"]*"></script>',
                   '<script src="/assets/js/theme.js"></script>', shell)
    shell = re.sub(r'<script src="[^"]*/assets/js/home-language\.js[^\"]*"></script>',
                   '<script src="/assets/js/home-language.js"></script>', shell)
    shell = re.sub(r'(["\'])/assets/(?!js/(?:theme|home-language)\.js)',
                   r'\1https://panjiashu.github.io/assets/', shell)
    start = shell.index('<article class="home-content">') + len('<article class="home-content">')
    end = shell.rfind('</article>', start, shell.index('</main>', start))
    sublayout = (ROOT / "_layouts/home-subpage.liquid").read_text(encoding="utf-8").split("---", 2)[2]
    for name, title, zh in [("about", "Home", "首页"), ("projects", "Projects", "项目"),
                            ("publications", "Publications", "论文")]:
        body = (ROOT / "_pages" / (name + ".md")).read_text(encoding="utf-8").split("---", 2)[2]
        if name != "about":
            body = sublayout.replace("{{ content }}", body)
        page = shell[:start] + render(body, title, zh) + shell[end:]
        page = re.sub(r'<title>.*?</title>', '<title>' + title + ' | Jia-Shu Pan</title>', page)
        # Source-page images/PDFs must be current local assets, not older deployed copies.
        for path in re.findall(r'(?:src|href)="(/assets/[^"?#]+)', page):
            source = ROOT / path.lstrip("/")
            target = DEST / path.lstrip("/")
            if source.is_file():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        folder = DEST if name == "about" else DEST / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(page, encoding="utf-8")
    shutil.copytree(ROOT / "feature-information-dynamics", DEST / "feature-information-dynamics", dirs_exist_ok=True)
    scripts = DEST / "assets/js"
    scripts.mkdir(parents=True, exist_ok=True)
    for name in ("theme.js", "home-language.js"):
        shutil.copy2(ROOT / "assets/js" / name, scripts / name)
    print("Preview built from current website sources: " + str(DEST))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--port", type=int, default=8768)
    args = parser.parse_args()
    build()
    if args.serve:
        from functools import partial
        server = http.server.ThreadingHTTPServer(
            ("127.0.0.1", args.port), partial(http.server.SimpleHTTPRequestHandler, directory=str(DEST))
        )
        print(f"Serving http://127.0.0.1:{args.port}/", flush=True)
        server.serve_forever()
