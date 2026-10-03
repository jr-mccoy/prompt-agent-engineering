---
title: "Campaign-Wide Branching Narrative and State Management — Flag Registry, Combinatorial Scope, Convergence, and Payoff Ledger"
category: game-development/narrative
description: "Govern the narrative state of a whole game rather than one quest: inventory every flag in a registry with owner, scope, set and read sites, compute how many variants each scene's reads multiply into, collapse that with derived tiers, additive inserts and convergence, keep a ledger of every choice's acknowledgement and payoff, plan pairwise test coverage, and keep old saves valid when flags are added."
techniques:
  - DS-01
  - NE-11
  - OC-03
  - QA-10
difficulty: advanced
tags:
  - narrative-design
  - branching-narrative
  - narrative-state
  - flag-registry
  - storylets
  - save-compatibility
  - choices-forgotten-later
  - too-many-endings
  - story-bugs-after-patch
updated: "2026-10-03"
related_prompts:
  - domain-game-development/narrative/narrative_quest_and_dialogue_design.md
  - domain-game-development/architecture/architecture_save_system.md
  - domain-game-development/testing/testing_automated_game_testing.md
---

# Campaign-Wide Branching Narrative and State Management

**Objective:** Keep a branching game's story shippable as it grows: one registry of
narrative state, a computed variant count for every scene that reads it, a plan
that holds that count inside the content budget, a ledger proving each promised
choice pays off, and a test and save plan that stops state bugs reaching players.

**When to Use:**
- The game has dozens of quests setting flags and no one owns the whole set.
- A late-game scene reads many earlier choices and the writing team cannot see how
  many versions it needs.
- Players report choices "forgotten" later, or patches broke story state in old saves.
- **Not this prompt if** you are designing one quest's beats, variables and
  dialogue nodes — use `domain-game-development/narrative/narrative_quest_and_dialogue_design.md`;
  this prompt governs state *across* quests. For the serialisation format and
  versioning mechanics of saves, use
  `domain-game-development/architecture/architecture_save_system.md`. For linear
  plot structure, use `domain-creative-writing/fiction/writing_story_structure_architect.md`.

## Inputs / Context

1. **Flag list or export** from the narrative tool or spreadsheet: names, types,
   defaults, where set, where read.
2. **Choice promises**: which choices the marketing, tutorial or UI tells players matter.
3. **Scenes that read many flags**: finales, companion reunions, epilogues, hub
   reactivity.
4. **Content budget**: lines, cinematics, localisation languages.
5. **Tooling**: Ink, Yarn Spinner, articy:draft, engine-native graph or custom —
   what derived variables and queries it supports `[verify against current docs]`.
6. **Save history**: shipped versions and flags added since.

## Method

1. **Build the flag registry (OC-03).** One row per flag: name, type and range,
   scope (global / region / quest), owner, default, set sites, read sites, version
   introduced. Flag defects: set-never-read (payoff debt), read-never-set (bug),
   duplicates with different names, booleans that should be one enum.
2. **Name the campaign structure (DS-01).** Branch-and-bottleneck (foldback),
   parallel paths, open hubs, storylet/quality-based selection (content chosen by
   conditions on state), salience-based selection (most specific matching line
   wins). Each controls combinatorics differently; state which the game uses where.
3. **Compute each heavy scene's variant count (NE-11).**
   `branching variants = Π (values of each flag the scene branches on)`. Additive
   reads (a line inserted, not a scene forked) add rather than multiply.
4. **Collapse to budget.** In order of preference: derive a tier from several flags
   (standing = f(faction, betrayal)); demote a flag from *branching* to an *additive
   insert*; acknowledge early and converge; drop the read. Recompute after each step.
5. **Keep a payoff ledger.** Every promised choice: immediate acknowledgement,
   short-term reflection, long-term payoff, each with location. Choices with no
   later read are listed as debt with a decision: add a payoff or stop promising.
6. **Plan test coverage (QA-10).** Exhaustive combinations of a heavy scene's flags
   are rarely testable; use pairwise (every pair of values appears in some test
   case) for branching flags, plus named critical paths. Minimum pairwise cases ≥
   product of the two largest domains. Add automated state assertions where tooling allows.
7. **Protect saves.** Every new flag has a default for old saves, derived from
   existing state where possible; renamed flags keep an alias; removed flags are
   tombstoned, not reused.
8. **Assign ownership and naming rules.** Prefix by scope, one owner per flag,
   review required to add a global flag.

## Output Format

