---
title: "Bow-Tie Analysis — Threats, One Top Event, Consequences, and the Barriers Between Them"
category: risk/barrier-analysis
description: "Build a bow-tie for one serious hazard: name the single top event (the moment control is lost), map the threats that lead to it and the consequences that follow, place preventive barriers on the left and mitigative barriers on the right, rate each barrier effective / degraded / missing on evidence, list the degradation factors that erode barriers and the controls on them, check barrier independence, and rank the thinnest paths; distinct from `domain-risk/risk_fmea_analysis.md` (step-by-step failure modes with RPN scores) and `domain-risk/risk_threat_model_non_technical.md` (intelligent adversaries)."
techniques:
  - DS-01
  - RT-07
  - DT-05
  - QA-02
  - DS-06
difficulty: intermediate
tags:
  - bow-tie
  - barrier-analysis
  - hazard-analysis
  - process-safety
  - controls
  - risk-assessment
updated: "2026-09-24"
reasoning:
  styles: [causal, structural, systems, adversarial]
  stakes: high
  horizon: weeks_to_months
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: [diagram_table, matrix_ranked_list]
  user_role: [operator, safety-lead, risk-lead, facilities, engineer]
  mode: [audit, diagnose, plan]
related_prompts:
  - domain-risk/risk_fmea_analysis.md
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_after_action_review.md
---

# Bow-Tie Analysis

**Objective:** For one hazard that could hurt people, stop the operation or end the
business, show every route to the moment control is lost and every route from it to harm,
and show — barrier by barrier, on evidence — how much actually stands in the way. The
product is a ranked list of the thinnest paths and what would thicken them.

**When to Use:**
- One hazard dominates the register (fire, a toxic release, a payment sent to the wrong
  party, a data leak, a patient given the wrong dose) and "we have controls" needs checking.
- A regulator, insurer or client asks you to demonstrate control of a major hazard.
- After a near-miss, to see which barriers held and which were only on paper.
- To explain to non-specialists why one control failing matters more than another.

**Not this prompt if:**
- The subject is a multi-step process where you need failure modes per step with severity,
  occurrence and detectability — `domain-risk/risk_fmea_analysis.md`.
- The threat is an intelligent adversary adapting to your defences — `domain-risk/risk_threat_model_non_technical.md`.
- You need a catalogue of many risks — `domain-risk/risk_register_builder.md`; a bow-tie is one hazard deep.
- It has already happened and you need learning — `domain-risk/risk_after_action_review.md`
  (bring this bow-tie to it).

## Inputs / Context

1. **The hazard:** the thing with potential for harm (stored energy, a chemical, money in motion, personal data).
2. **The operation around it:** sites, shifts, people, equipment, suppliers.
3. **Existing controls** as written (procedures, equipment, training, contracts) and any
   evidence of how they perform: inspection records, audit findings, near-miss reports.
4. **Incident and near-miss history** for this hazard or peers.
5. **Who owns each control** today.

## Method

1. **Name one top event (DS-01).** The moment control of the hazard is lost — not a cause,
   not a consequence. "Fire in battery storage", not "faulty charger" and not "warehouse
   destroyed". If you cannot choose, you have two bow-ties.

2. **List threats (left).** Each is an independent route to the top event. Four to eight is
   typical; merge threats that share every barrier.

3. **List consequences (right).** Each is a distinct harm: to people, assets, operations,
   compliance, reputation. Quantify where you can.

4. **Place barriers on each path (DT-05).** Preventive barriers between each threat and the
   top event; mitigative barriers between the top event and each consequence. A barrier must
   be able to stop the sequence on its own: a detection alone is not a barrier unless someone
   or something acts on it. Training and procedures count only when tied to a specific action.

5. **Rate each barrier on evidence.** Effective (inspected or tested, working) / Degraded
   (exists, evidence of lapses) / Missing (on paper only, or not at all). Record the evidence
   and the owner.

6. **Add degradation factors and their controls.** For each Degraded or critical barrier:
   what erodes it (time pressure, maintenance backlog, shift change, supplier change) and what
   keeps that factor in check.

7. **Check independence (QA-02).** Barriers sharing a power supply, a contractor, a person or
   an IT system can fail together. Count them as one on that path.

8. **Trace escalation and rank the thin paths (RT-07, DS-06).** For each path count the
   independent Effective barriers. Paths with zero or one rank first, weighted by the severity
   of the consequence they lead to. Assign each fix an owner and date.

## Output Format

```
# Bow-tie — [hazard] at [operation], [date]
Top event: [the moment control is lost]

## Left side — threats and preventive barriers
| Threat | Barrier | Rating E/D/M | Evidence | Owner | Independent of |

## Right side — consequences and mitigative barriers
| Consequence (quantified) | Barrier | Rating E/D/M | Evidence | Owner | Independent of |

## Degradation factors
| Barrier | What erodes it | Control on the erosion | Owner |

## Barrier summary
Preventive: [n] total — [e] effective, [d] degraded, [m] missing
Mitigative: [n] total — [e] effective, [d] degraded, [m] missing

## Thin paths, ranked
| Path | Independent effective barriers | Consequence severity | Fix | Owner | Due |
```

