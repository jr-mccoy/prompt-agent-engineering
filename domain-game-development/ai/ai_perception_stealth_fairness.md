---
title: "Enemy Perception and Stealth Fairness Tuning — Sight Cones, Awareness Meters, Tells, and the Cheating-AI Audit"
category: game-development/ai
description: "Tune how enemies see and hear the player so detection is fast enough to threaten and fair enough to learn: write the perception model as a formula, compute time-to-suspicious and time-to-alert for representative scenarios, set a minimum reaction window between the first tell and full detection, check that the AI senses the same light, cover and noise the player is shown, and audit every way the AI might be cheating."
techniques:
  - NE-11
  - DS-02
  - QA-18
  - QA-24
difficulty: advanced
tags:
  - game-ai
  - stealth-design
  - enemy-perception
  - awareness-meter
  - sight-cone
  - telegraphing
  - spotted-out-of-nowhere
  - guards-see-through-walls
  - stealth-feels-unfair
updated: "2026-10-03"
related_prompts:
  - domain-game-development/ai/ai_npc_decision_architecture.md
  - domain-game-development/design/design_hud_and_game_feel_review.md
  - domain-game-development/design/design_difficulty_combat_balancing.md
---

# Enemy Perception and Stealth Fairness Tuning

**Objective:** Turn "the guards feel unfair" into a perception model with numbers:
how quickly each situation leads to suspicion and to full alert, how long the player
has to react after the first tell, and whether the AI is using any information the
player cannot see.

**When to Use:**
- A stealth or stealth-optional game is in tuning and players report being "spotted
  out of nowhere" or, the opposite, walking past guards with impunity.
- The awareness meter, light indicator or noise display and the AI's actual senses
  were built by different people and may disagree.
- You need detection rules designers can tune per difficulty without an engineer.
- **Not this prompt if** you are choosing the decision architecture (BT, utility,
  GOAP) or the per-frame AI budget — use
  `domain-game-development/ai/ai_npc_decision_architecture.md`; this prompt tunes the
  senses that feed that layer. For the HUD indicator's size, contrast and placement,
  use `domain-game-development/design/design_hud_and_game_feel_review.md`. For combat
  time-to-kill once a fight starts, use
  `domain-game-development/design/design_difficulty_combat_balancing.md`.

## Inputs / Context

1. **Senses implemented**: vision cone (half-angles, ranges), peripheral zone,
   hearing radii per action and surface, any special senses (smell, cameras, dogs).
2. **Awareness model**: meter range, fill and decay rates, thresholds (suspicious,
   searching, alert), and the modifiers applied (distance, light, posture, movement).
3. **Player-facing signals**: light/visibility indicator, noise ring, awareness
   icons over heads, barks and animations at each threshold.
4. **Where the AI samples**: which points on the player body are raycast and lit
   for visibility, and how occlusion and foliage are handled.
5. **Evidence of the problem**: playtest notes, telemetry of detections (distance,
   light value, posture), video of disputed detections.
6. **Difficulty modes** and what each is allowed to change.

## Method

1. **Write the model as one formula (NE-11).**
   `fill rate = base × distance factor × light × posture × movement × zone`
   per second while the player is perceived; `decay` per second when not.
   `time to threshold T = T ÷ fill rate`. If decay exceeds the fill rate the player
   is never detected in that situation — say so explicitly.
2. **Set the fairness metrics before tuning (DS-02).** Agree targets such as:
   reaction window (time from the first tell to full alert) ≥ a stated value beyond
   point-blank range; "safe" states (e.g., crouched, still, in shadow beyond X m)
   that never reach alert; same situation → same outcome every time.
3. **Build the scenario matrix.** 6–10 representative situations spanning
   distance, light, posture, movement and focal vs peripheral vision. Compute time
   to suspicious, time to alert and the reaction window for each; mark each cell
   against the targets.
4. **Check perception symmetry.** For each modifier, compare what the AI samples
   with what the player is shown: light at the same body point as the indicator,
   occlusion against the same geometry the player sees as cover, noise radius
   matching the noise display, foliage that hides from both or neither.
5. **Run the cheating-AI audit (QA-18, QA-24).** Check each candidate and record it
   as *cheat*, *intended* (and disclosed or readable) or *cleared* with the guard
   that clears it: knows position after losing sight; sees through foliage or
   thin cover the player reads as hiding; hears through walls without attenuation;
   shares knowledge instantly with allies with no audible call; detects at range
   before any tell plays; spawns or turns to face the player on cue.
6. **Map tells to thresholds.** Every threshold needs a tell the player can perceive
   from the player's likely position: a bark, a head turn, a step toward, an icon.
   The tell must play before the state change it announces.
7. **Write the per-difficulty levers.** Which multipliers change by mode (base rate,
   decay, thresholds) — not the symmetry rules, which hold on every mode.
8. **List the telemetry to keep it honest.** Detection events with distance, light
   value sampled, posture, zone and the time since first tell.

## Output Format

```
# Perception tuning — [game / archetype]   Modes: [..]

## Model
fill rate = [..]; decay = [..]; thresholds: suspicious [..] / alert [..]
| Modifier | Values | AI samples at | Player is shown via |

## Fairness targets
| Metric | Target | Source of target |

## Scenario matrix
| # | Situation | Fill/s | t suspicious | t alert | Window | Verdict |

## Symmetry check
| Modifier | AI sense | Player signal | Match? | Fix |

## Cheating-AI audit
| Candidate | How checked | Verdict (cheat / intended / cleared) | Guard or fix |

## Tells by threshold
| Threshold | Tell (audio / anim / UI) | Plays at | Readable from |

## Difficulty levers  |  Telemetry to add  |  Confidence
```

## Verification

