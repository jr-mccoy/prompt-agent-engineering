---
title: "Level Flow and Pacing Analysis from Telemetry — Funnel, Intended-vs-Observed Beat Chart, Hotspots, and Cleared Hypotheses"
category: game-development/level-design
description: "Analyse a playable level from position traces and events: build the section funnel with quits, compare observed median time per beat with the designed beat chart, compute path efficiency, dwell hotspots and death clusters, separate confusion from difficulty from intended exploration, clean instrumentation artefacts, record the hypotheses checked and cleared, and set retest targets for each fix."
techniques:
  - RT-06
  - NE-11
  - QA-04
  - QA-24
difficulty: intermediate
tags:
  - level-design
  - game-telemetry
  - heatmaps
  - player-flow
  - pacing-analysis
  - funnel-analysis
  - players-quit-this-level
  - players-get-lost
  - level-takes-too-long
updated: "2026-10-03"
related_prompts:
  - domain-game-development/level-design/level_blockout_and_pacing.md
  - domain-game-development/testing/testing_playtest_protocol_synthesis.md
  - domain-game-development/design/design_difficulty_combat_balancing.md
---

# Level Flow and Pacing Analysis from Telemetry

**Objective:** Use what players actually did in a level — where they went, how long
each beat took, where they died, stalled or quit — to show where the level departs
from its design, diagnose why, and set measurable targets for the retest.

**When to Use:**
- A level is playable end to end and a beta, external playtest or live build has
  produced position traces and events.
- The level runs far longer than designed, or a section loses players.
- The team argues whether a stall is confusion, difficulty or players enjoying the space.
- **Not this prompt if** the level is still on paper or in greybox and you are
  planning metrics, beats and teaching — use
  `domain-game-development/level-design/level_blockout_and_pacing.md`; this prompt
  checks the finished level against that plan. For running the playtest itself and
  synthesising what players said, use
  `domain-game-development/testing/testing_playtest_protocol_synthesis.md`. For
  re-tuning an encounter's damage numbers, use
  `domain-game-development/design/design_difficulty_combat_balancing.md`.

## Inputs / Context

1. **Designed beat chart**: sections, purpose, intensity, intended minutes.
2. **Section events**: enter/exit per section per player, quits, completion.
3. **Position traces** (e.g. sampled once a second) and the critical-path length per
   section.
4. **Deaths** with position and cause; retries; interactions with key objects.
5. **Session context**: pause, menu and loading time; idle detection; build version.
6. **Player segments**: genre experience, difficulty mode, platform; sample size per segment.

## Method

1. **Clean the data first.** Exclude pause, menu and load time from durations;
   exclude idle sessions by a stated rule; confirm section triggers fire once.
   Report what was excluded and how many sessions remain.
2. **Build the funnel.** Players entering each section, quits inside each section,
   and completion. A quit concentration in one section is the first lead.
3. **Compare observed to intended (NE-11).** Per section: median and interquartile
   range of time, ratio `observed median ÷ intended minutes`; flag outside a stated
   band (e.g. 0.75–1.33). Note that the sum of section medians is not the median total.
4. **Compute flow metrics (NE-11).** `path efficiency = distance travelled in section
   ÷ critical-path length`; dwell hotspots (cells or volumes with long median dwell);
   backtracking (re-entries to earlier sections); deaths per player reaching the
   section and their spatial clusters by cause.
5. **Diagnose by pattern (RT-06).**
   - *Confusion*: long dwell, high path efficiency ratio, low deaths, quits without death.
   - *Difficulty*: deaths and retries concentrated at a cluster, time driven by retries.
   - *Intended exploration*: long time in optional space, normal critical-path time, no quits.
   - *Under-engagement*: very short times on content meant to be looked at.
   Cross-check with the intended intensity: a long, deadly section designed as a
   peak is less alarming than the same numbers in a rest beat.
6. **Record checked-and-cleared hypotheses (QA-24).** Each suspected problem the
   data does not support, with the evidence that clears it.
7. **State confidence by sample (QA-04).** Counts, not percentages, for small
   segments; separate new and experienced players where they differ.
8. **Set retest targets.** For each fix: the metric, the current value, the target,
   and the sample needed to judge it.

## Output Format

```
# Level flow analysis — [level]   Build: [..]   Sessions: [n in funnel / n used for times]

## Data cleaning      — exclusions and reasons
## Funnel             — section | entered | quits inside | reached next
## Beat comparison    — section | intended min | observed median (IQR) | ratio | flag
## Flow metrics       — section | path efficiency | top dwell hotspot | deaths/player | top death cause
## Diagnoses          — section | pattern | evidence | confidence
## Cleared hypotheses — hypothesis | evidence that clears it
## Fixes and retest   — fix | metric | now | target | sample needed
```

## Verification

