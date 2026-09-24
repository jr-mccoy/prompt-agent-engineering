---
title: "Promotion Case Writer — The Manager's Packet, Mapped to the Next Level and Honest About Gaps"
category: hr-management/performance-reviews
description: "Draft the manager-side promotion packet for one person: each claim mapped to a named next-level anchor with a dated artefact, counter-evidence stated rather than omitted, a two-axis readiness × evidence-confidence verdict under a stated rule with INSUFFICIENT EVIDENCE as a real outcome, and the questions a promotion committee will ask answered in advance — distinct from hr_manager_writing_employee_review (the periodic review of the past cycle) and negotiation_salary_raise_promotion (the employee's own ask)."
techniques:
  - RT-05
  - OC-13
  - QA-02
  - CM-02
  - DD-07
difficulty: intermediate
tags:
  - promotion
  - promotion-packet
  - career-ladder
  - evidence-based
  - manager-writing
  - calibration
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/performance-reviews/hr_manager_writing_employee_review.md
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
  - domain-negotiation/contexts/negotiation_salary_raise_promotion.md
---

# Promotion Case Writer

**Objective:** Draft the packet a manager submits to argue that one person already
operates at the next level: every claim tied to a named anchor in the career ladder and
to a dated artefact, the evidence against stated plainly, and a verdict that can be
"not yet" or "insufficient evidence" as easily as "ready". A packet written as advocacy
with the gaps left out is refused.

**When to Use:**
- You are nominating a report for promotion and the committee wants a written case.
- You believe someone is ready but cannot yet say which next-level anchors they meet.
- A previous case failed and you need to know whether the gap was the person or the packet.

**Distinct from:**
- `hr_manager_writing_employee_review.md` — the periodic review of the past cycle against
  the *current* level. This argues against the *next* level, and a strong review does
  not make one.
- `../../domain-negotiation/contexts/negotiation_salary_raise_promotion.md` — the
  employee's own ask to their manager. This is the manager's submission to whoever
  decides.
- `hr_calibration_facilitator.md` — the meeting where cases are compared. This prepares
  one case for it.

**When NOT to use:** there is no written ladder. Build one first with
`../people-ops/hr_career_ladder_framework.md`; a case argued against an unwritten bar
is an argument about the manager's taste.

---

## Inputs

1. **The ladder text** for the current and next level, verbatim.
2. **The organisation's promotion evidence rule** — count, period, dimensions required.
3. **Evidence**: shipped work, documents, decisions, incidents, feedback — each with a date
   and a link or artefact name.
4. **Counter-evidence**: anything a sceptical committee member already knows about.
5. **The committee's format and length limit.**

---

## Method

1. **Map before writing (CM-02).** Build the evidence map first: one row per next-level
   anchor, with the artefacts that meet it. Prose written before the map drifts toward
   whatever the person did most visibly, which is often current-level work done well.

2. **Test each artefact against the anchor, not the effort (RT-05).** Ask of each: does
   this show the *difference* between the current and next level, or is it excellent
   current-level work? Only the former counts. Record the latter separately; it belongs
   in the periodic review.

