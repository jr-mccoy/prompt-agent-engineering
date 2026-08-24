---
title: "Dependency Map — Topology, Chokepoints, and Single Points of Failure"
category: reasoning-craft/systems
description: "Map the structural (topological) dependencies of a system as nodes and directed edges, then surface single points of failure, fan-in/fan-out concentration, and cycles. Distinct from a causal loop diagram, which is dynamic and behavioral; this is the static wiring diagram. Counters the failure mode of discovering a critical dependency only when it breaks, and of treating a hairball of components as if every node mattered equally."
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
  - systems-thinking
  - dependency-mapping
  - topology
  - single-point-of-failure
  - chokepoints
updated: "2026-05-21"
reasoning:
  styles: [systems, structural, topological]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: node_edge_map_plus_chokepoint_ranking
  user_role: [engineer, operator, analyst, founder, executive]
  mode: [audit, diagnose, synthesize]
related_prompts:
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
  - domain-risk/risk_dependency_chain_audit.md
  - domain-reasoning-craft/systems/systems_intervention_pre_mortem.md
---

# Dependency Map

**Objective:** Build the structural dependency map of a system: nodes (components, teams, vendors, services, processes, knowledge holders), directed edges (A depends on B), and the topological features that determine fragility — single points of failure, fan-in (one node many depend on), fan-out (one node depending on many), and cycles (circular dependencies). Output a node-edge text representation plus a chokepoints list ranked by blast radius. This is the static wiring diagram, not the dynamic behavior model.

**When to use:**
- You need to know what breaks if a given node fails, before it fails.
- Onboarding to an unfamiliar system and mapping how the pieces depend on each other.
- Planning a migration, deprecation, or vendor change and tracing what's downstream.
- A single team, person, or service seems to be involved in everything and you want to confirm and quantify the concentration.

**When NOT to use:**
- The question is *behavioral* — feedback, delays, why the system oscillates — use `systems_causal_loop_diagram.md`. Dependency maps are static; they don't capture feedback dynamics.
- You want risk *prioritization with mitigation and ownership* rather than the structural map — use `risk_dependency_chain_audit.md` (the risk-management companion to this systems-mapping prompt).
- The system is trivially small and the dependencies are already obvious to everyone.

**Audience:** Engineers, operators, founders, and analysts who need to see a system's wiring and find where it's brittle.

---

## Inputs / Context

1. **The system boundary.** What's in scope (a service, a product, an org, a supply chain, a process) and what's treated as external.
2. **The node list.** The components/teams/vendors/processes/knowledge involved — or a description the model can extract them from.
3. **Known dependencies.** Any "A needs B to function" relationships you already know.
4. **Failure question.** What you're trying to protect against (an outage, a key-person loss, a vendor exit) — this focuses the chokepoint ranking.
5. **Substitutability notes (optional).** How replaceable each node is, if known.

---

## Constraints

