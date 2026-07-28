# Humanist Motion Grammar

## Four motion modes

### Continuous

Use for:

- currents;
- fingerprint ridges;
- flowing parallel lines;
- light, fog, and scanning;
- rotation with optical continuity.

Render at 24 or 30 distinct frames per second. Keep neighboring components phase-offset rather than synchronized.

### Held stop motion

Use for:

- figures;
- hands;
- pencils;
- paper collage;
- mechanical gestures;
- objects that should feel physically repositioned.

Render in a 24 fps container but hold each pose for 2–4 frames. Vary hold lengths slightly when appropriate.

### Progressive mark

Use for:

- writing;
- drawing;
- printing;
- highlighting;
- scanning;
- assembling or erasing.

The visible result must originate at the active contact point.

### Material breathing

Use for:

- grain;
- condensation;
- translucent film;
- soft shadow;
- registration;
- blur.

Keep amplitude low and local. Atmospheric motion supports the main action; it must not become generic noise.

## Neighbor choreography

For repeated elements, derive motion from a shared field plus local variation:

```text
local motion = shared envelope
             + alternating direction
             + per-element phase
             + small amplitude variance
             + material irregularity
```

Do not use independent randomness every frame. Seed variations so forms remain recognizable and loops remain stable.

## Ripple behavior

For rings, ridges, pages, keys, or stacked units:

- group motion into nearby bands;
- alternate direction or delay across neighbors;
- vary amplitude gradually;
- allow one disturbance to travel across the system;
- preserve a stable overall silhouette unless transformation is the idea.

A fingerprint should feel like many ridges responding to a current, not a circular image layer spinning.

## Physical contact

Contact creates credibility:

- pencil tip touches the page;
- hand grips or releases the object;
- book lands on another book and changes its shadow;
- roller touches paper;
- lens movement changes the scanned line.

Check contact points frame by frame.

## Human anatomy

- Prefer whole connected silhouettes when source resolution is limited.
- Rotate limbs around plausible joints.
- Keep hands attached to wrists and tools attached to grips.
- Avoid masks that cut through anatomy.
- If extraction breaks the body, move a larger contiguous region or rebuild the limb.

## Loop design

- Use integer motion cycles for seamless continuous loops.
- Return position, rotation, opacity, and phase to their starting state.
- For writing or falling sequences, design a quiet reset through occlusion, page advance, fade, or cut.
- Do not reverse a physical action merely because it is convenient unless the reversal feels intentional.

## Amplitude

Check motion at the intended display size:

- primary action must be visible without staring;
- secondary action should be discoverable;
- atmospheric action may remain subtle;
- text and layout should not drift.

If only one motion point is visible, strengthen or simplify the plan.
