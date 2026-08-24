---
title: "Pairing Criteria Design — Matching, Disqualifiers, and Re-match Triggers"
category: discipleship/pairing-and-relationship
description: "Design the criteria for matching someone seeking discipleship with someone able to offer it — separating hard safety constraints from fit preferences, defining disqualifiers and re-match triggers, and preventing the matching process from encoding bias or leaving people unmatched indefinitely."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - OC-03
  - QA-01
difficulty: advanced
tags:
  - discipleship
  - pairing-and-relationship
  - matching
  - safeguarding
  - program-design
updated: "2026-08-04"
related_prompts:
  - domain-discipleship/pairing-and-relationship/discipleship_relationship_covenant.md
  - domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md
  - domain-discipleship/program-operations/discipleship_participant_onboarding_design.md
  - domain-discipleship/mentor-equipping/discipleship_mentor_readiness_assessment.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md
---

# Pairing Criteria Design

**Objective:** Design how a program matches a person seeking discipleship with a person able to offer
it — separating hard safety constraints from genuine fit factors from mere preferences, defining what
disqualifies a pairing outright, and specifying the triggers that end or re-make a match, so that
matching is accountable rather than intuitive.

> **Boundary guardrail.** Matching criteria are not a substitute for screening. A pairing process
> cannot make an unscreened mentor safe, and criteria must sit downstream of the program's safeguarding
> policy — see `../program-operations/discipleship_safeguarding_and_conduct_policy.md`. Any pairing
> involving a minor or a vulnerable adult carries requirements this prompt does not state from memory;
> those are `[VERIFY]` with the safeguarding lead and qualified local counsel.

**When to use:** Standing up a pairing program, or fixing a matching process that is producing
mismatches, leaving people unmatched, or making decisions nobody can explain afterwards.

**When NOT to use:**
- You have not written the safeguarding policy — write it first; criteria depend on it.
- You are assessing one candidate's readiness — use
  `../mentor-equipping/discipleship_mentor_readiness_assessment.md`.
- You are designing what you collect from participants — use
  `../program-operations/discipleship_participant_onboarding_design.md`.
- You are launching small groups rather than pairs — use
  `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md`.

**Audience:** Program leads and platform designers building the matching layer.

---

## Inputs / Context

**Required:**

1. **The safeguarding policy.** Supplied or described. Its constraints become hard constraints here.
2. **Who is on each side.** The range of people seeking, the range offering, and the rough numbers —
   because a two-to-one imbalance produces different criteria than a balanced pool.
3. **What the relationship is for.** The scope of the discipling relationship, since criteria that make
   sense for a twelve-week foundations pathway differ from those for an open-ended one.
4. **Who decides.** Whether matching is done by a person, by participant choice, by algorithm, or a
   combination — and who can override.

**Optional:**

5. **Declared tradition (optional).** May impose pairing conventions — same-gender pairing, membership
   requirements, elder approval, a pastor's involvement — applied as that stream's rule and named as
   such.
6. **Known mismatches.** Pairings that went wrong before, and why. The strongest available evidence.
7. **Platform constraints.** What can actually be collected, stored, and acted on.

**If any required input is missing:** Ask clarifying questions before proceeding. If the safeguarding
policy does not exist, stop and say so — criteria written before it will have to be rewritten, and in
the interim they will look authoritative.

---

## Constraints

### Must

- Separate criteria into **three tiers**: hard safety constraints (never overridden), fit factors
  (weighted, tradeable), and preferences (honoured where possible, never blocking).
- Define **disqualifiers** — combinations that must not be matched regardless of other fit — and state
  who enforces them.
- Define **re-match and end triggers** in advance, so ending a mismatch is a normal procedure rather
  than a crisis requiring someone to be blamed.
- Include a **no-match protocol**: what happens to someone who cannot be matched, with a time limit
  beyond which they are actively offered something else rather than left in a queue.
- Audit the criteria for **bias**: whether they systematically disadvantage anyone by age, ethnicity,
  disability, class, language, marital status, or newness to the community.
- State the **override rule** — who may override a fit factor, on what basis, and where it is recorded.
- Say what the criteria **cannot predict**, since matching quality is only weakly knowable in advance.
- Make every criterion **collectable** — if onboarding cannot capture it, it is not a criterion.

### Must Not

