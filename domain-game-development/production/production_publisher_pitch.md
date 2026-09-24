---
title: "Game Publisher and Investor Pitch"
category: game-development/production
description: "Build the pitch a game publisher or games investor actually evaluates: a hook, a vertical slice that proves the core loop at target quality, comparable titles with stated estimation methods, a line-item budget with contingency, milestone payments, recoupment scenarios, and the objections they will raise — distinct from the internal game design document and from a general company fundraising deck."
techniques:
  - ST-46
  - NE-23
  - NE-11
  - QA-26
difficulty: advanced
tags:
  - game-pitch
  - publishing
  - vertical-slice
  - game-budget
  - comparable-titles
  - fundraising
  - indie-game-funding
  - publishers-said-no
  - investor-meeting
updated: "2026-09-24"
related_prompts:
  - domain-game-development/design/design_game_design_document.md
  - domain-game-development/testing/testing_playtest_protocol_synthesis.md
  - domain-game-development/design/design_core_loop_analysis.md
---

# Game Publisher and Investor Pitch

**Objective:** Produce a pitch in which every claim a publisher cares about — the
game is fun, the team can finish it, it can sell, the money is enough — leads with
the assertion and is followed by evidence they can check.

**When to Use:**
- Preparing to approach publishers, platform funds, or games-focused investors.
- A publisher asked for "a deck, a budget and the build" and the team has a GDD.
- A previous round of pitches got polite passes and the team wants to know why.

**When NOT to use:**
- The internal design reference — `design_game_design_document.md`. The GDD
  describes the game to the team; the pitch is distinct because it argues a
  business case to someone taking financial risk.
- An equity raise for a company whose product is not a specific game — use the
  general fundraising and presentation prompts elsewhere in the repository.
- Deal terms and contract review — `domain-legal/contracts-transactional/`.

## Inputs

1. **Game**: genre, platform, price, one-line hook, target audience.
2. **Build**: what the vertical slice contains and how long it plays.
3. **Evidence**: playtest results, wishlists, demo metrics, community size.
4. **Team**: roles, shipped titles, who is full-time.
5. **Budget inputs**: headcount, loaded monthly cost, schedule, outsourcing, QA, tools.
6. **What you are asking for**: amount, and what the partner gets (recoupment,
   revenue share, services such as porting, marketing, QA).
7. **Target partner**: their portfolio and what they have funded recently.

## Method

1. **Write the assertions first (ST-46).** Five headlines, one per question the
   partner asks: *Is it fun? Can they finish? Will it sell? Is the budget real?
   What do we get?* Each section opens with its assertion.
2. **Define the vertical slice as proof, not preview.** It must show the core loop
   end to end at target quality for 10–20 minutes; list what is placeholder.
   Attach playtest evidence, not adjectives.
3. **Build comps with a stated method.** Three to five titles: same genre, price
   band, platform, release within ~5 years. State how sales were estimated (e.g.
   review count × multiplier range) and mark every figure `[verify]`. Include at
   least one comp that underperformed.
4. **Build the budget (NE-11).** `headcount × loaded monthly cost × months` + tools
   + outsourcing + QA/certification; contingency 10–20% as its own line.
5. **Schedule milestone payments** tied to verifiable deliverables; they must sum
   to the ask.
6. **Model recoupment (NE-11).** `units to recoup = ask ÷ net revenue per unit`;
   low/base/high scenarios anchored to the comps, with the partner's return in each.
7. **Pre-empt objections (NE-23).** The three hardest questions this partner will
   ask, each with the evidence that answers it — or an honest "not yet, here is
   how we will know by milestone 2".
8. **Run the first-invented-fact test (QA-26).** Read the pitch as the partner;
   the first number you would have to take on trust is the next thing to evidence.

## Output Format

```
## Hook            — one sentence + the player fantasy
## Proof           — vertical slice contents, playtest evidence
## Market          — comps table with method and [verify] markers
## Team            — who, shipped what, full-time or not
## Budget          — line items, contingency, total = ask
## Milestones      — deliverable | month | payment; sum = ask
## Recoupment      — low/base/high units, net, partner return
## Objections      — objection | evidence | status
## Open items      — first invented fact and how it will be evidenced
```

## Verification

- [ ] Every section opens with an assertion, followed by evidence.
- [ ] Budget line items sum to the total; milestones sum to the ask.
- [ ] Every comp sales figure states its method and carries `[verify]`.
- [ ] At least one comp underperformed; the base case is not set by the best comp.
- [ ] Recoupment maths reproduces from the stated net-per-unit assumption.
- [ ] Each objection has evidence or a dated plan to get it.

## False-Positive Prevention

