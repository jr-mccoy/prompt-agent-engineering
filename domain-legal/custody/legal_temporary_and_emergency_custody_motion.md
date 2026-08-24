---
title: "Temporary and Emergency Custody Motion Drafter"
category: legal/custody
description: "Draft a motion for temporary custody orders or, where a child faces immediate risk, an ex parte emergency custody motion: state the standard for temporary vs. ex parte relief, plead the specific facts of harm or risk (abuse, neglect, abduction risk, substance endangerment), preserve or alter the status quo with justification, address UCCJEA (including temporary emergency jurisdiction), and supply the supporting declaration and proposed order — sized to the controlling state and local rules."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - emergency-custody
  - temporary-orders
  - ex-parte
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_custody_petition_or_motion_drafter.md
  - domain-legal/custody/legal_supervised_visitation_and_safety_plan.md
  - domain-legal/divorce/legal_domestic_violence_protective_order_petition.md
  - domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md
---

**Purpose:** Draft a temporary-custody motion or, where a child faces immediate danger, an ex parte emergency custody motion that meets the applicable standard, pleads specific facts of harm or risk, and supplies the declaration and proposed order. Output is a filing-ready motion package distinguishing the high bar for ex parte relief from ordinary temporary orders.

**When to use:** A child faces immediate risk (abuse, neglect, abduction/flight risk, substance endangerment); the status quo must be set or preserved pending a hearing; responding to the other parent's emergency motion.

---

## Your Input

- **Jurisdiction:** [State; county; court; the standard for temporary and ex parte custody relief; local ex parte procedure `[CITE: …]`]
- **Posture:** [Noticed temporary-orders motion / ex parte emergency motion / response to the other side's motion]
- **Child(ren):** [Names, ages, current location and caregiver, school]
- **Risk facts:** [Specific, dated facts of harm or imminent risk — abuse, neglect, substance use, threats, abduction/flight indicators, with evidence]
- **Status quo:** [The current arrangement and what change is sought and why]
- **UCCJEA facts:** [Home state; child's presence; any emergency-jurisdiction basis; existing orders]
- **Notice:** [Whether notice to the other party is possible/required, or why ex parte without notice is justified]
- **Relief sought:** [Temporary legal/physical custody, supervised or suspended parenting time, no-removal/travel restriction, surrender of passports]

---

## Constraints

**Must:**
- State the **applicable standard**: ordinary temporary orders vs. the **higher ex parte standard** (immediate/irreparable harm; why notice cannot be given) `[CITE: …]`.
- Plead **specific, dated facts** of harm or imminent risk tied to the standard — not conclusory fear.
- Justify any **change to the status quo**; absent immediate risk, courts preserve the existing arrangement pending hearing.
- Address **UCCJEA**, including **temporary emergency jurisdiction** (child present + emergency) and the duty to defer to the home state and set an early hearing `[CITE: …]`.
- Address **notice**: comply with the ex parte notice rule or state why notice without the order would risk the child (e.g., abduction).
- Request **proportionate relief** with an early **hearing date** so the order is genuinely temporary.
- Include the **supporting declaration** (personal-knowledge facts) and a **proposed order** with a return/hearing date.
- For abduction/flight risk, include **travel/passport** safeguards.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Seek ex parte relief without immediate-harm facts and a notice justification (these are scrutinized and sanctionable if abused).
- Use an emergency motion to gain tactical advantage absent genuine risk (MRPC 3.1).
- Treat temporary emergency jurisdiction as a permanent custody basis.
- Plead conclusory danger without specific incidents.
- Invent the standard, the ex parte procedure, or UCCJEA application.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Standard.** State the temporary vs. ex parte standard and which applies `[CITE: …]`.
2. **Risk facts.** Plead specific, dated facts of harm/risk tied to the standard, with evidence references.
3. **Status quo & change.** State the current arrangement and justify the requested change.
4. **UCCJEA.** Confirm jurisdiction; if relying on temporary emergency jurisdiction, address the child's presence, the emergency, and home-state deferral.
5. **Notice.** Address the notice requirement or the justification for proceeding without notice.
6. **Relief & hearing.** Request proportionate temporary relief and an early hearing date; add travel/passport safeguards for flight risk.
7. **Declaration & proposed order.** Draft the personal-knowledge declaration and the proposed order with the return date.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}
{Caption}     Case No. {____}

{EX PARTE EMERGENCY / TEMPORARY} MOTION FOR CHILD CUSTODY ORDERS

I. STANDARD. {Temporary-orders standard / ex parte immediate-harm standard} [CITE: …].

II. FACTS OF HARM / RISK. {Numbered, dated specific incidents with evidence references}.

III. STATUS QUO & REQUESTED CHANGE. Current arrangement: {…}; requested change and justification: {…}.

IV. UCCJEA. Jurisdiction: {basis}; {if emergency: child present + emergency; home state {state}; early hearing to defer}.

V. NOTICE. {Notice given / notice cannot be given because {abduction/harm risk}}.

VI. RELIEF & HEARING. Movant requests: temporary {legal/physical} custody to {}; {supervised/suspended} parenting time for {}; {no-removal / travel restriction / passport surrender}. A hearing is requested on {date}.

DECLARATION OF {MOVANT}. I declare under penalty of perjury: {numbered personal-knowledge facts}.

[PROPOSED] {EX PARTE} ORDER. The Court orders {…}; hearing set for {date}; service by {…}.
```

---

## Verification

- [ ] Correct standard stated (temporary vs. ex parte) and applied.
- [ ] Specific, dated harm/risk facts pleaded and tied to the standard.
- [ ] Status-quo change justified by immediate risk; otherwise preservation favored.
- [ ] UCCJEA addressed, including temporary emergency jurisdiction and home-state deferral.
- [ ] Notice requirement satisfied or justified for proceeding without notice.
- [ ] Proportionate relief with an early hearing date; travel/passport safeguards for flight risk.
- [ ] Supporting declaration and proposed order with return date included.
- [ ] No conclusory danger; no invented standard or procedure; no tactical misuse.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Seeking ex parte relief without immediate-harm facts | Plead specific, dated risk facts and the notice justification; ex parte is scrutinized |
| Conclusory "the child is in danger" | Provide dated incidents and evidence tied to the standard |
| Changing the status quo without immediate risk | Absent risk, request preservation pending a noticed hearing |
| Treating emergency jurisdiction as permanent | It is temporary; set an early hearing and defer to the home state |
| Skipping the notice analysis | Comply with the notice rule or justify proceeding without notice |
| No early hearing date | Request a prompt return date so the order is genuinely temporary |
| Ignoring abduction/flight safeguards | Add travel restrictions and passport surrender where flight risk exists |
| Using the motion for tactical advantage | Require a genuine risk basis (MRPC 3.1) |
| Inventing the ex parte standard or procedure | Use [CITE]/[NEED] placeholders |
| Omitting the supporting declaration | Personal-knowledge declaration is required for emergency relief |
