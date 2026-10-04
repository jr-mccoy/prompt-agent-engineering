---
title: "Adaptive Music System Design — Vertical Layering, Horizontal Resequencing, Transition Matrix, and Repetition Budget"
category: game-development/audio
description: "Design how a game's score responds to play: map game states to a small set of music states, choose vertical layering, horizontal resequencing or a hybrid per state, specify every transition's sync point, bridge and stinger with its worst-case latency in seconds, add hysteresis so music does not thrash, and budget enough material that the longest-dwelt states do not loop audibly."
techniques:
  - DS-01
  - NE-11
  - OC-03
  - DP-07
difficulty: intermediate
tags:
  - game-audio
  - adaptive-music
  - interactive-music
  - vertical-layering
  - horizontal-resequencing
  - music-transitions
  - music-loops-too-much
  - music-cuts-awkwardly
  - combat-music-wont-stop
updated: "2026-10-03"
related_prompts:
  - domain-game-development/audio/audio_system_architecture.md
  - domain-game-development/audio/audio_gameplay_readability_mix.md
  - domain-game-development/level-design/level_blockout_and_pacing.md
---

# Adaptive Music System Design

**Objective:** Produce a music design that composers, audio designers and engineers
can all build from: the music states, the technique each uses, a transition matrix
with sync points and latencies, the parameters that drive it, and a material budget
that keeps the score from wearing thin.

**When to Use:**
- A score is being commissioned or restructured and nobody has written how it will
  respond to play.
- Players say the music "loops too much", "cuts awkwardly" or "combat music won't stop".
- A composer needs to know stem counts, tempos, loop lengths and exit points before
  writing.
- **Not this prompt if** you need bus hierarchy, middleware choice, voice limits,
  streaming and memory — use `domain-game-development/audio/audio_system_architecture.md`;
  that prompt plumbs music into the engine, this one designs how the music behaves.
  For whether music masks gameplay-critical sound, use
  `domain-game-development/audio/audio_gameplay_readability_mix.md`.

## Inputs / Context

1. **Game states** that could drive music: exploration, tension, combat tiers,
   boss phases, stealth, menus, story scenes, victory, death.
2. **Dwell times**: how long players typically stay in each state (telemetry,
   playtest, or design estimate).
3. **Musical constraints**: tempos and meters, keys, instrumentation, how many
   minutes of music the budget can buy.
4. **Middleware or engine** capabilities (e.g. FMOD, Wwise, engine-native) — which
   sync points and transition features it supports `[verify against current docs]`.
5. **Pacing references**: level beat charts, encounter director cycle, cinematic list.
6. **Stream budget** from the audio architecture (concurrent streams available to music).

## Method

1. **Collapse game states into music states.** Many game states share one music
   state; a music state exists only if the player should *feel* a change. Aim for
   the fewest states that carry the emotional arc.
2. **Choose a technique per state (DS-01).**
   - *Vertical layering (re-orchestration)*: stems of one piece added or removed by a
     parameter. Responds within one fade; harmony and tempo cannot change.
   - *Horizontal resequencing*: segments chained, switching at sync points; allows
     new keys, tempos and themes but responds only at the next sync point.
   - *Hybrid*: horizontal between states, vertical within one.
   - *Stingers* over the top for one-off events; *silence* as a deliberate state.
3. **Compute transition latency (NE-11).** `beat = 60 ÷ BPM`;
   `bar = beats per bar × beat`; worst-case wait = one sync unit (beat, bar, phrase,
   segment end). Assign sync points by urgency: threat onset needs ≤ ~1 bar plus an
   immediate stinger; resolution can wait for a phrase.
4. **Write the transition matrix (OC-03).** For each from → to: sync point,
   bridge/transition segment, fade-out and fade-in times, stinger, worst-case latency
   in seconds.
5. **Add hysteresis.** Enter thresholds and exit thresholds differ; exit requires a
   hold time with no threat. Smooth continuous parameters (slew rate) so layers do
   not pump.
6. **Budget the material.** For each state:
   `repetitions per visit = median dwell ÷ unique material length`. Above ~2–3 in a
   long-dwell state, add alternate segments (random without immediate repeat),
   variations or planned silence windows.
7. **Predict failure modes (DP-07).** Thrash between neighbouring states; stinger
   spam; combat music outliving the fight; layers out of phase after a seek;
   music state contradicting a cinematic; transitions landing under dialogue.
8. **Specify the parameters and owners.** Each parameter: source in game code,
   range, smoothing, who tunes it.

## Output Format

```
# Adaptive music design — [game / area]   Tempo/meter: [..]

## Music states        — state | game states mapped | technique | material (min:s) | stems
## Parameters          — name | source | range | smoothing | owner
## Latency units       — beat / bar / phrase in seconds at each tempo
## Transition matrix   — from → to | sync | bridge | fades | stinger | worst-case latency
## Hysteresis          — enter / exit thresholds, hold times
## Repetition budget   — state | median dwell | unique material | repeats | remedy
## Failure modes       — symptom | cause | guard
## Composer brief      — per state: tempo, key range, stem list, loop/exit points
## Confidence
```

