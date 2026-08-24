---
title: "Game Economy System Design"
category: game-development/economy
description: "Design game economies covering currency flows, pricing models, inflation control, drop rate tables, and F2P monetization balancing"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - game-design
  - economy
  - balancing
  - monetization
  - currency
  - f2p
updated: "2026-03-19"
related_prompts:
  - domain-game-development/design/design_player_progression.md
  - domain-game-development/design/design_core_loop_analysis.md
  - domain-game-development/design/design_mechanics_design.md
---

# Game Economy System Design

**Objective:** Design comprehensive game economy systems covering currency types and flows (sources/sinks), pricing models, inflation control mechanisms, loot drop rate tables, crafting cost curves, and F2P monetization balancing that avoids pay-to-win.

## When to Use

- Use when designing the economy for a new game (RPG, MMO, survival, strategy, F2P mobile)
- Use when an existing economy has inflation, deflation, or player frustration issues
- Use when adding monetization to a game and need to balance paid vs earned currency
- Don't use for player stat progression curves — use `design_player_progression.md` instead

## Instructions

1. **Define Economy Philosophy**
   - Monetization model: premium (buy-to-play), F2P with cosmetics, F2P with gameplay items, subscription
   - Economy type: closed (finite resources, zero-sum), open (generated on demand), hybrid
   - Player trading: no trading, limited trading, full player-driven market (auction house)
   - Currency count: single currency (simple) vs dual (soft/hard) vs multiple (specialized)
   - Target: how many hours of play to earn [key item X]? (anchors the whole economy)

2. **Design Currency System**
   - **Soft currency (earned through play):** Gold, coins, credits
     - Sources: quest rewards, enemy drops, selling loot, daily bonuses
     - Sinks: equipment purchase, consumables, crafting costs, repair bills, fast travel
   - **Hard currency (purchased or rare):** Gems, diamonds, premium tokens
     - Sources: real money purchase, rare achievements, season pass rewards
     - Sinks: cosmetics, convenience items (XP boosts, inventory expansion), battle pass
   - **Specialized currencies:** Crafting materials, reputation tokens, seasonal currency
   - Rule: soft currency should NEVER be convertible to hard currency at a fixed rate (inflation risk)

3. **Model Currency Flow (Sources and Sinks)**
   - Calculate expected income per hour at each game stage:
     - Early game (level 1-10): X gold/hour
     - Mid game (level 11-30): Y gold/hour
     - Late game (level 31-50): Z gold/hour
   - Calculate expected spending per hour at each stage
   - **Net flow should be slightly positive** (players feel rewarded) but controlled
   - Create a source/sink balance sheet and verify equilibrium
   - Model over 100 hours: does the player accumulate too much? Run out?

4. **Design Pricing and Vendor Systems**
   - Price scaling: items cost more as player progresses (matches income growth)
   - Use a "purchasing power" anchor: at any level, a "good item" costs ~2 hours of play
   - Vendor buy/sell ratio: vendors buy at 20-40% of sell price (gold sink)
   - Crafting cost: materials + gold fee (materials are the gate, gold is the sink)
   - Repair costs: 5-10% of item value per full durability restore (passive sink)
   - Avoid: items that are so expensive they feel unattainable, or so cheap they're meaningless

5. **Design Loot and Drop Rate Tables**
   - Rarity tiers with drop rates:
     - Common: 60-70%
     - Uncommon: 20-25%
     - Rare: 8-12%
     - Epic: 2-4%
     - Legendary: 0.5-1%
   - Pity system: guarantee minimum rarity after N attempts without a rare+ drop
   - Smart loot: weight drops toward player's class/build (reduces frustration)
   - Duplicate protection: reduce drop rate of already-owned items (collections)
   - Display rates: legally required in many regions for paid loot boxes (China, Belgium, Japan)

6. **Design Inflation Control Mechanisms**
   - **Gold sinks:** Repair costs, auction house fees, cosmetic unlocks, guild perks
   - **Item sinks:** Durability loss, enchantment failure, upgrade consume base item
   - **Time sinks:** Daily/weekly purchase limits, cooldowns on high-value rewards
   - **Seasonal resets:** Seasonal currencies expire, preventing hoarding
   - Monitor: if average gold per player grows >10% per month, add sinks

7. **Balance Monetization (F2P)**
   - Rule: paying players get **time** and **cosmetics**, never **exclusive power**
   - Battle pass: free tier earns gameplay items, premium tier adds cosmetics + convenience
   - Store pricing: anchor premium currency to real money ($0.01 = 1 gem, round prices)
   - Never sell: exclusive weapons, stats, levels, matchmaking advantages
   - Acceptable: XP boosts (cosmetic), inventory space, cosmetic skins, emotes, battle pass
   - Gacha/loot box: include pity timers, display rates, no duplicates in premium boxes

