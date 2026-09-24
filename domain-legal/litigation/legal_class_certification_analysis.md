---
title: "Class Certification Analysis — Rule 23 Element-by-Element with Evidence and Damages-Model Fit"
category: legal/litigation
description: "Attorney-facing analysis for moving for or opposing class certification under Rule 23 or a state analogue — class-definition audit, each Rule 23(a) and (b) requirement tested against the evidentiary record, damages-model fit to the liability theory, standing and arbitration-waiver problems, and fallback options — distinct from a general case-strategy assessment and from settlement valuation."
techniques:
  - DT-05
  - RT-05
  - QA-02
  - QA-05
  - DS-33
difficulty: advanced
tags:
  - legal
  - litigation
  - class-action
  - rule-23
  - class-certification
  - many-people-same-harm
  - opposing-class-action
updated: "2026-09-24"
related_prompts:
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

# Class Certification Analysis — Rule 23 Element-by-Element with Evidence and Damages-Model Fit

> **Scope guard — attorney-facing only.** This prompt is for counsel for a putative class or for a defendant, preparing or opposing a certification motion. It does not evaluate whether any individual should join, opt out of, or object to a class. A potential class member without counsel should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Do not invent case names, holdings, circuit positions, rule text, or record citations. Circuit law on several certification questions is split or unsettled — state the question and mark it `[VERIFY: circuit position]`. Use `[CITE: …]`, `[NEED PIN: …]`, `[NEED HOLDING: …]`, and `[REC: record cite needed]`.

## When to Use

- Plaintiffs' counsel is building the certification motion and needs to see which requirement is weakest before expert reports are finalized.
- Defense counsel is preparing the opposition and needs the strongest individualized-issue and damages-model attacks.
- Either side needs an early read, before class discovery closes, on what evidence certification will turn on.

**Not this prompt if:**
- You need the whole-case strategy (merits, forum, budget) — use `domain-legal/litigation/legal_case_strategy_assessment.md`; feed its certification question here.
- You are valuing a class settlement — use `domain-legal/litigation/legal_settlement_value_range_analysis.md` after this analysis sets certification risk.
- The certification question depends on an unresolved circuit split you have not mapped — build the map with `domain-legal/research/legal_jurisdiction_split_analysis.md` first.

## Inputs

