---
title: "Android Compose UI Design Studio (Interactive, Anti-Cookie-Cutter)"
category: mobile-development
description: "Runs an interactive design-exploration session that uses the AskUserQuestion tool to brainstorm, diverge, and lock a distinctive Jetpack Compose design system that avoids generic AI-generated UI defaults — then emits theme tokens, component specs, and a reference screen."
techniques:
  - RP-01
  - MP-03
  - NE-02
  - RP-04
  - DP-04
  - NE-06
difficulty: advanced
tags:
  - android
  - mobile-development
  - jetpack-compose
  - ui-design
  - design-system
  - interactive
updated: "2026-05-28"
related_prompts:
  - domain-software-engineering/mobile/android/implementation/android_compose_screen_builder.md
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_polish.md
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_market_dominance_review.md
  - domain-prompt-engineering/escape-median/escapemedian_default_position_mapper.md
---

# Android Compose UI Design Studio (Interactive, Anti-Cookie-Cutter)

**Objective:** Act as a senior product designer + Android UI engineer and run an *interactive design-exploration session* that brainstorms, diverges, and locks a **distinctive Jetpack Compose design system** — one that escapes the generic, templated look of AI-generated UI — then translates it into Compose theme tokens, component specifications, and a reference screen.

**When to Use:** Use this *before* `android_compose_screen_builder.md`. Reach for it when starting a new app or feature, redesigning a UI that "looks like every other app," or when you have a product idea but no opinionated visual identity yet. This is a planning/design prompt, not an implementation dump — its first job is to ask, not to answer.

**Prompt Type:** Interactive Comprehensive (design discovery → divergence → system lock → code scaffold)

**Tooling Requirement:** This prompt is designed for an agent with the **`AskUserQuestion` tool** (e.g., Claude Code). The decision points below MUST be surfaced as `AskUserQuestion` calls — never silently assumed. If the tool is unavailable, fall back to numbered questions and STOP for answers at each gate; do not proceed on guesses.

---

## Operating Principle: Ask, Don't Default

The fastest way to produce cookie-cutter UI is to skip the conversation and reach for the median. This prompt inverts that: **every consequential design decision is a question to the user, not an assumption by the model.** You are facilitating a design studio, not generating a screen.

- Use `AskUserQuestion` for divergent choices (directions, palettes, type, motion personality, density).
- Offer 2–4 *genuinely distinct* options per question — never four variations of the same safe answer.
- Make one option the recommended one (first, labeled "Recommended") **only when you have an evidence-based reason**; otherwise present options as neutral peers.
- Always let the user steer with "Other." Treat their custom answers as binding.
- Batch related decisions into a single `AskUserQuestion` call (up to 4 questions) so the user isn't drip-fed.

---

## The Anti-Slop Doctrine (what you are designing *against*)

Before any work, internalize the failure modes that make UI read as "AI-generated" or "template." You will actively design away from these, and you will audit against them at the end.

| # | Cookie-Cutter Tell | The Distinctive Alternative |
|---|--------------------|------------------------------|
| 1 | Default Material 3 dynamic purple / untouched baseline color scheme | A deliberate, named palette derived from brand + emotional intent |
| 2 | Purple→blue (or teal→green) gradient on the hero / buttons | Flat intentional color, or a gradient that is a *signature*, used once |
| 3 | Everything is a centered, rounded, drop-shadowed card on a gray background | Varied surface treatments; intentional flat regions, dividers, edges, full-bleed |
| 4 | Uniform spacing, no rhythm — every gap is 16dp | A spacing scale with intentional hierarchy (tight clusters, generous breaks) |
| 5 | Default Roboto/Inter at one size with bold for "emphasis" | A real type scale with contrast in weight, size, and tracking; a display voice |
| 6 | Symmetric "4 stat cards in a 2×2 grid" dashboard cliché | Asymmetry, a clear focal point, content-driven layout |
| 7 | "Hero image + 3 feature cards + CTA" landing template | Layout that follows *this* product's actual primary action |
| 8 | Emoji used as iconography; generic undraw-style illustrations | A coherent icon set + illustration style chosen on purpose (or none) |
| 9 | Lorem ipsum shaping the layout; placeholder-driven design | Real or realistic content; layout that survives long/short/empty real data |
| 10 | No motion personality — only default fades and the platform's stock transitions | A defined motion signature (easing, duration, one memorable moment) |
| 11 | Identical empty/error/loading states with a centered icon + "Try again" | States with the product's voice and a useful next action |
| 12 | Decorative density mismatch (airy spa UI for a power-user tool, or vice versa) | Density chosen to match the user's task frequency and expertise |

If the user's brand or product *genuinely wants* one of the left-column patterns (e.g., a finance app that needs Material defaults for trust), that is a legitimate decision — but it must be a **chosen** decision surfaced via a question, not a default you fell into.

---

## Phase 0 — Frame the Studio (no questions yet)

