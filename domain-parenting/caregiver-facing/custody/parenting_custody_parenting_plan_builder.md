---
title: "Parenting Plan Builder (Court-Presentable)"
category: parenting/custody
description: "Build a complete, child-centered parenting plan document — residential schedule, holiday and vacation rotation, decision-making authority, communication rules, transportation and exchanges, and standard provisions — written in factual, neutral language a parent can use day-to-day and present to a mediator, guardian ad litem, or court. Not legal advice."
techniques:
  - DS-01
  - ST-03
  - ST-02
  - CM-01
  - QA-02
difficulty: advanced
intended_use: model-testing
tags:
  - parenting
  - custody
  - cross-age
  - parenting-plan
  - co-parenting
  - court-presentable
updated: "2026-06-01"
related_prompts:
  - domain-parenting/caregiver-facing/custody/parenting_custody_schedule_designer_by_age.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_holiday_vacation_schedule_builder.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_common_plan_provisions_explainer.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_special_needs_plan_addendum.md
---

**Purpose:** Help a parent assemble a complete parenting plan — the document that says where the children live and when, who decides what, and how the two parents coordinate — written so it works as a practical daily reference AND reads as a calm, factual, child-centered document a mediator, guardian ad litem (GAL), parenting coordinator, or court will take seriously. The output organizes the parent's own decisions and information; it does not argue, accuse, or invent legal standards.

**When to use:** Drafting a first parenting plan before mediation or filing; preparing a proposal to bring to the other parent or a mediator; consolidating a patchwork of informal arrangements into one written document; updating a plan as children age. Works for any custody arrangement (joint, primary-residential, etc.) and any family structure.

**When NOT to use:** You need to know what a court is likely to order, what the custody standard is in your state/country, or whether a term is enforceable → that is legal advice; take the draft to an attorney or mediator. There is a safety emergency, active abuse, or a protective-order situation → handle safety first (see Safety Block) and work through counsel, not a self-serve document.

---

## Safety Block

Stop and use a different pathway if:
- A child is being abused or is unsafe in either home → in the US, Childhelp National Child Abuse Hotline 1-800-422-4453; emergencies 911. Do not negotiate a schedule around an unsafe situation; document and route to CPS/law enforcement and your attorney.
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Exchange logistics and contact rules must be designed for safety first, usually with legal/advocate involvement — not drafted unilaterally. See `parenting_coparenting_with_unsafe_or_absent_parent.md`.
- A child is talking about not wanting to be alive, or you are worried about their mental health → 988 Suicide & Crisis Lifeline (US); pediatrician same-day.

This prompt is educational support for organizing your own decisions. It is not a substitute for clinical, safety, or legal services.

---

## Scope Boundary — Read First

This builds a **parent-authored document**. It is **not legal advice, a legal filing, or a substitute for an attorney, mediator, or your jurisdiction's custody law.** Custody standards, mandatory parenting-plan provisions, terminology (legal vs. physical custody, "parenting time," "conservatorship," "residence order"), and what a court will accept **vary by state and country and change over time.** Have an attorney or mediator review this draft before you rely on it, submit it, or sign it. This prompt will **not** invent statutes, predict what a court will decide, or tell you that a term is "enforceable" or "standard" — where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **The plan is for the children, not against the other parent.** Every section is framed around the children's stability, routine, and relationship with both parents. A plan that reads as an attack on the other parent undermines itself in front of a GAL or judge.
2. **Specific beats vague.** "Reasonable visitation" causes fights; "alternating weekends, Friday 6pm to Sunday 6pm" does not. A good plan removes ambiguity so neither parent has to interpret intent in the moment.
3. **Factual and neutral tone.** No characterizations of the other parent ("he is irresponsible"), no editorializing, no history-relitigating. Just who, what, when, where, how.
4. **Build for the predictable, name the process for the rest.** You cannot script every future event. Where you cannot fix a rule, fix a *process* for deciding (e.g., "disputes about activities go to mediation before court").
5. **Age-appropriate and revisable.** A plan for a toddler is not a plan for a teenager. Name a review cadence.
6. **You decide; this organizes.** The content is the parent's choices. This prompt structures them into a recognized format and pressure-tests them for gaps.

---

## Your Input

