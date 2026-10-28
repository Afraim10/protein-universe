---
name: artifact-template-protein-universe-posters
description: Create or refine protein biology and computational proteomics posters in the approved Protein Universe visual style, using retained reference images. Use for companion posters, molecular machinery illustrations, and landscape or portrait designs in this series.
---

# Protein Universe Posters

Produce original science posters that look like members of the user's approved series. Preserve its specific visual language, rather than approximating a generic colorful science infographic. The user values dramatic molecular beauty, technical precision, and a finished image, not merely a proposed concept.

## Load the visual reference

1. Read `artifact-template.json`, resolve its retained image paths relative to this skill, and read [the design specification](references/design-system.md).
2. Inspect `assets/reference.png` with the image viewer before composing a new poster. This is the approved final **Protein Universe** image and the primary style authority. For a portrait, also inspect `assets/collagen-portrait.png`; for machinery or motion, inspect the closest of `assets/atp-synthase.png` and `assets/kinesin.png`. Paths are relative to this skill, not the current workspace.
3. Read [prompt construction and scientific review](references/prompt-and-review.md). Read the relevant historical prompt under `references/approved-prompts/` only when it helps with a similar composition.

The retained images are style and composition references, not validated atomic structures. Scientific errors or simplifications in a reference must not be propagated. Follow explicit user changes over these defaults.

## Make the poster

- Infer a suitable subject when the user asks for another interesting protein. Choose one clear mechanism or structural hierarchy with a strong silhouette; do not present a long menu or ask the user to select unless needed. Do not repeat the four existing subjects unless requested.
- Honor the requested orientation. Otherwise use landscape approximately 1.414:1; portrait is 2:3. Keep the subject and layout newly designed while preserving the series' visual grammar. A portrait is recomposed, never squeezed or cropped from a landscape.
- Briefly announce the concept and why it suits the composition. Verify specialist biological claims using primary research or authoritative structural resources such as RCSB PDB and EMBL-EBI. Identify compartment, directionality, subunit identity, and relevant mechanistic states before generating.
- Use an available image-generation tool for raster artwork; if the host provides an **imagegen** skill, follow it. This package supplies instructions, not a model or API access. If image generation is unavailable, explain the missing capability and provide the prompt without claiming to have generated artwork. Follow the actual tool's rules for new generation versus editing and reference attachments; do not invent a reference-image parameter. Inspect retained references and describe their visible traits explicitly even when new-generation calls cannot attach them. Use exact local paths for supported edits.
- Build a subject-specific prompt from the guide. Preserve the dark background, cyan/coral/violet palette, flat bounded shading, dominant hero, sparse meaningful annotations, and integrated scientific footer. The studio name alone is insufficient to specify the style.
- Generate one poster by default. Inspect the result for science, text, orientation, and resemblance to the approved final images. When there is observable drift or an error, make a targeted edit that preserves successful content. Do not perform an obligatory second generation when the first already succeeds, or regenerate indefinitely. After two unsuccessful correction passes, report the remaining limitation rather than claim it is resolved.
- Save the chosen final PNG and a concise `art-direction-and-prompts.md` containing the exact generation/refinement prompts, scientific sources, and material schematic limitations in a new named directory under the active workspace's `output/`. Never overwrite the retained reference images. Include the final image/download link and brief concept explanation. State built-in generation was used. Do not claim that a raster concept is a print-ready vector master or an experimentally derived structure.

## The visual acceptance standard

Match the approved **final** posters, not their more glossy first drafts. At thumbnail size there should be one clear molecular subject, a bold white title, a dark field, and controlled cyan/coral contrast. At full size there should be clean silhouettes, readable captions, purposeful gold accents, and scientifically coherent detail. Preserve this design system across subjects; do not freeze the first poster's specific proteins, words, or arrangement into every new image. Visual fidelity is the target, not a promise of pixel-identical generative output.

## Public distribution

This independent AI-assisted series credits Kurzgesagt as visual inspiration; it is not affiliated with or endorsed by the studio. Included PNGs are generated series examples, not original studio posters. Keep scientific sources and limitations with new outputs. Never label illustrative charge, hydrophobicity, or energy maps as computed results. Current preference is simple lighting and broad flat color regions.

## Latest flat-color references

Also inspect `assets/egfr-flat.png` for landscape work or `assets/proteasome-flat.png` for portrait machinery. These newer examples establish the preferred simpler lighting; keep older images as composition references. Preserve scientific distinctions rather than copying their simplified molecular geometry.
