# Production and QA

## Layer preparation

- Work from the highest-resolution final poster.
- Keep a pristine source.
- Separate locked type, moving art, reconstructed background, and atmospheric overlays.
- Use alpha masks that match silhouettes.
- Feather only where the material requires softness; do not hide bad extraction with blur.
- Match reconstructed paper color, grain, noise, and lighting to neighboring pixels.

## Tool choice

- Use vector or code-based animation for lines, typography, paths, diagrams, and repeat systems.
- Use image editing or frame painting for organic cutouts and background reconstruction.
- Use compositing tools for masks, occlusion, and layer timing.
- Use video encoding tools that preserve orientation and aspect ratio.
- Choose the tool that preserves editability and edge quality rather than forcing every job through one method.

## Frame rate and cadence

- Default container: 24 fps.
- Smooth optical motion: 24–30 unique frames per second.
- Hand-made held motion: 6–12 unique poses per second inside the container.
- Keep duration between 5 and 8 seconds unless requested otherwise.

## Encoding

- Default to H.264 MP4.
- Preserve source aspect ratio.
- Confirm pixel dimensions, duration, codec, and file size.
- Avoid accidental orientation transforms.
- Do not trust source frames alone; inspect the encoded video.

## Required inspection

1. Extract at least three frames from the encoded file.
2. Compare them with the source poster.
3. Check:
   - upright orientation;
   - no mirroring;
   - no crop change;
   - exact typography;
   - moving-part continuity;
   - restored backgrounds;
   - no visible mask shapes;
   - no duplicated original beneath moved art;
   - readable amplitude;
   - loop closure.
4. Inspect contact points and anatomy at 200%.
5. Inspect the whole composition at phone size.

## Storyboard proof

Provide a representative storyboard when practical:

- start;
- early action;
- peak action;
- settle or loop return.

For repeated systems, select frames that reveal neighboring elements moving differently.

## Common failures

| Failure | Cause | Correction |
|---|---|---|
| visible circle or rectangle | moving a crop instead of components | rebuild or mask sub-components |
| ghost object | original not removed | reconstruct hidden background |
| broken hand | mask cuts anatomy | move a contiguous region or articulate joints |
| floating writing | path not tied to tip | calculate contact point and reveal from it |
| motion barely visible | amplitude judged only at full size | test on phone and strengthen primary action |
| everything moves alike | shared easing and phase | vary neighbors with a coherent field |
| muddy image | excess texture and dark overlays | restore light field and reduce atmosphere |
| upside-down video | coordinate mismatch during encoding | inspect encoded frame and fix transform |
