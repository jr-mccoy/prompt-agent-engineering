---
title: "Custody Petition / Motion Drafter"
category: legal/custody
description: "Draft an initial custody petition or motion (within a divorce/parentage case or as a standalone): UCCJEA jurisdiction allegations and declaration, the legal and physical custody and parenting-time sought, the best-interests basis tied to the state's factors, decision-making allocation, child support request, and the prayer for relief — sized to the controlling state's statute and local rules."
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
  - custody
  - family-law
  - petition
  - pleading
  - parenting-time
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_temporary_and_emergency_custody_motion.md
  - domain-legal/custody/legal_paternity_parentage_establishment_and_custody.md
---

**Purpose:** Draft a filing-ready custody petition or motion that invokes UCCJEA jurisdiction, states the legal and physical custody and parenting time sought, ties the request to the state's best-interests factors, and requests child support and ancillary relief. Output is a captioned pleading conformed to the controlling state and local rules — not a memo.

**When to use:** Opening a custody case (standalone, or within divorce or parentage); seeking an initial custody and parenting-time order; establishing decision-making and a residential schedule.

---

## Your Input

- **Jurisdiction:** [State; county; court; whether standalone, in a divorce, or in a parentage action; local rules]
- **Parties & child(ren):** [Parents/parties; children's names, ages; current residence and schedule]
- **UCCJEA facts:** [Child's residence history for the lookback; existing orders; other proceedings]
- **Custody sought:** [Legal custody (joint/sole + decision categories); physical custody and the proposed parenting schedule]
- **Best-interests basis:** [The facts supporting the request under the state's factors]
- **Child support:** [Request and the guideline inputs]
- **Ancillary relief:** [Transportation/exchanges; communication; holiday schedule; right of first refusal; fees]
- **Safety facts:** [Any DV/abuse/substance issues affecting the request]
- **Required attachments:** [UCCJEA declaration, parenting plan, child-support worksheet, local forms]

---

## Constraints

**Must:**
- Plead the **UCCJEA jurisdictional allegations** and attach the **UCCJEA declaration** (residence history, other proceedings, custody claimants).
- State the **legal custody** (decision-making) and **physical custody** sought, distinctly, with the **proposed parenting schedule**.
- Tie the request to the state's **best-interests factors** `[NEED FACTOR LIST: …]` `[CITE: …]` without reciting facts not supplied.
- Request **child support** and reference the guideline worksheet.
- Include **ancillary terms** (exchanges, communication, holidays, right of first refusal) or incorporate a proposed parenting plan.
- Where safety is implicated, request appropriate **protective conditions** (supervised parenting time, no-contact, exchange safeguards) and coordinate with any protective order.
- Use the **controlling state's pleading format** and the correct case type (standalone vs. within divorce/parentage).
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Omit the UCCJEA allegations/declaration (it can defeat custody jurisdiction).
- Conflate legal and physical custody.
- Plead best-interests conclusions without a factual basis.
- Invent the state's factors, statutes, or local forms.
- Request relief the court cannot grant in the chosen case type.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Caption & case type.** Court, parties, case number; identify standalone/divorce/parentage posture.
2. **Jurisdiction (UCCJEA).** Allege the jurisdictional basis and reference the attached declaration.
3. **Children & current arrangement.** Identify the children and the existing schedule/order.
4. **Custody requested.** State legal-custody allocation (with decision categories) and physical custody plus the parenting schedule.
5. **Best-interests basis.** Tie the request to the state's factors with the supplied facts.
6. **Child support.** Request support and reference the worksheet.
7. **Ancillary & safety terms.** Exchanges, communication, holidays, right of first refusal; protective conditions if needed.
8. **Prayer & attachments.** Enumerate relief; list mandatory attachments.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}
{In re the {Marriage/Parentage} of … / {Petitioner} v. {Respondent}}     Case No. {____}

{PETITION / MOTION} FOR CHILD CUSTODY AND PARENTING TIME

1. JURISDICTION (UCCJEA). The Court has jurisdiction under {state UCCJEA [CITE: …]}. The children's residence history and other-proceeding information are set out in the attached UCCJEA Declaration.

2. CHILDREN. {Names/DOB}; current arrangement: {…}; existing order: {…}.

3. CUSTODY REQUESTED.
   - Legal custody: {joint/sole to {}}; decision-making over {education/health/religion}: {…}.
   - Physical custody and parenting time: {schedule}.

4. BEST INTERESTS. The requested arrangement serves the children's best interests under {state factors [CITE: …] [NEED FACTOR LIST]} because {facts}.

5. CHILD SUPPORT. {Movant} requests child support per guideline (worksheet attached).

6. ANCILLARY & SAFETY TERMS. {Exchanges / communication / holidays / right of first refusal}; {protective conditions: supervised time / exchange safeguards}.

WHEREFORE, {Movant} requests the Court: (a) award legal and physical custody as set forth; (b) adopt the proposed parenting plan/schedule; (c) order guideline child support; (d) {ancillary relief}; (e) grant such other relief as is just.

Attachments: UCCJEA Declaration; Proposed Parenting Plan; Child-Support Worksheet; {local forms}.
{Verification/declaration; attorney or self-represented block}
```

---

## Verification

- [ ] UCCJEA allegations pleaded and declaration attached.
- [ ] Legal and physical custody stated distinctly with a proposed schedule.
- [ ] Request tied to the state's best-interests factors with supplied facts only.
- [ ] Child support requested with worksheet referenced.
- [ ] Ancillary terms and any protective/safety conditions included.
- [ ] Correct case type and pleading format; mandatory attachments listed.
- [ ] No invented factors, statutes, or forms; no relief beyond the case type.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Omitting the UCCJEA allegations/declaration | Always plead jurisdiction and attach the declaration |
| Conflating legal and physical custody | State decision-making and residential time separately |
| Pleading best-interests conclusions without facts | Tie the request to the state's factors using supplied facts only |
| Forgetting the child-support request/worksheet | Request guideline support and reference the worksheet |
| Ignoring safety issues in the request | Add supervised time/exchange safeguards; coordinate with any protective order |
| Requesting relief unavailable in the case type | Match relief to standalone/divorce/parentage posture |
| Inventing the state's factors or forms | Use [CITE]/[NEED] placeholders |
| Omitting ancillary terms (holidays, exchanges) | Include them or incorporate a proposed parenting plan |
| Using another state's pleading nomenclature | Conform to the controlling state's format |
| Failing to identify the existing order/arrangement | State the status quo so the requested change is clear |
