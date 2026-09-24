---
title: "Difficulty and Combat Balancing"
category: game-development/design
description: "Balance combat and difficulty with explicit maths: DPS and effective-HP models, time-to-kill and time-to-death tables per enemy and difficulty mode, a difficulty curve across the game, and an ethics check for dynamic difficulty adjustment (disclosure, opt-out, never tied to spend) — distinct from XP/progression curves and from economy balancing."
techniques:
  - NE-11
  - RT-06
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - game-design
  - balancing
  - combat
  - difficulty
  - dynamic-difficulty
  - time-to-kill
  - game-too-hard
  - fights-drag-on
  - easy-mode
updated: "2026-09-24"
related_prompts:
  - domain-game-development/design/design_player_progression.md
  - domain-game-development/design/design_mechanics_design.md
  - domain-game-development/testing/testing_playtest_protocol_synthesis.md
---

# Difficulty and Combat Balancing

**Objective:** Make combat difficulty a table the team can argue about instead of
a feeling: compute time-to-kill and time-to-death for every enemy at every mode,
compare them to design targets, and decide whether and how the game adapts
difficulty without deceiving or exploiting the player.

**When to Use:**
- An enemy roster exists and fights feel too long, too short, or inconsistent.
- Difficulty modes are being defined and nobody has written what each changes.
- The team is considering dynamic difficulty adjustment (DDA) or rubber-banding.

**When NOT to use:**
- XP curves, unlock pacing, skill trees — `design_player_progression.md`. This
  prompt is distinct because it balances moment-to-moment combat maths, not
  long-run progression.
- Currency, drop rates, monetization — `economy/economy_system_design.md`.
- Designing the mechanic itself — `design_mechanics_design.md`.

## Inputs

1. **Player offence**: weapons/abilities with damage, rate, and an accuracy or
   uptime assumption.
2. **Enemy roster**: HP, mitigation, damage, attack rate, hit chance, role.
3. **Player defence**: HP, mitigation, healing, invulnerability windows.
4. **Design targets**: intended TTK per enemy role, intended time-to-death in a
   standard encounter, per mode.
5. **Modes and audience**: difficulty options, accessibility options, competitive
   or not, monetization model.
6. **Playtest or telemetry**, if any: deaths per encounter, completion rates.

## Method

1. **Model offence (NE-11).** `effective DPS = damage × rate × accuracy`.
   State the accuracy assumption; it dominates everything.
2. **Model defence (NE-11).** `EHP = HP ÷ (1 − mitigation)`; `TTK = EHP ÷ effective DPS`.
   Do the same in reverse for time-to-death (TTD) against a standard encounter.
3. **Build the TTK/TTD table** per enemy × mode and mark each cell against its
   target band. Out-of-band cells are the findings.
4. **Change the fewest variables.** Prefer one lever per finding (enemy HP, or
   damage, or rate) and show the recomputed cell.
5. **Chart the curve across the game (RT-06).** Standard-encounter TTD by level or
   chapter; cross-check against deaths per encounter from telemetry or playtest.
   Spikes that match death spikes are real; spikes the data does not show may be
   offset by player skill growth.
6. **Define modes by what they change.** Incoming damage, enemy aggression,
   checkpoint density, assist options — each a named multiplier or switch.
7. **Apply the DDA constraints (CM-02).** If the game adapts difficulty:
   - Disclose it in settings or the manual; offer an off switch.
   - Never in ranked or competitive play; never adjust one side of PvP.
   - Never correlated with spend: no harder fights that sell boosts, no easier
     fights after a purchase.
   - Bound it: a stated maximum adjustment, and it must not silently undo a mode
     the player chose.
8. **Verify (QA-01).** Recompute every changed cell from the formula.

## Output Format

```
## Assumptions — accuracy, uptime, standard encounter definition
## TTK table   — enemy × mode: EHP, eff. DPS, TTK, target band, verdict
## TTD table   — encounter × mode: incoming DPS, player EHP, TTD, target, verdict
## Changes     — one lever per finding, before → after
## Curve       — TTD by chapter vs deaths per encounter
## Modes       — multipliers and switches per mode
## DDA         — design, bounds, disclosure, and the constraint checklist
## Confidence  — per section
```

## Verification

- [ ] Every TTK and TTD cell is reproducible from the stated formula and inputs.
- [ ] Accuracy/uptime assumptions are stated and used consistently.
- [ ] Each change moves exactly one lever and shows the recomputed value.
- [ ] Every DDA constraint in step 7 is answered yes/no, not skipped.
- [ ] Curve spikes are cross-checked against observed deaths where data exists.

