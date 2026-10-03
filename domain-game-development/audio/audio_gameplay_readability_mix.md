---
title: "Gameplay Readability Mix Pass — Information Priority, Loudness, Masking, Repetition, and Localisation"
category: game-development/audio
description: "Audit a game's actual mix for whether players can hear what they need to act on: rank every sound by the decision it informs, measure integrated loudness and true peak against a stated platform target, find where gameplay-critical cues are masked in level or frequency, check variation counts and randomisation on high-frequency sounds, test whether players can locate threats by ear, and close gaps with priority, ducking and accessibility options."
techniques:
  - RT-02
  - DS-02
  - QA-18
  - DS-06
difficulty: intermediate
tags:
  - game-audio
  - mixing
  - sound-design
  - audio-readability
  - spatial-audio
  - audio-accessibility
  - cant-hear-footsteps
  - game-too-loud
  - sounds-repetitive
updated: "2026-10-03"
related_prompts:
  - domain-game-development/audio/audio_system_architecture.md
  - domain-game-development/design/design_hud_and_game_feel_review.md
  - domain-game-development/ai/ai_perception_stealth_fairness.md
---

# Gameplay Readability Mix Pass

**Objective:** Tell the audio team which gameplay-critical sounds players cannot
hear, locate or tell apart in real play, why (level, masking, priority, repetition,
spatialisation), and what to change — each finding backed by a capture measurement
or a listening test, not a preference.

**When to Use:**
- A milestone build needs a mix pass before external playtest or certification.
- Players say "I can't hear footsteps", "the game is too loud" or "it all sounds the same".
- A competitive or stealth game depends on audio as information and nobody has
  tested whether it delivers it.
- **Not this prompt if** you are designing bus structure, middleware, voice limits
  or memory — use `domain-game-development/audio/audio_system_architecture.md`; this
  prompt audits the mix that architecture produces. For the feel of a single action
  (hitstop, shake, impact layers), use
  `domain-game-development/design/design_hud_and_game_feel_review.md`. For whether
  enemies *hear the player* fairly, use
  `domain-game-development/ai/ai_perception_stealth_fairness.md`.

## Inputs / Context

1. **Captures**: multitrack or bus-level recordings of a quiet scene, a typical
   fight and the busiest fight, from the target platform's output.
2. **Sound inventory** for gameplay events: event, bus, priority, voice limit,
   variation count, randomisation (pitch/volume), attenuation range.
3. **Platform and listening setups**: TV speakers, headphones, handheld speakers;
   the loudness target the team has chosen and its source.
4. **Mode**: single-player, co-op, competitive; whether audio is a competitive signal.
5. **Accessibility options** already present (subtitles for sounds, visual sound
   indicators, mono, dynamic-range settings, per-bus sliders).
6. **Player reports** with locations or clips.

## Method

1. **Rank sounds by information value (RT-02).** For each gameplay sound: the
   decision it informs (dodge, turn, reload, retreat), urgency, and whether another
   channel (UI, animation) carries the same information. Tiers: *critical*
   (decision fails without it), *supporting*, *ambience/music*.
2. **Measure loudness (DS-02).** Integrated loudness (LUFS) over each capture and
   maximum true peak (dBTP), against the team's chosen target — e.g. a published
   console loudness recommendation `[verify current]`. Record the meter and the
   target's source. Report the offset in LU.
3. **Find masking.** For each critical cue in the busy capture: its level relative
   to the bed around it and its main frequency band versus what is loud at the same
   moment (weapon tails, music, explosions, allies). A critical cue more than a few
   dB under a sound in the same band is a candidate.
4. **Check priority and ducking.** Does the critical cue survive voice limits? Is
   anything ducked *under* it, or is it ducked under something less important?
   Prefer ducking the competitor in the cue's band over raising the cue.
5. **Run the repetition smell tests (QA-18).** High-frequency sounds with fewer
   variations than plays per few seconds ("machine-gun effect"); no
   random-without-repeat; no pitch/volume randomisation; identical impacts for
   different weights.
6. **Test localisation.** A point-to-the-sound test: N trials across positions
   (front, back, sides, above/below) on headphones and speakers; record errors,
   especially front/back confusion and elevation.
7. **Check accessibility.** Critical cues captioned or visualised; mono option
   keeps critical cues audible; separate sliders; a reduced dynamic range option.
8. **Prioritise (DS-06).** Severity by effect on decisions: *blocks* (cue
   unheard), *degrades* (heard late or mislocated), *polish*. Mark which need a
   listening test to confirm.

## Output Format

```
# Readability mix pass — [game / build]   Target: [LUFS ± , dBTP] (source)

## Information ranking   — sound | decision informed | tier | other channel?
## Loudness              — capture | integrated LUFS | max true peak | offset
## Masking               — critical cue | masker | band | level gap | fix
## Priority and ducking  — cue | survives limits? | ducked by / ducks | fix
## Repetition            — sound | plays per 10 s | variations | randomisation | fix
## Localisation test     — position | trials | errors | notes
## Accessibility         — option | present? | covers critical cues?
## Findings              — severity | finding | evidence | fix | needs listening test?
```