## Verification

- [ ] Every music state has a technique and a reason for it.
- [ ] Every transition in the matrix has a worst-case latency computed from tempo.
- [ ] Threat-onset transitions are responsive (stinger or ≤ ~1 bar) or the delay is justified.
- [ ] Every exit has a hold time or hysteresis.
- [ ] Repetition figures follow from stated dwell and material lengths.
- [ ] Stem counts fit the stream budget from the audio architecture.

## False-Positive Prevention

1. **Delay is not always a defect.** Waiting for a phrase end on resolution is
   musical; only threat onset and failure states need speed.
2. **Silence is a state, not a gap.** Do not fill every minute; long exploration often
   benefits from planned silence.
3. **Not every game needs adaptive music.** A puzzle or narrative game with authored
   cues per scene may be better served by a linear cue list.
4. **Dwell times drive the budget.** Do not demand variations for a state players
   see for 40 seconds.
5. **Middleware features differ by version.** Mark sync and transition features
   `[verify against current docs]`; do not promise behaviour the tool may not have.
6. **Taste is not a finding.** Comment on structure, timing and repetition; leave
   the composition to the composer.

## Example Output

**Input:** Open-world adventure, gameplay music at 96 BPM 4/4. Game states:
explore (day/night), stealth, alerted, combat (scaled by enemy count), boss,
victory, death, town. Median dwell: explore 18 min/session, combat 70 s, town 6 min.
Complaints: combat music lingers; explore loop "heard it a hundred times". Stream
budget for music: 4.

```
# Adaptive music design — overworld   96 BPM, 4/4

## Music states
| State | Game states | Technique | Material | Stems |
| Explore | explore day/night, stealth | horizontal pool of segments | 6 × 0:40 = 4:00 | 2 |
| Tension | alerted | vertical layer on Explore (+perc) | shares Explore | +1 |
| Combat | combat 1–8 enemies | vertical: 4 stems by intensity | 1:20 loop | 4 |
| Boss | boss | horizontal per phase | 3 × 1:00 | 4 |
| Town | town | horizontal | 2 × 1:30 | 2 |
| Stingers | victory, death, discovery | one-shots | 3 × 0:04 | — |

## Latency units (96 BPM)
beat 0.625 s · bar 2.5 s · 4-bar phrase 10 s

## Transition matrix
| From → to | Sync | Bridge | Fades | Stinger | Worst case |
| Explore → Combat | next bar | 1-bar riser | out 0.5 s / in 0 | hit on next beat | 0.63 s stinger, 2.5 s music |
| Combat → Explore | phrase end after hold | 2-bar tail | out 2 s | — | hold 8 s + 10 s = 18 s |
| Combat → Victory | next beat | — | out 1 s | victory | 0.63 s |
| Any → Death | immediate | — | cut, 1.5 s reverb tail | death | 0 s |
| Explore → Town | segment end | — | crossfade 4 s | — | 40 s (segment) |

## Hysteresis
Combat intensity param: slew 0.5/s. Enter Combat at threat ≥ 0.3; exit at threat
< 0.1 held 8 s (was 0, causing flips during reloads, but exit used segment end
= 80 s → "music won't stop"). Now phrase end: worst case 18 s.

## Repetition budget
| Explore | 18 min | 4:00 pool + 1:00 silence after every 3 segments = 6:00 per pass | 18 ÷ 6 = 3.0 passes, never same order | OK |
| Combat | 70 s | 1:20 | 0.9 | OK |
| Town | 6 min | 3:00 | 2.0 | OK |
Was: single 3:20 Explore loop → 18 ÷ 3.33 = 5.4 identical repeats.

## Failure modes
| Combat ↔ Explore flips | equal enter/exit thresholds | hysteresis + 8 s hold |
| Stinger spam on multi-kills | stinger per kill | max 1 per 4 bars |
| Combat stems pump | raw enemy count | slewed intensity param |
| Music under dialogue | no rule | dialogue lowers to 2 stems (mix ducking per architecture) |

## Composer brief (Explore)
96 BPM, 4/4, D dorian ± relative keys; 6 segments of 16 bars, each starts and ends
on tonic-compatible harmony; 2 stems (bed, melody) + percussion layer for Tension.

## Confidence
Latencies: High (from tempo). Dwell times: Medium — 2 weeks of telemetry.
Silence windows: Medium — needs playtest.
```

## Techniques Used

- **DS-01 Framework Application** — vertical layering, horizontal resequencing, hybrid and stingers as named techniques per state.
- **NE-11 Embedded Calculation Formulas** — beat/bar/phrase latency and repetitions per visit.
- **OC-03 Markdown Table Specification** — the transition matrix engineers and composers build from.
- **DP-07 Failure Mode Prediction** — thrash, stinger spam, pumping and dialogue collisions with guards.

## Related Prompts

- `domain-game-development/audio/audio_system_architecture.md` — buses, middleware, streaming and voices that carry the score.
- `domain-game-development/audio/audio_gameplay_readability_mix.md` — keeping music from masking gameplay cues.
- `domain-game-development/level-design/level_blockout_and_pacing.md` — the beat chart music states follow.
