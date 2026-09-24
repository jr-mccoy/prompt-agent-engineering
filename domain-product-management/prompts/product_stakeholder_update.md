---
title: "Product Stakeholder Update — Decisions First, Metric Movement Against Target, Roadmap Changes With Reasons"
category: product-management/prompts
description: "Write the recurring update a product manager sends to leadership and partner functions: decisions needed at the top with options, a recommendation, a deadline and the cost of delay (or a provisional-decision default), outcome metrics against target with honest attribution, what was learned rather than only shipped, roadmap changes with what moved later, and risks with owners — distinct from work_status_update_writer (generic project status) and business_writing_status_report (delivery progress against a project plan)."
techniques:
  - RP-02
  - NE-17
  - DP-16
  - DS-06
  - RT-05
difficulty: beginner
tags:
  - stakeholder-update
  - product-communication
  - decisions-needed
  - metrics-reporting
  - roadmap-changes
  - executive-communication
updated: "2026-09-24"
related_prompts:
  - domain-productivity/workplace/work_status_update_writer.md
  - domain-professional-writing/business-writing/business_writing_status_report.md
  - domain-product-management/prompts/product_north_star_metric_definition.md
---

# Product Stakeholder Update

**Objective:** Write the weekly or monthly product update so that a busy reader can act
on the first screen. Lead with decisions needed, then outcome metrics against target
with attribution stated honestly, what the team learned, what changed on the roadmap
and why, and the risks. Updates that open with a list of shipped features, report a
metric without its target, or claim credit for movement the team did not cause are
refused.

**When to Use:**
- Your update is a changelog and leadership still asks "so is it working?"
- Decisions you need are buried in paragraph four and do not get made.
- The roadmap changed and partner teams found out from the release.

**Distinct from:**
- `../../domain-productivity/workplace/work_status_update_writer.md` — a generic project
  status update for any audience.
- `../../domain-professional-writing/business-writing/business_writing_status_report.md`
  — delivery progress against a project plan with on-track/at-risk/blocked status. Use it
  when the question is "will the project land on time?" This prompt answers "are we
  moving the outcome, and what do you need to decide?"
- `product_release_notes_writer.md` — tells customers and support what changed. This
  tells stakeholders what it achieved.

---

## Inputs

1. **Readers**: who, what they decide, and how much they will read.
2. **Outcome metrics** with targets, the current value and the previous period.
3. **What shipped and what was learned**: experiments, research, launches.
4. **Decisions you need**, from whom, by when.
5. **Roadmap changes** since the last update.
6. **Risks**, with owners.

---

## Method

1. **Put decisions needed first (NE-17, DP-16).** For each: the question in one sentence;
   the options (two or three); your recommendation; the deadline; and the cost of
   delay. Where you can, make it provisional: "Unless you object by [date], we will [do
   the recommendation]." If nothing needs deciding, say "No decisions needed" in the
   first line.

2. **Report outcomes against target (RT-05).** For each outcome metric: current value,
   target, previous period, and whether the change is outside normal variation. Then
   state attribution honestly. "Up 2 points, with our experiment still running, so not
   yet attributable" is a finding. "Up 2 points thanks to our onboarding work" is a claim
   that needs the readout first.

3. **Report learning, not just shipping.** For each item shipped or tested, say what the
   team now knows that it did not before, including disproved assumptions. A shipped
   list with no learning cannot show whether the work mattered.

4. **State roadmap changes with reasons.** What moved earlier, what moved later, and why.
   Always name what got pushed out. Partner teams plan around what they were told, so a
   silent deferral is the change that damages trust.

5. **Rank risks (DS-06).** Top three at most, each with likelihood, impact, an owner and
   the next action. A risk with no owner is a worry.

6. **Tailor length to the reader (RP-02).** Write a five-line summary block for
   executives, then detail sections for partner teams. The summary must stand alone.

---

## Output Format

