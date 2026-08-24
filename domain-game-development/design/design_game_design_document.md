---
title: "Game Design Document Generator"
category: game-development/design
description: "Generate a structured Game Design Document from a game concept covering core loop, audience, platforms, and milestones"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - OC-01
  - DS-01
difficulty: intermediate
tags:
  - game-design
  - gdd
  - documentation
  - planning
  - concept
updated: "2026-03-19"
---

# Game Design Document Generator

**Objective:** Generate a comprehensive, structured Game Design Document (GDD) from a game concept pitch, covering core gameplay loop, target audience, platform constraints, feature scope, art direction, and development milestones.

**When to Use:**
- Use when: Starting a new game project and need a structured design foundation
- Use when: Translating a loose concept or game jam idea into a production-ready document
- Use when: Aligning a team around shared vision, scope, and priorities
- Use when: Pitching a game concept to stakeholders or publishers
- Don't use when: You need a technical design document (architecture, engine specifics)
- Don't use when: You already have a GDD and need to analyze its core loop (use core loop analysis instead)

## Instructions

1. **Extract the Core Concept**
   - Identify the genre (primary and secondary, e.g., "roguelike deckbuilder")
   - Distill the unique hook — what makes this game different from existing titles in the genre?
   - Write a 2-sentence elevator pitch that a non-gamer could understand
   - Identify 3-5 reference titles and what specifically you are borrowing from each
   - Define the core fantasy — what does the player get to *feel* or *be*?

2. **Define Target Audience and Platform**
   - Identify primary audience segment (age range, gaming experience, play preferences)
   - Specify target platforms (PC, console, mobile, web) and their constraints
   - Define expected session length (quick sessions vs. long play)
   - Identify monetization model (premium, F2P, ad-supported, subscription)
   - Note accessibility requirements and content rating targets

3. **Design the Core Gameplay Loop**
   - Map the action-reward-expansion cycle:
     - **Action:** What does the player *do* moment-to-moment?
     - **Reward:** What does the player *receive* for doing it?
     - **Expansion:** How does the game *grow* or change over time?
   - Define the micro loop (second-to-second), meso loop (session-level), and macro loop (cross-session)
   - Identify the primary skill the player develops (mechanical, strategic, creative)
   - Describe what makes the loop intrinsically satisfying independent of external rewards

4. **Define Feature Scope with MoSCoW Prioritization**
   - **Must Have:** Features required for the game to function and be fun
   - **Should Have:** Features that significantly enhance the experience
   - **Could Have:** Features that are nice but not essential
   - **Won't Have (this version):** Features explicitly deferred — these are cut candidates
   - For each feature, estimate relative complexity (S/M/L/XL)
   - Tag features that have technical risk or unknowns

5. **Art and Audio Direction**
   - Define visual style (pixel art, hand-drawn, low-poly, photorealistic, stylized 3D)
   - Specify color palette direction and mood board references
   - Describe UI/UX style and information density
   - Define audio direction: music genre, sound design tone, voice acting (yes/no)
   - Identify asset pipeline needs (outsourced, in-house, procedural, AI-assisted)

6. **Technical Requirements**
   - Specify target engine or framework
   - Define minimum hardware/platform specs
   - Identify networking requirements (single-player, local co-op, online multiplayer)
   - List key technical risks (procedural generation, physics, large worlds, etc.)
   - Define data persistence needs (save system, cloud saves, cross-platform sync)

7. **Milestone and Scope Planning**
   - Define development phases: Prototype, Vertical Slice, Alpha, Beta, Launch
   - For each phase, list deliverables and success criteria
   - Identify the "proof of fun" milestone — when can you validate core loop enjoyment?
   - Estimate team size requirements per phase
   - Include cut plan: what gets dropped first if schedule slips?

8. **CRITICAL: Verify the GDD for internal consistency**
   - Does the scope match the stated team size and timeline?
   - Do the Must Have features actually support the core loop?
   - Are platform constraints reflected in feature design (e.g., no right-click on mobile)?
   - Does the monetization model align with the game design (e.g., no pay-to-win in competitive)?
   - Is the art direction achievable with the stated asset pipeline?
   - Are there features in "Must Have" that should be "Should Have"?

## False-Positive Prevention (MUST follow)

