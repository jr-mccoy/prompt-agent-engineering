---
title: "MI Change-Talk Coder (DARN-CAT Transcript Coding)"
category: psychology/modalities/motivational-interviewing
description: "Code a session transcript or excerpt for DARN-CAT change talk vs sustain talk, with line-by-line tags, frequency tallies, MI-adherence audit, and feedback for the interviewer."
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
  - DARN-CAT
  - change-talk
  - sustain-talk
  - MITI
  - coding
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_decisional_balance_facilitator.md
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_oars_response_generator.md
  - domain-psychology/modalities/motivational-interviewing/psychology_mi_ambivalence_map.md
---

# MI Change-Talk Coder (DARN-CAT Transcript Coding)

## Objective

Code a session transcript or excerpt for client change talk (DARN-CAT) and sustain talk, line by line. Produce a coded transcript, frequency tallies, and an MI-adherence audit of the clinician's behavior. The output supports supervision, MITI-style feedback, and clinician self-correction.

## When to Use

- Supervision / consultation review of an MI session.
- MITI-style fidelity coding (informal — full MITI 4.2.1 coding requires certification).
- Self-review by the clinician.
- Training / didactic exercise.
- Pre/post training comparison.
- Not as a substitute for live MITI certification.

## Inputs / Context

- Transcript excerpt (verbatim, with speaker labels) or accurate paraphrase with line numbers.
- Behavior under discussion (target behavior the MI session is addressing).
- Stance: equipoise or change-favoring.
- Stage of change at the time.
- Clinician's training level and the supervision goal.
- Modality of the session.

## Constraints

### Must

- Tag **every client utterance** with one of:
  - **CT-D** (Desire), **CT-A** (Ability), **CT-R** (Reasons), **CT-N** (Need), **CT-C** (Commitment), **CT-Ac** (Activation), **CT-TS** (Taking Steps) — change talk subtypes.
  - **ST-D / ST-A / ST-R / ST-N / ST-C / ST-Ac / ST-TS** — sustain talk subtypes.
  - **Neutral / Follow / Other**: not on the target topic.
- Tag **every clinician utterance** with MI behavior:
  - Open question (OQ), Closed question (CQ), Simple reflection (SR), Complex reflection (CR), Affirmation (AF), Summary (SU), Information / advice with permission (I/A+), Information / advice without permission (I/A−), Confront (CF — MI-inconsistent), Direct (DI — MI-inconsistent), Persuade (PE — MI-inconsistent).
- Compute frequency tallies and ratios:
  - Change-talk : sustain-talk count.
  - Reflections : questions (target ≥ 1:1; MI-adherent commonly ≥ 2:1).
  - Complex : simple reflections (target ≥ 50% complex).
  - MI-inconsistent behavior count (target 0).
- Identify any **sequential turn** where the clinician's response amplified change talk or evoked sustain talk.
- For MI-inconsistent moments, propose an MI-consistent alternative.
- Document supervisor / clinician's feedback goal.
- Mark uncertainty: if a tag is borderline, note `[?]` and explain.

### Must Not

- Do not over-count change talk — tag conservatively. Borderline = `[?]`.
- Do not coach during coding; the artifact is for review, not in-vivo redirect.
- Do not claim MITI certification unless the coder holds it.
- Do not omit MI-inconsistent behaviors to protect the clinician; that defeats supervision.
- Do not impose a stance on the clinician different from what they intended; note discrepancy if any.
- Do not fabricate client or clinician utterances; if transcript is incomplete, mark gaps.

## Instructions

1. Read the excerpt; note speakers and line numbers.
2. Tag each utterance with the codes above.
3. Compute tallies and ratios.
4. Identify pivot moments (clinician responses that amplified change talk or evoked sustain talk).
5. For MI-inconsistent behaviors, write an alternative response.
6. Provide a feedback summary aligned with the supervisor's goal.
7. Note uncertainty and gaps.

## Output Format

```
=== MI CHANGE-TALK CODING REPORT ===
Coder: [Name]    Date: [YYYY-MM-DD]    Transcript source: [Session date / supervisor request]
Clinician: [Name]    Stage of change at session: [...]
Stance (declared): [Equipoise / Change-favoring]
Target behavior: [...]

CODED TRANSCRIPT
| Line | Speaker | Utterance (verbatim) | Tag | Notes |
|------|---------|----------------------|-----|-------|
| 1 | Clinician | "[...]" | OQ | [...] |
| 2 | Client | "[...]" | CT-R | [...] |
| 3 | Clinician | "[...]" | CR | reflects change talk |
| 4 | Client | "[...]" | CT-D | amplification |
| ... | ... | ... | ... | ... |

TALLIES
- Client change talk: CT-D [N], CT-A [N], CT-R [N], CT-N [N], CT-C [N], CT-Ac [N], CT-TS [N] = total CT [N]
- Client sustain talk: ST-D [N], ST-A [N], ST-R [N], ST-N [N], ST-C [N], ST-Ac [N], ST-TS [N] = total ST [N]
- Ratio CT:ST = [N:M]

- Clinician OQ: [N]    CQ: [N]    SR: [N]    CR: [N]    AF: [N]    SU: [N]
- I/A+: [N]    I/A−: [N]    CF: [N]    DI: [N]    PE: [N]
- Reflections : questions = [N:M]
- Complex : simple = [N:M]
- MI-inconsistent count: [N]

PIVOT MOMENTS
- Line [k]: clinician [SR/CR] amplified [CT-X] in next client turn.
- Line [k]: clinician [CF/PE/DI] preceded [ST-X] surge — alternative: "[...]"

OBSERVATIONS
- Strength: [...]
- Growth area: [...]
- Stance fidelity: [Declared stance vs in-session behavior]

FEEDBACK FOR CLINICIAN
- Top 1–2 takeaways: [...]
- Next-session focus: [Reflections-to-questions; complex reflections; reduce I/A−]

UNCERTAINTY / GAPS
- Borderline tags: [Line(s); rationale]
- Transcript gaps: [...]

NOTES
- Not MITI 4.2.1 certified coding unless coder holds certification.
- For research, use MITI-trained raters.
```

## Verification

- [ ] Every client utterance tagged with DARN-CAT or sustain subtype.
- [ ] Every clinician utterance tagged with MI behavior.
- [ ] Tallies and ratios computed.
- [ ] Pivot moments identified.
- [ ] MI-inconsistent moments have proposed alternatives.
- [ ] Borderline tags marked uncertain.
- [ ] Feedback summary aligned with supervision goal.
- [ ] No fabricated lines.
- [ ] No claim of MITI certification beyond actual.
- [ ] Gaps in transcript noted.
