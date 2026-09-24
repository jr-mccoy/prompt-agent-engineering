---
title: "Post-Trial Motion Set"
category: legal/litigation
description: "Draft the coordinated post-trial motion set after a verdict or bench judgment — renewed judgment as a matter of law, new trial, remittitur or additur, alteration or amendment of judgment, and amended findings — with a hard-deadline gate, a preservation check against the pre-verdict record, and appellate-clock effects, distinct from the appellate issue-selection memo that comes after these motions are decided."
techniques:
  - DD-03
  - RT-02
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - legal
  - litigation
  - post-trial
  - new-trial
  - jmol
  - lost-at-trial-what-now
  - jury-verdict-too-high
updated: "2026-09-24"
related_prompts:
  - domain-legal/appellate/legal_issue_selection_memo.md
  - domain-legal/litigation/legal_jury_instruction_drafter.md
  - domain-legal/litigation/legal_motion_in_limine_set.md
---

# Post-Trial Motion Set

**Objective:** In the short, typically non-extendable window after judgment, produce the right combination of post-trial motions — each ground preserved, each motion under the correct rule and standard, alternatives pleaded so the court can rule conditionally — and protect the appellate clock. The output is a deadline-and-preservation map first, then the motions.

> **Scope guard — attorney-facing.** For trial or appellate counsel of record after a verdict or bench judgment. It does not decide whether to appeal. A self-represented party should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` immediately; post-trial deadlines are short.

## When to Use

- A jury verdict or bench judgment has been entered (or is about to be) and your client lost, won less than it should, or faces an excessive award.
- You won and need to anticipate and oppose the other side's post-trial motions (run the method from the other side and produce oppositions).
- The judgment contains a clerical or computational error, omits prejudgment interest, or misstates relief.

**Not this prompt if:**
- Post-trial motions have been decided and you are choosing appellate issues — use `domain-legal/appellate/legal_issue_selection_memo.md`.
- The case ended on summary judgment or dismissal (no trial) — a motion to alter or amend may still apply, but the JMOL and new-trial analysis here does not; narrow the method accordingly.
- You are still at trial and need to make the pre-verdict motion — that motion must be made before submission to the jury `[VERIFY: FRCP 50(a) or analog]`; draft it separately.

## Inputs

- **Jurisdiction (required):** Court (federal or state), the post-trial rules that apply (e.g., FRCP 50(b), 52(b), 59, 60 or state analogs), and the date of entry of judgment as docketed.
- **Trial record:** Pre-verdict JMOL motion(s) and the grounds stated; objections to instructions and the verdict form; evidentiary objections and rulings; motions in limine; offers of proof.
- **Verdict and judgment:** Verdict form answers, damages by category, judgment text.
- **Grounds you believe exist:** Insufficient evidence on an element, legal error in instructions or evidence rulings, verdict against the weight of the evidence, excessive or inadequate damages, inconsistent verdict, juror or attorney misconduct, newly discovered evidence.
- **Appellate plans:** Whether an appeal is likely and by whom.

## Method

**Ground rules:** Do not state post-trial or appellate deadlines from memory; compute from the supplied rules and docket date and mark `[VERIFY]`. Many of these deadlines cannot be extended by the court `[VERIFY: FRCP 6(b)(2) or analog]` — treat them as fixed. Do not invent case law on standards, remittitur, or waiver; use `[CITE: …]` / `[NEED HOLDING: …]`. Record cites use `[R. __]` placeholders until supplied.

1. **Deadline gate (fail-fast).** From the entry-of-judgment date, list each motion's deadline, whether it is extendable, and the effect of a timely motion on the time to appeal `[VERIFY: FRAP 4(a)(4) or analog]`. Put the earliest deadline at the top of the output.
2. **Preservation check.** For each candidate ground, find where it was preserved: the renewed JMOL can raise only grounds stated in the pre-verdict motion `[VERIFY]`; instruction errors require a timely, specific objection `[VERIFY]`; evidentiary errors require an objection or offer of proof. Mark each ground Preserved / Partially / Not preserved (and whether plain-error review is available `[VERIFY]`).
3. **Route each ground to its motion and standard.**
   - Legally insufficient evidence on an element → renewed JMOL (no reasonable jury standard; evidence viewed in the non-movant's favor).
   - Verdict against the clear weight of the evidence, prejudicial error, misconduct, excessive/inadequate damages → new trial (court's broader discretion `[CITE]`).
   - Excessive damages → remittitur as an alternative to a new trial (the plaintiff must be offered the choice of a new trial `[VERIFY]`); additur is generally unavailable in federal court `[VERIFY]` but may exist under state law.
   - Errors in the judgment's terms, interest, or relief → motion to alter or amend.
   - Bench trial findings → motion to amend findings, often combined with alter/amend.
   - Clerical errors → the rule for correcting clerical mistakes; newly discovered evidence, fraud, or other grounds → relief-from-judgment rule, with its own timing `[VERIFY]`.
4. **Prioritize grounds.** Rank by preservation status, standard of review, and likely impact. Lead with the strongest; drop grounds that dilute credibility.
5. **Plead alternatives and conditional rulings.** Combine renewed JMOL with a new-trial motion in the alternative, and ask the court to rule conditionally on the new-trial motion if it grants JMOL `[VERIFY: FRCP 50(c) or analog]`.
6. **Draft each motion.** For each ground: the record facts (with `[R. __]` cites), the element or error, the standard, and why the standard is met. For damages: show the calculation the evidence supports and the excess.
7. **Stress-test from the other side.** Write the non-movant's best response to each ground (substantial evidence exists; objection not specific; harmless error) and revise.
8. **If you are the non-movant,** convert steps 2–7 into oppositions and add a waiver/forfeiture analysis for each ground the movant raises.

## Output Format

```markdown
# Post-Trial Motion Set — {Caption} — Judgment entered {date}

