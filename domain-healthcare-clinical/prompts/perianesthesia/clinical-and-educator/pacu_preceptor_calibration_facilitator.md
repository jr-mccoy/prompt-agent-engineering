---
title: PACU Preceptor Calibration Facilitator
category: pacu/preceptor-evaluation
task_type: COMMUNICATE
audience: Educator, charge, or lead preceptor facilitating a norming session across 2–4 PACU preceptors
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - calibration
  - norming
  - bias
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_peer_preceptor_360_feedback.md
  - prompts/pacu_preceptor_difficult_conversation_guide.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Rater-bias and small-N calibration literature (organizational behavior)
---

# PACU Preceptor Calibration Facilitator

> Safety reminder: Calibration aligns sign-off interpretation across preceptors. It does not substitute for facility sign-off documentation, patient-safety event reporting, or formal HR processes.

## Objective

Prepare for or facilitate a **small-N calibration / norming session** among PACU preceptors (typically 2–4 preceptors norming on 1–3 shared orientees) — with explicit bias interventions, anchor-defusing sequencing, and a documentation template that makes the sign-off outcome defensible.

## What calibration is and is not

**Is:**
- A structured conversation to resolve inconsistencies in how preceptors apply the scaffold.
- A venue to catch individual-rater biases.
- A check that sign-off dispositions would look defensible to a charge nurse or educator reading the documentation.

**Is not:**
- Forced distribution or stack-ranking.
- A venue to surface new critical feedback about an orientee for the first time (that should already be known to the orientee via debriefs).
- A place to air grievances about preceptor or orientee personalities.

## When to use

- Two or more preceptors have worked with the same orientee and their sign-off dispositions disagree.
- Multiple orientees are being signed off at a similar phase and the facility wants consistent standards across preceptors.
- A new preceptor is joining the rotation and the facility wants to norm their interpretation of the sign-off scale.

## Inputs

- **Roster:** For each orientee being discussed: initials, phase, primary preceptor, each preceptor's proposed sign-off disposition (Advance / Extend / Remediation) with a one-sentence justification.
- **Scaffold** from `pacu_orientee_evaluation_meta_prompt.md` — the competency list and behavioral anchors everyone used.
- **Sign-off scale:** Defaults to **Independent / With Cues / With Direction / Not Yet** unless facility uses different tokens.
- **Known risks in the room:** new preceptors, notably lenient/severe raters, preceptors with a known relationship conflict, orientees whose dispositions have already generated escalations.
- **Time available** and number of preceptors.

## Audience / Scope

- **Primary:** Facilitator — educator, charge, or lead preceptor.
- **Secondary:** Preceptors in the room.
- **Scope:** PACU Phase 1 orientation sign-off. For non-orientation staff calibration, defer to facility HR tooling.

## Output requirements

If the user is **preparing** for calibration, produce:

