---
title: "Quest Structure and Branching Dialogue Design"
category: game-development/narrative
description: "Design a quest and its dialogue trees as a state machine the team can build and test: a named branching structure, state variables that are both set and read, a node map with every choice's consequence, a VO/line budget, and an audit for dead ends, soft-locks and false choices — distinct from story structure for prose and from voice-assistant dialog state design."
techniques:
  - DT-01
  - DS-01
  - OC-03
  - QA-02
difficulty: intermediate
tags:
  - narrative-design
  - quest-design
  - branching-dialogue
  - game-writing
  - interactive-narrative
  - state-variables
  - choices-dont-matter
  - player-gets-stuck
  - too-many-branches
updated: "2026-09-24"
related_prompts:
  - domain-game-development/design/design_game_design_document.md
  - domain-game-development/architecture/architecture_state_machine_design.md
  - domain-creative-writing/fiction/writing_story_structure_architect.md
---

# Quest Structure and Branching Dialogue Design

**Objective:** Turn a quest premise into a buildable narrative spec — structure,
state, dialogue nodes, line budget — and prove before anyone records VO that
every branch ends somewhere, every choice changes something, and nothing can
soft-lock the player.

**When to Use:**
- A quest or conversation is moving from pitch to scripting and needs a structure
  engineers, writers and QA can all read.
- Branching is growing and nobody can say how many lines a single playthrough sees.
- Playtesters report choices that "didn't matter" or a quest that stalled.

**When NOT to use:**
- Plot and act structure for a novel or screenplay —
  `domain-creative-writing/fiction/writing_story_structure_architect.md`. Prose has
  one reader path; this prompt exists because a game has many.
- Conversational state for a voice assistant or chatbot —
  `domain-voice-conversational-ui/dialog-architecture/dialog_architecture_state_machine_design.md`.
- The engine-side state machine that runs the quest —
  `architecture/architecture_state_machine_design.md`. This prompt produces the
  design that machine implements; it is distinct from that code-level pattern choice.

## Inputs

1. **Premise** in two sentences: who wants what, and what stands in the way.
2. **Where it sits**: main path or side content, level range, what the player
   already knows.
3. **Player agency promise**: which choices the game has told players matter.
4. **Existing world state** the quest may read (factions, companions, prior flags).
5. **Budget**: VO lines or words available, localisation languages, cinematic count.
6. **Tooling**: Ink, Yarn Spinner, articy:draft, engine-native graph, or spreadsheet.

## Method

1. **Choose the branching structure by name (DS-01).** Linear with flavour
   choices; branch-and-bottleneck; parallel paths that converge; open-state
   (quest reads world variables rather than branching). State why, in terms of
   budget: each true branch multiplies content, each bottleneck caps it.
2. **Decompose into beats (DT-01).** Hook → objective → complication → decision →
   resolution → aftermath. For each beat: the player's goal, the information they
   gain, and the exit condition.
3. **Declare state variables.** Name, type, range, where it is **set**, where it is
   **read**. A variable set but never read is a false choice; one read but never
   set is a bug waiting for QA.
4. **Map dialogue nodes (OC-03).** For each conversation: node ID, speaker, gate
   (condition to appear), player options, and each option's consequence — a
   variable write, a relationship change, or an explicit "flavour only".
5. **Budget the lines.** Lines per beat and per branch; lines seen on the
   shortest and longest playthrough. Report the ratio: content built vs content
   any one player sees.
6. **Attack the graph (QA-02).** Walk it as a hostile player: skip the quest-giver,
   kill the key NPC, sell the quest item, do beats out of order, load a save from
   before a flag existed. Record every dead end, soft-lock and orphan node.
7. **Mark the consequences the player will actually notice.** A consequence the
   player never sees reflected is, to the player, no consequence.

## Output Format

```
## Structure       — named pattern, beat list, why this pattern for this budget
## State variables — table: name | type | range | set at | read at
## Dialogue map    — per conversation: node | speaker | gate | options → consequence
## Line budget     — per beat; shortest vs longest playthrough; % of built content seen
## Graph audit     — dead ends, soft-locks, orphans, false choices, each with fix
## Confidence      — High/Medium/Low per section, with what would raise it
```

## Verification

- [ ] Every beat has an exit condition; every branch reaches a resolution.
- [ ] Every state variable appears in both "set at" and "read at".
- [ ] Every player option lists a consequence or is explicitly marked flavour.
- [ ] The line-budget totals equal the sum of their beats.
- [ ] The hostile walk covered: key NPC dead, item lost, out-of-order, old save.
- [ ] At least one consequence of each major choice is visible to the player.

## False-Positive Prevention