1. **A trailer is not a vertical slice.** If the loop cannot be played, the pitch
   is a concept pitch; say so and adjust the ask.
2. **Hit comps are survivorship bias.** A base case set by the genre's breakout
   hit will be discounted by any experienced publisher.
3. **Do not present estimates as sales data.** Review-count multipliers are rough;
   show the range and the method.
4. **Contingency is not padding.** Removing it to lower the ask makes the budget
   less credible, not more.
5. **Wishlists are not sales.** Report them as a signal with the conversion
   assumption stated, not as units.
6. **Do not tailor away the game.** Fitting a partner's portfolio is good; pitching
   a different game than the one in the build is not.

## Example

**Input:** "Lanternfall", a co-op roguelite deckbuilder, PC then console, $19.99.
Team of 6, 18-month schedule. Slice: 15 minutes, two biomes. Ask: advance + porting.

```markdown
## Hook
"Two players share one deck and one lantern — every card you play lights the
path or burns the fuel your friend needs."

## Proof
Assertion: the shared-deck loop is fun with strangers.
Slice: 2 biomes, 38 cards, 1 boss; art final in biome 1, placeholder in biome 2.
Playtest (N = 12, fresh genre players): 10/12 chose to play a second run;
median session 52 min of a 60-min slot.

## Market (all figures [verify]; method: reviews × 30–60)
| Comp | Year | Price | Reviews | Est. units |
|---|---|---|---|---|
| Comp A (co-op deckbuilder) | 2023 | $19.99 | 4,200 | 126k–252k |
| Comp B (solo roguelite deckbuilder) | 2022 | $14.99 | 1,900 | 57k–114k |
| Comp C (co-op roguelite, breakout) | 2021 | $24.99 | 9,800 | 294k–588k — outlier, excluded from base |

## Team
Lead designer and lead programmer shipped one prior roguelite together; 6 FTE.

## Budget
| Line | Calc | Amount |
|---|---|---|
| Staff | 6 × $8,500 × 18 months | $918,000 |
| Tools & software | | $36,000 |
| Outsourcing (audio, localisation, console port) | | $150,000 |
| QA & certification | | $60,000 |
| Subtotal | | $1,164,000 |
| Contingency | 15% | $174,600 |
| **Total ask** | | **$1,338,600** |

## Milestones
| # | Deliverable | Month | Payment |
|---|---|---|---|
| M1 | Signing | 0 | $200,000 |
| M2 | Production-ready slice (all systems) | 4 | $200,000 |
| M3 | Content alpha (4 biomes) | 8 | $250,000 |
| M4 | Beta, online co-op stable | 12 | $250,000 |
| M5 | Content complete, localised | 16 | $250,000 |
| M6 | Gold + console cert passed | 18 | $188,600 |
| | | **Sum** | **$1,338,600** |

## Recoupment
Assumption: $10 net per unit after platform share, regional pricing, discounts.
Units to recoup = $1,338,600 ÷ $10 = 133,860. Post-recoup split 50/50.
| Case | Units | Net | Partner recovers | Post-recoup each |
|---|---|---|---|---|
| Low (≈ Comp B low end) | 60,000 | $600,000 | $600,000 (45%) | $0 |
| Base (within Comp A range) | 150,000 | $1,500,000 | $1,338,600 | $80,700 |
| High | 400,000 | $4,000,000 | $1,338,600 | $1,330,700 |

## Objections
| Objection | Evidence | Status |
|---|---|---|
| "Co-op roguelites need online play; can you ship netcode?" | lead programmer shipped rollback co-op before | Partial — online not in slice; M4 gate |
| "Deckbuilders are saturated." | Comp A/B show demand at this price; shared-deck hook untested in comps | Open — wishlist test at demo |
| "Six people, 18 months, console port?" | port outsourced, $ in budget | Answered |

## Open items
First invented fact: $10 net per unit. Evidence it with the partner's own
discount and regional-pricing history before term-sheet stage.
```

## Techniques Used

- **ST-46 (Assertion-Evidence Content Structure):** every section leads with its claim.
- **NE-23 (Objection Pre-emption):** the partner's three hardest questions answered in advance.
- **NE-11 (Embedded Calculation Formulas):** budget, milestone and recoupment arithmetic.
- **QA-26 (First-Invented-Fact Test):** finds the number the partner must take on trust.

## Related Prompts

- `domain-game-development/design/design_game_design_document.md` — the internal design the pitch draws on.
- `domain-game-development/testing/testing_playtest_protocol_synthesis.md` — producing the "is it fun" evidence.
- `domain-game-development/design/design_core_loop_analysis.md` — what the vertical slice must prove.
