# Prompt construction and targeted review

## Choose a story before choosing decorations

For an open-ended request, pick a protein whose geometry or mechanism has a clear visual organizing principle: an enclosing chamber, a branching network, a rotary or translating motor, a molecular gate, a scaffold, a folding/assembly hierarchy, or a switch. Explain the choice in one or two sentences and proceed. Previously completed subjects are protein ensembles, ATP synthase, kinesin-1 and collagen; these are references, not an exhaustive topic list.

Verify claims before committing them to the image. RCSB PDB-101 and primary structure/mechanism papers are useful; EMBL-EBI supports proteomics methods. Avoid quantitative claims unless necessary and sourced. Choose an actual protein family/member so a mechanism belonging to one member is not universalized across the family.

## Prompt skeleton

Fill this with a concrete design rather than forwarding unresolved alternatives to image generation:

```text
Use case: scientific-educational.
Create one [landscape approximately 1.414:1 / portrait 2:3] full-bleed science art poster.
Title: "[EXACT TITLE]". Subtitle: "[EXACT SUBTITLE]".

STYLE: Match the approved Protein Universe poster series: sophisticated Kurzgesagt-inspired flat vector illustration, midnight navy and indigo ground, saturated cyan/turquoise against coral/magenta/violet, sparse gold reserved for [FUNCTION]. Smooth precise contours, interlocking rounded silhouettes, broad clean ribbon bands, 3–5 bounded solid color regions per object, a simple darker side plane. Depth through overlap and scale. Bold white geometric sans-serif title. Dark breathing room. Not glossy 3D, atomistic foam, metal machinery, neon haze or ornate fantasy art. No studio logo, watermark, frame or photographed mockup.

COMPOSITION: [One specifically located dominant hero, its silhouette and relative size.] [Orientation-specific reading path.] [One or two subordinate insets, only where useful.] Background objects are sparse quiet silhouettes of relevant biology.

MOLECULAR ARCHITECTURE: [Subunit/chain count if critical; topology; compartment and membrane orientation; identity-preserving colors; continuous connections; state/direction and transport mechanism.] Distinguish [MAIN POTENTIAL CONFUSION]. Schematic structure, not a claimed experimental model.

STORY: [One clear scientifically grounded action or structural hierarchy.] Show [explicit state ordering / causal arrows / separate scales]. [Exact label placement and leader destination.]

TEXT: [List exact title, labels, short captions and allowed footnotes. No additional invented paragraphs, sequences or measurements.]

FOOTER: A narrow dark band with thin cyan rule, heading "[HEADING]", [three/four] unboxed icon/caption groups. [Specify method and caption for each, distinguish measurements from simulations.] Schematic plots with meaningful axes and no fabricated empirical values. Small caption "Schematic illustration • not to scale" and illustrative-data note where appropriate.

FINISH: Collectible scientific poster, dramatic at thumbnail size and rewarding up close. Maintain the approved series' visual identity and readable hierarchy.
```

For new generation, obey the image tool's current input schema, including any restriction on attaching reference paths. Viewing an image is not the same as passing it into generation. For an edit, inspect the target first and use supported reference-image inputs. Never silently substitute HTML/SVG drawing for requested image-generation artwork.

## Inspect the actual result

Review the image, not just the prompt. Check both a whole-image view and the small scientific insets when necessary.

**Series fidelity:** correct aspect; dark ground; dominant hero; consistent palette; flat bounded shading; sparse purposeful gold; meaningful silhouette; legible title/labels; integrated footer. The most common observed drift was excessive plastic/3D shading and noisy molecular detail. Flatten it while preserving composition rather than rebuilding an otherwise good poster.

**Mechanism:** arrows point to the intended destination; state labels agree with actual order; subunit identities and colors persist through frames; membrane sides and transport direction agree; moving and stationary components are distinct; numbers of chains/heads are credible; protein connections do not accidentally branch; differing scale views remain separated.

**Evidence:** captions avoid unsupported numbers; charts and sequences do not masquerade as measured data; a network edge is not an unexplained reaction arrow; schematic status is clear. Generic protein surfaces need not be atomically exact, but the illustrated mechanism should not contradict the explanation.

Examples of checks learned from this series (apply only when relevant):

- Folding landscapes represent free-energy projections and multiple accessible states, not a physical hole in a cell or a mandatory single route. Functional disorder has a legitimate place. A conformational change is not automatically a new proteoform.
- ATP synthase: proton paths belong at the membrane rotor/stator interface, not through the central shaft. Matrix-facing catalysis, stationary support and rotation should agree. A simple catalytic inset must depict open → loose → tight → open in the intended synthesis direction. Do not draw a direct TCA-cycle-to-motor energy conversion.
- Kinesin-1: two heads preserve identity while changing leading/trailing roles; a three-frame schematic can be AB → BA → AB. Check motion arrows as well as labels. Plus-end transport applies to conventional kinesin-1, not every kinesin. Microtubules are hollow tubulin assemblies, not DNA.
- Collagen: three chains, not DNA's two; Gly–X–Y is a repeat, not a full sequence; strand colors do not imply three different chain types. An enlarged molecular segment should not physically become the larger-scale fibril in the drawing. Fibrillar assembly is not the entire biosynthetic pathway.

## Refinement prompt pattern

```text
Preserve the successful composition, title, exact wording, orientation, palette and [specific retained features]. Correct only:
1. [Observable scientific/text error with explicit desired geometry or state order.]
2. [Observable visual drift.] Replace glossy modeling with clean bounded flat colors; remove excess detail and quiet the background. Keep the same architecture and identity colors.
3. [Other necessary targeted correction, if present.]
Do not add unrelated objects or paragraphs. Keep full-bleed artwork and the established series style.
```

Do not correct unobserved failures automatically. If no material issue is visible, deliver the first generation. If correction introduces another error, inspect and address that specific error within the bounded review loop; never claim a diagram is validated merely because it looks polished.

## Retained prompt records

The exact original generation and refinement prompts are retained for provenance and adaptation:

- `approved-prompts/protein-universe.md`
- `approved-prompts/atp-synthase.md`
- `approved-prompts/kinesin.md`
- `approved-prompts/collagen-portrait.md`

Each path is relative to this reference directory. Read only the relevant record. These prompts are historical evidence, not a requirement to repeat every original instruction or subject.
