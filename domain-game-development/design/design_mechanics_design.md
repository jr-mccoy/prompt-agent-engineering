---
title: "Game Mechanics Design & Prototyping"
category: game-development/design
description: "Design game mechanics from a concept brief with interaction rules, feedback systems, and emergent behavior analysis"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-01
difficulty: advanced
tags:
  - game-design
  - mechanics
  - prototyping
  - systems-design
  - emergence
updated: "2026-03-19"
---

## Game Mechanics Design & Prototyping

**Objective:** Design detailed game mechanics from a concept brief, defining interaction rules, player feedback loops, input/output systems, emergent behavior potential, and paper-prototype specifications.

**When to Use:**
- Designing new game mechanics from scratch based on a concept or game design document
- Iterating on existing mechanics that don't "feel right" or fail playtesting
- Analyzing why a mechanic is or isn't fun and identifying specific improvement levers
- Creating paper-prototype specifications before committing to implementation

**Instructions:**

1. **Decompose the mechanic into atomic elements:** Break the mechanic down into its fundamental components:
   - **Player Inputs:** What actions can the player take? (button presses, holds, gestures, analog stick directions, timing windows)
   - **Game Rules:** What constraints govern the mechanic? (cooldowns, resource costs, spatial requirements, state prerequisites)
   - **Outputs/Feedback:** What does the player see, hear, and feel in response? (animations, particles, sound effects, camera behavior, UI changes)
   - **State Changes:** What changes in the game world as a result? (position, health, inventory, environment, NPC state, progression)

2. **Define the "feel" and feedback (juice):** For each phase of the mechanic (anticipation, action, result), specify:
   - **Visual feedback:** Screen shake intensity/duration, particle effects, flash frames, animation curves (ease-in, ease-out, overshoot)
   - **Audio feedback:** Sound effect timing, pitch variation, layering (impact + whoosh + environmental reaction)
   - **Haptic feedback:** Controller rumble patterns (intensity, duration, motor selection for asymmetric rumble)
   - **Animation timing:** Startup frames, active frames, recovery frames, cancel windows
   - **Camera behavior:** Zoom, shake, slow-motion (hitstop), tracking adjustments

3. **Map interaction with other game systems:** Document how this mechanic connects to:
   - **Progression system:** Does mastery unlock new variations? Do stats modify parameters?
   - **Combat system:** Does this mechanic deal damage, provide defense, enable combos?
   - **Economy system:** Does it consume or generate resources?
   - **Traversal system:** Does it enable new movement options or shortcuts?
   - **Social/multiplayer system:** How does it interact with other players (cooperative synergies, competitive counters)?
   - **Narrative system:** Does it reinforce themes or character identity?

4. **Analyze emergence potential:** Identify behaviors that can arise from rule interactions that were not explicitly designed:
   - **Intended emergent behaviors:** Combinations the designer hopes players discover (skill expression)
   - **Unintended but positive emergence:** Surprising creative uses that add depth
   - **Degenerate strategies:** Exploits or optimal strategies that bypass intended engagement
   - **Edge cases:** What happens at extreme parameter values or unusual combinations?

5. **Create paper-prototype rules:** Write simplified rules that can be tested without code:
   - Use dice, cards, tokens, or grid paper to simulate the mechanic
   - Define turn structure or timing representation
   - Specify win/loss conditions for the test scenario
   - List what questions the paper prototype should answer

6. **Define tuning parameters:** Create a table of every numeric value that affects the mechanic:
   - **Parameter name and description**
   - **Initial value and valid range**
   - **Sensitivity:** How much does changing this value affect feel? (Low/Medium/High)
   - **Method:** Should this be tuned by calculation, playtesting, or A/B testing?