## Verification

- [ ] Every critical cue names the decision it informs.
- [ ] Loudness values cite the meter, the capture and the target's source.
- [ ] Every masking finding gives the masker, the band and a measured level gap.
- [ ] Repetition findings give plays per time window against variation count.
- [ ] Localisation results are counts of trials, not impressions.
- [ ] Fixes prefer lowering competitors over raising cues, or explain why not.

## False-Positive Prevention

1. **Loud is not wrong in a set piece.** Judge integrated loudness over representative
   play, not one explosion.
2. **Not every sound must be heard.** Ambience may be masked in a fight by design;
   only critical cues carry a readability requirement.
3. **Raising the cue is usually the wrong fix.** It feeds a loudness war; ducking or
   filtering the masker preserves headroom.
4. **Speakers differ from headphones.** A localisation failure on TV speakers may be
   a limit of the setup; report results per setup.
5. **Do not quote loudness targets from memory.** Record the document and date, or
   mark `[verify current]`.
6. **One tester is not a test.** Localisation and audibility claims need several
   listeners and stated trial counts.

## Example Output

**Input:** 5v5 competitive tactical shooter, PC and console. Target chosen: −24 LUFS
±2 integrated, true peak ≤ −1 dBTP, per the team's console loudness reference
`[verify current]`. Complaint: "can't hear enemies behind me".

```
# Readability mix pass — build 0.31   Target: −24 ±2 LUFS, ≤ −1 dBTP

## Information ranking (excerpt)
| Enemy footsteps | turn / pre-aim | critical | no (no minimap) |
| Enemy reload | push window | critical | no |
| Own low-ammo click | reload | critical | ammo UI |
| Ally footsteps | none mid-fight | supporting | — |
| Music | mood | ambience | — |

## Loudness
| 20-min representative session | −19.1 LUFS | +0.4 dBTP | 4.9 LU hot; peaks clip |
| Busy fight 60 s | −16.8 LUFS | +0.4 dBTP | context: where the overs occur |
| Quiet round start | −27.5 LUFS | −9.0 dBTP | context: quiet scenes sit below the integrated target by design |

## Masking
| Enemy footsteps (1–4 kHz) | own rifle tail 2.5 s | 1–4 kHz | −9 dB | shorten 1P tail to 0.8 s; −4 dB sidechain in 1–4 kHz when enemy step within 15 m |
| Enemy footsteps | ally footsteps, same level | 1–4 kHz | 0 dB | allies −6 dB + high-pass 300 Hz |
| Enemy reload | music | 2–5 kHz | −6 dB | music lowered to bed-only stem in rounds |

## Priority and ducking
Low-ammo click ducked −6 dB by music sidechain → invert: music ducks under click.

## Repetition
| Footsteps (sprint, concrete) | 32 per 10 s | 4 | none | 10 variations, random-no-repeat, ±1 st pitch, ±1.5 dB |

## Localisation test (headphones, 5 players × 4 rear/side positions = 20 trials)
| Rear left/right | 10 | 6 errors (front/back) | HRTF off by default |
| Sides | 10 | 1 error | — |
Retest with HRTF on before calling fixed.

## Accessibility
| Visual sound indicator | No | add for footsteps, reload, gunfire direction |
| Mono | Yes | footstep panning lost — indicator covers it |

## Findings
| Sev | Finding | Evidence | Fix | Test? |
| Blocks | Enemy steps masked by own rifle tail | −9 dB in 1–4 kHz | tail + sidechain | Yes |
| Blocks | Rear steps mislocated | 6/10 front/back errors | HRTF default on headphones | Yes |
| Degrades | Mix 4.9 LU hot, +0.4 dBTP | 20-min session | master −5 dB (→ −24.1), limiter ceiling −1 dBTP | No |
| Degrades | Footstep machine-gun | 32 plays/10 s on 4 variations | 10 variations + randomisation | Yes |
| Polish | Ally steps compete | 0 dB gap | −6 dB, HPF | No |
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — each sound scored on decision, tier, level, band, repetition and location.
- **DS-02 Metric Specification** — LUFS, true peak, level gaps and trial counts as the evidence standard.
- **QA-18 Domain-Specific Smell Tests** — machine-gun effect, raised-cue loudness war and inverted ducking checks.
- **DS-06 Prioritization and Severity Guidance** — blocks / degrades / polish by effect on the player's decision.

## Related Prompts

- `domain-game-development/audio/audio_system_architecture.md` — buses, ducking rules and voice limits the fixes land in.
- `domain-game-development/design/design_hud_and_game_feel_review.md` — visual channels that back up audio cues.
- `domain-game-development/ai/ai_perception_stealth_fairness.md` — the AI-hearing side of the same footsteps.
