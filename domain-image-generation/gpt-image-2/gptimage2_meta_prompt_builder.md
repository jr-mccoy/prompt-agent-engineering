---
title: "GPT Image 2 Meta-Prompt Builder"
category: image-generation/meta-prompt
description: "Converts a one-line image brief into a fully-structured gpt-image-2 prompt with the right parameters, text-rendering contract, and constraints."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - QA-01
  - SV-11
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - gpt-image-2
  - meta-prompt
  - prompt-builder
  - image-generation
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/gpt-image-2/README.md
---

# GPT Image 2 Meta-Prompt Builder

**Objective:** Take a short, possibly vague image brief and emit a production-grade gpt-image-2 prompt that uses the 5-section structure, picks the right parameters, and includes a text-rendering contract when needed.

**When to use:**
- You have a one-line brief ("logo for a coffee co-op", "ad for our new hiking pack").
- You don't want to hand-write the full structured prompt.
- You want the output to follow the patterns in [`../GPT_IMAGE_2_GUIDE.md`](../GPT_IMAGE_2_GUIDE.md).

**When NOT to use:**
- You already have a structured 5-section prompt — just send it.
- You're editing an existing image — use [`gptimage2_surgical_edit_change_preserve.md`](gptimage2_surgical_edit_change_preserve.md) instead.

---

## Inputs

Provide:
- **Brief:** one or two sentences describing the desired image.
- **Use case:** ad / editorial / UI mockup / infographic / product hero / logo / social post / slide / merch / other.
- **In-image text (optional):** verbatim copy that must appear in the image.
- **Brand or identity refs (optional):** description of any brand colors, fonts, mascots, or reference images.
- **Hard constraints (optional):** must-have orientation, must-not-have elements, audience, regulatory requirements.

---

## Constraints (Must / Must Not)

**Must:**
- Output a complete prompt block ready to paste into the OpenAI API or ChatGPT.
- Use the 5-section structure: SCENE / SUBJECT / KEY DETAILS / USE CASE / CONSTRAINTS.
- Recommend `size`, `quality`, and `n` explicitly.
- If the brief includes any in-image text, include a verbatim text-rendering contract (quoted text, font, hex color, placement, "100% readable at full resolution") and require `quality="high"`.
- Strip out slop words ("stunning", "masterpiece", "8K", "ultra-detailed", "trending on ArtStation").
- State a style commitment up front if the brief implies non-photorealistic output.

**Must Not:**
- Pass `input_fidelity` (disabled in gpt-image-2).
- Recommend an output edge ≥ 3840 px or a non-multiple-of-16 size.
- Recommend a long-to-short aspect ratio above 3:1.
- Invent brand names, statistics, or copy that the user did not provide.
- Add web-search-grounded facts unless explicitly requested.

---

## Instructions

1. **Parse the brief.** Identify subject, scene, use case, and any text.
2. **Pick `size`** based on use case:
   - Square social → `1024×1024`
   - Mobile portrait → `1024×1536`
   - Slide / banner / web hero → `1536×1024`
   - 2K hero → `2560×1440`
   - Cinematic 3:1 / 1:3 → `2880×960` / `960×2880`
   - 4K (only when explicitly requested) → `3824×2144`, flag as experimental
3. **Pick `quality`:**
   - In-image text, dense infographic, identity-sensitive portrait → `high`
   - Most production work → `medium`
   - Throwaway variants, rapid ideation → `low`
4. **Pick `n`:**
   - Logo / ad creative pool → `n=4`
   - Otherwise → `n=1`
5. **Determine style commitment.** State photorealistic / illustrated / painterly / etc. up front in CONSTRAINTS to block thinking-mode realism bias if needed.
6. **If text is present**, build the verbatim text contract.
7. **Write the prompt** using the template in the Output Format below.
8. **Self-check** against the validation block.

---

## Output Format

Emit exactly this structure:

```
=== GPT IMAGE 2 PROMPT ===

SCENE:
[Environment, time of day, lighting, atmosphere — concrete visual facts.]

SUBJECT:
[Primary focus. Scale and framing. Pose / gaze / interaction.]

KEY DETAILS:
[Materials, textures, secondary objects, expressions, color cues — name hex codes when relevant.]

USE CASE:
[ad / editorial / UI mockup / infographic / product hero / logo / slide — establishes polish level.]

CONSTRAINTS:
- Style commitment: [photorealistic / illustrated / painterly / etc.]
- EXACT TEXT (verbatim, no extra characters): "[copy]" — [font style], [weight], [hex color], [placement], 100% readable at full resolution.
- Preserve: [non-negotiables]
- Forbidden: [things that must not appear — watermarks, lorem ipsum, additional people, etc.]
- Format: size [WxH], orientation [landscape/portrait/square], n=[N]

=== API PARAMETERS ===

model: gpt-image-2
size: [WxH]
quality: [low|medium|high]
n: [N]
background: [opaque if product extraction; otherwise omit]

=== RATIONALE (one line each) ===
- Why this size: [...]
- Why this quality: [...]
- Why this n: [...]
- Style commitment reason: [...]

=== ITERATION PLAN (next 3 single-axis follow-ups if Phase 1 misses) ===
1. [single-change follow-up #1]
2. [single-change follow-up #2]
3. [single-change follow-up #3]
```

---

## Verification

Before emitting, confirm:

- [ ] All 5 sections present and non-empty.
- [ ] `size` is multiple-of-16 on both edges, edge < 3840, ratio ≤ 3:1.
- [ ] `quality="high"` whenever EXACT TEXT is in the prompt.
- [ ] No slop words remain.
- [ ] No `input_fidelity` mentioned.
- [ ] No invented brand names, copy, or stats beyond what the user provided.
- [ ] Style commitment stated if output should not be photorealistic.
- [ ] Iteration plan is single-axis per step (one change per follow-up).

If any check fails, fix it before emitting.
