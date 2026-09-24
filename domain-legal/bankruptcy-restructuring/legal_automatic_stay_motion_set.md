---
title: "Automatic Stay Relief Motion Set (Motion and Opposition)"
category: legal/bankruptcy-restructuring
description: "Draft a motion for relief from the automatic stay or the debtor's / trustee's opposition — for cause (including lack of adequate protection), for lack of equity where the property is not necessary to an effective reorganization, or on other statutory grounds — with a burden-of-proof map, valuation evidence plan, adequate-protection alternatives, and proposed order, all without inventing hearing deadlines or case law."
techniques:
  - ST-02
  - ST-03
  - RT-05
  - QA-02
difficulty: advanced
tags:
  - legal
  - bankruptcy
  - automatic-stay
  - relief-from-stay
  - adequate-protection
  - motion-practice
  - valuation
updated: "2026-09-24"
reasoning:
  styles: [adversarial, evidential, procedural]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: structured
  user_role: [lawyer]
  mode: [document, respond]
related_prompts:
  - domain-legal/bankruptcy-restructuring/legal_proof_of_claim_drafter.md
  - domain-legal/bankruptcy-restructuring/legal_chapter_11_plan_analysis.md
  - domain-legal/litigation/legal_motion_for_summary_judgment.md
  - domain-legal/research/legal_research_memo_irac.md
---

# Automatic Stay Relief Motion Set (Motion and Opposition)

**Objective:** Produce a filable motion for relief from the automatic stay (creditor side) or an opposition (debtor / trustee side), built around the statutory grounds actually available on the facts, a burden-of-proof map showing which party must prove which element, a valuation and evidence plan, and — for the debtor — concrete adequate-protection offers that defeat the motion or narrow it to conditional relief.

**When to use:**
- A secured creditor, lessor, or litigation plaintiff needs to proceed against property or in a non-bankruptcy forum.
- Debtor's counsel or a trustee must oppose or negotiate conditional relief.
- Evaluating whether a prior-filing history means the stay never arose or has terminated (and a comfort order is needed instead).

**Distinct from:**
- `domain-legal/litigation/` motion prompts — civil-procedure standards; stay relief proceeds under the Code's own grounds, burdens, and expedited timeline.
- `domain-legal/personal-self-advocacy/housing-landlord-tenant/` — tenant self-help; this is counsel-side motion practice.
- Motions to extend or impose the stay after prior dismissed cases — noted as a branch, not drafted in full here.

**Audience:** Bankruptcy litigators for creditors, debtors, and trustees.

---

## Your Input

- **Side:** [Movant / Opponent]
- **Case:** [Debtor, case no., district, chapter, petition date; prior filings within the relevant look-back]
- **Property or proceeding at issue:** [Real property, vehicle, equipment, lease, pending lawsuit, licence]
- **Claim and collateral facts:** [Claim amount, lien priority and perfection, other liens, collateral value evidence (appraisals, BPOs), insurance status, taxes]
- **Payment history:** [Pre- and post-petition payments missed or made]
- **Reorganization prospects:** [Plan filed? Exclusivity status? Projections? Is the property needed?]
- **Grounds you want to assert or anticipate:** [Cause / lack of adequate protection / no equity + not necessary / single-asset real estate / scheme to hinder / other]
- **Local rules and procedures:** [Notice periods, preliminary vs. final hearing practice, required forms or worksheets — paste; do not assume]
- **Controlling authority supplied:** [Circuit cases on cause, equity cushion, "effective reorganization" standard]

---

## Constraints

### Must
- Identify each **statutory ground** separately (cause including lack of adequate protection; no equity and not necessary for effective reorganization; special single-asset real estate ground; scheme-based in-rem relief) and brief them in separate sections `[VERIFY: §362(d)(1)–(4)]`.
- Build a **burden map**: the movant bears the burden on the debtor's equity; the party opposing relief bears the burden on other issues `[VERIFY: §362(g)]`. Show which evidence carries each burden.
- Treat **valuation** as the case: specify the valuation standard argued, the date, and the evidence (appraisal, testimony, comparables); identify the equity cushion under each side's number.
- For the opposition, propose **adequate protection** alternatives (periodic payments, replacement liens, insurance, cure schedule) and a conditional-relief fallback (drop-dead / default provisions).
- Flag the **expedited hearing timeline** and automatic-termination risk if the hearing is not held timely `[VERIFY: §362(e) and local procedure]`.
- Include a **proposed order** with waiver or retention of any stay-of-order period `[VERIFY: Rule 4001(a)(3)]`.

### Must Not
- Invent notice periods, hearing deadlines, or local forms; pull from the pasted local rules or mark `[VERIFY]`.
- Argue "cause" as a catch-all without identifying the specific cause (missed post-petition payments, lapsed insurance, bad faith filing, litigation more efficiently resolved elsewhere).
- Conflate "no equity" with "not necessary for an effective reorganization"; both prongs are required for that ground.
- Rely on valuation figures not in the evidence; use `[NEED: appraisal]`.
- Cite cases not supplied; use `[CITE: …]` and `[NEED HOLDING: …]`.

