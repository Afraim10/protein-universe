# Approved visual system

## Canonical examples

All paths below resolve from the skill root. View the images; prose alone cannot capture the visual standard.

| Image | What to inherit | What is specific to that image |
| --- | --- | --- |
| `assets/reference.png` | Master palette, flat molecular forms, title hierarchy, layered scientific storytelling, footer | The folding landscape, ribbon protein and proteomics questions |
| `assets/atp-synthase.png` | Single machine as hero, selective gold for energy flow, subordinate state inset | Membrane polarity, rotary architecture, open/loose/tight cycle |
| `assets/kinesin.png` | A sweeping directional track, distinct subunit colors, cargo-scale contrast | Plus-end transport, paired motor heads, microtubule lattice |
| `assets/collagen-portrait.png` | Portrait rhythm, long structural motif, separated magnification scales, three-column footer | Triple helix, sequence repeat and staggered fibrillar assembly |

The user's initial references were Kurzgesagt's Quasars, Universe, Evolution Map, periodic-table posters and Space Artbook. Their influence is expressed through the approved images above: a dramatic hero from the Quasar poster, discoverable details from the Evolution Map, and consistent visual vocabulary from the tables. Retain the resulting series style rather than reinterpreting the studio from scratch. Do not add the studio's logo or imply official authorship.

## Color and rendering

Use these approximate working colors as guides, not measured swatches or a rigid per-pixel palette:

| Role | Approximate color |
| --- | --- |
| Main dark field | Midnight navy `#031331` |
| Background depth | Indigo `#111E5B` |
| Primary molecular color | Cyan `#24CDEB` |
| Cool secondary | Turquoise `#18A9C5` |
| Warm partner | Coral `#FF758B` |
| Warm shadow/accent | Magenta `#DB3B9E` |
| Structural complement | Violet `#8858E8` |
| Light complement | Lavender `#B994F5` |
| Sparse functional highlight | Gold `#FFD34C` |
| Main text | Soft white `#F5F7FF` |

- Navy is a substantial visual field, not a narrow border. Lower the contrast of distant objects.
- Cyan, coral and violet carry the main molecular masses. Assign colors consistently to chains or subunits across states.
- Gold is scarce and meaningful: ligand, ATP, proton, chemical tag, cross-link, or a process arrow. It is not random sparkle.
- Construct forms from rounded, interlocking silhouettes, smooth ribbon bands, scalloped color regions and repeated geometric units. Use about 3–5 bounded color regions per component, often just a base color and a darker side plane.
- Suggest depth through overlap, scale, occlusion and flat shadow regions. Small gradients are acceptable where the approved examples use them, but avoid shiny plastic, glossy highlights, ambient-occlusion rendering and atomistic foam.
- Do not drift toward photoreal molecular renders, ornate fantasy paintings, neon haze, mesh textures, fractal detail, metallic machinery or generic cosmic scenery. No faces, human limbs, gears, wheels or mascots unless explicitly requested.
- Molecular curves provide motion. Ghost contours can show alternative conformations, but are subordinate to the primary silhouette.

## Composition and type

The image should work at three distances: striking silhouette across a room, recognizable mechanism at arm's length, and informative labels up close.

- One dominant molecular hero, normally occupying roughly 40–60% of the artwork region. Secondary insets support its story rather than compete with it.
- Reserve roughly 80–84% of the canvas for artwork and title, and 16–20% for the integrated footer. These are proportional guides, not mandatory grids.
- Titles use bold, uppercase white geometric sans-serif forms, normally upper left with short line breaks. The type is large and highly legible. Do not invent a specific font identification from the raster reference.
- Titles in the series include **THE PROTEIN UNIVERSE**, **THE MOLECULAR MOTOR**, **THE MOLECULAR WALKER**, and **THE MOLECULAR WEAVE**. Choose an equally concise new title appropriate to the subject; do not mechanically reuse 'molecular' if awkward. A smaller subtitle names the protein and central idea.
- Use short white or pale-cyan labels, fine leader lines and restrained arrows. Exact wording must be in the generation prompt. Keep paragraphs minimal: one or two brief explanatory sentences at most in the artwork.
- Avoid dashboard cards, elaborate panel borders and equal-weight grids. One small cycle or magnification inset can be enclosed when it improves comprehension.
- Background motifs should be sparse, larger, quieter silhouettes of relevant biology. Empty navy areas are part of the design.

## Orientation-specific behavior

**Landscape, approximately 1.414:1:** title at upper left; broad hero or sweeping track across center; one or two small inset scenes in available negative space; three or four compact footer groups. Use the ATP synthase and kinesin examples for geometry suited to machines and transport.

**Portrait, 2:3:** title high on the page; a long vertical or gently diagonal central motif; side labels spaced along the descent; lower assembly or scale transition; usually three footer groups. Use a long protein, filament, transmembrane assembly, or vertically unfolding process when naturally appropriate. Preserve readable type; do not shrink a four-column landscape footer indiscriminately.

## Scientific footer

The footer connects the biological world to ways of investigating it. It has a thin cyan top rule, a short uppercase heading and compact icons above/beside short captions, without boxed cards. Select only methods relevant to the subject.

Examples: identify proteins or peptides from spectra; quantify abundance; map modifications; measure trajectories; simulate conformational changes or mechanics; connect interactions or pathways. These are complementary approaches, not an obligatory single pipeline. Keep molecular simulation distinct from proteomics, and single-molecule tracking distinct from mass spectrometry.

Use schematic spectra or plots with meaningful axes and no fabricated experimental values. Mark illustrative data when appropriate. A small 'Schematic illustration • not to scale' caption is characteristic of the series. Do not imply that a simple bottom-up spectrum completely identifies every proteoform or resolves protein dynamics.

## Fidelity hierarchy

1. Explicit current user constraints.
2. Scientific correctness of the new subject.
3. The approved final images' visual language.
4. This document's approximate tokens and layout guides.
5. Historical prompts, which record intent but can contain ambiguities or instructions not perfectly achieved.

Preserve overall appearance while correcting misleading details. The references are concept artwork, not atomic models. Do not reproduce errors just to maintain similarity.
