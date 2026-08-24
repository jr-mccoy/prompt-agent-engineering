# Video Generation Prompt Guide

**Purpose:** Authoritative guide for creating AI video generation prompts, focused on Google Veo 3 / Veo 3.1. Based on official documentation, community best practices, and empirical testing of what produces cinematic-quality results.

**Key Insight:** Video generation models understand film grammar. The more precisely you communicate using cinematic language — shot types, camera movements, lighting setups, and audio layers — the more the model behaves like a cinematographer who gets your vision on the first take.

**Related Guide:** For image generation prompts, see [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md).

---

## The 7 Core Elements

Every effective video prompt should address these elements. Not all are required for every prompt, but the more you include, the more control you have.

### 1. Shot Framing & Camera Motion

**Problem:** Vague camera instructions like "show the scene" produce generic, static compositions.

**Solution:** Use professional cinematography terminology. Veo is trained to interpret standard film terms.

**Shot Types:**
| Term | Description |
|------|-------------|
| Extreme close-up (ECU) | Detail shot — eyes, hands, textures |
| Close-up (CU) | Face or single object fills frame |
| Medium close-up (MCU) | Head and shoulders |
| Medium shot (MS) | Waist up |
| Medium wide shot (MWS) | Knees up |
| Wide shot (WS) | Full body with environment |
| Extreme wide shot (EWS) | Landscape with tiny subject |
| Over-the-shoulder (OTS) | Camera behind one character looking at another |
| Dutch angle | Tilted camera for tension or unease |
| POV | First-person perspective |

**Camera Movements:**
| Term | Description |
|------|-------------|
| Static / locked-off | No camera movement |
| Pan left/right | Horizontal rotation on fixed point |
| Tilt up/down | Vertical rotation on fixed point |
| Dolly in/out | Camera moves toward/away from subject |
| Tracking / lateral dolly | Camera moves alongside subject |
| Crane shot | Camera moves vertically through space |
| Orbit / arc | Camera circles around subject |
| Steadicam / handheld | Subtle organic movement |
| Rack focus | Shift focus between foreground and background |
| Zoom in/out | Lens zoom without camera movement |

**Example:**
```
BAD: "Show a person walking down a street"
GOOD: "A slow dolly forward follows a woman in a navy trench coat from behind as she walks down a rain-slicked cobblestone alley at dusk. Medium shot, shallow depth of field, warm street lamp lighting."
```

---

### 2. Style & Visual Aesthetic

**Problem:** Without style direction, the model defaults to a generic "stock video" look.

**Solution:** Specify the visual approach explicitly — film genre, era, format, or artistic style.

**Effective style descriptors:**
- Film genres: "film noir shot on 35mm," "80s VHS aesthetic," "Wes Anderson symmetrical framing"
- Camera/lens references: "shot on Arri Alexa," "anamorphic lens flare," "85mm portrait lens at f/1.4"
- Artistic styles: "claymation," "anime," "photorealistic," "watercolor animation," "stop-motion"
- Lighting moods: "golden hour backlighting," "harsh overhead fluorescent," "neon-lit," "dappled forest light," "volumetric fog rays"
- Color grading: "teal and orange color grade," "desaturated," "high contrast black and white"

**Example:**
```
"Cinematic 35mm film look with warm color grading. Shallow depth of field. Anamorphic lens with subtle horizontal flare. Natural lighting from a window camera-left."
```

---

### 3. Subject & Character Details

**Problem:** Generic character descriptions produce inconsistent, forgettable subjects.

**Solution:** Use specific, distinctive visual markers. Describe as if explaining to someone over the phone.

**Include:**
- Age, build, distinguishing features
- Clothing (specific items, colors, textures)
- Hair (style, color, length)
- Expressions and micro-expressions
- Props they carry or interact with

**Example:**
```
"A woman in her thirties with auburn hair pulled back in a loose bun, wearing a charcoal peacoat and silver-rimmed glasses. She pauses on a cobblestone bridge, her breath visible in the cold air, and looks directly at the camera with a knowing smile."
```

**Character consistency across clips:** Keep a character bible — repeat the same detailed description verbatim across prompts. Similar prompts yield similar-looking characters.

---

### 4. Setting & Atmosphere

**Problem:** Missing environmental detail forces the model to invent context, often generically.

**Solution:** Paint the scene with sensory detail — location, time, weather, objects, textures.

**Include:**
- Specific location type (not just "outdoors" but "a cluttered Victorian study")
- Time of day and season
- Weather and atmospheric conditions
- Key props and environmental details
- Ambient texture (dust motes, steam, rain puddles, etc.)

**Example:**
```
"A bustling Tokyo street market at night: neon signs reflecting in rain-puddles, steam rising from food stalls, paper lanterns swaying in the breeze."
```

