---
title: "Domestic Violence Protective Order Petition"
category: legal/divorce
description: "Draft a petition for a domestic-violence protective/restraining order with the supporting affidavit: establish the qualifying relationship, plead the statutory abuse acts with dated specific incidents, request the available relief (no-contact, stay-away, residence exclusion, temporary custody and parenting-time restrictions, support, firearm surrender), and address ex parte/emergency vs. noticed-hearing procedure and confidential-address protection — sized to the controlling state's DV statute."
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
  - protective-order
  - domestic-violence
  - safety
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
  - domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md
  - domain-legal/custody/legal_temporary_and_emergency_custody_motion.md
  - domain-legal/custody/legal_supervised_visitation_and_safety_plan.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
---

**Purpose:** Draft a domestic-violence protective/restraining-order petition and supporting affidavit that establish the qualifying relationship, plead the statutory acts of abuse with specific dated incidents, and request the full range of available protective relief — handling both the emergency/ex parte posture and the noticed hearing, and protecting the petitioner's confidential address. Output is a filing-ready petition package, not a memo.

**When to use:** A client needs protection from an intimate partner, spouse, co-parent, or household member; DV surfaces during a divorce/custody intake; seeking emergency relief, temporary custody, residence exclusion, or firearm surrender.

---

## Your Input

- **Jurisdiction:** [State; county; court; the state's DV statute, qualifying relationships, and available relief `[CITE: …]`]
- **Parties:** [Petitioner; respondent; qualifying relationship (spouse, former spouse, dating, co-parent, household member)]
- **Children:** [Names/ages; whether protection or temporary custody for them is sought; existing orders]
- **Incidents:** [Dated, specific acts — physical harm, threats, stalking, harassment, property damage, coercion — with locations, injuries, witnesses, police reports, photos, messages]
- **Imminent danger facts:** [Basis for emergency/ex parte relief]
- **Relief sought:** [No-contact; stay-away (distance, locations); residence exclusion; temporary custody/parenting restrictions; support; firearm surrender; possession of pets/essentials; no-cancel-utilities]
- **Safety/confidentiality:** [Need for address confidentiality; safe contact method; safety plan in place]
- **Firearms:** [Whether the respondent possesses firearms]

---

## Constraints

**Must:**
- Identify the state's **DV statute**, the **qualifying relationships**, and the **defined acts of abuse**; confirm the parties' relationship qualifies `[CITE: …]`.
- Plead **specific, dated incidents** tied to the statutory acts — not conclusory labels — with evidence references (police reports, photos, messages, medical records, witnesses).
- Distinguish **ex parte/emergency (temporary)** relief (immediate, based on imminent danger) from relief available only after a **noticed hearing**, and request the correct procedure.
- Request the **full available relief**: no-contact, stay-away, residence exclusion, **temporary custody and parenting-time restrictions in the children's best interests**, support, **firearm surrender/prohibition**, and protection of pets/essentials.
- Use the **confidential-address procedure** and a safe contact method; do not disclose the petitioner's location.
- Coordinate with any pending **divorce/custody** case (the protective order can set the temporary custody status quo).
- Note **service, duration, and renewal**, and the firearm-surrender enforcement mechanism.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied statutes or facts.

**Must Not:**
- Plead conclusory "abuse" without specific incidents and dates.
- Disclose the petitioner's confidential address or safe location.
- Request relief the statute does not authorize, or seek the order for tactical advantage absent a genuine safety basis (MRPC 3.1).
- Overstate or fabricate incidents — accuracy is essential to credibility and to the client's safety and case.
- Invent the statute, qualifying relationships, or available relief.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Relationship & jurisdiction.** Confirm the qualifying relationship and the court's authority `[CITE: …]`.
2. **Incident affidavit.** Draft the supporting affidavit with numbered, dated incidents tied to statutory acts, with evidence references and any injuries/witnesses.
3. **Imminent danger / ex parte basis.** State the basis for emergency relief if sought.
4. **Relief requested.** Enumerate each protective provision (no-contact, stay-away, residence exclusion, temporary custody/parenting, support, firearm surrender, pets/essentials).
5. **Children.** Request temporary custody and parenting-time terms consistent with the children's safety and best interests; coordinate supervised visitation if appropriate.
6. **Confidentiality & safety.** Invoke the confidential-address procedure and a safe contact method.
7. **Procedure.** Address ex parte issuance, the noticed-hearing date, service on the respondent, duration, renewal, and firearm-surrender enforcement.
8. **Coordination.** Note interplay with any pending divorce/custody matter.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}
{PETITIONER} v. {RESPONDENT}     Case No. {____}

