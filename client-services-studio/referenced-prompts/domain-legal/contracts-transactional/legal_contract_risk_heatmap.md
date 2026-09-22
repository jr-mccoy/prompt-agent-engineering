---
title: "Contract Risk Heatmap with Negotiation Posture"
category: legal/contracts-transactional
description: "Produce a triage-grade issues list scoring each risk on severity, likelihood, and deal impact; categorize each as must-have / should-have / fallback; and identify escalation triggers requiring business or executive input."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: beginner
tags:
  - legal
  - contracts
  - risk-assessment
  - triage
  - escalation
  - playbook
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Produce a heatmap, not a redline. Score each identified risk on severity × likelihood × deal impact; classify each as must-have-change, should-have-change, or acceptable fallback; identify which issues require escalation beyond legal (CFO for financial caps, CISO for security, GM for commercial terms). Output is triage-grade — fast, structured, and decision-ready.

**When to use:** Early-stage review when the question is "is this paperable at all and where do I focus?"; pre-call prep before a negotiation; portfolio review across many contracts; executive-summary deliverable for non-lawyers.

---

## Your Input

- **Contract document:** [Paste full text or attach]
- **Contract type:** [MSA / SOW / SaaS / License / NDA / Reseller / Other]
- **Governing law:** [State + country]
- **Posture:** [Buyer/Customer/Licensee OR Supplier/Vendor/Licensor]
- **Deal value:** [Annual contract value, total contract value, term length]
- **Strategic importance:** [Critical vendor / commodity / pilot / strategic partner]
- **Counterparty leverage:** [High / equal / low]
- **Regulatory overlay:** [HIPAA, GDPR, GLBA, FedRAMP, sector-specific]
- **Internal authority matrix:** [Who can approve LoL cap exceptions; who approves uncapped indemnity carve-outs; who approves data-breach exposure beyond $X]
- **Timeline pressure:** [Days to signature]

---

## Constraints

**Must:**
- Score every issue on three axes: **Severity** (1–5), **Likelihood** (1–5), **Deal Impact** (1–5). Composite score drives tier.
- Classify each issue as **Must-Have** (block signature), **Should-Have** (push hard, accept defensible fallback), or **Fallback-Acceptable** (note, do not block).
- Identify the **escalation owner** for each Must-Have issue (Legal / CFO / CISO / Privacy / GM / CEO / Board).
- Distinguish **legal risk** (enforceability, regulatory, indemnity) from **commercial risk** (price, term, exit cost) — both appear in the heatmap but only legal risk gets routed to Legal-Critical.
- Include a **counterfactual line** for each Must-Have: what happens at signature if this is not changed.
- Order the heatmap by composite score, descending.
- Provide a **one-line top-of-page recommendation**: sign / sign with negotiation / do not sign.

**Must Not:**
- Invent citations or statutes. Use `[CITE: ...]`.
- Confuse heatmap with redline; this prompt does not produce markup language. Refer the user to the full or targeted redline prompts for markup.
- Inflate severity scores to drive attention; the heatmap loses utility when everything is Critical.
- Score in the abstract — every score must reference a specific section number and the operative text.
- Use generic disclaimers about consulting counsel.

---

## Severity Tiers (composite score → tier)

| Composite Score | Tier | Definition |
|---|---|---|
| 12–15 | **Critical** | Block signature. Sign-as-is creates material legal, regulatory, or financial exposure. Escalation required. |
| 9–11 | **High** | Strong push. Defensible fallback exists. Do not concede in round 1. |
| 5–8 | **Medium** | Negotiate if leverage allows. Tradeable for higher-tier wins. |
| 3–4 | **Low** | Note only. Do not block. |

Composite = Severity + Likelihood + Deal Impact (each 1–5). Severity scores the harm if the risk materializes; Likelihood scores how often this risk hits in similar deals; Deal Impact scores how much the issue moves total cost / revenue / exposure.

---

## Instructions

1. **Issue identification pass.** Scan the contract for the standard issue catalog: indemnity, LoL, IP, warranties, termination, payment, audit, data protection, confidentiality, assignment, governing law, dispute resolution, regulatory addenda, insurance, force majeure, MFN, exclusivity, change-of-control, source-code escrow.
2. **Score each issue.** Apply the three-axis scoring. Anchor every score in the operative text and posture.
3. **Classify each issue.** Must-Have / Should-Have / Fallback-Acceptable.
4. **Assign escalation owner.** Use the input authority matrix where provided; otherwise default mapping (LoL cap exception → CFO; data-breach exposure → CISO + Privacy; uncapped indemnity → Legal + CEO; commercial caps → GM).
5. **Identify gaps.** Issues the contract does not address but should given posture and regulatory overlay (e.g., missing DPA, missing BAA, missing source-code escrow for critical systems).
6. **Build the heatmap table.** One row per issue. Sort by composite score descending.
7. **Write the counterfactual** for each Critical issue: what is the exposure at signature?
8. **Write the recommendation** at the top.

