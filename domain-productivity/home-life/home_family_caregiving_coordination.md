---
title: "Family Caregiving Coordination — Weekly Rota, Shared Expense Ledger, and Sibling Updates After the Care Decision"
category: productivity/home-life
description: "Run the ongoing operations of caring for a parent or relative once the arrangement has been chosen: a weekly care rota measured in hours with a named backup for every slot, a shared expense ledger with an agreed split and a monthly settle-up, a one-page care information sheet, a short standing update to siblings, and a monthly load check that catches one person quietly doing everything; distinct from `domain-personal-development/major-decisions/personal_caring_for_aging_parent.md` (deciding the arrangement) and `home_family_schedule_coordinator.md` (one household's weekly calendar)."
techniques:
  - OC-03
  - NE-11
  - DS-06
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - caregiving
  - aging-parents
  - family
  - coordination
  - shared-expenses
  - siblings
  - siblings-not-helping
  - splitting-costs
  - care-schedule
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/major-decisions/personal_caring_for_aging_parent.md
  - domain-productivity/home-life/home_family_schedule_coordinator.md
  - domain-productivity/home-life/home_chore_rotation_designer.md
---

# Family Caregiving Coordination

**Objective:** Turn "we'll all help" into an operating rhythm — who covers which hours,
who pays for what and how it is settled, what everyone needs to know about the person's
care, how siblings stay informed without a group-chat flood — and a monthly check that
the load is still where the family agreed it would be.

**When to Use:**
- The care arrangement is decided (via `domain-personal-development/major-decisions/personal_caring_for_aging_parent.md` Step 4 or a
  family conversation), and now it has to run week after week.
- One sibling lives nearby and is doing most of it; others want to help but do not know how.
- Money is being spent by different people and nobody knows who is owed what.
- Updates happen by scattered calls and messages, and someone always hears last.

**Not this prompt if:**
- You have not decided the arrangement (home, move-in, facility) — `domain-personal-development/major-decisions/personal_caring_for_aging_parent.md` first.
- You are choosing between specific facilities — `domain-personal-development/major-decisions/personal_care_facility_comparison.md`.
- You are coordinating your own household's calendar — `home_family_schedule_coordinator.md`.
- The primary carer needs time off — `home_caregiver_respite_plan.md` builds the breaks this rota must protect.
- Medical care decisions or medication changes — the care team decides; this prompt only records who attends and what was said.

**Audience:** An adult child, sibling group or spouse coordinating care for one person. Works
whether the person lives at home, with family or in a facility (visits and admin still need a rota).

## Inputs Required

1. **The arrangement** and the care tasks it creates: personal care, meals, medications
   (who manages, not what), appointments and transport, shopping, bills and admin, visits,
   overnight cover.
2. **Each helper:** distance, hours they can realistically give per week, skills, constraints
   (work, own children, health), and whether they contribute time, money or both.
3. **Paid help** already in place and its hours.
4. **Costs:** recurring (care hours, facility fees, supplies) and irregular (repairs, equipment);
   who is paying now.
5. **The agreed split,** if one exists — or the disagreement, if not.
6. **The person's own preferences** about who does personal care, visits and routines.

## Instructions

### Step 1 — Inventory tasks in hours, not names
List every recurring task with frequency and time per week. Sum it. The total is the size of
the job; most families have never seen the number.

### Step 2 — Build the weekly rota (OC-03)
A grid of slots (day × part of day) with a primary and a **named backup** for every slot.
Distant siblings take remote tasks (bills, insurance calls, online shopping, appointment
booking, calls to the parent). Compare each person's hours to what they said they could give.

