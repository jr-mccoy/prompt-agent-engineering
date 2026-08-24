---
title: "Build a 90-Day Repositioning Plan Toward Surviving / Adjacent Roles"
category: personal-development/career-transformation
description: "Translate a vulnerability assessment and residual-skills inventory into a concrete 90-day plan: which adjacent role(s) to bridge into, what evidence the user will produce, what signals they'll send, and which weekly checkpoints catch drift. Plans, not wish-lists."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - career
  - repositioning
  - 90-day-plan
  - bridge-role
  - proof-of-work
updated: "2026-04-21"
related_prompts:
  - domain-personal-development/career-transformation/career_coordination_tax_audit.md
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
---

# Build a 90-Day Repositioning Plan Toward Surviving / Adjacent Roles

**Objective:** Produce a specific, weekly-checkpointed 90-day plan that moves the user from a vulnerable role into one of 1–3 named adjacent roles. The plan commits to evidence the user will produce, signals they will send, and stop conditions that redirect if the plan isn't working. Not a career lecture; not a motivational framework.

**When to use:**
- The user has already completed (or will complete as inputs) `career_role_structural_vulnerability.md` and `career_residual_skills_inventory.md`.
- The user has decided they want to reposition — not "explore options."
- The user has 90 days of bandwidth (roughly 3–6 hours/week of repositioning time is the floor; plan assumes this or more).
- User is willing to produce observable artifacts during the plan, not just "learn" quietly.

**Don't use when:** The user hasn't done the upstream assessments. The plan depends on a concrete vulnerability read and a real residual-skills inventory; without those it collapses into generic career advice.

**Audience:** An individual acting as their own program manager for the next 90 days.

---

## Inputs Required

Require all of these. Refuse to plan without 1, 2, 3, and 5.

1. **The vulnerability assessment output.** Axes + grades + load-bearing axis from `career_role_structural_vulnerability.md`.
2. **The residual skills inventory.** Ranked Residual + Compounding skills from `career_residual_skills_inventory.md`.
3. **2–5 candidate adjacent roles.** Role names, and why the user thinks each is plausibly bridgeable. If the user has zero candidates, ask them to list the 3 roles they'd be doing if they weren't in their current role — that's the starting set.
4. **Constraints.** Hours/week available for repositioning, geographic / remote constraints, timeline hard stops (e.g., contract ending, visa issue, parental leave), compensation floor. If any of these are unstated, ask.
5. **Public surface.** The user's current public footprint for this field: LinkedIn shape, writing, talks, repos, portfolio, network in the target domain. Honest description, not aspirational.
6. **Optional: a specific person who has already done this move.** Name and what the user knows about how they did it.

---

## Instructions

### Step 1 — Filter candidate roles

For each of the 2–5 candidate roles, score on three filters. Drop any role that fails any one filter.

- **Skill overlap:** Does the user's ranked Residual inventory (input 2) match what this role's first 12 months require? If no Residual skill is load-bearing in the candidate role, the candidate is a leap, not a bridge. Drop.
- **Vulnerability independence:** Does the candidate role have a different structural vulnerability profile than the user's current role? If the candidate shares the same failing axis (e.g., both are heavy on the same category of coordination tax), the move doesn't reposition — it just relocates. Drop or explicitly flag.
- **Bridge feasibility in 90 days:** Can a person with the user's current public surface (input 5) credibly show up as a candidate for this role within 90 days of focused effort? If no, the target is a 6–18 month move; this plan is not it.

If fewer than 1 candidate survives, say so plainly. Do not invent candidates.

### Step 2 — Pick the primary target + 1 backup

Rank surviving candidates. Choose one primary (highest overlap + highest independence + feasible bridge) and one backup. The plan commits to the primary; the backup exists so the user has a redirect if a stop condition fires.

### Step 3 — Define the bridge hypothesis for the primary

One paragraph. Specifically: what about the user — which Residual skills, which domain context, which recent work — makes the primary role a plausible hire in 90 days? If this paragraph isn't specific (falls back on personality words or "transferable skills"), the plan will not work. Redo or drop.

