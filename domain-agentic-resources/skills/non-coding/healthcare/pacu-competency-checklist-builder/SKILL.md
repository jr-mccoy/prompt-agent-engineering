---
name: pacu-competency-checklist-builder
description: Build a behaviorally anchored competency sign-off checklist for a PACU skill or role transition. Use when the user asks for a "competency checklist", "sign-off form", "skills validation", "orientation checkoff", or needs an observation-based evaluation document. Output separates observable behaviors from clinical knowledge, with explicit sign-off levels.
tags:
  - pacu
  - nursing-education
  - competency
  - sign-off
updated: "2026-04-14"
---

# PACU Competency Checklist Builder

## Purpose

Produce a preceptor-facing competency checklist with behavior-anchored items (what the orientee *does*, observable at the bedside), separate knowledge items (what they can *explain*), and structured sign-off levels.

## When to use

- End-of-orientation sign-off.
- Skill-specific validation (e.g., airway management, regional block assessment, PCA setup).
- Annual recredentialing or role transition (Phase 2 → Phase 1).

## When NOT to use

- Knowledge-only assessment → `pacu-quiz-generator`.
- Scenario-based demonstration → `pacu-case-scenario-writer`.

## Inputs required

1. **Competency scope** — one named skill or role.
2. **Sign-off levels** the facility uses (e.g., Independent / With Cues / With Direction / Not Yet). If unknown, offer a default 4-level scale.
3. **Required observation count** (default: 3 independent performances before sign-off).
4. **Source chapters / institutional policies** if applicable.
5. **Length target** (default: 1–2 pages).

## Workflow

1. **Confirm inputs.**
2. **Split content into three columns of focus:**
   - **Performs** — observable behaviors (verbs).
   - **Explains** — can articulate rationale (one-line "why").
   - **Escalates** — recognizes when to call for help and does so with appropriate SBAR.
3. **Write 8–15 behavior-anchored items** per skill. Each item is a single observable behavior that a preceptor can mark.
4. **Pair each item with** a minimum-observation count (how many times it must be observed).
5. **Sign-off levels** in column headings.
6. **Footer blocks:**
   - Preceptor signature + date.
   - Orientee self-assessment column.
   - Remediation plan space if any item is below threshold.
7. **Safety reminder. Self-check.**

## Output format

```markdown
# {Competency} — PACU Sign-Off Checklist

> Safety reminder: Sign-off validates demonstrated performance, not theoretical readiness — observation in actual PACU workflow is required.

## Orientee
Name: ____________    Start date: ____________    Target sign-off date: ____________

## Sign-off levels
- **I** — Independent (no cueing)
- **C** — With cues (prompts but correct action)
- **D** — With direction (preceptor walks through)
- **N** — Not yet observed / not yet met

## Required observations
Each behavior item must be observed ≥ {N, default 3} times at Independent level for final sign-off.

## Performs (observable behaviors)
| # | Behavior | Obs 1 | Obs 2 | Obs 3 | Final |
|---|---|---|---|---|---|
| 1 | ... | I / C / D / N | | | |

## Explains (rationale)
| # | Can articulate | Met? |
|---|---|---|
| 1 | Why {mechanism / threshold / intervention} | Y / N |

## Escalates (recognition + SBAR)
| # | Recognizes trigger | Initiates SBAR | Calls appropriate role |
|---|---|---|---|
| 1 | ... | | |

## Remediation plan (if any item is below threshold)
- Item(s): ...
- Plan: ...
- Reassessment date: ...

## Sign-off
Orientee: ____________    Date: ____________
Preceptor: ____________  Date: ____________
Educator: ____________   Date: ____________

## Sources / references
- ...
```

## Source-fidelity rules

- Behavior items are generic enough to apply across facilities; do not bake in specific equipment names or paging pathways (mark those as *per facility protocol* in the behavior wording).
- Knowledge items cite source chapters where the rationale lives.

## Self-check

- [ ] Performs / Explains / Escalates are separated.
- [ ] 8–15 observable behaviors; each is a single verb-anchored action.
- [ ] Sign-off levels defined at top.
- [ ] Minimum observation count stated.
- [ ] Remediation block present.
- [ ] No facility-specific specifics baked into behavior wording.
- [ ] Safety reminder at top.
