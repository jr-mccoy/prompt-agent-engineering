---
title: "Unauthorized Practice Jurisdictional Assessment — Cross-Border, Remote, and In-House Practice"
category: legal/ethics-professional-conduct
description: "Assess unauthorized-practice-of-law (UPL) and multijurisdictional-practice risk for a lawyer or legal team working across jurisdictions: map where the lawyer is physically located, where the client and matter sit, and which tribunal is involved; apply each host jurisdiction's supplied version of MRPC 5.5 and its pro hac vice, in-house registration, foreign-lawyer, and remote-practice rules; and identify the authorization path (temporary-practice safe harbor, admission, registration, association with local counsel) for each activity."
techniques:
  - DS-01
  - CM-03
  - QA-04
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - ethics
  - professional-responsibility
  - unauthorized-practice
  - multijurisdictional-practice
  - pro-hac-vice
  - in-house-counsel
  - remote-practice
updated: "2026-09-24"
reasoning:
  styles: [analytic, classificatory, rule_application]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [structured, matrix]
  user_role: [attorney, in_house_counsel, firm_general_counsel]
related_prompts:
  - domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
  - domain-legal/in-house-legalops/legal_legal_intake_triage_router.md
---

# Unauthorized Practice Jurisdictional Assessment

**Objective:** Decide, activity by activity, whether a lawyer (or a team including non-admitted lawyers or foreign lawyers) may lawfully perform the planned legal work in each jurisdiction the work touches, and if not, which authorization path fixes it. The assessment separates three location facts that UPL rules turn on — where the lawyer sits, where the client and legal issue are, and which tribunal is involved — applies each host jurisdiction's supplied multijurisdictional-practice rule and its admission, registration, and pro hac vice rules, and produces an authorization plan with owners and deadlines.

**When to use:**
- A lawyer admitted in one jurisdiction will advise a client, negotiate, or appear in another.
- A lawyer is working remotely from a jurisdiction where they are not admitted (relocation, extended stay, fully remote role).
- A company hires in-house counsel who will be based in a jurisdiction where they are not admitted, or a foreign-qualified in-house lawyer.
- A litigation team needs pro hac vice admission, or an arbitration or agency proceeding involves non-admitted counsel.
- A legal-services product, legal-operations team, or non-lawyer staff might be engaged in the practice of law.

**Distinct from:**
- `domain-legal/research/legal_jurisdiction_split_analysis.md` — how courts in different jurisdictions decide a substantive legal question; this prompt concerns the lawyer's authority to practise.
- `domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md` — conflicts of interest, not authorization to practise.
- `domain-legal/personal-self-advocacy/` and `domain-written-advocacy/` — non-lawyers acting for themselves; self-representation is not UPL.

---

## Your Input

