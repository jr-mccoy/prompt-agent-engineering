---
title: "Community Operations — Charter, Cadence, Moderation, and the Deltas a Paid Community Adds"
category: business-strategy/creator-economy
description: "Operate a community rather than launch one: a charter that says who it is for and what it is not, an engagement cadence one person can hold, a moderation policy with due process and a named decider, and the specific additions a paid membership forces — refunds alongside bans, an appeal path, and a stated obligation."
techniques:
  - CM-02
  - RT-05
  - DS-06
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - community
  - moderation
  - code-of-conduct
  - paid-membership
  - creator-economy
  - governance
updated: "2026-09-22"
related_prompts:
  - domain-business-strategy/creator-economy/creator_platform_choice_owned_vs_rented.md
  - domain-business-strategy/creator-economy/creator_prelaunch_demand_validation.md
  - domain-agentic-resources/skills/non-coding/cross-domain/handoff-approval-workflow/SKILL.md
---

# Community Operations

**Objective:** Produce the four operating documents a community needs to survive
its first difficult week: a charter, an engagement cadence, a moderation policy
with due process, and — where money is involved — the deltas a paid membership
forces.

**When to Use:**
- A community exists or is about to, and nobody has written down who it is for.
- Something went wrong and there was no policy, so the decision looked personal.
- You are charging for access and have not thought about what a ban means when
  the member has paid.
- Engagement depends entirely on you showing up, and you want a cadence that
  does not.

**When NOT to use:**
- You need to launch a community from zero, run a flywheel, recruit ambassadors
  or pick a platform — `domain-agentic-resources/skills/marketing/community-marketing/`
  owns all four, including the Platform Selection Guide and health metrics.
- You need membership *tier* design and pricing —
  `startup/monetization_subscription_design.md`,
  `skills/marketing/pricing-strategy/references/tier-structure.md`, and
  `skills/marketing/paywall-upgrade-cro/`.
- You need safeguarding policy for work with minors or vulnerable adults —
  `domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md` is the
  serious version and this prompt does not substitute for it.

## Inputs / Context

1. **What the community is for**, in the member's terms: what they get that they
   cannot get alone.
2. **Who it is for, and who it is not for.**
3. **Where it lives**, and what that platform makes easy or impossible.
4. **Free or paid**, and if paid, what the price implies about obligation.
5. **Hours per week the operator can give**, measured.
6. **Who else can moderate**, if anyone.
7. **What has already gone wrong**, here or in a community they have been in.

## Method

1. **Write the charter (CM-02).**
   Four parts, each one paragraph: what this is for; who it is for; **what it is
   not**; what members owe each other. The "what it is not" paragraph is the one
   that does the work — it is what you point at when someone arrives expecting
   something else, and writing it is what stops a general-interest drift.

   Craft precedent worth reading: `domain-science/lab-operations-mentorship/science_lab_culture_charter.md`
   builds a charter that states obligations rather than aspirations.

2. **Design the engagement cadence against measured hours (DS-06).**
   - What recurs, how often, who runs it, and how long it takes.
   - The **bad-week version**: what still happens when the operator is absent.
   - A cadence that only works when the founder is present is a schedule for one
     person, not a community, and it fails exactly when they most need it not to.

3. **Write the moderation policy, with due process (RT-05, OC-03).**
   Not a list of banned behaviours — a *procedure*:

   | Element | Must state |
   |---|---|
   | Standards | the small number of things that are not allowed, in observable terms |
   | Who decides | one named accountable person, not "the team" |
   | Steps | what happens first, second, and at removal |
   | Evidence | what is recorded, and where |
   | Appeal | to whom, in what window, and who is excluded from hearing it |
   | Publication | what the community is told about an enforcement, and what it is not |

   `domain-agentic-resources/skills/non-coding/cross-domain/handoff-approval-workflow/`
   is the general pattern for one accountable decider, a stated timeout and a
   rework path; apply it here rather than reinventing it.

4. **Add the paid deltas, if money is involved.**
   A paid membership changes three things and only three:
   - **A ban is also a refund decision.** State the rule *before* you need it:
     pro-rata, full, or none, and who signs it off.
   - **Due process is owed, not offered.** A paying member removed without a
     stated procedure has a grievance that is partly about the money.
   - **An obligation exists.** Price implies a promise: state what members are
     owed per month, and what happens if it is not delivered.

   Everything else about a paid community is a free community with a card on file.

5. **Verify the policy against a real incident (QA-01).**
   Take something that actually happened, in this community or another, and walk
   it through the procedure. If the procedure does not reach an outcome, it is
   not a procedure.

## Output Format

```
# Community operations — [name]

## Charter
**What this is for:** [paragraph]
**Who it is for:** [paragraph]
**What it is not:** [paragraph]
**What members owe each other:** [paragraph]

## Cadence
| What | How often | Who runs it | Time | Happens without the operator? |
|---|---|---|---|---|

Bad-week version: [what still happens if the operator disappears for two weeks]
Total operator hours/week: [n] against [n] available.

## Moderation policy
Standards (observable, short): [...]
Accountable decider: [named role]
Steps: 1. [...] 2. [...] 3. removal
Evidence recorded: [what, where, for how long]
Appeal: to [whom], within [window]; [who may not hear it]
What the community is told: [...]

## Paid deltas  (omit this section entirely if the community is free)
- Refund on removal: [pro-rata | full | none] — decided by [role]
- Due process owed: [what a paying member is entitled to]
- Monthly obligation: [what members are owed] — if undelivered: [...]

## Walkthrough
Incident: [a real one]
Through the procedure: [step by step, to an outcome]
What it exposed: [...]

## Open questions
- [unresolved, and what it blocks]
```

## Verification

- [ ] The charter's "what it is not" paragraph excludes something real.
- [ ] The cadence names a bad-week version that survives the operator's absence.
- [ ] Operator hours do not exceed hours available.
- [ ] The moderation policy names **one** accountable decider.
- [ ] There is an appeal path, with a window and an exclusion.
- [ ] If paid: the refund rule is written before it is needed.
- [ ] A real incident has been walked through to an outcome.

## False-Positive Prevention

1. **A code of conduct is not a moderation policy.** A list of prohibited
   behaviours with no procedure produces decisions that look personal, because
   in the absence of a procedure they are.
2. **"The team decides" is nobody deciding.** One named accountable person, or
   the first hard case stalls.
3. **Do not write the refund rule during the incident.** Whatever you decide
   under pressure will look like it was decided about that person.
4. **Values are not standards.** "Be respectful" cannot be enforced. Standards
   must be observable enough that two moderators reach the same verdict —
   `skills/non-coding/cross-domain/quality-rubric-template/` is the general
   method for that if the standards keep producing disagreement.
5. **Engagement that requires the founder is a schedule, not a community.** Test
   it by removing them for two weeks on paper.
6. **Paid does not mean more rules.** It means three specific additions. Adding
   a governance apparatus because money is involved is how a community becomes
   an obligation nobody enjoys.

## Related

- `domain-agentic-resources/skills/marketing/community-marketing/` — launching,
  the flywheel, ambassadors, health metrics, platform selection.
- `creator_platform_choice_owned_vs_rented.md` — where the community lives, and
  what that exposes it to.
- `domain-science/lab-operations-mentorship/science_lab_culture_charter.md` — charter craft.
- `domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md` — the
  serious safeguarding version, for communities that need one.
