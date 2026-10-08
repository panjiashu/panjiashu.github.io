# Website change audit — 2026-10-08

The personal website repository is the source of truth for the website. The
experimental repository's archived templates and generated pages are historical
artifacts and must not overwrite `feature-information-dynamics/index.html`.

## Findings and repairs

- The old integration-preview directory and project-page generator were moved to
  `Documents/Codex/_archive/feature-information-dynamics-development-20261008`.
  The old local server was no longer listening on port 8768.
- The archived generated article differs from the website: it contains clipping
  explanations and a finite-range cumulative-information formula. The website
  retains the requested concise explanation and integral from negative infinity.
  Preserve the website version; do not rebuild it from the archived generator.
- Added `tools/preview_site.py`, which builds the local preview directly from
  current website pages, shared includes, styles, scripts and project assets.
  Fixed missing local homepage images and restarted the preview on port 8768.

## Verified retained requirements

| Requirement | Verification |
| --- | --- |
| Home / Projects / Publications everywhere | Source includes and actual browser navigation |
| Six publications including DID and VFScale, no summaries on Publications | Six rendered cards; zero summary elements |
| Project PDF / arXiv / Code / BibTeX buttons | Four rendered buttons; populated BibTeX |
| Notebook link in the article, without a hero button | One in-text notebook link |
| Direct generation-order question before Sander's account | Article source and rendered page |
| Power-law spectrum explains limits of pixel spectral autoregression | Article source and rendered page |
| Hero conclusion explicitly names diffusion models | Rendered text |
| Hero question and conclusion use identical typography | Same computed family, size, weight, line-height and color |
| MMSE symbols explained before interactive panel | Source and rendered notation paragraph |
| Four panels: loss → MMSE gap → feature density → accumulated nats | Rendered panel titles and equations |
| Definitions use coloneqq, cumulative integral starts at negative infinity | Rendered MathJax equations |
| Chaining introduced generally, then frequency example | Rendered chain section |
| Aligned representation comparison and stable class/mask/Canny terms | Source and figure retained |
| Closing conjecture and research contact | Rendered closing section |
| Projects bilingual switch reuses homepage preference | Clicked EN and Chinese; checked visible content |
| System default and shared visible control | Cleared preference; default System rendered |
| Local Home → Projects → article → Publications navigation | Clicked the full route successfully |

Existing language tests: 3 passed. `git diff --check`: passed.
Desktop screenshots were inspected for the article, Publications and Chinese
Projects. This is an integration preview using the deployed Jekyll head and
global assets, not a complete local Jekyll build. All edits remain unpublished.

## Rebuilding the preview

Run `python tools/preview_site.py --serve` from this repository. Open
`http://127.0.0.1:8768/`. The generated preview is under the ignored `_site/`
directory. Re-run the builder after source edits; no experimental template is
involved.


## Navigation follow-up

Top navigation contains only page destinations: Home (/), Projects (/projects/), Publications (/publications/). No homepage section anchors are mixed in. Shared include marks the current page; the standalone research article marks Projects as its current section. Verified all four routes in the local browser. Unpublished.
