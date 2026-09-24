---
title: "Vendor Security Questionnaire Review — Reading a Supplier's Answers as the Buyer, Tiered by What They Will Touch"
category: risk
description: "Review a prospective or existing vendor's security questionnaire, attestation or trust-page claims from the buyer's side: tier the vendor by the data and access it will hold, ask only the questions that tier warrants, grade each answer by evidence strength rather than by 'yes', convert vague answers into checkable follow-ups, and end in approve / approve-with-conditions / escalate / decline with residual risk accepted by a named owner; distinct from `domain-business-strategy/research/research_vendor_evaluation.md` (whole-vendor fit and cost) and `domain-agentic-resources/skills/security/supply-chain-risk-auditor/SKILL.md` (software dependency risk)."
techniques:
  - ST-43
  - RT-05
  - DD-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - vendor-risk
  - third-party-risk
  - security-questionnaire
  - procurement
  - due-diligence
  - small-business
updated: "2026-09-24"
reasoning:
  styles: [evidential, evaluative, adversarial, structural]
  stakes: variable
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: [matrix, structured]
  user_role: [operator, procurement, founder, office-manager]
  mode: [audit, assess, decide]
related_prompts:
  - domain-business-strategy/research/research_vendor_evaluation.md
  - domain-agentic-resources/skills/security/supply-chain-risk-auditor/SKILL.md
  - domain-risk/risk_dependency_chain_audit.md
---

# Vendor Security Questionnaire Review

**Objective:** Turn a vendor's security answers into a decision you can defend — how much
scrutiny this vendor deserves, which answers are evidenced and which are just "yes", what
you still need to see, and what residual risk someone in your organisation is knowingly
accepting.

**When to Use:**
- You are about to give a SaaS tool, payroll provider, IT contractor or agency access to
  your data or systems, and a client, insurer or your own caution says "check their security".
- A vendor sent back a completed questionnaire, a SOC 2 / ISO certificate, or a trust-page
  link, and you cannot tell whether it is good.
- An existing vendor's renewal is due and nobody has looked since signing.

**Not this prompt if:**
- You are deciding whether the vendor is the right product at the right total cost —
  `domain-business-strategy/research/research_vendor_evaluation.md` (run it first; this is its security lens).
- You are assessing open-source or package dependencies in code — `domain-agentic-resources/skills/security/supply-chain-risk-auditor/`.
- You are the **vendor** answering a customer's questionnaire — this is buyer-side only.
- You need contract security clauses drafted — route to counsel; this prompt lists what to ask counsel for.
- You are negotiating price and terms — `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md`.

**Boundary:** Review of documents the vendor provides and public information only. No
scanning, probing or testing of the vendor's systems, which requires their written authorisation.

## Inputs / Context

1. **What the vendor will do**, and what it will hold or touch: data types (personal,
   financial, health, client-confidential), system access (admin? network? SSO?), volume.
2. **How replaceable it is** (from `risk_dependency_chain_audit.md` if run).
3. **The vendor's materials:** questionnaire answers, attestation reports and their scope
   and period, certificates, policies, trust page.
4. **Your obligations:** client contract clauses, insurer conditions, regulatory context
   (as stated in those documents — do not infer).
5. **Your appetite:** from `risk_appetite_statement.md` if one exists.

## Method

1. **Tier the vendor before reading answers (ST-43).**

   | Tier | Signature | Depth of review |
   |---|---|---|
   | 1 — Critical | Holds sensitive/regulated data, or has admin/network access, or hard to replace | Full review, evidence required, annual re-review |
   | 2 — Elevated | Holds internal/confidential data, no privileged access | Core questions, evidence for top items |
   | 3 — Low | No data beyond contact details, no access | Short checklist, trust page is enough |

   Over-reviewing tier 3 vendors is how small teams run out of time for tier 1.

2. **Ask the tier's core questions only.** For tier 1–2, the questions that carry the most
   weight for a buyer without a security team:
   - Multi-factor authentication for their staff and offered to you (SSO/MFA)?
   - Encryption of your data in transit and at rest?
   - Backups — and when a restore was last tested?
   - Breach notification to customers — commitment and timeframe **in the contract**?
   - Sub-processors — who, where, and notice of change?
   - Data return and deletion at exit?
   - Independent assurance — which report, what scope, what period?

3. **Grade each answer by evidence (RT-05).** E3 = independent evidence covering this service
   and a current period (e.g. an attestation report whose scope names the product). E2 =
   vendor document (policy, screenshot, contract clause). E1 = unsupported "yes". E0 = no answer
   or evasion. Check the **scope and period** of any report: a certificate for a different
   product, entity or an expired period is E1 at best.

4. **Translate vague answers into checkable follow-ups (DD-02).** "Industry-standard
   encryption" → "Which data stores are encrypted at rest, and who holds the keys?"
   "We take security seriously" → no information; re-ask the question.