PETITION FOR DOMESTIC VIOLENCE {PROTECTIVE / RESTRAINING} ORDER

1. RELATIONSHIP & JURISDICTION. Petitioner and Respondent are {qualifying relationship} within {statute [CITE: …]}. The Court has jurisdiction.

2. CHILDREN. {Names/ages}; Petitioner requests {temporary custody / parenting-time restrictions / inclusion in the order}.

3. ACTS OF ABUSE (see Affidavit). Respondent committed the following acts within {statute [CITE: …]}: {summary referencing affidavit paragraphs}.

4. IMMINENT DANGER (ex parte). {Basis for emergency relief, if sought}.

5. RELIEF REQUESTED. Petitioner requests an order that Respondent:
   a. Have no contact with Petitioner {and children} by any means;
   b. Stay at least {distance} away from Petitioner's {residence/work/school/children's school};
   c. Move out of and stay away from the residence at {[CONFIDENTIAL]};
   d. {Temporary custody to Petitioner; parenting time {supervised/suspended} pending hearing};
   e. Pay {temporary support};
   f. Surrender all firearms and not possess firearms per {statute [CITE: …]};
   g. Not damage property or cancel utilities/insurance; allow retrieval of {pets/essentials}.

AFFIDAVIT OF {PETITIONER}
I declare under penalty of perjury: 1. {Date — specific act, location, injury, witness, evidence}. 2. {…} {numbered, dated incidents}.

Petitioner's address is confidential and filed separately under {procedure}. Safe contact: {method}.

{Proposed Temporary (Ex Parte) Order; Notice of Hearing on {date}; Service instructions}
```

---

## Verification

- [ ] Qualifying relationship and court authority confirmed under the DV statute.
- [ ] Supporting affidavit pleads specific, dated incidents tied to statutory acts with evidence references.
- [ ] Ex parte/emergency basis stated where immediate relief is sought; noticed-hearing procedure addressed.
- [ ] Full available relief requested (no-contact, stay-away, residence exclusion, custody/parenting, support, firearm surrender, pets/essentials).
- [ ] Children's temporary custody/parenting terms tied to safety and best interests.
- [ ] Confidential-address procedure used; safe contact method given.
- [ ] Service, duration, renewal, and firearm-surrender enforcement addressed.
- [ ] No conclusory abuse allegations; no fabricated/overstated incidents; no invented statute or relief.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Pleading "abuse" conclusorily | Plead specific, dated incidents tied to the statutory acts with evidence |
| Disclosing the petitioner's address | Use the confidential-address procedure; never reveal the safe location |
| Requesting relief the statute does not authorize | Limit to the statute's available protective provisions [CITE] |
| Confusing ex parte and noticed-hearing relief | Match each request to the correct procedural posture |
| Omitting firearm surrender where warranted | Request surrender/prohibition and the enforcement mechanism |
| Ignoring children's temporary custody/safety | Request temporary custody and parenting restrictions tied to safety |
| Overstating or fabricating incidents | Keep the affidavit accurate; credibility and safety depend on it |
| Seeking the order purely for divorce leverage | Require a genuine safety basis (MRPC 3.1) |
| Inventing the DV statute or qualifying relationships | Use [CITE]/[NEED] placeholders |
| Failing to coordinate with the pending divorce/custody case | Note interplay; the order can set the temporary custody status quo |