```
# Narrative state plan — [game]   Flags: [n]   Shipped versions: [..]

## Structure        — pattern per act/region and why
## Flag registry    — name | type/range | scope | owner | default | set at | read at | since
## Registry defects — flag | defect | fix
## Heavy scenes     — scene | flags read (values) | branching vs additive | variants before → after
## Payoff ledger    — choice | acknowledgement | short-term | long-term | status
## Test plan        — scene | pairwise cases | critical paths | automated assertions
## Save migration   — flag | added in | default for old saves | derivation
## Ownership rules
```

## Verification

- [ ] Every registry row has both set and read sites, or is listed as a defect.
- [ ] Variant counts are reproducible from the listed flag domains.
- [ ] Every collapse step shows the recomputed count.
- [ ] Every promised choice appears in the payoff ledger with a status.
- [ ] Pairwise case counts meet the lower bound for each heavy scene.
- [ ] Every flag added after first ship has an old-save default.

## False-Positive Prevention

1. **Convergence is not betrayal.** Branches meeting again is how branching games
   ship; the defect is convergence that contradicts or ignores what the player did.
2. **Flavour flags are not debt.** A flag driving only a bark is legitimate if no one
   promised it matters.
3. **A big state space is not a big content bill.** Storylet and salience systems
   read many flags without forking scenes; count branching reads, not all reads.
4. **Pairwise is not proof.** It catches most interaction bugs, not all; keep named
   critical paths for the combinations the story depends on.
5. **Do not rename flags in shipped saves casually.** An alias costs nothing; a
   rename without one breaks old saves.
6. **Tool capabilities vary.** Do not assume derived variables or queries exist;
   check the tool's current documentation.

## Example Output

**Input:** Three-act RPG, 41 narrative flags in a spreadsheet, one patch shipped.
The Act 3 council scene reads six flags. Budget for that scene: 15 variants.

```
# Narrative state plan — three-act RPG   Flags: 41   Shipped: 1.0, 1.1

## Structure
Acts 1–2: branch-and-bottleneck per region. Hub reactivity: salience-based barks.
Act 3 council: branching scene + additive inserts.

## Registry defects
| 7 flags | set, never read (e.g. helped_smith) | 3 get payoffs; 4 demoted to bark-only |
| 2 flags | read, never set (relic_cleansed) | bug — set in Act 2 shrine |
| helped_smith / smith_saved | duplicate | merge; alias old name |

## Heavy scenes — Act 3 council
| Flag | Values | Read as |
| faction_ally | 3 | branching |
| betrayed_council | 2 | branching |
| mara_alive | 2 | branching |
| city_burned | 2 | branching |
| relic_state | 3 | branching |
| romance | 4 | branching |
Before: 3 × 2 × 2 × 2 × 3 × 4 = 288 variants (budget 15).
Step 1: standing = f(faction_ally, betrayed_council) → 3 tiers: 6 → 3 → 144.
Step 2: relic_state → additive line (3 inserts): 144 → 48.
Step 3: romance → additive epilogue insert (4 inserts): 48 → 12.
After: standing 3 × mara 2 × city 2 = 12 branching variants + 7 inserts. Within budget.

## Payoff ledger (excerpt)
| Spare the deserter | bark at camp | appears at Act 2 siege | testifies at council | OK |
| Burn the granary | city reacts | prices +20% | — | DEBT → council line (additive) |

## Test plan — council
Branching domains 3, 2, 2 → pairwise lower bound 3 × 2 = 6; generated set 6 cases
(vs 12 exhaustive — run all 12, it is affordable). Inserts: 7 single-flag checks.
Critical paths: mara dead + city burned + hostile standing (darkest path).
Assertion: council scene never plays with standing unset.

## Save migration
| standing | 1.1 | derived from faction_ally + betrayed_council on load |
| relic_cleansed | 1.1 | true if shrine quest complete, else false |

## Ownership rules
Prefixes g_/act2_/q_; one owner per flag; global flags reviewed by narrative lead.
```

## Techniques Used

- **DS-01 Framework Application** — branch-and-bottleneck, storylet and salience-based selection as named structures.
- **NE-11 Embedded Calculation Formulas** — variant products and pairwise lower bounds.
- **OC-03 Markdown Table Specification** — the registry and ledger tables writers, engineers and QA share.
- **QA-10 Test Battery Protocol** — pairwise cases, critical paths and state assertions before ship.

## Related Prompts

- `domain-game-development/narrative/narrative_quest_and_dialogue_design.md` — one quest's beats, variables and dialogue map.
- `domain-game-development/architecture/architecture_save_system.md` — save versioning that carries narrative state.
- `domain-game-development/testing/testing_automated_game_testing.md` — automating the state assertions.
