---
title: "Build a Proof-of-Work Portfolio Over a Defined Horizon"
category: personal-development/agency
description: "Plan a portfolio of shippable artifacts over a 3–12 month horizon, chosen so each one is defensible on its own, accumulates into a coherent track record, and forces the user into repeated shipping rather than repeated planning."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - agency
  - portfolio
  - track-record
  - consistent-shipping
  - career
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Build a Proof-of-Work Portfolio Over a Defined Horizon

**Objective:** Design a 3–12 month portfolio of shipped artifacts — not a resume, not a roadmap — where each entry is independently defensible, the full set tells a consistent story, and the cadence forces the user to finish things on a schedule rather than work indefinitely on one big thing.

**When to use:** The user wants to change jobs, get more serious about a craft, switch fields, or build a public track record. They tend to work on one large thing for a long time and have little to show in-flight. Or: they have lots of small fragments and no coherent whole.

**Audience:** An individual whose track record will be assessed, by themselves or by others, over a defined horizon. Not a team building a product roadmap.

---

## Inputs Required

1. **The horizon.** Start date, end date. (3–12 months; flag if outside this band.)
2. **The audience for the portfolio.** Who will look at this and in what context — hiring managers, clients, peers, the user themselves, a specific community? If "everyone," push back: the audience shapes the portfolio.
3. **The story the portfolio should tell.** "I can do X." One sentence. If the user can't state this, help them pick.
4. **What already exists.** Past work the user would include. Rough count and brief description.
5. **Available weekly hours** for portfolio work, realistic not aspirational.
6. **Domain.** Writing, code, video, design, research, speaking, teaching, product, etc. — shapes what "shipped" looks like.

If audience or story is absent, produce them first before the portfolio plan.

---

## Instructions

### Step 1 — Define the one-sentence story

The portfolio exists to make one claim. Write the claim in the form:

> "[Name] can [specific capability], demonstrated by [category of artifact]."

If the sentence has more than one "and," it's two portfolios. Split or narrow.

### Step 2 — Set cadence based on hours and domain

Compute a realistic cadence of finished artifacts per month given weekly hours and domain. Examples:

- Short writing (essays, ~1500 words): 1–2 per month at 4–6 hr/week.
- Long writing (~5000 words): 1 per 6–8 weeks.
- Code (small usable tool): 1 per 3–6 weeks.
- Substantial case study / report: 1 per 4–8 weeks.
- Short video: 1–2 per month.

Adjust to the user's domain. Cadence that assumes every hour is productive is wrong; discount by 30–40%.

### Step 3 — Choose the artifact types (max 3)

Pick at most three artifact types for the portfolio. Fewer types means a sharper story; more means thinner demonstrations. For each type, state:

- What a single instance looks like (size, format, where it lives).
- What it demonstrates that supports the story.
- Rough time to ship one.

If the user proposes five types, narrow. Three is the ceiling.

### Step 4 — Populate the horizon

Produce a month-by-month layout of planned artifacts. For each month:

- 1–3 planned artifacts, by type.
- Rough topic / subject for each (enough to be recognizable; not a full outline).
- One-line note on why this one now (sequencing, skill-build, audience, seasonality).

Leave explicit slack: at least one month in every three has no new portfolio artifact planned. Slack handles slippage, rest, and real life. Portfolios without slack miss.

### Step 5 — Pick the opener

The first artifact of the portfolio is special. It should:

- Be at the easier end of the chosen types.
- Be shippable in the first 3–6 weeks of the horizon.
- Exercise the full ship-pipeline end-to-end (not just drafting — the actual place it lives in public, the actual announcement).

If the opener is ambitious, it delays the start of the portfolio into planning; pick something smaller.

### Step 6 — Define the portfolio's shipping standard

State the common floor for every artifact:

- Where it lives (public URL, repo, platform).
- Has at least one specific external reader / viewer / user.
- Exists with a readable entry-point (title, README, description) a stranger could navigate.

Anything below this floor isn't in the portfolio.

### Step 7 — Anti-drift controls

Name the three drift risks for this user and a pre-committed response:

- **The one-big-thing trap.** Pre-commit: smallest portfolio-class artifact gets shipped within 6 weeks of start, before the big thing takes over.
- **Perfectionism on individual pieces.** Pre-commit: no revision past 2× the initial time budget; ship at the floor and move on.
- **Quiet drift from the story.** Pre-commit: at each monthly review, read the one-sentence story and the last artifact; if they don't align, say so.

---

## Constraints

### Must
- Produce a single one-sentence story.
- Produce a realistic cadence given hours.
- Limit artifact types to three or fewer.
- Leave at least one slack month per three.
- Define a common shipping floor.

### Must Not
- Propose a portfolio longer than 12 months (lose resolution) or shorter than 3 (not a portfolio).
- Treat portfolio work as career strategy advice — that's a different prompt.
- Plan artifacts that depend on new skills the user hasn't started building.
- Plan secret-portfolio work. If it isn't public, it isn't in the portfolio.
- Schedule every month full.

---

## False-Positive Prevention

1. **"Diverse portfolio" is often incoherent portfolio.** If three types of artifact don't share a story, the viewer sees noise. Narrow rather than diversify.
2. **Don't schedule flagship work in month 1.** The first artifact should be a small shippable proof, not the user's magnum opus.
3. **Don't confuse volume with proof.** Twelve thin artifacts can be weaker than five defensible ones. Cadence follows hours, not ambition.
4. **Don't assume no life happens.** A 12-month plan that ignores holidays, illness, and job pressure won't survive month 3.
5. **Don't let portfolio planning become the project.** If the user spends a week designing the portfolio before shipping anything, the portfolio is serving avoidance. Push to ship the opener concurrently with finalizing later months.

---

## Output Format

```
# Portfolio plan: [one-sentence story]

## Story
[Claim sentence.]

## Horizon
[Start date] → [End date]

## Audience
[Who this is for and in what context.]

## Artifact types (max 3)
1. **[Type]** — [what an instance looks like] — [what it demonstrates] — [ship time]
2. **[Type]** — [what an instance looks like] — [what it demonstrates] — [ship time]
3. **[Type]** — [what an instance looks like] — [what it demonstrates] — [ship time]

## Cadence assumption
[Realistic hours/week × discount factor → artifacts/month.]

## Shipping floor
Every artifact:
- Lives at [public location standard]
- Has at least one specific external reader/viewer/user
- Has a readable entry-point

## Month-by-month
| Month | Planned artifacts | Rough topic | Why this one now |
|-------|------------------|-------------|------------------|
| [M1]  | [N × type]       | [topic]     | [reason]         |
| [M2]  | [N × type]       | [topic]     | [reason]         |
| ...   |                  |             |                  |
(at least 1 slack month per 3)

## Opener
[First artifact, shippable in 3–6 weeks. Full ship-pipeline exercise.]

## Anti-drift pre-commitments
- One-big-thing trap → [response]
- Perfectionism → [response]
- Story drift → [response]

## Existing work to include
[List what's already done that fits the story.]

## Flags
[Constraint mismatches, cadence concerns, audience ambiguity.]
```

---

## Verification

- [ ] The story sentence has no "and."
- [ ] Cadence is derived from hours, not wishes.
- [ ] Three or fewer artifact types.
- [ ] At least one slack month per three.
- [ ] Opener is small and near-term.
- [ ] Shipping floor is defined and publicly observable.
- [ ] Anti-drift responses cover the user's known patterns.
