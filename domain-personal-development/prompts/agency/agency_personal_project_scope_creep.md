---
title: "Cut Scope Creep on a Personal Project Back to a Shippable Core"
category: personal-development/agency
description: "Reconstruct the original commitment for a stalled personal project, tag every element that got added since, classify each addition against a fixed taxonomy of creep sources, and re-cut to a shippable core with one next action."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - agency
  - scope-creep
  - shipping
  - project-management
  - re-cut
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
  - domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-productivity/bottlenecks/bottleneck_perfectionism_ship_threshold.md
  - domain-personal-development/prompts/goals/goals_skill_breakdown_blueprint.md
---

# Cut Scope Creep on a Personal Project Back to a Shippable Core

**Objective:** For a personal project that has quietly grown since it started, separate what the project became from what it was committed to be, then re-cut it to a shippable core — a named reduced scope, a deferred list, and a killed list — ending in one next action on the core.

**When to use:** The user started a project with a rough idea of what "done" meant, and months later it's bigger, unshipped, and heavier than the thing they set out to make. Also useful before a `agency_ship_sprint_design.md` sprint, to lock scope before the window starts. Not for a project whose direction genuinely changed on purpose — that's a pivot, not creep (route to `agency_project_ownership_converter.md`).

**Audience:** An individual re-cutting their own project. Not for scoping a team's roadmap or a client deliverable.

---

## Inputs Required

1. **The original commitment.** What the user first said they'd ship, and by roughly when — in their words at the time, not cleaned up. If they can only state today's version, flag it: the drift may be so complete they've lost the v0.
2. **Current scope.** Everything the project now contains or plans to contain — features, sections, chapters, polish items, infrastructure — as a flat list.
3. **Rough timeline.** When each item entered scope: was it in the original, or added later? Best recall is fine.
4. **Why each added item went in.** One phrase per addition ("realized readers would need it," "saw a nicer version," "as long as I'm in there").
5. **The purpose the original commitment served.** What shipping v0 was actually for — the reader, user, portfolio slot, or decision it was meant to serve.

If the user cannot produce input 1 at all, stop and treat that as the finding: the project has no reconstructable commitment to cut back to, and the first job is to declare one.

---

## Instructions

### Step 1 — Reconstruct the v0 scope

From input 1, write the original committed scope as a short bulleted list of what v0 was going to contain. This is the baseline every current item gets measured against. If the user's original was itself vague, sharpen it to the smallest coherent version that would have served the purpose in input 5.

### Step 2 — Tag every current item: original or added

Go through input 2. Tag each item **[original]** (traceable to the v0 scope) or **[added]** (entered after). Use input 3 to place ambiguous items; when unsure, tag **[added]** — the burden of proof is on staying in scope.

### Step 3 — Classify each added item against the creep taxonomy

For every **[added]** item, assign exactly one source from this fixed taxonomy:

| # | Creep source | Signature |
|---|---|---|
| 1 | **Justified discovery** | The v0 scope genuinely couldn't ship without it; a real gap, not a wish. |
| 2 | **Gold-plating** | Makes an already-adequate element nicer, not more shippable. |
| 3 | **Adjacent-project bleed** | Work that belongs to a different project migrated in. |
| 4 | **Prerequisite inflation** | An upstream "I must do this first" that pushed the ship date out. |
| 5 | **Audience-imagined** | Added for a hypothetical user/reader who has not asked for it. |
| 6 | **Completeness compulsion** | "As long as I'm here, I should also cover X" — coverage for its own sake. |
| 7 | **Feature envy** | Added to match someone else's version the user saw. |

Only source #1 is presumptively kept. All others are presumptively cut or deferred.

### Step 4 — Apply the cut test

For each item (original and added), decide **must-ship / defer / kill** against a single question: *does v0 serve its purpose (input 5) without this?*

- **Must-ship:** removing it means v0 no longer serves the purpose. Includes all [original] items still load-bearing and any source-#1 discovery.
- **Defer:** genuinely wanted, but v0 ships and serves its purpose without it. Goes to a named next-version list.
- **Kill:** serves no version of the purpose, or belongs to another project. Gold-plating, bleed, envy, and most completeness/audience-imagined items land here.

