---
title: "Find the Real Growth Constraint in Distribution / Relationships"
category: productivity/bottlenecks
description: "When output exists but nothing is growing, diagnose which specific distribution constraint is binding — audience absent, artifact wrong shape, channel mismatched, trust missing, or no ask made — and propose one concrete action tied to that specific cause rather than 'post more on LinkedIn.'"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - bottleneck
  - distribution
  - relationships
  - growth
  - reach
updated: "2026-04-20"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-productivity/bottlenecks/bottleneck_daily_execution_habits.md
  - domain-personal-development/prompts/agency/agency_feedback_extraction.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
---

# Find the Real Growth Constraint in Distribution / Relationships

**Objective:** Diagnose which specific distribution constraint is preventing work from reaching people, from a fixed set of five causes. Output must name exactly one binding cause and one concrete action tied to that cause — not a generic marketing suggestion.

**When to use:** After `bottleneck_locator.md` identifies distribution as binding — the user produces real work but nobody sees or acts on it. Also when "growth" has stalled despite continued shipping.

**Audience:** An individual trying to reach their own audience, clients, or collaborators. Not a marketing team running campaigns.

---

## Inputs Required

1. **What the user has shipped in the last 90 days.** Artifacts, projects, products, writings, services. Each with rough date.
2. **Who has seen / used it and how.** Named people where possible, channel (DM, email, public post, meeting, cold send) for each.
3. **Growth signal over last 6 months.** Followers, customers, clients, readers, collaborators — whatever the user is trying to grow. Actual numbers at start and end of the 6-month window.
4. **The target audience, as specifically as the user can state it.** Role / industry / need / location. "Anyone who would find this useful" is the symptom, not the answer.
5. **Direct asks made in the last 90 days.** Number of people explicitly asked to subscribe / buy / hire / refer / introduce. Not posts that might convert; explicit asks.
6. **The user's guess at the constraint.** Often wrong.

If input 1 is empty (nothing shipped in 90 days), the bottleneck is execution, not distribution. Redirect to `bottleneck_daily_execution_habits.md`.

---

## Instructions

1. **Evaluate the five possible binding constraints:**

   - **Audience absent** — there is no identified group of people for whom this work solves a named problem. Symptom: input 4 is vague ("anyone interested in X").
   - **Artifact wrong shape** — the work exists but in a form the audience doesn't consume. Symptom: input 1 shipped a 10-part course when the audience reads tweets; or shipped a GitHub repo when the audience buys SaaS.
   - **Channel mismatched** — the right form in the wrong place. Symptom: input 2 shows publishing on channels the audience isn't on.
   - **Trust missing** — the audience sees the work but doesn't believe the user can deliver. Symptom: engagement without conversion; "looks great" without purchase or referral.
   - **No ask made** — the audience sees the work and the user never asked for the next step. Symptom: input 5 shows near-zero direct asks.

2. **Score each against inputs.** For each, state the evidence or note "no signal either way." Do not guess.

3. **Pick exactly one binding constraint.** Tiebreakers, in order:
   - Prefer "No ask" over anything else if input 5 is < 5. Most distribution failures are here.
   - Prefer "Audience absent" over "Artifact wrong shape" — without a named audience, artifact shape is undetermined.
   - Prefer "Channel mismatched" over "Trust missing" only if the user has never published in the audience's native channel; otherwise trust is upstream.

4. **Name one concrete next action** tied to the constraint:
   - Audience absent → "Write a 50-word paragraph naming the person by role, situation, and specific problem. Send to three people who fit and ask them if the description is right."
   - Artifact wrong shape → "Take one recent artifact and reshape its key insight into the native format of the target audience — a 3-minute read, a 90-sec demo, a one-page sheet. Ship this week."
   - Channel mismatched → "Identify where the target audience actually gathers — publication, group, conference, newsletter. Publish one piece there this week; do not also cross-post to old channels."
   - Trust missing → "Ship a small proof of capability that's closer to the audience's work than to yours — a case study, a teardown, a demo of their problem solved."
   - No ask made → "Make five direct asks this week — named person, specific request, clear what they'd say yes or no to. Track responses."

5. **State what not to do.** The tempting action that addresses the wrong constraint. Example: "Do not post more until a direct ask has been made to existing viewers."

6. **Produce a 30-day signal to watch.** The single number that would move if this constraint were actually binding and relieved.

---

## Output Format

```
## Shipped (last 90 days)
[Summary count and artifacts]

## Growth Signal (6 months)
- Start: [number]
- End: [number]
- Delta: [abs, %]

## Target Audience as Stated
[Input 4]
Specificity: specific / partial / vague

## Five Constraints — Signal Check
| Constraint | Evidence | Score |
|---|---|---|
| Audience absent | [...] | binding / not binding / no signal |
| Artifact wrong shape | [...] | ... |
| Channel mismatched | [...] | ... |
| Trust missing | [...] | ... |
| No ask made | [...] | ... |

## Binding Constraint
[One named] — because [one sentence of evidence]

## Next Action (this week)
[Specific, physical, by Friday, tied to constraint]

## What Not to Do
[Tempting action that would address the wrong constraint]

## 30-Day Signal to Watch
[Single number that would move if this diagnosis is correct]
```

---

## Constraints

**Must:**
- Pick exactly one binding constraint.
- Use inputs 1–5 as evidence for the pick; note where inputs are silent.
- Produce one next action matched to the constraint.
- Name the tempting-but-wrong action.

**Must not:**
- Recommend "post more on [any platform]" as a generic answer.
- Suggest hiring a growth consultant, agency, or PR firm.
- Provide a multi-channel distribution plan. One constraint, one move.
- Push the user to pick a different audience unless the audience-absent constraint is binding.

---

## False-Positive Prevention

- **Volume fallacy:** The default wrong answer is "just do more." Volume without a diagnosed constraint wastes effort. Refuse to prescribe volume.
- **Audience-expansion fantasy:** "We need a bigger audience" often hides "we haven't asked our current audience for anything." Check input 5 before expanding.
- **Channel-obsession:** Users over-focus on channel and under-focus on ask. If input 5 is low, that's probably the real issue.
- **Trust without data:** "Trust missing" is easy to project. It's only binding if engagement exists without conversion — not if there's neither. No engagement = audience or artifact problem upstream.
- **Personal-brand bait:** The constraint isn't "your brand." It's structural. Refuse to make it about personal reinvention.

---

## Self-Verification (before finalizing)

- [ ] One constraint named as binding.
- [ ] Evidence cited from inputs 1–5 for the pick.
- [ ] Tiebreaker rules applied if multiple constraints show signal.
- [ ] Next action is specific, physical, dated, tied to the named constraint.
- [ ] "What not to do" names a tempting wrong move.
- [ ] 30-day signal is a single measurable number.
- [ ] No "post more," generic-marketing, or brand-reinvention advice.