**DON'T:**
- Over-scope for team size — a 3-person indie team cannot ship an open-world MMO
- Assume AAA budget, timeline, or team unless explicitly stated
- Skip platform constraints — mobile and console have fundamentally different input models
- List features without prioritization — everything cannot be "Must Have"
- Ignore monetization implications on game design decisions
- Produce a GDD that reads like marketing copy — it must be actionable for developers

**DO:**
- Tailor scope to stated team size and experience level
- Include explicit cut candidates so the team knows what to drop first
- Flag technical risks that could derail the timeline
- Define "proof of fun" as the earliest possible validation point
- Consider accessibility from the start, not as an afterthought
- Keep sections modular so they can be updated independently

## Expected Output

A structured Game Design Document containing:
- One-page summary with elevator pitch, genre, platforms, and audience
- Core gameplay loop diagram with micro/meso/macro layers
- MoSCoW-prioritized feature list with complexity estimates
- Art and audio direction brief
- Technical requirements and risk assessment
- Phased milestone plan with cut strategy

### Output Format

```markdown
## Game Design Document: [Title]

### One-Page Summary
[Elevator pitch, genre, platforms, audience, monetization]

### Core Concept
[Hook, references, core fantasy]

### Core Gameplay Loop
[Micro/meso/macro loops, action-reward-expansion]

### Feature Scope (MoSCoW)
[Prioritized feature list with complexity]

### Art & Audio Direction
[Visual style, audio direction, asset pipeline]

### Technical Requirements
[Engine, platforms, networking, risks]

### Milestones
[Phased development plan with cut strategy]
```

## Example Output

