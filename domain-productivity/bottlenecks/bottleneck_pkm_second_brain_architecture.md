---
title: "Design a Personal Knowledge System Sized to Real Use"
category: productivity/bottlenecks
description: "Architect note/reference system from observed retrieval behavior — what gets pulled out, where it goes, retention rules — not from aspirational structure. Counter to cargo-culted second-brain frameworks."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - NE-22
  - QA-19
difficulty: intermediate
tags:
  - pkm
  - second-brain
  - knowledge-management
  - retrieval
  - notes
updated: "2026-05-08"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-productivity/deep-work/deepwork_environment_friction_design.md
  - domain-productivity/deep-work/deepwork_project_state_synthesis.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
---

# Design a Personal Knowledge System Sized to Real Use

**Objective:** Design a personal knowledge / reference system from the *retrieval* end backward — what the user actually pulls out, when, and why — rather than from aspirational structure. Output: a minimal architecture, retention and link rules, and a 90-day check that distinguishes "system that gets used" from "system that gets maintained but not used."

**When to use:** The user has a notes/reference system (Notion, Obsidian, Apple Notes, plaintext folder, etc.) that has accumulated material but isn't producing value at retrieval — they don't pull from it, or they can't find what they pulled in. Or: the user wants to *start* a PKM and is at risk of cargo-culting a popular framework before proving the use case.

**Audience:** An individual designing their own PKM. Single-user. Not for shared team wikis.

---

## Inputs Required

1. **Current notes / reference state.** What exists today, where, in what tools, with rough item counts and oldest item.
2. **Real retrievals in the last 90 days.** When did the user actually pull something out of their notes / references and use it? List each: what was retrieved, what work it served, how the user found it. If "I never retrieve from my notes," that's a finding — the system is write-only.
3. **What the user wishes they could retrieve.** Things they know they captured but couldn't find when needed; or topics they wish were in the system but aren't.
4. **What gets captured today.** Categories of input: meeting notes, reading highlights, ideas, code snippets, recipes, references for ongoing work, decisions and their reasoning, links, quotes.
5. **Retention tolerance.** How long does the user actually want to keep most of this? Most users say "forever"; most usage data says "6 months max for the majority of items." Probe both.
6. **Time available for system maintenance.** Honest minutes per week.
7. **Existing tags / folders / structure.** Outline of what the user has in place, including which structures are aspirational (made but unused) vs. used.
8. **One real example of a retrieval that should have happened but didn't.** A specific case where the user needed something they had and couldn't find it.

