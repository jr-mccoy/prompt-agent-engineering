---
title: "Supplier Corrective Action (SCAR) and 8D Review — Issue, Contain, Verify Root Cause, and Prove Effectiveness, Then Close"
category: operations/supply-chain-procurement
description: "Issue a supplier corrective action request with a defect statement the supplier cannot argue with, then review the supplier's 8D response discipline by discipline — containment that covers parts in transit and at your site, a root cause for both occurrence and escape, permanent actions that remove it, and verification of effectiveness on post-change lots — and close only on evidence."
techniques:
  - QA-08
  - RT-09
  - AG-02
  - DP-24
difficulty: intermediate
tags:
  - scar
  - 8d
  - supplier-quality
  - corrective-action
  - containment
  - verification-of-effectiveness
  - supplier-keeps-sending-bad-parts
  - review-supplier-response
  - defective-shipment
updated: "2026-10-02"
related_prompts:
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
  - domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md
  - domain-risk/risk_fmea_analysis.md
---

# Supplier Corrective Action (SCAR) and 8D Review

**Objective:** Write a SCAR that states the nonconformance precisely enough to
demand a real investigation, then grade the supplier's 8D response against
gate criteria for each discipline (D0–D8) and decide accept, return for rework, or
escalate — closing only when post-change lots prove the fix.

**When to Use:**
- A supplier shipped nonconforming material and you need a formal corrective action,
  not an email apology.
- A supplier returned an 8D that says "operator error — retrained" and you suspect
  it will not hold.
- The same defect from the same supplier is back for the second time.
- Your quality system or customer requires documented supplier corrective action.
- **Not this prompt if** the problem is in your own process — use
  `domain-operations/process-improvement/ops_root_cause_a3_report.md` (your A3, your
  causes; here the supplier owns the investigation and you judge it). If you are
  deciding whether to replace the supplier, use
  `domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md`.
  To anticipate failure modes before a part is launched, use
  `domain-risk/risk_fmea_analysis.md`.

## Inputs / Context

1. **Nonconformance evidence**: part number, revision, lot/date codes, quantity
   received, quantity inspected, quantity defective, the requirement violated
   (drawing dimension, spec clause), photos, measurement data. Tag `measured` or
   `sampled (n=)`.
2. **Impact**: line stoppage, scrap, rework hours, customer escapes, sorting cost.
3. **History**: prior SCARs with this supplier, open or closed, and the defect type.
4. **Quality agreement terms**: response deadlines, chargeback rules, required format.
5. **The supplier's 8D response**, if you are reviewing one.

## Method

1. **D0 — decide whether a SCAR is warranted.** One isolated minor defect may need
   only a notification. Issue a SCAR for: repeat defects, safety or fit/function
   impact, customer escapes, or quantity above the agreement's threshold.
2. **Write the SCAR (D2 handed to the supplier).** Is/is-not form: what part, what
   defect, where on the part, how many of how many, which lots, when detected, what
   requirement — and what it is *not* (other lots, other features). No cause guessed.
   Set due dates: containment 24–48 h, root cause 10 working days, permanent action
   and verification 30–60 days.
3. **Gate each discipline (QA-08).** Review the response against these gates; any
   gate failed returns the 8D:
   - **D1 Team**: includes someone with process authority at the supplier, not only
     their quality clerk.
   - **D3 Containment**: covers stock at supplier, in transit, and at your site; states
     the sort method, quantity sorted, quantity found, and how sorted parts are
     identified. A clean-point lot number is defined.
   - **D4 Root cause**: two causes — **occurrence** (why the defect was made) and
     **escape** (why their controls did not catch it). Each verified by turning the
     defect on and off or by data, not by assertion (RT-09).
   - **D5 Permanent actions**: each addresses a verified cause; error-proofing or a
     process change outranks inspection and training.
   - **D6 Implementation**: dated, with the first lot produced under the change.
   - **D7 Prevention**: PFMEA and control plan updated; similar parts and lines checked.
   - **D8 Closure**: only after verification of effectiveness.
4. **Read skeptically (AG-02).** Treat "operator error", "isolated incident",
   "retrained", and "100% inspection added" as unproven until evidence shows why the
   process allowed it and how the change prevents it.
5. **Verification of effectiveness (DP-24).** Fix the closure criterion before the
   change runs: e.g. "zero defects of this mode in the first 5 lots or 10,000 parts,
   measured at your incoming inspection at tightened sampling." Supplier-reported
   results alone do not close a SCAR.
6. **Decide**: accept, return with specific gate failures, or escalate (supplier
   on probation, new business hold, re-sourcing review). Record cost recovery.

## Output Format

