# Bilingual Homepage Redesign

## Goal

Turn the existing al-folio site into a one-page bilingual academic homepage inspired by Huanran Chen's information architecture while preserving the existing Jekyll deployment and bibliography pipeline.

## Content

- A left identity rail with the user-provided Milky Way photograph, name, Westlake affiliation, location, academic links, CV, and language control.
- A right long-form page with anchored sections: About Me, Research, Selected Publications, Personality & Hobbies, and Contact.
- About Me states that Jia-Shu Pan started his Ph.D. at Westlake University in Fall 2025 under Prof. Tailin Wu, frames research as reducing confusion about the world, and focuses on interactions between data structure and model learning. Previous experience is limited to the Australian National University visit.
- Research highlights the NeurIPS 2026 submission on feature information dynamics and uses the supplied FID curve figure.
- Selected Publications contains only the NeurIPS 2026 submission and VFScale (ICLR 2026), with consistent author emphasis, venue labels, and paper/code links.
- Hobbies briefly covers running and anime/ACG culture.

## Visual System

- Keep al-folio's typography and light/dark tokens but replace the standard top-navigation homepage with a two-column editorial layout.
- Use a compact sticky identity rail on desktop and a stacked identity card on mobile.
- Use restrained blue accents, thin separators, compact publication metadata, and generous reading width.
- Crop the second supplied Milky Way image with CSS using a centered `object-fit: cover` treatment; preserve the source asset.

## Bilingual Behavior

- English is the server-rendered, no-JavaScript fallback and default language.
- All navigation and page content has English and Chinese variants in the same document.
- An `EN / 中文` control switches visible language, updates `document.documentElement.lang`, and stores the preference in `localStorage`.
- On later visits, the stored preference is restored before normal interaction. The control is keyboard accessible and exposes its state to assistive technology.

## Implementation Boundaries

- Preserve Jekyll, GitHub Pages deployment, social configuration, and bibliography rendering where useful.
- Add a homepage-specific layout/include and stylesheet rather than rewriting the entire theme.
- Keep publication metadata in BibTeX and add small homepage-specific markup only where bilingual copy or the DID feature block requires it.
- Convert the supplied PDF figure into a web-friendly high-resolution image while retaining the original PDF as a downloadable source if practical.

## Verification

- Unit-test the language preference and switching helper with Node's built-in test runner before wiring it into the page.
- Build the site with the repository's documented Jekyll command.
- Check desktop and mobile layouts, both languages, internal anchors, external links, image loading, dark mode, and no-JavaScript English fallback in a browser.