```markdown
# PACU Calibration Session Prep — {Date}

> Safety reminder: Prep artifact. Facility orientation program and ASPAN Standards govern final sign-off.

## Pre-reads (distribute 24–48 hours before meeting)
- Roster with proposed dispositions and one-sentence justifications.
- Scaffold from the meta-prompt.
- Sign-off scale definitions: Independent / With Cues / With Direction / Not Yet.

## Rater Tendency Snapshot (PACU, small-N)
| Preceptor | # orientees | Proposed distribution (Adv / Ext / Rem) | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

If sample is too small for a distribution to mean anything, say so. The goal is to spot individual patterns (one preceptor always advancing, another always extending), not to enforce a curve.

## Agenda (mixed sequence — do not start at the strongest or weakest orientee)
1. {Orientee initials — moderate case, not highest or lowest}
2. ...

Allocate ~8–12 minutes per orientee. Adjust for complexity.

## Ground Rules (read aloud at opening)
- We calibrate to the scaffold and the evidence, not to a distribution.
- Every proposed disposition change names the competency criterion and the evidence.
- No references to age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- No references to license pathway (BSN/ASN/LPN-bridge) or prior unit as performance signals.
- No personality labels — translate to observable behavior.
- The orientee's primary preceptor is the lead voice; others are the check.
- No critical feedback surfaces here for the first time — if it hasn't been in a debrief, we table the item and deliver it live first.

## Facilitator Bias-Intervention Cheat Sheet
| Pattern | What to say |
|---|---|
| Recency dominates | "Let's pause — what from the first half of the phase?" |
| Personality label | "Translate that to a specific behavior and impact." |
| Stack-ranking by vibe | "Which competency anchor separates these two? Let's look at it." |
| One preceptor dominating airtime | "Let's hear from {other preceptor} — would you sign off the same?" |
| ICU-halo or prior-unit bias | "Is that signal about PACU competency, or about a prior unit? Let's anchor to the PACU scaffold." |
| "I trained them so they must be ready" | "If a different preceptor had trained them, would the evidence support this disposition?" |
| Conflict-aversion leniency | "If extending orientation weren't socially awkward, would the evidence support advancing?" |
| Halo / horns across competencies | "We're rating everything the same direction. Where is this orientee mid-tier?" |
| Surprise critical feedback | "Has this been in a debrief? If not, we table the change until that conversation happens." |
| Similar-to-me signal | "What's the PACU requirement here versus personal preference?" |

## Documentation Template (per orientee)
```
- Orientee initials / phase
- Primary preceptor
- Preceptors in the room
- Proposed disposition: {Advance / Extend / Remediation}
- Final disposition after calibration: {...}
- If changed: competency criterion invoked, evidence cited, who raised the challenge
- If unchanged: whether anyone challenged and what the response was
- Open follow-up (e.g., "primary preceptor to deliver updated feedback to orientee by {date} using pacu_preceptor_difficult_conversation_guide.md")
```

## Close-out Actions
- Every preceptor leaves with a written record of what changed for their orientee and why.
- Any orientee whose disposition changed gets that communicated by their **primary** preceptor, with reasoning, **before** the written evaluation lands.
- No orientee learns of a calibration-driven change for the first time by reading their written evaluation.
- Pattern-level rater issues (systematic severity, systematic leniency, inconsistent anchor application) are flagged for a follow-up educator conversation — not silently absorbed by adjusting that preceptor's dispositions.
```

If the user is **running the session live** and asking for in-the-moment help:

```markdown
# PACU Calibration Intervention

Pattern I'm seeing: {name it in plain language}

Suggested intervention (verbatim script):
"{wording — short, anchored to scaffold}"

What to watch for next: {...}
```

## Per-orientee discussion structure

For each orientee in the mixed sequence:

1. **Primary preceptor presents.** 60–90 seconds: proposed disposition, top evidence per key competency.
2. **Clarifying questions only.** Not rebuttals yet.
3. **Alternative readings.** Any preceptor who would sign off differently names the competency criterion where they'd disagree and the evidence they'd weigh differently.
4. **Facilitator bias check.** Interject using the cheat sheet when you see a pattern.
5. **Decision.** Either the disposition stands, or the group agrees on a revised disposition tied to a specific competency criterion and evidence. Document the rationale.
6. **Next orientee.** Move on. Do not loop back unless new evidence surfaces.

## Must / Must not

**Must:**
- Anchor every disposition change to the scaffold and specific evidence.
- Intervene on biases by name in real time.
- Mix the sequence; do not start at the strongest or weakest orientee.
- Require that any critical feedback surfaced in calibration has already been delivered to the orientee in a debrief.
- Document every change and every non-change that was challenged.
- Down-scope the HR model to PACU reality: 2–4 preceptors norming on 1–3 orientees, not a large-N forced distribution.
- Name escalation partners by role (educator, charge, nurse manager, anesthesiology lead), never by name.

**Must not:**
- Enforce a forced distribution of orientation dispositions. If the pattern is off, surface the scaffold-application issue; do not silently move orientees.
- Allow references to age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Allow medical or family-situation speculation ("seems burned out," "has a lot going on at home").
- Allow personality labels as disposition rationale.
- Allow license-pathway or prior-unit background as a performance signal.
- Let one preceptor change another preceptor's disposition without the primary preceptor engaging with the challenge.
- Let the loudest voice set the norm.
- Introduce critical feedback about an orientee that has not previously been delivered to them — flag it for a debrief and defer.
- Rank orientees by gut.
- Fabricate distribution expectations; the facility sets them, the facilitator does not invent them.

