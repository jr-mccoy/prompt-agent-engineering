---
title: "Frontend Look-and-Feel Hunt — Elicit a Target Vibe and Return a Concrete Visual Spec"
category: frontend-development/design-direction
description: "Teach the model a target 'vibe' (playful, trustworthy, minimal, premium, energetic) through attribute elicitation and reference anchoring, then return a concrete look-and-feel spec covering color-palette intent, typographic personality, spacing/density, motion feel, imagery style, and layout energy."
techniques:
  - ST-01
  - ST-02
  - CM-01
  - RT-02
  - QA-04
difficulty: intermediate
tags:
  - look-and-feel
  - visual-direction
  - design-brief
  - frontend
  - branding-vibe
updated: "2026-06-07"
related_prompts:
  - domain-frontend-development/design-direction/frontend_visual_design_direction_finder.md
  - domain-hr-management/hiring/hr_hiring_screen_challenge_designer.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Frontend Look-and-Feel Hunt

**Objective:** Translate a fuzzy desired "vibe" (e.g. playful, trustworthy, minimal, premium, energetic) into a concrete, build-ready look-and-feel specification — covering color-palette intent, typographic personality, spacing/density, motion feel, imagery style, and overall layout energy — by first eliciting the target attributes and anchoring them against references, then committing to a directional spec that a designer or frontend engineer can act on.

> This is the **canonical look-and-feel prompt** in the repository. It absorbs a former product-domain duplicate. For the broader, product-led direction-finding workflow (audience research, competitive positioning, multi-direction concepts), use the sibling prompt `frontend_visual_design_direction_finder.md`; use *this* prompt when you already know roughly the feeling you want and need it pinned down into a usable visual spec.

**When to Use:**
- Use when you have a product, app, landing page, or component set and a felt sense of how it "should feel," but no concrete visual direction yet.
- Use when a stakeholder keeps describing the vibe in adjectives ("clean but warm," "premium but not stuffy") and you need to convert those adjectives into design decisions.
- Use when handing a frontend engineer or designer a starting point so they are not inventing palette, type, and spacing from nothing.
- Use to align a team on *one* direction before any pixels are committed, reducing rework.

**When NOT to use:**
- Don't use when you need actual rendered images or mockups — this produces a written spec, not artwork. For image generation route to `domain-image-generation/`.
- Don't use for a full brand identity system (logo suite, brand guidelines, voice) — that is a larger engagement; this is screen/UI look-and-feel.
- Don't use when accessibility compliance is the goal — pair the output with `frontend_accessibility_wcag_audit.md` to validate contrast and motion choices.
- Don't use when the direction is already locked and you only need implementation tokens — go straight to design-token authoring.

---

## Inputs / Context

Provide whatever you have; the prompt will elicit the rest.

1. **Product / surface:** What is being styled (marketing site, dashboard, mobile app, single component) and its primary job.
2. **Target vibe in your own words:** The adjectives or feeling you're chasing (e.g. "playful, energetic, a little irreverent").
3. **Audience:** Who uses this and what they expect (consumers, enterprise buyers, clinicians, kids, developers).
4. **References (optional but powerful):** Sites/apps/brands whose feel you admire OR want to avoid. Wrap any pasted descriptions in `<references>...</references>`.
5. **Hard constraints:** Existing brand colors/fonts that must stay, platform constraints, dark-mode requirement, performance budget that limits motion.
6. **Anti-goals:** Feelings to avoid (e.g. "must not feel corporate / clinical / cheap").

If the target vibe, audience, or surface is missing, **ask up to 3 clarifying questions before producing the spec** — do not guess on these three.

---

## Constraints

### Must
- Begin by **eliciting and confirming the target vibe** as a small set of named attributes (3–5) with a one-line definition of each, so the felt sense becomes explicit and testable.
- For each attribute, identify the **design levers** that express it (color, type, spacing, motion, imagery, layout) — the same vibe is carried by multiple levers, not one.
- Use **reference anchoring**: name 1–2 widely recognizable points of comparison per attribute ("trustworthy here means closer to a bank than to a startup") so the abstract word gains a concrete coordinate. Describe *qualities*, never reproduce protected assets.
- Express color as **palette intent** (roles, temperature, saturation level, contrast strategy) rather than only hex codes; if you give example hex values, label them illustrative and note they must be contrast-checked.
- Make every recommendation **directional and decisive** — pick a lane and justify it, rather than listing every option.
- Flag any choice that **interacts with accessibility** (low-contrast palettes, heavy motion, tiny type) and route it to validation.

### Must Not
- Do not produce vague mood-board adjectives with no translation into concrete levers ("make it modern and clean").
- Do not invent brand facts, claim a named brand "uses" a specific hex/font unless the user supplied it, or fabricate trend statistics.
- Do not reproduce or instruct copying of a specific company's proprietary design — anchor on qualities only.
- Do not present illustrative hex/type choices as final tokens or as accessibility-verified.
- Do not hedge across so many directions that the output gives no actual direction.

---

## Instructions

1. **Elicit and lock the vibe (attribute extraction).**
   - From the user's adjectives, references, and anti-goals, distill **3–5 named attributes**. Give each a one-sentence working definition ("Trustworthy = feels established, predictable, and careful; nothing surprises the user").
   - Where the user's words are ambiguous, resolve them with a reference coordinate ("'premium' — closer to a boutique hotel than to a luxury-car configurator?") and state the interpretation you're adopting.
   - Echo the locked attribute set back so the rest of the spec is traceable to it.

