---
title: "Nano Banana — JSON Schema Prompt Builder"
category: image-generation/meta-prompt
description: "Meta-prompt that converts a creative brief into a reusable JSON schema prompt for any Nano Banana model."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-12
  - SV-17
difficulty: intermediate
tags:
  - nano-banana
  - json-schema
  - meta-prompt
  - structured-prompting
  - reusable
  - google
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_meta_prompt_builder.md
---

# Nano Banana — JSON Schema Prompt Builder

**Objective:** Convert a plain-language creative brief into a structured JSON schema prompt that can be reused, parameterized, and version-controlled for any Nano Banana model. The output is a self-contained JSON object that serves as a repeatable generation template.

**Why JSON Schema Prompting:** Nano Banana models accept structured JSON as prompt input via their text content. This is a community-developed pattern (not a native API feature — `responseSchema` is text-only; images return as base64). The structure reduces ambiguity, makes prompts version-controllable, and enables batch generation with parameter substitution.

**API parameters:**
- `model=` any Nano Banana model (`gemini-2.5-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-image`)
- Pass the JSON as the text content of the generation request
- `quality="high"`, `n=1`

---

## Inputs

- `[CREATIVE BRIEF]` — plain-language description of what the user wants to generate
- `[TARGET MODEL]` — which Nano Banana model will consume the schema (affects available slots)
- `[REUSE INTENT]` — how the schema will be reused (batch variations, character consistency, campaign series, one-off)
- `[OUTPUT STYLE]` — photorealistic, illustration, flat design, 3D render, watercolor, etc.

---

## Constraints (Must / Must Not)

**Must:**
- Output valid JSON that can be pasted directly into a Nano Banana generation request.
- Include all 8 elements of the cross-model prompt grammar (deliverable, subject, action, environment, camera, lighting/style, text/labels, constraints).
- Mark parameterizable fields with `{{VARIABLE_NAME}}` syntax for easy substitution.
- Include a `_meta` section documenting the schema's purpose, target model, and variable descriptions.
- Include a `constraints` section that maps to the model's actual capabilities.

**Must Not:**
- Use `responseSchema` or `response_mime_type` for image generation — those are text-only API features.
- Include API-level parameters (model, n, quality) inside the prompt schema — those belong in the API call wrapper.
- Fabricate Nano Banana API features that don't exist.
- Create schemas so deeply nested that they confuse the model — keep to 2-3 levels max.

---

## Meta-Prompt (Feed This to Claude/GPT to Generate the Schema)

```
You are a prompt engineer specializing in structured image generation prompts
for Google's Nano Banana model family. Convert the creative brief below into
a reusable JSON schema prompt.

CREATIVE BRIEF:
{{CREATIVE_BRIEF}}

TARGET MODEL: {{TARGET_MODEL}}
REUSE INTENT: {{REUSE_INTENT}}

BUILD THE JSON SCHEMA FOLLOWING THESE RULES:

1. TOP-LEVEL STRUCTURE:
   {
     "_meta": { purpose, model, variables, version, author },
     "task": "Generate [deliverable type]",
     "subject": { ... },
     "action": { ... },
     "environment": { ... },
     "camera": { ... },
     "lighting_and_style": { ... },
     "text_and_labels": { ... },
     "constraints": { ... },
     "reference_allocation": { ... }
   }

2. PARAMETERIZE with {{VARIABLE_NAME}} any field the user will swap between
   generations. Document each variable in _meta.variables with:
   - name, type, description, default_value, example_values[]

3. REFERENCE ALLOCATION (model-dependent):
   - Nano Banana 2: up to 10 object + 4 character slots
   - Nano Banana Pro: up to 6 object + 5 character + 3 style slots
   - Nano Banana (original): no role-separated slots
   List each slot with: role, description, what_to_take, what_to_ignore.

4. CONSTRAINTS section must include:
   - style_commitment: the canonical rendering style
   - identity_lock: what must not change between generations
   - failure_conditions: what makes the output INCORRECT
   - quality: "high" or "standard"

5. Keep nesting to 2-3 levels maximum.

6. Output ONLY the JSON — no markdown fences, no explanation.
```

---

## Example: Product Campaign Schema

Given the brief: "Generate hero shots of a wireless earbud case in different environments for a social media campaign."