```markdown
# [Product area] update — [period] · [author]

## Summary (5 lines)
1. Decisions needed: [n] — first due [date]
2. Headline outcome: [metric] [value] vs target [x] ([on/off] track)
3. Main learning: [...]
4. Roadmap change: [...]
5. Top risk: [...]

## Decisions needed
| Decision | Options | Recommendation | Deadline | Cost of delay | Default if no reply |
|---|---|---|---|---|---|

## Outcomes
| Metric | Now | Target | Last period | Beyond normal variation? | Attribution |
|---|---|---|---|---|---|

## Learned
- [item] → [what we now know]

## Roadmap changes
| Item | Was | Now | Why | Who is affected |
|---|---|---|---|---|

## Risks
| Risk | Likelihood | Impact | Owner | Next action |
|---|---|---|---|---|
```

---

## Verification

- [ ] Decisions needed (or "none") appear in the first line
- [ ] Every decision has options, a recommendation, a deadline and a cost of delay
- [ ] Every metric is shown with its target and previous period
- [ ] Attribution is stated and does not claim causation without a readout
- [ ] Every shipped item has a learning, or is marked "no learning yet"
- [ ] Roadmap changes name what moved later and who is affected
- [ ] At most three risks, each with an owner and a next action
- [ ] The five-line summary stands alone

## False-Positive Prevention

1. **Movement is not causation.** A metric that rose while your change shipped may have
   risen for seasonal or marketing reasons. Say "not yet attributable" until an
   experiment or readout supports it.
2. **A metric without a target is not a status.** "41,200 invoices" means nothing. "41,200
   against 45,000" does.
3. **Do not bury a decision in the narrative.** If it is not in the decisions table, you
   did not ask for it.
4. **A provisional decision needs a real deadline and a real objection path.** Otherwise it
   is a fait accompli presented as consultation.
5. **Do not omit what moved later.** Reporting only additions makes the roadmap look like
   it grew for free.
6. **Do not pad with activity.** Meetings held and documents written are not outcomes.
   Leave them out unless a reader needs them for a decision.

---

## Example

**Context:** Monthly update, Invoicing area, for the VP Product, Sales lead and Support
lead. Author: Billing PM. September.

**Summary:**
1. Decisions needed: 1, due 15 Oct.
2. Weekly invoices sent: 41,200 vs target 45,000 (91.6%, off track).
3. Learned: reminders sent after bank-transfer payments are the main Auto-chase complaint.
4. Roadmap: Auto-chase general availability moves from 3 Nov to 17 Nov; CSV v2 moves to Q1.
5. Top risk: Stripe sync reliability.

| Decision | Options | Recommendation | Deadline | Cost of delay | Default |
|---|---|---|---|---|---|
| Delay Auto-chase GA by 2 weeks to add paid-by-transfer detection | (a) ship 3 Nov as is; (b) slip to 17 Nov | (b) | 15 Oct | Each week at 25% rollout sends ~40 reminders on paid invoices | Unless you object by 15 Oct, we slip to 17 Nov |

| Metric | Now | Target | Last | Beyond variation? | Attribution |
|---|---|---|---|---|---|
| Weekly invoices sent | 41,200 | 45,000 | 40,100 | No (+2.7%) | None claimed |
| 7-day activation | 32% | 35% | 30% | Unclear | Onboarding experiment running; readout 1 Dec |

(41,200 − 40,100) / 40,100 = 2.7%.

**Roadmap:** CSV v2 moves from Q4 to Q1 to free the two engineers for transfer detection.
Affected: Support, whose macro update is now due in Q1.

**Risk:** Stripe sync failures recur (medium likelihood, high impact). Owner: Platform
lead. Next action: add an alert on sync lag over 1 hour, by 20 Oct.

---

## Techniques Used

- **RP-02 Audience-Specific Framing** — an executive summary that stands alone, with detail for partner teams.
- **NE-17 Call-to-Action Mandatory Close** — decisions needed as the first, explicit ask.
- **DP-16 Provisional Decision Message Template** — "unless you object by [date]" defaults.
- **DS-06 Prioritization and Severity Guidance** — at most three risks, ranked, with owners.
- **RT-05 Evidence-Based Reasoning** — metrics with targets and attribution stated honestly.

## Related Prompts

- `../../domain-productivity/workplace/work_status_update_writer.md` — generic status update
- `../../domain-professional-writing/business-writing/business_writing_status_report.md` — delivery status against a plan
- `product_north_star_metric_definition.md` — the outcome metrics this reports
- `product_experiment_design.md` — the readout that makes attribution possible
