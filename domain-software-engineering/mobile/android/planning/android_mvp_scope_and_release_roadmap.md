---
title: "Android MVP Scope & Release Roadmap"
category: mobile-development
description: "Turn a validated Android app concept into a defended MVP cut line, a prioritized feature backlog (RICE + MoSCoW), and a phased MVP → V1 → V2 release train with explicit themes, exit criteria, and scope-creep guardrails."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - AG-12
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - mvp
  - product-planning
  - prioritization
  - release-planning
updated: "2026-06-06"
related_prompts:
  - android_app_concept_validation.md
  - android_feature_specification.md
  - android_estimation_and_milestone_plan.md
---

# Android MVP Scope & Release Roadmap

**Objective:** Convert a validated app concept into a buildable plan — define exactly what goes into the MVP (and, more importantly, what is cut), prioritize the full feature backlog with both RICE scoring and MoSCoW classification, tie every MVP feature to the assumption it validates, and sequence a MVP → V1 → V2 release train where each release has a single theme, a clear "definition of done," and measurable exit criteria.

**When to Use:** Use this prompt after you have decided to build (concept validated, go decision made) but before you write a feature specification or estimate timelines. Ideal when your idea has 15+ candidate features and you need to ruthlessly decide which 4–7 actually ship first, or when scope keeps expanding and you need a defensible cut line to point at.

**Sequence Map:** Use **after** [android_app_concept_validation.md](android_app_concept_validation.md) (you have a go decision and a rough feature list); use **before** [android_feature_specification.md](android_feature_specification.md) (you spec the features that survived the MVP cut) and [android_estimation_and_milestone_plan.md](android_estimation_and_milestone_plan.md) (you estimate the phased plan this produces).

**Important context:** The default failure mode for indie and small-team Android apps is not building the wrong app — it is building too much of the right app before learning anything. An MVP is not "version 1 with fewer features"; it is the smallest thing that lets you learn whether your riskiest assumption is true. Two disciplines fight scope creep: **riskiest-assumption-first** (build the feature that, if it fails, kills the product) and **walking-skeleton** (a thin end-to-end slice through every architectural layer — UI → ViewModel → repository → data source → ship — that proves the plumbing works before you widen any one feature). A backlog that is "prioritized" but never has a hard cut line is just a wish list. This prompt forces the cut line.

---

## Context Gathering

Before scoping anything, gather the inputs that constrain the cut line. Ask in groups; do not proceed until you have answers to groups 1–3.

1. **Concept & Validation State:**
   - "Paste your one-sentence app concept and the single riskiest assumption from your validation work (the thing that, if false, sinks the product)."
   - "What is the core user value — the one job the app does that, if removed, makes it pointless?"
   - "Has the concept been validated (interviews, landing page, competitor gap)? Or are you building to learn?"

2. **Resources & Team Shape:**
   - "Solo developer, or a team? If a team, how many engineers, and is there a designer / QA?"
   - "How many focused hours per week can the team actually commit (be honest — nights/weekends count differently)?"
   - "Is there a hard external deadline (event, funding, seasonality) or is the timeline flexible?"

3. **Feature Inventory:**
   - "List every feature you can imagine for the finished app — dump them all, no filtering. Aim for 12–25."
   - "For each, in a few words: what user problem does it solve?"
   - "Which features are 'table stakes' (competitors all have them and users would reject the app without them)?"

4. **Platform & Distribution Constraints:**
   - "Target minSdk and the device classes you care about (phones only? tablets/foldables? Wear/TV/Auto?)."
   - "Any release channel constraints — closed/open testing track, staged rollout, an existing user base to migrate?"
   - "Any non-negotiable compliance gates before public launch (Play Data safety form, account deletion endpoint, age rating)?"

5. **Definition of Success:**
   - "What single metric tells you the MVP worked? (e.g., 40% of new users complete the core action in week 1.)"
   - "What would make you kill or pivot the concept after the MVP?"

---

## Instructions

Work the phases in order. Each phase ends at a CHECKPOINT — present the artifact and get explicit confirmation before moving on. Do not generate the full roadmap in one shot; the user's reactions at each checkpoint reshape later phases.

