---
title: "MI OARS Response Generator"
category: psychology/modalities/motivational-interviewing
description: "Generate Open question, Affirmation, Reflection (simple + complex), and Summary responses for a given client utterance, with reasoning for each and an MI-adherence note."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - MI
  - motivational-interviewing
  - OARS
  - reflections
  - affirmations
  - open-questions
  - summaries
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_change_talk_coder.md
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_decisional_balance_facilitator.md
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_ambivalence_map.md
---

# MI OARS Response Generator

## Objective

Given a client utterance, generate MI-consistent OARS responses: at least one Open question, one Affirmation, one Simple reflection, one Complex reflection (continuing-the-paragraph or double-sided as appropriate), and one Summary at decision points. Each response includes a brief rationale and an MI-adherence note.

## When to Use

- Training, supervision, or self-study.
- Pre-session preparation for a client whose pattern is known.
- In-session reference (silent self-check between turns).
- MITI coder feedback for a moment that wasn't coded MI-adherent.
- Cross-modality use: MI spirit can support engagement in CBT, DBT, ACT, IFS.

## Inputs / Context

- Client utterance verbatim or paraphrased.
- Behavior under discussion (target).
- Stage of change.
- Stance (equipoise / change-favoring).
- Prior turn(s) for context (single-utterance responses can miss).
- Cultural / language fit.
- Any specific clinician growth area (e.g., "more complex reflections," "fewer questions").

## Constraints

### Must

- Generate at least one of each:
  - **Open question** (cannot be answered yes/no; invites elaboration).
  - **Affirmation** (acknowledges strength, effort, value; not praise).
  - **Simple reflection** (paraphrase; near-verbatim).
  - **Complex reflection** (adds meaning, emotion, or continues the paragraph; double-sided when sustain and change talk coexist).
  - **Summary** at decision points (transitional or collecting summary).
- Include 1-sentence rationale per response.
- Mark each as MI-adherent and consistent with the stance.
- Reflect **change talk preferentially** in change-favoring stance.
- For affirmations: anchor to a specific behavior or trait, not generic praise ("Great job").
- For double-sided reflections: order matters — end on the change-talk side to amplify.
- Note responses to **avoid** for the situation (e.g., closed questions that elicit yes/no; persuasion).
- If client utterance includes risk content (suicidality, AOD escalation), include a brief route-out note (this isn't the place to do risk; reflect, then transition).

### Must Not

- Do not generate persuasion, advice, warnings, or "righting reflex" responses; if generated for contrast, mark them MI-inconsistent.
- Do not affirm the absence of a behavior as a fixed trait ("you're so disciplined") if not supported.
- Do not use questions as covert advice ("Have you thought about quitting?").
- Do not over-fill the response set with reflections that all paraphrase the same surface meaning.
- Do not skip the rationale; the artifact is for learning.

## Instructions

1. Identify the client's underlying message: facts, feelings, ambivalence, change talk, sustain talk.
2. Generate Open question(s) inviting expansion.
3. Generate an Affirmation anchored to a specific behavior or quality.
4. Generate a Simple reflection paraphrasing surface meaning.
5. Generate a Complex reflection adding meaning, emotion, or continuing the paragraph. If sustain and change talk coexist, generate a double-sided reflection ending on the change-talk side.
6. Generate a Summary, if a decision point or transition is at hand.
7. Write rationale per response.
8. Note MI-inconsistent alternatives to avoid.

## Output Format

```
=== MI OARS RESPONSE SET ===
Client utterance: "[verbatim]"
Context: [Target behavior; stage of change; stance; prior turns if relevant]

UNDERLYING MESSAGE (clinician's read)
- Surface meaning: [...]
- Feeling / value: [...]
- Change talk present (DARN-CAT subtype): [...]
- Sustain talk present (subtype): [...]
- Ambivalence: [...]

OPEN QUESTIONS
- OQ-1: "[...]"
  Rationale: [Invites expansion of change talk / explores reasons]
- OQ-2: "[...]"
  Rationale: [...]

AFFIRMATION
- AF: "[Specific affirmation anchored to a behavior or value]"
  Rationale: [...]

SIMPLE REFLECTION
- SR: "[Paraphrase near-verbatim]"
  Rationale: [...]

COMPLEX REFLECTION
- CR: "[Adds meaning, emotion, or continues the paragraph]"
  Rationale: [...]
- Double-sided CR (if sustain + change present): "On one hand [sustain]; on the other hand [change]."
  Rationale: [Ends on change-talk side to amplify]

SUMMARY (at decision point / transition)
- SU: "[Collecting summary of the client's expressed change talk + ambivalence]"
  Rationale: [Anchors progress; sets up key question]
- Key question (if appropriate): "Where does that leave you?"

MI-INCONSISTENT ALTERNATIVES TO AVOID
- Persuasion: "[example]" → why MI-inconsistent
- Closed question: "[example]" → why
- Warning: "[example]" → why

STANCE / ADHERENCE NOTE
- Stance: [Equipoise / Change-favoring]
- This set aligns with stance: [Y/N — explain]

RISK / TRANSITION NOTE
- If risk content present, transition to risk-screen: [...]
```

## Verification

- [ ] At least one of each OARS element present.
- [ ] Open questions cannot be answered yes/no.
- [ ] Affirmation anchored to specific behavior / value.
- [ ] Simple and complex reflections clearly distinguished.
- [ ] Double-sided reflection (if sustain + change present) ends on change-talk side.
- [ ] Summary present at decision points.
- [ ] Rationale per response.
- [ ] MI-inconsistent alternatives explicitly marked.
- [ ] Stance adherence noted.
- [ ] Risk transition noted if applicable.
- [ ] No fabricated client wording.
