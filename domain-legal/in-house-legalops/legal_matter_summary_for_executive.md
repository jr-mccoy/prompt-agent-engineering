---
title: "Executive Matter Summary (One-Page)"
category: legal/in-house-legalops
description: "Produce a one-page executive summary of a legal matter for a non-lawyer business audience: status, exposure, probability, key risks, recent developments, decisions needed with deadlines, cost-to-date and budget remaining — framed for approve/decline/defer decisions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - in-house
  - legal-ops
  - executive-communication
  - matter-management
updated: "2026-05-11"
related_prompts:
  - domain-legal/in-house-legalops/legal_board_legal_update_brief.md
  - domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md
  - domain-legal/litigation/legal_litigation_budget_phase_estimator.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
---

**Purpose:** Produce a single-page executive summary of an active legal matter for a non-lawyer business audience (CEO, CFO, BU GM, GC's executive sponsor). The reader has 90 seconds. The output must surface the exposure, the decision needed, and the deadline — without internal counsel-speak.

**When to use:** Routine matter reporting to executives, escalation packets, settlement-authority requests, prep for an executive sponsor's meeting where the matter will be discussed, monthly portfolio reviews.

---

## Your Input

- **Matter name and internal ID:** [As tracked in the matter-management system]
- **Matter type:** [Litigation / regulatory investigation / pre-litigation dispute / transaction / employment / IP / other]
- **Counterparty / agency:** [Name; or "to be redacted"]
- **Forum / jurisdiction:** [Court, agency, arbitral body, or "pre-litigation"]
- **Status / procedural posture:** [Where the matter sits today]
- **Exposure estimate:** [Single-point or range, in dollars; or "non-monetary" with description]
- **Probability bands:** [Outside-counsel or internal estimate; e.g., reasonably possible / probable / remote per ASC 450 framing, or %-band if available]
- **Recent developments (last 30–60 days):** [Material events]
- **Decisions needed:** [Specific asks — settlement authority, budget approval, witness availability, document hold scope, business decision that affects the matter]
- **Deadline(s) for each decision:** [Date and what happens if missed]
- **Cost-to-date and budget remaining:** [Outside counsel fees billed YTD / matter-life, accrued, budget remaining, expected burn to next milestone]
- **Outside counsel of record:** [Firm + lead partner]
- **Privilege posture:** [Whether the summary is for inside-the-privilege audience only, or whether redactions are needed for broader distribution]

---

## Constraints

**Must:**
- Fit on **one page** (target 350–450 words of body content; bullets and short sentences).
- Open with an **attorney-client privilege caption** appropriate to the audience (e.g., "PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT — Prepared at the request of [executive]").
- Lead with the **decision needed** and the **deadline** — not the procedural history.
- Express exposure as a **dollar range with a probability band**, not a single point estimate, unless the user supplied a single point.
- Use **plain business English**: no Latin, no Rule numbers, no "fourth amended scheduling order" without a translation.
- Frame the recommendation as **approve / decline / defer**, with the consequence of each.
- Distinguish **what we know** from **what we estimate** from **what counterparty has asserted**.

**Must Not:**
- Invent case names, docket numbers, judges, regulators, dollar amounts, settlement offers, budget figures, or counsel names. If the user did not supply a field, write "[not supplied]" or omit.
- Exceed one page. If content does not fit, the summary is wrong — cut, do not shrink type.
- Use internal counsel-speak ("12(b)(6)", "summary judgment", "Markman", "Daubert", "motion in limine") without a one-clause translation.
- Hedge into uselessness ("could be material or immaterial depending on outcome"). Commit to a range.
- Embed legal advice the executive cannot act on without counsel. The summary supports a decision; it is not the legal opinion.
- Use boilerplate "consult counsel" disclaimers. The reader IS consulting counsel by reading this.

---

## Instructions

1. **Privilege caption.** Top of page. Tailor to whether the recipient is inside the privileged circle and whether the document will be shared further.
2. **Headline (one line).** Matter name, matter type, current status, headline exposure range. Example: "Acme v. Co. — commercial dispute — fact discovery — exposure $4M–$9M (reasonably possible)."
3. **Decision needed and deadline.** Above the fold. Bullet the asks; flag the deadline; state the consequence of missing it.
4. **Exposure.** Range with a probability band; identify what drives the upper and lower ends; flag whether an ASC 450 accrual or disclosure is in scope this quarter.
5. **Key risks.** 3–5 bullets. Each is one sentence. Each ends with a "so what" — why the executive should care.
6. **Recent developments.** 3–5 bullets covering the last 30–60 days. Material only. Procedural minutiae are out.
7. **Cost posture.** Spent to date, budget remaining, expected burn to next milestone, whether matter is on/over/under plan.
8. **Recommendation.** Approve / decline / defer. State the implication of each path.
9. **Owner & next checkpoint.** Internal owner (often the responsible attorney), next status date.
10. **Self-check.** Read aloud. If a smart non-lawyer cannot make the requested decision after 90 seconds, rewrite.

---

## Output Format

```markdown
PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT
Prepared at the request of {Executive} by {Inside Counsel}
{Date}

## {Matter Name} — Executive Summary

**Type / Status / Exposure:** {Matter type} | {Procedural posture} | {Exposure range} ({probability band})

### Decision Needed by {Deadline}
- {Ask 1 — e.g., "Approve settlement authority up to $X"}
- {Ask 2 — e.g., "Confirm CFO availability for deposition window of [dates]"}
- **Consequence if missed:** {What happens — e.g., trial date, regulatory deadline, business disruption}

### Exposure
- **Range:** {$ low – $ high}
- **Drivers (upper end):** {1–2 drivers}
- **Drivers (lower end):** {1–2 drivers}
- **Accounting flag:** {ASC 450 — probable / reasonably possible / remote; accrual status; disclosure status}

### Key Risks (so-what framing)
- {Risk 1 — so {business consequence}}
- {Risk 2 — so {business consequence}}
- {Risk 3 — so {business consequence}}

### Recent Developments (last {30–60} days)
- {Event 1}
- {Event 2}
- {Event 3}

### Cost Posture
- **Spent to date:** ${amount}
- **Budget remaining:** ${amount}
- **Expected burn to {next milestone}:** ${amount}
- **Status vs plan:** {On / Over / Under} — {one-line reason}

### Recommendation
**{Approve / Decline / Defer}** — {one-sentence rationale}.
- If approved: {implication}
- If declined: {implication}
- If deferred: {implication and re-decision trigger}

### Owner & Next Checkpoint
{Inside-counsel owner} | Next update: {date / trigger}
```

---

## Verification

- [ ] Document fits on one page at normal print settings.
- [ ] Privilege caption present and tailored to audience.
- [ ] Decision needed and deadline are above the fold and unambiguous.
- [ ] Exposure expressed as a range with a probability band (or explicitly stated as non-monetary).
- [ ] ASC 450 posture flagged if material.
- [ ] No invented case names, dockets, dollar amounts, or counsel names.
- [ ] No counsel-speak without translation; no Latin; no rule numbers without a plain-English equivalent.
- [ ] Recommendation is approve/decline/defer with the consequence of each.
- [ ] Cost-to-date, budget remaining, and burn-to-milestone all present.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Burying the ask under procedural history | Decision and deadline go above the fold; history is supporting context |
| Single-point exposure estimate dressed up as certainty | Use a range and tie endpoints to drivers; flag probability band |
| Using "12(b)(6) granted in part" without translation | Translate ("court dismissed two of the five claims") — keep the rule number only if needed for the record |
| Hedging the recommendation to avoid commitment | Commit to approve/decline/defer; the executive cannot act on hedge |
| Treating "reasonably possible" as a synonym for "likely" | Use ASC 450 terms with discipline; "reasonably possible" ≠ "probable" |
| Inventing a settlement number to make the page feel concrete | If no offer exists, say so; do not anchor with a fabricated number |
| Pasting the matter-management system status without translation | "Discovery — Phase 2 fact" means nothing to a CFO; translate to "depositions of our witnesses occur in {month}" |
| Omitting cost posture because it is uncomfortable | Cost-to-date and budget remaining are required fields; if over budget, say so and explain |
| Sending outside the privileged circle without redaction discipline | If broader distribution is contemplated, identify what must be redacted and re-issue a non-privileged variant |
| Boilerplate "this does not constitute legal advice" disclaimer | Remove — the recipient is consulting counsel by reading this |
