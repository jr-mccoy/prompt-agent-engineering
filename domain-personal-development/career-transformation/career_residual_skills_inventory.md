---
title: "Inventory Residual Skills That Survive Automation"
category: personal-development/career-transformation
description: "Catalog the judgment, taste, and context the user actually holds — separating real residual skills (scarce, transferable, defensible) from skills they wish they had, tasks they happen to do, or credentials that aren't skills. Produces a ranked inventory keyed to evidence."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - career
  - skills-inventory
  - judgment
  - taste
  - repositioning
updated: "2026-04-21"
related_prompts:
  - domain-personal-development/career-transformation/career_coordination_tax_audit.md
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/career-transformation/career_90_day_repositioning_plan.md
  - domain-personal-development/prompts/agency/agency_feedback_extraction.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
---

# Inventory Residual Skills That Survive Automation

**Objective:** Produce a ranked inventory of the user's residual skills — the judgment, taste, and context that remain scarce when broad task automation is priced in. Force evidence for every claim. Refuse credential-lists, wish-lists, and generic skill words.

**When to use:**
- Immediately after `career_role_structural_vulnerability.md` identifies axes at risk, to understand what the user actually still carries.
- The user is preparing a 90-day repositioning plan and needs to know what they're building from.
- The user is writing a narrative for a job search, a pitch, or an internal move and needs to separate real scarcity from generic claims.
- A manager is preparing a development conversation for someone on their team.

**Don't use when:** The user wants affirmation. This prompt strips skills that aren't backed by evidence.

**Audience:** An individual cataloging their own skills, or (more rarely) a manager preparing a reasoned skills picture of someone they know well and have observed directly.

---

## Inputs Required

Ask for all of these; refuse to inventory without 1, 2, 3, and 5.

1. **Three specific work episodes from the last 24 months where the user's judgment changed an outcome.** What was happening, what they decided, why others would have decided differently, and what happened after.
2. **Three specific work episodes where the user's taste changed a decision.** Not "big picture" — a specific moment where the user rejected, reframed, or rewrote something because it wasn't right, and was right to do so.
3. **The user's deep context.** What domain, system, org, customer base, or history does the user actually hold in their head? One to three domains.
4. **Feedback the user has received on specific work in the last year.** Verbatim if possible. If none exists, note that; don't substitute praise the user imagines getting.
5. **Work the user has shipped or delivered in the last 12 months that they're willing to point to.** 2–5 items. Can be artifacts, outcomes, or documented contributions.
6. **Skills the user believes they have that they can't source with the above.** Optional. These will be flagged as unsupported.

If inputs 1 or 2 read as generic ("I make good decisions"), ask for specific instances. Do not proceed with generic inputs.

---

## Instructions

### Step 1 — Classify every candidate skill into exactly one tier

| Tier | Definition | Evidence required |
|------|------------|-------------------|
| **Residual** | Scarce, transferable, defensible. Hard for a peer to replicate in under 6 months even with the same task list. | At least one specific episode from inputs 1–3, plus corroborating feedback (input 4) OR artifact (input 5). |
| **Compounding** | Growing in value; tied to a specific domain, system, or relationship network. Loses value if the user leaves the current context but holds it today. | Specific domain context (input 3) plus at least one episode. |
| **Commoditized** | Real skill, but broadly held or being rapidly eroded by tools. Still useful, not differentiating. | At least one episode OR artifact. |
| **Aspirational** | The user wants this skill or claims it but the evidence isn't there. | — (no evidence supports it). |
| **Credential-only** | A certification, title, or past role that isn't an active skill. | — (flagged as not a skill). |

Do not create "intermediate" tiers. Force a classification.

### Step 2 — Name skills in testable form

A residual skill must be named specifically enough that a hypothetical observer could design a test for it. Reject these as too generic:

- "Communication" → force into "Translating dense technical tradeoffs for a non-technical exec audience" or similar.
- "Leadership" → force into something like "Holding a contentious roadmap decision while the room disagrees in real time."
- "Problem solving" → force into "Decomposing a post-incident root cause when the obvious explanation is wrong."

If the user resists specificity, note the resistance — it often indicates the skill isn't as real as hoped.

### Step 3 — Score each Residual and Compounding skill on three dimensions

- **Scarcity.** How many people in the user's extended network (not the world) can do this at the same level? Bucket: many / some / few / very few.
- **Transferability.** Does the skill travel outside the current role / company / domain? Fully / partially / no.
- **Defensibility against AI + cheaper labor.** How long until a current or likely-near-future AI system, plus a modestly trained operator, can do 80% of what this skill does? Bucket: already / 0–12 mo / 12–36 mo / 3+ yr / structurally defensible.

If defensibility is "already" or "0–12 mo," the skill is NOT Residual; reclassify to Commoditized.

### Step 4 — Produce the ranked inventory

Rank Residual and Compounding skills by a simple composite of (scarcity × defensibility × transferability), breaking ties with evidence strength (more specific evidence wins).

Commoditized skills are listed but not ranked — they are real but not differentiating.

Aspirational and Credential-only skills are listed once at the end with a one-line note each; they are not counted as skills.

### Step 5 — Name the counterfactuals

