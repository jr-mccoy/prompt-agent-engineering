---
title: "Independence and Conflict-of-Interest Check Before Accepting an Engagement — Accounting and Consulting Firms: Relationship Search, Threats and Safeguards, Prohibited Services, Consent, and the Accept/Decline Record"
category: specialized-fields/professional-services
description: "Before an accounting, audit, advisory or consulting firm accepts new work, run the check its professional code requires: map the prospective client, its affiliates and counterparties against the firm's attest clients and existing engagements, search firm and personal relationships, classify each hit as an independence matter (attest clients, cannot be cured by consent) or a conflict of interest (may be managed with safeguards and informed consent), apply the threats-and-safeguards framework of the governing code (AICPA, IESBA, or regulator rules for public-interest entities), screen for prohibited services, and record an accept / accept with safeguards / accept with consent / decline decision for the firm's independence or ethics partner — distinct from a law firm's MRPC conflicts check (legal_conflicts_check_memo) and from commercial client-fit screening."
techniques:
  - DT-05
  - DS-33
  - DD-05
  - OC-10
difficulty: advanced
tags:
  - auditor-independence
  - conflict-of-interest
  - client-acceptance
  - threats-and-safeguards
  - aicpa-code
  - iesba-code
  - can-we-take-this-client
  - check-for-conflicts-before-new-work
  - is-this-a-conflict-of-interest
updated: "2026-10-03"
reasoning:
  styles: [rule_application, analytic, adversarial]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [engagement_partner, independence_partner, risk_management, practice_leader]
  mode: [evaluate, decide, document]
related_prompts:
  - domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md
  - domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md
  - domain-specialized-fields/professional-services/proserv_engagement_staffing_plan.md
---

# Independence and Conflict-of-Interest Check Before Accepting an Engagement

**Objective:** Give the partner who must approve a new engagement a complete,
documented view of every relationship that could impair the firm's independence or
create a conflict of interest — each one classified, assessed against the governing
code's threats-and-safeguards framework, and ending in a clear acceptance
recommendation that the firm's independence or ethics function decides.

**When to Use:**
- A new client or a new service for an existing client is proposed, especially
  transaction, valuation, litigation-support or advisory work.
- The prospective client is connected to an audit or attest client (parent,
  subsidiary, sister entity, investor, counterparty, competitor).
- A team member has a personal financial interest, family relationship or recent
  employment link to the client.
- **Not this prompt if** you are a **law firm** — attorney conflicts under the rules
  of professional conduct are `domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md`.
  Whether a client is a good commercial fit (budget, decision-maker, red flags) is
  `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md`.
  Research-funding conflicts of interest are
  `domain-science/ethics-integrity/science_conflict_of_interest_disclosure_drafter.md`.

## Inputs / Context

1. **The proposed engagement**: client, service, deliverable, fee basis (including
   any success or contingent fee), team, and counterparties.
2. **Client structure**: parent, subsidiaries, sister entities, significant
   investors, and entities the client controls or significantly influences.
3. **Firm relationships**: attest/audit clients and their affiliates, current and
   recent engagements for the client, its counterparties and competitors.
4. **Personal relationships**: team members' and their immediate family's
   financial interests, loans, employment history and family ties to the client.
5. **Governing code**: AICPA Code of Professional Conduct, the IESBA Code (or a
   national code adopting it), and any regulator rules (e.g. SEC and PCAOB for US
   issuer audit clients), plus the firm's own stricter policies.
6. **Fee data**: fees from the client group as a share of total firm or office fees.

Code provisions are cited only as supplied or marked `[verify — current code
section]`; codes and regulator rules change. This analysis supports, and does not
replace, the determination by the firm's independence or ethics function.

## Method

1. **Map the relationship web.** Client, affiliates (using the governing code's
   affiliate definition), counterparties and competitors; then search each against
   the firm's client and engagement records, and the team against personal
   independence confirmations.
2. **Classify each hit (DT-05).** **Independence matter** — the firm audits or
   performs attest work for the client or an affiliate; impairment cannot be cured
   by client consent. **Conflict of interest** — duties to two clients whose
   interests conflict, or the firm's own interest against a client's; may be
   managed with safeguards and informed consent, unless the code or firm policy says
   otherwise. **No issue** — recorded with why.
3. **Apply the jurisdiction's framework (DS-33).** Identify threats: self-interest,
   self-review, advocacy, familiarity, intimidation (IESBA); the AICPA framework adds
   management participation and adverse interest and uses undue influence. Evaluate
   whether each threat is at an acceptable level to a reasonable and informed third
   party.
4. **Screen for prohibitions first.** Services prohibited for an attest client
   regardless of safeguards (assuming management responsibilities; for issuer and
   public-interest-entity audits, wider lists such as bookkeeping, valuation and
   certain advisory work), contingent fees from attest clients, and fee-dependence
   thresholds. A prohibition ends the analysis for that service.
5. **Identify safeguards.** Separate teams, information barriers, review by an
   uninvolved professional, partner rotation, divestment of an interest, removal of
   a team member, or declining part of the service. Each safeguard is matched to the
   threat it reduces.
6. **Consent where it applies.** For conflicts of interest: disclosure to and
   informed consent from each affected client, in writing, without breaching
   either's confidentiality. Note when consent cannot be sought without disclosing
   confidential information — that usually means decline.
7. **Separate checks from judgement (DD-05).** Prohibitions and thresholds are
   checkable; whether a threat is reduced to an acceptable level is the independence
   partner's judgement.