## Verification

- [ ] Exactly one top event, phrased as loss of control.
- [ ] Every threat and consequence has at least one barrier or is flagged as unprotected.
- [ ] Every barrier can stop the sequence on its own; detection-only items are paired with a response.
- [ ] Every barrier rated E/D/M with evidence and an owner.
- [ ] Common-mode dependencies identified and counted once.
- [ ] Summary counts match the tables.
- [ ] Thin paths ranked by effective independent barriers × consequence severity, each with an owner and date.

## False-Positive Prevention

1. **Causes or harms as the top event.** "Charger fault" is a threat; "warehouse destroyed" is a
   consequence. A mislabelled centre scrambles every barrier placement.
2. **Paper barriers.** A procedure nobody follows is Missing, however well written. Rate on
   inspection, test or observation.
3. **Counting shared barriers twice.** Two alarms on one circuit are one barrier when the power fails.
4. **"Training" as a barrier.** Training supports a barrier; it is not one unless it maps to a
   specific action that stops the sequence.
5. **Barrier counting as safety.** Five degraded barriers can be thinner than one effective one.
   Rate quality before counting.
6. **Right side neglected.** Prevention-only bow-ties assume the top event never happens.
   Mitigation is where the size of the loss is decided.
7. **One-off diagram.** Barrier ratings decay. Tie re-rating to the inspection cycle.

## Example Output

```
# Bow-tie — lithium-ion battery stock at regional warehouse, 2026-09-15
Top event: uncontrolled fire in the battery storage bay

## Left side
| T1 Damaged battery accepted | B1 Inbound damage inspection | E | QA log, 100% of pallets checked | Receiving Lead | — |
|                             | B2 Quarantine bay for damaged units | D | Bay full in 40% of weeks | Receiving Lead | — |
| T2 Overcharge at charging station | B3 Chargers with automatic cut-off | E | Vendor test 2026-06 | Facilities | B5 (same contractor) |
|                                   | B4 Charging only in attended hours | D | Night charging seen on 3 of 10 checks | Shift Manager | — |
|                                   | B5 Monthly charger inspection | M | None since March | Facilities | B3 |
| T3 Hot works nearby | B6 Hot-work permit | E | Permit audit, 12 of 12 compliant | Facilities | — |
|                     | B7 60-minute fire watch after works | E | Permit sign-offs | Facilities | — |
| T4 Intrusion / arson | B8 Fencing + monitored CCTV | E | Monitoring contract, test 2026-08 | Security | — |

## Right side
| C1 Staff injury | M1 Aspirating smoke detection | E | Quarterly test | Facilities | — |
|                 | M2 Evacuation drill | D | Last drill 14 months ago | H&S Lead | — |
| C2 Spread to main warehouse ($3.1M stock) | M3 4-hour fire wall + separation | E | Fire engineer survey 2025 | Facilities | — |
|                                           | M4 Suppression rated for lithium fires | M | Sprinklers not rated for this hazard | Facilities | — |
| C3 Six-week shutdown | M5 Alternate-site continuity plan | D | Written, never tested | COO | — |
|                      | M6 Business-interruption insurance | E | Policy schedule | Finance | — |

## Degradation factors
| B4 | Night-shift pressure to charge for early dispatch | Timer lockout on chargers 22:00–06:00 | Facilities |
| B2 | Returns volume peaks after holidays | Overflow quarantine cage at peak | Receiving Lead |

## Barrier summary
Preventive: 8 total — 5 effective, 2 degraded, 1 missing
Mitigative: 6 total — 3 effective, 2 degraded, 1 missing

## Thin paths, ranked
1. T2 → top event: B3 and B5 share a contractor, B5 missing, B4 degraded → 1 independent effective barrier — reinstate monthly inspection by a second firm + timer lockout — Facilities — 2026-10-31
2. Top event → C2 ($3.1M): M3 only; M4 missing — specialist suppression quote and install decision — COO — 2026-12-15
3. Top event → C1: M1 effective, M2 degraded — evacuation drill — H&S Lead — 2026-10-10
```

## Techniques Used

- **DS-01 Framework Application** — the bow-tie structure itself.
- **RT-07 Cascade Effect Analysis** — paths traced from threat through top event to harm.
- **DT-05 Element-by-Element Assessment Matrix** — each barrier rated on evidence.
- **QA-02 Adversarial Stress-Test** — independence and common-mode failure check.
- **DS-06 Prioritization and Severity Guidance** — thin paths ranked by barriers × severity.

## Related Prompts

- `domain-risk/risk_fmea_analysis.md` — per-step failure modes when the subject is a process.
- `domain-risk/risk_register_builder.md` — where the hazard and its fixes are logged.
- `domain-risk/risk_key_risk_indicators.md` — monitor degradation factors as leading indicators.
- `domain-risk/risk_after_action_review.md` — after a near-miss, test which barriers held.
