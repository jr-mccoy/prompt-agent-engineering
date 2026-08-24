---
title: "Cofounder and Business Partner Selection — Failure Mode Audit with Pre-Mortem"
category: personal-development/major-decisions
description: "Evaluate a prospective cofounder or business partner against the failure modes that most commonly destroy co-founded companies. Covers skill complementarity, observed work ethic, values alignment on hard cases (not easy ones), conflict-resolution patterns, financial alignment, vesting and equity terms, exit-trigger clarity, and behavior under stress. Forces a pre-mortem: imagine the partnership has failed in 3 years, then reason backward to what the cause was. Counters the bias toward partnering with people you like rather than people you can work with through the hard parts."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - personal-decisions
  - cofounder
  - partnership
  - startup
  - relationships
updated: "2026-05-11"
reasoning:
  styles: [analytic, dialectical, pre-mortem, systems]
  stakes: high
  horizon: years
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: cross_domain
  collaboration: pair
  output_format: structured
  user_role: [founder, entrepreneur, executive]
  mode: [decide, audit, diagnose]
related_prompts:
  - domain-personal-development/major-decisions/personal_relocation_decision.md
  - domain-personal-development/major-decisions/personal_difficult_relationship_audit.md
  - domain-personal-development/major-decisions/personal_quit_or_persist.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/decisioning_regret_minimization.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
---

# Cofounder and Business Partner Selection

**Objective:** Evaluate a prospective cofounder or business partner against the failure modes that most commonly end co-founded companies. Cofounder breakups are among the top causes of early-stage company failure, and they usually result from problems that were present from the start but unexamined — divergent work ethics not revealed until the pressure arrived, values that seemed aligned until a hard decision surfaced them differently, equity terms never clearly stated, or exit conditions never discussed. This prompt surfaces those before they become crises.

**When to use:**
- Considering bringing on a cofounder for a company that doesn't yet have one.
- Evaluating a prospective business partner (agency, practice, LLC) before committing.
- Early enough that the terms can still be shaped (before founding documents are signed).
- Re-evaluating a partnership that's been informal and is about to become formal.

**When NOT to use:**
- The partnership is already legally constituted — this is a pre-commitment evaluation tool.
- You're evaluating a hired executive, not a partner with equity and governance rights.
- The partner is being considered for a non-ownership role — use offer evaluation instead.

**Audience:** Founders and entrepreneurs considering bringing on an equity partner at the company formation stage or early-stage inflection point.

---

## Inputs / Context

1. **The prospective partner.** Background, current situation, skills, track record. What they bring to the company.
2. **The company.** Stage, what's been built, what the equity split being considered is.
3. **How you know them.** Working relationship history (if any), personal relationship, how long and in what contexts.
4. **What's driving the partnership.** Why this person, why now?
5. **The gaps you're trying to fill.** What can they do that you can't, and vice versa?

---

## Constraints

### Must
- Evaluate observed behavior, not stated values or self-description. Anyone can say they're hard-working and values-aligned. What have you seen them do under pressure, under disappointment, under disagreement?
- Walk all eight dimensions explicitly: skill complementarity, work ethic, values alignment, conflict-resolution, financial alignment, vesting/equity terms, exit-trigger clarity, behavior under stress.
- Force the pre-mortem: the partnership has failed in 3 years. Reason backward through what caused the failure.
- Test values alignment on the hard cases, not the easy ones. Agreement on "we want to build a great company" is not alignment; alignment is what each person does when money is tight, an employee needs to be let go, a customer demands something you don't want to deliver, or you disagree about strategy.
- Assess vesting and equity terms for clarity. Ambiguity in equity agreements is a later-stage landmine.
- Include the option that the right answer is no partner.

### Must Not
- Confuse liking the person with working-compatibility. These are correlated but not equivalent.
- Accept self-reports of past behavior without triangulation. How they describe their previous work, conflicts, and failures tells you something; what others observed tells you more.
- Skip the financial alignment check. Divergent runway expectations (one partner has 6 months of savings; the other has 5 years) or divergent risk tolerances create pressure that breaks partnerships.
- Treat vesting as a formality. Founder vesting with a cliff is one of the most important structural protections against a partner who leaves early; absence of it is a major risk.
- Allow "we'll figure it out" to substitute for exit-trigger clarity.

