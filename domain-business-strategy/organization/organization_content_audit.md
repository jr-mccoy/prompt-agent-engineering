---
title: "Content Audit and Cleanup"
category: business-strategy/organization
description: "Audit a messy workspace, folder, or knowledge base and produce a prioritized cleanup plan — recommending keep / update / merge / archive / delete for each item, with conservative defaults and evidence-linked recommendations."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - organization
  - content-audit
  - knowledge-management
  - cleanup
  - workspace
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/organization/organization_knowledge_base_gap_analysis.md
  - domain-business-strategy/organization/organization_project_status_summary.md
  - domain-business-strategy/research/research_content_research.md
---

# Content Audit and Cleanup

**Objective:** Review the content in a workspace, folder, or database and produce an actionable cleanup plan that reduces clutter while preserving valuable information, with a recommendation and reason for every item.

**When to use:**
- Annual or periodic workspace/knowledge-base cleanup.
- Preparing a workspace for onboarding new team members.
- Information-architecture reviews where clutter is hurting findability.
- Consolidating overlapping or duplicate documentation.

**When NOT to use:**
- You cannot access the actual content (titles alone are not enough to judge).
- The content is regulated/records-retention-bound — deletion decisions need a compliance owner, not an audit prompt.
- A single document needs editing, not a portfolio-level cleanup.

**Audience:** Knowledge managers, ops leads, team admins, and individuals maintaining a personal or team workspace.

---

## Inputs / Context

The user should supply (or the audit should flag what is missing):

1. **Scope:** the workspace, folder, or database to audit, and what to include vs. ignore (e.g., skip archive, templates).
2. **Staleness threshold:** the timeframe after which untouched content is a review candidate (e.g., 6 months, 1 year).
3. **Access:** confirmation the auditor can actually open and read the items.
4. **Context on purpose:** who uses this content and why (helps judge "active" vs. "abandoned").
5. **Risk tolerance:** any content that must never be deleted (sole records, externally-linked pages).

---

## Constraints

### Must
- Base every recommendation on **actual content review**, not just the page/file title — and link to each item referenced.
- Give every item a **state** (Active / Outdated / Abandoned / Unknown) and a **recommendation** (Keep / Update / Merge / Archive / Delete) with a one-line reason.
- Default **conservatively**: when torn between archive and delete, recommend archive; never recommend deleting the only record of something.
- **Prioritize** the cleanup into a sequenced order (quick wins → high-impact updates → merges → archive sweep).
- Flag items that couldn't be accessed or understood with `[NEEDS REVIEW]`, and note a confidence level per recommendation.

### Must Not
- Recommend deleting content that may be externally linked or the sole record of something.
- Treat age alone as sufficient reason to delete (old ≠ worthless).
- Present a flat list with no prioritization or merge guidance.
- Fabricate item contents, dates, or purposes that weren't observed.

---

## Instructions

1. **Confirm scope and access.** State what's included, what's ignored, and the staleness threshold. Note anything you couldn't access as `[NEEDS REVIEW]`.
2. **Summarize the corpus.** Total items, oldest/newest/median last-updated dates, content types found.
3. **Assess each item.** Build a table: name (linked), last updated, content type, apparent purpose, state, recommendation, reason, action required. Base each on opened content.
4. **Cluster merge candidates.** Group items covering the same topic; pick the canonical version and specify what to pull from each.
5. **Separate archive vs. delete.** Archive: outdated-but-referential, time-specific-but-complete, untouched past threshold. Delete: truly empty, exact duplicates, abandoned no-value drafts.
6. **List update priorities.** Active references with stale info, important pages with broken links/missing context.
7. **Sequence the cleanup.** Quick wins → high-impact updates → merges → archive sweep, with an effort estimate.
8. **Self-check (verification step).** Re-read: is any recommendation based only on a title? Any deletion that risks losing a sole record? Any item assessed without being opened? Confirm `[NEEDS REVIEW]` flags and confidence notes are present.

---

## False-Positive Prevention

❌ **DON'T:**
- Recommend Delete/Archive from the title alone without opening the item.
- State an item is "abandoned" without checking last-edit and references.
- Recommend deleting anything that might be externally linked or a sole record.
- Invent last-updated dates or purposes you didn't observe.
- Deliver an item-by-item list with no prioritized cleanup order.

✅ **DO:**
- Link to every item referenced and base each call on opened content.
- Default to Archive over Delete when uncertain.
- Mark items you couldn't assess with `[NEEDS REVIEW]` and state confidence.
- Be specific in merge guidance (what to keep from each source).
- Give a sequenced cleanup order with an effort estimate so the plan is actionable.

---

## Output Format