5. **Rank the gaps (DS-06).** Severity = what the gap exposes × the tier. A missing MFA
   answer at a tier-1 vendor outranks five policy gaps at tier 3.

6. **Decide, with conditions and an owner.** Approve / approve-with-conditions (contract
   clause, configuration you must switch on, deadline for evidence) / escalate (to counsel or
   leadership) / decline. Residual risk is accepted by a **named role**, in writing.

## Output Format

```
# Vendor security review — [vendor], [service], [date]
Reviewer: [role] · Tier: [1/2/3] because [data/access/replaceability]

## Evidence table
| Question | Vendor answer (quoted) | Evidence grade E0–E3 | Scope/period check | Gap? |

## Follow-ups (vague → checkable)
| Original answer | Follow-up question | Needed by |

## Ranked gaps
| Gap | Exposes | Severity | Mitigation (theirs / ours / contract) |

## Decision: approve / approve-with-conditions / escalate / decline
Conditions: ... · Contract asks for counsel: ... · Our configuration to-dos: ...
Residual risk accepted by: [role], [date] · Re-review: [date]
Confidence: High / Medium / Low — [reason]
```

## Verification

- [ ] Tier set from data, access and replaceability before any answer was read.
- [ ] Every answer carries an evidence grade; unsupported "yes" is E1, not a pass.
- [ ] Every attestation's scope and period checked against this service.
- [ ] Every vague answer has a concrete follow-up question.
- [ ] Buyer-side configuration duties (turn on MFA/SSO, restrict sharing) listed.
- [ ] Breach-notification terms sourced to the contract, not the sales deck.
- [ ] Residual risk accepted by a named role with a re-review date.

## False-Positive Prevention

1. **"Yes" is not evidence.** A completed questionnaire of unsupported yeses is a sales
   document. Grade it E1.
2. **Right report, wrong scope.** An attestation for the parent company's other product, or
   last year's period, does not cover this service.
3. **Certificate worship.** An attestation shows controls existed and were tested for a
   period; it does not mean your configuration is safe. List your own set-up duties.
4. **Uniform depth.** Sending the 200-question form to a tier-3 newsletter tool wastes the
   time tier-1 needs, and vendors stop answering carefully.
5. **Trust page as contract.** Breach-notification promises on a web page are not
   obligations. Ask counsel what the contract says.
6. **Decline by default.** Most gaps are closable with a condition. The decision is about
   residual risk someone owns, not a perfect score.
7. **Testing their systems yourself.** Out of scope and possibly unlawful without authorisation.

## Example Output

```
# Vendor security review — ClearPayroll, payroll SaaS, 2026-09-20
Reviewer: Operations Manager · Tier 1: holds staff bank details and national ID numbers; hard to replace mid-year

## Evidence table
| MFA for our admins | "Supported" | E2 (help-centre doc) | n/a | Ours to enable |
| Encryption at rest | "Industry standard" | E1 | — | Yes → follow-up 1 |
| Independent assurance | Attestation report attached | E3 | Scope names "ClearPayroll Platform", period ends 2026-03 | No |
| Backup restore tested | No answer | E0 | — | Yes → follow-up 2 |
| Breach notification | "Within 72h" (trust page) | E1 | Not in draft contract | Yes → counsel |
| Sub-processors | List attached | E2 | Includes offshore support | Note for counsel |

## Follow-ups
| "Industry standard" | Which stores holding employee records are encrypted at rest; who holds keys? | Before signing |
| (no answer) | Date and result of last full restore test? | Before signing |

## Ranked gaps
1. Breach-notification not contractual — High — contract clause (counsel)
2. Restore test unknown — Medium — vendor evidence
3. Admin MFA off by default — Medium — ours: enable at onboarding

## Decision: approve-with-conditions
Conditions: follow-ups 1–2 answered at E2+; counsel adds notification + deletion-at-exit clauses; MFA enforced day 1.
Residual risk (offshore support access) accepted by: Managing Director, 2026-09-24 · Re-review: 2027-09
Confidence: Medium — attestation is strong; two answers still pending.
```

## Techniques Used

- **ST-43 Risk-Stratified Documentation** — review depth set by vendor tier.
- **RT-05 Evidence-Based Reasoning** — E0–E3 grading with scope and period checks.
- **DD-02 Vague-to-Concrete Translation** — marketing answers into checkable follow-ups.
- **DS-06 Prioritization and Severity Guidance** — gaps ranked by exposure × tier.
- **QA-12 False Positives Identification** — what not to accept as assurance.

## Related Prompts

- `../domain-business-strategy/research/research_vendor_evaluation.md` — the whole-vendor decision this feeds.
- `risk_dependency_chain_audit.md` — replaceability, which sets the tier.
- `risk_appetite_statement.md` — where "acceptable residual risk" is defined.
- `../domain-agentic-resources/skills/security/supply-chain-risk-auditor/SKILL.md` — software dependencies instead of service vendors.