### Must
- Represent the system as **nodes** (noun-phrase components) and **directed edges** "A → B" meaning *A depends on B* (B's failure affects A). Fix the edge direction convention up front and apply it consistently.
- Distinguish **hard dependencies** (A cannot function without B) from **soft dependencies** (A degrades but survives without B).
- Identify **single points of failure**: nodes whose loss disconnects or disables a meaningful part of the system.
- Quantify **fan-in** (how many nodes depend on each node) and **fan-out** (how many nodes each node depends on); high fan-in nodes are chokepoints.
- Detect **cycles** (A → B → C → A): circular dependencies that prevent clean startup, recovery, or replacement.
- Rank chokepoints by **blast radius** (how much fails if this node fails), incorporating substitutability where known.

### Must Not
- Mix directions. Pick "depends on" as the edge meaning and never silently flip to "feeds into." Inconsistent direction makes the whole map wrong.
- Confuse dynamic feedback with structural dependency. A dependency map has no R/B loops; cycles here are circular *dependencies*, not feedback loops.
- Treat all nodes as equal. The point is to find the few that carry disproportionate blast radius.
- Omit knowledge and people as nodes. The most common hidden single point of failure is "only one person understands X."
- Rank chokepoints by fan-in alone. A high-fan-in node with an instant substitute is less critical than a low-fan-in node that's irreplaceable.

---

## Instructions

### Step 1 — Set boundary and edge convention
State what's in scope and define the edge: "A → B means A depends on B (if B fails, A is affected)." Lock it.

### Step 2 — Enumerate nodes
List every component, service, vendor, team, process, and critical knowledge holder in scope. Tag node type. Don't forget people and tacit knowledge.

### Step 3 — Draw edges
For each node, list what it depends on. Mark each edge **hard** or **soft**. Note any edges you're inferring vs confirming.

### Step 4 — Compute fan-in and fan-out
For each node: fan-in = number of nodes depending on it; fan-out = number it depends on. High fan-in = a chokepoint (many things break if it dies). High fan-out = a fragile node (many things can break it).

### Step 5 — Find single points of failure
A SPOF is a node whose removal disconnects or disables a meaningful subgraph, with no parallel path. List them. Check hard edges specifically.

### Step 6 — Detect cycles
Trace for circular dependency chains. Flag them: cycles break clean startup ordering, complicate recovery, and can deadlock.

### Step 7 — Assess substitutability
For each high-fan-in node and each SPOF, rate how fast and cheaply it could be replaced (instant / days / months / effectively irreplaceable).

### Step 8 — Rank chokepoints by blast radius
Blast radius ≈ (downstream nodes affected by hard edges) weighted by (replacement difficulty). Produce the ranked list. The top entries are where structural resilience work pays off. For mitigation/ownership planning, hand off to `risk_dependency_chain_audit.md`.

---

## False-Positive Prevention

1. **Direction drift.** Silently flipping the meaning of edges mid-map. Lock "depends on" and audit a sample of edges against it.
2. **Feedback/dependency confusion.** Importing R/B loop thinking into a static map. Cycles here are circular dependencies, not feedback loops; keep the two models separate.
3. **Egalitarian map.** Treating every node as equally important. Without fan-in/blast-radius ranking, the map is a hairball, not a diagnosis.
4. **Fan-in-only ranking.** A node depended on by many but trivially replaceable is not your top risk. Always fold in substitutability.
5. **Missing people/knowledge nodes.** Diagrams of "systems" often omit the human single points of failure, which are frequently the worst ones. Include them explicitly.
6. **Soft-as-hard inflation.** Marking degraded-but-survivable dependencies as hard inflates the SPOF count and dilutes attention. Distinguish them.
7. **Inferred-as-confirmed.** Presenting guessed dependencies as known. Flag inferred edges so they can be verified.
8. **Static map mistaken for dynamic model.** This shows what breaks, not how the system behaves over time. Don't read timing or feedback into it.

---

## Output Format

```
# Dependency map — [system]

## Boundary and convention
- In scope: [list]
- External: [list]
- Edge meaning: A → B = A depends on B (B's failure affects A)

## Nodes
| # | Node            | Type (service/team/vendor/person/knowledge) |
|---|-----------------|---------------------------------------------|
| 1 | [noun phrase]   |                                             |
| … |                 |                                             |

## Edges
| From → To | Hard/Soft | Confirmed/Inferred | Note |
|-----------|-----------|--------------------|------|
| A → B     | hard      | confirmed          |      |
| …         |           |                    |      |

## Fan-in / fan-out
| Node | Fan-in | Fan-out | Substitutability      |
|------|--------|---------|-----------------------|
| [B]  | 6      | 1       | months / irreplaceable|
| …    |        |         |                       |

## Single points of failure
| SPOF node | What it disables | Parallel path? | Substitutability |
|-----------|------------------|----------------|------------------|
| [node]    | [subgraph]       | none           | irreplaceable    |

## Cycles
| Cycle           | Consequence                     |
|-----------------|---------------------------------|
| A → B → C → A   | blocks clean startup / recovery |

## Text map
```
[A] --> [B] <-- [C]   (B = fan-in hub: 3 hard dependents)
          ^
          |
        [D]
```

## Chokepoints ranked by blast radius
| Rank | Node | Downstream affected | Replacement difficulty | Why it ranks here |
|------|------|---------------------|------------------------|-------------------|
| 1    | [B]  | [count / list]      | irreplaceable          | [one line]        |
| …    |      |                     |                        |                   |
```

---

## Verification

- [ ] Edge direction convention stated and applied consistently.
- [ ] Hard vs soft dependencies distinguished.
- [ ] Fan-in and fan-out computed per node.
- [ ] Single points of failure identified with parallel-path check.
- [ ] Cycles detected and their consequence noted.
- [ ] Substitutability folded into the chokepoint ranking (not fan-in alone).
- [ ] People and tacit knowledge included as nodes.
- [ ] Inferred edges flagged separately from confirmed ones.
- [ ] No feedback-loop semantics imported into the static map.