```json
{
  "_meta": {
    "purpose": "Product hero shots for social media campaign",
    "model": "gemini-3.1-flash-image",
    "version": "1.0",
    "variables": {
      "ENVIRONMENT": {
        "type": "string",
        "description": "The setting where the product is placed",
        "default": "marble countertop with morning light",
        "examples": ["gym bench with towel", "cafe table with espresso", "bedside table at night"]
      },
      "MOOD": {
        "type": "string",
        "description": "The emotional tone of the image",
        "default": "clean and aspirational",
        "examples": ["energetic and active", "cozy and intimate", "minimal and zen"]
      },
      "ACCENT_COLOR": {
        "type": "string",
        "description": "Hex code for the accent color in the scene",
        "default": "#2563EB",
        "examples": ["#F59E0B", "#10B981", "#8B5CF6"]
      }
    }
  },
  "task": "Generate a product hero shot photograph",
  "subject": {
    "product": "Wireless earbud charging case",
    "finish": "Matte white with brushed aluminum hinge",
    "state": "Closed, logo facing camera, slight 15-degree angle",
    "scale_reference": "Product fills ~40% of frame width"
  },
  "action": {
    "product_state": "Static, resting on surface",
    "environmental_motion": "None — frozen moment"
  },
  "environment": {
    "setting": "{{ENVIRONMENT}}",
    "depth": "Shallow — background softly blurred",
    "props": "1-2 contextual objects that reinforce the setting, never competing with the product"
  },
  "camera": {
    "shot_type": "Product close-up",
    "angle": "15 degrees above eye level, slight three-quarter view",
    "focal_length_feel": "85mm equivalent — slight compression, shallow DOF",
    "focus": "Razor sharp on the product logo, background falls off naturally"
  },
  "lighting_and_style": {
    "key_light": "Soft directional from upper left, 45 degrees",
    "fill": "Ambient bounce from the surface",
    "style": "Commercial product photography — clean, aspirational",
    "mood": "{{MOOD}}",
    "color_temperature": "Daylight balanced, slight warm shift"
  },
  "text_and_labels": {
    "text_in_image": "None — clean product shot",
    "logo_visibility": "Product logo must be legible"
  },
  "constraints": {
    "style_commitment": "Commercial product photography — photorealistic, magazine-quality",
    "identity_lock": [
      "Product shape, finish, and proportions must match reference images",
      "Logo placement and size must be accurate",
      "Matte white finish — no color shifts"
    ],
    "failure_conditions": [
      "Product proportions distorted",
      "Logo illegible or misplaced",
      "Product finish appears glossy instead of matte",
      "Background elements compete with product for attention",
      "Style shifts from photorealistic to illustrated"
    ],
    "quality": "high"
  },
  "reference_allocation": {
    "model": "gemini-3.1-flash-image",
    "slots": {
      "obj_1": {
        "role": "Product front reference",
        "description": "Front view of the earbud case showing logo and finish",
        "take": "Exact shape, logo, finish, color",
        "ignore": "Background, lighting"
      },
      "obj_2": {
        "role": "Product angle reference",
        "description": "Three-quarter view showing hinge and depth",
        "take": "Proportions, hinge detail, side profile",
        "ignore": "Background"
      },
      "obj_3": {
        "role": "Environment reference",
        "description": "Photo of the target environment",
        "take": "Surface texture, ambient light quality, color palette",
        "ignore": "Objects in the reference"
      }
    }
  }
}
```

---

## Using the Generated Schema

### Single generation
Paste the JSON (with variables filled in) as the text content of your Nano Banana API request.

### Batch variations
Use a script to substitute `{{VARIABLE}}` values from a CSV or parameter list:

```python
import json, re

schema = json.load(open("product_hero_schema.json"))
schema_str = json.dumps(schema)

variations = [
    {"ENVIRONMENT": "gym bench with towel", "MOOD": "energetic", "ACCENT_COLOR": "#F59E0B"},
    {"ENVIRONMENT": "cafe table with espresso", "MOOD": "cozy", "ACCENT_COLOR": "#10B981"},
]

for params in variations:
    prompt = schema_str
    for key, value in params.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", value)
    # Pass `prompt` as text content to the Nano Banana API
```

### Version control
Store schemas in your project repo. Track changes to prompt structure separately from parameter values.

---

## Iteration Plan

1. "The schema is too deeply nested — flatten the [section] to reduce parsing ambiguity."
2. "Add a new variable for [field] — it needs to change between generations."
3. "The failure_conditions don't catch [specific drift] — add a condition for it."
4. "The reference_allocation is for Nano Banana 2 but I'm using Pro — update the slot layout."

---

## Verification

- [ ] Output is valid JSON (parseable, no trailing commas, no comments).
- [ ] All 8 prompt grammar elements present (task, subject, action, environment, camera, lighting/style, text, constraints).
- [ ] `_meta` section documents purpose, model, and all variables.
- [ ] Variables use `{{VARIABLE_NAME}}` syntax consistently.
- [ ] Reference allocation matches the target model's slot layout.
- [ ] Nesting depth is 3 levels or fewer.
- [ ] No fabricated API features (no `responseSchema` for images).
- [ ] `constraints.failure_conditions` lists at least 3 specific failure modes.
- [ ] Schema can be round-tripped: JSON → string → API call → image.
