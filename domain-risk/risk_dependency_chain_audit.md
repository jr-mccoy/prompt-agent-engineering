---
title: "Dependency Chain Audit — Single Points of Failure Ranked by Blast Radius × Replacement Difficulty"
category: risk/dependencies
description: "Map dependencies across a system, project, or operation — vendors, key people, infrastructure, contracts, knowledge — trace the chains (A depends on B, B depends on C), find the single points of failure whose loss collapses a chain, assess how fast each node could be replaced, and prioritize by blast radius × replacement difficulty. The risk-prioritization companion to the structural dependency map: that one draws the wiring, this one ranks what to harden first and prescribes the resilience move for each top node."
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
  - dependencies
  - single-point-of-failure
  - blast-radius
  - resilience
updated: "2026-05-10"
reasoning:
  styles: [systems, structural, probabilistic]
  stakes: variable
  horizon: variable
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: matrix_ranked_list
  user_role: [operator, engineer, founder, executive, analyst]
  mode: [audit, diagnose, plan]
related_prompts:
  - domain-reasoning-craft/systems/systems_dependency_map.md
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_fmea_analysis.md
---

# Dependency Chain Audit

**Objective:** Find and prioritize the single points of failure in a system, project, or operation. List the dependencies (vendors, key people, infrastructure, contracts, knowledge), trace the chains in which one depends on another (A → B → C), identify the **single points of failure** — nodes whose loss collapses a chain — assess **substitutability** (how fast each node could be replaced), and prioritize by **blast radius × replacement difficulty**. For each top node, prescribe a concrete resilience move. This is the risk-prioritization companion to `systems_dependency_map.md`: that prompt draws the static wiring (topology, fan-in/out, cycles); this one asks "which of these would hurt most and take longest to replace, and what do we do about it?"

**When to use:**
- You need to know which dependency, if it vanished tomorrow, would do the most damage — and how long you'd be down.
- Concentration risk is suspected: one vendor, one engineer, one contract, or one server is quietly load-bearing.
- Before a vendor negotiation, a key-person departure, or a contract renewal, to know your real exposure.
- Building a resilience or continuity plan and needing to sequence what to harden first.

**When NOT to use:**
- You want the structural wiring diagram with cycles and fan-in/fan-out topology — use `systems_dependency_map.md`.
- You want per-step failure modes with severity/occurrence/detectability — use `risk_fmea_analysis.md`.
- You want a portfolio register of all risk types with owners — use `risk_register_builder.md`.
- There are no meaningful external/internal dependencies (a self-contained, fully-owned system).

**Audience:** Operators, engineers, founders, executives, and analysts responsible for continuity who need to know where the operation is one failure away from collapse.

---

## Inputs / Context

1. **The system, project, or operation.** What's being audited and what it must keep doing. One paragraph.
2. **Known dependencies.** Any vendors, people, infrastructure, contracts, or knowledge the user already knows the operation leans on.
3. **What "down" costs.** What happens to the operation per unit time when a dependency is lost — to anchor blast radius.
4. **Replacement context.** Any known constraints on swapping a node — contracts, lead times, specialized knowledge, switching costs.
5. **Horizon / trigger.** Whether this is a standing audit or tied to a specific upcoming event (departure, renewal, migration).

---

## Constraints

### Must
- Enumerate dependencies across **all five classes**: vendors/third parties, key people, infrastructure/systems, contracts/legal, and knowledge/expertise. Knowledge dependencies (one person who understands a thing) are the most commonly missed — push for them.
- Trace **chains**: where one dependency depends on another (A → B → C). A node deep in a chain can be a hidden SPOF.
- Identify **single points of failure**: nodes with no redundancy whose loss collapses a chain or halts the operation.
- For each SPOF, assess two dimensions:
  - **Blast radius** — how much breaks and how badly, per unit of downtime, if this node is lost.
  - **Replacement difficulty / substitutability** — how fast and how painfully it could be replaced (hours / days / weeks / months / effectively irreplaceable).
- **Prioritize by blast radius × replacement difficulty.** A high-blast, hard-to-replace node is the top hardening target.
- For each top SPOF, prescribe a concrete **resilience move**: add redundancy, cross-train, document, dual-source, negotiate fallback terms, or pre-stage a replacement.
- Distinguish **hidden** SPOFs (deep in a chain, not obvious) from **obvious** ones — hidden ones are the audit's main value.

### Must Not
- List only direct/first-tier dependencies. The dangerous SPOF is often a sub-dependency (your vendor's single supplier, your engineer's single undocumented script).
- Treat all dependencies as equal. Prioritization by blast radius × replacement difficulty is the point.
- Conflate "important" with "single point of failure." A critical node with a hot standby is not a SPOF; a trivial-seeming node with no backup might be.
- Recommend "add redundancy" generically. Match the move to the dependency class — cross-training for people, dual-sourcing for vendors, documentation for knowledge.
- Omit knowledge/expertise dependencies because they're intangible. The bus-factor-of-one engineer is frequently the worst SPOF.

---

## Instructions

### Step 1 — Frame what must keep running
State the operation's core function and what "down" costs per unit time. This anchors blast radius.

