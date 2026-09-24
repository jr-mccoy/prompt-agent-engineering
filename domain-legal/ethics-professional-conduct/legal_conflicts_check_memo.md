---
title: "Conflicts Check Memo — Concurrent, Former-Client, and Imputed Conflicts with Waiver Options"
category: legal/ethics-professional-conduct
description: "Analyze conflict-of-interest hits for a proposed engagement or lateral hire under the controlling jurisdiction's adopted versions of MRPC 1.7 (concurrent), 1.9 (former client), 1.10 (imputation and screening), and 1.18 (prospective clients): identify each potential conflict, test consentability, evaluate imputation and screening, and set out waiver and informed-consent options with the disclosures each requires — ending in accept / accept with consents / accept with screen / decline."
techniques:
  - ST-02
  - DS-01
  - CM-02
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - legal
  - ethics
  - professional-responsibility
  - conflicts-of-interest
  - mrpc
  - imputation
  - screening
  - informed-consent
  - new-client-intake
updated: "2026-09-24"
reasoning:
  styles: [analytic, systematic, rule_application]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [attorney, general_counsel_law_firm, conflicts_analyst]
related_prompts:
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
  - domain-legal/ethics-professional-conduct/legal_sanctions_risk_premortem.md
  - domain-legal/ethics-professional-conduct/legal_unauthorized_practice_jurisdiction_assessment.md
---

# Conflicts Check Memo

**Objective:** Turn a conflicts-database report and matter facts into a reasoned memo for the firm's conflicts partner or general counsel. For every hit, decide whether a concurrent-client, former-client, prospective-client, or personal-interest conflict exists under the controlling jurisdiction's adopted rules; whether it is consentable; whether it is imputed to the firm and whether screening cures imputation; and what informed consent, confirmed in writing, would have to disclose. End with a disposition and the exact next steps.

**When to use:**
- New-matter intake returns one or more conflicts hits.
- A lateral lawyer or group is joining and brings former-client matters.
- A current matter changes (new party, new claim, merger of a client with an adverse party) and triggers a re-check.
- An advance waiver is proposed in an engagement letter and its enforceability needs assessment.

**Distinct from:**
- `domain-legal/client-intake-communications/legal_new_matter_intake_summary.md` — gathers the conflicts-check *inputs*; this prompt *analyzes* the hits.
- `domain-legal/client-intake-communications/legal_engagement_letter_drafter.md` — drafts the letter, including any waiver language this memo recommends.
- `domain-finance/regulatory-compliance/finance_reg_bi_fiduciary_check.md` — financial-adviser conflicts under securities standards, not lawyer conflicts.

---

## Your Input

