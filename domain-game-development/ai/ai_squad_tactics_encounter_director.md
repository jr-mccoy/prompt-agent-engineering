---
title: "Squad Tactics and Encounter Director — Attack Tokens, Role and Position Claims, and Intensity-Driven Pacing"
category: game-development/ai
description: "Design the layer above individual enemies: how a group shares out attacks, roles and positions so it pressures without piling on, and how a director reads player intensity to cycle build-up, peak, fade and relax with spawn rules the player never sees break — with the token maths tied to time-to-death and the adaptive parts held to disclosure and competitive-play limits."
techniques:
  - DS-01
  - NE-11
  - DP-07
  - CM-11
difficulty: advanced
tags:
  - game-ai
  - squad-ai
  - ai-director
  - encounter-design
  - spawn-system
  - pacing
  - enemies-gang-up
  - no-time-to-breathe
  - enemies-spawn-behind-me
updated: "2026-10-03"
related_prompts:
  - domain-game-development/ai/ai_npc_decision_architecture.md
  - domain-game-development/level-design/level_blockout_and_pacing.md
  - domain-game-development/design/design_difficulty_combat_balancing.md
---

# Squad Tactics and Encounter Director

**Objective:** Specify how enemies coordinate as a group and how a director paces
encounters over a session, so fights pressure the player in readable ways, rest
arrives when it should, and nothing appears where the player was just looking.

**When to Use:**
- Groups of enemies either queue politely one at a time or all attack at once.
- A horde, co-op or replayable level needs encounters assembled at runtime rather
  than all placed by hand.
- Players report "no time to breathe" or "they spawned right behind me".
- **Not this prompt if** you are choosing a single agent's decision architecture or
  its per-frame budget — use `domain-game-development/ai/ai_npc_decision_architecture.md`;
  this prompt sits one layer above it. If every encounter is placed by hand and paced
  by a beat chart, use `domain-game-development/level-design/level_blockout_and_pacing.md`.
  For TTK/TTD tables and the full dynamic-difficulty ethics checklist, use
  `domain-game-development/design/design_difficulty_combat_balancing.md`.

## Inputs / Context

1. **Enemy roster** with roles (melee, ranged, flanker, heavy, special) and per-enemy
   incoming DPS after hit chance.
2. **Player defence** (HP, mitigation, healing) and the time-to-death target for a
   "surrounded" moment and for a standard encounter.
3. **Mode**: single-player, co-op (how many players), or competitive.
4. **Level structure**: handcrafted beats that must stay fixed, spawn volumes, the
   flow direction (where "ahead" is), navmesh limits.
5. **Session target**: length, desired number of peaks and rests.
6. **Telemetry or playtest data**: damage taken over time, downs, spawn positions
   relative to player view.

## Method

1. **Choose the coordination mechanisms by name (DS-01).**
   - *Attack tokens*: a fixed number of enemies may attack a given player at once;
     others reposition, threaten or taunt.
   - *Role assignment*: the group fills roles (pin, flank, suppress) from whoever is
     best placed, not by enemy type alone.
   - *Position claims*: tactical points (cover, flank arcs) are claimed on a shared
     blackboard so two agents do not take the same one.
   - *Group morale*: casualties or a leader's death change the group's posture.
2. **Tie tokens to time-to-death (NE-11).**
   `TTD surrounded = player EHP ÷ Σ (tokens per role × per-enemy DPS)`.
   Set token counts so this meets the target, then show the arithmetic.
3. **Write the director's intensity model (NE-11).** Per player:
   `intensity += damage taken × a + nearby kills × b + downed × c`, decaying at a
   stated rate after a quiet period. Decide whether peaks trigger on the most
   stressed player or the team average, and say why.
4. **Define the cycle and its thresholds.** Build-up (spawn budget per second),
   peak (trigger value, sustain seconds), fade (no new spawns), relax (minimum
   seconds, or until intensity falls below a floor). Compute the expected cycle
   length and peaks per session.