### Phase 1: Establish the Riskiest Assumption & Core Value

Restate the product as a single sentence and isolate the one assumption the MVP must test. Everything downstream serves this.

```markdown
## MVP North Star

**One-liner:** [App] helps [user] do [job] so they can [outcome].

**Riskiest assumption (the MVP must test this):**
"[The specific belief that, if false, means we should stop or pivot.]"

**Core action (the walking skeleton must complete this end to end):**
"[The single user action the app exists to enable — e.g., 'log a workout and see it in history'.]"

**MVP success signal:** [Metric + threshold that confirms the assumption.]
**Kill/pivot signal:** [What result tells us to stop.]
```

**CHECKPOINT 1:** Confirm the riskiest assumption and core action with the user before scoring features. If the user cannot name a single riskiest assumption, that is itself a finding — push back before proceeding.

---

### Phase 2: Score the Backlog (RICE + MoSCoW)

Run **both** frameworks on the full inventory. They answer different questions: RICE ranks by expected value per effort; MoSCoW classifies by necessity for *this* release. A feature can be high-RICE but still `Won't` (great idea, wrong release).

**RICE scoring** — `(Reach × Impact × Confidence) / Effort`:

| Field | Scale | Android-specific guidance |
|-------|-------|---------------------------|
| **Reach** | est. users affected per period | Be specific to your SOM, not the whole Play Store. |
| **Impact** | 3 massive / 2 high / 1 medium / 0.5 low / 0.25 minimal | How much it moves the core action's completion. |
| **Confidence** | 100% high / 80% medium / 50% low | Drop confidence for anything needing unproven SDKs or backend work. |
| **Effort** | person-weeks | Include Android tax: Compose UI, ViewModel, repo, tests, Play review, edge-to-edge/predictive-back, config-change survival. |

| Feature | Reach | Impact | Confidence | Effort (pw) | RICE | MoSCoW |
|---------|-------|--------|------------|-------------|------|--------|
| [Core action flow] | … | 3 | 100% | … | … | Must |
| [Onboarding/auth] | … | 2 | 80% | … | … | Must |
| [Settings/DataStore] | … | 1 | 100% | … | … | Should |
| [Social sharing] | … | 1 | 50% | … | … | Could |
| [Widget / Wear tile] | … | 0.5 | 50% | … | … | Won't (V2) |

**MoSCoW definitions for this MVP:**
- **Must** — the walking skeleton breaks or the riskiest assumption can't be tested without it.
- **Should** — important, painful to omit, but the app still tests its assumption without it.
- **Could** — nice; include only if effort is near-zero and it doesn't widen the skeleton.
- **Won't (this release)** — explicitly deferred. Naming these is the point; an empty "Won't" list means nothing was actually cut.

**CHECKPOINT 2:** Present the scored table. Resolve every conflict where RICE rank and MoSCoW class disagree — these are the highest-value conversations (e.g., a high-RICE "Could" that's tempting to sneak in, or a low-RICE "Must" that's pure table stakes).

---

### Phase 3: Draw the MVP Cut Line

Produce the explicit in/out decision table. **Every "in MVP" feature must name the assumption it validates** — if a feature validates nothing and isn't table stakes, it doesn't belong in the MVP.

| Feature | In MVP? | MoSCoW | Validates which assumption / why table stakes | If cut, deferred to |
|---------|---------|--------|-----------------------------------------------|---------------------|
| [Core action flow] | ✅ In | Must | Directly tests the riskiest assumption | — |
| [Account / auth] | ✅ In | Must | Table stakes; needed to persist core data | — |
| [Local persistence (Room)] | ✅ In | Must | Walking skeleton: proves data layer | — |
| [Push notifications] | ❌ Out | Should | Retention lever, not assumption test | V1 |
| [Offline sync] | ❌ Out | Could | Premature until single-device value proven | V1/V2 |
| [Theming / Dynamic color] | ❌ Out | Could | Polish; doesn't test value | V1 |
| [Tablet/foldable layouts] | ❌ Out | Won't | Phone-first; revisit after PMF signal | V2 |