```
# SCAR [number] — [supplier] — [part, rev]     Issued: [..]   Status: [..]

## Nonconformance (is / is not)
| | Is | Is not |
| What | | |
| Where | | |
| When / lots | | |
| How many | | |
Requirement violated: [..]   Impact: [..]

## Due dates
Containment: [..]  Root cause: [..]  Permanent action + VoE: [..]

## 8D review
| D | Gate | Supplier response | Pass / Fail | Gap |

## Verification of effectiveness (criterion fixed [date])
| Criterion | Measured by | Lots / qty | Result |

## Decision
[accept | return | escalate] — reasons — cost recovery [..]
```

## Verification

- [ ] The SCAR has quantity defective out of quantity inspected, lot codes, and the violated requirement.
- [ ] The SCAR contains no assumed cause.
- [ ] Containment covers supplier, in-transit, and your site, with a clean-point lot.
- [ ] Root cause addresses both occurrence and escape, each verified.
- [ ] Every permanent action maps to a verified cause.
- [ ] The VoE criterion was fixed before post-change lots arrived and uses your own data.
- [ ] Decision and cost recovery are recorded.

## False-Positive Prevention

1. **Retraining as root cause.** If trained operators made the defect, training was
   not the gap. Ask what in the process made the error possible and invisible.
2. **Containment mistaken for correction.** 100% inspection at the supplier is
   containment. Accept it with an end date, not as D5.
3. **Escape cause missing.** An 8D explaining only occurrence leaves the same weak
   detection in place for the next defect.
4. **"Unable to reproduce."** That is a finding about the investigation, not
   evidence the defect is gone. Ask what was tried.
5. **Closure on paperwork.** A complete form with no post-change lot data is not
   closed.
6. **Your own measurement doubted last.** Before issuing, check that your gauge and
   drawing revision agree with theirs; a revision mismatch is a common false SCAR.
7. **Safety and regulated parts.** Automotive (IATF 16949), aerospace (AS9100/AS9145),
   and medical (ISO 13485) parts carry customer- or regulator-specific requirements;
   the responsible quality function approves closure.

## Example Output

```
# SCAR 2026-031 — Precision Stampings Ltd — Bracket 44-118 rev C   Issued 2026-09-08

## Nonconformance (is / is not)
|            | Is                                        | Is not                     |
| What       | hole Ø6.2 position out (1.4 mm vs ±0.25)  | hole diameter; flatness    |
| Where      | hole B only                               | holes A, C                 |
| When/lots  | lots 2608, 2609 (Aug 24–29)               | lots 2601–2607             |
| How many   | 212 of 1,500 sampled (sampled n=1,500, 14.1%) | —                      |
Requirement: drawing 44-118C, position ⌖0.25 to datum A|B.
Impact: line 3 stopped 6 h; 3,000 brackets sorted; $8,400 sort + downtime.

## Due dates
Containment 10 Sep; root cause 22 Sep; permanent action + VoE 23 Oct.

## 8D review (response received 21 Sep)
| D1 | Process owner on team      | Toolroom lead included     | Pass |                    |
| D3 | 3-location containment     | Sorted WIP + FG; transit not mentioned | Fail | 2 pallets in transit unsorted |
| D4 | Occurrence verified        | Pilot pin worn 0.3 mm; defect reproduced with worn pin, gone with new | Pass | |
| D4 | Escape verified            | "Operator missed it"       | Fail | why didn't first-piece check catch it? |
| D5 | Action → cause             | New pin; "retrain inspector" | Partial | pin life limit + escape action needed |
| D7 | PFMEA/control plan updated | not provided               | Fail |                    |
Decision on response: RETURN — 3 gate failures.

Resubmitted 2 Oct: transit stock sorted (0 defects of 400); escape cause =
first-piece check used a go/no-go pin not covering hole B position → new
position gauge for all three holes; pin replacement at 80,000 hits added to
control plan; sister die 44-120 checked. Gates now pass.

## Verification of effectiveness (criterion fixed 2 Oct)
| Zero hole-B position defects | our CMM, n=80/lot (tightened) | first 5 lots | [measure] |

## Decision
Accept D1–D7; D8 pending VoE. Chargeback $8,400 per quality agreement §7.
```

## Techniques Used

- **QA-08 Gate-Based Verification** — each discipline has explicit pass/fail gates.
- **RT-09 Root Cause Explanation Pattern** — occurrence and escape causes, each verified.
- **AG-02 Skeptical Default Stance** — common 8D claims treated as unproven until evidenced.
- **DP-24 Done Fudge Prevention** — the closure criterion fixed before post-change lots arrive.

## Related Prompts

- `domain-operations/process-improvement/ops_root_cause_a3_report.md` — root cause of a problem in your own process.
- `ops_supplier_selection_scorecard.md` — when repeated SCARs raise the re-sourcing question.
- `domain-risk/risk_fmea_analysis.md` — failure modes before they occur; the PFMEA the D7 update touches.
