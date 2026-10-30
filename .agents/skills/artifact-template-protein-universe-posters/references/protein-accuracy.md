# Protein-specific scientific fidelity

Visual references set rendering and composition. Structural sources set the protein. Retain scientific detail while reducing clutter; visual polish is not evidence that topology or chemistry is correct.

## Establish the structural brief

For a named subject, verify relevant primary papers and structural records before generation. Record what affects the image:

- Species, protein/complex, accession and isoform; precursor versus mature protein and numbering convention when residue numbers appear.
- PDB/EMDB/model identifiers actually consulted, biological assembly, state, ligands/cofactors, and coverage. Distinguish biological assembly from crystal asymmetric unit. Check alternative/uncertain assignments; an identifier alone is insufficient validation.
- Subunit types/counts, domain order, major fold topology, flexible/disordered segments, membrane orientation, and central interfaces/pockets.
- Regions measured, modeled, inferred, omitted, or schematic. Do not portray separate domain structures combined into a full-length model as one experimentally resolved conformation.

Use a compact table: **component/chain → identity color → state/position → evidence**. Distinguish chain instances from subunit types when relevant. Preserve identity across states even when leading/trailing or active/inactive roles change.

## Representation-specific checks

| View | Preserve and check |
| --- | --- |
| Ribbon/cartoon | Source-specific secondary-structure arrangement, helix handedness, strand directions, continuous backbone/loops, domain connections, pocket location. Simplify shading, not the fold into arbitrary coils. A single polypeptide cannot branch for composition. |
| Molecular surface | Recognizable envelope, clefts, interfaces, pores, and ligand access. Specify surface interpretation if quantitative. A surface is not a cloud of decorative beads. |
| Space-filling | Coordinate-grounded envelope at atomic scale, with a stated atom/chain scheme. Arbitrary circle illustrations are not exact atomic structures. |
| Ball-and-stick / chemistry | Atom identity, connectivity, bond order where shown, stereochemistry, sourced metal coordination. Give an element legend when departing from conventions. Chain colors must not silently overwrite atom meaning. |
| Binding/catalytic pocket | Distinguish substrate, catalytic residues/cofactor, and remote regulation. Verify residue identity, numbering, and geometry before labeling. Not every cleft is catalytic; do not enlarge a ligand into an impossible fit. |
| Electrostatics / charge | Name the quantity: potential is not identical to residue charge. Computed maps require an actual calculation or sourced result, preparation/conditions, units and scale. Otherwise label illustrative; never invent patches and call them computed. |
| Hydrophobicity | Name the scale/mapping method and surface for computed output. Label conceptual maps illustrative. Decorative colors do not establish affinity, membrane insertion, or hotspots. |
| Dynamics / ensembles | Distinguish observation, simulation, and schematic transitions. Ghosts are related states of the same protein. Do not imply every folded protein is rigid or a few snapshots establish a kinetic trajectory. |

For multiple views, retain identity, assembly, conformation, and camera orientation unless a rotation/state change is identified. Pockets should correspond across ribbon, surface, property-map, and chemical insets. Give identity colors and property maps separate keys; changing representation does not change the molecule.

## Mechanism and scale

- Preserve compartment boundaries, membrane leaflets and accessible sides. Transport arrows follow actual substrate/ion routes; rotation and translation use distinct conventions.
- Preserve stoichiometry, repeated-subunit identity, assembly order, and moving versus stationary parts. Do not add gears or impose symmetry on an asymmetric state.
- Distinguish covalent connections, binding interactions, reactions, and trajectories. Precise PTM/disulfide labeling requires supporting evidence.
- Separate magnifications and abstractions. A free-energy surface is a projection, not cellular terrain; a magnified protein does not physically join an organelle because curves align.
- Use scale bars only with supported geometry/size. Otherwise mark schematic/not to scale. Source or omit exact sequences, residue numbers, rates, values, and quantitative time axes.

## Limits of generation

For structure-informed educational artwork, inspect the relevant structure, specify geometry constraints, and compare the resulting folds/interfaces with it. A PDB citation attached to an invented ribbon does not make it accurate.

When coordinate-faithful structure, exact atoms, or quantitative surfaces are required, use coordinate-derived molecular rendering or a validated supplied structural panel as the geometry basis with available tools. Preserve that geometry during composition and verify stylization against it. Image-generation editing can alter connections despite instructions and cannot guarantee coordinate fidelity. If exact geometry cannot be preserved, identify the limitation and describe the output as schematic rather than claim atomic accuracy.

Source comparison is not experimental validation or independent peer review. Report actual checks and unresolved errors. These updated rules do not retroactively validate earlier generated posters.

## Source anchors

Consult the actual subject's records/papers each time. These sources support the workflow:

- [RCSB PDB-101: biological assemblies](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/biological-assemblies): assembly, asymmetric unit, assignment evidence.
- [UniProt: sequence processing](https://www.uniprot.org/help/sequence_processing): precursor/mature distinction.
- [EMBL-EBI: sequence and isoforms](https://www.ebi.ac.uk/training/online/courses/uniprot-exploring-protein-sequence-and-functional-info/exploring-a-uniprotkb-entry/the-entry-view/sequence-isoforms/): identify the illustrated sequence.
- [APBS workflow](https://apbs.readthedocs.io/en/latest/using/index.html): preparation, parameter assignment, calculation, visualization.
