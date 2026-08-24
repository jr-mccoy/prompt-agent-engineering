---
title: "Therapy Modality Fit Selector"
category: psychology/client-self-use/pre-therapy
description: "Plainly describe the major therapy approaches (CBT, DBT, EMDR, psychodynamic, IFS, ACT), map my concerns to the ones most likely to fit, and produce questions to ask a prospective therapist — treating fit as collaborative, not destiny."
techniques:
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - client-self-use
  - pre-therapy
  - modality
  - therapy-approaches
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/client-self-use/pre-therapy/clientself_finding_a_therapist_search_criteria.md
  - domain-psychology/client-self-use/pre-therapy/clientself_do_i_need_therapy_decision_aid.md
  - domain-psychology/client-self-use/pre-therapy/clientself_culturally_affirming_therapist_screening.md
---

# Therapy Modality Fit Selector

## Objective

Help me understand the major therapy approaches in plain language, see which ones tend to fit concerns like mine, and walk away with questions to ask a prospective therapist. The point is to start an informed conversation — fit is something a therapist and I figure out together, not a label I have to get "right" up front.

## When to Use

- I'm about to search for a therapist and keep seeing acronyms (CBT, DBT, EMDR, IFS, ACT) I don't understand.
- A previous approach didn't click and I want to try something different.
- I have a specific concern (trauma, panic, emotion regulation, stuck patterns) and want to know what's typically used.

## Inputs / Context

- What I want help with, in my own words.
- What I'm hoping therapy feels like (skills and homework, talking and insight, body-based, structured, exploratory).
- Anything I've tried before and how it landed.
- Practical limits (short-term vs open-ended, telehealth, budget) if they matter to me.

## Constraints

### Must

- Describe each relevant modality in 2–3 plain sentences: what it focuses on, what a session tends to feel like, and what it's commonly used for.
- Cover the requested set — **CBT, DBT, EMDR, psychodynamic, IFS, ACT** — and only highlight the ones relevant to my concern, with a one-line note on the rest.
- Output sections in order: **What I'm Looking For**, **Approaches, Plainly**, **Likely-Fit Map**, **Questions to Ask a Prospective Therapist**, **Reminder: Fit Is Collaborative**.
- In the Likely-Fit Map, rank 2–3 approaches as *likely fit* with a reason tied to what I said, and note overlap (many therapists integrate several).
- Flag where a concern (e.g., trauma history) means specialized training matters, so I know to ask about it.

### Must Not

- Don't tell me which modality is "best" in the abstract or rank them universally.
- Don't diagnose me or imply a concern requires one specific approach.
- Don't present modality as destiny — a skilled therapist in a "non-ideal" approach can be a better fit than a poor one in the "ideal" approach; say so.
- Don't overstate evidence or invent claims about effectiveness.

## Instructions

1. Reflect back what I want help with and how I want therapy to feel.
2. Describe the relevant approaches plainly; one-line the rest.
3. Build the likely-fit map with reasons grounded in my inputs.
4. Generate questions I can ask a prospective therapist to test fit.
5. Close with the reminder that fit is worked out together.

## Output Format

```
=== MODALITY FIT ===

What I'm Looking For:
- Concern: [...]
- I want therapy to feel: [skills-based / insight-based / body-based / structured / exploratory]

Approaches, Plainly:
- CBT — [focus / what a session feels like / commonly used for]
- DBT — [...]
- EMDR — [...]
- Psychodynamic — [...]
- IFS — [...]
- ACT — [...]
(One-liner on any not central to my concern.)

Likely-Fit Map:
1. [Approach] — likely fit because [tied to what I said]
2. [Approach] — also worth considering because [...]
3. [Approach] — possible if [...]
Note: many therapists blend these; the person often matters more than the label.
Specialized-training flag: [e.g., "for trauma, ask whether they're trained in EMDR or a trauma-focused approach"]

Questions to Ask a Prospective Therapist:
- "How would you describe your approach to someone like me dealing with [concern]?"
- "Do you give homework / use structured tools, or is it more open-ended?"
- "Have you worked with [my concern] before, and roughly how?"
- "How will we know together if this approach is working for me?"

Reminder: Fit Is Collaborative
[1–2 sentences: I don't have to pick perfectly; I'm choosing where to start a conversation, and I can say if it isn't working.]
```

## Verification

- [ ] Each relevant modality described plainly (focus / feel / common use).
- [ ] Requested set covered; non-central ones one-lined.
- [ ] Likely-fit map ranks 2–3 with reasons tied to my inputs and notes overlap.
- [ ] Specialized-training flag raised where relevant.
- [ ] Therapist questions are concrete and askable.
- [ ] No universal "best," no diagnosis, no modality-as-destiny, no invented evidence.