**Walking-skeleton check:** trace the core action through every layer and confirm each layer is represented by a Must:

```
[Tap "Add"] → Compose screen (Must) → ViewModel + StateFlow (Must)
   → Repository (Must) → Room DAO (Must) → [persisted] → list recomposes (Must)
```

If any layer is missing a Must feature, the skeleton has a hole — fix the cut line, don't paper over it.

**CHECKPOINT 3:** Get the user to verbally agree to the cut. The cut line is only real if they can say "yes, X is out of the MVP" without flinching.

---

### Phase 4: Define MVP "Definition of Done"

The MVP isn't done when features work — it's done when it's shippable to real users on a Play test track. Use a concrete checklist, not "feels finished."

```markdown
## MVP Definition of Done
**Functional**
- [ ] Core action completes end to end on a clean install
- [ ] All "Must" features implemented and manually verified on min + target API levels

**Android quality bar (non-negotiable in 2026)**
- [ ] Survives configuration changes & process death (state restored)
- [ ] Edge-to-edge layout correct; predictive back works
- [ ] No main-thread blocking (StrictMode clean on core flows)
- [ ] Handles no-network and permission-denied paths gracefully
- [ ] Accessibility: TalkBack can complete the core action; min touch targets met

**Release gates**
- [ ] Play Console: Data safety form, target API level, account-deletion path (if accounts), age rating
- [ ] Crash-free baseline established (Crashlytics/Play vitals wired)
- [ ] Analytics for the success metric instrumented BEFORE launch
- [ ] Closed/internal testing track validated with ≥N real testers
```

---

### Phase 5: Sequence the Release Train (MVP → V1 → V2)

Each release gets **one theme** and **exit criteria** that must be met before the next release starts. Themes prevent the "grab-bag release" anti-pattern.

| Release | Theme (one sentence) | Headline features | Exit criteria (start next release only when…) |
|---------|----------------------|-------------------|------------------------------------------------|
| **MVP** | Prove people complete and value the core action | Core flow, auth, local persistence | Success metric hit OR clear kill/pivot signal; crash-free ≥ baseline |
| **V1** | Make the validated value sticky | Push/reminders, basic offline, polish, onboarding refinement | Retention target met; top 3 user-reported gaps closed |
| **V2** | Expand reach & surfaces | Tablet/foldable adaptive UI, widget/Wear, sync, monetization | V1 retention stable; capacity for new platform support |

**Per-release detail block (repeat for each):**

```markdown
### Release: [MVP / V1 / V2]
**Theme:** [one sentence — the question this release answers]
**In scope:** [features, drawn from the backlog classes]
**Explicitly NOT in scope:** [the tempting things deferred — restate them]
**Learning goal:** [what shipping this teaches you]
**Exit criteria:** [measurable conditions to call it done and move on]
```

**CHECKPOINT 4:** Present the full release train and confirm the V1/V2 deferrals match the Phase 3 cut line (deferred features must land in a named release, not vanish).

---

### Phase 6: Scope-Creep Guardrails

Give the user a standing rule set to apply during the build, so new ideas get triaged instead of silently absorbed.

```markdown
## Scope-Creep Guardrails
1. New idea during MVP build → it goes to the backlog as "Won't (this release)" by DEFAULT.
   It only enters the MVP if it (a) tests the riskiest assumption or (b) fixes a broken
   walking-skeleton layer. Otherwise: V1+.
2. "While we're in there" features are forbidden. One PR, one purpose.
3. Any feature that adds a new architectural layer (new SDK, backend service, permission)
   during MVP requires a CHECKPOINT — re-run the cut-line table.
4. Polish (theming, animation, dynamic color, adaptive layouts) is V1+ unless it blocks
   the core action.
5. The cut-line table is the source of truth. If it isn't in the "In MVP" rows, it isn't in the MVP.
```

**Solo-dev vs team framing:**
- **Solo:** bias the cut line smaller (each Must has no backup if it slips). Prefer fewer, fully-finished Musts over many half-done ones. Effort estimates should assume you also do design, QA, and release ops.
- **Team:** the cut line is also a coordination contract — Musts can parallelize across people, but the walking skeleton's integration points need an owner. Add an explicit "integration owner" for the end-to-end core flow.

