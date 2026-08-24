---
title: "Therapeutic Termination Summary Drafter"
category: psychology/documentation
description: "Draft a therapeutic termination summary distinct from administrative discharge — focused on the relational arc, processing of the ending, gains internalized, and a forward-looking handoff to the client's future self."
techniques:
  - ST-04
  - DT-02
  - NE-07
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - termination
  - planned-ending
  - therapeutic-arc
  - relational-summary
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_discharge_summary.md
---

# Therapeutic Termination Summary Drafter

## Objective

Produce a termination summary that complements (not replaces) the administrative discharge summary. Where discharge documents the episode for billing, audit, and care continuity, **termination** documents the *therapeutic arc and ending*: the relational journey, what the client internalized, how the ending was processed, and what the client carries forward.

The summary must:

1. Capture the therapeutic alliance arc (initial → working → termination phase).
2. Articulate the client's specific gains in their own framing where possible.
3. Document how the ending itself was processed (planned, mutual, abrupt, ambivalent).
4. Provide a forward-looking handoff to the client's future self.

## When to Use

- Planned termination after meeting treatment goals.
- Mutual termination by agreement.
- Forced termination (clinician leaving practice / insurance change / move).
- Pairs with the discharge summary; either can be shared with client per practice policy.

## Inputs / Context

- Episode dates, total sessions.
- Initial referral / chief complaint and the client's framing of what they wanted.
- Modality and key interventions used.
- Turning points, ruptures, repairs.
- Final symptom and functional status.
- Termination process: how the ending was discussed, over how many sessions, what came up.
- Client's stated meaning of the work.
- Clinician's reflections on the alliance and the work.
- Anticipated future challenges and how the client plans to handle them.

## Constraints

### Must

- Output the following labeled sections in order: **Episode Frame**, **Initial Picture**, **Course of the Work**, **Turning Points**, **Gains Internalized**, **Ending Process**, **Letter to Future Self / Forward Handoff**, **Clinician Reflection**, **Continuity Note**.
- Use the client's voice in at least 2 sections (Initial Picture, Gains, or Letter to Future Self).
- Honor planned-vs-forced ending honestly. If termination is forced (clinician leaving), document that explicitly and how it was handled.
- Acknowledge any rupture-and-repair or unfinished business without sanitizing.
- The Letter to Future Self section is written from the clinician *with* the client's articulated content — not generic advice.

### Must Not

- Do not turn this into a duplicate of the discharge summary; do not list outcome-measure trajectories or aftercare specifics here (those live in discharge).
- Do not flatten ambivalent or unfinished endings into "successful completion" if they weren't.
- Do not introduce new clinical content (diagnoses, risk findings) — those go in the discharge summary or a final progress note.
- Do not fabricate the client's words; mark inputs needed as `[client input required: ...]`.

## Instructions

1. State episode frame: dates, total sessions, modality.
2. Reconstruct the initial picture in 1 paragraph: what the client said they wanted; clinician's initial impression.
3. Summarize the course of the work in 1–2 paragraphs: phases, focus shifts, modalities used.
4. List 2–4 turning points: events, sessions, or insights that moved the work forward; include any rupture-and-repair.
5. Articulate gains internalized: not symptom counts but what the client *can now do* / *now knows* / *now experiences differently*. Use client's framing where possible.
6. Document the ending process: planned/mutual/forced; how many sessions used to terminate; what came up emotionally; what the client said about ending.
7. Compose the Letter to Future Self / Forward Handoff section: anticipated stressors and the specific tools/practices/people the client identified for each. Written collaboratively in tone, not prescriptively.
8. Add brief Clinician Reflection (1 paragraph): what the work meant clinically, areas of growth, areas of remaining work the client knows about.
9. Add Continuity Note: where the discharge summary lives, who the receiving provider is (if any), how to reach the practice if the client wants to return.
10. Run verification.

## Output Format

```
=== TERMINATION SUMMARY ===

Client: [Initials/MRN]
Episode of care: [YYYY-MM-DD] – [YYYY-MM-DD]    Total sessions: [N]
Primary modality: [...]
Termination type: [Planned / Mutual / Forced / Other — brief descriptor]

INITIAL PICTURE
[1 paragraph. What the client said they wanted, in their words: "..." Clinician's initial impression.]

COURSE OF THE WORK
[1–2 paragraphs. Phases, focus shifts, modalities used; how the work changed shape over time.]

TURNING POINTS
1. [Event / session / insight, brief context, what shifted.]
2. [...]
3. [Rupture-and-repair if applicable: what happened, how it was addressed.]

GAINS INTERNALIZED
- [Capacity / awareness / practice gained, in client's framing where possible: "..."]
- [...]
- [What the client can now do that they couldn't before.]

ENDING PROCESS
[How the ending was discussed and over how many sessions; what came up emotionally; client's stated meaning of the ending; how planned-vs-forced shaped the work; any unfinished business explicitly named.]

LETTER TO FUTURE SELF / FORWARD HANDOFF
[Composed with the client. Anticipated stressors and the specific tools/practices/people the client named for each. Tone: addressed to the client, written from inside the work, not generic.]

Anticipated stressors and matched resources:
- [Stressor] → [Tool / practice / person]
- [...]

Reminders the client wanted to keep:
- "[client's own words]"
- [...]

CLINICIAN REFLECTION
[1 paragraph: what the work meant clinically, alliance arc, areas of growth, areas of remaining work the client is aware of.]

CONTINUITY NOTE
- Discharge summary location: [chart reference]
- Receiving provider (if any): [name, contact]
- Re-engagement: [How the client can return to the practice if desired; any wait or referral steps.]

Clinician: [name, credentials, signature, date]
```

## Verification

- [ ] All 9 labeled sections present and in order.
- [ ] Client's voice appears in at least 2 sections.
- [ ] Termination type honestly classified; forced/ambivalent endings not sanitized.
- [ ] Turning points include rupture-and-repair if any occurred.
- [ ] Gains stated in capacity / behavior / experience terms (not symptom-count terms).
- [ ] Letter to Future Self maps anticipated stressors → specific resources, not generic advice.
- [ ] No duplication of discharge summary content (no outcome-measure tables, no medication list).
- [ ] No fabricated client words; gaps flagged as bracketed prompts.