### Step 4 — Commit to evidence the user will produce

Pick 2–4 artifacts the user will ship publicly or semi-publicly in the 90 days. These are not projects for practice; they are proof the user does the thing the target role does. Each artifact has:

- **Name + form** (essay, repo, talk, case study, teardown, internal deck shared externally, client engagement, etc.).
- **Target audience.** One or two specific people or types of people it's intended for.
- **Ship date** within the 90 days.
- **Tie to Residual skill.** Which Residual skill this artifact demonstrates.
- **Cost to produce.** Rough hours.

If the user can't name any artifact, the plan is not viable; say so.

### Step 5 — Commit to signals the user will send

Signals are how the market finds out the user is now doing this work. Pick 2–4 specific signals — profile changes, writing cadence, 1-on-1 conversations with specific people, public association with the target domain. Each signal has:

- **What it is**
- **Ship date** within the 90 days
- **Observable evidence it has landed** (e.g., "3 inbound messages from people in the target role")

Signals are NOT applications. Applications are downstream; plan for them only after signals have landed.

### Step 6 — Build the week-by-week plan

13 rows. Each row has:

- **Week N**
- **Primary output** (what gets shipped / landed this week)
- **Artifact or signal advanced** (which one from steps 4–5)
- **Hours committed** (realistic, not aspirational)
- **Checkpoint question** (observable, yes/no by week end)

Leave Week 13 as a synthesis + decision week (continue / redirect / exit), not a new-shipping week.

### Step 7 — Define stop conditions and the redirect

Stop conditions fire before wasting 90 days:

- **Evidence-not-landing stop:** By week 5, at least one artifact has shipped and gotten at least one external response. If not: redirect.
- **Signal-not-landing stop:** By week 8, at least one signal has produced observable evidence (inbound DM, conversation, mention). If not: redirect.
- **Sunk-cost stop:** If hours invested in the primary cross 2× the plan's budget by week 8 with no checkpoint passes, redirect.

The redirect is NOT to quit — it's to switch to the backup target and compress the remaining weeks. Specify the redirect plan in one paragraph.

### Step 8 — Define success at Week 13

Not "got a new job." Realistic success for a 90-day plan is one of:

- At least one concrete hiring conversation in the target role.
- A portfolio of 2+ shipped artifacts that sit in the target domain.
- A clear, evidence-based read that the target role is actually the right target — or isn't.

Say all three, so the user doesn't conflate plan success with career outcome.

### Step 9 — Verify and output

Run the verification checklist before delivering.

---

## Constraints

### Must
- Commit to a single primary target and a single backup.
- Ship evidence publicly or semi-publicly, not in private practice.
- Constrain to the user's actually-available hours/week.
- Include stop conditions with dates, not vibes.
- Define Week 13 success in observable terms.

### Must Not
- List more than two live targets (primary + backup). More = no plan.
- Produce a "learning plan" as the primary output. Learning without shipped artifacts is a common failure.
- Use generic resume / interview tactics. That's the downstream work, not the plan.
- Hedge the bridge hypothesis. If the user can't state it specifically, the plan fails here.
- Commit the user to more than 1.5× their stated available hours.
- Promise career outcomes. The plan is the process; outcomes aren't plan-level commitments.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Accept "adjacent role" candidates that require reskilling from scratch. That's a pivot, not a repositioning.
- Let the user pick a candidate role whose structural vulnerabilities are worse than the current role. Check input 1 against the target.
- Let "build my network" stand as a signal. Force specificity: whose network, what form, observable evidence of landing.
- Let an artifact count as "learning." An artifact must ship and be observable to an audience outside the user's head.
- Let the plan run 13 shipping weeks with no synthesis week. The user burns out and the decision doesn't get made.

