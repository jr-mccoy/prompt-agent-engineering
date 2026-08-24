---
name: pacu-algorithm-flowchart-designer
description: Design a clinical decision algorithm for a PACU scenario — output both Mermaid flowchart source and a plain-text branching version. Use when the user asks for an "algorithm", "decision tree", "flowchart", or "protocol logic" for a PACU complication, phase transition, or assessment pathway. The plain-text output pairs cleanly with `image-meta-prompts/pacu_algorithm_flowchart_meta.md` for print-ready visuals.
tags:
  - pacu
  - nursing-education
  - algorithm
  - decision-tree
updated: "2026-04-14"
---

# PACU Algorithm / Flowchart Designer

## Purpose

Turn a clinical reasoning pathway into a formally structured algorithm suitable for bedside use and for pairing with an image generator. Output is always in two forms: Mermaid (copy-pasteable into docs that render it) and labeled plain-text branches (copy-pasteable into the image meta-prompt).

## When to use

- User asks for "algorithm", "decision tree", "flowchart", "protocol", "pathway logic".
- User wants visual pairing (e.g., the algorithm becomes a badge or infographic).

## When NOT to use

- User wants prose explanation → `pacu-in-depth-explainer`.
- User wants a complication reference card without branching → `prompts/pacu_red_flag_card.md`.

## Inputs required

1. **Trigger / entry point** — what clinical observation opens the algorithm. (e.g., "SpO2 < 92% in PACU".)
2. **Scope** — how far to go (stop at escalation call? include interventions? include reassessment loop?).
3. **Terminal nodes** — what outcomes end a branch (escalate, resolve, transfer, continue monitoring).
4. **Source chapters / protocols**.

## Workflow

1. **Confirm inputs.**
2. **Design tree:** each decision node is one clinical question with Yes/No or tiered answers. Keep to a max depth of 4 for bedside usability.
3. **Each action node** states: *what to do* + *time interval to reassess* + *reassessment criterion*.
4. **Each escalation node** names the *role* (not a person) and the *trigger*.
5. **Label every arrow** with the branching condition.
6. **Write two outputs:** Mermaid `flowchart TD` and a plain-text numbered branch list formatted for the image meta-prompt.
7. **Include a reassessment loop** by default — bedside algorithms should always return to reassessment.
8. **Safety reminder. Self-check.**

## Output format

```markdown
# {Scenario} — PACU Algorithm

> Safety reminder: Decision support only — clinical judgment and facility protocols override this algorithm.

## Entry point
[one-sentence trigger]

## Mermaid

```mermaid
flowchart TD
  A[Entry: {trigger}] --> B{Decision 1?}
  B -- Yes --> C[Action + reassess in X min]
  B -- No --> D{Decision 2?}
  C --> E{Reassessment: resolved?}
  E -- Yes --> F[Continue monitoring]
  E -- No --> G[Escalate: {role}]
  D -- ... --> ...
```

## Plain-text branches (for pairing with image meta-prompt)
1. **Entry:** {trigger}.
2. **Decision 1:** {question}.
   - If yes → **Action A** ({what} + reassess in {interval}).
     - Reassess: resolved? → continue monitoring.
     - Reassess: not resolved? → escalate ({role}, because {trigger}).
   - If no → Decision 2.
3. **Decision 2:** ...

## Escalation triggers (summary)
| Trigger | Call | Why |
|---|---|---|
| ... | ... | ... |

## Sources
- ...
```

## Source-fidelity rules

- Thresholds (BP, SpO2, pain score) must be sourced or marked *per facility protocol*.
- Medication nodes: name class or specific agent per source; dose is *per order* unless source gives a range.
- Time intervals should cite a source or default to "per facility reassessment standard".

## Self-check

- [ ] Max tree depth ≤ 4.
- [ ] Every action node has a time to reassess + reassess criterion.
- [ ] Every escalation names a role + trigger.
- [ ] Both Mermaid and plain-text output present.
- [ ] Reassessment loop exists (algorithm doesn't dead-end silently).
- [ ] Thresholds are sourced or marked per protocol.
- [ ] Safety reminder at top.
