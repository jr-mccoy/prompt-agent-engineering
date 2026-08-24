---
title: "Deep Four-Discipline Diagnostic with a Multi-Month Development Roadmap"
category: prompt-engineering/skill-development
description: "A deeper, evidence-based diagnostic across the four AI-work disciplines (prompt craft, context, intent, specification) that produces a sequenced 3–6 month development roadmap with checkpoints, artifacts to produce, and exit criteria per discipline. For users who've already run the rapid diagnostic twice and haven't moved."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - skill-development
  - diagnostic
  - roadmap
  - four-disciplines
  - deliberate-practice
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_rapid_four_discipline_diagnostic.md
  - domain-prompt-engineering/skill-development/promptcraft_personal_context_document.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
  - domain-prompt-engineering/skill-development/promptcraft_constraint_architecture_design.md
---

# Deep Four-Discipline Diagnostic with a Multi-Month Development Roadmap

**Objective:** Produce a 3–6 month, evidence-based development roadmap across the four AI-work disciplines — prompt craft, context management, intent clarity, and specification — with: sequenced focus per discipline, specific artifacts to produce, checkpoints, and an exit criterion for moving on. This is the deliberate-practice version of the rapid diagnostic; it's slower, needs real evidence, and returns a plan the user will actually work against for months.

**When to use:** The user has run `promptcraft_rapid_four_discipline_diagnostic.md` at least twice — and at least once the weakest discipline didn't change. The shallow diagnostic has stopped producing movement. Or: the user is willing to invest a real practice block (several hours a week for 3+ months) and wants a plan.

**Audience:** Individuals committed to leveling up as AI operators, not casual users. Expect to spend ~90 minutes on this diagnostic.

---

## Inputs Required

1. **A corpus of at least 10 recent chats or AI-assisted work artifacts** from the last 30 days, representing a mix of task types the user actually does. Not curated best-of; a real sample.
2. **A list of the user's most common task types** (e.g., "draft memos," "refactor code," "research a topic," "analyze a decision").
3. **At least three dissatisfying outputs.** Ideally labelled with what went wrong.
4. **The two most recent rapid-diagnostic results** (from `promptcraft_rapid_four_discipline_diagnostic.md`) — to compare claimed weakness against observed evidence.
5. **Time budget per week** the user will commit to deliberate practice (floor: 2 hours/week; below that, route to the rapid diagnostic).

Refuse to produce a roadmap without real chat evidence. A user who can't produce 10 real artifacts hasn't worked with AI enough to benefit from a 3–6 month plan. Send them to run AI-assisted work for a month and come back.

---

## Instructions

### Step 1 — Evidence-based scoring (not self-report)

Score each discipline 0–3 based on the 10+ real artifacts, not on how the user feels about their skill.

**Prompt craft evidence:**
- How often did prompts specify output format? (Count across the 10.)
- How often did prompts name "done" explicitly?
- How often did the user have to send a second message clarifying what they meant?
- Median prompt length. (Too short is usually prompt-craft weakness; too long without structure is also weakness.)

**Context management evidence:**
- How often was a file / codebase / doc pasted or attached when the task depended on it?
- How often did the model ask for information the user already had?
- Does the user have any persistent memory set up (CLAUDE.md, custom instructions, project context)?
- How often did answers come back confidently wrong about something the model couldn't have known?

**Intent clarity evidence:**
- How often could the task outcome be stated in one sentence before prompting?
- How often did the user accept the first plausible answer and only later realize it wasn't what they needed?
- How often did task scope change mid-chat?
- How often did "help me with X" show up as the opener?

**Specification evidence:**
- How often did prompts contain an observable criterion?
- Average iteration count before accepting an output.
- Was there a stop rule?
- How often did the user say "that's not quite right" without being able to say specifically what was wrong?

Score each discipline 0 (evidence is mostly negative) / 1 / 2 / 3 (evidence is mostly positive).

### Step 2 — Compare to rapid-diagnostic self-report

Where the deep score and the user's rapid-diagnostic self-report diverge, the deep score wins, and the divergence itself is a finding. A user who thinks prompt craft is their strength but scored 0 on evidence has a calibration problem as well as a skill problem; note this in the roadmap.

### Step 3 — Rank disciplines by leverage, not just score

A discipline scoring 0 isn't automatically the first priority. Rank by leverage:

1. **Specification (0 or 1):** Highest leverage. Every other discipline's gains leak out through weak specification. Fix first.
2. **Intent clarity (0 or 1):** Next highest. Prompt craft and context are waste motion if the user isn't sure what they want.
3. **Context management (0 or 1):** Moderate leverage. Fix once specification and intent are at 2+.
4. **Prompt craft (0 or 1):** Lowest leverage, easiest to fix. Usually improves by itself as the other three improve.

This ordering holds even if prompt craft scores lowest on evidence. Practicing prompt craft on top of weak intent is the single most common wasted-practice pattern.

### Step 4 — Build the sequence

Group the plan into 3 phases, each 4–8 weeks, targeting one (primary) + one (secondary) discipline per phase.

**Phase 1 (weeks 1–6): Primary = lowest-leverage discipline at score 0 or 1.**
**Phase 2 (weeks 7–14): Primary = next, per the leverage ranking.**
**Phase 3 (weeks 15–24): Primary = the last remaining weak discipline, OR — if all four are at 2+ — consolidation across the user's most common task types.**

If the user has only one discipline below 2, Phases 2 and 3 become consolidation and eval-harness work.

### Step 5 — Fill each phase with artifacts, not topics

For each phase, produce:

- **One primary artifact to build by end of phase.** Examples:
  - Specification phase: an eval harness for the user's top task type.
  - Intent phase: a written outcomes-log for the user's top 5 task types.
  - Context phase: a personal context document plus a CLAUDE.md.
  - Prompt-craft phase: a library of 5 reusable prompts for the user's top task types.
- **A practice cadence.** E.g., "three tasks/week run through `promptcraft_pre_ai_thinking_exercise.md` before prompting."
- **A checkpoint at week 3** to catch phases going sideways.
- **An exit criterion.** Evidence-based: e.g., "When 8 of 10 next prompts have an observable done criterion, move to Phase 2."

Vague phases ("work on prompt craft") don't produce movement. Artifact-based phases do.

### Step 6 — Wire in the failure modes

For each phase, name the two most likely ways this phase fails and what to do if they happen.

Common failure modes:
- **Tool-proliferation.** User reads lots about prompting and practices little. Cap reading; raise artifact count.
- **Practice on hypothetical tasks.** Practice must be on real work. If the user runs out of real work, the phase is too long.
- **Moving on before exit criterion.** The roadmap isn't a schedule; it's a dependency graph. Don't start Phase 2 until Phase 1's exit criterion is met.
- **Invisible progress.** Run the rapid diagnostic at each checkpoint; if it still names the same weakness, the plan isn't working — escalate.

### Step 7 — Set the total-plan re-check

A 3–6 month roadmap needs a hard check at the midpoint and at the end. At each:
- Re-run this deep diagnostic.
- Compare discipline scores against the plan's targets.
- If reality diverges from plan by more than 25%, rebuild from Step 1, don't patch.

### Step 8 — Name what's out of scope

State what the roadmap is *not* trying to fix: e.g., not a domain-skill roadmap; not a roadmap for model selection or tool selection; not a roadmap for team-level AI adoption. Scope creep on a skill-development plan is the #1 reason these plans collapse.

---

## Constraints

### Must
- Use 10+ real recent artifacts. No hypotheticals.
- Score each discipline 0–3 on evidence, not self-report.
- Rank by leverage, not by score alone (Specification > Intent > Context > Prompt craft).
- Produce 3 phases, each with a primary artifact and an evidence-based exit criterion.
- Run a rapid re-check at each phase boundary.

### Must Not
- Start a multi-phase plan for a user committing less than 2 hours/week.
- Recommend a roadmap built from reading goals ("read 3 articles on prompt engineering"). Artifacts only.
- Treat prompt craft as Phase 1 priority when specification or intent is also weak.
- Allow phases longer than 8 weeks. Beyond 8 weeks without a checkpoint, the plan silently rots.

---

## False-Positive Prevention

1. **Scores that mirror the rapid diagnostic exactly.** If the deep score matches the self-report exactly, the deep version isn't using evidence — it's inheriting the self-report. Force the reviewer to cite specific chats per discipline.
2. **A phase with no artifact.** If a phase's primary deliverable is "practice more X," the phase won't produce movement. Every phase needs an artifact.
3. **Exit criteria that can be waved through.** "Feels stronger" is not an exit criterion. Exit criteria must be observable: "8 of the next 10 prompts have a specific done criterion."
4. **A roadmap longer than the user's commitment can sustain.** Don't produce a 6-month plan for 1 hour/week. The plan will fail and the user will conclude they're bad at practice. Match the plan to the time budget.
5. **Refusing to name what the roadmap doesn't do.** If Step 8 is skipped, the plan will be blamed for failing at things it was never supposed to do.
6. **Using this on a user who hasn't run the rapid diagnostic twice.** The deep diagnostic is for users where the rapid version stopped moving. Before that, it's expensive overkill.

---

## Output Format

```markdown
## Evidence audit
- Artifacts reviewed: [N] (floor: 10)
- Task types represented: [...]
- Dissatisfying outputs analyzed: [N] (floor: 3)
- Weekly time budget: [hours]

## Evidence-based scores (0–3)
| Discipline | Score | Evidence cited |
|---|---|---|
| Prompt craft | [...] | [...] |
| Context management | [...] | [...] |
| Intent clarity | [...] | [...] |
| Specification | [...] | [...] |

## Divergence from rapid diagnostic
[Where deep scores and self-report diverged. Note calibration findings.]

## Leverage ranking (which to fix first)
1. [...] — reason.
2. [...] — reason.
3. [...] — reason.
4. [...] — reason.

## The roadmap

### Phase 1 (weeks 1–X): Primary = [...], Secondary = [...]
- Primary artifact: [specific artifact]
- Practice cadence: [specific count and rhythm]
- Checkpoint at week 3: [what to check]
- Exit criterion: [observable, measurable]
- Likely failure modes: [...]

### Phase 2 (weeks Y–Z): [...]
[Same structure.]

### Phase 3 (weeks A–B): [...]
[Same structure.]

## Midpoint and end re-checks
- Midpoint (date): re-run deep diagnostic. Criteria for adjusting plan.
- End (date): re-run deep diagnostic. Criteria for closing or extending.

## Out of scope for this roadmap
[What this plan explicitly isn't trying to improve.]
```

---

## Verification

- [ ] 10+ real artifacts were reviewed; no hypotheticals.
- [ ] Scores are evidence-cited per discipline.
- [ ] Divergence from rapid self-report was examined and noted.
- [ ] Disciplines are ranked by leverage, not raw score.
- [ ] Each phase has one primary artifact and an observable exit criterion.
- [ ] Each phase has named failure modes and a midpoint checkpoint.
- [ ] Plan length matches the user's stated time budget.
- [ ] "Out of scope" section is present and specific.