✅ **DO:**
- Push back when the bridge hypothesis is generic. Require domain-specific language.
- Force at least one artifact to be shippable by Week 4 (tests whether any artifact is actually viable).
- Treat the backup as a real second target — write its one-paragraph bridge hypothesis too, briefly.
- Require the weekly hours commitment to add to ≤ 1.5× the user's stated weekly availability. Include a rest/margin buffer.
- Name specific people, channels, or platforms by type where possible.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Plan is aspirational ("ship 6 essays, rebuild portfolio, get intros from 30 people, apply to 50 companies"). User fails by week 3 and concludes they can't reposition.

❌ **UNHELPFUL failure:** Plan is so hedged that it doesn't commit to anything. User ends Week 13 with the same question they started with.

✅ **Quality check:** A skeptical peer reading the plan could point to any single weekly row and say "what does 'done' look like for this week?" and get a specific answer.

---

## Output Format

```markdown
# 90-Day Repositioning Plan — [User Current Role] → [Primary Target]

## Target Selection
- **Primary:** [Role name]
- **Backup:** [Role name]
- **Dropped candidates:** [With one-line reason per drop]

## Bridge Hypothesis (Primary)
[One paragraph specifically naming residual skills + domain context + recent work that make the user a plausible hire in 90 days.]

## Bridge Hypothesis (Backup)
[One short paragraph.]

## Evidence (Artifacts to Ship)
| # | Artifact | Audience | Ship Week | Residual Skill | Hours |
|---|----------|----------|-----------|----------------|-------|
| 1 | | | | | |
| 2 | | | | | |

## Signals to Send
| # | Signal | Ship Week | Observable Landing Evidence |
|---|--------|-----------|----------------------------|
| 1 | | | |
| 2 | | | |

## Weekly Plan
| Week | Primary Output | Artifact/Signal Advanced | Hours | Checkpoint Question |
|------|----------------|--------------------------|-------|---------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |
| 12 | | | | |
| 13 | Synthesis + Decision | — | | Continue / Redirect / Exit? |

## Stop Conditions (Redirect Triggers)
- **Week 5 — Evidence check:** At least one artifact shipped and received external response. If not: [specific redirect action].
- **Week 8 — Signal check:** At least one signal produced observable landing. If not: [specific redirect action].
- **Week 8 — Sunk-cost check:** Hours > 2× budget with no passed checkpoints. If yes: [specific redirect action].

## Redirect Plan (to Backup)
[One paragraph. How the remaining weeks compress to attempt the backup target.]

## Success at Week 13 (Observable)
- [ ] At least one concrete hiring conversation in the target role, OR
- [ ] Portfolio of ≥2 shipped artifacts in the target domain, OR
- [ ] Clear evidence-based read that the target role is / isn't the right one.

## Constraints Honored
- Hours / week: [committed vs available]
- Geographic / remote: [honored]
- Timeline hard stops: [honored]
- Compensation floor: [honored or flagged]
```

---

## Verification

- [ ] Exactly one primary target and one backup.
- [ ] Bridge hypothesis is specific, not generic.
- [ ] Every artifact and signal has a ship week and observable landing criterion.
- [ ] Weekly plan has 13 rows; Week 13 is synthesis/decision, not new shipping.
- [ ] Stop conditions name dates and redirect actions.
- [ ] Hours committed ≤ 1.5× available hours/week.
- [ ] Success at Week 13 is observable, not outcome-based.
- [ ] No generic career or job-search advice.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a plan with weekly commitments and stop conditions, not career counseling.
- **ST-02 (Structured Sequential Instructions):** Nine steps from target filtering → bridge hypothesis → artifacts → signals → weekly plan → stops → success → verify.
- **CM-02 (Constraint Specification):** Must Not block prevents "learning plan" substitutes and aspirational over-commitment.
- **DS-01 (Framework Application):** Three filters (skill overlap / vulnerability independence / bridge feasibility) are the target-selection framework.
- **RT-11 (Error Recovery):** Stop conditions with redirect plans handle the failure modes before they consume the full 90 days.
- **QA-01 (Self-Verification):** Verification checklist catches generic bridge hypotheses, aspirational hours, and outcome-based success criteria.