- [ ] Every scenario cell is reproducible from the stated formula and modifiers.
- [ ] Fairness targets were written before the scenario matrix was computed.
- [ ] Every modifier has both an AI sampling point and a player-facing signal.
- [ ] Every cheating candidate has a verdict; "cleared" names the guard that clears it.
- [ ] Every threshold has a tell that plays before the state change.
- [ ] Symmetry rules are identical on every difficulty mode.

## False-Positive Prevention

1. **Fast detection is not unfair detection.** Being seen in two-tenths of a
   second while sprinting in a lit doorway is correct; the defect is a short
   window the player could not have read.
2. **Some "cheats" are design.** A guard who searches the last-known position, or
   a scripted ambush, is legitimate when readable; record it as intended.
3. **Do not flag decay-dominated safety as a bug.** A state that never reaches
   alert may be the intended safe state — check the targets first.
4. **Video is not proof of the numbers.** A disputed clip shows a symptom; confirm
   the sampled light and distance from telemetry or a debug overlay before calling
   it a symmetry fault.
5. **Generous is a choice.** Easy modes may lengthen windows; flag only if a mode
   breaks a symmetry rule or makes detection impossible where the brief needs threat.
6. **Rates are estimates until captured.** Mark modifiers `[measure]` when taken
   from design docs rather than the build.

## Example Output

**Input:** First-person stealth game, human guards. Base 2.0/s inside 5 m focal
(half-angle 30°), linear falloff to 0.25 at 20 m; peripheral (30–60°) ×0.4. Light:
lit 1.0, shadow 0.3. Posture: stand 1.0, crouch 0.6. Movement: still 0.5, walk 1.0,
sprint 1.5. Decay 0.15/s. Suspicious 0.4, alert 1.0. Complaint: "spotted from the
shadows" in the courtyard.

```
# Perception tuning — human guard   Modes: Story / Normal / Hard

## Model
fill = 2.0 × f(d) × light × posture × move × zone;  f(d) = 1 − 0.75 × (d − 5)/15 for 5–20 m
| Modifier | Values | AI samples at | Player is shown via |
| Light | lit 1.0 / shadow 0.3 | player FEET point | light gem (samples CHEST) |
| Occlusion | 3 rays: head, chest, feet | any ray clear = seen | cover outline |
| Noise | metal 12 m, stone 6 m | sphere, no wall attenuation | noise ring |

## Fairness targets (agreed with design lead)
| Window first tell → alert beyond 3 m (Normal) | ≥ 0.6 s |
| Crouched + still + shadow beyond 8 m | never reaches alert |

## Scenario matrix
| # | Situation | Fill/s | t susp. | t alert | Window | Verdict |
| 1 | Crouch, still, shadow, focal 12 m (f 0.65) | 0.117 | never | never | — | OK (decay 0.15 wins) |
| 2 | Walk, lit, peripheral 12 m | 0.52 | 0.77 s | 1.92 s | 1.15 s | OK |
| 3 | Sprint, lit, focal 18 m (f 0.35) | 1.05 | 0.38 s | 0.95 s | 0.57 s | Miss by 0.03 s → sprint 1.5 → 1.4 gives 0.61 s |
| 4 | Crouch-walk under courtyard awning, focal 8 m (f 0.85), feet lit | 1.02 | 0.39 s | 0.98 s | 0.59 s | FAIL — player was shown shadow |
| 4' | Same, light sampled at chest (0.3) | 0.306 | 1.31 s | 3.27 s | 1.96 s | OK |

## Symmetry check
| Light | feet point | gem uses chest | No | sample chest for both; gem driven by AI value |
| Noise | sphere through walls | ring drawn on floor | No | −50% radius per wall crossed |

## Cheating-AI audit
| Knows position after losing sight | debug overlay, 10 trials | cleared | search uses last-known position |
| Allies alerted instantly | 30 m broadcast, no bark | cheat | propagate only via audible shout (1.2 s) |
| Sees through hedge the player hides in | hedge has no occluder | cheat | add occluder or mark hedge as "thin" in UI |
| Detection before any tell | scenario 4 | cheat (via symmetry) | fixed by 4' |
| Turns to face player on alarm | scripted at 2 events | intended | keep; add audible cue first |

## Tells by threshold
| 0.4 suspicious | "Hm?" bark + head turn + yellow icon | at 0.4 | 25 m |
| 0.7 | guard steps toward source | at 0.7 | in view |
| 1.0 alert | shout + red icon | at 1.0 | 30 m (audible) |

## Difficulty levers
Base rate Story 1.4 / Normal 2.0 / Hard 2.6; decay unchanged; symmetry fixed on all.
Scenario 3 on Hard (sprint 1.4): fill 2.6 × 0.35 × 1.4 = 1.27 → window 0.47 s. The
window target is a Normal-mode rule; Hard documents the shorter window in its mode
description rather than breaking a symmetry rule.

## Telemetry to add
detect event: distance, light value sampled, posture, zone, time since first tell.

## Confidence
Model maths: High. Rates: Medium [measure] — taken from design sheet, not build.
Courtyard diagnosis: High — debug overlay shows feet point in lamp cone.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — fill-rate product and time-to-threshold for every scenario.
- **DS-02 Metric Specification** — reaction-window and safe-state targets set before tuning.
- **QA-18 Domain-Specific Smell Tests** — the stealth-specific cheating candidates checked on every archetype.
- **QA-24 Dismissed-Candidates Coverage Table** — each candidate recorded as cheat, intended or cleared with its guard.

## Related Prompts

- `domain-game-development/ai/ai_npc_decision_architecture.md` — the decision layer these senses feed.
- `domain-game-development/design/design_hud_and_game_feel_review.md` — readability of the indicators the player relies on.
- `domain-game-development/design/design_difficulty_combat_balancing.md` — what happens once detection becomes a fight.