- **Controlling jurisdiction(s):** [State bar(s) whose rules govern; choice-of-rule issues for multi-state matters]
- **Rules text supplied:** [Paste the jurisdiction's adopted Rules 1.0 (definitions of informed consent, confirmed in writing, screened), 1.7, 1.9, 1.10, 1.18, and relevant comments. State versions often depart from the ABA Model Rules — especially on lateral screening. Anything not supplied is marked `[VERIFY]`.]
- **Proposed engagement:** [Client, adverse parties, related parties (parents, subsidiaries, insurers, officers), matter type, scope, forum]
- **Conflicts report hits:** [For each: party, relationship (current client / former client / prospective client / adverse party / lawyer's personal interest), matter description, responsible lawyer, dates, status]
- **Confidential information exposure:** [For former-client and prospective-client hits: what information the firm or lawyer received]
- **Lateral facts (if any):** [Lateral's prior firm matters, personal involvement, information acquired]
- **Existing engagement terms:** [Advance waivers, corporate-family scope clauses, outside counsel guidelines of relevant clients]

---

## Constraints

**Must:**
- Analyze each hit separately and classify it: concurrent direct adversity; concurrent material-limitation risk; former client (same or substantially related matter, materially adverse); prospective client; personal-interest; none.
- For concurrent conflicts, test **consentability** against each condition in the supplied text of Rule 1.7(b) (or local equivalent), stating facts for each condition.
- For former-client conflicts, analyze "substantially related" by comparing the matters' facts and the confidential information that would normally have been obtained, not just the matter labels.
- Analyze imputation under the supplied Rule 1.10 (or equivalent): whether the conflict is personal and non-imputed, and whether screening is permitted and adequate for this type of conflict in this jurisdiction.
- For each consent required: identify who must consent, what the disclosure must cover (material risks and reasonably available alternatives), and the writing requirement per the supplied rule.
- Address corporate-family issues (is an affiliate of a current client itself a client for conflict purposes?) using the supplied rule comments and any engagement-letter terms.
- Address client outside counsel guidelines that impose stricter conflict terms than the rules.

**Must Not:**
- Invent rule text, comments, ethics opinions, or case law. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[NEED HOLDING: ...]`, `[VERIFY: {jurisdiction} version of Rule X]`.
- Assume the ABA Model Rule text governs a state that has adopted different language.
- Treat a hot-potato withdrawal (dropping a current client to clear a conflict) as a clean cure without flagging the risk.
- Treat an advance waiver as automatically effective; assess its specificity and the client's sophistication under the supplied comment text.
- Conclude "no conflict" because the hit's matter is closed without checking whether the client relationship is current.
- Use generic "consult counsel" boilerplate; the reader is the firm's ethics counsel.

---

## Instructions

1. **Jurisdiction and rule lock.** Identify controlling rules; list which were supplied and which are `[VERIFY]`.
2. **Relationship status.** For each hit, determine whether the person is a current, former, or prospective client, or unrelated; explain.
3. **Conflict classification.** Apply the supplied rule text to each hit.
4. **Consentability.** For concurrent conflicts, walk each 1.7(b)-type condition.
5. **Former-client analysis.** Substantial relationship and material adversity; information comparison.
6. **Imputation and screening.** Personal vs imputed; screening availability and required elements (timely screen, no fee apportionment where required, written notice) per supplied text.
7. **Consent plan.** Who, disclosure content, writing requirement, timing, and fallback if consent is refused.
8. **Disposition.** Accept / accept with consents / accept with screen / decline, with conditions and owners.

---

## Output Format

```markdown
# CONFLICTS MEMORANDUM — CONFIDENTIAL
**To:** {Conflicts partner / Firm GC} **From:** {...} **Date:** {...}
**Re:** {Proposed client} — {Matter} — Conflicts Analysis

## 1. Disposition
{Accept / Accept with consents / Accept with screen / Decline} — {one paragraph}

## 2. Controlling Rules
| Rule | Jurisdiction's version supplied? | Notable departure from Model Rule |
|---|---|---|

## 3. Hit-by-Hit Analysis
### Hit {n}: {Party} — {relationship}
- Status: {current / former / prospective / none} — basis
- Conflict type: {...} — rule applied (quoted)
- Consentable? {condition-by-condition}
- Imputed? Screen available? {...}
- Required consents: {who; disclosure content; writing}

## 4. Corporate-Family and Outside-Counsel-Guideline Issues
## 5. Consent and Screening Plan
| Action | Party | Content | Owner | Deadline |
|---|---|---|---|---|
## 6. Residual Risks (disqualification, fee forfeiture, discipline)
## 7. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** Firm is asked to sue a regional bank for a manufacturer on a lending-fraud claim. Hits: (1) the bank's wealth-management subsidiary is a current client in an unrelated trust-administration matter handled by a different office; (2) a lateral partner joining next month represented the bank at her prior firm three years ago in a loan-documentation dispute with a different borrower. Jurisdiction's Rules 1.7, 1.9, 1.10 supplied; its Rule 1.10 permits screening of laterals only for specified circumstances (as quoted by the user).

**Output (excerpt):**
- **Hit 1:** Whether the subsidiary's engagement makes the parent bank a current client depends on the supplied Rule 1.7 comment on affiliates and the engagement letter's scope clause. Engagement letter defines the client as the subsidiary only and the supplied comment text treats affiliates as non-clients absent shared general counsel or other stated factors; facts show separate legal departments. **No direct adversity**; material-limitation risk assessed as low (different office, unrelated matter). Recommend courtesy disclosure under the subsidiary's outside counsel guidelines, which require notice of adverse engagements against affiliates.
- **Hit 2:** Former-client analysis: the prior matter concerned the bank's loan-documentation practices — the same practices at issue in the fraud claim → **substantially related**; lateral would have normally obtained confidential information on documentation procedures. Personal conflict under 1.9(a). Imputation: the supplied Rule 1.10 permits screening in the stated circumstances; whether the lateral's "substantial participation" exception applies is **Open** — `[VERIFY: meaning of "substantial participation" in jurisdiction's comments or ethics opinions]`.
- **Disposition:** Accept with screen, conditioned on confirming the screening exception and implementing the screen before the lateral's start date with written notice to the bank as the supplied rule requires.

---

## Verification

- [ ] Jurisdiction lock: every rule applied is the controlling jurisdiction's supplied version; departures from the Model Rules noted.
- [ ] Citation discipline: no invented rules, comments, ethics opinions, or cases.
- [ ] Every hit has a relationship status and a classification.
- [ ] Consentability walked condition by condition for each concurrent conflict.
- [ ] Former-client analysis compares facts and information, not labels.
- [ ] Imputation and screening analyzed per supplied Rule 1.10 text, including notice requirements.
- [ ] Consent plan specifies who, content, writing, and fallback.
- [ ] Outside counsel guidelines checked.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Applying ABA Model Rule 1.10 lateral screening in a state with narrower screening | Use the supplied state text; `[VERIFY]` if not supplied |
| "Different matter, so no conflict" for a current client | Direct adversity to a current client is a conflict regardless of relatedness |
| Substantial relationship decided by matter labels | Compare facts and the confidential information normally obtained |
| Treating an affiliate as automatically a client, or automatically not | Apply the supplied comment factors and engagement-letter scope |
| Advance waiver treated as blanket consent | Assess specificity, client sophistication, and whether the conflict was reasonably foreseeable when waived |
| Dropping a current client to convert it to a former client | Flag the hot-potato risk; do not present as a cure |
| Ignoring stricter outside counsel guidelines | Check client guidelines; breach can cost the relationship even where rules permit |