- Allow any fit factor or preference to override a hard safety constraint.
- State a legal requirement about background checks, minors, data retention, or reporting. Mark
  `[VERIFY]` and route to `domain-legal/` and the safeguarding lead.
- Compute a single numeric compatibility score and match on it alone, without a human able to see and
  question the reasoning.
- Encode a preference for people who are demographically or socially similar to existing mentors, which
  is how matching quietly becomes exclusionary.
- Invent matching research, compatibility models, or statistics about mentoring outcomes.
- Leave someone unmatched indefinitely with no protocol and no communication.
- Quote Scripture text from memory; addresses only where a criterion is grounded in a passage.
- Treat a mentee's difficulty, doubt, or messiness as a reason to deprioritize them for matching.

### Tradition-neutral stance (Must / Must Not)

- **Must:** where a tradition requires a pairing convention — same-gender pairing, membership standing,
  elder or pastoral approval, marital-status considerations — apply it as that stream's rule, record it
  as tradition-specific rather than as a safety constraint, and note other streams differ.
- **Must Not:** present one tradition's pairing convention as a universal safeguarding requirement, or
  import a convention the program's own tradition does not hold.

---

## Instructions

### Step 1 — Import the safety constraints

Take every constraint the safeguarding policy imposes and restate it as a hard matching constraint.
These are not weighed, traded, or overridden. Mark any point with legal weight `[VERIFY]`.

### Step 2 — Identify the genuine fit factors

Distinguish factors that plausibly affect whether the relationship works — life stage, availability
overlap, language, what the seeker is asking for versus what the mentor can offer, experience with a
particular season — from factors that merely feel relevant. Weight them and say why.

### Step 3 — Separate preferences

List what participants may prefer that will be honoured where possible but never block a match. Say
plainly which stated preferences fall here, since participants often express a preference as a
requirement.

### Step 4 — Define disqualifiers

Name combinations that must not be matched: existing conflict, a prior harmful relationship, a
supervisory or employment relationship, close family, an unresolved complaint, or anything the
safeguarding policy names. State who checks and who enforces.

Include **church-internal power asymmetry**, which is the most common one here and the most often
missed: an elder, pastor, staff member, group leader, or volunteer coordinator discipling someone whose
standing, role, membership, participation, or reference they influence. The workplace and campus variants
already treat this as a deal-breaker on the employer's and the institution's lines
(`../context-variants/discipleship_context_workplace_and_marketplace.md`,
`../context-variants/discipleship_context_campus_ministry.md`); the same asymmetry inside a church is not
a lesser version of it. Where the pool is small enough that this rules out most available mentors, the
answer is a mentor from outside the person's own sphere or a longer wait — not a match with a declared
caveat attached.

### Step 5 — Write the re-match and end triggers

Define in advance what ends a pairing: either party requests it, a stated number of missed meetings, a
safeguarding concern, a boundary breach, a change in circumstances, or scope drift. Make requesting a
re-match require no justification, and say so.

### Step 6 — Audit for bias

Walk the criteria and ask, for each: who does this systematically disadvantage? Pay particular
attention to newness, language, disability, work pattern, class, and single or divorced status. Where a
criterion disadvantages someone without a safety justification, remove or rework it.

### Step 7 — Write the no-match protocol and state the limits

Define what happens when someone cannot be matched: how long before something else is actively offered,
what that is, and who tells them. Then state what the criteria cannot predict.

---

## Output Format

Produce exactly this structure.

```
# Pairing Criteria — [program]

## Tier 1: Hard Safety Constraints (never overridden)
| Constraint | Source | Who enforces |
|---|---|---|
| [..] | safeguarding policy | [role] |

**[VERIFY]** Requirements involving minors, vulnerable adults, background checks, and data handling
are jurisdiction-specific. Confirm with the safeguarding lead and qualified counsel — see
`domain-legal/`. Nothing here states what the law requires.

## Tier 2: Fit Factors (weighted, tradeable)
| Factor | Weight | Why it plausibly matters | Collectable at onboarding? |
|---|---|---|---|

## Tier 3: Preferences (honoured where possible, never blocking)
| Preference | Note |
|---|---|

## Tradition-Specific Conventions
| Convention | Stream | Applied here? |
|---|---|---|
[Recorded separately from safety constraints.]

## Disqualifiers — Never Matched
| Combination | Why | Who checks |
|---|---|---|
| Mentor influences the mentee's standing, role, membership, or reference in this church | Power asymmetry — same line as employer and campus | [..] |

## Re-match and End Triggers
| Trigger | Who can invoke | Justification required? | What happens |
|---|---|---|---|
| Either party requests it | either | **No** | [..] |

## Bias Audit
| Criterion | Who might it disadvantage? | Safety justification? | Kept / reworked / removed |
|---|---|---|---|

## Override Rule
- Who may override a Tier 2 factor: [role]
- On what basis: [..]
- Recorded where: [..]
- **Tier 1 is never overridden.**

## No-Match Protocol
- Maximum time unmatched before action: [..]
- What is actively offered instead: [..]
- Who communicates, and how: [..]

## What These Criteria Cannot Predict
[Matching quality is weakly knowable in advance. These criteria reduce obvious mismatches; they do not
produce good relationships, and a well-matched pair can still not work.]
```