8. **CRITICAL: Validate Economy Balance**
   - Simulate 100-hour playthrough at minimum, average, and maximum income rates
   - Verify purchasing power stays within target (good item = ~2 hours of play) at all stages
   - Test with and without monetization spending — free players must feel viable
   - Check for exploits: is there any loop that generates infinite currency?
   - Verify inflation model: does currency accumulate dangerously over time?
   - Test edge cases: what if a player only farms? Only does quests? Only crafts?

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't assume every game needs F2P monetization — ask first
- Don't recommend pay-to-win mechanics even if asked — flag the business risk
- Don't design economies that require spreadsheet-level math from players to navigate
- Don't create so many currencies that players can't track them (max 3-4 active currencies)
- Don't set drop rates without considering session length (mobile ≠ PC pacing)

✅ **DO:**
- Model real play sessions when calculating income (30min mobile vs 4hr PC)
- Include pity/bad luck protection for all random reward systems
- Consider the emotional experience: players should feel rewarded, not manipulated
- Separate economy balance for PvE and PvP (PvE can be generous, PvP must be tight)
- Provide actual numbers, formulas, and spreadsheet data — not just "balanced"

## Expected Output

A game economy design document including:

- Economy philosophy and monetization model
- Currency system with source/sink mapping
- Income/spending curves by game stage
- Pricing table for key items
- Drop rate table with pity system
- Inflation control mechanisms
- Monetization boundaries (what's for sale, what's not)
- 100-hour simulation results

## Example Output

