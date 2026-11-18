# GR-DOS Website Design Specification

**Status:** Approved design direction; implementation handoff  
**Date:** 2026-11-17  
**Target:** [gr-dos.org](https://gr-dos.org/)  
**Layout reference:** [ticoedit.org](https://ticoedit.org/)  
**Project code:** [github.com/gr-dos](https://github.com/gr-dos)

## 1. Design goal

Build a fun, welcoming, old-school website for GR-DOS. It should look like it belongs to the same family of personal websites as TicoEdit and TurboPerl, while remaining clearly identifiable as a DOS operating-system project.

**Core direction: use TicoEdit's *layout* as the model, keep the existing GR-DOS site's blue/yellow header gradient and shared footer, and use the approved handwritten-label 5.25-inch floppy illustration as GR-DOS's identity.**

A useful guiding thought: *a homebrew DOS disk from an alternate 1980s that is still being developed today.*

The site should be playful but functional, readable, fast, and relatively simple. Resist turning it into a contemporary SaaS landing page or a full-screen terminal simulation.

## 2. Source references and what is established

The design is informed by two browser captures supplied on 2026-11-17:

- **Existing GR-DOS placeholder:** two-band blue/yellow gradient header; sunflower icon; large serif “GR-DOS” heading; white page body; compact shared footer with links to sibling websites. Body is otherwise blank.
- **TicoEdit homepage:** the same general two-band gradient; compact icon plus pixel-like `tico` wordmark and block cursor; centered bracketed text navigation; an approximately two-column hero with a large illustrated bird at left and a terminal/editor image within a beige monitor at right; serif text below; narrow, centered reading column; shared footer.

The goal is to borrow the structure and proportions, **not** TicoEdit's bird or its editor-specific wording. Do not infer additional site features from the captures.

### Existing visual conventions to preserve

1. **Keep the existing blue-to-yellow gradients.** They are part of a recurring theme across the owner's websites. Do **not** replace them with a charcoal-only or monochrome DOS theme.
2. **Keep the conventional white main content area**, dark readable text, and fairly traditional typography.
3. **Keep the cross-project footer** and its visual simplicity. Preserve the actual site list/URLs from the implementation, rather than reconstructing them from memory.
4. Use familiar links and headings; no overdesigned card grid, excessive rounded corners, or heavy animations.

## 3. Approved GR-DOS brand artwork

The canonical icon is an **illustrated, slightly tilted 5.25-inch floppy disk**. Use the **latest approved artwork from this conversation**, not one of the earlier concept variants.

### Characteristics locked in

- **Body:** very dark charcoal / near-black, clean and comparatively unworn; subtle material texture and modest highlights.
- **Shape:** credible physical proportions of a 5.25-inch flexible-disk sleeve, not a 3.5-inch hard-shell disk.
- **Angle:** slightly tilted; preserve its energetic, informal posture.
- **Paper label:** warm aged cream, visibly worn and crinkled, placed **off-center toward the left** so that appreciable dark disk surface remains to its right.
- **Label graphics:** blue band and red stripe; bold informal blue handwriting spelling **`GR-DOS`** with an underline. This is intentionally *handwritten*, not typeset corporate branding.
- **Hub:** gray circular ring and center opening.
- **Lower opening:** the narrow vertical slot beneath the hub.
- **Write-protect notch:** higher on the right edge, an **open rectangular cutout**, showing background through the gap. The last edit deliberately removed a spurious connecting line: **do not reintroduce a line or bridge across the open notch**.
- **Background in the approved illustration:** warm pale cream, with a subtle blue cast shadow beneath the disk.

The icon itself has **no eyes, mouth, arms, legs or shoes**. A character mascot may be a future extension, but **not** in the initial site's primary logo.

### Reuse rules

Use **the same underlying floppy** for all of:

- GitHub `gr-dos` organization avatar
- Small header mark on the website
- Large homepage hero illustration
- Favicon and social preview artwork

At very small sizes, simplify fine paper wear and handwriting if necessary, but do not switch to a different floppy design.

**Important:** The approved artwork is a raster illustration produced in the other ChatGPT conversation. Treat it as the visual reference. If a genuine SVG is required, redraw/vectorize faithfully; do not assume the source image is a native editable SVG, and do not embed a raster file inside an SVG while calling it vector art. Obtain the approved PNG explicitly from the owner if it is not present in the website repository.

## 4. Visual style and palette

Use the existing site gradient as the primary unifying brand element. The floppy fits it naturally: blue handwriting/stripe against the light blue end, aged cream against yellow, and a high-contrast dark sleeve.

Suggested supporting colors **for new content** (not mandatory replacements for existing gradient values):

| Purpose | Suggested color |
| --- | --- |
| Floppy sleeve | `#18191F` or comparable near-black charcoal |
| Paper label | `#F3E9CF` |
| Ink blue / selective UI accents | `#23446C` |
| Bright stripe blue | `#1769B5` |
| Warm highlight | `#E9B95F` |
| Body background | `#FFFFFF` |
| Main text | `#111111` |

**Preserve the precise existing header gradient if it can be reused directly from GR-DOS or TicoEdit CSS.** The table above is supporting guidance, not a mandate to recolor established website-family branding.

Avoid gritty faux aging over the entire page. The label may look worn; the disk and interface should remain clean.

## 5. Layout architecture

### 5.1 Header

Use a compact, full-width **two-band horizontal blue/yellow gradient**, visually similar to the current GR-DOS header and the TicoEdit site.

Within it, align the **small floppy icon** and **GR-DOS wordmark** on one line, analogous to TicoEdit's bird icon and `tico` text.

- Replace the sunflower in the placeholder with the floppy mark.
- Prefer a strong, simple wordmark; an optional solid block cursor (`█`) can echo TicoEdit's title treatment.
- Keep the header relatively short. This is not a giant hero banner.
- Make sure the icon remains legible at small display sizes and is not clipped.

### 5.2 Navigation

Immediately below the header, center compact text links in square brackets, matching the general TicoEdit convention:

`[ home | download | documentation | compatibility | development | about ]`

These are **proposed destinations**, not necessarily current routes. The implementation agent should choose actual route names based on the existing site's conventions. Do not present placeholder links as working pages.

An initial release can have fewer links if those pages do not yet exist. Avoid dead links.

### 5.3 Homepage hero

Model the overall composition after TicoEdit:

- **Left:** large approved floppy artwork, with its tilt, label, notch and shadow visible.
- **Right:** a screenshot of GR-DOS running in a period-appropriate monitor illustration or frame.
- The hero should remain balanced; the floppy is the personality, while the monitor demonstrates that GR-DOS is real, working software.
- Do not substitute an unrelated image or generate fake output that could be mistaken for a verified GR-DOS screenshot.
- Prefer an actual DOSBox-X or real-hardware screenshot, e.g. `VER` and `DIR`. Obtain a current verified capture before publishing it as real.
- If no authentic screenshot is ready, use a clearly labeled mockup or leave a clean reserved image area initially.

Below (or alongside, when space permits), use a concise H1, e.g.:

> **A DOS for classic PCs**

Follow with a brief accurate introduction. The implementation agent should confirm technical statements, supported machines, current release/version, and licensing against the GR-DOS repository/docs before publishing them.

### 5.4 Main content

Below the hero, use the TicoEdit approach: **a narrow centered column, serif paragraphs, ordinary headings, normal hyperlinks**, and comfortable whitespace.

Suggested homepage content order:

1. **What is GR-DOS?** Short description and its open development.
2. **Get GR-DOS.** Primary download link, current release and installation entry point (live data/actual URLs only).
3. **Run it on a classic PC.** Supported machine classes and media, only where documented.
4. **What's included?** Concise summary of DOS commands and the surrounding utilities/project ecosystem, without claiming unfinished features are released.
5. **Documentation and source.** Getting started, build/source, GitHub organization.
6. **Project background.** Short note about published MS-DOS 4.0 sources, provenance, licensing, and community development; verify the exact wording against project docs.

Avoid overcrowding the homepage. Longer compatibility tables and installation steps should live on dedicated pages.

### 5.5 Footer

Keep the small, centered, bracketed family-of-projects footer from the existing site, including copyright treatment, with the real set of sibling links already configured.

Do not redesign it into a large multi-column corporate footer.

## 6. Typography

- **Long-form body:** normal, readable serif text, consistent with TicoEdit.
- **Header wordmark:** bold, recognizable GR-DOS text; can have a restrained text-mode/monospace feeling.
- **Commands and terminal output:** monospace.
- **Floppy label:** use the handwritten art as-is, not an HTML font approximation.
- **Accessibility:** legible text sizes, good contrast, clear heading hierarchy.

Use no more fonts than necessary. Prioritize fast loading and ordinary system fonts where practical.

## 7. Responsive behavior

Desktop: centered maximum-width layout with a side-by-side floppy/monitor hero.

Mobile: retain the compact gradient header; let navigation wrap gracefully; **stack the hero elements** without cropping the floppy, hiding the write-protect notch, or making the monitor unreadable.

Images must have sensible aspect ratios and `alt` text. Preserve a comfortable reading width at every size.

## 8. Site assets

Suggested repository asset layout (adjust to the actual framework/build system):

```text
public/
  images/
    gr-dos-floppy.png           # approved, high-res artwork
    gr-dos-floppy-small.png     # optimized icon derivative
    gr-dos-screen.png          # verified real GR-DOS screenshot
    gr-dos-monitor.png         # optional composite/frame
    gr-dos-social.png          # social-card derivative
  favicon.ico
  favicon.svg                  # optional simplified true vector icon
  apple-touch-icon.png
```

Source/master artwork can live separately under `branding/` if useful.

Produce optimized image variants as needed. Use the same floppy for the GitHub org avatar; a 1024×1024 PNG with safe margins is appropriate. Check the image at 32×32 and within a circular crop before applying it.

**Do not upload the GitHub avatar as part of deploying the website unless separately authorized.**

## 9. Terminal styling (optional)

Small DOS text examples are welcome. Keep them simple, for example a static `<pre>` block using authentic GR-DOS output.

A simulated interactive terminal is **not needed for the first version**. If added later it should be clearly simulated, keyboard accessible, and not prevent users from reading the site.

Never hardcode a fictional current version number into an apparently genuine screenshot.

## 10. Implementation notes for the website agent

- First inspect the existing GR-DOS website and, where useful, TicoEdit's HTML/CSS or layout implementation. Reuse shared structural CSS and footer conventions if practical.
- Keep the site's existing deployment mechanism, domain configuration, and content framework unless there is a concrete reason to change them.
- Do not make TLS setup a prerequisite for producing the design; the existing HTTP placeholder is sufficient for incremental work.
- Use semantic HTML, keyboard-accessible links, responsive CSS and descriptive image alternatives.
- Avoid dependencies on heavyweight JS frameworks just for a mostly static homepage.
- Do not fabricate downloads, versions, GitHub release links, screenshots, compatibility or licensing claims.
- Include basic metadata: descriptive page title, summary, favicon, and social preview.
- Keep generated assets and their source/reference provenance organized in the repository.
- Preserve the ability to grow into separate download, docs, compatibility and development pages.

## 11. Proposed delivery sequence

### Phase 1 — Layout and branding

Replace the sunflower; integrate the approved floppy; preserve the gradient and footer; add TicoEdit-style bracketed navigation; implement responsive two-column hero and readable main content.

### Phase 2 — Accurate project content

Connect real download/documentation/source links; add a verified GR-DOS screenshot; review all technical copy against the current repository and releases.

### Phase 3 — Polish and deploy

Optimize images, validate small-screen layouts, check contrast and keyboard access, add favicon/social card, test live deployment. Update the GitHub org avatar separately using the canonical brand asset.

## 12. Acceptance checklist

- [ ] Existing blue-to-yellow gradient is preserved.
- [ ] Existing shared family-of-sites footer is preserved.
- [ ] Sunflower is replaced by the approved GR-DOS floppy.
- [ ] Floppy reproduces the latest approved design, including **dark clean body**, **left-offset aged handwritten label**, **slight tilt**, and **fully open higher right-hand write-protect notch**.
- [ ] Compact bracketed navigation works and has no dead links.
- [ ] Hero follows TicoEdit's basic **illustration left / software monitor right** structure.
- [ ] Body uses a narrow centered reading column and traditional readable typography.
- [ ] Real technical claims and release/download URLs are verified before publishing.
- [ ] Layout works on mobile and desktop without clipping the disk or making content illegible.
- [ ] GitHub avatar and favicon derivatives are visually consistent with the master floppy.
- [ ] Site remains fast, lightweight, accessible and easy to maintain.

---

## One-paragraph brief for implementation

> Evolve the existing gr-dos.org placeholder into a simple, fun, retro-computing website modeled on the ticoedit.org homepage. **Keep the site's blue/yellow gradient and existing cross-project footer.** Replace the sunflower with the approved slightly tilted 5.25-inch GR-DOS floppy illustration (near-black clean body, off-center worn cream sticker, handwritten blue `GR-DOS`, blue/red stripes, and an open write-protect notch). Use a compact header, centered bracketed text navigation, and TicoEdit's two-column hero layout: large floppy on the left, authentic GR-DOS screenshot in a vintage monitor on the right. Follow with readable serif project content, download/documentation links, compatibility information and GitHub source links. Keep it lightweight and responsive. Verify all release and technical claims rather than inventing them.