2. **Map attributes to design levers (multi-dimensional translation).**
   - For each attribute, note which levers carry it most and *how*. Example: "Energetic" is carried mainly by motion (snappy, springy) and color (saturated accents), lightly by type (condensed, bold weights), and *not* by spacing (which should stay generous to avoid feeling frantic).
   - Resolve tensions between attributes explicitly (e.g. "playful + trustworthy" → playful in motion and illustration, trustworthy in layout and type).

3. **Specify color-palette intent.**
   - Define palette **roles**: primary/brand, secondary, accent, neutral/surface ramp, semantic (success/warn/error).
   - State **temperature** (warm/cool/neutral), **saturation level** (muted → vivid), and **contrast strategy** (high-contrast punchy vs. soft low-contrast calm).
   - Specify **light/dark** intent if relevant. Give illustrative hex values *labeled as illustrative*, and require WCAG contrast verification before they become tokens.

4. **Specify typographic personality.**
   - Recommend a **type pairing direction** (e.g. "geometric sans display + humanist sans body") and the *personality* it signals, not just font names.
   - Define **weight and contrast usage**, **scale/rhythm** (tight vs. airy), and **case/letterspacing** tendencies that reinforce the vibe.
   - Note fallback/performance considerations (variable font, system stack option).

5. **Specify spacing, density, and layout energy.**
   - State the **density** target (airy/spacious vs. dense/efficient) and the spacing scale feel.
   - Describe **layout energy**: grid regularity, alignment discipline, use of asymmetry, whitespace as a feature, edge-to-edge vs. contained.

6. **Specify motion feel and imagery style.**
   - **Motion:** easing character (snappy, smooth, springy, restrained), duration band, and where motion appears (micro-interactions, transitions, hero). Flag reduced-motion handling.
   - **Imagery / illustration:** style direction (photographic vs. illustrated vs. abstract/geometric), color treatment, and tone.

7. **Run a coherence and accessibility self-check before reporting.**
   - Confirm every lever traces back to a locked attribute and nothing contradicts the anti-goals.
   - Flag every choice that touches contrast, motion sensitivity, or minimum readable size, and route it to validation.
   - Assign a **confidence level** (High / Medium / Low) to the overall direction based on how complete the inputs were.

---

## False-Positive Prevention

1. **Adjective-only output.** Do not return "modern, clean, fresh" without translating each into concrete levers. If a lever can't be specified, say why and ask.
2. **Single-lever fixation.** A vibe is carried by several levers at once. Don't reduce "premium" to "use black and gold" — address type, spacing, and restraint too.
3. **Fabricated brand/trend facts.** Never assert that a named brand uses a specific font/hex or cite a "2026 design trend" statistic unless the user supplied it. Anchor on observable qualities.
4. **Illustrative-as-final.** Any hex code or font name offered as an example must be labeled illustrative and marked "verify contrast / licensing before use."
5. **Accessibility blind spots.** Trendy low-contrast palettes and heavy motion are common false wins. Flag them rather than silently recommending them.
6. **Direction-laundering.** Listing five equally-weighted options is not a direction. Commit to one and explain the tradeoff you accepted.
7. **Ignored anti-goals.** Re-check the final spec against the stated feelings-to-avoid; a "warm" palette that reads "cheap" violates the brief.

---

## Output Format

```
# Look-and-feel spec — [product / surface]

## Confirmed vibe (locked attributes)
1. [Attribute] — [one-line definition] — reference coordinate: [closer to X than Y]
2. [Attribute] — [...]
3. [Attribute] — [...]
(3–5 total)
Anti-goals honored: [list]

## Attribute → lever map
| Attribute | Carried mainly by | Lightly by | Deliberately NOT by |
|-----------|-------------------|------------|---------------------|
| [...]     | [...]             | [...]      | [...]               |

## Color — palette intent
- Temperature / saturation / contrast strategy: [...]
- Roles: primary [...], secondary [...], accent [...], neutral ramp [...], semantic [...]
- Light/dark intent: [...]
- Illustrative values (VERIFY CONTRAST before use): [#... labeled illustrative]

## Typography — personality
- Pairing direction: [display + body] → signals [...]
- Weight / contrast / scale / rhythm: [...]
- Performance / fallback: [...]

## Spacing, density & layout energy
- Density target: [airy ↔ dense]
- Layout energy: [grid discipline, asymmetry, whitespace, containment]

## Motion feel
- Easing character / duration band: [...]
- Where it appears: [...]
- Reduced-motion handling: [...]

## Imagery / illustration style
- Direction: [...]
- Treatment / tone: [...]

## Accessibility & validation flags
- [Choice] → [risk] → validate with [contrast check / reduced-motion / min-size]

## Direction confidence: [High | Medium | Low]
Rationale: [completeness of inputs, unresolved tensions]

## Next steps
- [What to validate, what to tokenize, what to prototype first]
```

---

## Verification

- [ ] 3–5 named attributes are locked, each with a definition and a reference coordinate.
- [ ] Every attribute maps to specific design levers (not adjectives).
- [ ] Tensions between competing attributes are resolved explicitly.
- [ ] Color is expressed as palette intent (roles, temperature, saturation, contrast), not only hex.
- [ ] Any hex/font given is labeled illustrative and flagged for contrast/licensing verification.
- [ ] Typography, spacing/density, motion, and imagery are each specified directionally.
- [ ] Accessibility-touching choices are flagged and routed to validation.
- [ ] The spec is checked against the stated anti-goals.
- [ ] One direction is committed to, with tradeoffs named — not a menu of equal options.
- [ ] A confidence level is assigned to the overall direction.
- [ ] No fabricated brand facts, trend statistics, or claims about named products.
