# Motion Decomposition

## Build an object tree

Describe the poster as nested parts rather than a flat image.

Example:

```text
poster
├── locked typography
├── printing machine
│   ├── roller
│   │   ├── cylinder
│   │   └── surface marks
│   ├── wheel and handle
│   ├── paper ribbon
│   │   ├── page contour
│   │   └── printed lines
│   └── resulting trace
│       ├── outer ridges
│       ├── inner ridges
│       └── accent mark
└── substrate
    ├── paper grain
    └── registration marks
```

Do not plan motion until the object tree reaches the smallest visually meaningful units.

## Motion-zone selection

Choose two or three zones that can be read at phone size:

1. **Primary action:** carries the metaphor.
2. **Causal support:** explains how the primary action happens.
3. **Human or atmospheric response:** adds touch, scale, or consequence.

More zones are allowed only when the image remains quiet.

## Component examples

### Repeated lines

- Separate neighboring lines or small bands.
- Offset phase and direction.
- Use local ripple, spacing change, dash travel, or curvature change.
- Keep a shared envelope so the field stays coherent.

### Books and paper

- Separate each visible book, page group, cover, bookmark, and contact shadow.
- Use staggered settling and different travel distances.
- Preserve stacking order and occlusion.
- Do not move the entire pile as one rectangle.

### Human figures

- Identify torso, head, upper arm, forearm, hand, tool, and contact point.
- Choose either a full connected silhouette or plausible joint articulation.
- Rebuild the background behind moving limbs.
- Check that the figure does not duplicate or detach.

### Writing and drawing

- Track the tool tip.
- Start the mark exactly at the tip.
- Reveal the stroke along its path.
- Keep the mark attached to the paper plane.
- Synchronize hand movement, tip movement, and mark growth.

### Machines

- Identify input, actuator, transmission, output, and residue.
- Create a causal sequence rather than independent loops.
- Vary the surface texture separately from rigid mechanical motion.

### Translucent material

- Separate the veil, condensation, objects behind it, and surface highlights.
- Move blur, droplets, and silhouettes at different rates.
- Preserve partial visibility and depth.

### Typography

- Decide whether text is locked, decorative, or semantic.
- Keep semantic text stable by default.
- If type participates, animate by word, glyph, baseline, counter, or occlusion—not one arbitrary group transform.

## Flattened artwork

When layers do not exist:

1. Identify what must move.
2. Reconstruct the hidden background.
3. Extract or redraw the moving component with a silhouette-aware mask.
4. Restore locked type above it.
5. Inspect the original position for ghosting.

If clean extraction is impossible, rebuild the component as vector, line, or painted animation rather than exposing a crude mask.
