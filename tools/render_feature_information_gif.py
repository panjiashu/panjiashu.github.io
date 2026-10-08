"""Capture the canonical project page for the code repository's README."""
import argparse
import io
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('--url', default='http://127.0.0.1:8767/feature-information-dynamics/?lang=en')
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--browser', help='Optional Chromium executable path')
args = parser.parse_args()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(**({'executable_path': args.browser} if args.browser else {}))
    page = browser.new_page(viewport={'width': 1100, 'height': 1000})
    page.goto(args.url, wait_until='domcontentloaded')
    page.wait_for_function("document.documentElement.lang === 'en' && document.querySelector('.chart-formula .katex') !== null")
    page.select_option('#sample', label='Digit 3')
    page.add_style_tag(content='.demo-footnote{display:none!important}.chart-step:not(:first-child) .chart-caption{display:none!important}.charts{grid-template-columns:repeat(4,minmax(0,1fr))!important}')
    # Keep the first plot's legend, but omit explanatory captions from every plot.
    page.evaluate("""() => {
        const caption = document.querySelector('.chart-step .chart-caption');
        const labels = [...caption.querySelectorAll('span')];
        caption.replaceChildren(labels[0], document.createElement('br'), labels[1]);
    }""")
    panel = page.locator('section.panel').filter(has=page.locator('#slider'))
    frames = []
    for index in range(page.evaluate('data.levels.length')):
        page.evaluate('(index) => choose(index)', index)
        page.evaluate('async () => { await Promise.all([...document.querySelectorAll(".pictures img")].map(img => img.decode())); }')
        frames.append(Image.open(io.BytesIO(panel.screenshot())).convert('RGB'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(args.output, save_all=True, append_images=frames[1:],
                   duration=[1000] + [150] * (len(frames)-2) + [1500], loop=0, optimize=True)
    print(f'{len(frames)} frames written to {args.output}')
    browser.close()
