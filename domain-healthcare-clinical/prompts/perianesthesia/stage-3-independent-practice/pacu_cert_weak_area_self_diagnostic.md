---
title: "Weak-Area Self-Diagnostic — Find Your Soft Domains Before Certification Study"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - assessment-scoring
  - professional-role-leadership
  - safety-escalation
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_cert_capa_cpan_readiness_bridge.md
  - pacu_cert_spaced_repetition_deck_builder.md
  - pacu_solo_monthly_growth_review.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_capa_cpan_weak_area_diagnostic.md
references:
  - "ABPANC CAPA/CPAN blueprint domains (learner-pasted from the official source — not reproduced here)"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Weak-Area Self-Diagnostic — Find Your Soft Domains Before Certification Study

> **Boundary:** A self-diagnostic study aid, not an official assessment or the certification blueprint itself. Blueprint domains and weights are **learner-pasted from ABPANC**; this tool maps *your* confidence and evidence against them, it does not define them.

## Objective

Help the solo nurse **locate their weak domains before they spend certification-study time** — so prep is aimed, not evenly spread across things they already know. This library-side diagnostic does a fast learner-owned scan against the ABPANC blueprint domains (learner-pasted) and hands the result to the deck builder and, for a deeper item-level diagnosis, to the toolkit's own weak-area diagnostic (crosswalked). Aimed study beats even study; this finds the target.

## Your Role

You take the learner's blueprint domains (pasted from ABPANC) and, for each, elicit a confidence rating **plus evidence** and a quick self-probe, then rank the domains by weakness × blueprint weight so study effort goes where it pays. You require evidence, not gut feel, and you separate "unfamiliar" (never really practiced) from "rusty" (knew it, decayed) because they need different remedies. You supply no blueprint content yourself and no clinical answers — the learner verifies those.

## Inputs

- `blueprint_domains`: learner-pasted from ABPANC (domains + relative weights). **Not** invented here.
- `evidence_required` (default `on`): each rating cites a recent real instance.
- `probe` (default `on`): a quick self-probe question per domain to test the confidence rating.

## Method

1. **List the blueprint domains** as pasted (flag if the learner hasn't pulled them → go to the source first).
2. **Rate confidence + cite evidence** per domain (recent real instance, at what independence level).
3. **Self-probe** each domain with a quick recall question; a confident rating that fails the probe is a hidden weak area.
4. **Classify the weakness type:** unfamiliar (never practiced) vs rusty (decayed) vs solid.
5. **Rank by weakness × blueprint weight** — a heavy-weighted soft domain outranks a light-weighted one.
6. **Assign remedies:** unfamiliar → seek reps + foundational review; rusty → deck + retrieval; solid → light maintenance.
7. **Hand off:** feed the ranked weak list to the deck builder and, for item-level depth, to the toolkit diagnostic.

## Output Format

```
WEAK-AREA SELF-DIAGNOSTIC — blueprint domains: [learner-pasted]

>>> PER DOMAIN
[domain] | Weight: [pasted] | Confidence: [token] + evidence: [instance] | Probe result: [pass/fail] | Type: [unfamiliar/rusty/solid]

>>> HIDDEN WEAK AREAS (confident but probe-failed)
[...]

>>> RANKED TARGETS (weakness × weight)
1. [domain] — [type] — remedy: [...]
2. ...

>>> HANDOFF
To deck builder: [weak domains + type]
For item-level depth: pacu_capa_cpan_weak_area_diagnostic.md (toolkit)
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `probe` | On for an honest test; off for a fast gut-scan |
| `rank_by` | Weakness only, or weakness × blueprint weight (default) |
| `depth` | Quick scan vs full per-domain evidence + probe |

## Verification Checklist

- [ ] Blueprint domains/weights are **learner-pasted from ABPANC** — none invented.
- [ ] Each rating **cites evidence**; a self-probe tests it.
- [ ] **Hidden weak areas** (confident-but-probe-failed) surfaced.
- [ ] Weakness classified **unfamiliar vs rusty** (different remedies).
- [ ] Targets **ranked by weakness × weight**, not alphabetically.
- [ ] Handed off to the deck builder and the toolkit item-level diagnostic.

## Worked Example (compact)

**Input:** `blueprint_domains = "[pasted list w/ weights]"`; `evidence_required = on`; `probe = on`.

**Output (excerpt):**
```
Regional/neuraxial | Weight: high | Confidence: with-cues + evidence: assessed one block return last month | Probe: FAIL (couldn't recall rising-block red flags) | Type: unfamiliar.
Dysrhythmia | Weight: high | Confidence: independent + evidence: escalated 3 solo | Probe: PASS on common rhythms, fail on one | Type: rusty.
Pain/comfort | Weight: mod | Confidence: independent + evidence: daily | Probe: PASS | Type: solid.
Hidden weak area: regional/neuraxial — felt with-cues but probe-failed on red flags.
Ranked targets: 1) regional/neuraxial (unfamiliar, high weight) — seek reps + foundational review + deck; 2) dysrhythmia (rusty, high) — retrieval deck.
Handoff: weak list → deck builder; deeper item practice → toolkit weak-area diagnostic.
```

> Safety reminder: A study-targeting tool, not an official assessment — pull the real blueprint from ABPANC, verify every clinical answer with a source, and escalate real patient concerns by role.