---

## Verification

- [ ] Safety constraints are a separate tier and are never weighed or traded.
- [ ] Every fit factor is collectable at onboarding; uncollectable factors are removed.
- [ ] Re-match on request requires no justification, and the output says so explicitly.
- [ ] The bias audit covers newness, language, disability, work pattern, class, and marital status.
- [ ] A no-match protocol exists with a time limit and a named alternative.
- [ ] No legal requirement is stated; all such points are `[VERIFY]` and routed.

---

## False-Positive Prevention

❌ **DON'T:**
- Match on a single compatibility score. When a pairing goes wrong, nobody can explain the reasoning,
  and the score will have quietly encoded whatever bias was in the weights.
- Treat "similar to our existing mentors" as fit. It is the mechanism by which programs become
  homogeneous and then wonder why newcomers do not stay.
- Let a preference block a match while calling it a requirement. Participants routinely state
  preferences in absolute terms; the tiering exists to handle exactly that.
- Deprioritize the people who most need matching because they seem difficult, doubting, or messy.
- Leave someone in an unmatched queue with no communication. It reads as rejection and usually ends
  their engagement.
- Require a justification to end a pairing. It keeps people in relationships that are not working,
  which is worse for both.

✅ **DO:**
- Import safeguarding constraints verbatim as Tier 1, and make it structurally impossible to trade
  them against fit.
- Test each fit factor against whether onboarding can actually collect it. Uncollectable criteria
  become guesses at the point of matching.
- Write the end triggers before the first match, so the first mismatch is handled as procedure rather
  than as failure.
- Run the bias audit with specific groups named, not as a general principle. General commitments to
  fairness do not surface a criterion that excludes shift workers.
- Set a hard time limit on being unmatched, with something real offered at it.
- State plainly that good matching does not produce good relationships — it only removes obvious
  mismatches.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** safety constraints are imported before fit factors are
  invented, so the design cannot produce criteria that trade against safeguarding.
- **RT-02 (Multi-Dimensional Analysis Framework):** the three-tier separation (safety / fit /
  preference) plus the bias audit analyzes matching along axes that a single compatibility model
  collapses into an unexaminable score.
- **CM-02 (Constraint Specification):** the never-overridden Tier 1 rule, the collectability rule, and
  the no-justification-to-end rule are hard constraints against the characteristic failures of
  matching systems.
- **OC-03 (Markdown Table Specification):** the tier tables and the bias-audit table force every
  criterion to declare its justification and its enforcement owner in the same row.
- **QA-01 (Self-Verification):** the verification block checks tier separation, collectability, and
  bias coverage before criteria go live, and confirms no legal claim was asserted.

---

## Related Prompts

- [`discipleship_relationship_covenant.md`](discipleship_relationship_covenant.md) — what the matched
  pair agrees once paired
- [`../program-operations/discipleship_safeguarding_and_conduct_policy.md`](../program-operations/discipleship_safeguarding_and_conduct_policy.md) —
  supplies the Tier 1 constraints; write it first
- [`../program-operations/discipleship_participant_onboarding_design.md`](../program-operations/discipleship_participant_onboarding_design.md) —
  collects what the fit factors require
- [`../mentor-equipping/discipleship_mentor_readiness_assessment.md`](../mentor-equipping/discipleship_mentor_readiness_assessment.md) —
  screening that must happen before matching
- [`domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md`](../../domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md) —
  the small-group launch counterpart