```markdown
## Economy Design — "Forgeheart" (Action RPG, F2P with Cosmetics)

### 1. Economy Philosophy

| Attribute | Value |
|-----------|-------|
| Monetization model | F2P with cosmetic-only premium store |
| Economy type | Open (currency generated by gameplay) |
| Player trading | No direct trading (prevents RMT abuse) |
| Currencies | 2: Gold (soft), Crystals (hard/premium) |
| Anchor | "Good weapon" = 2 hours of play at current level |

### 2. Currency System

#### Gold (Soft Currency)
| Source | Amount | Frequency |
|--------|--------|-----------|
| Enemy drops | 5-50 per enemy | Per kill |
| Quest rewards | 200-2,000 | Per quest |
| Dungeon completion | 500-5,000 | Per run (20 min) |
| Daily login bonus | 500 flat | Daily |
| Item vendoring | 20-40% of item value | Per sale |

| Sink | Cost | Frequency |
|------|------|-----------|
| Weapon purchase (vendor) | 1,000-50,000 | When upgrading |
| Armor purchase | 800-40,000 | When upgrading |
| Consumables (potions) | 50-200 each | Per dungeon run (5-10) |
| Equipment repair | 5% of item value | Per death or 20 durability uses |
| Crafting fee | 500-10,000 | Per craft |
| Fast travel | 100 per destination | Per use |
| Cosmetic recolors | 5,000-20,000 | One-time unlock |

#### Crystals (Hard Currency)
| Source | Amount |
|--------|--------|
| $0.99 purchase | 100 Crystals |
| $4.99 purchase | 550 Crystals (10% bonus) |
| $9.99 purchase | 1,200 Crystals (20% bonus) |
| Weekly challenge (free) | 50 Crystals |
| Season pass (free tier) | 200 Crystals over season |

| Sink | Cost |
|------|------|
| Cosmetic weapon skin | 300-800 Crystals |
| Character outfit | 500-1,500 Crystals |
| Emote | 200 Crystals |
| Battle pass (premium tier) | 950 Crystals per season |
| **NEVER:** weapons, armor, stats, XP boosts | — |

### 3. Income/Spending Curves

**Gold income per hour by level range:**

| Level Range | Gold/Hour | Key Purchases | Net Flow |
|-------------|-----------|--------------|----------|
| 1-5 | 800 | Starter gear (500-1,000 each) | +400/hr |
| 6-15 | 2,500 | Mid gear (2,000-5,000) | +1,000/hr |
| 16-25 | 5,000 | Good gear (5,000-15,000) | +1,500/hr |
| 26-35 | 8,000 | Rare gear (10,000-30,000) | +2,000/hr |
| 36-50 | 12,000 | Epic gear (20,000-50,000) | +2,500/hr |

**"Good weapon" at each tier:**
- Level 10: 3,000 gold = 1.2 hours ✅ (under 2hr target)
- Level 25: 12,000 gold = 2.4 hours ✅ (near target)
- Level 40: 30,000 gold = 2.5 hours ✅ (near target)
- Level 50 (endgame): 50,000 gold = 4.2 hours ⚠️ (intentionally longer for endgame)

### 4. Loot Drop Rate Table

| Rarity | Drop Rate | Pity Timer | Avg Drops/Hour |
|--------|-----------|------------|----------------|
| Common (white) | 65% | — | 39 |
| Uncommon (green) | 22% | — | 13.2 |
| Rare (blue) | 9% | Every 30 drops | 5.4 |
| Epic (purple) | 3.5% | Every 100 drops | 2.1 |
| Legendary (orange) | 0.5% | Every 500 drops | 0.3 |

**Pity system:** Tracks drops since last rare+ item. If threshold reached without a drop
of that rarity or higher, next drop is guaranteed at that rarity.

**Smart loot:** 70% of equipment drops match player's current class. 30% are random
(allows trading in future, keeps variety).

### 5. Inflation Control Model

**100-Hour Simulation (average player):**

| Hour | Gold Earned (cumulative) | Gold Spent (cumulative) | Net Gold |
|------|------------------------|------------------------|----------|
| 10 | 15,000 | 8,000 | 7,000 |
| 25 | 55,000 | 35,000 | 20,000 |
| 50 | 180,000 | 130,000 | 50,000 |
| 75 | 380,000 | 310,000 | 70,000 |
| 100 | 650,000 | 560,000 | 90,000 |

**Observation:** Net gold grows from 7K to 90K over 100 hours. This is intentional —
endgame players should feel wealthy. Controlled by:

- Endgame cosmetic gold sinks (recolors: 5K-20K each, dozens available)
- Crafting experimentation (crafting fee + material cost for each attempt)
- Alt-character gear (transfer gold, but not items)

**Inflation guardrails:**
- If avg net gold at 100hrs exceeds 120K: increase repair costs by 2%
- If avg net gold at 100hrs drops below 60K: increase quest rewards by 10%
- Seasonal content adds new gold sinks (seasonal cosmetics, guild hall upgrades)

### 6. Monetization Boundaries

| Category | For Sale? | Rationale |
|----------|-----------|-----------|
| Cosmetic skins | ✅ Yes (Crystals) | Core revenue, no gameplay impact |
| Emotes/titles | ✅ Yes (Crystals) | Social expression, no power |
| Battle pass | ✅ Yes (Crystals) | Seasonal engagement, free tier earns gameplay items |
| Inventory expansion | ✅ Yes (Crystals) | Convenience, one-time purchase, cap at +20 slots |
| Weapons/armor | ❌ Never | Pay-to-win, destroys competitive integrity |
| Stats/XP boosts | ❌ Never | Devalues time investment of free players |
| Loot boxes with power items | ❌ Never | Gambling + pay-to-win, regulatory risk |
| Crafting materials | ❌ Never | Would create pay-to-progress |

### 7. Tuning Parameters

| Parameter | Current | Increase Effect | Decrease Effect |
|-----------|---------|----------------|----------------|
| Enemy gold drop base | 5 per kill | Faster progression, inflation risk | Slower, grindier |
| Quest reward multiplier | 1.0× | More quest-focused play | More grind-focused play |
| Vendor buy-back ratio | 30% | Players vendor more (gold sink ↓) | Players vendor less (gold sink ↑) |
| Repair cost % | 5% of item value | Stronger gold sink | Weaker sink, more gold hoarding |
| Pity timer (epic) | 100 drops | Faster gear progression | Longer "droughts" |
| Crafting fee | 500-10K by tier | Slower crafting, more sink | Faster crafting, less sink |

**Live ops monitoring:**
- Dashboard: average gold per player at each level bracket (daily)
- Alert: if 90th percentile gold >3× median at any bracket
- Alert: if median time-to-good-weapon deviates >30% from 2-hour target
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines balanced, non-exploitative economy as goal
- **ST-02 (Structured Sequential Instructions):** Eight-step process from philosophy to validation
- **RT-02 (Multi-Dimensional Analysis):** Evaluates currencies, pricing, drops, inflation, and monetization separately
- **RT-05 (Evidence-Based Reasoning):** Requires simulation data, income curves, and actual numbers
- **DS-03 (Tool and Methodology Suggestions):** Provides formulas, tables, and monitoring strategies

## Related Prompts

- [Player Progression](../design/design_player_progression.md) — Progression drives demand; economy supplies it
- [Core Game Loop Analysis](../design/design_core_loop_analysis.md) — Economy rewards are core loop outputs
- Game Balance Data Model — Detailed stat math underlying economy