3. **Tag each dimension on two independent axes (OC-13).**
   - **Readiness:** at next level / at current level / below current level.
   - **Evidence confidence:** High (artefact plus an independent corroborator), Medium
     (artefact only, or one example), Low (manager's recollection only).
   A dimension can be at the next level on Low confidence; report both rather than
   blending them into one colour.

4. **State the counter-evidence (QA-02).** For each weakness a committee member will
   raise, write it down with the context and whether it is resolved. An omitted weakness
   that surfaces in the meeting sinks the case and the manager's credibility with it.

5. **Apply the stated rule mechanically.** Use the organisation's rule. If none exists,
   default: *READY* if a majority of dimensions are at the next level on Medium or High
   confidence and none is below the current level; *NOT YET* if fewer; *INSUFFICIENT
   EVIDENCE* if the verdict turns on a dimension with only Low-confidence evidence. State
   the single cheapest piece of evidence that would resolve it.

6. **Pre-answer the committee.** List the three questions most likely to be asked and
   answer each in two sentences with a reference to the map.

7. **Self-audit before submitting (DD-07).** Run the verification table below and record
   the result in the packet.

---

## Output Format

```markdown
# Promotion case — [name], [current] → [next level], [cycle]
**Manager:** [name] · **Rule applied:** [org rule or default]

## Summary (3 sentences)
[what they do now that is next-level work; strongest evidence; main gap and its status]

## Evidence map
| Next-level anchor (verbatim) | Artefact (dated) | Why it is next-level, not current-level | Readiness | Confidence |
|---|---|---|---|---|

## Excellent current-level work (not counted)
- [item] — belongs in the periodic review

## Counter-evidence
| Concern | Context | Resolved? |
|---|---|---|

## Verdict
**READY / NOT YET / INSUFFICIENT EVIDENCE** — by [rule]: [count at next level] of [n] dimensions,
[any below current level]
Cheapest evidence to resolve (if insufficient): [...]

## Anticipated questions
1. [question] — [answer, referencing the map]

## Self-audit
[the verification checklist, with results]
```

---

## Verification

- [ ] Every claim cites an anchor verbatim and a dated artefact
- [ ] Each artefact states why it is next-level rather than excellent current-level work
- [ ] Readiness and confidence are tagged separately for every dimension
- [ ] Counter-evidence is present, not omitted
- [ ] The verdict follows mechanically from the stated rule, and the arithmetic is shown
- [ ] If INSUFFICIENT, the cheapest resolving evidence is named
- [ ] No reference to tenure, potential, retention risk or "they deserve it" as evidence
- [ ] No reference to protected characteristics, health or family circumstances

## False-Positive Prevention

1. **Volume is not level.** Ten current-level wins do not make one next-level example.
   Move them to the "not counted" list rather than padding the map.
2. **Retention risk is not evidence.** "We will lose them if we don't" is a compensation
   or role problem. It does not belong in a case, and committees discount packets that
   rely on it.
3. **Do not count the team's output as the person's.** For each artefact, say what this
   person decided or produced. A launch they attended is not a launch they led.
4. **Potential is not the bar.** The rule is sustained operation at the next level. Write
   "has not yet had the opportunity" as a gap, not as a strength.
5. **A NOT YET verdict is a useful output, not a failure.** It produces the development
   plan: name the one or two anchors to target and an opportunity to show them.
6. **Do not inflate confidence.** A dimension supported only by the manager's memory is
   Low, however vivid the memory.
7. **Check for asymmetric scrutiny.** If this packet includes counter-evidence that peer
   packets for similar people omit, flag it to the calibration facilitator. The
   inconsistency is the finding, not this person's weakness.

---

## Example

**Context:** Priya, E3 → E4, ladder from `../people-ops/hr_career_ladder_framework.md` (five dimensions).
Rule: default — majority (3 of 5) at next level on Medium/High confidence, none below E3.

| Anchor (E4) | Artefact | Readiness | Confidence |
|---|---|---|---|
| Scope: a problem spanning two or more teams | Billing migration design doc, 14 Feb; delivered across Payments and Platform | E4 | High (Platform lead corroborates) |
| Autonomy: chooses which project should exist | Proposal to retire the legacy invoice service, approved 9 May | E4 | High |
| Ambiguity: resolves an unscoped cross-team problem | Incident follow-up plan, 2 Jul | E4 | Medium (one example) |
| Influence: another team's roadmap changed from their proposal | Platform Q3 roadmap added her rate-limit design, 18 Jun | E4 | High |
| Craft | Strong code review record | E3 | High |

Four of five dimensions at E4, all on Medium or High confidence; none below E3 →
4 ≥ 3 → **READY**.

- **Not counted:** 11 features shipped on schedule. That is excellent E3 work.
- **Counter-evidence:** the March migration slipped three weeks. Context: a Platform
  dependency. She flagged it at week one, so this is resolved as a planning, not a
  judgement, concern.
- **Anticipated question:** "Is ambiguity proven on one example?" Answer: it is Medium
  confidence and not needed for the verdict (3 High dimensions already meet the rule).
  The Q4 on-call redesign is the second opportunity.

---

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — each claim tied to a verbatim anchor and a dated artefact.
- **OC-13 Two-Axis Verdict** — readiness and evidence confidence reported separately.
- **QA-02 Adversarial Stress-Test** — counter-evidence and committee questions answered in advance.
- **CM-02 Constraint Specification** — tenure, potential and retention risk banned as evidence.
- **DD-07 Self-Audit Table** — the packet carries its own verification result.

## Related Prompts

- `hr_manager_writing_employee_review.md` — the periodic review; excellent current-level work goes there
- `hr_calibration_facilitator.md` — where cases are compared across managers
- `../people-ops/hr_career_ladder_framework.md` — the anchors this case is argued against
- `../../domain-negotiation/contexts/negotiation_salary_raise_promotion.md` — the employee's side of the same moment