---

### 5. Action & Movement

**Problem:** Static descriptions produce static scenes. Overly complex action sequences get confused.

**Solution:** Describe specific movements with temporal progression. For complex scenes, break action into "beats."

**Principles:**
- Specify what the subject IS doing, not just what they look like
- Use movement quality keywords: "graceful," "energetic," "hesitant," "deliberate"
- For fast-paced scenes, provide play-by-play timing
- Keep action scope appropriate to clip duration (see Duration section below)

**Example:**
```
"A barista methodically tamps espresso grounds, places the portafilter into the machine, and pulls a shot. Steam rises as dark espresso flows into a white ceramic cup."
```

---

### 6. Dialogue & Audio

**Problem:** Audio is either missing, mismatched, or generates unwanted subtitles.

**Solution:** Veo 3+ generates synchronized audio from text prompts. Format dialogue and sound cues explicitly.

**Dialogue formatting:**
```
CRITICAL: Use "says:" with a colon to prevent subtitle generation.

GOOD: Character says: "We have to leave now."
BAD:  Character says "We have to leave now."

Always add: "No subtitles, no text overlay, no captions."
```

**Three audio layers to specify:**

| Layer | Description | Example |
|-------|-------------|---------|
| **Dialogue** | Character speech with emotional tone | `She says softly: "I knew you'd come back."` |
| **Sound Effects** | Specific environmental sounds | `SFX: thunder cracks in the distance, glass shatters` |
| **Ambient** | Background soundscape | `Ambient: quiet hum of a starship bridge, distant engine vibrations` |

**Tips:**
- Use phonetic spelling for unusual proper nouns to ensure correct pronunciation
- Specify emotional tone: "says nervously," "whispers," "shouts with frustration"
- Target ~8 seconds of speaking to avoid rushed or garbled audio
- Specify ambient audio to prevent "audio hallucinations" like unwanted audience laughter
- Explicitly describe background soundscape: "the quiet hum of an office," "forest rustling"

---

### 7. Technical Specifications

**Problem:** Without explicit technical parameters, outputs may not match intended format or quality.

**Solution:** Specify duration, aspect ratio, and negative constraints.

**Duration guidance:**
| Duration | Best For |
|----------|----------|
| 4 seconds | Establishing shots, product showcases, minimal movement |
| 6 seconds | Narrative content, dialogue scenes, multi-stage actions |
| 8 seconds | Complex sequences, extended dialogue, multiple actions |

**Aspect ratios:**
| Ratio | Use Case |
|-------|----------|
| 16:9 | Standard widescreen (default) |
| 9:16 | Vertical mobile / social media |
| 1:1 | Square format |

**Negative prompt (elements to exclude):**
```
Always include: "No subtitles, no text overlay, no captions, no watermarks, no lens distortion, no camera shake."
```

---

## Prompt Length & Structure

### Optimal Length

Aim for **100-300 words** (roughly 3-6 sentences):
- Under 100 words: outputs feel generic
- 100-300 words: sweet spot for detail vs. clarity
- Over 400 words: model may struggle to prioritize, results become unpredictable

### Recommended Structure

**Short-form (evocative, for simple scenes):**
```
A slow-motion close-up of a honeybee landing on a sunflower. Golden hour light
catches translucent wings. Macro lens, shallow depth of field. Sound of gentle
buzzing and distant wind through grass.
```

**Long-form (detailed, for complex scenes):**
```
Shot: Medium shot, slow dolly forward.
Setting: A dimly lit jazz club in 1950s Harlem. Smoke drifts through amber stage
lighting. Dark wood tables with white tablecloths.
Subject: A saxophone player in his forties, wearing a rumpled brown suit and
loosened tie. Eyes closed, sweat beading on his forehead.
Action: He leans into a solo, fingers moving fluidly over the keys. He opens his
eyes briefly, nodding to the pianist off-screen.
Audio: Warm tenor saxophone solo over soft piano comping and brushed drums.
Ambient crowd murmur and clinking glasses.
Style: Shot on 35mm film, warm grain, shallow depth of field. Teal and amber
color palette.
No subtitles, no text overlay.
```

---

## JSON Prompting (Advanced)

A major breakthrough discovered in mid-2025: complex JSON structures produce dramatically superior results for Veo 3, providing granular control over every aspect.

### JSON Prompt Template

