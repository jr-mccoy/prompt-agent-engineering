---
title: "Audit the Inner Critic's Specific Sentences"
category: personal-development/identity
description: "Capture the user's actual recurring self-critical sentences verbatim, classify each by distortion type, and produce a counter-sentence grounded in evidence — not affirmations."
techniques:
  - ST-01
  - ST-02
  - AG-11
  - NE-07
  - QA-12
  - RT-09
difficulty: intermediate
tags:
  - identity
  - self-talk
  - inner-critic
  - cognitive-distortion
  - counter-evidence
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/identity/identity_confidence_calibration.md
  - domain-personal-development/prompts/agency/agency_burnout_recovery.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-personal-development/prompts/thinking/thinking_mindset_shift_reframe.md
---

# Audit the Inner Critic's Specific Sentences

**Objective:** Catch the exact verbatim sentences the user's inner critic actually says, classify each by distortion pattern, and produce one evidence-based counter-sentence per critical sentence. Not affirmations. Not "love yourself." Specific counters grounded in the user's specific facts.

**When to use:** The user notices a recurring negative self-narrative ("I always …", "I'm the kind of person who …", "I should have …") and wants to interrupt it without resorting to positive-thinking exercises that don't stick.

**Audience:** An individual examining their own internal narration. **This prompt is not therapy.** If the inner critic includes self-harm ideation, persistent hopelessness, or descriptions consistent with a mental health condition, this prompt refuses and refers to professional help.

---

## Inputs Required

1. **Verbatim critical sentences.** 5–10 sentences the user actually hears in their own head. Word for word — not summaries. If the user can only paraphrase, ask them to write them down for one day first and come back. The exact words matter; "I'm not good enough" and "I'm a fraud" are different sentences with different counters.
2. **Triggering context for each sentence.** When does each one show up? After meetings? Late at night? Reading other people's work? Be specific.
3. **One concrete situation in the last 14 days where the sentence ran loud.** Just one — the one the user remembers most clearly.
4. **Three pieces of factual counter-evidence the user already knows but doesn't credit.** Specific events, outcomes, feedback, or observed behavior that contradicts the critic. Not affirmations. Facts.

If input 1 contains self-harm ideation or persistent hopelessness, refuse this prompt and output: "This prompt is not the right tool. Please contact a licensed mental health professional. In the US, dial or text 988." Do not proceed.

If input 4 is empty ("I can't think of any"), the user is too inside the loop to do this exercise alone. Recommend they collect counter-evidence over a week (one observation per day) before running the prompt.

---

## Instructions

### Step 1 — Acknowledge before analyzing

Open the response with one sentence acknowledging that these sentences are real, painful, and being taken seriously. Do not skip this step. Do not extend it. One sentence. Then move to analysis. (NE-07 emotional validation, bounded.)

### Step 2 — Classify each verbatim sentence

For each sentence in input 1, label exactly one distortion pattern from this fixed taxonomy:

| # | Pattern | Signature | Example |
|---|---|---|---|
| 1 | **Globalization** | "Always," "never," "everyone," "no one." | "I never finish anything." |
| 2 | **Identity collapse** | A behavior treated as the whole self. | "I'm a fraud." (vs. "I felt like a fraud in that meeting.") |
| 3 | **Mind-reading** | Attributing thoughts to others without evidence. | "They think I'm stupid." |
| 4 | **Catastrophizing** | One outcome stretched to disaster. | "If I don't ship this, my career is over." |
| 5 | **Should-tyranny** | "Should," "ought," "must" without source. | "I should be further along by now." |
| 6 | **Comparison-as-fact** | Someone else's outcome treated as your verdict. | "X did this in their 20s; I'm too late." |
| 7 | **Past-self conviction** | A judgment from years ago re-applied as current truth. | "I've always been bad at this." |
| 8 | **Discounting evidence** | Counter-facts dismissed as flukes or charity. | "They were just being nice." |
| 9 | **Predictive certainty** | A future outcome stated as fact. | "I'm going to fail this." |
| 10 | **Other-as-correct** | Someone else's standard treated as the only standard. | "A real engineer would have known this." |

Do not invent new patterns. If a sentence fits two, pick the one that does the most damage; name the second.

### Step 3 — Trace the trigger

For each classified sentence, name in one phrase what triggers it from input 2 (e.g., "after performance reviews," "Sunday night," "reading a peer's launch post"). The trigger is part of the pattern; counters that ignore it won't stick.

### Step 4 — Generate one evidence-based counter

For each sentence, write one counter-sentence with these properties:

- **Grounded in input 4** (the user's existing factual evidence) or in a specific instance from input 3.
- **Concrete, not abstract.** "On April 12 I shipped X to 200 people" beats "I am capable."
- **Same scope as the original.** A globalization gets a specific instance. An identity collapse gets a behavior frame ("I felt like a fraud *in that meeting*"). A predictive certainty gets a probabilistic frame ("This might fail; here's what would actually happen if it did").
- **Not an affirmation.** Affirmations and the critic exist on the same axis; the counter must operate on a different axis (specificity, evidence, scope).

If no counter-evidence exists for a particular sentence, do not invent one. Mark it: *"Insufficient evidence to counter directly — collect data: [one specific observation to look for over the next 14 days]."*

### Step 5 — Identify the loudest sentence

Pick **one** sentence — the one with highest frequency × highest situational cost (from input 3). That's the priority. Restate its counter and propose one physical practice for the next 14 days:

- Write the counter where the user will see it during the trigger context.
- When the sentence runs, name it by its distortion-pattern number out loud. Naming interrupts the loop without arguing with it.
- Log one occurrence per day for 14 days: *trigger, sentence ran (Y/N), counter applied (Y/N).* This is data collection, not journaling.

### Step 6 — Refuse three temptations

Close the output by explicitly stating what this prompt is *not* doing, so the user doesn't expect it:

- It is not eliminating the inner critic.
- It is not replacing the critic with a cheerleader.
- It is not therapy.

The goal is to interrupt the loop often enough that the critic loses its monopoly on the user's self-description.

---

## Constraints

### Must
- Open with one sentence of acknowledgment, then move to analysis.
- Classify every sentence into exactly one distortion pattern from the taxonomy.
- Generate one counter per sentence, grounded in user-supplied evidence (input 4) or specific instances (input 3).
- Pick exactly one priority sentence and one 14-day practice.
- Refuse if input contains self-harm ideation; refer to professional help.

### Must Not
- Use affirmations ("you are enough," "you are loved").
- Generate a counter from generic positive psychology rather than user-supplied evidence.
- Diagnose mental health conditions, prescribe medication, or offer clinical interpretations.
- Try to eliminate the inner critic. Goal is interruption, not eradication.
- Add patterns to the taxonomy.

---

## False-Positive Prevention

1. **Don't paraphrase the verbatim sentences.** "I'm a failure" and "I always fail" are different patterns. Use the user's exact words throughout.
2. **Don't generate counters that are themselves overconfident.** A counter to "I'm a fraud" is not "you are exceptional" — that's the same axis. It's "in [specific situation] I [specific evidence]."
3. **Don't moralize about which sentences the user "shouldn't" think.** The point is to interrupt the loop, not litigate it.
4. **Don't extend acknowledgment into reassurance.** One sentence. Then work.
5. **Don't run this prompt with fewer than 5 sentences.** Two sentences won't show patterns; ask for more.
6. **Watch for distortion #8 in real time.** If the user dismisses the prompt's counter ("yeah but…"), that dismissal is itself an instance of "discounting evidence" — name it.

---

## Output Format

```
[One sentence acknowledging the difficulty of these sentences.]

## Sentence-by-sentence audit
| # | Verbatim sentence | Distortion pattern | Trigger | Counter (evidence-based) |
|---|---|---|---|---|
| 1 | "..." | #N — [pattern name] | [phrase] | [specific counter or "insufficient evidence — collect: ..."] |
| 2 | ... | ... | ... | ... |

## Priority sentence (highest frequency × cost)
**Sentence:** "..."
**Pattern:** #N — [name]
**Counter:** [restated]

## 14-day practice
- Where the counter goes (physical or digital location): [specific]
- Trigger-naming protocol: when the sentence runs, say "[#N]" out loud
- Daily log columns: trigger / sentence ran (Y/N) / counter applied (Y/N)

## What this prompt is not doing
- Not eliminating the critic
- Not replacing it with a cheerleader
- Not therapy

## When to escalate
If after 14 days the critic's volume hasn't decreased, or if any sentence in input 1 shifts toward self-harm or persistent hopelessness, contact a licensed mental health professional.
```

---

## Verification

- [ ] One sentence of acknowledgment, no more.
- [ ] Every input sentence classified into exactly one pattern from the taxonomy.
- [ ] Every counter cites specific evidence from input 3 or 4 (or marks itself "insufficient evidence — collect …").
- [ ] No affirmations. No "you are …" statements.
- [ ] Exactly one priority sentence + one 14-day practice.
- [ ] Refusal block triggered if self-harm content was present.
- [ ] No clinical interpretation, no diagnosis.