---

## Instructions

1. **Check the stay's existence and scope.** Did it arise? Is it limited or terminated by prior-filing history? Is the property estate property? If relief is unnecessary, draft a comfort-order request instead.
2. **Select grounds** based on the facts; drop grounds without factual support.
3. **Build the burden map** and the evidence list per element.
4. **Valuation section:** the competing values, the equity cushion under each, and why the movant's (or opponent's) valuation is more reliable.
5. **Draft the motion or opposition** with separate argument sections per ground.
6. **Adequate protection / conditional relief:** movant — why nothing short of relief protects it; opponent — concrete offers with numbers from the inputs.
7. **Prepare declarations list** (custodian of payment history, appraiser) and exhibits.
8. **Proposed order** with conditional terms if negotiating.
9. **Hearing plan:** preliminary vs. final, witnesses, time estimate, timing risk.

---

## Output Format

```markdown
{COURT CAPTION — Bankr. {district}}
{MOVANT}'S MOTION FOR RELIEF FROM THE AUTOMATIC STAY   |   or   |   {DEBTOR}'S OPPOSITION TO …

## Preliminary Statement
## Jurisdiction and Procedural Posture   ({notice period and hearing per local rule [VERIFY]})
## Background   (claim, lien, collateral, payment history)
## Burden Map
| Issue | Party with burden | Evidence |
## Argument
I. Cause Exists (Including Lack of Adequate Protection)   [VERIFY: §362(d)(1)]
II. Debtor Lacks Equity and the Property Is Not Necessary to an Effective Reorganization   [VERIFY: §362(d)(2)]
III. {Other ground, if any}
## Adequate Protection / Conditional Relief
## Conclusion and Relief Requested
## Declarations and Exhibits List
## Proposed Order   (incl. stay-of-order waiver or retention [VERIFY])
## Hearing Plan and Timing Risks
```

---

## Worked Example

**Input (abridged):** Side: opponent (Chapter 11 debtor). Lender holds first mortgage on a mixed-use building; claim $2.35M; lender appraisal $2.2M; debtor appraisal $2.7M. Debtor missed four pre-petition payments; has paid post-petition interest-only since filing; insurance current. Plan filing expected within 60 days; building produces 70% of debtor's revenue. Lender moves on cause and no-equity grounds.

**Output (excerpt):**

> **Burden map.** Equity: lender bears the burden — its own appraisal ($2.2M vs. $2.35M claim) shows no equity, so the debtor must rebut with the $2.7M appraisal and attack the lender's comparables. Necessity for an effective reorganization and adequate protection: debtor bears the burden.
>
> **II. No-equity ground fails on the second prong.** Even if the court accepts the lender's value, the building generates 70% of revenue and a plan is imminent; the debtor must show a reorganization that is reasonably in prospect, not merely conceivable `[NEED HOLDING: controlling circuit articulation]`.
>
> **Adequate protection offer:** continue monthly payments of $11,800 (equal to contract interest), maintain insurance with lender as loss payee, and a replacement lien on rents. **Conditional-relief fallback:** if any payment is more than 10 days late after written notice, lender may file a certification of default and obtain relief without further hearing — proposed as a drop-dead term in the order.
>
> **Timing risk:** confirm whether local practice treats the first hearing as preliminary and whether the stay could terminate by operation of law if no hearing concludes within the statutory period `[VERIFY: §362(e) + local rule]`.

---

## Verification

- [ ] Jurisdiction lock: district and circuit stated; local rules taken from pasted text or marked `[VERIFY]`.
- [ ] Stay existence and scope checked before arguing relief.
- [ ] Each ground argued separately with its own elements.
- [ ] Burden map assigns each issue to the correct party.
- [ ] Valuation evidence identified; equity cushion computed under both values.
- [ ] Opposition includes numeric adequate-protection offers and a conditional-relief fallback.
- [ ] Proposed order addresses the stay-of-order period.
- [ ] Citation discipline: no invented cases, holdings, pinpoints, or deadlines.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Moving for relief when the stay never arose or has terminated | Check prior filings and property of the estate first; seek a comfort order if appropriate |
| Treating "cause" as undefined | Name the specific cause and its evidence |
| Arguing no-equity alone | That ground needs both no equity and not necessary for an effective reorganization |
| Putting the equity burden on the debtor | The movant carries equity; the opponent carries the rest |
| Adequate-protection offers without numbers | State amounts, frequency, and source of funds from the inputs |
| Stating hearing deadlines from memory | Use pasted local rules or `[VERIFY]`; timing failures can terminate the stay |
| Ignoring the order's automatic stay period | Address waiver or retention explicitly in the proposed order |
