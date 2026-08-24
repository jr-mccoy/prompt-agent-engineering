---
title: "Knowledge Base Gap Analysis"
category: business-strategy/organization
description: "Analyze a knowledge base against the processes and questions it should cover, identify documentation gaps (missing, partial, outdated, conflicting, orphaned, hard-to-find), and produce a prioritized plan grounded in actual content review."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - organization
  - knowledge-management
  - gap-analysis
  - documentation
  - findability
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/organization/organization_content_audit.md
  - domain-business-strategy/organization/organization_project_status_summary.md
  - domain-business-strategy/research/research_content_research.md
---

# Knowledge Base Gap Analysis

**Objective:** Compare what a knowledge base *should* cover against what it actually documents, and produce a prioritized list of gaps — missing, partial, outdated, conflicting, orphaned, or hard-to-find content — grounded in real content review and the users' needs.

**When to use:**
- Documentation audits before onboarding or scaling a team.
- Knowledge-management or process-improvement initiatives.
- Diagnosing why people keep asking the same questions or can't find answers.
- Establishing a documentation backlog with priorities.

**When NOT to use:**
- You cannot read the actual content (you'd be guessing from titles).
- You only need to declutter existing content — use the content audit prompt instead.
- The "gaps" are really product gaps, not documentation gaps.

**Audience:** Knowledge managers, ops/enablement leads, team leads, and documentation owners.

---

## Inputs / Context

The user should supply (or the analysis should flag what is missing):

1. **Topic/area** the knowledge base covers and the **sources** to review (folders/databases).
2. **Who uses it** and **why** (primary use cases).
3. **Critical processes/workflows** it should cover (the "should" baseline).
4. **Signals of demand** if available: repeated questions, support tickets, tribal knowledge surfaced in chats/notes.
5. **Decision the analysis feeds:** documentation backlog, onboarding prep, ownership assignment.

---

## Constraints

### Must
- Build the gap assessment against a **stated "should-cover" baseline** (the critical processes + recurring questions), not abstract completeness.
- Base every coverage judgment on **actual content review** (open the pages), link to each page, and date it.
- Classify each topic: **documented (Yes/Partial/No)**, quality (Complete/Needs Update/Stub), and last updated.
- Distinguish **"doesn't exist"** from **"exists but can't be found"** (a findability gap).
- **Prioritize** the top gaps by frequency of need, severity if missing, and effort to create; name a likely owner.
- Flag areas you couldn't fully assess with `[NEEDS REVIEW]` and state overall confidence.

### Must Not
- Judge coverage from page titles alone.
- Invent the existence, content, or dates of documentation.
- Treat theoretical completeness as the goal over real user needs.
- Present a gap list with no priority ranking or ownership.

---

## Instructions

1. **Establish the baseline.** From critical processes and recurring questions, list the topics the KB *should* cover.
2. **Review actual coverage.** For each baseline topic, open the relevant docs and record: exists (Yes/Partial/No), quality, last updated, link (or "Missing").
3. **Identify well-documented areas.** Strong, current sections that could serve as templates.
4. **Catalog the gap types:** critical gaps (no docs), partial docs (what's there vs. missing), outdated content (how stale + risk), conflicting info (which appears more current), orphaned content (exists but disconnected), structural/findability issues (naming, navigation, missing entry points).
5. **Surface tribal knowledge.** Note undocumented knowledge implied by repeated questions or chat/notes references.
6. **Prioritize.** Rank the top 5–10 gaps by need × severity × effort; suggest who could create each and an outline for missing pages.
7. **Self-check (verification step).** Re-read: any coverage call made from a title? Any claimed doc you didn't actually open? Are findability gaps separated from true absence? Confirm `[NEEDS REVIEW]` flags and confidence.

---

## False-Positive Prevention

❌ **DON'T:**
- Declare a topic "missing" without checking whether it exists under another name (findability vs. absence).
- Assess quality from the title without opening the page.
- Invent that a page exists, or guess its content/date.
- Chase theoretical completeness over what users actually need.
- Hand over a gap list with no priorities or owners.

✅ **DO:**
- Anchor gaps to the stated should-cover baseline and real user demand signals.
- Open and link every page assessed; record its date.
- Separate "doesn't exist" from "exists but hard to find."
- Prioritize by frequency, severity, and effort, and name a likely owner.
- Flag unassessable areas `[NEEDS REVIEW]` and state confidence; suggest outlines for top gaps.

---

## Output Format

```
# Knowledge Base Gap Analysis: [Topic / Area]

## Context & Baseline
- Used by: [...]   | Primary use cases: [...]
- Critical processes it should cover: [list]
- Sources reviewed: [...]
- Confidence in overall assessment: [High/Medium/Low]; not fully assessed: [list, [NEEDS REVIEW]]

## Coverage Assessment
| Topic / Process | Documented (Y/Partial/N) | Quality | Last updated | Link |
|-----------------|--------------------------|---------|--------------|------|
| ...             | ...                      | Complete/Needs Update/Stub | ... | link / "Missing" |

## Well-Documented Areas
- [Topic] — [why strong; could template others]

## Partial Documentation
- [Topic] — has [...]; missing [...]

## Critical Gaps
- [Topic] — why it matters (who/when); priority: Critical/High/Medium; suggested outline: [...]

## Outdated Content
- [Topic] — staleness; risk of following it

## Conflicting Information
- [Topic] — contradiction; which appears more current; resolution needed

## Orphaned / Findability Issues
- [Topic] — exists but disconnected / hard to find; suggested placement

## Tribal Knowledge to Capture
- [What people repeatedly ask that isn't documented]

## Recommended Priorities (top 5–10)
1. [Gap] — need × severity × effort; likely owner: [...]
```

---

## Example Output

```
# Knowledge Base Gap Analysis: Customer Support KB (placeholder)

## Context & Baseline
- Used by: support agents (tier 1 & 2)   | Primary use cases: resolve tickets fast, escalate correctly
- Critical processes it should cover: refunds, account recovery, billing disputes, escalation paths, SLA rules
- Sources reviewed: /support-kb (Notion, 52 pages, placeholder)
- Confidence: Medium; not fully assessed: "Billing internal (restricted)" [NEEDS REVIEW]

## Coverage Assessment
| Topic / Process | Documented | Quality | Last updated | Link |
|-----------------|------------|---------|--------------|------|
| Refunds | Yes | Complete | 2026-04 | [link](#) |
| Account recovery | Partial | Needs Update | 2024-08 | [link](#) |
| Billing disputes | No | — | — | Missing |
| Escalation paths | Yes | Stub | 2025-11 | [link](#) |
| SLA rules | Yes | Complete | 2026-03 | [link](#) |

## Well-Documented Areas
- Refunds — step-by-step with screenshots; use as the template for other procedures.

## Partial Documentation
- Account recovery — covers password reset; missing 2FA-lockout and email-change flows.

## Critical Gaps
- Billing disputes — no documentation; agents improvise. Priority: Critical (high ticket volume). Suggested outline: dispute types → evidence to collect → resolution authority → escalation.

## Outdated Content
- Account recovery — last updated 2024-08, predates the new 2FA system; risk of giving wrong steps.

## Conflicting Information
- Escalation paths page lists tier-2 contact differently than the SLA page; SLA page appears more current (2026-03). Reconcile to one source.

## Orphaned / Findability Issues
- A thorough "chargeback handling" note exists but isn't linked from any index — agents can't find it. Link it under Billing.

## Tribal Knowledge to Capture
- Agents repeatedly ask in chat how to handle duplicate charges — no doc exists; capture it.

## Recommended Priorities (top 5)
1. Billing disputes doc — high need, high severity, medium effort; owner: senior billing agent.
2. Update Account recovery for 2FA — high need, high severity, low effort; owner: enablement.
3. Reconcile escalation contact conflict — medium need, high severity, low effort; owner: support lead.
4. Link orphaned chargeback note + add duplicate-charge guide — medium need, low effort; owner: KB admin.
```

---

## Verification

- [ ] Gaps assessed against a stated should-cover baseline and real demand signals.
- [ ] Every coverage call based on opened content, linked and dated.
- [ ] "Doesn't exist" separated from "exists but hard to find."
- [ ] Outdated and conflicting content surfaced with resolution guidance.
- [ ] Top gaps prioritized by need × severity × effort with owners.
- [ ] No invented pages, content, or dates.
- [ ] Unassessable areas flagged `[NEEDS REVIEW]`; overall confidence stated.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a prioritized, user-needs-driven gap analysis.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines coverage across existence, quality, recency, consistency, and findability.
- **DS-02 (Evidence-Based Decision Making):** Requires coverage judgments to rest on opened, linked, dated content.
- **DS-06 (Prioritization and Severity Guidance):** Ranks the top gaps by need, severity, and effort with owners.
- **QA-01 (Self-Critique Triggers):** Final self-check guards against title-only judgments and confusing absence with findability.

---

## Related Prompts

- `domain-business-strategy/organization/organization_content_audit.md` — Declutter existing content rather than find what's missing.
- `domain-business-strategy/organization/organization_project_status_summary.md` — Synthesize scattered docs into a status snapshot.
- `domain-business-strategy/research/research_content_research.md` — Gather source material to fill identified gaps.
