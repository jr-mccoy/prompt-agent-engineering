---
title: "Audit a Work Week Against Coordination-Tax Categories"
category: personal-development/career-transformation
description: "Classify each recurring block on a real calendar week into coordination-tax categories (status, alignment, approval, translation, rework, triage) so the user can see how much of their week is coordination rather than production work — and which categories are automatable, delegatable, or structurally load-bearing."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - career
  - coordination-tax
  - work-audit
  - automation
  - role-design
updated: "2026-04-21"
related_prompts:
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
---

# Audit a Work Week Against Coordination-Tax Categories

**Objective:** Given a real calendar week plus the user's own description of the non-calendared work that filled it, classify every block into a fixed taxonomy of coordination-tax categories and output a honest split between production time and coordination time — with the specific coordination categories that dominate.

**When to use:**
- The user feels "busy but not productive" and wants an evidence-based read on why
- The user is evaluating whether their role is structurally vulnerable to automation and needs a baseline of how their time actually goes
- The user is about to propose a role redesign or team restructure and needs a defensible picture of where the time goes
- The user is a manager or IC preparing a repositioning plan (see `career_90_day_repositioning_plan.md`)

**Don't use when:** The user cannot or will not share an actual week's calendar + task reality. This prompt refuses to operate on imagined or "typical" weeks — the whole point is to force contact with real data.

**Audience:** An individual knowledge worker auditing their own time, or a manager auditing their own week before asking their team to do the same.

---

## Inputs Required

The user MUST provide all of the following. If any are missing, ask once, then stop — do not fabricate.

1. **The calendar week.** Pasted as a list of blocks with: day, start–end, title, attendees (count is enough), whether the user ran it or attended, and whether it recurred.
2. **Non-calendared time.** The work that filled the gaps between meetings: what the user actually did in Slack/email/docs/code/tickets during each workday. Rough blocks are fine.
3. **Role + level.** One sentence each. (e.g., "Staff PM on a platform team, 8 years in.")
4. **What "production work" means for this role.** One sentence defining the output the role is ultimately judged on (shipped feature, closed deal, published report, merged PR, clinical decision, etc.).
5. **Anything the user suspects is coordination tax but isn't sure about.** Optional; used as a tie-breaker during classification.

If the week shown is unusually atypical (vacation, onboarding, launch week), ask the user to confirm whether to proceed or pick a more representative week.

---

## Instructions

### Step 1 — Normalize the week

Re-render the week as a flat list of blocks, including non-calendared work. Merge contiguous blocks only if they share a category and context. Time unaccounted for (gaps, bathroom, lunch, DM scroll) stays labeled as "unaccounted" and is reported separately — do not silently redistribute it.

### Step 2 — Classify every block into exactly one category

Use only this taxonomy. If two categories plausibly fit a block, pick the one earliest in the chain (status ≺ alignment ≺ approval ≺ translation ≺ rework ≺ triage ≺ production ≺ learning ≺ unaccounted).

| # | Category | Definition | Examples |
|---|----------|------------|----------|
| 1 | **Status** | Communicating what has happened or will happen, without changing a decision. | Standups, status updates, written weeklies, recap emails, ticket hygiene. |
| 2 | **Alignment** | Getting multiple humans to agree on scope, direction, or priority. | Roadmap debates, stakeholder syncs, pre-meetings for meetings. |
| 3 | **Approval** | Asking for or granting permission the work needs to proceed. | Review meetings, sign-off chains, PR approval, procurement gates. |
| 4 | **Translation** | Converting the same content across audiences or formats. | Exec deck from IC doc, customer-facing from internal spec, same update rewritten for three channels. |
| 5 | **Rework** | Redoing work because a prior step was misaligned, misunderstood, or skipped. | Second draft after exec feedback, re-scoping after missed requirement, retesting after late input change. |
| 6 | **Triage** | Deciding what to work on or responding to interruptions before doing the work. | Inbox zero passes, Slack triage, on-call paging, prioritization meetings. |
| 7 | **Production** | The output the role is judged on, per the user's definition in input 4. | Shipped code, closed deal, written report, clinical encounter, merged PR. |
| 8 | **Learning** | Deliberate skill or domain input clearly separable from production. | Tutorials, reading a spec to understand it, a scoped prototype to learn a tool. |
| 9 | **Unaccounted** | Gaps the user couldn't reconstruct. Reported separately; never reassigned. | — |

Do not invent new categories. If a block genuinely doesn't fit (e.g., personal medical appointment), mark as "non-work" and exclude it from percentages.

### Step 3 — Assign each block two attributes

For every block in categories 1–6 (coordination tax), assign:

- **Automatability:** High / Medium / Low. High = an LLM or simple automation can do 80%+ of this block today. Low = the block is load-bearing on human judgment or politics.
- **Delegatability:** High / Medium / Low. High = a competent peer could do this block with the information the user has. Low = only this person in this role can do this block.

Do NOT collapse these into one score. Automatable ≠ delegatable (a decision meeting may be high-delegatable, low-automatable; a status summary may be high-automatable, low-delegatable if the user hears something live).

### Step 4 — Compute the split

- Total week hours (working hours only).
- Hours + % in each category.
- Hours + % in coordination tax (categories 1–6) vs production (7) vs learning (8) vs unaccounted (9).
- Largest coordination category and its share.
- High-automatability coordination hours.
- Low-automatability, low-delegatability hours — these are the structural core.

### Step 5 — Flag the three honest signals

