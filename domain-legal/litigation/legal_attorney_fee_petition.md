---
title: "Attorney Fee Petition (Lodestar)"
category: legal/litigation
description: "Draft a post-judgment or post-ruling motion for attorney's fees and non-taxable expenses — entitlement basis (statute, contract, rule, or order), prevailing-party showing, lodestar built from audited time entries and rate evidence, billing-judgment reductions, and any adjustment request — distinct from the litigation budget estimator (forward-looking) and the legal-spend anomaly analyzer (client-side invoice review)."
techniques:
  - NE-11
  - RT-05
  - NE-23
  - QA-01
difficulty: advanced
tags:
  - legal
  - litigation
  - attorney-fees
  - lodestar
  - fee-shifting
  - make-the-other-side-pay-legal-fees
  - we-won-can-we-get-fees
updated: "2026-09-24"
related_prompts:
  - domain-legal/litigation/legal_litigation_budget_phase_estimator.md
  - domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md
  - domain-legal/discovery/legal_motion_to_compel_drafter.md
---

# Attorney Fee Petition (Lodestar)

**Objective:** Produce a fee motion that survives the line-by-line attack it will receive: a clear entitlement basis, a prevailing-party showing tied to the actual result, time entries audited and cut *before* filing, rates supported by evidence from the relevant market, a lodestar computed transparently, and any enhancement or reduction argument grounded in facts the governing standard recognizes.

> **Scope guard — attorney-facing.** For counsel seeking fees for a client under a fee-shifting statute, contract, rule, or court order. It is not a client billing dispute tool. A self-represented party asking about fees should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- Judgment or a dispositive ruling has been entered and a statute, contract, rule, or order authorizes fee-shifting.
- A court has granted a discovery or sanctions motion and ordered the other side to pay fees in an amount to be proved.
- A settlement leaves fees to the court.

**Not this prompt if:**
- You are forecasting fees for a budget — use `domain-legal/litigation/legal_litigation_budget_phase_estimator.md`.
- You are reviewing outside-counsel bills as the client — use `domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md`.
- You need only a short fee declaration inside a discovery motion — the fee section of `domain-legal/discovery/legal_motion_to_compel_drafter.md` covers it.
- The fee request is a percentage of a common fund in a class settlement — different method; flag and stop.

## Inputs

- **Jurisdiction (required):** Court, governing law of the fee basis, and the procedural rule for fee motions (e.g., FRCP 54(d)(2) or state analog) including deadline, required content, and any local rule on conferral or fee-motion format `[VERIFY]`.
- **Entitlement basis:** Statute, contract clause (quote it), rule, or order; any prerequisites (prevailing party definition, offer-of-judgment effects, notice requirements).
- **Result obtained:** Judgment, relief on each claim, claims lost or abandoned.
- **Time records:** Exported entries (date, timekeeper, hours, narrative, task code) for the recoverable period.
- **Timekeepers:** Name, role, years of experience, standard rate, rate actually charged (if any), and any rate evidence (surveys, declarations of other practitioners, prior awards) — as supplied.
- **Expenses:** Non-taxable expenses sought, with receipts; taxable costs are handled separately `[VERIFY: 28 U.S.C. § 1920 or analog]`.
- **Fee arrangement:** Hourly, contingency, pro bono, or hybrid.

## Method

**Ground rules:** Do not invent case names, rate awards, multiplier standards, or market rates; authority is supplied or `[CITE: …]`, and market-rate figures come only from supplied evidence or `[NEED: rate evidence]`. The fee-motion deadline is taken from the supplied rule or order and marked `[VERIFY]`. Draft for the stated forum and fee basis only.

