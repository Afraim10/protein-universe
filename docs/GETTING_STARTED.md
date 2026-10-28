# Create your first poster

## 1. Choose a compatible environment

Use Codex with image-generation capability, file access, and preferably web research. Capabilities and account access depend on your host. The skill does not enable missing tools. These examples were made with the built-in image generator in the desktop environment.

## 2. Open the repository

Download the repository ZIP and extract it, or clone the repository. Open its root folder as your Codex workspace. The repo-local skill lives inside `.agents/skills/`.

For use in another project, copy the entire `artifact-template-protein-universe-posters` folder into that project's `.agents/skills/` directory, including `assets/` and `references/`. Do not copy only SKILL.md.

See the current [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and installation details specific to your host. Reload your workspace if needed.

## 3. Ask for a concrete subject

Example prompt:

> Use $artifact-template-protein-universe-posters to create a portrait poster about human carbonic anhydrase II. Use simple flat colors and lighting. Show the fold, molecular surface and catalytic zinc pocket. Verify the mechanism with primary structural sources. Label illustrative property maps clearly. Save the final image and its prompts, sources and limitations.

In a host that does not support the `$` selector, ask Codex to read the skill's SKILL.md file at its repository path and follow it.

## 4. Review the result

Check the scientific story, membrane compartments, chain connections, residue labels, charge/atom legends, arrow directions and equation. Ask for focused corrections. Do not treat visual polish as evidence of accuracy. Read the [review guide](SCIENTIFIC_REVIEW.md).

## 5. Save and share

Keep the image with the exact prompt, references and limitations. Credit this workflow when redistributing or adapting its material; see the license. A new generated output's permissions also depend on the generation service and material you supply.

If image generation is unavailable, the skill can help prepare a specification, but cannot itself render a poster. Do not upload credentials or API keys to the repository.
