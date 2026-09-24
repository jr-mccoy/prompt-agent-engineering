---
title: "Subpoena or Civil Investigative Demand Response Strategy"
category: legal/regulatory-compliance
description: "Build a response strategy for a government subpoena, civil investigative demand (CID), or third-party subpoena: deadline and authority check, hold scope, request-by-request scope objections and negotiation positions, a phased production plan, privilege protocol, and the role assessment (target, subject, or witness) that drives posture. Works from the demand's text; never asserts objection deadlines or meet-and-confer rules that are not in the supplied rules."
techniques:
  - ST-02
  - CM-03
  - CM-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - regulatory-compliance
  - subpoena
  - civil-investigative-demand
  - government-investigations
  - document-production
  - privilege
updated: "2026-09-24"
reasoning:
  styles: [analytic, systematic, strategic]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, in_house_counsel]
related_prompts:
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_privilege_review_protocol.md
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
  - domain-legal/regulatory-compliance/legal_internal_investigation_plan.md
---

# Subpoena or CID Response Strategy

**Objective:** Turn a received subpoena, CID, or similar compulsory demand into a response strategy that protects the client's position and meets the demand's obligations: confirm the issuing authority and every deadline from the demand and the rules supplied, scope the preservation obligation, decide on request-by-request objections and narrowing proposals, plan phased production with privilege protection, and set the posture for the first call with the issuing attorney or agency.

**When to use:**
- A government agency (federal or state) has served a subpoena or CID on the client.
- The client received a third-party subpoena in someone else's litigation.
- A grand-jury subpoena has been served (use with care: criminal exposure changes the posture; see Step 3).

**Distinct from:**
- `domain-legal/discovery/legal_discovery_response_objections.md` — party discovery in pending civil litigation under the civil rules; this prompt handles compulsory process from an investigating authority or a non-party subpoena, where role assessment and negotiation with the issuer dominate.
- `domain-legal/regulatory-compliance/legal_internal_investigation_plan.md` — the company's own fact-finding; often run in parallel with this response.
- `domain-legal/discovery/legal_privilege_review_protocol.md` — use it to design the privilege review once this strategy sets scope.

---

## Your Input

- **Demand text (verbatim):** [Full subpoena / CID, including definitions, instructions, schedule of requests, return date, and any cover letter]
- **Issuer and authority:** [Agency / court / party; the statute or rule the demand cites]
- **Jurisdiction and governing procedural rules (text):** [Paste the rule or statute governing objections, petitions to modify/quash, and meet-and-confer, if available]
- **Date of service and method:** [...]
- **Client's relationship to the matter:** [What the client knows about the investigation or litigation; any prior contact; industry context]
- **Data landscape:** [Custodians, systems, data volumes, date ranges, cross-border data, third-party-held data]
- **Existing holds:** [Any hold already in place and its scope]
- **Sensitivities:** [Trade secrets, personal data, privileged material, foreign blocking or data-protection statutes, parallel proceedings]
- **Client objectives:** [Minimize burden / preserve relationship with agency / protect confidential information / avoid becoming a target]

---

## Constraints