1. **Deadline and prerequisite gate.** Compute the filing deadline from the supplied rule/order; list prerequisites (conferral, statement of amount, disclosure of fee agreement if the court orders it `[VERIFY]`). Flag if the deadline has passed or is imminent.
2. **Entitlement.** Quote the basis; show each element (prevailing party, claim within the fee provision, any required finding). If only some claims carry fees, identify the fee-bearing claims.
3. **Result analysis.** Compare relief sought to relief obtained. Identify unsuccessful claims and whether they share a common core of facts or related legal theories with successful ones `[CITE: governing standard]`; plan reductions where they do not.
4. **Audit the time before the other side does.** Flag and cut or fix: block-billed entries, vague narratives, clerical tasks billed at professional rates, duplicate attendance, excessive intra-office conferences, time on unsuccessful unrelated claims, work before the fee period, and time on the fee motion itself (recoverable only if the basis permits `[VERIFY]`). Record every cut in a billing-judgment schedule — the voluntary reductions are an argument in themselves.
5. **Rates.** For each timekeeper, the requested rate, the relevant market (usually the forum `[VERIFY]`), and the evidence supporting it. Do not supply a market rate from general knowledge.
6. **Compute the lodestar.** Reasonable hours × reasonable rate per timekeeper, summed; show the arithmetic in a table; reconcile totals.
7. **Adjustments.** Argue an enhancement only if the governing standard recognizes the factor and the facts support it; otherwise say none is sought. Address any expected reduction arguments (limited success, overstaffing) pre-emptively.
8. **Assemble the package.** Motion, memorandum, lead-counsel declaration (entitlement facts, staffing, billing judgment), timekeeper declarations or rate-evidence declarations, the time-entry exhibit, the billing-judgment schedule, expense exhibit, proposed order.

## Output Format

```markdown
# Fee Motion Package — {Caption}

## 1. Deadline and Prerequisite Gate
| Item | Requirement | Source [VERIFY] | Status |

## 2. Entitlement and Result
- Basis (quoted): {…}
- Prevailing-party showing: {…}
| Claim | Fee-bearing? | Result | Related to successful claims? | Treatment |

## 3. Billing-Judgment Schedule
| Entry ID | Timekeeper | Hours | Issue (block/vague/clerical/duplicate/unrelated) | Hours cut | Revised |

## 4. Rate Support
| Timekeeper | Role / years | Requested rate | Evidence | Gap |

## 5. Lodestar Computation
| Timekeeper | Reasonable hours | Rate | Subtotal |
| **Total** | | | {…} |

## 6. Motion and Memorandum (draft)
I. Relief Requested  II. Entitlement  III. Reasonable Hours  IV. Reasonable Rates
V. Lodestar  VI. {Adjustment — only if sought}  VII. Non-Taxable Expenses  VIII. Conclusion
## 7. Declarations (outline)  ## 8. [Proposed] Order
## 9. Anticipated Objections and Responses
## 10. Verification Items
```

## Verification

- [ ] Jurisdiction lock: fee basis, fee-motion rule, deadline, and local requirements tied to the stated forum.
- [ ] Citation discipline: no invented authority, rate awards, or multiplier standards.
- [ ] Scope discipline: fees and non-taxable expenses only; taxable costs routed to the cost bill.
- [ ] Deadline gate completed and stated at the top.
- [ ] Every time entry either passes audit or appears in the billing-judgment schedule.
- [ ] Rates supported only by supplied evidence; gaps marked `[NEED]`.
- [ ] Lodestar arithmetic reconciles across tables.
- [ ] Limited-success issues addressed before the opposition raises them.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Filing raw billing records | Audit first; show voluntary cuts in the billing-judgment schedule |
| Supplying "prevailing market rates" from memory | Rates only from supplied evidence or `[NEED: rate evidence]` |
| Seeking fees for claims outside the fee provision | Claim-by-claim entitlement table |
| Requesting a multiplier by default | Seek an adjustment only when the standard and facts support it |
| Mixing taxable costs into the fee motion | Separate cost bill `[VERIFY]` |
| Missing the short fee-motion deadline | Deadline gate is step 1 |

## Example

**Input sketch:** Federal court; plaintiff tenant association (fictional) prevailed on a fair-housing claim with a fee-shifting provision; lost a related state-law contract claim. Records: 612 hours across a partner, an associate, and a paralegal. Rate evidence: two declarations from local fair-housing practitioners.

**Output (abridged):**

> **Gate.** Deadline per supplied rule and judgment date: `[VERIFY: FRCP 54(d)(2)(B) and any order]`. Local rule requires conferral on fees before filing `[VERIFY]` — not yet done → schedule it.
>
> **Entitlement table.** Contract claim — not fee-bearing — lost — shares the same facts about the habitability complaints → treat as related; no separate reduction proposed, but 14.2 hours of research unique to the contract theory cut.
>
> **Billing-judgment schedule (excerpt).** E-0412, paralegal, 3.0 h, "organize files, calendar" — clerical — cut 3.0. E-0588, partner and associate both attended a status conference — duplicate — cut associate 1.5.
>
> **Lodestar.** After 41.7 hours of voluntary cuts: partner 188.0 h × requested rate `[NEED: rate evidence supports]`; associate 301.3 h × rate; paralegal 81.0 h × rate. Arithmetic shown per row; no enhancement sought.