For each Residual skill, write the counterfactual in one sentence: "If a competent peer replaced me tomorrow, what would specifically not happen for the next 6–12 months?" If the answer is "nothing concrete," the skill is not Residual — downgrade.

### Step 6 — Flag inventory shape

Write 3–5 sentences on the shape of the inventory:

- Is the user concentrated in one kind of skill (all judgment, no taste; all context, no decision history)?
- Are all Residual skills tied to one domain (concentration risk if the user leaves the domain)?
- Is there a Residual skill that also appeared as a Counterweight in `career_role_structural_vulnerability.md`? Call that out — it's a linchpin.
- Is the inventory thin (fewer than 2 Residual skills)? Say so. Do not pad.

### Step 7 — Verify and output

Run the verification checklist before delivering.

---

## Constraints

### Must
- Every Residual skill is named specifically enough to design a test for.
- Every Residual and Compounding skill cites at least one specific episode from inputs 1–3.
- Defensibility "already" or "0–12 mo" forces reclassification to Commoditized.
- Aspirational and Credential-only are listed with evidence gaps named.
- Inventory shape is stated honestly, including thinness.

### Must Not
- Infer skills from role title or job description.
- Use generic skill words (communication, leadership, problem solving, strategic thinking, execution) as residual skills without forcing specificity.
- Create an "intermediate" tier or soften a classification.
- Pad the inventory with commoditized or aspirational skills to hit a count.
- Claim defensibility of Residual skills beyond what the evidence supports.
- Prescribe how to use the inventory — that's the repositioning prompt's job.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Treat the user's self-assessed list at face value. Every claimed skill must be sourced to episodes.
- Accept credentials as skills. A degree or past role is evidence of having been in the room, not of current skill.
- Mark "context" as Residual without specifying which system / domain / customer base and how deep.
- Let one impressive episode carry a skill into Residual. A single episode without corroboration (feedback or artifact) is Compounding at best.
- Grade defensibility by intuition. Tie it to a specific plausible substitute: "Claude + a moderately trained analyst could do 80% of this within 12 months" or "no substitute with comparable quality exists today."

✅ **DO:**
- Quote episode details verbatim as evidence.
- Push back on generic skill names; force specific ones.
- Downgrade aggressively. An honest thin inventory is more useful than a padded one.
- Treat "the user is the only person who…" as a claim requiring evidence, not a conclusion.
- Call out concentration risk if every Residual skill sits in one domain.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Inventory inflates skills to make the user feel reassured. Produces a confidently ranked list with no evidence strength behind it, and the user bets a career move on it.

❌ **UNHELPFUL failure:** Refuses to credit anything as Residual, or hedges every skill. User gets no signal on what they actually hold.

✅ **Quality check:** Every Residual skill, challenged by a skeptical senior operator, would survive on the evidence provided. Skills that wouldn't are not Residual.

---

## Output Format

```markdown
# Residual Skills Inventory — [User Role + Domain]

## Ranked Inventory

### Residual Skills (scarce, transferable, defensible)
#### 1. [Specific skill name]
- **Episode evidence:** [Quote or paraphrase from inputs 1–3]
- **Corroborating feedback / artifact:** [From input 4 or 5]
- **Scarcity:** [many / some / few / very few]
- **Transferability:** [full / partial / none]
- **Defensibility:** [already / 0–12 mo / 12–36 mo / 3+ yr / structural]
- **Counterfactual:** If a competent peer replaced me tomorrow, [what would not happen].

#### 2. [...]

### Compounding Skills (growing, context-tied)
[Same structure, shorter.]

### Commoditized Skills (real but not differentiating)
- [Skill] — [one-line why it's commoditized]

### Aspirational (user claimed; evidence doesn't support)
- [Skill] — [evidence gap]

### Credential-Only (not a current skill)
- [Credential / past role] — [why flagged]

## Inventory Shape
- Concentration: [domain(s) the Residual skills sit in]
- Distribution: [judgment / taste / context mix]
- Linchpin with vulnerability counterweight: [yes/no + which skill]
- Thinness: [# Residual skills; honest read]

## Open Questions
- [Evidence the user could surface that might promote a Compounding skill to Residual, or vice versa]
```

---

## Verification

- [ ] Every Residual skill has episode evidence AND corroborating feedback or artifact.
- [ ] Every skill is named specifically (not "communication" or "leadership" or "execution").
- [ ] Defensibility grades drive reclassification where applicable.
- [ ] Aspirational and Credential-only are listed with gap notes.
- [ ] Inventory shape is stated honestly, including thinness.
- [ ] No prescriptive career advice.
- [ ] Generic skill words that survived are flagged, not accepted silently.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is an evidence-keyed inventory, not an affirmation list.
- **ST-02 (Structured Sequential Instructions):** Seven steps force classification → specificity → scoring → ranking → counterfactual → shape → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids role-title inference, generic skill words, and intermediate tiers.
- **DS-01 (Framework Application):** Five-tier taxonomy is the framework; disallowing intermediate tiers keeps it honest.
- **QA-01 (Self-Verification):** Every skill must survive the "could this be defended to a skeptic?" check; failures are downgraded.
