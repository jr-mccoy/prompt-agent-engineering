---
title: PACU CAPA/CPAN Weak-Area Diagnostic
category: pacu/exam-prep
task_type: ANALYZE
audience: PACU RN preparing for CAPA or CPAN, diagnosing weak content domains
updated: "2026-05-15"
tags:
  - pacu
  - certification
  - capa
  - cpan
  - exam-prep
  - diagnostic
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
difficulty: intermediate
related_prompts:
  - prompts/pacu_capa_cpan_blueprint_aligned_study_plan.md
  - prompts/pacu_capa_cpan_practice_question_generator.md
references:
  - ABPANC official exam blueprint (current edition — user pastes in domains)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU CAPA/CPAN Weak-Area Diagnostic

> Safety reminder: Self-diagnostic is approximate. The official ABPANC blueprint defines the domains; this prompt produces a candidate-confidence map, not a competency assessment.

## Objective

Produce a **ranked weak-area map** across the candidate's blueprint domains, combining self-rated confidence with practice-question performance. Output feeds `pacu_capa_cpan_blueprint_aligned_study_plan.md` (weak-area multiplier) and prioritizes specific sub-topics to revisit.

## Inputs

- **Exam:** {{CAPA | CPAN | both}}
- **Current ABPANC blueprint domains (paste):** {{candidate-pasted}}
- **Self-rated confidence per domain (1–5):** {{1 = no confidence, 5 = high confidence}}
- **Recent practice-question performance per domain (% correct if available):** {{optional but useful}}
- **Specific sub-topics the candidate has gotten wrong recently:** {{list 5–10}}
- **Time to exam:** {{weeks}}

## Audience / Scope

- **Primary:** Candidate.
- **Secondary:** Coaching educator.
- **Scope:** Confidence + performance map. Not a clinical competency assessment.

## Output requirements

```markdown
# Weak-Area Diagnostic — {date}

> Safety reminder: This is a candidate confidence + performance snapshot. Not endorsed by ABPANC.

**Exam:** {CAPA | CPAN}
**Weeks to exam:** {N}

## Domain map

| Domain | Self-confidence (1–5) | Practice % (if available) | Priority |
|---|---|---|---|
| {domain A — from user paste} | 4 | 78% | low |
| {domain B} | 2 | 55% | high |
| {domain C} | 3 | 70% | medium |
| (etc.) |  |  |  |

Priority rules:
- Self-confidence ≤ 2 OR practice < 65% → **high priority** (1.3x study weight).
- Self-confidence 3 OR practice 65–75% → **medium priority** (1.0x).
- Self-confidence ≥ 4 AND practice ≥ 75% → **low priority** (0.8x, but still spaced-repetition coverage).

## Calibration check

For each domain, ask: does self-confidence match practice performance?
- **Confidence > performance** (overconfident): flag — candidate may underestimate study need.
- **Confidence < performance** (underconfident): flag — candidate may overstudy strong areas.
- **Aligned:** no flag.

Examples:
- Domain B: self-rated 2, practice 55%. Aligned — true weak area.
- Domain D: self-rated 5, practice 65%. Overconfident — flag for diagnostic re-rating.

## Specific sub-topic priorities

Roll up the candidate's "recent items missed" list into sub-topic clusters. For each cluster:
- **Sub-topic:** {e.g., "Aldrete scoring nuances at the borderline"}
- **Domain home:** {which blueprint domain}
- **Number of recent misses on this:** {n}
- **Recommended action:** {targeted reading + 5 practice items on this sub-topic}

## What this diagnostic is not

- Not a competency assessment.
- Not an HR or licensure document.
- Not a pass/fail prediction.
- Not endorsed by ABPANC.

## Re-run cadence

- After every 50 practice questions completed.
- After any score-shifting study activity (full practice test).
- Final 2 weeks before exam.

## Sources / reference

- Candidate-pasted ABPANC blueprint.
- ASPAN *Core Curriculum* — for sub-topic mapping.
```

## Must / Must not

**Must:**
- Use candidate-pasted blueprint domains only.
- Distinguish self-confidence from practice performance and surface calibration mismatches.
- Apply weak-area multiplier within bounded range (0.8x to 1.3x).
- Roll up missed-items list into sub-topic clusters, not individual items.
- Flag overconfidence and underconfidence by name.

**Must not:**
- Fabricate blueprint domains.
- Project pass/fail.
- Use this diagnostic for any clinical competency claim.
- Reference protected characteristics in the diagnostic.
- Multiply weak-area weight beyond 1.3x (the plan unravels).
- Treat self-confidence alone as adequate evidence — flag if no practice data.

## Quality signals

- Candidate finishes the diagnostic with a ranked list and 2–3 sub-topic priorities to drive next week's study.
- Calibration mismatches are surfaced, not hidden.
- The output feeds cleanly into the study plan.

## Verification

- [ ] Domains match user-pasted blueprint.
- [ ] Priority rules applied.
- [ ] Calibration mismatches flagged.
- [ ] Sub-topic clusters rolled up.
- [ ] Multiplier capped at 1.3x.
- [ ] Re-run cadence stated.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No fabricated blueprint domains or weights.**
- **No fabricated practice question correct-rates** beyond what the candidate provided.
- **No fabricated ABPANC sub-topic taxonomy.**
- **No projected pass probability** from confidence or practice scores.
- **No fabricated coaching effectiveness claims.**
- **No invented Drain's / Core Curriculum sub-topic mapping** (use chapter titles, not invented sections).
- **No protected-characteristic-based priority adjustments.**
- **No license-pathway-based diagnostic conclusions.**

## Worked Example

<details>
<summary>Example: CPAN, 8 weeks to exam, mixed confidence + practice data (click to expand)</summary>

```markdown
| Domain | Confidence | Practice % | Priority |
|---|---|---|---|
| {Domain A from candidate paste} | 4 | 80 | low |
| {Domain B} | 2 | 55 | high |
| {Domain C} | 5 | 65 | medium (calibration flag: overconfident) |
| {Domain D} | 3 | 70 | medium |

## Calibration check

- Domain C: confidence 5, practice 65% — overconfident. Flag: re-rate confidence after next 25 practice items on this domain.
- Domain B: aligned, true weak area.

## Sub-topic priorities

- Aldrete scoring at borderline → Domain {x}; 4 recent misses → 30 min targeted reading + 5 practice items.
- Reversal-agent timing → Domain {y}; 3 recent misses → 30 min reading + 5 items.

## Re-run

After next 50 practice items.
```

Notes: priorities applied, calibration flagged, sub-topic rolled up, no fabricated content.
</details>

## Self-check

- [ ] User-pasted blueprint only.
- [ ] Priority rules applied.
- [ ] Calibration mismatches flagged.
- [ ] Sub-topic clusters present.
- [ ] Multiplier in range.
- [ ] Re-run cadence stated.
- [ ] FPP section passed.
