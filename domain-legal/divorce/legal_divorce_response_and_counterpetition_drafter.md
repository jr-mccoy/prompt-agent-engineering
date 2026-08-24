---
title: "Divorce Response and Counterpetition Drafter"
category: legal/divorce
description: "Draft a response (answer) to a petition for dissolution with paragraph-by-paragraph admissions/denials, affirmative defenses, jurisdictional and residency challenges where available, and a counterpetition asserting the respondent's own grounds, property/separate-property claims, custody and support requests, and prayer for relief — sized to the controlling state's dissolution statute and response deadline."
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
  - divorce
  - family-law
  - response
  - counterpetition
  - pleading
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_divorce_petition_complaint_drafter.md
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
  - domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md
  - domain-legal/litigation/legal_answer_with_affirmative_defenses.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
---

**Purpose:** Draft a timely response to a dissolution petition that admits, denies, or pleads lack of knowledge to each allegation, raises available defenses and jurisdictional challenges, and—where the respondent seeks affirmative relief—asserts a counterpetition. Output is a captioned, filing-ready pleading conformed to the controlling state and the response deadline.

**When to use:** Responding to a served dissolution/legal-separation/annulment petition; asserting the respondent's own grounds and property/custody/support claims; challenging residency, jurisdiction, or venue.

---

## Your Input

- **Jurisdiction:** [State; county; court; local rules]
- **Property regime:** [Community / equitable distribution]
- **The petition:** [Copy or paragraph-numbered summary of every allegation in the petition]
- **Service & deadline:** [Date served; response/answer deadline; default risk]
- **Respondent's position per allegation:** [Admit / deny / lack knowledge for each numbered paragraph]
- **Defenses available:** [Residency/jurisdiction defect; improper venue; existing marriage validity issue; statute issues]
- **Counterpetition relief:** [Respondent's grounds, separate-property claims, custody/parenting requests, support requests, fees, name restoration]
- **Children & UCCJEA:** [Respondent's UCCJEA position; any competing proceeding]
- **Required forms:** [State response form, UCCJEA declaration, fee waiver]

---

## Constraints

**Must:**
- Confirm the **response deadline** and flag default risk if it is near or passed.
- Respond to **each numbered allegation** with admit / deny / insufficient knowledge; do not leave allegations unaddressed (unanswered allegations may be deemed admitted).
- Raise **jurisdiction, residency, and venue challenges** only where a good-faith basis exists; these may be waived if not timely raised.
- Where the respondent seeks affirmative relief, include a **counterpetition** with its own grounds, allegations, and prayer.
- Include **UCCJEA allegations** in the counterpetition where children are involved.
- Use the **controlling state's response/counterpetition format** and terminology.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied statutes, deadlines, or facts.

**Must Not:**
- Invent the response deadline, statutory citations, or facts.
- Deny allegations the respondent has confirmed true, or admit allegations that are contested, without instruction.
- Raise frivolous jurisdictional challenges (MRPC 3.1).
- Omit a counterpetition where affirmative relief (custody, support, property, fees) is sought — relief generally requires a request.
- Disclose a protected party's confidential address.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Caption & deadline.** Mirror the petition's caption; state the response deadline and default posture.
2. **Paragraph responses.** For each numbered allegation: admit, deny, or state lack of sufficient knowledge.
3. **Affirmative defenses.** Plead available defenses (residency/jurisdiction/venue defects, validity of marriage, others) with the factual basis.
4. **Counterpetition — jurisdiction & grounds.** Allege respondent's residency basis (if independent), grounds, marriage facts.
5. **Counterpetition — children/UCCJEA.** Allege children, residence history, custody/parenting requests.
6. **Counterpetition — property & support.** Assert separate-property claims, division request, spousal/child support, fees.
7. **Prayer for relief.** Enumerate all affirmative relief sought.
8. **Verification & signature; attachments.**

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}

In re the Marriage of {PETITIONER} and {RESPONDENT}     Case No. {____}

RESPONSE TO PETITION AND COUNTERPETITION FOR {DISSOLUTION / LEGAL SEPARATION}

RESPONSE
Respondent answers the Petition as follows:
1. {Admit / Deny / Lacks sufficient knowledge and therefore denies} the allegations of Paragraph 1.
2. {…}
{continue for every numbered paragraph}

AFFIRMATIVE DEFENSES
First Defense — {e.g., Petitioner fails to meet the durational residency requirement of {statute [CITE: …]} because {facts}}.
Second Defense — {improper venue / other}.

COUNTERPETITION
Respondent, as Counter-Petitioner, alleges:
1. RESIDENCY & JURISDICTION. {basis [CITE: …]}
2. MARRIAGE. {date/place; separation date}
3. GROUNDS. {statutory ground [CITE: …]}
4. CHILDREN & UCCJEA. {children; residence history; custody/parenting requested}
5. PROPERTY & DEBTS. {separate-property claims; division requested}
6. SUPPORT. {spousal / child support requested}

WHEREFORE, Counter-Petitioner prays the Court: {a–h relief enumerated as in a petition}.

{Verification/declaration as required}
{Attorney block / self-represented}
Attachments: {Response form; UCCJEA declaration; [confidential address request]}
```

---

## Verification

- [ ] Response deadline confirmed; default risk flagged if applicable.
- [ ] Every numbered allegation answered (admit/deny/insufficient knowledge).
- [ ] Affirmative defenses pleaded only with a good-faith basis.
- [ ] Jurisdiction/residency/venue challenges raised timely where available.
- [ ] Counterpetition included where affirmative relief is sought, with grounds and prayer.
- [ ] UCCJEA allegations present in the counterpetition when children are involved.
- [ ] Verification/declaration and signature block included; mandatory attachments listed.
- [ ] No invented deadlines, statutes, or facts; confidential address protected.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Leaving petition allegations unanswered | Respond to every numbered paragraph; unanswered allegations may be deemed admitted |
| Seeking custody/support/property in argument but not pleading a counterpetition | Affirmative relief requires a counterpetition/request |
| Raising a residency/jurisdiction challenge with no basis | Plead only good-faith defenses (MRPC 3.1); frivolous challenges risk sanctions |
| Waiving a jurisdiction/venue defense by not raising it timely | Raise threshold defenses in the first responsive pleading |
| Admitting contested allegations or denying confirmed ones | Follow the respondent's instructions per paragraph |
| Omitting UCCJEA allegations from the counterpetition | Include residence history and custody claims to invoke custody jurisdiction |
| Missing the response deadline / default | Confirm and calendar the deadline; flag default risk prominently |
| Disclosing a protected party's address | Use the confidential-address procedure |
| Inventing the deadline or statutory citations | Use [NEED]/[CITE] placeholders |
| Using another state's response terminology | Conform to the controlling state's pleading format |
