---
title: "Pharmacology Brand–Generic Recall Set (High-Frequency Generics by Class)"
category: medical-education/learner-foundational-sciences
description: "Produce a two-way recall deck for brand ↔ generic name pairs within a named drug class, ranked by US prescription frequency. Locked table format, no fluff, dual-direction cards."
techniques:
  - ST-03
  - OC-03
  - CM-02
  - DS-02
  - QA-12
difficulty: beginner
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pharmacy-student
  - pa-student
  - nursing-student
tags:
  - pharmacology
  - brand-name
  - generic-name
  - drug-class
  - flashcards
  - recall
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_pharmacology_mechanism_flashcard_set.md
---

## Objective

Generate a recall table for brand ↔ generic name pairs in a named drug class, ranked by US prescription frequency (high → low), and produce dual-direction flashcards (generic→brand, brand→generic). No mechanism, no AE, no monitoring — those belong in the mechanism flashcard set. This is name recall only.

## Your Role

You are a pharmacy preceptor building name-recall material for students starting a clinical rotation. The student needs to recognize "Lipitor" as atorvastatin within one second.

## Inputs

- `drug_class`: e.g., "statins," "SSRIs," "SGLT2 inhibitors," "non-DHP calcium channel blockers," "beta-blockers — cardioselective"
- `top_n`: integer, how many highest-frequency members to include (default 10; cap 25)
- `country_market`: `US` | `EU-UK` | `Canada` | `Australia` — affects which brand names are listed
- `include_combination_products`: `true | false` — include common combo pills (e.g., losartan/HCTZ → Hyzaar)?
- `include_otc`: `true | false`

## Method

1. **Build the ranked member list.** Order members by US prescription frequency (or stated market) — most-prescribed first. If you are unsure of exact ranks beyond top 5, group remaining members as "secondary frequency" rather than fabricating ranks.

2. **For each member, populate the row:** generic name, all common brand names (primary + alternates), year of US generic availability if relevant, marketing memory hook if it helps (e.g., "Pravachol — pravastatin").

3. **Locked table format (OC-03).** Markdown table. Columns: `#`, `Generic`, `Brand (primary)`, `Brand (alternates)`, `Notes`.

4. **Dual-direction cards.** Below the table, generate the deck:
   - Direction A: Generic → primary brand
   - Direction B: Primary brand → generic
   - Each row produces two cards. Skip alternates unless the alternate is itself high-frequency (e.g., DiaBeta, Micronase, Glynase for glyburide).

5. **Confusable-pair callouts (QA-12).** End with a short list of *commonly confused* generic names (e.g., hydroxyzine vs. hydralazine; clonidine vs. klonopin/clonazepam) — explicitly flag the trap.

6. **Combination products section.** If `include_combination_products = true`, separate table for each combo with components.

## Output Format

```
BRAND–GENERIC RECALL — [class]
Market: [...]   Top N: [...]   Combos: [yes/no]   OTC: [yes/no]

| # | Generic | Brand (primary) | Brand (alternates) | Notes |
|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [year generic; memory hook] |
| 2 | ...   |  ...  | ...   | ... |

>>> DECK CARDS

A. Generic → Brand
A1  [generic]   →   [primary brand]
A2  ...

B. Brand → Generic
B1  [primary brand]   →   [generic]
B2  ...

>>> COMMONLY CONFUSED (QA-12)
- [drug A] vs. [drug B]: A is a [class/use]; B is a [class/use]. Mnemonic: [...]
- ...

>>> COMBINATION PRODUCTS (if requested)
| Combo brand | Components |
|---|---|
| [...] | [generic1 + generic2 (+ generic3)] |
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `top_n` | Controls deck size |
| `country_market` | Switches brand-name list (US Lipitor vs. UK Lipitor or Lipostat for pravastatin) |
| `include_combination_products` | Adds combo-pill table |
| `include_otc` | Adds OTC members (loratadine = Claritin, etc.) |
| `add_pronunciation` | Adds phonetic spelling column (useful for nursing students) |
| `add_class_marker_suffix` | Adds reminder line listing the stem identifier (e.g., "-statin," "-pril," "-sartan," "-olol") |

## Verification Checklist

- [ ] Members are ranked by frequency, not alphabetical, unless the user explicitly asks alphabetical.
- [ ] Every entry has at least the primary brand name; alternates listed when commonly seen.
- [ ] No invented brand names. If a brand is regional, country flag stated.
- [ ] Dual-direction cards present for every row.
- [ ] Confusable-pair callouts include at least one *real* trap encountered in clinical practice (not made up).
- [ ] If combos requested, components are correct and dose-strength caveats noted where relevant.
- [ ] Class-stem suffix listed if `add_class_marker_suffix = true`.

## Worked Example (compact)

**Input:** `drug_class = statins`, `top_n = 7`, `country_market = US`, `include_combination_products = true`, `add_class_marker_suffix = true`.

**Output:**

```
BRAND–GENERIC RECALL — Statins (HMG-CoA reductase inhibitors)
Market: US   Top N: 7   Combos: yes   OTC: no
Class stem: "-statin"

| # | Generic | Brand (primary) | Brand (alternates) | Notes |
|---|---|---|---|---|
| 1 | atorvastatin | Lipitor | — | Most-prescribed statin in US; generic 2011 |
| 2 | rosuvastatin | Crestor | — | High-intensity dose-equivalent; generic 2016 |
| 3 | simvastatin | Zocor | — | Older; CYP3A4 interactions limit dose |
| 4 | pravastatin | Pravachol | — | Hydrophilic; preferred with cyclosporine |
| 5 | lovastatin | Mevacor | Altoprev (ER) | First statin approved (1987) |
| 6 | fluvastatin | Lescol | Lescol XL | Lower-potency; less interaction |
| 7 | pitavastatin | Livalo | Zypitamag | Newer; minimal CYP interactions |

>>> DECK CARDS

A. Generic → Brand
A1  atorvastatin → Lipitor
A2  rosuvastatin → Crestor
A3  simvastatin → Zocor
A4  pravastatin → Pravachol
A5  lovastatin → Mevacor
A6  fluvastatin → Lescol
A7  pitavastatin → Livalo

B. Brand → Generic
B1  Lipitor → atorvastatin
B2  Crestor → rosuvastatin
B3  Zocor → simvastatin
B4  Pravachol → pravastatin
B5  Mevacor → lovastatin
B6  Lescol → fluvastatin
B7  Livalo → pitavastatin

>>> COMMONLY CONFUSED (QA-12)
- pravastatin vs. pitavastatin: spell-alike, different potency tiers and CYP profile.
- simvastatin vs. sitagliptin: prefix collision; sitagliptin is a DPP-4 inhibitor (Januvia), not a statin.
- Lipitor vs. Lopressor: Lipitor = atorvastatin (statin); Lopressor = metoprolol tartrate (beta-blocker).

>>> COMBINATION PRODUCTS
| Combo brand | Components |
|---|---|
| Caduet | amlodipine + atorvastatin |
| Vytorin | ezetimibe + simvastatin |
| Liptruzet | ezetimibe + atorvastatin |
```