```
# Content Audit: [Workspace / Folder / Database]

## Scope & Method
- Reviewed: [...]   | Ignored: [...]   | Staleness threshold: [...]
- Items not accessible: [list, marked [NEEDS REVIEW]]

## Summary Statistics
- Total items reviewed: [...]
- Last updated — oldest / newest / median: [...]
- Content types found: [...]

## Content Assessment
| Item (link) | Last updated | Type | Apparent purpose | State | Recommendation | Reason | Action | Confidence |
|-------------|--------------|------|------------------|-------|----------------|--------|--------|------------|
| ...         | ...          | ...  | ...              | Active/Outdated/Abandoned/Unknown | Keep/Update/Merge/Archive/Delete | ... | ... | H/M/L |

## Merge Candidates
- Topic group: [items] → canonical: [item]; pull from each: [...]

## Archive Candidates
- [Item] — [why archive not delete]

## Delete Candidates
- [Item] — [why safe to delete]

## Update Priorities
- [Item] — [what's stale / broken]

## Suggested Cleanup Order
1. Quick wins: [...]
2. High-impact updates: [...]
3. Merges: [...]
4. Archive sweep: [...]
- Total effort estimate: [...]
```

---

## Example Output

```
# Content Audit: Team Wiki — "Engineering" space (placeholder)

## Scope & Method
- Reviewed: all pages in /engineering   | Ignored: /templates, /archive   | Staleness threshold: 12 months
- Items not accessible: "Legacy Runbook (restricted)" [NEEDS REVIEW]

## Summary Statistics
- Total items reviewed: 38 (placeholder)
- Last updated — oldest 2023-01 / newest 2026-05 / median 2024-09
- Content types found: runbooks, design docs, meeting notes, onboarding guides, drafts

## Content Assessment
| Item (link) | Last updated | Type | Apparent purpose | State | Recommendation | Reason | Action | Confidence |
|-------------|--------------|------|------------------|-------|----------------|--------|--------|------------|
| [On-call Runbook](#) | 2026-05 | runbook | active ops reference | Active | Keep | current, high-traffic | none | H |
| [API v1 Design](#) | 2023-02 | design doc | superseded by v2 | Outdated | Archive | historical value, not current | move to /archive | M |
| [Q3 Planning Notes](#) | 2023-09 | notes | one-time event | Outdated | Archive | complete, time-specific | move to /archive | H |
| [Untitled draft](#) | 2023-04 | draft | empty placeholder | Abandoned | Delete | no content, no links in | delete | H |
| [Onboarding Guide](#) | 2024-03 | guide | new-hire reference | Active | Update | active but mentions retired tools | refresh tool list | H |
| [Setup Notes A / B](#) | 2024-06 | notes | overlapping setup steps | Active | Merge | duplicate topic | merge into canonical "Dev Setup" | M |

## Merge Candidates
- "Dev environment setup": Setup Notes A + Setup Notes B → canonical: new "Dev Setup" page; pull current steps from A, troubleshooting section from B.

## Archive Candidates
- API v1 Design — superseded but useful for history; archive, don't delete.
- Q3 Planning Notes — event complete; archive.

## Delete Candidates
- Untitled draft — empty, no inbound links; safe to delete.

## Update Priorities
- Onboarding Guide — references retired CI tool; high-traffic, refresh first.

## Suggested Cleanup Order
1. Quick wins: delete empty draft; archive Q3 notes.
2. High-impact updates: refresh Onboarding Guide.
3. Merges: consolidate Setup Notes A/B into "Dev Setup".
4. Archive sweep: API v1 Design + other superseded design docs.
- Total effort estimate: ~3–4 hours.
```

---

## Verification

- [ ] Every recommendation based on opened content, not the title alone.
- [ ] Each item has a state, recommendation, reason, and confidence.
- [ ] Every referenced item is linked.
- [ ] Conservative default applied (archive over delete when uncertain).
- [ ] No deletion of potential sole records or externally-linked items.
- [ ] Merge candidates specify canonical version and what to keep from each.
- [ ] Cleanup is sequenced with an effort estimate.
- [ ] Inaccessible items flagged `[NEEDS REVIEW]`.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as producing a prioritized, evidence-based cleanup plan.
- **RT-02 (Multi-Dimensional Analysis Framework):** Assesses each item across state, purpose, recency, and recommendation.
- **DS-02 (Evidence-Based Decision Making):** Requires recommendations to be based on opened content and linked, not assumed from titles.
- **DS-06 (Prioritization and Severity Guidance):** Sequences the cleanup into quick wins, updates, merges, and archive sweep.
- **QA-01 (Self-Critique Triggers):** Final self-check guards against title-only calls and risky deletions.

---

## Related Prompts

- `domain-business-strategy/organization/organization_knowledge_base_gap_analysis.md` — Find what's missing rather than what's cluttered.
- `domain-business-strategy/organization/organization_project_status_summary.md` — Pull scattered docs into a single status snapshot.
- `domain-business-strategy/research/research_content_research.md` — Gather and organize source material for new content.