- [ ] Exclusions are stated with counts and the remaining sample.
- [ ] Funnel counts are monotonic and quits reconcile with the drop between sections.
- [ ] Every ratio is computed from the stated intended and observed values.
- [ ] Every diagnosis cites at least two metrics that fit its pattern.
- [ ] Cleared hypotheses name the evidence, not just "fine".
- [ ] Every fix has a numeric retest target.

## False-Positive Prevention

1. **Long is not broken.** Players lingering in optional space they enjoy is
   success; check critical-path time and quits before calling it a problem.
2. **Short rest beats are usually fine.** Players skimming a lore room is not a
   pacing failure unless the room carries must-convey story.
3. **Deaths in a peak are the design.** Judge death clusters against the beat's
   intended intensity and the game's difficulty identity.
4. **Heatmaps show where, not why.** Pair a hotspot with what is visible from it
   before proposing a fix.
5. **Instrumentation lies quietly.** Pause time, AFK sessions and double-firing
   triggers produce fake stalls; clean before diagnosing.
6. **Small segments are anecdotes.** Report counts and avoid percentages for groups
   of a dozen or fewer.

## Example Output

**Input:** "Flooded Cannery", linear action level, designed at 22 minutes (beats
B1–B8 from the blockout plan). External beta: 64 sessions, 58 completions; 2 AFK
completions excluded from time medians.

```
# Level flow analysis — Flooded Cannery   Build: beta 2   Sessions: 64 in funnel; 56 completers for total time

## Data cleaning
Pause/menu/load time removed. 2 completers idle > 30 min excluded from times → 56
completers for total time. Section triggers verified single-fire.

## Funnel
| B1–B3 | 64 | 1 quit in B3 | 63 |
| B4 | 63 | 0 | 63 |
| B5 Valve room | 63 | 4 | 59 |
| B6 Arena | 59 | 0 | 59 |
| B7 Chase | 59 | 1 | 58 |
| B8 Roof | 58 | 0 | 58 completed |

## Beat comparison (band 0.75–1.33)
| B1 | 2 | 2.5 | 1.25 | — |
| B2 | 3 | 3.4 | 1.13 | — |
| B3 | 3 | 3.8 | 1.27 | — |
| B4 rest | 2 | 1.2 | 0.60 | low |
| B5 valve | 4 | 9.6 (6.1–14.0) | 2.40 | HIGH |
| B6 arena | 4 | 5.1 | 1.28 | — |
| B7 | 2 | 2.4 | 1.20 | — |
| B8 | 2 | 1.0 | 0.50 | low |
Sum of medians 29.0 min; median total 28.4 min vs 22 designed.

## Flow metrics
| B5 | 3.1 (level median 1.4) | locked stairwell door: 41/63 dwell > 60 s | 0.1 | — |
| B6 | 1.3 | drained-tank cover | 2.9 (171 deaths / 59) | catwalk riflemen 61% (104) |

## Diagnoses
| B5 | Confusion | path efficiency 3.1, door dwell 41/63, deaths 0.1, all 4 quits after > 10 min with 0 deaths | High |
|    | Segment | new players 17/22 dwell at door; experienced 24/41 | Medium |
| B6 | Difficulty spike at the twist | 61% of deaths from catwalk after cover drains; time near design | Medium |

## Cleared hypotheses
| B2 conveyor jump too hard | 0.3 deaths/player; time ratio 1.13 |
| B4 rest room skipped = boredom | rest beat, no must-convey story; 0 quits |
| B8 too short | reward beat; chest opened by 58/58 |

## Fixes and retest
| B5: light shaft + valve glint visible from door | median B5 time | 9.6 | ≤ 5.0 min | ≥ 30 sessions |
|  | door dwell > 60 s | 41/63 | ≤ 1 in 4 | same |
| B6: 3 s klaxon + lights before drain; riflemen enter after drain | deaths/player | 2.9 | ≤ 1.8 | ≥ 30 sessions |
Retune of rifleman damage, if needed, goes to the combat balancing pass.
```

## Techniques Used

- **RT-06 Correlation and Cross-Analysis** — dwell, path efficiency, deaths and quits read together to separate confusion from difficulty.
- **NE-11 Embedded Calculation Formulas** — observed-to-intended ratios, path efficiency and deaths per player.
- **QA-04 Uncertainty Acknowledgment** — counts for small segments and confidence per diagnosis.
- **QA-24 Dismissed-Candidates Coverage Table** — suspected problems checked and cleared with their evidence.

## Related Prompts

- `domain-game-development/level-design/level_blockout_and_pacing.md` — the designed beat chart this analysis tests.
- `domain-game-development/testing/testing_playtest_protocol_synthesis.md` — running the sessions and weighing what players said.
- `domain-game-development/design/design_difficulty_combat_balancing.md` — re-tuning the encounter behind a death spike.