---

## Output Format

```markdown
# Contract Risk Heatmap — {Contract Title}
**Posture:** {Buyer/Supplier}  |  **Governing Law:** {state}  |  **Date:** {YYYY-MM-DD}

## Top-of-Page Recommendation
{One line: Sign / Sign with negotiation / Do not sign}

## Summary by Tier
- Critical: {count} | High: {count} | Medium: {count} | Low: {count}
- Escalations needed: {CFO / CISO / GM / CEO}

## Heatmap

| # | Issue | § | Sev | Lik | Impact | Score | Tier | Classification | Escalation | Counterfactual |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Uncapped indemnity for data breach | § 8.1 | 5 | 4 | 5 | 14 | Critical | Must-Have | Legal + CEO | Single incident could exceed $XXM; no insurance recovery beyond cyber policy limits |
| 2 | LoL cap = 6 months fees | § 9.2 | 4 | 3 | 4 | 11 | High | Should-Have | CFO | Cap below industry norm of 12 months × fees |
| 3 | Auto-renewal with 90-day notice window | § 12.3 | 2 | 5 | 2 | 9 | High | Should-Have | GM | Missed window = full additional year |
| ... | | | | | | | | | | |

## Gaps (Issues Not Addressed)
| Gap | Required because | Recommended insertion |
|---|---|---|
| Missing DPA | GDPR — counterparty processes EU PII | Add DPA + SCCs as addendum |
| ... | | |

## Critical Issue Detail

### Critical-1: {Issue Title}
- **Section:** § __
- **Current text:** "{quote}"
- **Risk:** {1–3 sentences}
- **Posture-specific impact:** {how this hurts the reviewer}
- **Counterfactual at signature:** {what happens if signed as drafted}
- **Required change (high level):** {what direction the redline should take — refer to redline prompt for markup}
- **Escalation owner:** {role}
- **Decision deadline:** {date}

### Critical-2: ...

## Escalation Routing
- **Legal-Critical (sign-block):** {issue numbers}
- **CFO sign-off needed:** {issue numbers — financial cap exceptions}
- **CISO / Privacy sign-off needed:** {issue numbers — security and data}
- **GM / Business sign-off needed:** {issue numbers — commercial terms}
```

---

## Verification

- [ ] Every row in the heatmap references a specific section number and operative text.
- [ ] Composite score = Severity + Likelihood + Deal Impact (each 1–5).
- [ ] Tier assignment follows the score band.
- [ ] Every Critical issue has a counterfactual statement.
- [ ] Gaps section identifies missing provisions, not just bad ones.
- [ ] Escalation owner assigned for every Must-Have.
- [ ] No invented citations or facts. Placeholders for missing inputs.
- [ ] Top-of-page recommendation is one line and supports the heatmap.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Scoring every indemnity issue as Critical | Severity depends on scope, cap interplay, and likelihood. Uncapped IP indemnity in a software license is Critical; capped, narrow third-party-claim-only indemnity is Medium |
| Listing 30 Medium issues with no Criticals | If nothing is Critical the recommendation is sign-with-changes; do not pad the Critical tier |
| Heatmap with no Gaps section | Missing provisions (DPA, BAA, audit, source escrow, insurance) are often more important than bad provisions; always run the gap pass |
| Routing every escalation to Legal | Legal owns enforceability; CFO owns financial caps; CISO owns data; GM owns commercial. Distribute |
| Treating Likelihood as 3 by default | Score Likelihood against actual base rates: data breach 3–4 in a SaaS deal; IP infringement claim by customer-supplied material 1–2; auto-renewal missed-notice 4–5 |
| Confusing the heatmap with a redline | Heatmap identifies and ranks; markup belongs in the redline prompts |
| Composite score that doesn't match the tier | Cross-check every row: 14 = Critical, 7 = Medium. Tier should fall out of the math |
| Counterfactual for a Critical that is theoretical ("could expose company") | Make it concrete: dollar exposure, regulatory action, customer-data scenario |
| Missing the regulatory-required addenda (BAA, DPA, SCCs) | Always run the regulatory pass; these are Critical by default when applicable |
| Generic "consult counsel" rec at the top | Replace with a concrete sign / negotiate / do-not-sign recommendation |