## Quality signals

- Every proposed change is traceable to a competency criterion and cited evidence.
- Airtime is reasonably distributed among preceptors in the room.
- No protected-characteristic or personal-circumstance talk occurred.
- No surprise critical feedback landed on an orientee without a plan to deliver it live first.
- Pattern-level rater concerns are flagged for follow-up training, not quietly absorbed.

## Self-check (facilitator, during and after)

**During:**
- [ ] Every proposed change is tied to a competency criterion.
- [ ] I have intervened on at least one bias pattern by name.
- [ ] No protected-characteristic or personal-circumstance talk.
- [ ] No surprise critical feedback has landed without a plan.
- [ ] Airtime is distributed.
- [ ] No patient-identifying information surfaced in discussion.

**After:**
- [ ] Every change is documented with competency criterion, evidence, and who raised the challenge.
- [ ] Every preceptor has a written list of their orientees' final dispositions and why.
- [ ] Rater patterns are flagged for training, not silently absorbed.
- [ ] No orientee will learn of a calibration-driven change for the first time via a written evaluation.
- [ ] Safety reminder present on the session prep artifact.

## Verification

Before the session runs:

- [ ] Pre-reads have been distributed 24–48 hours ahead.
- [ ] Agenda mixes the sequence (does not start at strongest or weakest orientee).
- [ ] Ground rules block explicitly lists protected-characteristic exclusions and license-pathway exclusion.
- [ ] Facilitator bias-intervention cheat sheet covers recency, halo, stack-ranking, ICU-halo, "I trained them," conflict-aversion, and similar-to-me.
- [ ] Documentation template has a row for "disposition unchanged but challenged" — not just "changed."

After the session:

- [ ] Every disposition change has: competency criterion invoked, evidence cited, who raised the challenge.
- [ ] No new critical feedback surfaced in calibration — it was either known or tabled for a debrief first.
- [ ] Pattern-level rater issues (systematic severity, systematic leniency) were flagged for educator follow-up, not silently absorbed via disposition changes.

## False-Positive Prevention

Do **not** fabricate or encourage:

- **No forced distribution.** The facility sets any distribution expectation; the facilitator does not invent one.
- **No invented rater-tendency statistics** if the sample size is small — say the sample is small and skip the distribution.
- **No new critical feedback about an orientee during calibration.** If it hasn't been in a debrief, it does not drive a disposition change.
- **No invented facility HR process specifics** (PIP thresholds, termination pathways, EAP escalation criteria).
- **No personality labels** as disposition rationale.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as signals.**
- **No speculation about the orientee's medical, mental-health, or family circumstances.**
- **No invented competency rubric thresholds or weights.**
- **No patient-identifying information** in the discussion record.

## Worked Example

<details>
<summary>Example: Facilitator intervention snippet — two preceptors disagree on a Week 10 final disposition (click to expand)</summary>

```markdown
# PACU Calibration Intervention

Pattern I'm seeing: Preceptor A is leaning "Advance" citing "she handled the last two weeks well." Preceptor B is leaning "Extend" citing "I never saw her independently escalate."

Suggested intervention (verbatim script):
"Let's pause — Preceptor A, the last two weeks is recency. Can you pull from Weeks 5–8? Preceptor B, 'never saw her independently escalate' — let's anchor to the scaffold. Which escalation competency, on which shifts, and what was the cueing level?"

What to watch for next: If Preceptor A can pull evidence from Weeks 5–8 that matches the "Independent" anchor, the disposition may stand. If Preceptor B names a specific shift where cueing was required, that becomes a sign-off-level specific change — not an overall disposition change.
```

Notes: names the bias pattern (recency vs halo-from-one-shift), provides verbatim wording tied to the scaffold, anticipates the next decision point.
</details>