Every non-must-ship item must name where it goes (defer list or killed list). Nothing floats.

### Step 5 — Re-cut to the shippable core

State the reduced scope as the must-ship set only. Sanity-check it two ways: it must still be a coherent, recognizable artifact (not cut so hard it stops being the thing), and no genuinely load-bearing item was deferred. If the core fails either check, move the minimum item back.

### Step 6 — One next action on the core

Produce a single physical next action on the re-cut core — at the level of "open [file] and [motion]" (see `agency_next_action_spec.md` if the action needs full specification). Not a plan to work through the deferred list. The decisive output is the smaller scope plus the first motion inside it.

---

## Constraints

### Must
- Reconstruct a concrete v0 scope before judging any current item.
- Tag every current item original/added and classify every added item to exactly one taxonomy source.
- Route every non-must-ship item to a named defer or kill list — nothing floats.
- Verify the re-cut core is still a coherent, shippable artifact.
- End in exactly one next action on the core.

### Must Not
- Treat every addition as creep — source #1 (justified discovery) is real and stays.
- Confuse scope creep with a deliberate pivot (route pivots to `agency_project_ownership_converter.md`).
- Cut so aggressively the artifact stops being recognizable or stops serving its purpose.
- Defer an item that the core genuinely depends on.
- Moralize about the creep or use motivational language about "focus" and "discipline."

---

## False-Positive Prevention

1. **Don't cut justified discovery.** Some additions are real: the original scope was under-built and would not have shipped. Source #1 items stay in must-ship even though they're [added].
2. **Don't call a pivot creep.** If the project deliberately changed what it is (different audience, different artifact), that's a re-decision, not creep — this prompt would cut the wrong things. Send it to project ownership.
3. **Don't over-cut into incoherence.** A shippable core is still the whole thing at v0, not a stub. If the cut leaves an artifact a stranger couldn't use or read, a must-ship item was mis-tagged.
4. **Don't defer load-bearing items.** "Nice to have" is about the purpose, not the user's affection for the item. Test each defer against whether the core survives its removal.
5. **Don't miss scope-as-avoidance.** Some creep is planning-masquerade — adding scope to avoid finishing. If the added items cluster in prerequisite inflation and audience-imagining with zero shipped artifact, run `agency_planning_masquerade_detector.md` alongside this.
6. **Don't assume the original was right.** If v0 itself was over-scoped, cut below it. The baseline is the purpose (input 5), not the first plan.

---

## Output Format

```
## Original commitment (v0)
[Reconstructed baseline scope, bulleted. Flag if it had to be sharpened or could not be recovered.]

## Purpose v0 serves
[One line from input 5 — the test every item is measured against.]

## Scope inventory
| Item | Origin | Creep source (if added) | Verdict |
|---|---|---|---|
| ... | original / added | [taxonomy # + name, or "—"] | must-ship / defer / kill |

## Re-cut shippable core
[The must-ship set only. Confirm it is still a coherent, recognizable artifact.]

## Deferred (next version)
- [Item → why wanted but not now]

## Killed
- [Item → why it serves no version of the purpose]

## Next action on the core
[One physical motion: open [file], do [Y]. Not a plan for the deferred list.]

## Flag (if any)
[Pivot suspected / v0 unrecoverable / creep looks like avoidance — with the prompt to run next.]
```

---

## Verification

- [ ] A concrete v0 baseline was reconstructed before any item was judged.
- [ ] Every current item is tagged original/added; every added item has exactly one taxonomy source.
- [ ] Every non-must-ship item is routed to a named defer or kill list.
- [ ] Justified-discovery additions were kept, not reflexively cut.
- [ ] The re-cut core is confirmed to still be a coherent, shippable artifact.
- [ ] Output ends in exactly one physical next action on the core.
- [ ] No moralizing about focus or discipline, no motivational language.
