---
title: "New Matter Intake Summary"
category: legal/client-intake-communications
description: "Structured intake summary for a prospective or new client matter — captures factual narrative, conflicts-check inputs, scope candidates, fee-structure analysis, immediate-action triggers, and MRPC 1.18 prospective-client and MRPC 1.1 competence assessments — in a form suitable for conflicts check, engagement decision, and engagement letter drafting."
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
  - client-intake
  - intake-summary
  - conflicts-check
  - scope
  - fee-structure
updated: "2026-05-11"
related_prompts:
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
---

**Purpose:** Produce a complete intake summary for a new or prospective matter that supports (a) a conflicts check, (b) the lawyer's go/no-go engagement decision, (c) drafting the engagement letter, and (d) early triage of deadlines and preservation obligations. Output is internal-firm work product; it is not a client deliverable and not legal advice.

**When to use:** First substantive contact with a prospective client; before sending an engagement letter; before opening a matter in the firm's billing/conflicts system; when transferring a matter to a new responsible attorney.

---

## Your Input

- **Jurisdiction(s):** [State(s) of the client, the matter's situs, the forum likely to hear any dispute — state bar rules vary]
- **Practice area:** [E.g., commercial litigation, employment, family, immigration, IP, criminal defense, transactional]
- **Posture / stage:** [Pre-dispute / demand received / suit filed and served / appeal / transactional negotiation / regulatory inquiry]
- **Prospective client identity:** [Name(s); business form (individual / LLC / corp / partnership / trust); decision-maker(s) with authority]
- **Source of referral:** [Self-referral / lawyer referral / existing client / advertising / referral service — note any fee-sharing implications]
- **Factual narrative (client's account):** [Who, what, when, where, harm — verbatim where possible, paraphrased where not]
- **Adverse parties (known/suspected):** [Names, business form, counsel if known]
- **Related entities:** [Affiliates, parents, subsidiaries, insurers, indemnitors, guarantors, spouses, co-tenants, co-borrowers]
- **Witnesses and material non-parties:** [Names, role, anticipated favorability]
- **Documents in client's possession:** [Contracts, communications, regulatory notices, court papers, medical/financial records]
- **Known deadlines:** [Statute of limitations estimate, response deadlines, regulatory notice windows, contract-cure periods]
- **Client's stated objective:** [What outcome the client wants; budget tolerance; appetite for litigation]
- **Conflicts already disclosed by client:** [E.g., "I previously had a consultation with another lawyer at your firm"]

---

## Constraints

**Must:**
- Capture the **jurisdiction(s)** governing both the substantive claim and the lawyer's licensure / bar rules.
- Produce **conflicts-check inputs** as a discrete, machine-checkable list (every party, related entity, adverse party, key witness, prior counsel).
- Identify **immediate-action triggers**: statute-of-limitations estimate, evidence-preservation / litigation-hold trigger, regulatory notice deadlines, contractual cure or notice deadlines.
- Identify **scope candidates** (limited-scope / full-service / unbundled) and the practice-area-appropriate **fee structures** with the state-bar rules that constrain each.
- Assess **MRPC 1.1 competence** explicitly: does the firm have the substantive and jurisdictional competence, or does the matter require co-counsel / association / decline?
- Treat the prospective client as a **MRPC 1.18 prospective client**: information received is confidential even if no engagement results; note any disqualification risk.
- Use placeholders `[CITE: ...]`, `[NEED: ...]`, `[VERIFY: ...]` for any statute, rule, deadline, or fact not supplied.
- Mark factual statements as **client-reported** vs. **document-verified** vs. **counsel's inference**.

**Must Not:**
- Invent party names, dates, dollar amounts, deadlines, statutory citations, or witness identities.
- Provide legal advice to the prospective client in this internal document.
- Treat conflicts as "cleared" — output the inputs; clearance is a separate firm process.
- State a definitive statute-of-limitations expiration date without citation — provide an **estimate range** flagged for verification.
- Include generic "consult counsel" disclaimers — this is an internal lawyer work product, not a client-facing document.

---

## Instructions

1. **Header.** Date of intake, intake interviewer, proposed responsible attorney, prospective-client name, matter short title.
2. **Factual narrative.** Structured chronology (who / what / when / where / harm). One event per bullet where possible. Mark each entry as client-reported, document-verified, or counsel inference.
3. **Conflicts-check inputs.** Discrete list: prospective client and all aliases / prior names / DBAs; spouses and household members where relevant; business form and all related entities (parents, subs, affiliates); adverse parties and their related entities; insurers / indemnitors; material witnesses; opposing counsel if known; prior counsel.
4. **Jurisdictional analysis.** Governing substantive law; likely forum; lawyer's bar admissions vs. forum requirements; pro hac vice or local-counsel need.
5. **MRPC 1.1 competence assessment.** Substantive competence (does the firm handle this area?); jurisdictional competence; resource competence (capacity, deadlines); co-counsel / association need; decline-and-refer recommendation if competence is absent.
6. **Scope candidates.** Limited scope (specific task — e.g., draft a demand only); unbundled (advice + ghost drafting); full-service representation through resolution; phased scope with defined off-ramps. Note client's stated preference.
7. **Fee-structure analysis.** Evaluate each candidate fee structure for the practice area and jurisdiction:
   - **Hourly** with rates and billing increment; advance retainer / evergreen retainer requirement; IOLTA handling.
   - **Flat fee** with scope tied to defined deliverable; refundability under the state's rules (some states require flat fees be deposited in trust until earned).
   - **Contingency** with the state-bar contingency-fee cap or schedule where applicable (e.g., medical malpractice caps, workers' comp schedules), written-agreement requirements, and prohibited matters (criminal, most domestic relations per MRPC 1.5(d)).
   - **Hybrid** (reduced hourly + success fee) and reasonableness under MRPC 1.5.
   - **Statutory / court-awarded fee** matters (fee-shifting statutes, common fund).
8. **Immediate-action triggers.** Statute-of-limitations estimate (with the operative trigger date and the limitations period flagged for verification); evidence-preservation steps and litigation-hold trigger; regulatory notice deadlines (EEOC, NLRB, agency-specific); contractual cure/notice/demand prerequisites; insurance-notice deadlines; spoliation risk.
9. **Client capacity & decision-maker.** Confirm the individual with authority to engage and to settle (entity client: officer with authority; minor: guardian; estate: PR; co-owners: all signers); language / accessibility needs.
10. **MRPC 1.18 prospective-client confidentiality.** Note that all information received is confidential; flag any disqualification risk if engagement is declined.
11. **Recommendation.** Engage / engage with conditions / decline / refer; if engage, recommended scope and fee structure; if decline, reason category.

---

## Output Format

```markdown
# NEW MATTER INTAKE SUMMARY — INTERNAL / ATTORNEY WORK PRODUCT
**Privileged & Confidential — MRPC 1.18 Prospective-Client Information**

Intake date: {date}
Intake by: {name, role}
Proposed responsible attorney: {name}
Matter short title: {e.g., "Smith v. Acme — Employment"}

## 1. Prospective Client
- Name / business form: {…}
- Decision-maker with engagement authority: {name, role, basis for authority}
- Contact: {…}
- Referral source: {…}  [fee-sharing implications: {none / disclose}]

## 2. Factual Narrative
[Chronological. Mark: (CR) client-reported, (DV) document-verified, (CI) counsel inference.]
- {YYYY-MM-DD}: {event} (CR)
- {YYYY-MM-DD}: {event} (DV — {doc})
- …
Harm alleged: {…}
Client's stated objective: {…}

## 3. Conflicts-Check Inputs
- Prospective client + aliases/DBAs/prior names: {…}
- Related entities (parents, subs, affiliates, spouses where relevant): {…}
- Adverse parties + related entities: {…}
- Insurers / indemnitors / guarantors: {…}
- Material witnesses: {…}
- Opposing / prior counsel: {…}

## 4. Jurisdictional Analysis
- Governing substantive law: {…}
- Likely forum: {…}
- Lawyer / firm bar admissions vs. forum: {…}
- Pro hac vice / local counsel need: {yes / no / [NEED: …]}

## 5. MRPC 1.1 Competence Assessment
- Substantive: {…}
- Jurisdictional: {…}
- Resource / capacity / deadlines: {…}
- Co-counsel / association / decline: {…}

## 6. Scope Candidates
- [ ] Limited scope — {specific task}
- [ ] Unbundled — {advice + ghost drafting components}
- [ ] Full-service representation through {milestone / resolution}
- [ ] Phased with off-ramps at {…}
Client's stated preference: {…}

## 7. Fee-Structure Analysis
| Structure | Viable here? | Notes / bar-rule constraints |
|---|---|---|
| Hourly + advance retainer (IOLTA) | {y/n} | Rate range {…}; replenishment terms {…} |
| Flat fee | {y/n} | Refundability under {state} rule [CITE: …] |
| Contingency | {y/n} | Cap/schedule [CITE: …]; MRPC 1.5(c) writing required |
| Hybrid | {y/n} | Reasonableness under MRPC 1.5 |
| Statutory / fee-shifting | {y/n} | Basis: [CITE: …] |
Recommended: {…}

## 8. Immediate-Action Triggers
- Statute of limitations: estimate {N} years from {trigger date}; expiration ~{date}. [VERIFY against [CITE: …]]
- Evidence preservation / litigation hold: {trigger met? action needed by {date}}
- Regulatory notice deadlines: {agency, deadline} [VERIFY]
- Contractual cure / notice prerequisites: {…}
- Insurance notice: {…}
- Spoliation risk: {…}

## 9. Client Capacity & Decision-Maker
- Capacity confirmed: {y/n; basis}
- Settlement authority: {…}
- Language / accessibility: {…}

## 10. MRPC 1.18 Note
Information received is confidential. Disqualification risk if declined: {assessment}.

## 11. Recommendation
- [ ] Engage — scope: {…}; fee: {…}
- [ ] Engage with conditions: {…}
- [ ] Decline — reason: {conflict / competence / capacity / fit / non-meritorious / other}
- [ ] Refer to: {…}
Next step: {draft engagement letter / send non-engagement letter / run conflicts}
```

---

## Verification

- [ ] Jurisdiction(s) for substantive law and lawyer licensure both identified.
- [ ] All conflicts-check inputs listed as a discrete checkable list.
- [ ] Factual statements marked CR / DV / CI.
- [ ] Statute-of-limitations estimate present with trigger date and verification flag.
- [ ] Evidence-preservation / litigation-hold trigger addressed.
- [ ] MRPC 1.1 competence assessment present.
- [ ] MRPC 1.18 prospective-client confidentiality acknowledged.
- [ ] Scope candidates and fee structures both evaluated against the practice area and state-bar rules.
- [ ] No invented party names, dates, dollar amounts, citations.
- [ ] Recommendation is one of: engage / engage with conditions / decline / refer.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating intake as a client deliverable | This is internal attorney work product; do not insert advice or disclaimers to the client |
| Stating SOL "expires on {exact date}" without verifying the controlling statute | Provide an estimate range with `[VERIFY against [CITE: …]]`; identify the operative trigger |
| Listing only the named prospective client for conflicts | List all related entities, insurers, witnesses, spouses, prior counsel — conflicts run wider than the caption |
| Recommending contingency in a prohibited matter (criminal, most domestic relations) | MRPC 1.5(d) prohibits — flag and re-evaluate |
| Skipping the MRPC 1.18 note when the firm may decline | Prospective-client confidentiality and imputed-disqualification risk attach regardless of engagement |
| Confusing client-reported facts with verified facts | Mark CR / DV / CI on every factual line |
| Recommending hourly without addressing trust-account / IOLTA handling for the advance retainer | State which funds go to trust vs. operating, and replenishment terms |
| Failing to note co-counsel need where competence is partial | MRPC 1.1 permits association of competent counsel; flag the gap and the proposed cure |
| Capturing only the individual contact when the client is an entity | Identify the officer with binding authority and the basis for that authority |
| Omitting fee-sharing disclosure when matter came via paid referral | MRPC 7.2 / 1.5(e) implications — flag at intake |