7. **CRITICAL verification — confirm all of the following before finalizing:**
   - **Player agency:** Verify the mechanic gives players meaningful choices, not just execution tests. If the optimal action is always the same regardless of context, the mechanic lacks agency.
   - **Proportional feedback:** Verify that feedback intensity is proportional to the significance of the action. A minor attack should not produce the same screen shake as a super move.
   - **Degenerate strategy check:** Verify there is no single dominant strategy that makes all other options irrelevant. If one exists, identify counterplay or balancing levers.
   - **Platform fit:** Verify the input requirements are achievable on the target platform (a mechanic requiring 6 simultaneous buttons does not work on mobile).

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT over-engineer simple mechanics — sometimes a single button press with good juice is the right design. Not every mechanic needs 12 interacting subsystems.
- ❌ Do NOT ignore feel/juice — a mechanically sound system with no feedback will feel terrible in practice. "Fun" lives in the feedback, not the rules.
- ❌ Do NOT design mechanics in isolation — every mechanic exists within a larger game. A perfect mechanic that conflicts with the game's pacing, tone, or other systems is a bad mechanic.
- ❌ Do NOT confuse complexity with depth — adding more rules does not make a mechanic deeper. Depth comes from meaningful decisions emerging from simple rules.
- ❌ Do NOT assume digital-only — if a mechanic cannot be approximated on paper, it may be too opaque for players to understand.
- ✅ DO identify which parameters need playtesting vs. calculation — physics constants can be calculated, but "fun" values must be playtested.
- ✅ DO consider platform input constraints — touch vs. controller vs. keyboard/mouse fundamentally change what mechanics are viable.
- ✅ DO test for degenerate strategies — identify the optimal play pattern and ask: "Is the optimal strategy also the most fun strategy?" If not, redesign.
- ✅ DO specify cancel windows and state transitions — players will try to interrupt every action. Define what happens when they do.
- ✅ DO reference comparable mechanics in shipped games — grounding in precedent helps communicate intent to the team.

**Expected Output:** A comprehensive mechanic design document containing:

1. Mechanic decomposition (inputs, rules, outputs, state changes)
2. Feedback specification with timing and intensity values
3. System interaction map showing connections to other game systems
4. Emergence analysis with intended, unintended, and degenerate possibilities
5. Paper-prototype rules ready for tabletop testing
6. Tuning parameter table with initial values and sensitivity ratings
7. Verification checklist results confirming agency, feedback proportionality, and balance

**Example Output:**

