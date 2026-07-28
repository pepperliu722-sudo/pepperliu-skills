---
name: animate-humanist-posters
description: Turn finished posters, covers, editorial graphics, campaign images, or still illustrations into detailed 5–8 second humanist motion videos, cinemagraphs, loops, or stop-motion pieces. Use when Codex needs to animate a static design while preserving its typography and art direction; create tactile hand-drawn, frame-by-frame, collage, print, ripple, writing, paper, machine, figure, or object motion; or plan and produce granular motion where small constituent parts move independently instead of applying generic whole-object transforms.
---

# Animate Humanist Posters

## Purpose

Translate a still composition into motion without losing its taste. Animate the smallest meaningful parts, preserve the poster’s hierarchy, and make movement reveal how the visual idea works.

Do not redesign the poster unless the user asks. Treat the finished, typeset still as the source of truth.

## Required workflow

1. Inspect the full-resolution poster and record:
   - canvas and crop;
   - exact text and locked brand elements;
   - focal relationship;
   - materials and edge behavior;
   - foreground, middle ground, background, and occlusion;
   - every object’s internal structure.
2. State the motion job in one sentence: what should feel alive, what should remain quiet, and what the viewer should notice.
3. Build an object tree before proposing effects. Read [references/motion-decomposition.md](references/motion-decomposition.md).
4. Mark a lock list. Keep headlines, support copy, metadata, URL, logos, and critical layout stable unless text animation is explicitly requested.
5. Choose two or three motion zones. Each zone may contain many micro-components.
6. Propose at least two different motion narratives. Change cadence, cause, sequence, and focal action—not only amplitude.
7. For every zone, specify:
   - component granularity;
   - physical or visual cause;
   - direction;
   - amplitude;
   - cadence;
   - phase;
   - loop behavior;
   - occlusion and background restoration;
   - relationship to neighboring components.
8. Write a motion plan. Use [references/motion-plan-example.json](references/motion-plan-example.json) as a shape and run `scripts/validate_motion_plan.py` when practical.
9. Prepare clean layers. Reconstruct the background under anything that will move. Never leave the original object underneath a shifted copy.
10. Animate with a mixed cadence:
    - smooth continuous motion where continuity is the idea;
    - held or stepped poses where hand-made rhythm is the idea;
    - progressive reveal where marks are being drawn, printed, scanned, or assembled.
11. Render the complete video, not only frames. Extract representative frames from the encoded file and verify orientation, crop, duration, typography, and layer integrity.

Read [references/motion-grammar.md](references/motion-grammar.md) before building motion. Read [references/production-and-qa.md](references/production-and-qa.md) before encoding and delivery.

## Granularity rule

Animate the smallest meaningful unit that carries the metaphor.

- A fingerprint contains ridges; animate individual ridges or local waves, not one circular crop.
- A stack of books contains books, pages, covers, bookmarks, and shadows; stagger them rather than floating one block.
- A line field contains neighboring lines; vary direction, phase, spacing, and amplitude.
- A machine contains roller, wheel, handle, paper, ink, and output; connect their actions causally.
- A person contains a contiguous body and plausible joints; move the whole silhouette or articulated limbs without breaking anatomy.
- Writing contains hand, tool, tip, contact point, emerging mark, and paper; the mark must begin at the moving tip.
- Typography contains glyphs, words, lines, counters, and baselines; animate only when meaning and legibility survive.
- Condensation or grain contains many small marks; use local variation rather than one opacity pulse.

Do not interpret “two or three motion points” as two or three large cutouts. Use two or three readable zones with detailed internal motion.

## Motion causality

Every movement must have a reason:

- a roller turns, therefore paper advances;
- a pencil touches paper, therefore a mark grows from the tip;
- a hand releases text, therefore pieces fall and settle;
- a scanning lens moves, therefore the active line changes;
- a current passes through lines, therefore neighboring lines respond with phase offsets.

Avoid unrelated simultaneous motion.

## Neighbor variation

Adjacent repeated elements must not move identically.

Vary at least two of:

- direction;
- amplitude;
- speed;
- phase;
- hold length;
- path curvature;
- spacing;
- opacity or registration;
- start and settle time.

Alternating direction is useful but not sufficient by itself. Preserve an overall rhythm so the result feels authored rather than random.

## Cadence

- Use 24 or 30 fps for smooth loops, drawing contact, flowing lines, ripples, scanning, or optical continuity.
- For stop-motion character, hold drawings inside a 24 fps container at an effective 6–12 poses per second.
- Mix cadences only when the contrast has meaning.
- Use eased or irregular motion sparingly; do not apply one sine wave to every element.
- Design the first and last frame as a loop when looping is required.

## Layer integrity

- Restore or reconstruct the hidden background before moving a layer.
- Use masks that follow the object silhouette; avoid visible circles, rectangles, or elliptical patches unless they are part of the design.
- Keep translucent materials translucent.
- Re-composite locked type above moving artwork when necessary.
- Inspect edges at 200% for halos, seams, duplicated limbs, ghost objects, and crop jumps.
- When the source is flattened, prefer local reconstruction, vector rebuilding, or detailed re-drawing over crude whole-object extraction.

## Typography

- Keep required copy upright, non-mirrored, stable, and readable.
- Do not animate all text merely because it exists.
- If letters fall, stretch, blur, or write themselves, keep at least one stable reading state.
- Preserve exact wording and line breaks.
- Keep UI, CTA, and factual copy static unless the user explicitly requests otherwise.

## Default delivery

- Duration: 5–8 seconds.
- Aspect ratio: preserve the source unless the user requests another crop.
- Container: H.264 MP4 unless another format is requested.
- Frame rate: 24 fps by default.
- Audio: none unless requested.
- Deliver the final video, representative storyboard frames, and editable or reproducible source when practical.

## Anti-patterns

- one circular cutout rotating over a static original;
- whole-poster zoom, parallax, or floating as the only motion;
- every object bobbing on the same sine wave;
- moving a stack as one rigid rectangle when its parts are visible;
- disconnected hands, duplicated people, broken joints, or ghosted objects;
- handwriting that does not start at the pen or brush tip;
- static original imagery visible beneath a moved copy;
- motion so small that only one element can be perceived;
- motion so broad that the poster’s hierarchy collapses;
- mirrored or upside-down encoding;
- animating text at the cost of reading.

## Quality gate

Do not deliver until every answer is yes:

1. Are there two or three clearly readable motion zones?
2. Does each zone animate meaningful sub-components?
3. Do adjacent repeated elements differ in at least two motion properties?
4. Is every movement causally related to the visual idea?
5. Are bodies, hands, tools, and contact points intact?
6. Has the hidden background been restored?
7. Are locked words unchanged and legible?
8. Is the motion visible at phone size?
9. Does the encoded file play upright and non-mirrored?
10. Is the duration 5–8 seconds unless otherwise requested?
11. Does the loop avoid an obvious jump when looping is required?
12. Does the result feel handcrafted rather than template-driven?

## Handoff

Provide:

- one-sentence motion concept;
- motion-zone list and component granularity;
- duration, frame rate, size, codec, and loop notes;
- final encoded video;
- storyboard or representative frames;
- editable layers, frame sequence, or reproducible script when practical;
- brief QA note covering direction, anatomy, text, seams, and motion visibility.