```markdown
## Game Design Document: Hexbound

### One-Page Summary

| Field | Detail |
|-------|--------|
| **Title** | Hexbound |
| **Genre** | Roguelike Deckbuilder with Hex-Grid Tactics |
| **Elevator Pitch** | Build a deck of elemental spells, then deploy them on a hex grid where positioning and terrain matter as much as card synergies. Die, learn, and rebuild stronger. |
| **Platforms** | PC (Steam), Nintendo Switch |
| **Target Audience** | Strategy gamers aged 16-35 who enjoy Slay the Spire, Into the Breach, and Tactical RPGs |
| **Session Length** | 30-60 minute runs |
| **Monetization** | Premium ($19.99), no microtransactions |
| **Team Size** | 4 people (1 designer/producer, 1 programmer, 1 artist, 1 audio/QA) |
| **Target Launch** | 18 months from prototype start |
| **Content Rating** | ESRB E10+ / PEGI 7 |

### Core Concept

**Unique Hook:** Unlike pure deckbuilders where cards resolve instantly, Hexbound
places your spells on a tactical hex grid. A fireball isn't just "deal 8 damage" — it
hits a hex and splashes to adjacent tiles. Positioning your mage, managing terrain
effects, and exploiting elemental combos (water + lightning = chain) create emergent
tactical depth that pure deckbuilders lack.

**Core Fantasy:** You are an elemental mage who grows from a novice with 3 basic
spells into a master who chains devastating combos across the battlefield.

**Reference Titles:**
| Game | What We Borrow |
|------|----------------|
| Slay the Spire | Roguelike run structure, card drafting, relic system |
| Into the Breach | Grid-based tactics, telegraphed enemy moves, spatial puzzles |
| Pokémon TCG | Elemental type interactions and combo potential |
| Hades | Meta-progression between runs, narrative threading |
| Dominion | Deck thinning and engine-building as core strategy |

### Core Gameplay Loop

**Micro Loop (second-to-second):**
1. Survey the hex grid — enemies have telegraphed moves showing where they'll attack
2. Play a spell card from your hand onto a target hex
3. See immediate feedback — damage numbers, elemental effects, terrain changes
4. Reposition your mage to avoid telegraphed attacks
5. End turn, draw new cards, enemies execute their telegraphed moves

**Meso Loop (per encounter, 5-10 minutes):**
1. Enter a hex-grid battlefield with a new enemy configuration
2. Spend 3-6 turns defeating all enemies using hand management and positioning
3. Receive rewards: choose 1 of 3 new spell cards, gain gold, or find a relic
4. Choose next node on the branching run map (elite, shop, event, rest)

**Macro Loop (per run, 30-60 minutes):**
1. Start a new run with a starter deck of 8 basic spells
2. Progress through 3 acts, each with a boss encounter
3. Build your deck through drafting, shops, and events
4. Die or defeat the final boss
5. Unlock new starter spells and relics for future runs via meta-progression

**Primary Skill Developed:** Spatial reasoning — reading the board state and
planning card placement for maximum elemental chain reactions.

**Intrinsic Satisfaction:** The "aha" moment when a player realizes they can
chain water → freeze → shatter across 4 hexes to clear the board. The
emergent combo discovery is the core joy.

### Feature Scope (MoSCoW)

#### Must Have (MVP)
| Feature | Complexity | Notes |
|---------|------------|-------|
| Hex-grid combat system (7x9 grid) | XL | Core mechanic — prototype first |
| 40 unique spell cards across 4 elements | L | Fire, Water, Earth, Air |
| Elemental interaction system (6 combos) | L | Water+Fire=Steam, Water+Lightning=Chain, etc. |
| 3-act run structure with branching map | M | 15 nodes per act |
| 8 unique enemy types with telegraphed AI | L | 2 per element |
| 3 boss encounters (1 per act) | L | Unique mechanics per boss |
| Deck management (add, remove, upgrade) | M | Core deckbuilder system |
| 10 relics that modify rules | M | Passive bonuses |
| Save and resume mid-run | S | Required for Switch |
| Basic meta-progression (unlock 12 cards) | M | Reason to replay after death |

#### Should Have
| Feature | Complexity | Notes |
|---------|------------|-------|
| Terrain types (lava, ice, poison, water) | M | Adds tactical depth |
| 20 additional spell cards (60 total) | M | More build variety |
| 5 additional relics (15 total) | S | Combo potential |
| Event nodes with narrative choices | M | Non-combat variety |
| Daily challenge mode | S | Community engagement |
| Stats and run history tracking | S | Player analytics |
| Accessibility options (colorblind, text size) | M | Broader audience |

#### Could Have
| Feature | Complexity | Notes |
|---------|------------|-------|
| Ascension/difficulty modifiers (10 levels) | M | Endgame content |
| Achievement system | S | Completionist appeal |
| Animated card art | L | Polish item |
| Procedural encounter generation | L | Infinite variety |
| Leaderboards | M | Community feature |

#### Won't Have (This Version)
| Feature | Rationale |
|---------|-----------|
| Multiplayer (PvP or co-op) | Scope explosion for 4-person team |
| Full voice acting | Budget constraint |
| Level editor | Post-launch consideration |
| Mobile port | Input model requires redesign |
| Story campaign with cutscenes | Roguelike structure tells story through gameplay |

### Art & Audio Direction

**Visual Style:** Hand-drawn 2D with watercolor textures. Spell effects use
particle systems with painterly splashes. Think "Darkest Dungeon meets
Slay the Spire" in terms of fidelity, but with a brighter, more vibrant
color palette.

**Color Palette:**
- Fire: Warm oranges, deep reds (#E85D26, #B22222)
- Water: Teals, deep blues (#1E90FF, #008B8B)
- Earth: Rich browns, forest greens (#8B4513, #228B22)
- Air: Light purples, silver whites (#9370DB, #C0C0C0)
- UI: Dark slate background (#2C3E50) with gold accents (#FFD700)

**UI/UX Style:** Clean, card-game inspired. Hand of cards along bottom,
hex grid center screen, enemy intent icons above enemies (borrowed
from Slay the Spire's clarity model). Minimal HUD — health, mana,
deck/discard counts.

**Audio Direction:**
- Music: Orchestral-light with elemental themes. Each element has a
  leitmotif that layers in as you play cards of that element.
- SFX: Satisfying, punchy spell impacts. Elemental combos get unique
  "combo trigger" sounds that create audio feedback for good play.
- Voice: No voice acting. Text-based narrative.

**Asset Pipeline:**
- Character and card art: Outsourced to freelance illustrator
- UI and hex tiles: In-house (artist on team)
- VFX: Particle systems built in-engine
- Music: Commissioned from freelance composer (5 tracks)
- SFX: Licensed library + custom recording

### Technical Requirements

| Requirement | Specification |
|-------------|---------------|
| **Engine** | Unity 2022 LTS (C#) |
| **Minimum PC Spec** | Intel i5-6400, 4GB RAM, integrated graphics |
| **Switch Target** | 30fps docked, 30fps handheld |
| **Networking** | None (single-player only) |
| **Save System** | JSON serialization, local saves, Steam Cloud |
| **Build Size Target** | < 2GB |
| **Resolution Support** | 1080p to 4K (PC), 720p/1080p (Switch) |

**Technical Risks:**
| Risk | Severity | Mitigation |
|------|----------|------------|
| Hex-grid pathfinding performance on Switch | Medium | Pre-compute adjacency tables, limit grid size |
| Elemental combo system complexity | Medium | Prototype interaction matrix early, keep to 6 combos |
| Save/resume state serialization | Low | Use established save patterns, test early |
| Card balance across 60+ cards | High | Build spreadsheet sim, plan 3 balance passes |

### Milestones

#### Phase 1: Prototype (Months 1-3)
**Goal:** Prove the hex-grid deckbuilder is fun.

| Deliverable | Success Criteria |
|-------------|-----------------|
| Hex-grid combat with 5 placeholder cards | Player can win and lose a single fight |
| Elemental combo system (3 combos) | Combos feel satisfying and emergent |
| Basic enemy AI with telegraphing | Player can read and react to threats |
| **Proof of Fun playtest** | 5/8 playtesters say "I want to play again" |

#### Phase 2: Vertical Slice (Months 4-7)
**Goal:** One complete act that represents final quality.

| Deliverable | Success Criteria |
|-------------|-----------------|
| Act 1 complete (15 nodes, 1 boss) | 30-minute play session feels complete |
| 20 spell cards with final art | Cards are visually clear and readable |
| Deck management (add/remove/upgrade) | Strategic choices feel meaningful |
| 5 relics | Build diversity increases |
| Music and SFX for Act 1 | Audio enhances, doesn't distract |

#### Phase 3: Alpha (Months 8-12)
**Goal:** All 3 acts playable, all Must Have features complete.

| Deliverable | Success Criteria |
|-------------|-----------------|
| Acts 2 and 3 with bosses | Full 60-minute run is possible |
| 40 spell cards | Multiple viable build archetypes |
| Meta-progression system | Players feel motivated after death |
| Save/resume system | Switch certification ready |
| Balance pass #1 | No dominant strategy; all elements viable |

#### Phase 4: Beta (Months 13-15)
**Goal:** Content complete, polish and balance.

| Deliverable | Success Criteria |
|-------------|-----------------|
| Should Have features (terrain, events) | Depth increased without scope creep |
| Balance pass #2 | Community beta feedback incorporated |
| Accessibility options | Colorblind mode, remappable controls |
| Performance optimization | Stable 30fps on Switch |
| Localization (EFIGS) | 5 languages ready |

#### Phase 5: Launch (Months 16-18)
**Goal:** Ship on Steam and Switch.

| Deliverable | Success Criteria |
|-------------|-----------------|
| Platform certification (Switch) | Passes Nintendo lotcheck |
| Steam page, trailer, press kit | Marketing materials ready |
| Day-1 patch plan | Known issues documented |
| Balance pass #3 | Final tuning |
| Launch | Reviews average 75+ on Metacritic |

**Cut Plan (if schedule slips):**
1. First cut: Daily challenge mode and leaderboards
2. Second cut: Terrain types (playable without them)
3. Third cut: Switch port (launch PC-only, port later)
4. Emergency cut: Reduce to 2 acts, ship Act 3 as free update
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a specific, actionable objective for GDD generation
- **ST-02 (Structured Sequential Instructions):** 8 numbered steps guide the user through the full document
- **ST-03 (Explicit Scope Boundaries):** MoSCoW prioritization and "Won't Have" section define scope limits
- **OC-01 (Structured Output Format):** Specifies exact sections and table formats for the GDD
- **DS-01 (Decision Framework):** MoSCoW framework for feature prioritization and cut planning

## Related Prompts

- [design_core_loop_analysis.md](design_core_loop_analysis.md) - Deep-dive analysis of core gameplay loops
- [design_mechanics_design.md](design_mechanics_design.md) - Detailed mechanic design and prototyping
- [design_player_progression.md](design_player_progression.md) - Progression system design with mathematical models
