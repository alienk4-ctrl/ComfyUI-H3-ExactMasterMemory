# ComfyUI-H3-ExactMasterMemory

Custom nodes for the MiniMax H3 Reference Director Pro long-form exact-audio path.

## Main node: H3 Exact Master Audio + Memory Sampler

This fills the specific gap in the current H3 ecosystem:

- long-form visual memory / identity continuity;
- fixed REF2VA references across the chain;
- exact prerecorded master audio driving every shot;
- no regenerated/concatenated H3 soundtrack.

It does **not** add a second model or a second diffusion pass.

### Performance design
- master audio resampled once;
- fixed reference images encoded once;
- one audio-VAE target encode per shot;
- generated H3 audio is never decoded;
- final output audio is the original source master timeline;
- text encoder is evicted before sampling when it shares the DiT GPU.

### Recommended Workflow 02 path
REF2VA + Sage + RES multistep + simple + 20 steps.
Use fixed identity/product/style references and memory_frames=2, anchor_frames=1.

### Dependency
When `reference_images` are connected, install the current
`jlucasmcrell/ComfyUI-H3-Multishot`. Its runtime AV-bank patch allows REF2VA
reference rows and chaining keyframes to coexist.

## Utility node: H3 Exact Master Audio Segment
Use this in Motion Context exact-audio graphs. Set overlap_frames to the actual
pinned head size (for example 22) so the H3 generation receives the correct
overlapping slice of the original master soundtrack.

## Validation
- Python source syntax checked.
- Timeline mathematics unit tested.
- GPU/H3 inference cannot be executed in this environment; target-machine smoke
  testing is still required before production release.

## Research basis
- ComfyUI native MiniMax H3 primitives
- ComfyUI-H3-Multishot (MIT)
- h3-audio-injection (MIT)
- MiniMax-H3-NativeAudio-MusicVideo-Workflow (technique reference)
- H3 Motion Context (GPL-3.0; used as an external workflow dependency, no code copied)

## License
This package source is MIT. Models and dependencies retain their own licenses.

## v0.2.0 - Stable interior H3 keyframes

Adds **H3 Keyframes - Stable Interior (MotionContext Patch)**.

This replaces the brittle exact-source-text rewrite used by the older H3
interior-keyframe patch with the current H3 Motion Context positional-wrapper
ABI. Current `ComfyUI-H3-Motion-Context` is required for interior anchors.
First/last-only anchors still work without it.

## v0.2.2 — duplicate-folder cleanup + behavioral patch probe

- `H3StableKeyframes` no longer requires a particular marker attribute.
  It builds a tiny `PackedLayout` probe and verifies that
  `motion_context_index=N` really moves the cond rows to frame N.
- Backup/duplicate `ComfyUI-H3-ExactMasterMemory*` folders inside
  `custom_nodes` are explicitly warned about. Renaming a backup folder is not
  sufficient because ComfyUI imports every valid custom-node folder there.
- The companion installer moves legacy backup copies outside `custom_nodes`.

## v0.3.0 — Workflow UI utility nodes

Adds three beginner-facing utility nodes used by the upgraded Workflow 01:

- **H3 Resolution Preset**
  - one-click resolution/orientation presets
  - avoids raw width/height editing

- **H3 Duration Planner**
  - user enters simple target seconds
  - converts to a valid H3 generation frame count on the 17k+5 grid
  - also outputs exact final delivery frame count

- **H3 Trim A/V To Frames**
  - trims decoded video frames and decoded audio to the requested final duration

This keeps the frontend much cleaner while preserving the validated H3 backend path.


## v0.4.0 — Semantic reference auto-remapping

Stock MiniMax H3 compacts only active references before assigning prompt ordinals.
This breaks fixed-role workflows when optional references are skipped.

New node:
**H3 Semantic Reference Director — Auto Remap**

It accepts fixed logical roles, compacts the active media, and rewrites logical
Picture/Video/Audio tags to the actual active H3 ordinals immediately before
tokenization.

Additional fixes:
- wardrobe top-crop control for references containing another person
- strict missing-tag detection
- H3-safe 32px resolution presets
- short delivery requests generate at least 124 frames before exact trim


## v0.4.1 — semantic prompt preflight fix

Fixes a Workflow 01 failure where the workflow's own role boilerplate could
mention inactive optional references and trigger strict_missing_tags.

Changes:
- missing-reference validation/remapping now happens BEFORE VAE encoding
- genuine bad tags fail immediately instead of after expensive reference encoding
- Workflow 01 v1.4.1 no longer puts the full optional-role dictionary inside
  the actual H3 creative prompt
- motion/video encoding path itself is unchanged from v0.4.0