- **Jurisdiction (required):** Court (federal district and circuit, or state court and its class-action rule); whether the case is in federal court under a removal or original-jurisdiction statute.
- **Posture:** Moving or opposing; certification deadline and briefing schedule; state of class discovery.
- **Proposed class definition(s):** Verbatim, including subclasses and class period.
- **Claims and elements:** Each cause of action and its elements under the governing law (which state's law, if choice-of-law is contested).
- **Evidence:** Named plaintiffs' facts and deposition excerpts; common documents (form contracts, uniform policies, standardized disclosures); data showing class size and membership; expert reports (liability and damages) and any Daubert challenges.
- **Defenses:** Arbitration agreements and class waivers; releases; individualized defenses (reliance, consent, causation, limitations, offset).
- **Relief sought:** Injunctive / declaratory, monetary, or both.

## Method

1. **Jurisdiction lock.** Identify the governing class rule, the circuit's rigorous-analysis and evidentiary standards at certification (including whether expert evidence must satisfy admissibility review at this stage) `[VERIFY: circuit position]`, and any state-rule differences.
2. **Class-definition audit.** Test for fail-safe definitions (membership turns on winning the merits), overbreadth (sweeps in people with no injury or no claim), vagueness, and — where the circuit requires it — administrative feasibility of identifying members `[VERIFY: circuit's ascertainability standard]`. Propose corrected definitions.
3. **Rule 23(a), one requirement at a time.** Numerosity (evidence of size, not assumption); commonality (identify at least one question whose answer, generated classwide, drives resolution — not just shared questions); typicality (do named plaintiffs' claims arise from the same conduct and theory; any unique defenses?); adequacy (conflicts within the class, named plaintiffs' knowledge and involvement, class counsel's qualifications).
4. **Rule 23(b) category.** For (b)(2): is the relief indivisible, and is any monetary relief individualized or, at most, incidental to the injunctive or declaratory relief `[VERIFY: circuit treatment]`? For (b)(3): list each element of each claim and mark it common proof / individual proof / mixed, with the evidence. Then weigh — predominance is qualitative, not a head count. For superiority: manageability, other pending litigation, members' interest in individual control.
5. **Damages-model fit.** Does the damages model measure only damages attributable to the liability theory being certified? Can it be applied classwide with common evidence? Identify individual damages calculations and whether they defeat predominance under the circuit's approach `[VERIFY]`.
6. **Standing and uninjured members.** Assess whether the class includes members without concrete injury and how the circuit treats that at certification versus later `[VERIFY: circuit position]`.
7. **Arbitration and waivers.** Identify members bound by arbitration agreements or class waivers; propose carve-outs or subclasses, or (for defendants) the motion sequencing to raise them.
8. **Fallbacks.** Subclasses, narrowed class period, issue classes on particular questions `[VERIFY: circuit's approach]`, or a (b)(2)-only class.
9. **Interlocutory review.** Note the availability and timing of a petition for permission to appeal the certification order `[VERIFY: rule and deadline]`.

## Output Format

```markdown
# Class Certification Analysis — {Case} — {Court}
**Posture:** {moving | opposing}  |  **Certification motion due:** {date}  |  **Governing rule:** {…}  |  **Attorney Work Product**

## 1. Executive Read (likely outcome and the one requirement that decides it)
## 2. Class Definition Audit
| Issue | Present? | Fix / attack |
## 3. Rule 23(a) Matrix
| Requirement | Evidence [REC] | Strongest argument for | Strongest argument against | Rating |
## 4. Rule 23(b) Analysis
### Element-by-element proof table
| Claim | Element | Common / individual / mixed | Evidence [REC] |
### Predominance weighing
### Superiority / (b)(2) fit
## 5. Damages-Model Fit
## 6. Standing, Arbitration, and Waiver Issues
## 7. Fallback Options
## 8. Interlocutory Review Posture [VERIFY deadline]
## 9. Evidence Still Needed Before Filing
## 10. Verification Items
```

## Verification

- [ ] Jurisdiction lock: court, circuit, and governing class rule stated; each circuit-dependent standard marked `[VERIFY]`.
- [ ] Citation discipline: every case and holding supplied or marked `[CITE]` / `[NEED HOLDING]`; every fact carries `[REC]` or a supplied cite.
- [ ] Scope discipline: analysis limited to certification; merits addressed only where they overlap with a Rule 23 requirement.
- [ ] Commonality identifies a question with a classwide answer, not merely a shared question.
- [ ] Predominance analysis is element-by-element for every claim, not a summary judgment on "common issues."
- [ ] Damages model tested for fit to the specific liability theory.
- [ ] Both sides' strongest arguments appear for every requirement, regardless of which side the user represents.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Listing shared questions as commonality | Require a common *answer* that drives resolution for the whole class |
| Counting common issues to find predominance | Weigh qualitatively, element by element, including individualized defenses |
| Ignoring the damages model | Test whether it measures only the certified theory's damages on classwide proof |
| Assuming uniform circuit law | Ascertainability, uninjured members, and expert admissibility at certification vary — `[VERIFY]` |
| Treating numerosity as automatic | Cite evidence of size and membership, not an estimate |
| Writing only the client's side | Present the opponent's best argument for every requirement so the brief meets it |

## Example

**Input (abridged):** Federal district court. Fictional plaintiffs allege Lakeside Fitness Clubs charged a "facility enhancement fee" not disclosed in its standard membership contract. Proposed class: "All members charged the fee who were harmed by its non-disclosure." Some members signed a later contract version with an arbitration clause. Damages expert: refund of all fees charged.

**Output (excerpt):**

> **Definition audit — fail-safe.** "Who were harmed" makes membership depend on liability. Fix: "All persons who paid the facility enhancement fee under Contract Versions A or B between {dates}."
>
> **Commonality — strong for plaintiffs.** Whether the standard contract disclosed the fee is answerable from the contract itself, once, for everyone on Versions A–B `[REC: contract exhibits]`.
>
> **Predominance — contested.** If the claim requires individual reliance under the governing state law `[VERIFY: element]`, defense will argue members who saw the fee on the sign-up screen did not rely on the contract. Plaintiffs' answer: reliance is presumed from the uniform written contract `[VERIFY: presumption under governing law]`; the defense must show the screen variation mattered `[NEED: screen-version data]`.
>
> **Arbitration.** Version C members signed an arbitration clause — carve them out or propose a subclass; defendants should raise the clause before or with the opposition `[VERIFY: circuit timing on waiver of the right to arbitrate]`.