---

## Expected Output

1. **MVP North Star** — one-liner, riskiest assumption, core action, success and kill signals.
2. **Scored Backlog** — full feature table with RICE scores and MoSCoW classes, with RICE/MoSCoW conflicts called out.
3. **MVP Cut-Line Table** — explicit in/out decision per feature, each "in" feature mapped to the assumption it validates, each "out" feature mapped to a future release.
4. **Walking-Skeleton Trace** — the core action threaded through every layer, confirming no layer lacks a Must.
5. **MVP Definition of Done** — functional, Android quality, and release-gate checklists.
6. **Release Train** — MVP → V1 → V2 table plus a per-release detail block (theme, scope, learning goal, exit criteria).
7. **Scope-Creep Guardrails** — standing rules tailored to solo vs team.

---

## CRITICAL: Verification Requirements

- [ ] The riskiest assumption is named and a single MVP success metric is defined (not a vague "users like it").
- [ ] Every "In MVP" feature is justified by either an assumption it validates or table-stakes necessity.
- [ ] The "Won't (this release)" / "Out" list is non-empty — something was actually cut.
- [ ] The walking skeleton has a Must feature at every layer (UI → ViewModel → repository → data).
- [ ] Both RICE and MoSCoW were applied, and every disagreement between them was resolved on the record.
- [ ] Each release (MVP/V1/V2) has exactly one theme and measurable exit criteria.
- [ ] The MVP Definition of Done includes Android release gates (Data safety, target API, account deletion, accessibility), not just "features work."
- [ ] Every feature cut from the MVP is assigned to a named later release (nothing disappears).

---

## False-Positive Prevention

- ❌ Do NOT pad the MVP with features that don't test the riskiest assumption — "would be nice" is a V1 signal, not an MVP signal.
- ❌ Do NOT classify everything as "Must" — if more than ~6–7 features are Musts for a first release, the cut line failed.
- ❌ Do NOT recommend offline sync, multi-device, adaptive tablet/foldable layouts, or theming systems in the MVP unless they are the core value itself.
- ❌ Do NOT treat RICE rank as automatic inclusion — a high-RICE feature can still be the wrong release.
- ❌ Do NOT over-engineer the roadmap for a small project (a learning app or a side project may legitimately have no V2).
- ✅ DO match plan complexity to project ambition and team size — a solo nights-and-weekends app gets a smaller MVP and a looser train than a funded team.
- ✅ DO keep table-stakes features (auth, persistence) in the MVP even when their RICE is unglamorous.
- ✅ DO let "validate, then expand" drive sequencing — prove single-device value before sync, prove phone value before foldables.
- ✅ DO accept a deliberately tiny MVP as a strong outcome, not a sign of under-ambition.

---

## Techniques Used

- **ST-01** (Clear Objective Statement): Anchors the whole plan to one riskiest assumption and one core action.
- **ST-02** (Structured Sequential Instructions): Phased flow from north star → scoring → cut line → DoD → release train → guardrails.
- **RT-02** (Multi-Dimensional Analysis Framework): RICE and MoSCoW evaluate the backlog along independent axes (value/effort vs. necessity).
- **DS-06** (Prioritization and Severity Guidance): Explicit MoSCoW classes and the cut-line decision table force prioritization.
- **AG-12** (Quantitative Success Metrics): RICE numerics, success/kill thresholds, and measurable release exit criteria.
- **NE-02** (Phased Workflow Architecture): CHECKPOINT gates prevent generating the full roadmap before the user shapes each stage.

---

## Related Prompts

- [android_app_concept_validation.md](android_app_concept_validation.md) — Validate the concept and reach the go decision that feeds this roadmap.
- [android_feature_specification.md](android_feature_specification.md) — Specify the features that survived the MVP cut.
- [android_estimation_and_milestone_plan.md](android_estimation_and_milestone_plan.md) — Estimate timelines and milestones for the phased release train.