---

## Instructions

### Step 1 — Skill complementarity
Map the skills the company needs against what you bring and what the prospective partner brings:
- Where do you overlap? Overlap isn't inherently bad (two strong engineers can be fine) but it means the gap is elsewhere.
- Where do they fill a genuine gap that the company needs filled?
- Is the gap they fill actually the blocking constraint on the company, or is it a nice-to-have?
- Is the skill gap fillable through a hire rather than a partner? (A hire is cheaper, more controllable, and reversible. A cofounder is none of those things.)

### Step 2 — Work ethic match (observed, not stated)
- What have you seen them do, not what they say about themselves?
- Have you worked with them under pressure, on a deadline, on something that failed? What was their behavior?
- Are your expected work rhythms (hours, focus, pace) compatible?
- What happens when they're not interested in a task that still needs to get done?

### Step 3 — Values alignment on hard cases
Name five scenarios that would require a hard call and ask (explicitly, in conversation) what each of you would do:
- A customer wants a feature that compromises your values — they'll leave if you don't build it.
- An early employee isn't working out. When do you let them go, how?
- You disagree about the direction of the company in a meeting — neither person concedes.
- The company needs more money; one option dilutes significantly, another means cutting burn including salaries.
- One partner wants to sell; the other doesn't.

Look for: does the other person engage with these questions seriously, avoid them, or give you whatever answer they think you want?

### Step 4 — Conflict-resolution patterns
- When have you disagreed with this person? How did it go?
- Do they move to resolution or to winning?
- Can they be wrong and handle it? Can they tell you you're wrong?
- What does their conflict pattern look like after 48 hours — do they return to normal, or do they carry it?

### Step 5 — Financial alignment
- Runway: how many months of personal financial runway does each partner have?
- Salary expectations: what does each partner need/want from the company as it scales?
- Risk tolerance: one partner willing to work at $0 salary for 18 months; the other needs $80K at month 6 — this creates a crisis.
- Outcome expectations: are you building to IPO, to $10M ARR and lifestyle, or to an early acquisition? Divergent outcomes goals are a slow-building conflict.

### Step 6 — Vesting and equity terms
- What's the equity split? Is it justified by contribution, or by negotiating power at the moment of founding?
- Is there a vesting schedule with a cliff? (Standard: 4 years / 1-year cliff.)
- What happens to equity if a partner leaves before fully vested?
- What happens to equity if a partner is terminated?
- Are there buyback rights at what price?
- Is there a drag-along or deadlock resolution mechanism in the governance documents?

### Step 7 — Exit-trigger clarity
- Under what conditions does each partner have the right to exit? The obligation to exit?
- If you fundamentally disagree about the direction of the company and can't resolve it — what's the resolution mechanism? (Buy-sell? Arbitration? Co-CEO deadlock clause?)
- If the company becomes acquirable below what one partner wants to sell at — who wins?
- Under what conditions would either of you consider replacing the other in their role?

### Step 8 — Behavior under stress
- How does this person behave when things go badly? When they're embarrassed? When they've been publicly wrong?
- How do they treat people with less power when they're stressed?
- What happens to their decision quality when they're afraid?

### Step 9 — Pre-mortem
Imagine: it's three years from now. The partnership has failed — broken acrimoniously. The company either failed or is continuing without one of you. Work backward:
- What was the precipitating event?
- What were the warning signs at formation that were visible but not addressed?
- Which of the dimensions above (work ethic, financial alignment, exit terms, conflict style) was the rupture point?
- Now: are any of those warning signs visible today?

### Step 10 — Decision
- Go: proceed with this partner, with the specific terms and structural protections named.
- Counter: proceed if specific concerns (equity terms, vesting, exit clarity) are addressed.
- Wait: gather more evidence (work together on something concrete first) before committing.
- No-go: the risk profile from the pre-mortem analysis exceeds the strategic value of the partnership.

---

## False-Positive Prevention

