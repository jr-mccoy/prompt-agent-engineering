---
name: game-feel-juice-pass
description: Implements and tunes the feedback layers that make a core action feel responsive (input buffering, coyote time, hitstop, trauma-based screenshake, flashes, knockback, particles, layered audio and haptics) as named, data-driven parameters with starting ranges, an intensity hierarchy, stacking caps and comfort toggles. Use when asked to "add juice", "make hits feel punchy", "implement screenshake or hitstop", or "the jump feels floaty".
metadata:
  tags:
    - game-dev
    - game-feel
    - juice
    - screenshake
    - hitstop
    - tuning
  updated: "2026-10-04"
---
# Game-Feel Juice Pass

A procedure for adding feedback to a game's core actions so they feel responsive, without
creating noise, nausea or frame-time spikes. Every effect becomes a named parameter with a
starting range, so the team tunes numbers instead of rewriting code.

## Purpose

"Juice" is usually added piecemeal: someone adds shake to the explosion, someone else adds
a flash to the hit, and the result is either flat or a wall of noise where a pickup shakes
the screen harder than a boss kill. This pass fixes input responsiveness first, then adds
feedback in a deliberate intensity hierarchy with caps, accessibility toggles and an A/B
check.

## When to Use This Skill

- A core verb (attack, jump, shoot, land, collect) works but feels weak, floaty or unresponsive
- Implementing screenshake, hitstop, hit flash, knockback or impact particles
- Juice exists but is inconsistent across events, or players report motion discomfort
- Preparing a vertical slice where feel will be judged

## When NOT to Use This Skill

- **Diagnosing what feels wrong, or reviewing HUD and menus.** Use the one-off review
  prompt `domain-game-development/design/design_hud_and_game_feel_review.md` first; this
  skill implements its findings.
- **Mixing and prioritising game audio.** See
  `domain-game-development/audio/audio_gameplay_readability_mix.md`.
- **The action is mechanically wrong** (damage numbers, enemy behaviour, level timing).
  Feedback cannot fix a design problem; see
  `domain-game-development/design/design_mechanics_design.md`.
- **Frame-rate or hitching problems.** Profile first with
  `domain-game-development/performance/performance_frame_budget_analysis.md`; juice on a
  hitching game feels worse.

## Prerequisites

- A build that runs at the target frame rate on the minimum-spec device
- A way to change parameters at runtime (inspector, debug menu or hot-reloaded data file)
- A way to record gameplay at full frame rate and step through it frame by frame

## Workflow

### Step 1: Inventory the events

Pick at most three core verbs. For each, list the events and what the player must learn
from each one.

| Event | Player must learn | Current feedback | Tier |
|---|---|---|---|
| Light hit lands | "I connected" | sound only | light |
| Heavy hit lands | "that was strong" | sound + small flash | medium |
| Enemy killed | "it's done; move on" | enemy disappears | heavy |
| Player takes damage | "I'm hurt; where from" | health bar changes | heavy |
| Jump / land | "I left / reached the ground" | none | light |
| Invalid action (no stamina) | "that did not work, and why" | none | light |

Assign each event a **tier** (light, medium, heavy, critical). Feedback strength must
follow tier order everywhere; this is the intensity hierarchy.

### Step 2: Fix the input layer before adding any effect

Juice cannot hide latency. Measure frames from button press to first visible response
(record at the target frame rate and step through).

| Parameter | What it does | Common starting point (tune by playtest) |
|---|---|---|
| Input-to-response | Frames until the first visual change | 0–2 frames for actions that must feel instant |
| Input buffer | Remembers a press slightly early (e.g. attack pressed before recovery ends) | ~80–150 ms |
| Coyote time | Allows a jump shortly after walking off a ledge | ~60–120 ms |
| Variable jump height | Releasing early cuts upward velocity | cut multiplier ~0.4–0.6 |
| Anticipation | Wind-up before an attack becomes active | keep short for player attacks; long wind-ups belong to enemy telegraphs |

These are widely used starting points, not standards. Record the chosen values in the
parameter file with the date and reason.

### Step 3: Build the feedback matrix

For each event, choose layers. Not every event gets every layer; light events should use
one or two.

| Layer | Light | Medium | Heavy | Critical |
|---|---|---|---|---|
| Hit flash (target) | 1–2 frames | 2–3 frames | 3–4 frames | 3–4 frames |
| Hitstop | none or ~30 ms | ~50–80 ms | ~80–130 ms | ~130–200 ms |
| Screenshake (trauma added) | none | 0.1–0.2 | 0.3–0.5 | 0.6–0.8 |
| Knockback | small | moderate | large | large + brief slow-motion (optional) |
| Particles | few, short-lived | moderate | burst + debris | burst + lingering |
| Audio | single transient | transient + body | transient + body + tail | full layer + music sting |
| Haptics | short, weak | short, medium | longer, strong | strongest |

The ranges are starting points for 60 fps action games; slower or more strategic games
need less. Express durations in seconds or milliseconds, never in frames, so feel does not
change with frame rate.

### Step 4: Implement each layer as data-driven code

All tunables live in one data file or asset (for example `feel_params.json` or a
ScriptableObject/Resource), keyed by tier.

**Trauma-based screenshake** (popularised by Squirrel Eiserloh's GDC talk on camera
math). Events add trauma; shake strength is trauma squared or cubed, so small additions
barely register and big ones are strong. Use smooth noise rather than random values so
the camera does not jitter.