5. **Write the spawn rules as reasoned constraints (CM-11).** Each rule with its
   reason, so edge cases can be judged: never in any player's view (it breaks the
   world's credibility); minimum path distance (the player needs time to read the
   threat); ahead on the flow, not behind (behind reads as punishment);
   handcrafted beats override the director (the designer's set pieces stay intact).
6. **Make coordination readable.** Each group action gets a tell: a flank call, a
   suppressing bark, a leader's gesture. Coordination the player cannot perceive
   reads as luck or cheating.
7. **Predict failure modes (DP-07).** Pile-on, token hoarding by out-of-sight
   agents, all flankers on one route, spawn-in-view, endless peak, director fighting
   a handcrafted beat. For each: symptom, cause, guard, and the telemetry that
   detects it.
8. **Bound the adaptation.** A director that reads player performance is adaptive
   difficulty: disclose it, keep it out of competitive modes, bound how far it can
   push either way, and never tie it to spending.

## Output Format

```
# Squad and director spec — [game / mode]

## Coordination mechanisms   — chosen, rejected, why
## Tokens and TTD            — role | tokens per player | DPS each | sum | TTD vs target
## Roles and claims          — role | selection rule | claim | release rule | tell
## Intensity model           — formula, weights, decay, peak trigger (max or mean) and why
## Director cycle            — phase | entry condition | spawn budget | duration
## Spawn rules               — rule | reason | how verified
## Failure modes             — symptom | cause | guard | telemetry
## Adaptation bounds         — disclosure, competitive exclusion, limits
## Confidence
```

## Verification

- [ ] TTD with full tokens is computed from stated DPS and meets the target.
- [ ] Every token, role and claim has a release rule.
- [ ] Peak trigger states max vs mean and the reason.
- [ ] Cycle phases sum to a stated cycle length; peaks per session follow from it.
- [ ] Every spawn rule carries its reason and a way to verify it in telemetry.
- [ ] Each group action has a player-perceivable tell.
- [ ] Adaptation is excluded from competitive play and is disclosed.

## False-Positive Prevention

1. **Being surrounded is not a bug.** Horde games promise it; the defect is a TTD
   below target or attackers the player cannot see.
2. **Not every game needs a director.** A linear handcrafted campaign is often better
   served by a beat chart; recommend a director only where encounters vary.
3. **Long peaks can be the set piece.** A finale may hold intensity deliberately —
   check the level brief before calling it an endless peak.
4. **Spawn "behind" may be a flow error, not a rule error.** Check the flow
   direction data before rewriting spawn rules.
5. **Weights are tuning, not truth.** Mark intensity weights `[tune]` and give the
   telemetry that will set them.
6. **Group cleverness the player cannot read is wasted CPU.** Prefer a simpler tactic
   with a tell over a smarter one without.

## Example Output

**Input:** 4-player co-op horde shooter. Player 100 HP, no mitigation. Melee grunt
8 DPS on contact, ranged grunt 4 DPS. TTD target when surrounded ≥ 4 s. Current
tokens: 3 melee + 2 ranged per player. Session 30 min. Telemetry: 6 relax phases in
30 min; downed players report "pile-on"; 11% of spawns within a player's view frustum.

```
# Squad and director spec — co-op horde mode

## Coordination mechanisms
Attack tokens + position claims (flank arcs). Role assignment rejected for grunts —
too little behaviour to read; kept for the "Caller" special only.

## Tokens and TTD
| Role | Tokens/player | DPS | Sum |
| Melee | 3 → 2 | 8 | 24 → 16 |
| Ranged | 2 | 4 | 8 |
| Total incoming | | | 32 → 24 DPS |
TTD = 100 ÷ 32 = 3.1 s (fails ≥ 4 s) → 100 ÷ 24 = 4.2 s (passes).
Extra melee circle at 4 m, taunting; they take a token as one is released.

## Roles and claims
| Flank arc | nearest enemy with path ≤ 15 m | claim arc on blackboard | release on death or 6 s | "Going round!" bark |
| Ranged token | holder must have LOS | — | release after 1 s without LOS | muzzle flash |

## Intensity model
intensity += 1 per HP lost + 5 per kill within 5 m + 20 when downed; decay 5/s after
4 s without damage. Peak trigger: MAX across players (was mean). Mean let one downed
player at 100 sit under three at 20 (mean 40 < 70), so the horde kept coming.

## Director cycle
| Build-up | all players < 70 | 1 spawn / 2 s | until peak (~60 s) |
| Peak | any player ≥ 70 | sustain current wave | 4 s |
| Fade | after sustain | no new spawns | until all < 25 (~10 s) |
| Relax | after fade | ambient wanderers only | ≥ 35 s |
Cycle ≈ 60 + 4 + 10 + 35 = 109 s → ≈ 16 peaks in 30 min (observed 6 relaxes: mean trigger).

## Spawn rules
| Not in any view frustum + no LOS | credibility | log angle-to-camera per spawn (was 11%) |
| Path distance ≥ 20 m | time to read threat | log path distance |
| Ahead on flow ≥ 60% of spawns | behind reads as punishment | flow-distance per spawn |
| Handcrafted crescendo events suspend director | designer set pieces | event flag |

## Failure modes
| Pile-on on downed player | mean trigger | MAX trigger | intensity trace at downs |
| Ranged hoard tokens behind walls | no LOS release | 1 s LOS release | tokens held without LOS |
| Flankers all go left | shared arc | arc claims | claims per arc |

## Adaptation bounds
Co-op PvE only; described in the game's help text. Spawn budget never exceeds the
mode's authored maximum and never falls below 50% of it. No purchasable item affects it.

## Confidence
TTD maths: High. Intensity weights: Low [tune] — set from 2 weeks of traces.
Pile-on cause: High — reproduced in 3 traces.
```

## Techniques Used

- **DS-01 Framework Application** — attack tokens, claims, roles and the director cycle as named patterns.
- **NE-11 Embedded Calculation Formulas** — token-sum TTD, intensity accumulation and cycle length.
- **DP-07 Failure Mode Prediction** — pile-on, hoarding, same-route flanking and spawn-in-view with guards.
- **CM-11 Reasoning-Based Constraint Design** — every spawn rule carries the reason that lets edge cases be judged.

## Related Prompts

- `domain-game-development/ai/ai_npc_decision_architecture.md` — the individual agent beneath the group layer.
- `domain-game-development/level-design/level_blockout_and_pacing.md` — handcrafted beats the director must not override.
- `domain-game-development/design/design_difficulty_combat_balancing.md` — TTK/TTD targets and dynamic-difficulty ethics.
