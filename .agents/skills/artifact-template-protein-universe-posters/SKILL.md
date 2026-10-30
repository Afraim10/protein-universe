---
name: artifact-template-protein-universe-posters
description: Create or refine protein biology and computational proteomics posters in the approved Protein Universe visual style, using retained reference images. Use for companion posters, molecular machinery illustrations, and landscape or portrait designs in this series.
---

# Protein Universe Posters

Create original scientific posters with the visual hierarchy of **The Protein Universe — Life in Motion**, the user's strongest style reference. Combine rich graphic color and layered storytelling with protein-specific structural detail. Simplify rendering, not molecular topology. A finished image is the usual deliverable.

## Load the right references

1. Read `artifact-template.json` and [the design system](references/design-system.md). Inspect `assets/reference.png`; it outranks later series examples for color, lighting, atmosphere, and composition.
2. Read [the reference study](references/reference-study.md). If its private reference library is present, inspect two or three examples relevant to the new composition, rather than attaching all sixteen. The screenshots guide art direction, never biological facts.
3. Read [production and review](references/prompt-and-review.md) and [protein accuracy](references/protein-accuracy.md). Inspect a secondary series image only for a useful subject/layout precedent: `assets/collagen-portrait.png`, `assets/atp-synthase.png`, or `assets/kinesin.png`. If present, `assets/egfr-flat.png` and `assets/proteasome-flat.png` illustrate optional simpler lighting; they do not override the primary reference.

Resolve paths from this skill directory. Historical prompts under `references/approved-prompts/` preserve provenance; their blanket flattening instructions are superseded by this design system. Existing images are schematic artwork, not validated structures.

## Produce the poster

- Choose one compelling protein story when the user leaves the subject open. Prefer a distinctive fold, interaction, motion, or assembly; check the conversation to avoid repeating subjects unintentionally. Honor requested orientation; otherwise landscape is approximately 1.414:1 and portrait 2:3. Recompose for orientation.
- Briefly explain the concept. Verify specialist claims with primary research and authoritative structural resources. Establish species, assembly/state, topology, chain-color mapping, and distinct magnification scales before generation. Keep these decisions concise in the working notes.
- Use available image-generation tools, following the host's **imagegen** skill when provided. This skill supplies art direction, not a model or generation access. Inspect references and translate visible features into the prompt; obey the actual tool's attachment rules. If generation is unavailable, say so and supply the specification without claiming an image was made.
- Default to **layered graphic depth**: bounded color shapes, hue-shifted shadows, selective highlights, coherent color families, and a quiet dark environment. Retain detailed infographics and structure-specific molecular geometry. A request for simple lighting changes shading, not chain identity, topology, information content, or color hierarchy.
- Generate one image unless the user requests variants. Inspect actual output against the primary reference and scientific brief. Correct observed failures specifically; do not automatically flatten everything. After two unsuccessful correction passes, report the unresolved limitation instead of claiming success.
- Save the selected PNG and `art-direction-and-prompts.md` in a new named directory under the workspace's `output/`. Record exact prompts, references actually used, structural sources, chain/property-color legends, and material limitations. Preserve retained assets. Deliver the image with a brief concept explanation; report the tool actually used and real dimensions. Do not equate upscaling with structural validation or a vector master.

## Acceptance and reference handling

At thumbnail size: one dominant story, dark breathing room, distinguishable warm/cool masses, readable title. Up close: coherent folds and interfaces, persistent chain identities, deliberate highlights, useful labels and insets. Accuracy takes priority over decorative symmetry or palette convenience.

This independent AI-assisted series credits Kurzgesagt as visual inspiration without implying official authorship or endorsement. The optional `assets/private-style-references/` library contains user-supplied third-party artwork for personal reference only. Exclude that entire directory from public repositories, downloads, and licensing of the original generated series. Public guidance remains usable with the retained generated examples.
