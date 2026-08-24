---
title: "UX Copy Tone Swap — Rewrite a UI Snippet in Three Brand Tones with Clarity and Accessibility Flags"
category: professional-writing/writing
description: "Rewrite a UI-copy snippet (button, error, empty-state, onboarding line, etc.) in three distinct brand tones, justify each choice against the moment and audience, and flag any tone that risks clarity or accessibility. The canonical tone-swap prompt for the repository."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - ux-writing
  - microcopy
  - tone-of-voice
  - accessibility
  - brand-voice
  - error-messages
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/writing/writing_voice_print_extractor.md
  - domain-professional-writing/writing/writing_precision_doc_edit.md
  - domain-professional-communication/design/design_frontend_look_feel_hunt.md
---

# UX Copy Tone Swap

**Objective:** Rewrite a single UI-copy snippet in three distinct brand tones, justify why each fits (or doesn't fit) the moment and audience, and explicitly flag any version that trades away clarity, comprehension, or accessibility for personality.

**When to Use:**
- Choosing a voice for a button, error, empty state, toast, onboarding line, paywall, or confirmation dialog.
- Aligning microcopy to a brand tone-of-voice spec or testing how far personality can go before it hurts.
- A copy line "works" but you want graded alternatives (neutral → warmer → boldest) with the risks named.
- Reviewing AI- or template-generated UI copy that feels off-tone or unclear.

**When NOT to use:**
- Long-form content (docs, marketing pages, emails) — use a prose-editing or narrative prompt.
- You need to *extract* a reusable voice spec from samples first — use `writing_voice_print_extractor.md`.
- The snippet's underlying logic/flow is the problem, not its wording.

**Audience:** UX writers, product designers, PMs, and developers shipping interface copy.

---

## Inputs / Context

1. **The snippet** (required): the exact current copy, plus its **element type** (button | error | empty state | toast | onboarding | confirmation | tooltip | other). Wrap it as `<ui_copy>` … `</ui_copy>`.
2. **The moment:** what the user just did / is trying to do, and their likely emotional state (frustrated by an error? exploring? mid-task?).
3. **Brand tone spec** (optional): any existing voice guidelines, or three named target tones. If none given, propose a sensible neutral / warm / bold trio and say so.
4. **Audience & context:** product type, audience, locale, regulatory/safety sensitivity (finance, health, legal).
5. **Constraints:** character limits, button-width limits, localization needs, reading-level target.

---

## Constraints

### Must
- Preserve the **functional meaning and the user's next action** in every version — tone changes wording, never what the UI does.
- Produce **three genuinely distinct tones** (e.g., neutral/clear, warm/human, bold/playful), each labeled and **justified** against the moment and audience.
- Respect the **element type's job**: a button says the action; an error says what happened, why, and how to recover; an empty state orients and invites; onboarding reduces friction.
- For each version, give a **fit rating** (good / risky / avoid) for *this* moment, with a one-line reason.
- **Flag clarity and accessibility risks** explicitly: jargon, ambiguity, idioms that don't localize, reading-level creep, humor at a bad moment, reliance on tone the screen reader can't convey.
- Respect any **character/width/reading-level constraints** and note when a tone can't fit them.
- For high-stakes moments (data loss, payment, security, errors), **prioritize clarity over personality** and say so.

### Must Not
- Change what happens, what the button does, or what recovery step the user must take.
- Add jokes or whimsy to error, failure, payment, security, or safety-critical moments where it undermines trust.
- Use idioms, slang, or cultural references that break under localization without flagging them.
- Sacrifice comprehension for cleverness, or produce copy a non-native speaker, low-vision, or screen-reader user can't parse.
- Present three near-identical rewrites as "three tones."

---

## Instructions

1. **Read the moment, not just the words.**
   - Identify the element type, what the user just did, and their likely emotional state. Copy that's "fun" in an empty state is hostile in a failed-payment error.

2. **Establish the three tones.**
   - Use the provided brand spec, or propose a neutral / warm / bold trio. Name each tone in one phrase so the choice is legible.

3. **Lock the functional core.**
   - State in one line what every version must still communicate (the action, the cause+recovery for errors, the orientation for empty states). This is the invariant.

4. **Write each version.**
   - Rewrite the snippet in each tone, honoring character/width/reading-level limits. Keep the functional core intact.

5. **Justify and rate fit.**
   - For each version, explain why the tone fits this moment and audience, and give a fit rating (good / risky / avoid) with a reason.

6. **Run the clarity + accessibility scan.**
   - For every version, check: plain language, no ambiguity, no untranslatable idioms, reading level, no tone-only meaning, no humor at a trust-critical moment. Flag every risk found.

7. **Acknowledge stakes and uncertainty (QA-04).**
   - For high-stakes moments, state plainly that clarity should win. Where the right tone depends on brand context you don't have, say so rather than guessing confidently.

8. **Recommend.**
   - Name the best-fit version for this exact moment and why; note when none fit and a clearer rewrite is needed.

---

## False-Positive Prevention

1. **Tone change that breaks function.** If a rewrite changes what the button does or drops the recovery step from an error, it's wrong regardless of how good it sounds. Verify the functional core survives in all three.
2. **Humor at the wrong moment.** Playful copy on a failed payment, lost data, security alert, or hard error erodes trust. Flag and downrate it; don't ship personality where users need reassurance and a fix.
3. **Cleverness over comprehension.** A witty line that a tired, stressed, non-native, or low-literacy user can't parse fails its only job. Test each version at the target reading level; clarity wins ties.
4. **Idioms that don't localize.** "You're on a roll!" or "Whoops, butterfingers" break in translation and for many readers. Flag any idiom/slang/pun as a localization and accessibility risk.
5. **Three theses, one tone.** If the three versions differ only in punctuation or a single word, they aren't three tones. Make the tonal distance real.
6. **Tone-only meaning.** Copy whose meaning depends on visual tone (sarcasm, winking caps) is lost to screen readers and skimmers. Flag it.
7. **Ignoring width/character limits.** A warm error that overflows the toast or wraps a button is unshippable. Note when a tone can't fit the constraint.
8. **Overconfident brand calls.** Without a brand spec, "this is the on-brand choice" is a guess. Label proposed tones as proposals and defer to the team's voice guidelines (QA-04).

---

## Output Format

```
# Tone swap — [element type]

## Original
> [current snippet]
Moment: [what the user just did / emotional state]
Functional core (invariant): [what every version must still say/do]
Constraints: [char/width limit, reading level, locale]

## Tones in play
1. [Tone A name] — [one-phrase description]
2. [Tone B name] — [...]
3. [Tone C name] — [...]

## Version A — [Tone A]
> [rewrite]
Why it fits: [...]
Fit for this moment: [good | risky | avoid] — [reason]
Clarity/accessibility flags: [none | list]

## Version B — [Tone B]
> [rewrite]
Why it fits: [...]
Fit: [...] — [reason]
Flags: [...]

## Version C — [Tone C]
> [rewrite]
Why it fits: [...]
Fit: [...] — [reason]
Flags: [...]

## Recommendation
Best fit for this moment: [version] — [why]
Stakes note: [if high-stakes, clarity-first statement]
Open question: [any brand/context info needed to finalize]
```

---

## Verification

- [ ] Functional meaning and the user's next action are preserved in all three versions.
- [ ] Three genuinely distinct, named tones (not reworded twins).
- [ ] Element type's job is respected (button = action; error = cause + recovery; etc.).
- [ ] Each version has a fit rating (good / risky / avoid) with a reason.
- [ ] Clarity and accessibility flags applied: jargon, ambiguity, idioms, reading level, tone-only meaning.
- [ ] Character/width/reading-level constraints honored or violations noted.
- [ ] High-stakes moments prioritize clarity, stated explicitly.
- [ ] No humor at trust-critical moments.
- [ ] A best-fit recommendation is given, with brand uncertainty acknowledged where relevant.