**Must:**
- Extract every date from the demand (return date, any stated objection or petition deadline) and from supplied rules. If the governing rule's deadline is not supplied, write `[VERIFY: deadline to object / petition under {rule}]` and put it at the top of the output.
- Perform a role assessment first: target, subject, witness, or third party — based on the facts supplied — and state what would change it.
- Issue or expand a legal hold scoped to the demand's definitions and date range the same day; note the hold's relationship to routine deletion.
- For each request: parse the definitions it incorporates, estimate burden, state the objection basis (if any), and propose a narrowing (custodians, date range, search terms, sampling).
- Separate **objections to preserve** from **negotiating positions**: objections stated in writing; narrowing proposed in the meet-and-confer.
- Include a privilege protocol (log format, clawback or non-waiver agreement proposal, inadvertent-production handling) and a confidentiality request (e.g., confidential treatment or FOIA-exemption request where the issuer's rules allow; `[VERIFY: mechanism]`).

**Must Not:**
- Invent objection deadlines, petition-to-quash procedures, meet-and-confer requirements, or agency confidentiality rules. Use `[CITE: ...]`, `[VERIFY: ...]`.
- Recommend boilerplate "overbroad and unduly burdensome" objections without a request-specific basis.
- Recommend any action that could be characterized as destruction or alteration of responsive material; routine deletion suspends on receipt.
- Treat a third-party subpoena as low-risk without assessing whether the client could become a party or subject.
- Add generic "consult counsel" language.

---

## Instructions

1. **Deadline and authority check.** List every date; confirm issuer authority on the face of the demand (statute, rule, signatory); note service defects without relying on them.
2. **Hold.** Define hold scope (custodians, systems, date range, data types) mapped to the demand's definitions; list who receives the notice today.
3. **Role assessment.** Target / subject / witness / third party, with the facts supporting each; list the facts that would change the classification and whether individual employees need separate counsel.
4. **Request-by-request analysis.** Table: request, definitions invoked, responsive universe estimate, objection basis, narrowing proposal, priority for first production.
5. **Production plan.** Phases (e.g., organizational documents and policies first; custodial email later), search methodology, format and load-file specs, rolling dates.
6. **Privilege and confidentiality protocol.** Log format and timing, clawback / non-waiver proposal, confidential-treatment requests, handling of personal data and cross-border data.
7. **First-call plan.** Agenda for the call with the issuing attorney: introduce counsel, request investigation scope and client's role, propose narrowing, propose rolling production, request extension if needed (with the specific date).
8. **Parallel-risk scan.** Parallel civil litigation, other agencies, disclosure obligations (public company, lenders, insurers), employee notifications.

---

## Output Format

```markdown
# Response Strategy — {Issuer} {Subpoena / CID} to {Client}
**Privileged & Confidential — Attorney Work Product**

## 0. Deadlines (verify first)
| Event | Date | Source (demand ¶ / rule) | Verified? |
|---|---|---|---|

## 1. Authority and Service
## 2. Legal Hold Scope
| Custodian / system | Data types | Date range | Notice sent |
|---|---|---|---|

## 3. Role Assessment
- Classification: {target / subject / witness / third party} — basis
- What would change it: {...}
- Separate counsel for individuals: {yes / no / evaluate}

## 4. Request-by-Request Analysis
| Req. | Definitions invoked | Responsive universe | Objection basis | Narrowing proposal | Phase |
|---|---|---|---|---|---|

## 5. Production Plan
## 6. Privilege and Confidentiality Protocol
## 7. First-Call Agenda
## 8. Parallel Risks and Disclosure Obligations
## 9. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** A regional software company receives a CID from a state attorney general under the state's consumer-protection statute seeking "all documents concerning" auto-renewal practices from January 2019 to present, with a 20-day return date stated on the face. The governing statute's petition-to-modify timing was not supplied.

**Output (excerpt):**
- Deadlines: Return date — stated in CID ¶ 1. Petition to modify / set aside — `[VERIFY: deadline and procedure under the state consumer-protection statute cited on the CID's face]`. Priority task today.
- Role assessment: **Subject** — the company's own practices are the object; no facts suggest a third party is the focus. Would become **target** if the AG references specific consumer complaints or prior warning letters.
- Request 4 ("all documents concerning cancellation flows"): definition of "documents" includes chat and ephemeral messaging. Objection basis: date range precedes the product's launch by 18 months (burden without relevance). Narrowing proposal: launch date forward; 6 named custodians; product-spec repository plus support-ticket export filtered by the cancellation tag. Phase 1.
- First call: request a 30-day extension to a specific date, propose rolling production, offer a written narrative of the renewal flow's history in lieu of the earliest-period documents.

---

## Verification

- [ ] Jurisdiction lock: procedures and deadlines come from the demand and supplied rules only.
- [ ] Citation discipline: no invented rules, deadlines, or confidentiality mechanisms; `[VERIFY]` items listed at the top.
- [ ] Hold issued with scope mapped to the demand's definitions and date range.
- [ ] Role assessment stated with the facts that would change it.
- [ ] Every objection is request-specific; narrowing proposals are concrete (custodians, dates, terms).
- [ ] Privilege protocol includes log timing and a non-waiver / clawback proposal.
- [ ] Parallel proceedings and disclosure obligations checked.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Asserting a fixed objection or petition deadline from memory | Extract from the demand or supplied rule; otherwise `[VERIFY]` at the top of the output |
| Boilerplate general objections to every request | Request-specific basis tied to definitions, burden, and relevance; general objections are often disregarded |
| Treating a third-party subpoena as routine | Run the role assessment; third parties sometimes become subjects |
| Delaying the hold until scope is negotiated | Preserve to the demand's full scope now; narrowing affects collection and production, not preservation |
| Ignoring the demand's definitions ("document," "concerning," "Company" including affiliates) | Parse definitions first; they often expand scope beyond the request text |
| Missing individual-counsel issues when employees are witnesses | Flag when an employee's interests may diverge from the company's |
| Producing privileged material without a non-waiver agreement | Propose clawback / non-waiver terms before the first production |
