---
title: "Risk Register Builder — A Maintainable Register, Not a One-Off List"
category: risk/register
description: "Build a structured, maintainable risk register for a project, product, initiative, or operation. Each risk carries a category, likelihood and impact scores, a composite score, a named owner, mitigation and monitoring, an escalation trigger, and a residual-risk estimate after mitigation. Enforces ownership and review cadence so the register stays alive instead of decaying into a stale spreadsheet."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - risk-management
  - risk-register
  - mitigation
  - ownership
  - governance
updated: "2026-05-10"
reasoning:
  styles: [systems, structural, probabilistic]
  stakes: variable
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [pm, operator, executive, founder, analyst]
  mode: [audit, document, plan]
related_prompts:
  - domain-risk/risk_heat_map.md
  - domain-risk/risk_tail_risk_scan.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Risk Register Builder

**Objective:** Produce a structured risk register for a defined project, product, initiative, or operation. For each risk, capture a name, category, likelihood (1–5), impact (1–5), composite score, named owner, mitigation, monitoring approach, escalation trigger, and residual-risk estimate after mitigation. The deliverable is a *maintainable* register with explicit ownership rules and a review cadence — not a one-time brainstorm that rots in a folder. The discipline this enforces: every risk has exactly one accountable owner, a concrete trigger that fires escalation, and a residual estimate so the team knows what's left after the mitigation is applied.

**When to use:**
- Standing up risk governance for a new project, launch, or operation.
- An existing risk list is a stale brainstorm with no owners, no scores, and no review rhythm.
- A stakeholder, board, or auditor wants a defensible, maintained register.
- Before a major milestone where uncatalogued risks would be expensive.

**When NOT to use:**
- Hunting for unknown tail / black-swan risks — use `risk_tail_risk_scan.md`; the register captures *known* risks.
- Visualizing and force-ranking an existing register — use `risk_heat_map.md`.
- Process- or product-level failure decomposition with severity/occurrence/detectability — use `risk_fmea_analysis.md`.
- A throwaway decision with no ongoing exposure; a register implies maintenance you won't do.

**Audience:** Project managers, operators, founders, program leads, executives, and risk analysts who own delivery and need a living register others can read and act on.

---

## Inputs / Context

1. **The scope.** What the register covers — the project, product, initiative, or operation, and its boundaries. One paragraph.
2. **Objectives at stake.** What success looks like; risks are threats to these.
3. **Time horizon.** The window the register governs (e.g., next quarter, through launch, ongoing operation).
4. **Known risks / concerns.** Any risks the user already has in mind, however rough.
5. **Owners available.** The people or roles who can own risks. Without real owners, the register is decorative.
6. **Risk appetite.** How much residual risk is tolerable, in qualitative or threshold terms (e.g., "no high-impact risk may sit unmitigated").
7. **Review cadence preference.** How often the register will be revisited, if the user has one.

---

## Constraints

### Must
- Assign every risk to exactly **one** of these categories: financial / operational / strategic / regulatory / reputational / technical / people / external.
- Score **likelihood (1–5)** and **impact (1–5)** with the anchored scales below, and compute **composite = likelihood × impact** (1–25).
- Give every risk **exactly one named owner** (a person or a single accountable role, never "the team").
- Write a **mitigation** that is a concrete action, not a restatement of the risk.
- Define a **monitoring approach**: the observable and the cadence that tells the owner the risk is moving.
- Define an **escalation trigger**: the specific condition that forces the risk up to a decision-maker.
- Estimate **residual likelihood and impact after mitigation**, and a residual composite. If the mitigation doesn't move the score, say so and explain why it's still worth doing (or drop it).
- End with **ownership rules** and a **review cadence** so the register is maintained.

### Must Not
- Use "team" or "everyone" as an owner. Shared ownership is no ownership.
- Write a mitigation that just negates the risk ("mitigation: don't let it happen").
- Leave residual risk blank or equal to inherent risk without justification.
- Collapse two distinct risks into one row because they share a cause; split them if they have different owners or mitigations.
- Score by gut without applying the anchored scales — anchoring is what makes scores comparable across risks and over time.
- Produce a static artifact with no review cadence; an unmaintained register gives false comfort.

---

## Instructions

### Step 1 — Frame the scope and objectives
State what the register covers and the objectives the risks threaten. One paragraph. This bounds what belongs in the register and what doesn't.

### Step 2 — Surface candidate risks across all eight categories
Walk each category deliberately and ask "what could go wrong here?":
- **Financial** — budget, funding, cash flow, cost overrun, revenue shortfall.
- **Operational** — delivery, capacity, process failure, throughput.
- **Strategic** — wrong bet, market shift, competitor move, misaligned priorities.
- **Regulatory** — compliance, licensing, legal change, audit exposure.
- **Reputational** — public perception, trust, brand damage.
- **Technical** — system failure, scalability, security, technical debt.
- **People** — key-person dependency, hiring, attrition, skills gap, morale.
- **External** — supply chain, macro conditions, geopolitical, weather, third parties.

Aim for breadth first; you'll prune in Step 5.

### Step 3 — Score each risk on anchored scales
**Likelihood (1–5):**
1. Rare — would be surprising (<10% in the horizon).
2. Unlikely — possible but not expected (~10–30%).
3. Possible — could go either way (~30–55%).
4. Likely — expected more often than not (~55–80%).
5. Almost certain — expect it (>80%).