1. **More branches is not more agency.** Players feel agency when a choice is
   acknowledged, not when a hidden graph forks. Two reflected choices beat six
   silent ones.
2. **Flavour choices are not defects.** Tone options that change no state are a
   legitimate tool; flag them only when the game promised they matter.
3. **"Convergent" is not a failure mode by itself.** Branch-and-bottleneck is the
   standard way to ship on a budget; the defect is convergence that contradicts
   what the player chose.
4. **Do not count a soft-lock the design already prevents.** If the key NPC is
   flagged essential, "player kills NPC" is not a finding — say so and move on.
5. **Line counts are estimates until scripted.** Mark them `[estimate]` and
   re-run the budget after first draft; do not present them as locked.
6. **Do not rewrite the premise.** Review the structure you were given; propose a
   different premise only if the structure cannot meet the budget.

## Example

**Input:** Side quest "The Salt Ledger", level 12–15 RPG. The player finds a
smuggler's ledger implicating the harbourmaster. Budget: 220 VO lines, 5 languages.

```markdown
## Structure
Branch-and-bottleneck. One decision point (confrontation) with three outcomes that
converge on a shared aftermath. Chosen because 220 lines cannot fund three
independent quest halves.

Beats: B1 Hook (Mara hands over ledger) → B2 Investigation (3 optional leads,
any 2 unlock B3) → B3 Confrontation (decision) → B4 Resolution (3 variants) →
B5 Aftermath (barks + world change)

## State variables
| Name | Type | Range | Set at | Read at |
|---|---|---|---|---|
| ledger_state | enum | held / given_guard / burned | B1, B3 | B3, B4 |
| harbourmaster | enum | free / arrested / extorted | B4 | B5, dock vendor prices |
| trust_mara | int | -3..+3 | B2, B3 | B4 variant lines, companion recruit |
| leads_found | int | 0..3 | B2 | B3 gate (≥2) |

## Dialogue map — B3 Confrontation (excerpt)
| Node | Speaker | Gate | Options → consequence |
|---|---|---|---|
| C1 | Harbourmaster | leads_found ≥ 2 | "I know about the salt." → C2 |
| C2 | Harbourmaster | — | Expose → harbourmaster=arrested, trust_mara +2 |
|    |               |   | Extort → harbourmaster=extorted, trust_mara −2, +400 gold |
|    |               |   | Burn ledger → ledger_state=burned, harbourmaster=free |
| C3 | Harbourmaster | ledger_state=given_guard | "The guard already has it." → arrested (no choice) |

## Line budget
| Beat | Lines |
|---|---|
| B1 Hook | 18 |
| B2 Investigation (3 leads × 24) | 72 |
| B3 Confrontation | 46 |
| B4 Resolution (3 × 20) | 60 |
| B5 Aftermath barks | 14 |
| **Total** | **210** (10 under budget) |

Shortest playthrough: 18 + 48 (2 leads) + 30 + 20 + 6 = 122 lines (58% of built).
Longest: 18 + 72 + 46 + 20 + 14 = 170 lines (81%). 40 lines are only reachable on
a second playthrough — acceptable for side content.

## Graph audit
| # | Finding | Type | Fix |
|---|---|---|---|
| 1 | Player sells ledger to vendor before B3 → B3 gate unreachable | Soft-lock | Mark ledger as quest item (unsellable) |
| 2 | Mara killed in B2 → B4 "Expose" variant has her speak | Dead end | Add Mara-dead variant (6 lines) or make essential |
| 3 | trust_mara set in B2 but only read in B4 lines | False choice risk | Also read it in companion recruit gate (already listed — confirm with systems) |
| 4 | C3 gives no choice after player handed ledger to guard | Intended | Not a defect; acknowledge choice in C3's first line |
| 5 | "Burn ledger" leaves harbourmaster=free with no visible change | Unreflected | Dock vendor raises prices 10% (reads harbourmaster) |

## Confidence
Structure: High. Line budget: Medium — [estimate] until first draft.
Graph audit: Medium — covers the four hostile walks; old-save migration not yet
checked against the save-version table.
```

## Techniques Used

- **DT-01 (Hierarchical Task Breakdown):** quest → beats → conversations → nodes.
- **DS-01 (Framework Application):** named branching structures chosen against budget.
- **OC-03 (Markdown Table Specification):** state and node tables engineers and QA consume directly.
- **QA-02 (Adversarial Stress-Test):** the hostile-player walk that finds soft-locks.

## Related Prompts

- `domain-game-development/design/design_game_design_document.md` — where the quest sits in the game.
- `domain-game-development/architecture/architecture_state_machine_design.md` — implementing the quest state.
- `domain-creative-writing/fiction/writing_story_structure_architect.md` — linear story structure craft.
