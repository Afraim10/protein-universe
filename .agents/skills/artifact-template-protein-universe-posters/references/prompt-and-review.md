# Production and targeted review

## Make a concrete brief

Choose one story and a composition arising from its biology. Read the primary image and relevant entries in the reference study, then use the accuracy guide to establish:

- **Evidence:** species, assembly/state, structural sources and their limits, critical fold/interface/mechanism details.
- **Color:** component/chain identity families, shadow/highlight variations, background family, focal event, separate legends for property maps.
- **Space/time:** dominant subject and reading path, subordinate scenes, state ordering, magnification boundaries, camera changes.
- **Text:** exact title, labels, brief explanatory captions, relevant footer and schematic/data qualifiers.

These are concise working notes, not a mandatory extra user-facing approval step. Use already supplied information and make routine art-direction decisions autonomously.

## Prompt scaffold

Resolve choices before generation. Adapt the scaffold to the subject rather than forwarding every option:

```text
Create one [orientation and aspect] full-bleed scientific art poster.
Title: "[EXACT TITLE]". Subtitle: "[EXACT SUBTITLE]".

STYLE ANCHOR: The approved The Protein Universe — Life in Motion poster.
Rich graphic scientific illustration: dark navy/indigo/aubergine ground,
clean organic silhouettes, layered bounded colors, hue-shifted shadows,
selective bright accents and restrained local gradients. Depth from overlap,
scale and contrast hierarchy. Detailed protein geometry, crisp editorial
finish; not shiny plastic, photoreal rendering, atomistic foam, neon haze,
metal machinery, generic cosmic decoration or a boxed dashboard.
No studio logo, watermark, frame or room mockup.

COLOR SCRIPT: [Hero chain/subunit → family mapping]. [Partner and environment
families]. [Shadow/highlight relationships]. Reserve the strongest local
contrast for [event/site]. Background [specific biological forms] stay
[quiet colors/contrast]. Maintain identities through every state and inset.
[Property/atom-map legends and their separate meaning, if needed.]

COMPOSITION: [Specific hero position, scale, silhouette and camera].
[One strong reading path arising from the mechanism]. [Secondary scenes
and magnifiers in particular negative spaces]. [Quiet dark channels].
[Clearly separated times/scales]. Rich discoveries up close without making
every molecule, particle or label equally prominent.

MOLECULAR ARCHITECTURE: [Organism/member, state and source-derived shape].
[Subunit count/order, topology, continuous connections, domains, actual
fold features, interfaces, ligands and correct compartment orientation].
[Exact details that must survive simplification]. [Known schematic regions].
For ribbons preserve helix/strand/loop geometry; for surfaces preserve the
envelope and pocket; for atoms preserve chemistry. Do not replace a named
protein with an unrelated decorative fold. [Identity-preserving state changes].

STORY: [Grounded process and causal order]. [Substrate/ion/rotation paths].
[What is enlarged, abstract or illustrative]. Keep physically different
objects and time points distinguishable even where contours echo.

TEXT: [Exact permitted wording and leader targets; no invented paragraphs,
residue numbers, sequences or measurements]. Bold white geometric title,
quieter captions on uncluttered fields. Preserve the requested infographic
detail by hierarchy and local magnification, not by removing it.

FOOTER: [Heading, relevant unboxed groups with exact labels and short captions].
Subordinate dark strip, restrained thin rule, sufficient text size.
[Meaningful axes; illustrative-data qualifier when applicable].
[Schematic / scale / composite note appropriate to the actual output].

FINISH: One readable story at thumbnail size; scientific and visual detail
at full size. Maintain the primary reference's warm–cool balance, broad
color masses, dark breathing room, and layered graphic depth.
```

For an explicitly requested simple-lighting variant, change the rendering clause to fewer hard-edged internal tones. Preserve composition, structural detail, colors, annotation density, and molecular identity. Do not use a blanket “remove almost all detail/3D” instruction.

Use the tool's actual schema for new generation versus editing and reference inputs. Inspect an edit target first. Viewing a reference is not the same as attaching it to generation. Do not claim an attachment was used if it was only visually inspected. Do not silently substitute code-drawn artwork for requested image generation.

## Inspect the actual output

Use a whole-image view and necessary enlarged details. Compare with the primary reference, not only with the latest generated poster.

1. **Hierarchy:** Does the eye find the main event before the labels? Are broad warm/cool masses separated by quiet dark space? Are background forms subordinate? Is the image rich without uniform sparkle, equal contrast, or cyan dominating all roles?
2. **Rendering:** Are hue-shifted shadow regions and selective highlights giving shape? Are folds readable? Has the image drifted into glossy plastic or, conversely, featureless two-tone stickers? Correct the specific drift.
3. **Structure:** Compare source-informed architecture, subunit count, chain continuity/colors, domains, fold and pocket locations. Check the representation-specific rules; count visually instead of trusting the prompt.
4. **Mechanism:** Check labels and arrowheads against state order, compartments, moving/stationary parts and actual transport routes. Distinguish multiple time points and magnifications.
5. **Information:** Check all text, leader endpoints, legends, repeated labels, equations, plot axes, and source/scale qualifiers. Data-looking maps need an honest computed/illustrative status. An identifier alone does not validate the drawing.

Examples carried forward from the series, only when relevant:

- Folding landscapes are projections with multiple accessible states, not cellular holes or a compulsory single route. Functional disorder matters. A conformational change is not automatically a distinct proteoform.
- ATP synthase: ion paths at the rotor/stator interface, not through the central shaft. Check organism-specific orientation, moving/stationary parts and catalytic state order. Matrix-facing catalysis refers to mitochondrial context; do not generalize it to bacteria.
- Conventional kinesin-1: two heads retain identities while exchanging leading/trailing roles (AB → BA → AB). Check direction arrows. Do not generalize its plus-end motion to every kinesin. Microtubules are tubulin assemblies, not DNA.
- Collagen: distinguish three-chain helix from DNA, a Gly–X–Y repeat from a complete sequence, chain instances from types, and molecular magnification from fibril-scale assembly.
- Repeated-subunit diagrams: count labels as well as units; a repeated Rpt label can leave another subunit missing even when the ring has six shapes. Treat retained examples as fallible references.

## Refine without losing what works

```text
Preserve [successful geometry, composition, identity mapping, text and palette].
Correct these observed issues only:
1. [Scientific/text error: explicit intended structure, label or direction].
2. [Visual hierarchy issue: named component too bright/dull, missing warm
countermass, background competing, or illegible overlap].
3. [Rendering issue if present: replace specular gloss with bounded chromatic
shadows OR restore selective highlight/hue layers to overly flat forms].
Keep topology, interfaces, chain identities, information content and scale
separations intact. No unrelated objects, paragraphs or generic replacement fold.
```

Do not apply corrections to unobserved problems. If the first image succeeds, deliver it. Limit correction attempts as specified in SKILL.md and state unresolved errors honestly. Save exact prompts, source links/identifiers, reference roles, actual checks, and limitations beside the selected output. Historical approved prompts remain provenance, not higher-priority production instructions.
