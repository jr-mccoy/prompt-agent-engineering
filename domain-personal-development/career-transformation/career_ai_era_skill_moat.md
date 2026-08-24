---
title: "Separate Your Durable Skill Moat From Your Automatable Surface Area"
category: personal-development/career-transformation
description: "Split the user's working skillset into a durable moat (judgment, taste, relationships, deep context) versus automatable surface area, using evidence of where their skills actually hold value, then concentrate future investment on the one moat component with the most leverage."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - career
  - skill-moat
  - automation-risk
  - judgment
  - concentration
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/career-transformation/career_reskilling_roadmap.md
  - domain-personal-development/prompts/identity/identity_taste_development.md
---

# Separate Your Durable Skill Moat From Your Automatable Surface Area

**Objective:** Classify each of the user's real working skills as either **moat** (durable: judgment, taste, relationships, context) or **surface area** (automatable or commoditizing), then name the single moat component worth concentrating investment in — and the surface-area skills worth deliberately *stopping* investing in.

**When to use:** The user is deciding what to get better at over the next 1–3 years and doesn't want to over-invest in skills that tools are collapsing. Useful after `career_residual_skills_inventory.md` (which catalogs what they hold) to decide where the next hours go. Also for someone who feels they're "spreading thin" across too many skills. Not for: a one-off decision about a single job offer (use `major-decisions/personal_career_offer_evaluation.md`).

**Audience:** An individual planning their own skill investment. Not for rating a report or a team, and not clinical. If anxiety about automation is persistent or overwhelming, this prompt won't resolve it — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Skill list — what the user actually does.** 8–15 skills they use in real work, in their own words. Not a resume; the things that fill their actual days.
2. **For each skill, one concrete instance where it changed an outcome in the last 12 months.** What happened, what they did, what would have happened without them. Skills with no instance get flagged, not scored.
3. **Tools the user has seen touch each skill.** For each skill, note any AI system, script, vendor, or junior hire that already does part of it, and roughly how much (none / a slice / most).
4. **Where the user's judgment is trusted.** Situations where colleagues route decisions *to* them specifically — with a real example. If none exist, say so.
5. **Relationships and context the user holds.** Named people, systems, customer histories, or domains they carry in their head that a competent newcomer would not have.

If input 2 is missing for more than half the skills, refuse and ask for instances. A skill list without instances is a wish-list.

---

## Instructions

### Step 1 — Assign every skill to exactly one moat quadrant

| Quadrant | Definition | Evidence required |
|----------|------------|-------------------|
| **Judgment** | Deciding well under ambiguity, incomplete data, or conflicting pressure — where the "right answer" isn't retrievable. | An instance (input 2 or 4) where the user's call diverged from the obvious one and was right. |
| **Taste** | Knowing what's good, what to cut, what's off — before it can be justified. | An instance where the user rejected/reframed something because it wasn't right, and that mattered. |
| **Relationships / trust** | Access, credibility, or coordination that took time to build and is held with specific people. | Named people or a specific relationship from input 5. |
| **Deep context** | A model of a system, domain, customer base, or history that isn't written down anywhere. | Specific system/domain from input 5, plus how a newcomer would lack it. |
| **Surface area** | Everything else: production, formatting, retrieval, routine analysis, standard craft — real skills, but broadly held or being collapsed by tools. | Default bucket. Assign here unless a moat quadrant is earned by evidence. |

Default to **Surface area**. A skill enters a moat quadrant only on the evidence named. No "partial moat."

### Step 2 — Pressure-test each moat claim

For every skill placed in a moat quadrant, apply input 3: how much of it does a current tool or a modestly trained operator already do?
- If **most** of it is already done by a tool/junior, move it to **Surface area** regardless of how it feels.
- If a **slice** is automated but the hard core (the judgment/taste/context) remains, it stays in the moat — but name the automated slice explicitly so the user stops investing there.

### Step 3 — Rate each moat skill on leverage

For each skill still in a moat quadrant, rate two things:
- **Scarcity** in the user's real market (how many peers do this at their level): many / some / few.
- **Compounding** — does getting 20% better at this raise the value of the user's *other* skills, or is it flat? (compounds / flat)