**Impact (1–5):**
1. Negligible — absorbed without noticeable effect.
2. Minor — small cost/delay, recoverable within normal operations.
3. Moderate — meaningful cost/delay, requires management attention.
4. Major — threatens a key objective or milestone.
5. Severe — threatens the project/operation's viability or causes lasting damage.

Compute **composite = likelihood × impact**.

### Step 4 — Assign a single owner per risk
Name one person or one accountable role. The owner is responsible for the mitigation, the monitoring, and pulling the escalation trigger. If no real owner exists, that is itself a finding — flag it.

### Step 5 — Write mitigation, monitoring, and escalation trigger
For each retained risk:
- **Mitigation:** a concrete action that reduces likelihood, impact, or both.
- **Monitoring approach:** the observable the owner watches and on what cadence.
- **Escalation trigger:** the specific condition (a threshold, a date, an event) that forces the risk to a decision-maker.

Prune duplicates and trivial risks here; keep the register sharp.

### Step 6 — Estimate residual risk after mitigation
Re-score likelihood and impact assuming the mitigation is in place. Compute residual composite. Compare to inherent composite. If residual is still above the user's risk appetite, the risk needs a stronger mitigation, an explicit acceptance decision, or escalation now.

### Step 7 — Set ownership rules and review cadence
- **Ownership rules:** how owners are assigned, what they're accountable for, what happens when an owner leaves.
- **Review cadence:** how often the register is reviewed (tie to score — e.g., high-composite risks reviewed weekly, low ones monthly/quarterly), who runs the review, and how new risks enter.

### Step 8 — Summarize the risk posture
Top risks by composite, top risks by residual composite, any risks above appetite with no adequate mitigation, and any risks lacking a real owner.

---

## False-Positive Prevention

1. **Owner-by-committee.** "The team owns it" means no one does. Force a single name per risk; an unassignable risk is a flag, not a row to fill in vaguely.
2. **Mitigation-as-restatement.** "Risk: server crashes. Mitigation: prevent crashes." A mitigation is a concrete action (redundancy, monitoring, runbook), not a wish.
3. **Residual = inherent.** Copying the inherent score into residual hides whether the mitigation does anything. If it doesn't move the score, justify the mitigation or drop it.
4. **Score inflation/deflation.** Scoring by mood instead of the anchored scales makes risks incomparable. Always anchor.
5. **Trigger vagueness.** "Escalate if it gets bad" never fires. The trigger is a threshold, date, or event observable in advance.
6. **Category smuggling.** Filing a reputational risk under "operational" because it's less alarming. Categorize by the dominant nature of the harm.
7. **Static register.** No cadence, no entry path for new risks — the register is a snapshot, not a system. The cadence section is mandatory.
8. **Comprehensiveness theater.** Forty low-impact risks bury the three that matter. Prune; surface the consequential ones.
9. **Appetite blindness.** Filling scores without comparing residual risk to the user's stated tolerance. The summary must flag anything above appetite.

---

## Output Format

```
# Risk register — [scope]

## Scope & objectives
- Scope: [what this register covers, boundaries]
- Objectives at stake: [...]
- Horizon: [window]
- Risk appetite: [tolerance / thresholds]

## Register
| ID | Risk | Category | L (1–5) | I (1–5) | Composite | Owner | Mitigation | Monitoring (observable + cadence) | Escalation trigger | Residual L | Residual I | Residual composite |
|----|------|----------|---------|---------|-----------|-------|-----------|-----------------------------------|--------------------|-----------|-----------|--------------------|
| R1 | [name] | technical | 4 | 5 | 20 | [name] | [action] | [observable, weekly] | [condition] | 2 | 4 | 8 |
| R2 | [name] | people    | 3 | 4 | 12 | [name] | [action] | [observable, monthly] | [condition] | 2 | 3 | 6 |
| …  |      |          |         |         |           |       |           |                                   |                    |           |           |                    |

## Risk posture summary
- Top risks by inherent composite: [R#, R#, R#]
- Top risks by residual composite: [R#, R#, R#]
- Above appetite after mitigation: [R# — why, and what's needed]
- Risks lacking a real owner: [R# — flag]

## Ownership rules
- Assignment: [how owners are set]
- Accountability: [what an owner is responsible for]
- Owner transition: [what happens when an owner leaves]

## Review cadence
- High-composite risks (≥ [threshold]): reviewed [cadence], run by [role]
- Medium risks: reviewed [cadence]
- Low risks: reviewed [cadence]
- New-risk intake: [how risks enter the register between reviews]
```

---

## Verification

- [ ] Every risk has exactly one of the eight categories.
- [ ] Likelihood and impact scored on the anchored 1–5 scales; composite computed.
- [ ] Every risk has exactly one named owner (or is flagged as ownerless).
- [ ] Every mitigation is a concrete action, not a restatement of the risk.
- [ ] Every risk has a monitoring observable with a cadence.
- [ ] Every risk has a specific escalation trigger (threshold / date / event).
- [ ] Residual likelihood, impact, and composite estimated; any unchanged residual is justified.
- [ ] Risks above appetite after mitigation are surfaced in the summary.
- [ ] Ownership rules and a review cadence are specified.
- [ ] No "team owns it"; no mitigation-as-restatement; no static register.