1. **Affinity-for-compatibility substitution.** You like this person. That makes you want to believe the working relationship will be good. These are correlated but not the same thing.
2. **Stated-values acceptance.** "I value hard work and integrity" is unfalsifiable until tested. Require observed evidence from working interactions.
3. **Hard-case avoidance.** If the prospective partner dodges the hard-case scenarios or gives you what you want to hear, that is data.
4. **Urgency pressure.** "We need to move fast" is frequently offered as a reason to skip the diligence that would reveal the incompatibility.
5. **Sunk-relationship cost.** You've been talking to this person for 6 months and both of you have invested time. That's not a reason to proceed with a partnership that has red flags.
6. **Vesting-as-formality.** Founder vesting with a cliff is one of the most important structural tools available. "We trust each other" is not a substitute.
7. **Financial-alignment skip.** Divergent runway = divergent time horizon = ticking clock on the partnership. Ask directly.
8. **Exit-trigger deferral.** "We'll figure it out if we get there" — the time to agree on exit terms is before the conflict, not during it.
9. **Pre-mortem skip.** The exercise feels pessimistic. It is the most useful part of this analysis.

---

## Output Format

```
# Cofounder evaluation — [name / role]

## Skill map
| Skill area          | Me | Partner | Company needs | Gap filled? |
|---------------------|-----|---------|---------------|-------------|
| [Area 1]            |     |         |               |             |
| [Area 2]            |     |         |               |             |
| Hire-vs-partner gap? | — | —       | [yes/no — which gaps are better filled by hire] |

## Work ethic (observed)
- Interactions under pressure: [...]
- Rhythm compatibility: [...]
- Ownership of unpleasant tasks: [...]

## Values alignment — hard cases
| Scenario              | My position | Partner's position | Aligned? |
|-----------------------|-------------|-------------------|----------|
| [Scenario 1]          |             |                   |          |
| [Scenario 2]          |             |                   |          |

## Conflict-resolution
- Known disagreements and how they resolved: [...]
- Move-to-resolution or move-to-winning: [...]
- Carry-forward behavior: [...]

## Financial alignment
| Factor                | Me | Partner | Alignment? |
|-----------------------|-----|---------|------------|
| Personal runway (mo)  |     |         |            |
| Salary expectation    |     |         |            |
| Risk tolerance        |     |         |            |
| Outcome goal          |     |         |            |

## Vesting and equity terms
- Proposed split: [X% / Y%] — justified by: [...]
- Vesting schedule: [4yr / 1yr cliff — or: not yet established (risk)]
- Departure clause: [...]
- Deadlock mechanism: [...]

## Exit-trigger clarity
- Voluntary exit terms: [clear / ambiguous / not discussed]
- Forced exit terms: [clear / ambiguous / not discussed]
- Acqui-hire / sale disagreement mechanism: [...]

## Behavior under stress (observed or inferred)
- [evidence from observed behavior or situations]

## Pre-mortem
"In 3 years the partnership has failed acrimoniously. The cause was:"
- Precipitating event: [...]
- Warning signs visible today: [...]
- Which dimension was the rupture point: [...]

## Decision
- Recommendation: [go / counter / wait / no-go]
- If counter: specific terms or conditions: [...]
- Structural protections required before proceeding: [...]
- Calibration anchor (write down today): "I am partnering with [name] because [specific skills/evidence], having addressed [specific risk], with vesting terms of [terms] and exit clarity on [mechanisms]."
```

---

## Verification

- [ ] All eight dimensions (skill, work ethic, values, conflict, financial, vesting, exit, stress) evaluated.
- [ ] Values alignment tested on hard cases, not easy ones.
- [ ] Work ethic assessment based on observed behavior, not self-report.
- [ ] Financial alignment (runway, salary, risk tolerance, outcome goal) assessed.
- [ ] Vesting terms (schedule, cliff, departure clause) specified or flagged as missing.
- [ ] Exit-trigger clarity assessed — "we'll figure it out" flagged as a risk if present.
- [ ] Pre-mortem completed: failure scenario reasoned backward.
- [ ] Hire-vs-partner question asked for each skill gap.
- [ ] Recommendation includes structural protections required before proceeding.
- [ ] Calibration anchor written.
