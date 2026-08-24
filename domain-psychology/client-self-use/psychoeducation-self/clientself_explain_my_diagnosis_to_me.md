---
title: "Explain My Diagnosis to Me — Plain Language"
category: psychology/client-self-use/psychoeducation-self
description: "Give a plain-language, general explanation of a mental-health diagnosis a clinician gave me — what it commonly means, what it does not mean, typical treatment options, and questions to bring back to my clinician."
techniques:
  - ST-04
  - RT-04
  - RP-02
  - ED-01
  - QA-04
difficulty: beginner
tags:
  - client-self-use
  - psychoeducation
  - diagnosis
  - plain-language
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/client-self-use/symptom-understanding/clientself_anxiety_depression_burnout_differentiator.md
  - domain-psychology/client-self-use/identity-transitions/clientself_post_diagnosis_adjustment.md
  - domain-psychology/client-self-use/psychoeducation-self/clientself_my_med_was_just_prescribed_questions.md
---

# Explain My Diagnosis to Me — Plain Language

## Objective

Give a clear, general, plain-language explanation of a mental-health diagnosis a clinician has given me, so I can understand the words and walk back into the next appointment with informed questions. This explains the diagnosis **in general** — it does not tell me whether the label fits *me* or what *my* version looks like. That belongs to my clinician.

## When to Use

- A clinician gave me a diagnosis and I left the appointment not really understanding it.
- I saw a diagnosis written on paperwork, a portal, or an insurance form.
- I want to understand a label before reading scary things online.
- I want to prepare questions for my next visit.

## Inputs / Context

- The diagnosis as it was written (name and, if present, any specifier — e.g., "moderate," "recurrent," "with anxious distress").
- Who gave it to me (therapist, psychiatrist, primary care, ER) and roughly when.
- What, if anything, they told me about it.
- What I'm most confused or worried about.
- Reading level / detail I want (quick overview vs. more depth).

## Constraints

### Must

- Explain the diagnosis **in general terms only** — what it commonly involves across people who carry it.
- Use plain language and at least one everyday analogy (RT-04) to make an abstract idea concrete.
- Include a clear **"What this does NOT mean"** section that names that a diagnosis is a description of a pattern, not a verdict on character, intelligence, worth, or future.
- Describe the **range** of common treatment options in general (therapy approaches, medication as a category, lifestyle/skills) without recommending a specific one for me.
- End with concrete questions to bring back to the clinician.
- State plainly that only the diagnosing clinician can confirm how — or whether — this fits me.

### Must Not

- Don't confirm, deny, or "re-diagnose" — never say "you definitely have this" or "this sounds wrong."
- Don't interpret my specific symptoms, history, or test results.
- Don't recommend a specific medication or any dosing.
- Don't predict my prognosis or how "severe" my case is.
- Don't catastrophize or minimize; stay neutral and factual.

## Instructions

1. Restate the diagnosis name plainly so I know what we're explaining.
2. Explain in general what kind of thing it is (a mood condition, an anxiety condition, a neurodevelopmental pattern, etc.).
3. List the features people with this diagnosis commonly experience — framed as "common," not "you have."
4. Give an everyday analogy.
5. Spell out what the diagnosis does NOT mean.
6. Lay out the general categories of treatment and how people often work with a clinician on them.
7. Generate questions to bring back to the diagnosing clinician.
8. Flag any escalation pathway if relevant.

## Output Format

```
=== UNDERSTANDING: [diagnosis name] (general explanation) ===

What kind of thing this is:
[Plain-language category and one or two sentences.]

A way to picture it:
[Everyday analogy.]

Features people with this diagnosis commonly have (general, not a checklist about you):
- [Feature 1]
- [Feature 2]
- [Feature 3]
- (How much, which ones, and how they show up varies a lot person to person.)

What this does NOT mean:
- It is not a statement about your character, intelligence, or worth.
- It is a description of a pattern, not a permanent identity.
- Having a name for it does not mean it can't change or be managed.
- [One more, tailored to common fears about this diagnosis.]

How people commonly work on it (general categories — your clinician decides what fits you):
- Talking therapies: [general approaches associated with this]
- Medication: [whether medication is commonly part of treatment, as a category only — no specific drug or dose]
- Skills / lifestyle: [sleep, routine, support, etc., in general]

Questions to bring back to my clinician:
1. "What did you see in me that led to this diagnosis?"
2. "Is this a working diagnosis or a settled one?"
3. "What are my treatment options, and what do you recommend for me specifically?"
4. "How will we know if it's improving?"
5. "[My own question: ____]"

If things get worse before my next appointment:
- Worsening this week → contact my clinician's office.
- Can't keep myself safe / thoughts of suicide → call or text 988 (US) now, or go to the nearest ER.

Reminder: This is a general explanation. Only the clinician who assessed you can confirm how this applies to you.
```

## Verification

- [ ] Diagnosis explained in general terms, not applied to the user.
- [ ] At least one everyday analogy used.
- [ ] "What this does NOT mean" present and names it is not a character verdict.
- [ ] Treatment options given as general categories, no specific med or dose.
- [ ] No prognosis or severity claim about the user.
- [ ] Questions for the clinician included.
- [ ] Escalation pathway (clinician / 988 / ER) included.
- [ ] Closing reminder routes confirmation back to the diagnosing clinician.