8. **Look forward.** If the engagement or a transaction changes the client group
   (an acquisition makes the client an affiliate of an attest client), list what
   must change before that date.
9. **Record the decision (OC-10).** Accept / accept with safeguards / accept with
   consent / decline, with approvals and the required disclaimer block.

## Output Format

```
# Independence and conflicts check — [prospective client] / [service]
Governing code(s): [..]   Firm policy: [..]   Requested by: [..]   Date: [..]

## 1. Relationship map (client · affiliates · counterparties · competitors)
## 2. Hits
| # | Relationship | Classification (independence / conflict / none) | Threats | Prohibited? |
## 3. Assessment per hit
Threat → significance → safeguard → residual (acceptable? — independence partner)
## 4. Consent requirements and feasibility
## 5. Forward-looking changes (transactions, new affiliates, fee dependence)
## 6. Recommendation: accept / with safeguards / with consent / decline
## 7. Approvals and record
Required statement: This check supports the firm's acceptance decision; independence
and ethics determinations are made by the firm's designated independence/ethics
partner under the governing code and firm policy. Not legal advice.
```

## Verification

- [ ] Affiliates are mapped using the governing code's definition, not intuition.
- [ ] Every hit is classified as independence, conflict, or none, with reasons.
- [ ] Prohibited services and contingent-fee rules are screened before safeguards.
- [ ] Each safeguard is tied to the specific threat it reduces.
- [ ] Consent is proposed only for conflicts, never to cure an independence impairment.
- [ ] Forward-looking changes from a transaction are listed with dates.
- [ ] The required statement and named approvers appear in the record.

## False-Positive Prevention

1. **Consent as a cure for independence.** An audit client's consent does not
   restore independence; only removing the threat does.
2. **Checking the entity, not the group.** Most misses are affiliates — a parent's
   new portfolio company, a sister entity, an investor with significant influence.
3. **Over-flagging.** Serving two competitors is not a conflict in itself; it
   becomes one when interests are directly adverse or confidential information is at
   risk. Say which.
4. **Safeguards without a threat.** Listing information barriers for every hit hides
   the hits where no safeguard is adequate.
5. **Ignoring personal interests.** A spouse's fund interest or a team member's
   recent employment is a firm problem once that person is on the engagement.
6. **Legal conflicts handled here.** Attorney conflicts follow different rules; send
   them to counsel.

## Example Output

```
# Independence and conflicts check — Northwind Capital Fund III / buy-side financial
due diligence on Delta Components Inc.   Codes: AICPA Code; firm policy   Date: 5 Oct

## 1. Relationship map
Delta Components: firm's AUDIT client (private company, FY audits 2023–2026).
Northwind Fund III: no current engagement. Kestrel Logistics (Northwind portfolio co.):
TAX client. Proposed fee: $140,000 + 0.25% success fee on closing.

## 2. Hits
| 1 | Acting for the acquirer of our audit client | Conflict + independence-adjacent | Advocacy, self-interest, adverse interest | — |
| 2 | Success fee from Northwind, which would become Delta's parent | Independence (post-close) | Self-interest | Contingent fee from attest client's affiliate [verify] |
| 3 | Engagement partner's spouse: 1.5% LP interest in Fund III | Independence (post-close) | Self-interest | Depends on materiality and control [verify] |
| 4 | Proposed senior manager was Delta's assistant controller until 9 months ago | Conflict / familiarity | Familiarity, confidentiality | — |

## 3. Assessment
Hit 1: DD for the buyer would use and test against information we hold as Delta's
auditor; Delta's interests (price, warranties) are adverse to Northwind's. Safeguards
(separate team, information barrier) do not address the advocacy threat to an audit
client. Residual: not acceptable [independence partner].
Hit 2: if the deal closes, Northwind controls an attest client; a success fee would be
a contingent fee from an affiliate → prohibited under firm policy regardless of safeguards.
Hits 3–4: manageable alone (rotate partner; exclude the senior manager).

## 4. Consent
Seeking Delta's consent would disclose Northwind's confidential interest in acquiring
it → consent not feasible.

## 5. Forward-looking (if Northwind acquires Delta without us)
Before close: evaluate Kestrel tax services as an affiliate service; spouse to divest
the Fund III interest or partner rotates off the Delta audit; no fees contingent on the deal.

## 6. Recommendation
DECLINE the due-diligence engagement. Notify Northwind without referring to Delta's
audit relationship beyond what is public. Start the independence transition plan above.

## 7. Approvals
Engagement partner: [ ] · Independence partner: [ ] · Risk management: [ ]
This check supports the firm's acceptance decision; independence and ethics
determinations are made by the firm's designated independence/ethics partner under
the governing code and firm policy. Not legal advice.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — each relationship hit classified and assessed on its own row.
- **DS-33 Jurisdiction-Adaptive Output** — AICPA, IESBA and regulator rules applied according to the client and engagement.
- **DD-05 Human Review Flags** — checkable prohibitions separated from the independence partner's judgement on residual threats.
- **OC-10 Mandatory Disclaimer Pattern** — the required statement and approvals built into the record.

## Related Prompts

- `domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md` — the law-firm equivalent under the rules of professional conduct.
- `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md` — commercial client-fit screening, a separate gate from ethics.
- `domain-specialized-fields/professional-services/proserv_engagement_staffing_plan.md` — applying individual restrictions when staffing accepted work.