- **Lawyer(s):** [Name/role; jurisdictions of admission and status (active, inactive); foreign qualifications]
- **Physical location(s):** [Where each lawyer will actually work, and for how long; frequency of travel]
- **Client:** [Identity; employer relationship if in-house; client's locations]
- **Planned activities:** [Advice, drafting, negotiation, court or agency appearance, arbitration, mediation, supervision of others, marketing / holding out]
- **Legal issues and governing law:** [Which jurisdiction's law, including federal law or foreign law]
- **Tribunal(s):** [Court, agency, arbitral forum, and location]
- **Rules text supplied:** [Each host jurisdiction's version of Rule 5.5 and comments; pro hac vice rule; in-house counsel registration rule; foreign-lawyer rules; any remote-practice ethics opinion or rule. Anything not supplied is marked `[VERIFY]`.]
- **Firm or company structure:** [Offices, whether the lawyer is held out as practising in a jurisdiction (letterhead, website, signature block)]

---

## Constraints

**Must:**
- Build a location grid for each activity: lawyer's physical location × client location × issue's governing law × tribunal.
- Apply each host jurisdiction's **supplied** version of the multijurisdictional-practice rule; the ABA Model Rule is a structure, not the governing text.
- For each activity, identify the authorization path: admitted; temporary-practice safe harbor (and which one — associated with local counsel, related to a pending or reasonably anticipated proceeding, arbitration or mediation, or arising out of home-jurisdiction practice — as the supplied text defines them); in-house / employer-client authorization; federal-law or tribunal-specific authorization; registration; pro hac vice; or none.
- Distinguish **temporary** from **systematic and continuous presence**, and address holding out (letterhead, bios, signature blocks, email footers).
- For in-house counsel, check registration requirements, limits on appearing in court, pro bono permissions, and whether advice to the employer's affiliates or employees is covered.
- For pro hac vice, list the requirements in the supplied rule (local counsel association, fees, disclosure of prior admissions, limits on number of appearances) and the timing.
- Flag supervision issues where non-admitted lawyers or non-lawyers work under an admitted lawyer.

**Must Not:**
- Invent rule text, ethics opinions, registration deadlines, pro hac vice limits, or case law. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[NEED HOLDING: ...]`, `[VERIFY: {jurisdiction} {rule}]`.
- Assume that because a jurisdiction adopted "Rule 5.5," its safe harbors match the Model Rule.
- Treat remote work from a jurisdiction as automatically permitted or automatically prohibited; apply the supplied rule or opinion, or mark `[VERIFY]`.
- Conclude that advising only on home-jurisdiction or federal law is always safe without checking the host jurisdiction's text and the holding-out analysis.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Rule inventory.** For each jurisdiction touched, list the rules supplied and the rules to verify.
2. **Location grid.** One row per activity with the four location facts.
3. **Activity analysis.** For each row, apply the host jurisdiction's rule: is this the practice of law there? Is the lawyer admitted? If not, which authorization path applies, and are its conditions met (quote)?
4. **Presence and holding-out analysis.** Temporary vs systematic and continuous; marketing, signatures, and office designations.
5. **In-house and foreign-lawyer analysis** where applicable.
6. **Tribunal-specific authorization.** Pro hac vice, agency practice rules, arbitration rules.
7. **Authorization plan.** Each gap → fix (admission, registration, pro hac vice, local-counsel association, restructure the activity, change holding out) → owner → deadline or `[VERIFY]` lead time.
8. **Residual-risk statement.** Remaining uncertainty and its consequences (discipline in home jurisdiction, fee forfeiture, void appearance), with probability language.

---

## Output Format

```markdown
# UPL / Multijurisdictional Practice Assessment — {Lawyer or team} — {Engagement}
**Confidential**

## 1. Bottom Line
{Activities cleared; activities needing authorization; activities to restructure or stop}

## 2. Rules Inventory
| Jurisdiction | Rule | Supplied? | Departure from Model Rule noted |
|---|---|---|---|

## 3. Location Grid and Activity Analysis
| Activity | Lawyer location | Client location | Governing law | Tribunal | Admitted? | Authorization path (quoted condition) | Conditions met? |
|---|---|---|---|---|---|---|---|

## 4. Presence and Holding-Out
## 5. In-House / Foreign-Lawyer Issues
## 6. Tribunal-Specific Authorization
## 7. Authorization Plan
| Gap | Fix | Owner | Deadline / lead time |
|---|---|---|---|
## 8. Residual Risk
## 9. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** A lawyer admitted only in State A accepts an in-house role with a company headquartered in State B and will work fully remotely from her home in State C. She will advise the company on State B and federal employment law and will attend a State B state-court hearing. The user supplied State B's Rule 5.5 and in-house registration rule, and State B's pro hac vice rule; nothing for State C.

**Output (excerpt):**

| Activity | Lawyer location | Client location | Governing law | Tribunal | Admitted? | Authorization path | Conditions met? |
|---|---|---|---|---|---|---|---|
| Advice to employer on State B employment law | State C | State B | State B / federal | — | No (B, C) | State B in-house provision (quoted from supplied Rule 5.5) | Only if registered under the supplied registration rule → **Not yet** |
| Same advice, analyzed from State C | State C | State B | State B / federal | — | No | `[VERIFY: State C's Rule 5.5 and any remote-practice rule or opinion]` | **Unknown** |
| State B court hearing | State B (travel) | State B | State B | State B trial court | No | In-house provision in the supplied text excludes court appearances → pro hac vice under the supplied rule | Requires local-counsel association and motion → **Not yet** |

- **Holding out:** Company website lists her as "Employment Counsel, [State B city]" → implies a State B office; recommend listing admission as "Admitted in State A only; registered in-house counsel in State B" once registration is complete.
- **Authorization plan:** File State B in-house registration (owner: GC; lead time `[VERIFY]`); verify State C position before start date; retain State B local counsel and file pro hac vice for the hearing.

---

## Verification

- [ ] Jurisdiction lock: each activity analyzed under the host jurisdiction's supplied rule text; unsupplied rules marked `[VERIFY]`.
- [ ] Citation discipline: no invented rules, opinions, deadlines, or cases.
- [ ] Location grid covers lawyer location, client location, governing law, and tribunal for every activity.
- [ ] Authorization path and its quoted conditions stated for each non-admitted activity.
- [ ] Temporary vs systematic presence and holding out analyzed.
- [ ] In-house limits (court appearances, affiliates, pro bono) addressed where relevant.
- [ ] Authorization plan has owners and deadlines.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Analyzing only the client's jurisdiction and ignoring where the lawyer physically sits | Location grid requires lawyer location for every activity |
| Assuming the host state's Rule 5.5 matches the Model Rule | Quote the supplied state text; note departures |
| "Federal-law practice is always permitted anywhere" | Check the host rule's text and the holding-out analysis |
| Treating in-house registration as permitting court appearances | Check the supplied registration rule's limits; pro hac vice is usually a separate path |
| Declaring remote work permitted or forbidden from memory | Apply the supplied rule or opinion; otherwise `[VERIFY]` |
| Ignoring website bios, letterhead, and signature blocks | Holding out is analyzed separately and can create exposure on its own |
| Missing lead times for registration or pro hac vice | List each fix with a deadline or `[VERIFY]` lead time |