```text
on_event(tier):  trauma = min(1.0, trauma + params[tier].trauma)

each frame (dt in unscaled seconds):
  trauma  = max(0.0, trauma - params.trauma_decay_per_sec * dt)
  shake   = trauma ^ params.shake_exponent          # 2 or 3
  t       = time_unscaled * params.noise_frequency
  offset.x = params.max_offset * shake * noise(seed_x, t)   # noise returns -1..1
  offset.y = params.max_offset * shake * noise(seed_y, t)
  angle    = params.max_angle  * shake * noise(seed_a, t)   # 2D: rotational shake reads well
  camera.apply_offset(offset * settings.shake_scale, angle * settings.shake_scale)
```

Apply the offset on top of the camera's follow position; never move the follow target
itself, or the shake accumulates.

**Hitstop.** Freeze only the participants (attacker and target), not the whole game, so
UI, audio and other entities keep running. Use a local time scale per entity.

```text
on_hit(attacker, target, tier):
  duration = params[tier].hitstop_sec
  attacker.local_time_scale = 0;  target.local_time_scale = 0
  schedule_unscaled(duration, restore: local_time_scale = 1)

# multi-hit attacks: scale hitstop down per successive hit within a window,
# e.g. duration * params.multi_hit_falloff ^ hits_in_window
```

If the engine only offers a global time scale (for example Unity's `Time.timeScale` or
Godot's `Engine.time_scale`; verify behaviour against current docs), drive UI animation
and the restore timer from unscaled time, or the game can freeze permanently.

**Hit flash.** Swap to a flash material or add an additive white tint for the tier's
duration; restore the exact previous material, not a default.

**Audio.** Layer transient, body and tail. Randomise pitch and volume slightly per play
(for example ±3–5% pitch) to avoid identical repeats, and set a voice limit per event so
rapid hits do not stack into a roar.

**Haptics.** Use the platform's rumble or haptics API with intensity and duration from
the same tier table. Platform APIs differ; verify against current docs.

### Step 5: Add caps and the hierarchy check

- Trauma clamps at 1.0; particle spawns per frame have a budget; identical sounds
  within ~50 ms are deduplicated.
- Frequent events get weaker feedback: a weapon that hits ten times a second uses the
  light tier, whatever its damage.
- Feedback never covers a telegraph: shake and particles must not hide an enemy wind-up
  or a projectile.
- **Hierarchy check:** list events by tier and play each in turn. If a lower-tier event
  feels as strong as a higher one, adjust before continuing.

### Step 6: Add comfort and accessibility options

Ship these with the pass, not later:

| Option | Default | Notes |
|---|---|---|
| Screenshake intensity | 100%, slider down to 0% (off) | Multiplies `settings.shake_scale` |
| Reduce flashing | off | Replaces full-screen flashes with edge or icon cues |
| Camera motion (kick, zoom punches) | on, toggle | Separate from shake |
| Haptics intensity | 100%, slider to 0% | |
| Visual cue for audio-only feedback | on where needed | e.g. off-screen damage direction indicator |

Keep full-screen flashing below three flashes in any one-second period, and avoid large
saturated red flashes (see the WCAG 2.3.1 flash thresholds and platform photosensitivity
guidance; verify against your platform holder's current requirements).

### Step 7: Tune with an A/B comparison

1. Bind a debug key that toggles all juice off and on, and one that cycles 0%, 100%, 150%.
2. Record the same 30-second sequence at each setting.
3. Step through the 100% clip frame by frame and check each event's timeline against the
   feedback matrix.
4. Treat team preference as weak evidence. Confirm in a playtest (see
   `playtest-telemetry-capture`, and the playtest protocol prompt) by watching whether
   players register hits and damage, not by asking whether it "feels good".

## Verification

- [ ] Input-to-response measured and within target for each core verb
- [ ] Every event in the inventory has a tier, and feedback strength follows tier order
- [ ] All effect values come from the parameter file; no magic numbers in gameplay code
- [ ] Durations are time-based; feel is identical at 30, 60 and 120 fps
- [ ] Shake at 0% removes all shake; reduce-flashing removes full-screen flashes
- [ ] Frame time on minimum spec unchanged within budget during the busiest combat scene
- [ ] A/B clips archived with the parameter file version

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Game stays frozen after a hit | Global time scale restored by a scaled timer | Restore with unscaled time, or use per-entity time scale |
| Multi-hit attacks stutter | Full hitstop on every hit | Apply falloff per hit within a window |
| Shake feels jittery or nauseating | Random per-frame offsets; linear strength | Use smooth noise; square or cube trauma; lower max offset; add rotation sparingly |
| Camera drifts after shaking | Offset applied to the follow target | Apply shake as a separate additive offset |
| Pickups feel bigger than kills | No hierarchy; effects added ad hoc | Re-tier events; run the hierarchy check |
| Feel changes on high-refresh displays | Frame-counted durations or decay | Convert to seconds; use delta time |
| Combat unreadable | Particles and shake hide telegraphs | Reduce layers on frequent events; keep telegraph areas clear |
| Frame spikes during big fights | Uncapped particles or audio voices | Spawn budget per frame; voice limits; pool particle systems |

## Safety & Constraints

**NEVER:**
- Ship screenshake or full-screen flashing without an off option
- Use juice to mask input latency or a mechanical problem
- Tune only on a high-end development machine

**ALWAYS:**
- Keep a one-key "all juice off" toggle in development builds
- Version the parameter file, so a tuning change can be reverted on its own

## Related Skills

- `playtest-telemetry-capture`: capture whether players actually register the feedback
- `godot-gdscript-patterns` / `unity-ecs-patterns`: engine-specific structure for the
  parameter resources and effect systems
- Prompt `domain-game-development/design/design_hud_and_game_feel_review.md`: the frame-by-frame review this pass implements
- Prompt `domain-game-development/audio/audio_gameplay_readability_mix.md`: audio priority
  and ducking so impact sounds read through the mix