```json
{
  "scene": {
    "setting": "A cluttered Victorian cartographer's study",
    "time": "Late afternoon, golden hour light through dusty windows",
    "atmosphere": "Warm, scholarly, slightly mysterious"
  },
  "camera": {
    "shot_type": "Medium shot",
    "movement": "Slow dolly forward",
    "lens": "50mm, shallow depth of field",
    "angle": "Eye level, slightly low"
  },
  "subject": {
    "description": "A cartographer in his sixties, round spectacles, burgundy vest over white shirt",
    "action": "Traces a route on an ancient map with his index finger, then looks up",
    "expression": "Determined curiosity shifting to quiet excitement"
  },
  "dialogue": {
    "line": "According to this sea chart, the lost island exists. We sail at dawn.",
    "delivery": "Measured, building to quiet conviction",
    "format": "Speaking directly to someone off-camera"
  },
  "audio": {
    "ambient": "Ticking clock, distant rain, creaking wood",
    "sfx": "Paper rustling as finger traces the map",
    "music": "None"
  },
  "style": {
    "visual": "Cinematic, warm color grade, shot on 35mm",
    "lighting": "Golden hour window light, practical lamp on desk",
    "reference": "Barry Lyndon candlelight aesthetic"
  },
  "technical": {
    "duration": "6 seconds",
    "aspect_ratio": "16:9",
    "negative": "No subtitles, no text overlay, no watermarks"
  }
}
```

**When to use JSON:** Complex scenes with multiple elements that need precise coordination — especially scenes combining dialogue, specific camera work, and layered audio.

**When to use text:** Simple scenes, quick iterations, and when the evocative quality of prose helps convey mood better than structured data.

---

## Multi-Shot Storytelling

### Maintaining Consistency Across Clips

For multi-clip narratives, consistency is the primary challenge. These techniques help:

**1. Character Bible**
Prepare 6-8 expressions/poses as reference descriptions. Reuse the exact same character description across all prompts:
```
Character: Maya — early thirties, dark curly hair to shoulders, olive skin,
angular jaw, wearing a faded denim jacket over a black turtleneck, silver
hoop earrings.
```

**2. Scene Continuity**
- Repeat the same palette descriptors and time-of-day across connected shots
- Use the same lighting description (changing lighting mid-sequence breaks immersion)
- Switch to tripod or dolly shots for transitions — stable movement reduces visual discontinuity

**3. Frame Conditioning (Veo 3.1)**
- Generate shot N to a clean last frame, then use that frame to start shot N+1
- This preserves motion vectors, subject orientation, and lighting continuity
- Reference image support: up to 3 images for first/last frame control

**4. Seed Consistency**
- Reuse the same `seed` value across related shots for stylistic consistency
- Combine with consistent palette and lighting descriptors

### Shot Planning Approach

Break narratives into individual "beats" rather than trying to describe entire sequences:

```
Beat 1 (Establishing): Wide shot of the lighthouse at dawn. Waves crash against rocks.
Beat 2 (Introduction): Medium shot of the keeper opening the heavy door, lantern in hand.
Beat 3 (Discovery): Close-up of her face as she notices something unusual on the horizon.
Beat 4 (Reaction): Over-the-shoulder shot as she raises binoculars, hands trembling slightly.
```

---

## Iterative Workflow

### The Refinement Process

Getting perfect output on the first attempt is rare. Follow this workflow:

1. **Start simple** — test with a short, clear prompt at lower resolution
2. **Evaluate** — identify what's 80% right and what needs adjustment
3. **Refine specific elements** — add detail to weak areas, don't rewrite everything
4. **Lock working elements** — once camera/style/character works, keep those exact words
5. **Run variations** — the same prompt produces slightly different output each run
6. **Scale up** — move to higher resolution and longer duration after validating

### Resolution & Cost Strategy

| Phase | Resolution | Duration | Purpose |
|-------|-----------|----------|---------|
| Prompt testing | 720p | 4 seconds | Rapid iteration, low cost |
| Refinement | 720p | 6 seconds | Validate timing and narrative |
| Production | 1080p | 6-8 seconds | Final quality output |

**Cost tip:** Disabling audio generation reduces costs by 33-50% during prompt iteration phases.

---

## Common Problems & Solutions

### Problem: Generic, stock-video look

**Add to prompt:**
```
Shot on Arri Alexa with anamorphic lenses. Subtle film grain. Shallow depth of
field with natural bokeh. [Specific color grade] color palette.
```

### Problem: Subtitles or text overlays appear

**Add to prompt:**
```
Character says: "dialogue" (use colon before quotes)
No subtitles. No text overlay. No captions. No on-screen text whatsoever.
```

### Problem: Audio doesn't match visuals

**Add to prompt:**
```
Explicitly describe all audio layers:
Ambient: [specific environmental sounds]
SFX: [specific sound effects tied to actions]
Dialogue delivery: [emotional tone, volume, pace]
```

### Problem: Characters look different across clips