1. **Ratio check.** If coordination tax > 60% of working hours, call it out. Do not soften.
2. **Dominance check.** If one category is > 50% of coordination tax, name it as the dominant tax.
3. **Core check.** Report how many hours fell into low-automatability + low-delegatability. This is the hours the user is structurally uniquely positioned for. If that number is < 5 hours across the whole week, say so plainly.

### Step 6 — Output, then verify

Produce the output in the format below. Then run the verification checklist at the end and fix anything that fails before delivering.

---

## Constraints

### Must
- Classify every block into exactly one taxonomy category.
- Use the user's own definition of production work (input 4). Do not substitute your own.
- Report unaccounted time separately, never reassign it.
- Report automatability and delegatability as two independent dimensions.
- State the three honest signals (ratio, dominance, core) even if uncomfortable.

### Must Not
- Invent new categories.
- Generate an "ideal" week or prescribe what the user should cut. A separate prompt does that.
- Use benchmarks ("most ICs spend X% on meetings") — the user's own data is the only evidence.
- Smooth over gaps by spreading unaccounted time across categories.
- Advise career moves. This prompt audits; it does not prescribe.
- Claim anything about the user's performance or value — only about time allocation.

---

## False-Positive Prevention (MUST follow)

**Don't confuse:**

❌ **DON'T:**
- Treat every meeting as coordination tax. A design review that produces a shipped artifact is production; a design review that only aligns opinions is alignment. Classify by what came out, not by form.
- Call translation "rework." Translation is planned reformatting across audiences; rework is re-doing work because a prior step failed.
- Grade automatability based on whether a tool exists. Grade based on whether, given the inputs the user actually has in that block, a current LLM + basic tooling could produce the output the user produced.
- Mark 1:1s as status by default. If the 1:1 produced a decision or unblocked work, it's alignment or approval.
- Conflate delegatable with "should delegate." The question is whether it could be delegated with the information the user currently holds, not whether delegation is politically feasible.

✅ **DO:**
- Re-read the block's actual output before classifying.
- When in doubt between two categories, pick the earlier one in the chain and note the runner-up.
- Quote the user's own block description verbatim when the classification might look wrong.
- Treat unaccounted time as real data — its size is itself a finding.
- Call out blocks where the user's own description contradicts the category suggested by the title (e.g., a "standup" that's really a decision meeting).

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Audit looks rigorous but is fabricated — filling in hours the user didn't describe, inferring meeting contents, or inventing a "typical week." This produces a confident-sounding report based on nothing.

❌ **UNHELPFUL failure:** Refuses to classify when inputs are messy, or hedges every block as "could be anything." The user has no more clarity than before.

✅ **Quality check:** A senior operator reading this report could point to any single classification and ask "why this category?" and get an answer grounded in the block's actual content.

---

## Output Format

```markdown
# Coordination-Tax Audit — Week of [dates]

## Summary
- Total working hours audited: [N]
- Production time: [N h, P%]
- Coordination tax (cats 1–6): [N h, P%]
- Learning: [N h, P%]
- Unaccounted: [N h, P%]

## Three Honest Signals
1. **Ratio:** Coordination tax is [N%] of working hours. [Above/below 60% threshold.]
2. **Dominance:** [Category] is [N%] of coordination tax. [Dominant tax / no dominant category.]
3. **Core:** [N] hours this week were low-automatability AND low-delegatability. [Assessment.]

## Per-Block Classification
| Day | Block | Hours | Category | Automatability | Delegatability | Notes |
|-----|-------|-------|----------|----------------|----------------|-------|
| Mon | [title] | 1.0 | Alignment | Medium | High | Runner-up: Status |
| ... | ... | ... | ... | ... | ... | ... |

## Category Totals
| Category | Hours | % of week | Avg automatability | Avg delegatability |
|----------|-------|-----------|--------------------|--------------------|
| Status | | | | |
| Alignment | | | | |
| Approval | | | | |
| Translation | | | | |
| Rework | | | | |
| Triage | | | | |
| Production | | | | — |
| Learning | | | | — |
| Unaccounted | | | — | — |

## Notable Blocks
- **Quoted block → actual category:** [block description] → classified as [category] because [reason rooted in the block's described output].
- [2–4 entries where classification was non-obvious]

## Open Questions Raised by the Data
- [Things the user should clarify in a future audit, e.g., "3 recurring meetings had no described output — is the output in a channel we didn't capture?"]
```

---

## Verification

Run this checklist before delivering; fix any failures.

- [ ] Every block has exactly one category.
- [ ] Unaccounted time is reported separately, not reassigned.
- [ ] Automatability and delegatability are two independent scores per block.
- [ ] The three honest signals are stated even if they contradict what the user seems to want to hear.
- [ ] No block classification is based on title alone — each has a described output or explicit uncertainty.
- [ ] No career advice, role recommendations, or "ideal week" content.
- [ ] Production category uses the user's definition from input 4.
- [ ] Totals reconcile to the week's working hours.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** The goal is a categorized week split, not a productivity lecture. Output is diagnostic, not prescriptive.
- **ST-02 (Structured Sequential Instructions):** Six explicit steps from normalize → classify → attribute → compute → flag → verify.
- **CM-02 (Constraint Specification):** Must / Must Not blocks the most common failure: fabricating hours or smoothing gaps.
- **DS-01 (Framework Application):** The 9-category taxonomy is the framework; disallowing invented categories is what makes it load-bearing.
- **QA-01 (Self-Verification):** Verification checklist runs before delivery; every block must tie to described output.