```markdown
## Mechanic Design Document: Grappling Hook

### 1. Concept Summary

**Game:** 3D action-platformer (single-player, controller primary, PC/console)
**Mechanic:** Physics-based grappling hook for traversal and combat
**Design Pillars:** Momentum mastery, spatial creativity, risk/reward traversal
**Reference Games:** Titanfall 2 (grapple pilot), Halo Infinite (grappleshot), Sekiro (grappling hook)

---

### 2. Mechanic Decomposition

#### 2.1 Player Inputs

| Input | Action | Timing |
|-------|--------|--------|
| LT (hold) | Aim mode — show grapple reticle, slow movement by 30% | Instant activation |
| RT (press) | Fire grapple — launch hook toward reticle target | 0.1s startup |
| RT (hold) | Reel in — pull player toward anchor point | Continuous while held |
| RT (release) | Detach — release grapple and inherit momentum | Instant |
| A (press during reel) | Launch — detach + upward boost (adds vertical velocity) | 0.05s window after release |
| B (press during reel) | Slam — detach + downward acceleration for ground pound | 0.1s startup |

#### 2.2 Game Rules

- **Range:** Maximum grapple distance = 40 meters. Reticle turns green when a valid anchor is in range.
- **Valid Anchors:** Designated grapple points (rings), any ledge/edge, enemies (special interaction), physics objects (pull toward player instead).
- **Cooldown:** 2 seconds after detach. Cooldown resets immediately on landing.
- **Momentum Preservation:** Player velocity at detach = reel-in velocity + player's pre-grapple velocity (capped at terminal velocity of 30 m/s).
- **Swing Physics:** If the player moves perpendicular to the grapple line, the hook acts as a pendulum pivot (swing arc). Gravity applies normally.
- **Stamina Cost:** None for traversal. Combat grapple (pulling enemies) costs 1 stamina bar segment.

#### 2.3 Outputs and Feedback

| Phase | Visual | Audio | Haptic |
|-------|--------|-------|--------|
| Aim | Reticle appears, line preview shows trajectory arc | Subtle UI hum (pitch rises near valid target) | Light sustained rumble (left motor) |
| Fire | Hook projectile with trail VFX, sparks on anchor contact | "Thwip" launch + metallic "clang" on attach | Sharp pulse (right motor, 50ms) |
| Reel-in | Speed lines, FOV widens 5-15% based on speed, wind particles | Rising wind whoosh, cable tension creak | Escalating rumble (both motors) |
| Detach/Launch | Momentum trail, brief slow-motion (0.1s), FOV snap back | Satisfying "snap" release + air rush | Strong pulse then fade (100ms) |
| Slam (ground pound) | Downward speed lines, impact crater VFX, screen shake | Descending whoosh + bass impact thud | Heavy slam pulse (200ms, full intensity) |

#### 2.4 State Changes

- **Player position:** Moves along grapple line or swing arc
- **Player velocity:** Set to reel-in direction + inherited momentum on detach
- **Enemy state (combat grapple):** Stunned for 1.5s, pulled toward player if lighter; player pulled toward enemy if heavier
- **Environment:** Physics objects pulled toward player; destructible anchor points break after 3 uses
- **Cooldown timer:** Starts on detach (2s), resets on landing

---

### 3. System Interactions

#### 3.1 Traversal System
- Grapple enables access to verticality that jumping alone cannot reach
- Momentum chains: grapple → swing → detach → wall-run → grapple creates flow state
- Shortcuts: skilled players can skip platforming sections via creative grapple angles

#### 3.2 Combat System
- **Engage:** Grapple to close distance on ranged enemies (risk: flying into danger)
- **Displace:** Pull lighter enemies out of cover or off ledges
- **Combo starter:** Grapple-launch into aerial attack (1.5x damage multiplier while airborne from grapple)
- **Escape:** Grapple to high anchor point to retreat and heal

#### 3.3 Progression System
- **Base grapple:** Unlocked in Act 1 (reel-in only, no swing)
- **Swing upgrade (Act 2):** Enables pendulum physics, opens swing-based traversal puzzles
- **Combat grapple (Act 2):** Enables pulling/stunning enemies
- **Dual hook (Act 3):** Two simultaneous grapple points, enables slingshotting
- Skill tree modifiers: +range, -cooldown, momentum damage bonus, electric grapple (stun AoE)

#### 3.4 Economy System
- Grapple hook cosmetics purchasable (cable color, hook model, trail VFX)
- No gameplay-affecting economy interaction (traversal is core, not purchasable advantage)

---

### 4. Emergence Analysis

#### 4.1 Intended Emergent Behaviors
- **Momentum chaining:** Skilled players chain grapple → swing → detach → grapple to maintain high speed across large spaces
- **Combat mobility:** Using grapple mid-combat to reposition creates dynamic, vertical fights
- **Shortcut discovery:** Players find creative grapple paths that skip intended routes

#### 4.2 Unintended but Positive Emergence
- **Pendulum sniping:** Swinging on a grapple point while shooting (high skill expression)
- **Enemy juggling:** Grapple-pull an enemy, launch them upward, aerial combo
- **Physics object surfing:** Grapple a physics object, stand on it, pull it forward for improvised transport

#### 4.3 Degenerate Strategies (Must Address)

| Strategy | Risk | Mitigation |
|----------|------|------------|
| Perma-grapple (never touch ground) | Trivializes ground hazards and melee enemies | 2s cooldown between grapples; aerial enemies that punish sustained air time |
| Boss cheese (grapple to safe spot, ranged attack) | Bypasses intended boss patterns | Bosses destroy nearby grapple anchors periodically; arena grapple points on timers |
| Speed-skip (grapple past all content) | Players miss narrative and progression content | Gate critical grapple points behind story triggers; momentum walls in key corridors |

#### 4.4 Edge Cases
- Grapple target destroyed mid-reel: Player inherits current velocity, enters freefall, no cooldown penalty
- Two valid targets equidistant: Prioritize target closest to reticle center
- Grapple into ceiling at high speed: Velocity clamped, player slides along surface
- Grapple while already grappling: First hook detaches, new hook fires (intentional — enables hook-switching)

---

### 5. Paper-Prototype Rules

**Materials:** Grid paper (1 square = 2 meters), 6-sided die, player token, enemy tokens, pencil

**Setup:**
- Draw a side-view level on grid paper with platforms, gaps, and grapple point markers (circled dots)
- Place player token at start position
- Place 3 enemy tokens at designated positions

**Turn Structure:**
1. **Move phase:** Move player token up to 3 squares in any direction (walking)
2. **Grapple phase (optional):** If a grapple point is within 20 squares line-of-sight:
   - Draw a line from player to grapple point
   - Move player to any square along that line or within 3 squares of the grapple point (simulating swing arc)
   - Roll 1d6: on 5-6, gain "momentum" token (allows +5 squares movement next turn)
3. **Action phase:** Attack adjacent enemies (roll 1d6, hit on 3+) or interact with objects
4. **Enemy phase:** Each enemy moves 2 squares toward player and attacks if adjacent

**Test Questions:**
- Do players choose between safe/slow paths and risky/fast grapple paths?
- Does momentum chaining feel rewarding (accumulating momentum tokens)?
- Are grapple points spaced so players must plan 2-3 moves ahead?
- Do enemies create tension around grapple decisions (do I grapple toward enemies or away)?

---

### 6. Tuning Parameters

| Parameter | Initial Value | Range | Sensitivity | Tuning Method |
|-----------|--------------|-------|-------------|---------------|
| Max grapple range | 40m | 20-60m | High | Playtesting (level design dependent) |
| Reel-in speed | 25 m/s | 15-40 m/s | High | Playtesting (must feel fast but controllable) |
| Cooldown duration | 2.0s | 0.5-4.0s | High | Playtesting (flow state vs. trivializing ground) |
| Momentum preservation | 85% | 50-100% | Medium | Playtesting (too high = uncontrollable, too low = unsatisfying) |
| Terminal velocity cap | 30 m/s | 20-50 m/s | Medium | Calculation (based on level geometry) |
| FOV increase at max speed | +15 degrees | +5 to +25 | Medium | Playtesting (motion sickness threshold) |
| Screen shake on slam | 0.3s, 8px | 0.1-0.5s, 2-15px | Low | Playtesting (subjective feel) |
| Aim slowdown | 30% speed reduction | 0-60% | Low | Playtesting (accessibility consideration) |
| Combat stun duration | 1.5s | 0.5-3.0s | High | Playtesting (combo viability) |
| Launch vertical boost | 8 m/s upward | 3-15 m/s | Medium | Calculation (must reach X platform height) |
| Swing gravity scale | 0.8 (slightly floaty) | 0.5-1.2 | High | Playtesting (pendulum arc feel) |
| Hook projectile speed | 80 m/s | 40-120 m/s | Medium | Playtesting (must feel instant but readable) |

---

### 7. Verification Checklist

| Check | Status | Notes |
|-------|--------|-------|
| Player agency: meaningful choices exist | PASS | Player chooses when to grapple, where to aim, when to detach, whether to swing or reel — each choice has different outcomes |
| Feedback proportionality | PASS | Casual swing = light rumble + wind; slam ground pound = heavy shake + impact VFX + bass thud; escalation matches action significance |
| No dominant degenerate strategy | PASS (with mitigations) | Perma-grapple addressed via cooldown + aerial threats; boss cheese addressed via destructible anchors |
| Platform fit | PASS | Primary input is aim + trigger (works on controller); aim assist for analog sticks; touch adaptation requires auto-aim lock-on |
| Complements other systems | PASS | Enhances traversal, combat, and progression without replacing any of them |
| Paper prototype testable | PASS | Grid-based prototype captures core decision-making loop |

---

### 8. Comparable Shipped Mechanics

| Game | Mechanic | What to Learn |
|------|----------|---------------|
| Titanfall 2 | Grapple pilot ability | Momentum physics, swing arc feel, cooldown pacing |
| Halo Infinite | Grappleshot | Combat integration, enemy pull, limited charges |
| Sekiro | Grappling hook | Instant traversal (no swing), designated points only |
| Bionic Commando (2009) | Bionic arm | Full swing physics, momentum mastery skill ceiling |
| Just Cause 3 | Grapple + parachute | Creative traversal combos, emergence from simple tools |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with precise goal: design mechanics from concept brief to paper-prototype specification
- ST-02 (Structured Sequential Instructions) - Seven numbered steps with logical progression from decomposition through verification
- RT-02 (Multi-Dimensional Analysis Framework) - Analyzes mechanic across inputs, rules, outputs, system interactions, and emergence
- CM-01 (Contextual Adaptation) - Framework adapts to any mechanic type (traversal, combat, puzzle, social) while maintaining structure
- DS-01 (Framework Application) - Applies established game design frameworks (MDA, feedback loops, emergence theory)

**Related Prompts:**
- `design_player_progression.md` - Design progression systems that modify mechanic parameters over time
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md` - Identify design patterns in mechanic implementation code
- `domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md` - Plan implementation sprints for mechanic development
