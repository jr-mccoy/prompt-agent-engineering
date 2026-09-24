---
title: "Release Notes Writer — One Change Inventory, a Customer Variant and an Internal Variant That Agree"
category: product-management/prompts
description: "Turn a release's change list into two consistent documents from one classified inventory: user-facing notes written as what the reader can now do, with breaking changes and required actions first and nothing that is still behind a partial rollout, and internal notes for support, sales and success with affected segments, rollout state, expected questions and workarounds — distinct from the changelog-automation skill (developer changelogs generated from commits) and product_launch_readiness_gate (whether to ship)."
techniques:
  - NE-14
  - RP-02
  - OC-04
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - release-notes
  - product-communication
  - changelog
  - customer-communication
  - internal-enablement
  - rollout
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/developer-tools/changelog-automation/SKILL.md
  - domain-product-management/prompts/product_launch_readiness_gate.md
  - domain-product-management/prompts/product_feature_sunset_decision.md
---

# Release Notes Writer

**Objective:** Write release notes that customers read and support teams can rely on.
Build one classified inventory of what changed, then produce two variants from it: a
user-facing version in terms of what the reader can now do, and an internal version
covering who is affected and what they will ask. The two must never contradict each
other. Notes that list ticket titles, announce features the reader cannot yet see, or
bury a breaking change are refused.

**When to Use:**
- A release is going out and the notes are currently a list of ticket titles.
- Support learns about changes from customers.
- A behaviour change shipped last month and customers found out from a broken workflow.

**Distinct from:**
- `../../domain-agentic-resources/skills/developer-tools/changelog-automation/SKILL.md` —
  generating developer changelogs from commits (Keep a Changelog, semantic-release). Its
  output can be this prompt's input. This prompt writes for customers and customer-facing
  staff.
- `product_launch_readiness_gate.md` — decides whether to ship. These notes are one input
  to marketing's and support's readiness there.
- `product_feature_sunset_decision.md` — decides whether to remove something. This prompt
  announces a removal after that decision.
- For a launch *announcement* (blog post, email campaign), use
  `../../domain-agentic-resources/skills/marketing/copywriting/`.

---

## Inputs

1. **The change list**: tickets, PRs or a generated changelog.
2. **Rollout state per change**: 100%, a percentage, a flag, specific plans or segments.
3. **Audience**: who reads the user-facing notes (admins, end users, developers via API).
4. **Known issues** shipping with the release.
5. **House style and length**, if any.

---

## Method

1. **Classify every change into one inventory (CM-02).** For each item, record:
   - **Type:** new, improved, fixed, changed behaviour, deprecated/removed, or internal only.
   - **Visible to:** all users, some plans or segments, or nobody.
   - **Rollout:** 100% or partial.
   - **Action required:** does the reader have to do anything?
   Nothing is written until every change is classified.

2. **Filter per variant (OC-04).**
   - **User-facing:** only changes visible to the reader *and* at 100% for them.
     Internal-only and partially rolled-out items are excluded.
   - **Internal:** every customer-affecting change, including partial rollouts, plus a
     one-line list of what was deliberately excluded and why.

3. **Order by consequence.** Put breaking changes and required actions first, then
   deprecations, then new, improved and fixed. A reader who stops after three lines must
   already know anything that could break their work.

4. **Write the user-facing entries (RP-02).** Lead each with what the reader can now do
   or no longer has to do. Use the reader's vocabulary, not internal names. For fixes,
   describe the symptom they saw, not the cause. For changed behaviour, say what was true
   before, what is true now, and what to do. One or two sentences per entry.

5. **Write the internal entries (NE-14).** For each item: what changed; who is affected
   (plans, segments, integrations); rollout state and when it reaches 100%; the question
   support will get and the answer; any workaround; and the owner to escalate to.

6. **Cross-check the variants (QA-01).** Every user-facing entry appears in the internal
   notes with the same facts. Nothing in the user-facing notes is partial. Every
   changed-behaviour or removal entry has an action or an explicit "no action needed".

---

## Output Format