Read any provided context (existing app, codebase, brand assets, competitor names, screenshots). In 3–5 sentences, state back what you understand: the product, who uses it, and the single most important thing a user comes to do. If you cannot infer the primary user action, that is your **first** `AskUserQuestion`.

Do not propose any visual direction yet. You don't have enough to be non-generic.

---

## Phase 1 — Discovery (AskUserQuestion)

Goal: gather the raw material that makes design *specific*. Run as 1–2 `AskUserQuestion` batches. Adapt wording to what context already answered — never ask what you already know.

Cover these dimensions (group into ≤4 questions per call):

1. **Primary job + emotional target.** What is the one action the UI must make effortless, and how should the user *feel* doing it (e.g., calm/confident, fast/in-control, playful/delighted, serious/trustworthy)?
2. **Audience & context of use.** Who, how often, where (one-handed on the move? focused desk session? accessibility needs? low-end devices?).
3. **Brand anchors.** Existing colors/logo/wordmark/voice? Any non-negotiables (legal, accessibility contrast, dark-mode-first)?
4. **Anti-references (critical for escaping the median).** Name 1–3 apps whose look you want to *avoid*, and 1–3 you admire — and *why*. This is the single highest-signal question for distinctiveness.

Example `AskUserQuestion` shape:

```
Q1 header: "Primary job"      → 2–4 candidate "core actions" you inferred + Other
Q2 header: "Emotional tone"   → distinct tones (Calm/Confident · Fast/Utilitarian · Playful/Warm · Premium/Serious) + Other
Q3 header: "Brand anchors"    → "I have brand colors", "Logo only", "Blank slate", "Dark-mode first" + Other
Q4 header: "Anti-references"  → free-form expected; offer common traps to react to + Other
```

---

## Phase 2 — Divergence (AskUserQuestion)

Goal: produce **genuinely different directions** and let the user choose — this is where you escape the default.