## 1. Deadline Gate
| Motion | Rule | Deadline (computed) [VERIFY] | Extendable? | Effect on appeal time [VERIFY] |

## 2. Preservation Map
| Ground | Where preserved [R. __] | Status (P / Partial / Not) | Motion | Standard | Rank |

## 3. Renewed Motion for Judgment as a Matter of Law
I. Grounds (limited to pre-verdict grounds)  II. Standard [CITE]  III. Argument by element  IV. Conditional new-trial ruling requested

## 4. Motion for New Trial (in the alternative)
I. Grounds  II. Standard [CITE]  III. Argument  IV. Remittitur (alternative) — calculation

## 5. Motion to Alter or Amend Judgment / Amend Findings (if applicable)
## 6. Proposed Orders
## 7. Opposition Stress Test
| Ground | Non-movant's best response | Our reply |
## 8. Verification Items
```

## Verification

- [ ] Jurisdiction lock: every rule and deadline tied to the stated court; federal and state rules not mixed.
- [ ] Citation discipline: no invented authority on standards, remittitur, or preservation; record cites are `[R. __]` until supplied.
- [ ] Scope discipline: post-trial motions only; appellate issue selection deferred.
- [ ] Deadline gate computed from the docketed entry date and placed first.
- [ ] Renewed JMOL grounds match the pre-verdict motion; unmatched grounds rerouted to the new-trial motion.
- [ ] Each ground routed to the correct motion and standard.
- [ ] Remittitur request preserves the plaintiff's option of a new trial.
- [ ] Conditional ruling on the new-trial motion requested where JMOL is sought.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Raising a JMOL ground not made before the verdict | Preservation map; route to new-trial motion or drop |
| Stating a post-trial deadline from memory | Compute from supplied rule and docket date; mark `[VERIFY]` |
| Using the JMOL standard for a weight-of-evidence argument | Route each ground to its own standard |
| Asking for a reduced judgment without a new-trial option | Remittitur must offer the choice `[VERIFY]` |
| Including every conceivable error | Rank and drop weak grounds |
| Forgetting the effect on the appellate clock | Deadline gate includes appeal-time effects |

## Example

**Input sketch:** Federal jury awarded plaintiff Aldous Orchards (fictional) $3.1M against defendant Selby Irrigation on negligence: $600K property damage, $2.5M lost future profits. Selby's pre-verdict JMOL motion argued only lack of causation evidence. Selby objected to the lost-profits instruction as lacking a reasonable-certainty requirement. Judgment entered 2026-09-15.

**Output (abridged):**

> **Deadline gate.** Renewed JMOL and new-trial motion: deadline computed from 2026-09-15 under the supplied rule `[VERIFY: FRCP 50(b), 59(b)]` — not extendable `[VERIFY: FRCP 6(b)(2)]`. Timely motion resets appeal time `[VERIFY: FRAP 4(a)(4)(A)]`.
>
> **Preservation map.** Causation insufficiency — preserved in pre-verdict JMOL [R. __] — renewed JMOL — rank 2. Lost-profits speculative — *not* in pre-verdict JMOL — cannot support renewed JMOL → route to new trial / remittitur — rank 1. Instruction error (reasonable certainty) — objection preserved [R. __] — new trial — rank 3.
>
> **Remittitur (excerpt).** The only lost-profits evidence was the owner's projection of five years of 40% growth, without historical data beyond one season [R. __]. The maximum award the evidence supports is `[NEED: calculation from trial exhibits]`. Selby asks the Court to order a new trial on damages unless Aldous accepts a remittitur to that amount.