### Step 3 — Set up the expense ledger (NE-11)
Columns: date, item, amount, paid by, category, receipt link. Agreed split rule (equal,
by income share, time-offsets-money, or parent's own funds first). Monthly settle-up:
`each person's share = total × their split %`; `balance = paid − share`; positive balances are
owed. Anything paid from the parent's own funds is logged separately and transparently —
whoever manages it is handling someone else's money, and questions about authority to do so
go to the attorney who drafted any power of attorney.

### Step 4 — Write the care information sheet
One page every helper can see: routines, preferences, allergies and medication list *location*
(not doses rewritten from memory), doctors and pharmacy, emergency contacts, who holds
decision-making authority (as documented, not assumed), and "what to do if…" for falls,
confusion and missed medications — each pointing to the care team's instructions.

### Step 5 — Set the update rhythm
A short weekly written update from the primary carer (template: how they are; what changed;
appointments coming; decisions needed; help needed). One channel, one day. Decisions that
need everyone go to a monthly call with an agenda, not the chat.

### Step 6 — Monthly load check (DS-06, QA-01)
Compare planned hours and money to actual. Flag anyone above their agreed share by more than
~20% — usually the nearest sibling. Rebalance by moving remote tasks, adding paid hours, or
revisiting the split. If the primary carer's load is unsustainable, trigger the respite plan
and, if the arrangement itself no longer works, revisit the care decision prompt's tripwire.

## Constraints

### Must
- Give every rota slot a backup.
- Measure load in hours and money, not in goodwill.
- Keep the parent's own funds separate in the ledger.
- Record decision-making authority as documented; route questions about it to the attorney.

### Must Not
- Rewrite medication doses or care instructions from memory — point to the care team's version.
- Let the chat become the decision forum.
- Assign personal care to someone the person has said they do not want doing it, without discussing it.

## Output Format

```
## Caregiving coordination — [person/relationship], from [date]
Arrangement: [...] · Total care load: [n] h/week · Paid help: [n] h/week

### Weekly rota
| Slot | Task | Primary | Backup | Hours |

### Hours vs. capacity
| Person | Offered h/wk | Rostered h/wk | Difference |

### Expense ledger (columns) + split rule + settle-up formula
### Care information sheet (one page)
### Weekly update template · channel · day
### Monthly load check | Person | Planned h | Actual h | Planned £/$ | Actual | Flag |
```

## Verification

- [ ] Total weekly care hours stated.
- [ ] Every slot has a primary and a backup.
- [ ] No one is rostered beyond the hours they offered without it being flagged.
- [ ] Split rule agreed and written; settle-up formula shown.
- [ ] Parent's funds logged separately.
- [ ] Care sheet points to care-team instructions rather than restating doses.
- [ ] Monthly load check has a threshold and a rebalancing action.

## False-Positive Prevention

1. **"We share it equally" with no numbers.** Without hours per person, the nearest sibling
   does most of it and the others believe they are helping equally.
2. **No backups.** A rota with one name per slot fails at the first illness.
3. **Money settled by feel.** Unlogged spending becomes resentment. Log and settle monthly.
4. **Distance as exemption.** Remote siblings can own admin, calls and bills; the rota should
   say so.
5. **The group chat as control room.** Decisions made in a chat are missed by whoever was
   driving. Weekly written update, monthly decisions call.
6. **Care sheet as medical record.** Copying doses from memory introduces errors; point to the
   authoritative list.
7. **Ignoring the parent's say.** Who helps with bathing or finances is their preference too.

## Example Output

```
## Caregiving coordination — Mum (lives at home, L2 needs), from 2026-10-01
Total care load: 21 h/week · Paid help: 6 h/week (agency, Mon/Wed/Fri mornings)

### Weekly rota (excerpt)
| Tue/Thu evening | Meal + meds check | Jo (10 min away) | Sam (video call + neighbour Rita) | 3 |
| Sat | Shopping + visit | Sam (drives 2 h) alternate weeks | Jo | 4 |
| Weekly | Bills, insurance calls, pharmacy reorder | Priya (abroad) | Sam | 2 |

### Hours vs. capacity
| Jo | 6 | 9 | +3 ⚠ |
| Sam | 5 | 4 | −1 |
| Priya | 2 | 2 | 0 |

### Split rule: care costs from Mum's pension first; shortfall split Jo 25% / Sam 35% / Priya 40% (Priya contributes less time)
September settle-up: shortfall [amount]; Jo paid [amount] for grab rails → balance owed to Jo [calc]

### Weekly update — Sundays, family email, Jo writes (5 lines)
### Monthly load check (October): Jo +3 h over offer → move Thursday meds check to Sam by video + add 2 agency hours; review in November
```

## Techniques Used

- **OC-03 Markdown Table Specification** — rota, capacity and load-check tables.
- **NE-11 Embedded Calculation Formulas** — share, balance and settle-up arithmetic.
- **DS-06 Prioritization and Severity Guidance** — over-share threshold that triggers rebalancing.
- **CM-02 Constraint Specification** — backups, separate parent funds, no rewritten doses.
- **QA-01 Self-Verification** — monthly planned-vs-actual check.

## Related Prompts

- `../../domain-personal-development/major-decisions/personal_caring_for_aging_parent.md` — the decision this operationalises.
- `home_caregiver_respite_plan.md` — protected breaks for the primary carer.
- `home_family_schedule_coordinator.md` — the carer's own household calendar.
- `home_chore_rotation_designer.md` — load-by-time distribution, the same principle at home.