- **Children:** [names/initials, ages, school/grade]
- **Current living situation:** [who lives where now; what's working / not]
- **Custody arrangement you are proposing:** [joint, primary with one parent, etc. — in plain words]
- **Distance between homes / commute to school:**
- **Each parent's work schedule / availability:**
- **Special considerations:** [medical, disability, ADHD/autism, infant nursing, religious observance, language]
- **Conflict level with the other parent:** [low / moderate / high — affects communication & exchange design]
- **Existing orders or agreements:** [any current temporary order, mediation outcome — describe, don't assume legal effect]
- **What's contested vs. agreed:** [where the two of you already align, where you don't]
- **Audience for this draft:** [just for us / for mediation / to bring to my attorney]

---

## Constraints

**Must:**
- Frame every section around the children's needs and both parents' continued involvement.
- Use specific dates, times, and locations — no "reasonable" or "as agreed" without a fallback rule.
- Keep tone factual and neutral throughout; suitable to hand to a GAL or judge.
- Distinguish what's **agreed** from what's **proposed/contested**, and flag the contested items for mediation/counsel.
- Include a dispute-resolution process and a review cadence.
- Flag every legal concept with *confirm with counsel for your jurisdiction.*
- Note where the parent should fill in jurisdiction-specific requirements (this plan won't guess them).

**Must Not:**
- Characterize, accuse, diagnose, or disparage the other parent anywhere in the document.
- Invent legal standards, statutes, custody-percentage norms, or predict court outcomes.
- Assert that any term is "enforceable," "standard," or "what the court wants."
- Insert the children as messengers, spies, or decision-makers about adult matters.
- Produce inflammatory or strategic language designed to disadvantage the other parent.

---

## Instructions

### Stage 1 — Confirm Scope and Audience
Restate the arrangement the parent is proposing in plain language, confirm the audience (private / mediation / attorney), and flag anything in the inputs that is a legal question (route to counsel) versus a parenting decision (proceed).

### Stage 2 — Assemble the Plan, Section by Section
Work through the sections below. For each: draft the parent's stated choice in neutral language; where the parent hasn't decided, present 2–3 child-centered options with trade-offs; mark contested items clearly.

**A. Children & Purpose** — names/ages; a one-line, neutral purpose statement (e.g., "This plan sets out how [parent A] and [parent B] will share parenting of [children] so they have stable routines and a strong relationship with both parents").

**B. Decision-Making** — how major decisions get made (education, non-emergency medical, religion, extracurriculars): jointly, by domain, or by the residential parent for day-to-day. Define "major" vs. "day-to-day." Add an emergency clause (either parent may act in a true emergency and must notify the other promptly). *Legal vs. physical custody terminology — confirm with counsel.*

**C. Residential Schedule** — the regular week-to-week schedule with specific days and exchange times. If undecided, route to `parenting_custody_schedule_designer_by_age.md` and insert its output here.

**D. Holidays, School Breaks & Special Days** — rotation for holidays, birthdays, school breaks, summer. If undecided, route to `parenting_custody_holiday_vacation_schedule_builder.md` and insert its output here. State that the holiday schedule **supersedes** the regular schedule.

**E. Transportation & Exchanges** — who drives, where, when; exchange location; what travels with the child (clothes, devices, medication, comfort items, homework). For higher-conflict situations, route to `parenting_custody_exchange_and_transition_protocol.md`.

**F. Communication** — how the parents communicate (app, email, text), expected response time for non-emergencies, how the children contact the other parent during each parent's time, and a no-children-as-messengers rule.

**G. Standard Provisions** — name the common provisions the parent wants (e.g., right of first refusal, relocation/move-away notice, travel notice and consent, access to school/medical records, introducing new partners). Use `parenting_custody_common_plan_provisions_explainer.md` for plain-language definitions; flag each *confirm with counsel for your jurisdiction.*

**H. Children with Special Needs** — if applicable, route to `parenting_custody_special_needs_plan_addendum.md` and attach.

**I. Dispute Resolution** — the agreed process when parents disagree (e.g., direct discussion → mediation → then court as last resort). *Whether a court requires a specific process — confirm with counsel.*

**J. Review & Modification** — review cadence (e.g., yearly, and at each school-stage transition) and how either parent proposes a change. *How a plan is legally modified — confirm with counsel.*

### Stage 3 — Mark Agreed vs. Contested
Produce a short summary table separating items both parents already agree on from items still contested, so the parent (and a mediator) can focus on the open questions.

### Stage 4 — Tone & Court-Readiness Pass
Re-read the whole draft for any accusatory, characterizing, or strategic language and rewrite it to neutral. Confirm every legal concept carries the confirm-with-counsel flag.

---

## Output Format

```markdown
# Parenting Plan — [Children's initials]
Draft [version], [date]. Status: [private draft / for mediation / for attorney review]
NOT A LEGAL FILING. Subject to review by counsel/mediator and jurisdiction requirements.

## 1. Children & Purpose
[Children; neutral purpose statement.]

## 2. Decision-Making
- Major decisions (education / medical / religion / activities): [how decided]
- Day-to-day decisions: [residential parent]
- Emergencies: [either parent may act; must notify other]
- [Legal terminology note — confirm with counsel.]

## 3. Residential Schedule
[Specific week-to-week schedule with days + exchange times.]

## 4. Holidays, Breaks & Special Days
[Rotation table; supersedes regular schedule.]

## 5. Transportation & Exchanges
[Who / where / when / what travels with the child.]

## 6. Communication
[Parent-to-parent channel + response time; child-to-parent contact; no messengers.]

## 7. Standard Provisions
[Each selected provision in plain language + "confirm with counsel."]

## 8. Special-Needs Addendum
[Attached if applicable.]

## 9. Dispute Resolution
[Agreed process.]

## 10. Review & Modification
[Cadence + how to propose changes.]

---

## Agreed vs. Contested (working summary — not part of the plan itself)
| Item | Agreed | Contested → route to |
|---|---|---|
| ... | ✅ | mediation / counsel |

## Open questions for your attorney/mediator
- [Jurisdiction-specific items this draft could not resolve.]
```

---

## Verification

- [ ] Every section framed around the children, not against the other parent?
- [ ] All schedule items use specific days/times/locations (no bare "reasonable")?
- [ ] Tone is factual and neutral throughout — no characterizations of the other parent?
- [ ] Agreed vs. contested items separated?
- [ ] Dispute-resolution process and review cadence included?
- [ ] Every legal concept flagged *confirm with counsel for your jurisdiction*?
- [ ] No invented statutes, custody norms, or court-outcome predictions?
- [ ] Jurisdiction-specific gaps surfaced as open questions, not guessed?
- [ ] Emergency and communication clauses present?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Write "Dad is unreliable so he gets less time" | State the schedule neutrally; let the arrangement speak |
| Use "reasonable visitation as agreed" | Specify days, times, exchange points, and a fallback |
| Quote a statute or a custody percentage | Explain the concept plainly and flag "confirm with counsel" |
| Predict "the judge will give you primary" | Stay silent on outcomes; route prediction to an attorney |
| Bury contested items inside agreed ones | Separate agreed vs. contested explicitly |
| Make the child carry messages or choose between parents | No-messenger rule; adults coordinate adult matters |
| Add inflammatory history ("after everything he did") | Keep it to who/what/when/where; omit relitigating |
| Assume your state's required provisions | Flag jurisdiction gaps as questions for counsel |
| Treat the draft as final/binding | Label it a draft subject to mediator/attorney review |
| Script every contingency rigidly | Fix a rule where you can; fix a *process* where you can't |

---

## Adaptations

**By age band:**
- **0–3:** Shorter, more frequent contact; consistent caregiving routines; nursing/feeding logistics; minimize long separations from the primary attachment figure. Plan to revisit as the child's tolerance for longer blocks grows.
- **4–8:** Predictable weekly rhythm; a transition object that travels; school-day continuity; simple language if the plan is ever explained to the child.
- **9–12:** Build in the child's activities and friendships; some input on logistics (not on adult decisions); homework/device continuity across homes.
- **13–18:** More flexibility for the teen's schedule, job, and social life; the plan increasingly accommodates rather than dictates the teen's time; name how the teen's reasonable preferences are weighed (without making the teen the decider). *Whether a court weighs a teen's preference — confirm with counsel.*

**By situation/profile:**
- **High-conflict co-parent:** Maximize specificity; minimize discretion and required real-time coordination; use a parenting app and a neutral exchange point; pair with `parenting_custody_communication_log_template.md` and `parenting_coparenting_high_conflict_response_strategy.md`.
- **Long distance:** Larger blocks (school breaks/summer) plus a virtual-contact schedule; pair with `parenting_coparenting_long_distance_protocol.md`.
- **Child with ADHD/autism/medical needs:** Attach `parenting_custody_special_needs_plan_addendum.md`; prioritize routine continuity, medication/therapy continuity, and shared documentation.
- **Safety concerns:** Do not self-draft exchange/contact terms around an unsafe parent; see Safety Block and `parenting_coparenting_with_unsafe_or_absent_parent.md`; work through counsel/advocate.

---

## Cross-References

- `parenting_custody_schedule_designer_by_age.md` — build the residential schedule that drops into Section 3.
- `parenting_custody_holiday_vacation_schedule_builder.md` — build the rotation for Section 4.
- `parenting_custody_common_plan_provisions_explainer.md` — plain-language definitions for Section 7.
- `parenting_custody_special_needs_plan_addendum.md` — the addendum for Section 8.
- `parenting_custody_exchange_and_transition_protocol.md` — detailed, low-conflict exchange design for Section 5.
- `parenting_custody_communication_log_template.md` — records that support the plan over time.
- `parenting_custody_child_focused_proposal_articulator.md` — turn this plan into a child-centered proposal for mediation.