```markdown
## Release [version] — [date]

### Inventory
| # | Change | Type | Visible to | Rollout | Action required | User notes? | Internal notes? |
|---|---|---|---|---|---|---|---|

### User-facing notes
**Action needed** (if any)
- [changed behaviour or breaking change: before → now → what to do]
**New**
- [what you can now do]
**Improved** · **Fixed** (symptom you saw)
**Known issues**

### Internal notes
| Change | Who is affected | Rollout (100% by) | Expected question → answer | Workaround | Escalate to |
|---|---|---|---|---|---|
Excluded from user notes: [item — reason]
```

---

## Verification

- [ ] Every change in the source list is classified in the inventory
- [ ] The user-facing notes contain nothing that is partially rolled out or internal only
- [ ] Breaking changes and required actions come first
- [ ] Every entry leads with a reader outcome, not a ticket title or internal name
- [ ] Fixes describe the symptom, not the cause
- [ ] Changed-behaviour entries state before, now and action
- [ ] Every user-facing entry appears in the internal notes with identical facts
- [ ] Internal notes carry rollout dates, expected questions and an escalation owner
- [ ] Excluded items are listed internally with reasons

## False-Positive Prevention

1. **Do not announce what the reader cannot see.** A feature at 25% rollout in public
   notes generates tickets from the 75% who cannot find it.
2. **Ticket titles are not notes.** "FE-2231 refactor invoice list" means nothing to a
   customer. If you cannot state a reader outcome, the item belongs in internal notes or
   nowhere.
3. **"Improved performance" with no noticeable effect is noise.** Include performance
   work only when the reader would notice, and say where.
4. **A behaviour change is not a fix.** If anyone relied on the old behaviour, classify it
   as changed behaviour and say what to do, even if the old behaviour was a bug.
5. **Do not hide known issues.** Stating one in the notes costs less than handling the
   tickets it would otherwise generate.
6. **Do not let the variants drift.** Edit the inventory, then regenerate both variants.
   Editing one variant directly is how contradictions appear.

---

## Example

**Context:** Release 4.12 of an invoicing app. 9 changes in the source list.

| # | Change | Type | Visible to | Rollout | Action | User | Internal |
|---|---|---|---|---|---|---|---|
| 1 | CSV export includes tax column | changed behaviour | all | 100% | update import mappings | yes | yes |
| 2 | Auto-chase reminders | new | Pro plan | 25% flag | — | no | yes |
| 3 | Recurring invoices on custom schedules | new | all | 100% | — | yes | yes |
| 4 | Faster client search | improved | all | 100% | — | yes | yes |
| 5 | Bulk mark-as-paid | improved | all | 100% | — | yes | yes |
| 6 | PDF showed wrong currency symbol for CAD | fixed | all | 100% | — | yes | yes |
| 7 | Duplicate reminder emails | fixed | all | 100% | — | yes | yes |
| 8 | Stripe payouts failing to sync | fixed | Stripe users | 100% | — | yes | yes |
| 9 | Invoice list refactor | internal only | nobody | 100% | — | no | excluded |

User-facing: 7 entries (1, 3–8). Internal: 8 entries (1–8), with #9 listed as excluded.
7 + 1 partial (#2) + 1 internal-only (#9) = 9.

**User-facing, first line:** "**Action needed:** CSV exports now include a Tax column
after Subtotal. If you import exports into accounting software, update your column
mapping."

**Fix entry:** "Invoices in Canadian dollars now show C$ on the PDF instead of $."

**Internal, #2:** Pro plan, 25% of accounts, 100% by 3 Nov. Expected question: "Where is
Auto-chase?" Answer: "Rolling out to all Pro accounts by 3 November." Escalate to the
Billing PM.

---

## Techniques Used

- **NE-14 Multi-Audience Documentation Targeting** — one inventory, two audience variants.
- **RP-02 Audience-Specific Framing** — user entries lead with the reader's outcome in their vocabulary.
- **OC-04 Conditional Output Logic** — rollout and visibility decide which variant an item enters.
- **CM-02 Constraint Specification** — no partial rollouts publicly, no ticket titles, breaking changes first.
- **QA-01 Self-Verification** — the cross-check that the variants agree.

## Related Prompts

- `../../domain-agentic-resources/skills/developer-tools/changelog-automation/SKILL.md` — generated changelogs as input
- `product_launch_readiness_gate.md` — ship decision; notes are one function's readiness evidence
- `product_feature_sunset_decision.md` — the removal decision these notes announce