## False-Positive Prevention

1. **Long TTK is not automatically wrong.** Bosses and tanks are meant to be
   long; judge against the role's target band.
2. **Spreadsheet balance is not felt balance.** A correct TTK with an unreadable
   tell still feels unfair; flag such cells for playtest, do not re-tune numbers.
3. **Hard is not a defect in a game promising hard.** Compare to the game's
   stated difficulty identity, not a genre average.
4. **Do not tune off one player's deaths.** Use counts across players.
5. **Assist options are not a lesser mode.** Do not label them "easy" or gate
   achievements behind them without a design reason.
6. **DDA is not inherently unethical.** Disclosed, bounded, spend-independent
   adaptation in single-player is a legitimate accessibility tool.

## Example

**Input:** Third-person shooter. Pistol 25 dmg × 4/s; accuracy assumption 60%.
Player 100 HP, no mitigation. Targets: Grunt TTK 2–3 s; Brute 8–10 s;
TTD vs 3 Grunts on Normal 6–8 s.

```markdown
## Assumptions
Effective player DPS = 25 × 4 × 0.60 = 60. Standard encounter = 3 Grunts.
Grunt: 10 dmg/hit, 1 attack/s, 50% hit chance → 5 incoming DPS each.

## TTK table (Normal)
| Enemy | HP | Mitig. | EHP | Eff. DPS | TTK | Target | Verdict |
|---|---|---|---|---|---|---|---|
| Grunt | 150 | 0% | 150 | 60 | 2.5 s | 2–3 s | OK |
| Brute | 600 | 25% | 800 | 60 | 13.3 s | 8–10 s | Too long |

## TTD table (3 Grunts = 15 incoming DPS at ×1.0)
| Mode | Incoming × | Incoming DPS | Player EHP | TTD | Target | Verdict |
|---|---|---|---|---|---|---|
| Story | 0.5 | 7.5 | 100 | 13.3 s | ≥ 12 s | OK |
| Normal | 1.0 | 15 | 100 | 6.7 s | 6–8 s | OK |
| Hard | 1.5 | 22.5 | 100 | 4.4 s | 4–5 s | OK |

## Changes
Brute HP 600 → 450: EHP = 450 ÷ 0.75 = 600; TTK = 600 ÷ 60 = 10.0 s (in band).
Mitigation unchanged, so armour-piercing weapons keep their niche.

## Curve (Normal, standard-encounter TTD by chapter)
Ch1 8.0 s · Ch2 7.1 s · Ch3 6.7 s · Ch4 4.9 s · Ch5 4.6 s
Playtest deaths per encounter: Ch3 0.8 · Ch4 2.6 · Ch5 1.4. Ch3→Ch4 drop (−27%)
matches a death spike → real. Ch5 is similar TTD with fewer deaths → skill growth.
Fix: introduce Ch4's sniper enemy in Ch3 at half density.

## Modes
| Mode | Incoming dmg | Enemy aggression | Checkpoints | Aim assist |
|---|---|---|---|---|
| Story | ×0.5 | low | every room | strong |
| Normal | ×1.0 | medium | every encounter | medium |
| Hard | ×1.5 | high | every 2 encounters | off by default |

## DDA
Single-player only. After 3 deaths in one encounter, offer (not apply) "reduce
incoming damage ×0.8 for this fight". Bound: never below Story values.
| Constraint | Met? |
|---|---|
| Disclosed and switchable | Yes — Settings › Assist |
| Absent from competitive | Yes — no PvP mode |
| Independent of spend | Yes — no purchasable combat items |
| Bounded, respects chosen mode | Yes — offer only, floor = Story |

## Confidence
TTK/TTD maths: High (reproducible). Accuracy 60%: Medium — [measure] from
telemetry. Curve reading: Medium, N = 12 playtest.
```

## Techniques Used

- **NE-11 (Embedded Calculation Formulas):** DPS, EHP, TTK and TTD formulas applied cell by cell.
- **RT-06 (Correlation and Cross-Analysis):** TTD curve cross-checked against observed deaths.
- **CM-02 (Constraint Specification):** hard constraints on dynamic difficulty.
- **QA-01 (Self-Verification):** every changed cell recomputed.

## Related Prompts

- `domain-game-development/design/design_player_progression.md` — how power grows between fights.
- `domain-game-development/design/design_mechanics_design.md` — the combat mechanics being balanced.
- `domain-game-development/testing/testing_playtest_protocol_synthesis.md` — gathering the death data.