If input 2 is empty (no retrievals in 90 days) and input 3 is empty (the user can't name things they wished to retrieve), the system isn't needed. State plainly: most "I should have a PKM" instincts are aspiration; some users genuinely don't need one. Refuse to design a system without retrieval evidence.

---

## Instructions

### Step 1 — Build the retrieval map first (NE-22 inversion)

Most PKMs are designed from the capture end ("how do I take notes?"). This prompt designs from the retrieval end backward. The architecture follows from what actually gets pulled out.

From inputs 2, 3, and 8, construct a retrieval map:

| Retrieved item (or wished-for) | Work it served / would have served | How retrieved (or how it should be retrievable) | Frequency |
|---|---|---|---|

Look for retrieval *patterns*. Most users have only 3–6 actual retrieval modes:

- **Project-context retrieval:** pulling notes about a current project's history, decisions, constraints.
- **Reference retrieval:** finding a specific known item — a quote, a code snippet, a contact, a rule.
- **Pattern-recognition retrieval:** noticing a current situation reminds the user of a past one, retrieving the past one.
- **Source-hunt retrieval:** "where did I read that?" — finding the source for a fact or idea.
- **Decision-context retrieval:** revisiting why a past decision was made.

Most personal systems serve 2–4 of these well. Identify which of these the user actually does, ranked by frequency.

### Step 2 — Choose the minimal architecture

Based on the retrieval modes used, pick the simplest architecture that supports them. Three patterns:

| Architecture | When | Structure |
|---|---|---|
| **Project-folders + reference-folder** | User's primary retrieval is project-context and reference. | One folder per active project; one "reference" folder for permanent items; archive folder for closed projects. No tags. |
| **Plaintext + search** | User's retrievals are mostly source-hunt and pattern-recognition. Search is the primary access pattern. | Flat or shallow structure; rely on full-text search; minimal taxonomy. |
| **Project-folders + reference-folder + linking** | User has all five retrieval modes and the work benefits from cross-references. | Add a third layer: explicit links between current-project notes and reference items. Tags allowed *only if a tag passes the use-it-twice rule* (Step 3). |

Pick one. Do not invent a fourth. If the user has a current system in place that's working, do not redesign — name what's working and apply only the minimum changes.

### Step 3 — Apply the use-it-twice rule for any feature

Any structural feature (a tag, a folder, a template, a metadata field, a sub-database) must be justified by *at least two retrieval cases* in the last 90 days. Otherwise, it's aspirational structure and goes in the cut list.

Build the cut list explicitly: existing tags, folders, or structures from input 7 that don't meet the rule. Most users have a 30–60% reduction available here.

### Step 4 — Define retention rules

Retention determines what stays and what gets archived/deleted. Default rules:

- **Reference items:** kept until proven irrelevant. No automatic deletion.
- **Project notes:** archived 60 days after the project closes.
- **Meeting notes:** kept 90 days unless a specific decision or commitment made them important; the important ones are extracted into the reference layer at the end of each project.
- **Reading highlights:** the prompt explicitly recommends *not* keeping every highlight — keep ones the user re-encounters in writing or thinking. Otherwise: archive after 90 days of no retrieval.
- **Ideas:** ideas not acted on within 6 months are archived. Most ideas are not acted on; this is fine.

Adjust to the user's input 5 tolerance, but bias toward shorter retention than the user's first instinct. Hoarding is the dominant PKM failure mode.

### Step 5 — Define link rules (only if Architecture #3)

If using linking, the rules are:

- **Link only when the link will be traversed.** A link no one follows is taxonomic noise.
- **Forward links are higher value than backlinks** for personal use. Forward = current note → reference. Backlink autopopulation is impressive but rarely retrieved.
- **Linking is its own work.** If the user budgets [N] minutes/week for system maintenance and linking is taking > 25% of that budget, scope down. Most personal PKMs over-link.

### Step 6 — Address the failed retrieval (input 8)

For input 8 (specific retrieval that should have happened), answer:

- Is it actually in the system? (Often it isn't — never captured.) If never captured, that's a capture problem; route to `bottleneck_capture_triage_system_design.md`.
- If it's there, why couldn't it be found? Naming, structure, search strategy, item buried in the wrong layer.
- Fix the *findability* of similar items going forward. Often the fix is a one-time renaming pass on a specific category.

### Step 7 — Define the 90-day usefulness check

The system is succeeding at day 90 if:

- The user has retrieved at least [target count, sized to input 2's baseline]: usually 3× the prior 90 days' retrieval count if starting from a low base, or holding/growing if already retrieving regularly.
- At least one retrieval in the 90 days served high-leverage work (a decision, a writing piece, a code change, a conversation).
- Maintenance time stayed within the input 6 budget.
- The cut list (Step 3) was actually executed.

If after 90 days retrievals haven't grown, the architecture is the wrong shape — re-run with new retrieval data, not by adding more structure.

### Step 8 — Refuse the cargo-culting

Close with explicit refusal:

- This prompt does not import GTD, PARA, BASB, Zettelkasten, or any branded framework wholesale. Patterns can be borrowed; dogma cannot.
- This prompt does not produce a "complete knowledge system." Personal knowledge management is local, idiosyncratic, and retrieval-driven.
- This prompt does not promise that more capture produces more retrieval. The opposite is often true: less, better-organized capture often retrieves more.

---

## Constraints

### Must
- Build the retrieval map *before* the architecture.
- Pick exactly one of the three architectures.
- Apply the use-it-twice rule to every structural feature; produce a cut list.
- Define retention rules with bias toward shorter retention than user's first instinct.
- If linking, apply the link rules; otherwise omit links entirely.
- Address input 8 with a specific findability fix.
- Define the 90-day usefulness check with concrete numbers.

### Must Not
- Recommend a specific app or tool. (User's existing tool stays unless it's the binding constraint, in which case state that.)
- Import a branded framework wholesale.
- Add tags or fields beyond the use-it-twice rule.
- Recommend "capture more." Capture without retrieval is the failure pattern.
- Promise a system that "frees your mind." Goal is high-leverage retrieval, not psychological state.

---

## False-Positive Prevention

1. **Don't design for the retrievals the user wishes they were doing.** Design for the retrievals that actually happen, scaled. Aspirational retrievals justify aspirational structure that goes unused.
2. **Don't add structure to compensate for capture failure.** If the user "captured but can't find," the issue is sometimes capture quality, not retrieval architecture.
3. **Don't accept "I want to keep everything forever."** Probe input 5 with: of items captured 12 months ago, how many have been retrieved? The answer is almost always low. Adjust retention accordingly.
4. **Don't recommend a tool migration as the fix.** Tool migrations consume the maintenance budget for ≥ 30 days and rarely change retrieval patterns.
5. **Don't link prolifically.** A backlink that never gets traversed is overhead. Force the use-it-twice rule on links too.
6. **Don't conflate this prompt with `bottleneck_capture_triage_system_design.md`.** That one is the inbox / triage / decision-rule system. This one is the reference / retention / retrieval layer. They cooperate but solve different problems.
7. **Don't recommend a PKM at all if input 2 and input 3 are empty.** State: the user doesn't have evidence of need. Better to refuse than to design aspirational structure.

---

## Output Format

```
## Retrieval map
| Retrieved (or wished) | Work served | How retrieved | Frequency |
|---|---|---|---|

## Retrieval modes used (ranked)
1. ...
2. ...
...

## Architecture
**Pattern:** Project + reference / Plaintext + search / Project + reference + linking
**Why:** [one sentence based on retrieval modes]

## Use-it-twice rule — cut list
| Existing structure (from input 7) | Justified by ≥ 2 retrievals? | Decision (Keep / Cut) |
|---|---|---|

## Retention rules
- Reference: ...
- Project notes: ...
- Meeting notes: ...
- Reading highlights: ...
- Ideas: ...

## Link rules (if Architecture #3)
[Rules; or "linking not used in this architecture."]

## Failed retrieval (input 8) — fix
**Was the item captured?** [Yes / No]
[If yes: findability fix.]
[If no: route to `bottleneck_capture_triage_system_design.md`.]

## 90-day usefulness check
- Retrievals: target [N] (vs. baseline [N₀])
- ≥ 1 high-leverage retrieval
- Maintenance time within [N] min/week budget
- Cut list executed (Y/N)

If retrievals haven't grown at day 90: architecture is wrong shape — re-run with new retrieval data, not more structure.

## What this prompt is not doing
- Not importing a branded framework
- Not recommending a tool change
- Not promising a "complete knowledge system"
- Not recommending more capture
```

---

## Verification

- [ ] Retrieval map built before architecture.
- [ ] Architecture chosen from the three options with justification.
- [ ] Use-it-twice rule applied; cut list produced.
- [ ] Retention rules defined with shorter-than-instinct bias.
- [ ] Link rules applied only if Architecture #3.
- [ ] Input 8 (failed retrieval) addressed with findability fix or capture referral.
- [ ] 90-day usefulness check stated as concrete numbers.
- [ ] No tool migration recommendation as primary fix.
- [ ] No branded framework imported wholesale.