**Solution:** Create a character bible and repeat it verbatim:
```
Reuse exact description across all prompts. Include: age, build, hair (style/color),
distinguishing features, specific clothing items with colors.
```

### Problem: Action is too complex for clip duration

**Solution:** Decompose into beats:
```
Instead of one 8-second prompt with 5 actions, create:
- Beat 1 (4s): Actions 1-2
- Beat 2 (4s): Actions 3-5
Use frame conditioning to connect beats.
```

### Problem: Camera movement feels unnatural

**Solution:** Use specific cinematography terms:
```
BAD: "The camera moves around the subject"
GOOD: "Slow 180-degree orbit around the subject, starting from camera-left
profile to camera-right three-quarter view. Steadicam smooth."
```

### Problem: Wrong aspect ratio or framing

**Solution:** Specify explicitly:
```
Aspect ratio: 16:9 widescreen.
Subject centered in frame with headroom.
No vertical format. No square crop.
```

---

## Veo 3 / 3.1 API Parameters

When using Veo through Vertex AI or other API integrations:

| Parameter | Values | Notes |
|-----------|--------|-------|
| `prompt` | string | Main generation prompt (100-300 words optimal) |
| `negativePrompt` | string | Elements to exclude ("subtitles, watermarks, text") |
| `durationSeconds` | 4, 6, 8 | Clip length |
| `aspectRatio` | "16:9", "9:16", "1:1" | Frame format |
| `generateAudio` | boolean | Enable/disable audio generation |
| `seed` | integer | For reproducibility and style consistency |
| `enhancePrompt` | boolean | Auto-enrichment with cinematic terminology (default: on) |

**Note:** Disable `enhancePrompt` when you want precise control without automated additions.

---

## Quality Checklist for Video Generation Prompts

Before finalizing any video generation prompt, verify:

- [ ] Specifies shot type and camera movement using film terminology
- [ ] Includes visual style direction (not just "cinematic")
- [ ] Describes subject with distinctive, specific visual markers
- [ ] Sets environment with sensory detail (lighting, weather, textures)
- [ ] Scopes action appropriately for clip duration
- [ ] Formats dialogue with colon syntax and subtitle prevention
- [ ] Layers audio: dialogue + SFX + ambient
- [ ] Specifies duration and aspect ratio
- [ ] Includes negative prompt for unwanted elements
- [ ] Falls within 100-300 word optimal range
- [ ] For multi-shot: repeats character bible and palette descriptors

---

## Technique Cross-Reference

Video generation techniques complement the image generation techniques in [`IMAGE_GENERATION_GUIDE.md`](IMAGE_GENERATION_GUIDE.md) and map to the SV (Specialized Visual) family in [`MASTER_TECHNIQUE_INDEX.md`](../techniques/MASTER_TECHNIQUE_INDEX.md):

| Technique | Image Equivalent | Video Application |
|-----------|-----------------|-------------------|
| Shot Framing & Camera Motion | SV-12 Grid Forcing | Cinematic composition control |
| Style & Visual Aesthetic | SV-11 Terminology Steering | Film grammar and genre direction |
| Subject Detail | SV-16 Physical Context | Character bible and distinctive markers |
| Audio Layering | N/A (video-specific) | Dialogue + SFX + ambient specification |
| Negative Prompting | SV-14 Negative Space Control | Exclude unwanted elements |
| Duration Scoping | SV-17 Deliverables Locking | Match action complexity to clip length |
| Iterative Refinement | SV-18 Validation Checklist | Progressive quality improvement |

---

## Summary

The difference between amateur and cinematic AI video comes down to **film literacy and specificity**:

1. **Speak film** — Use professional cinematography terminology
2. **Layer audio** — Specify dialogue, SFX, and ambient separately
3. **Be specific** — Distinctive visual markers, not generic descriptions
4. **Scope correctly** — Match action complexity to clip duration
5. **Iterate** — Start simple, refine progressively, lock what works
6. **Stay consistent** — Character bibles and palette repetition for multi-shot

Video models understand narrative structure. The more clearly you communicate your creative intent using the language of cinema, the better your results.

---

*Based on official Google Veo documentation, community best practices, and empirical testing, February 2026*

### Sources

- [Google DeepMind Veo Prompt Guide](https://deepmind.google/models/veo/prompt-guide/)
- [Ultimate Prompting Guide for Veo 3.1 (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- [Veo Video Gen Prompt Guide (Vertex AI Docs)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Veo 3 Prompting Guide (GitHub - snubroot)](https://github.com/snubroot/Veo-3-Prompting-Guide)
- [Veo 3 Prompt Guide (fal.ai)](https://fal.ai/learn/devs/veo3-prompt-guide-master-google-video-generation)