1. Synthesize Phase 1 into **2–3 named design directions** that are materially distinct in mood, layout philosophy, and color/type strategy — not three shades of the same idea. For each, give:
   - A one-line **concept** ("Editorial calm: type-led, generous whitespace, near-monochrome with one ink accent")
   - **Color strategy** (not hex yet — strategy: monochrome+accent / warm earthy / high-contrast dark / etc.)
   - **Type strategy** (display voice, scale contrast)
   - **Layout philosophy** (what's the focal point; symmetric vs asymmetric; card-light vs card-heavy)
   - **Motion signature** (one sentence)
   - **The one signature moment** that becomes the app's identity
2. Surface them with `AskUserQuestion` (use the `preview` field to show a short mock layout sketch in ASCII/markdown per direction if helpful). Ask the user to pick a direction or blend.
3. If the user blends or picks "Other," confirm the merged direction in one short `AskUserQuestion` before locking.

**Constraint (DP-04 — must-not):**
- ❌ Do NOT present directions that differ only in accent color.
- ❌ Do NOT include a direction that is "safe default Material 3" unless the user's Phase-1 answers explicitly call for it.
- ❌ Do NOT proceed past Phase 2 without an explicit chosen direction.

---

## Phase 3 — Lock the Design System (targeted AskUserQuestion + decision)

Translate the chosen direction into concrete, named tokens. Decide what you can justify; ask only where taste genuinely forks. Produce this table:

```markdown
## Design System — [Direction Name]

### Color (semantic, not just raw)
| Token | Light | Dark | Role / where it appears |
|-------|-------|------|--------------------------|
| brand/primary | #...  | #... | Primary action only |
| ink/strong    | #...  | #... | Headlines, key text |
| surface/base  | #...  | #... | App background |
| surface/raised| #...  | #... | Where elevation is intentional |
| accent/signature | #... | #... | The ONE place we go loud |
| state/error, state/success ... |

### Type Scale (intentional contrast)
| Token | Font / weight | Size / line / tracking | Use |
|-------|---------------|------------------------|-----|
| display | ... | ... | The voice; used sparingly |
| title / body / label / mono ... |

### Spacing & Rhythm
4dp base grid → scale: 4 / 8 / 12 / 16 / 24 / 32 / 48. Note where tight clusters vs generous breaks are used (reject uniform 16dp everywhere).

### Shape & Elevation
Corner radii per surface tier; where we go SHARP/edge/flat on purpose; shadow vs tonal elevation policy.

### Motion Signature
Standard easing + durations; the one memorable transition.
```

Ask the user (one `AskUserQuestion` batch) only the forks that matter, e.g.: light-first vs dark-first vs both; density (compact/comfortable/spacious); corner language (sharp / soft / pill); whether dynamic color (Material You) is allowed to override the brand palette.

---

## Phase 4 — Emit Compose Scaffold

Only now produce code. All code must be copy-paste ready with file paths and use the **named tokens**, never raw hardcoded values inline.

Produce, in order:

1. **`ui/theme/Color.kt`** — the locked palette as named `Color` values (light + dark).
2. **`ui/theme/Type.kt`** — a `Typography` built from the type scale (custom `FontFamily` if a display voice was chosen).
3. **`ui/theme/Shape.kt` + `ui/theme/Spacing.kt`** — shape set and a spacing object/`CompositionLocal` (`LocalSpacing`) so spacing is a token, not a magic number.
4. **`ui/theme/Theme.kt`** — the `MaterialTheme` wrapper wiring the above; show how/whether dynamic color is gated per the Phase-3 decision.
5. **`ui/theme/Motion.kt`** — easing/duration tokens for the motion signature.
6. **One reference screen** (`ui/<feature>/<Feature>Screen.kt`) that demonstrates the system on the product's *actual* primary action — including the signature moment, a real-content layout, and intentional non-uniform spacing. Add `@Preview` for light, dark, and a long-content edge case.
7. **Component specs** (prose, not full code) for 3–5 core components, each noting how it diverges from the default Material look.

Code requirements:
- ❌ No raw hex or `.dp` magic numbers inside composables — reference tokens.
- ❌ No state left unhoisted; previews must not depend on a ViewModel.
- ✅ Include `contentDescription`/`semantics` and respect 48dp touch targets from the start (accessibility is not a later phase).
- ✅ Honor the user's density/contrast/dark-mode decisions exactly.

---

## Phase 5 — Anti-Slop Self-Audit (NE-06)

Before finishing, audit your own output against the doctrine. Fill this table honestly; any ❌ must be fixed or explicitly justified as a user-chosen decision.

```markdown
## Anti-Cookie-Cutter Self-Audit
| Check | Pass? | Evidence / token |
|-------|:----:|------------------|
| Palette is derived from brand/intent, not Material default purple | ☐ | Color.kt |
| Gradients (if any) are a deliberate signature, not decoration | ☐ | |
| Surfaces vary — not every block is a shadowed rounded card | ☐ | |
| Spacing has rhythm (not uniform 16dp) | ☐ | Spacing.kt |
| Type scale has real weight/size/tracking contrast + a display voice | ☐ | Type.kt |
| Layout has a clear focal point tied to the primary action | ☐ | Screen.kt |
| Reference screen uses realistic content, survives long/empty data | ☐ | previews |
| A defined motion signature exists (not just default fades) | ☐ | Motion.kt |
| Empty/error/loading states carry the product voice | ☐ | |
| Density matches the audience's task (not generic comfortable) | ☐ | |
| Accessibility: contrast, touch targets, semantics present | ☐ | |
| At least one "signature moment" that is this app's identity | ☐ | |
```

End with: a one-paragraph **design rationale** (why this looks like *this* product and nothing else), a list of the **decisions the user made** (with their answers), and the **open questions / next steps** for implementation (hand off to `android_compose_screen_builder.md`).

---

## Constraints (Must / Must Not)

**Must:**
- Treat every divergent design decision as an `AskUserQuestion`, not an assumption.
- Keep Phase 0–2 strictly question-and-synthesis; emit no theme code before a direction is chosen.
- Ground distinctiveness in the user's anti-references and primary action — not in generic "make it pop."
- Reference named tokens in all code.

**Must Not:**
- ❌ Jump straight to generating a screen or a default Material theme.
- ❌ Offer false-choice options (4 near-identical answers) in any `AskUserQuestion`.
- ❌ Invent brand facts, user research, or competitor data the user didn't provide — ask instead.
- ❌ Override a user's stated brand/accessibility/density decision in pursuit of "distinctiveness."
- ❌ Manufacture novelty for its own sake when the product genuinely calls for convention (e.g., a banking app). Distinctive ≠ gimmicky; surface the trade-off as a question.

---

## Techniques Used

- **RP-01** (Expert Role Assignment): senior product designer + Android UI engineer framing.
- **MP-03** (Task Clarification): the prompt's spine — `AskUserQuestion` at every fork.
- **NE-02** (Phased Workflow Architecture): Frame → Discover → Diverge → Lock → Build → Audit, with gates.
- **RP-04** (Socratic Dialogue): divergence is driven by questions, including the high-signal anti-reference question.
- **DP-04** (Must-Not Constraints): explicit anti-slop and anti-default guardrails per phase.
- **NE-06** (Self-Audit Requirements): the Phase-5 anti-cookie-cutter audit table before completion.

---

## Customization Guide

- **Existing design system present?** Run only Phase 0 + a trimmed Phase 1, then jump to Phase 4 to *extend* the system, and still run Phase 5.
- **Multi-platform (Compose Multiplatform)?** Keep tokens in `commonMain`; flag any Android-only Material APIs in the component specs.
- **Tablet/foldable target?** Add a Phase-3 question on adaptive layout strategy (list-detail vs single-pane) and emit `WindowSizeClass` branching in the reference screen.
- **Strict brand kit handed over?** Skip Phase 2 divergence; spend the questions on *interpretation* forks (which brand color is the action color, where the one loud moment goes).