A moat skill that is *few* + *compounds* is a concentration candidate.

### Step 4 — Name the surface area to deprioritize

List the skills that landed in Surface area, and mark the 2–4 the user is currently spending real time improving. These are the stop-investing candidates: real skills, poor return on further practice. Do not tell the user to stop *doing* them — tell them to stop *getting better* at them by hand and to route them to tools/delegation where possible.

### Step 5 — Pick one concentration bet

From the concentration candidates in Step 3, pick **one** moat component to concentrate investment in over the next quarter. Choose the one with the best combination of scarcity, compounding, and existing evidence base (you build fastest where you already have traction). Tie the bet to a physical, time-bounded first action — a specific piece of work, a specific relationship to deepen, a specific decision-type to take on — not "study" or "reflect."

State the trade: what the user stops sharpening (from Step 4) to fund this.

---

## Constraints

### Must
- Assign every skill to exactly one quadrant, defaulting to Surface area.
- Move any moat skill that tools/juniors already mostly do into Surface area.
- Name the automated slice of every partially-eroded moat skill.
- Produce exactly one concentration bet with a physical first action and a named trade-off.
- Cite a specific instance for every moat placement.

### Must Not
- Grant a moat quadrant on job title, tenure, or self-description without an instance.
- Use generic skill words (communication, leadership, strategy) as moat skills without forcing a specific instance.
- Recommend investing in more than one moat component — that's spreading thin, which is the problem.
- Tell the user everything they do is a moat, or that everything is doomed. Both are non-diagnostic.
- Moralize about "future-proofing" or cheerlead. Observe and rank.

---

## False-Positive Prevention

1. **Enjoying a skill ≠ moat.** The user may love a craft skill that is squarely surface area. Enjoyment is a reason to keep doing it, not evidence of durability. Grade on scarcity and automation exposure, not affection.
2. **"Context" is over-claimed.** Deep context only counts if a competent 6-month newcomer would genuinely lack it. If the context is written down or learnable in a quarter, it's surface area.
3. **Relationships decay if unfed.** A relationship moat from a job the user left two years ago is a lapsed asset, not a current one. Require the relationship to be currently live.
4. **Don't confuse being busy with a skill mattering.** High time-spend is not evidence of moat. Some surface-area skills eat the most hours precisely because they're routine.
5. **Recency bias on tools.** "A tool does this now" needs a real observation (input 3), not "AI can probably do this." Don't demote a moat skill on speculation, and don't protect a surface-area one on it.
6. **One concentration bet, not a portfolio.** If the output hedges across three bets, it has failed. The whole point is concentration.

---

## Output Format

```
## Skill map
| Skill | Quadrant | Instance evidence | Tool/junior exposure | Verdict |
|---|---|---|---|---|
| ... | Judgment/Taste/Relationships/Context/Surface | ... | none/slice/most | moat kept / demoted |

## Moat skills, rated
| Moat skill | Scarcity | Compounds? | Concentration candidate? |
|---|---|---|---|
| ... | many/some/few | yes/flat | yes/no |

## Stop sharpening (surface area you're currently investing in)
- [Skill] — route to [tool/delegation]; poor return on further hand-practice.

## The concentration bet
- **Invest in:** [one moat component] — because [scarcity + compounding + traction].
- **First action (this quarter):** [specific work / relationship / decision-type], by [date].
- **The trade:** stop sharpening [surface-area skill] to fund it.

Predicted check: within [N weeks], [observable — e.g., you're routed a decision-type you weren't before, or a piece of work lands that only the moat skill produces].
```

---

## Verification

- [ ] Every skill assigned to exactly one quadrant; Surface area is the default.
- [ ] Every moat placement cites a specific instance, not a title or self-description.
- [ ] Moat skills mostly done by tools/juniors were demoted to Surface area.
- [ ] Exactly one concentration bet, with a physical first action and a named trade-off.
- [ ] Stop-sharpening list names skills to route away, not to abandon.
- [ ] No generic skill words survived unchallenged.
- [ ] No cheerleading, no doom, no multi-bet hedge.