### Step 2 — Enumerate dependencies across all five classes
- **Vendors / third parties** — suppliers, SaaS, payment processors, hosts, partners.
- **Key people** — individuals whose absence stalls work.
- **Infrastructure / systems** — servers, databases, networks, physical assets.
- **Contracts / legal** — licenses, leases, agreements that permit operation.
- **Knowledge / expertise** — undocumented understanding held by one person or one place.

### Step 3 — Trace the chains
For each dependency, ask "what does *it* depend on?" Build chains (A → B → C). Flag sub-dependencies the team doesn't control or can't see (a vendor's single upstream supplier; a script only one person can run).

### Step 4 — Identify single points of failure
A node is a SPOF if its loss collapses a chain or halts the operation and there's no ready substitute. Mark each as **obvious** or **hidden** (deep in a chain, not on anyone's radar).

### Step 5 — Score blast radius
For each SPOF: how much breaks, how badly, and how fast the pain grows per unit of downtime. Scale: contained / significant / severe / total.

### Step 6 — Score replacement difficulty
For each SPOF: how fast could it be replaced or worked around? hours / days / weeks / months / effectively irreplaceable. Note the binding constraint (contract lock-in, lead time, tacit knowledge, certification).

### Step 7 — Prioritize
Rank SPOFs by **blast radius × replacement difficulty**. The top of the list: high blast, hard to replace. These get hardened first.

### Step 8 — Prescribe resilience moves
For each top SPOF, a concrete, class-matched move:
- **People:** cross-train, document, hire a second, retainer for a contractor.
- **Vendor:** dual-source, negotiate exit/fallback terms, build an abstraction layer.
- **Infrastructure:** redundancy, failover, backups with tested restore.
- **Contract:** renewal lead time, alternatives lined up, renegotiate exclusivity.
- **Knowledge:** write it down, pair someone on it, record the runbook.

State the residual exposure after the move and a rough cost/effort.

---

## False-Positive Prevention

1. **First-tier-only audit.** Stopping at direct dependencies. The expensive SPOF is usually a sub-dependency — your vendor's single supplier, your one engineer's one undocumented process. Trace the chains.
2. **Importance ≠ SPOF.** A critical node with redundancy isn't a single point of failure; a minor node with no backup is. Test for substitutability, not just importance.
3. **Knowledge blindness.** Skipping the undocumented-expert dependency because it's intangible. Bus-factor-of-one is frequently the worst SPOF. Always include knowledge dependencies.
4. **Equal-weighting.** Treating every dependency as equally worth hardening. Prioritize by blast radius × replacement difficulty.
5. **Generic redundancy.** "Add redundancy" for everything. The move must match the class — cross-training for people, dual-sourcing for vendors, documentation for knowledge.
6. **Hidden-SPOF miss.** Auditing only the obvious nodes. The audit's value is surfacing the load-bearing dependency nobody was watching. Mark hidden vs obvious.
7. **Substitutability optimism.** "We could replace that fast." Test the assumption against the real binding constraint — contract terms, lead times, tacit knowledge rarely move as fast as hoped.
8. **Static contracts as safe.** Treating a contract or license as a stable given. A non-renewing license or an exclusive supplier clause is a SPOF with a calendar trigger.

---

## Output Format

```
# Dependency chain audit — [system / operation]

## What must keep running
- Core function: [...]
- Cost of being down: [per unit time]

## Dependency inventory
| ID | Dependency | Class | Depends on (sub-dependencies) | Redundancy? |
|----|------------|-------|-------------------------------|-------------|
| D1 | [name] | vendor | [B → C] | none |
| D2 | [name] | knowledge | — | none (single person) |
| … | | | | |

## Dependency chains
- Chain 1: [A] → [B] → [C]  (SPOF: [node], hidden)
- Chain 2: [X] → [Y]  (SPOF: [node], obvious)
- …

## Single points of failure (ranked by blast radius × replacement difficulty)
| Rank | Node | Class | Hidden? | Blast radius | Replacement difficulty | Binding constraint | Priority |
|------|------|-------|---------|--------------|------------------------|--------------------|----------|
| 1 | [node] | knowledge | hidden | total | months (tacit knowledge) | only one person knows it | top |
| 2 | [node] | vendor | obvious | severe | weeks (contract lock-in) | 90-day exit clause | high |
| … | | | | | | | |

## Resilience moves
| SPOF | Move | Class-matched action | Residual exposure | Cost/effort |
|------|------|----------------------|-------------------|-------------|
| [#1] | document + cross-train | [specifics] | one backup person, still thin | moderate |
| [#2] | dual-source | [specifics] | both vendors share one upstream | high |
| … | | | | |

## Summary
- Worst SPOF (highest blast × difficulty): [node]
- Most dangerous hidden dependency: [node]
- Top-3 hardening targets this cycle: [nodes]
```

---

## Verification

- [ ] Dependencies enumerated across all five classes, including knowledge/expertise.
- [ ] Sub-dependencies traced; chains drawn (A → B → C).
- [ ] SPOFs identified and marked hidden vs obvious.
- [ ] Each SPOF scored on blast radius and replacement difficulty.
- [ ] SPOFs ranked by blast radius × replacement difficulty.
- [ ] Each top SPOF has a class-matched resilience move with residual exposure.
- [ ] Importance distinguished from single-point-of-failure (redundancy tested).
- [ ] Contract/license dependencies with calendar triggers included.
- [ ] No first-tier-only audit; no generic "add redundancy."
- [ ] Worst SPOF and most dangerous hidden dependency named.
