---
title: "Decision Log Entry — Append-Only Running Record"
category: decision-making/documentation
description: "Produce a single, lightweight, append-only entry for an ongoing decision log: date, decision, context, rationale, alternatives considered, decider, review date, and status (active / superseded / abandoned). Far lighter than a full options memo — built to accumulate in a markdown file or database as a searchable institutional record. Includes an explicit upgrade rule for when an entry's stakes or contestedness demand a full options memo instead."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-documentation
  - decision-log
  - decision-record
  - adr
  - institutional-memory
updated: "2026-05-10"
reasoning:
  styles: [structured, archival]
  stakes: low
  horizon: variable
  uncertainty: variable
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: small_team
  output_format: structured
  user_role: [pm, engineer, founder, manager, individual, operator]
  mode: [document]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-decision-making/documentation/decisiondoc_one_pager.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Decision Log Entry

**Objective:** Generate one **append-only** entry for a running decision log. Where the options memo is a deliberation artifact for a single significant decision, the log entry is institutional memory at volume: a short, uniform record that accumulates so that six months later anyone can answer "why did we decide X, who decided it, what did we consider, and is it still in force?" The discipline it enforces is **lightweight uniformity** — every entry has the same fields, captured at the moment of decision while the reasoning is still fresh, before motivated reconstruction sets in.

It is append-only by design: you never edit the rationale of a past entry. If a decision changes, you write a **new** entry that supersedes the old one, and mark the old one's status. This preserves the audit trail.

**When to use:**
- A team or individual maintaining a running decision log (markdown file, Notion/Confluence database, ADR directory).
- Capturing the steady stream of small-to-medium decisions that don't each warrant a memo but collectively define how a project actually works.
- Onboarding/handoff contexts where "the log of past decisions" is the fastest way to transmit accumulated context.
- Recording a decision the moment it's made, so the rationale is captured before it's forgotten or rewritten.

**When NOT to use:**
- A high-stakes or contested decision that needs deliberation, steelmanned alternatives, and stakeholder objections — use `decisiondoc_options_memo.md` (see the upgrade rule below).
- A decision that follows mechanically from existing policy — no entry needed.
- You're trying to *make* the decision. The log records decisions; it doesn't deliberate them.

**Audience:** PMs, engineers, founders, managers, operators, and individuals keeping a durable record of decisions over time.

---

## Inputs / Context

1. **The decision** in one sentence (what was decided).
2. **Context** — what prompted it; the situation at decision time.
3. **Rationale** — the reasons, as bullets.
4. **Alternatives considered** — each as a one-liner with why-not.
5. **Decider** — the person/role accountable.
6. **Date** — when decided.
7. **Review date** (optional) — when to revisit, if applicable.
8. **Stakes / contestedness** — to apply the upgrade rule.

---

## Constraints

### Must
- Keep it to **one screen**. The log's value is in volume + uniformity; a bloated entry defeats it.
- Capture all core fields: **date, decision, context, rationale (bullets), alternatives considered (one-liners), decider, review date, status**.
- Write **alternatives as one-liners each with a why-not** — even at log weight, "what we ruled out" is the highest-value field for future readers.
- Set **status** to one of: `active`, `superseded by [entry id/date]`, `abandoned`. New entries default to `active`.
- Be **append-only**: never rewrite a past entry's rationale. Supersession is a *new* entry plus a status flip on the old one.
- Apply the **upgrade rule** (below) and, if it fires, recommend writing a full options memo instead of (or in addition to) the log entry.
- Use a stable **entry id** (date + short slug) so other entries can reference it for supersession.

### Must Not
- Pad the entry into a memo. If it needs a memo, say so (upgrade rule) — don't quietly grow the log entry.
- Edit history. Past entries are immutable; corrections are new entries.
- Omit the decider. An unattributed decision can't be questioned or owned.
- Record only the chosen path with no alternatives. The ruled-out options are what make the log worth reading later.
- Invent a review date where none applies — use `n/a` rather than a fake date.

---

## Upgrade rule (log entry → full options memo)

Write a full `decisiondoc_options_memo.md` instead of (or alongside) a log entry when **any** of these fire:
- **High stakes:** one-way-door and materially consequential (Quadrant D in `tradeoff_reversibility_stakes_grid.md`).
- **Contested:** stakeholders actively disagree and the decision needs documented objections-and-responses.
- **Expensive to revisit:** reopening later would be costly, so the reasoning must be airtight now.
- **Audit-sensitive:** regulatory, legal, or governance scrutiny is likely.

If none fire, the log entry is the right weight.

---

## Instructions

### Step 1 — Apply the upgrade rule first
Check the four triggers. If any fires, recommend an options memo and (optionally) still write a log entry that points to it. If none fires, proceed.

### Step 2 — State the decision
One sentence. What was decided, concretely.

### Step 3 — Capture context
2–4 bullets: what prompted this, the situation at decision time, any deadline or forcing function.

### Step 4 — Capture rationale
Bullet list of the actual reasons. Reasons, not restatement of the decision.

### Step 5 — Capture alternatives considered
Each as: **[alternative] — not chosen because [reason].** Even one line each.

### Step 6 — Attribute and schedule
Decider (name/role). Review date if the decision is time-bound or experimental; otherwise `n/a`.

### Step 7 — Set status and id
Default `active`. Assign a stable id (e.g., `2026-05-10-vendor-switch`). If this entry supersedes a prior one, note the prior id and instruct flipping the prior entry's status to `superseded by [this id]`.

---

## False-Positive Prevention

1. **Memo creep.** A log entry that's swelling into a multi-page memo. Apply the upgrade rule and split it out.
2. **History editing.** "Fixing" a past entry's rationale. Forbidden — append a new entry; mark the old superseded.
3. **No alternatives.** Recording only the chosen path. The ruled-out one-liners are the field future readers most need.
4. **Anonymous decisions.** No decider listed. Always attribute.
5. **Fake review dates.** Inventing a revisit date to fill the field. Use `n/a` when none applies.
6. **Rationale = restatement.** "We decided X because we chose X." Capture the actual reasons.
7. **Status rot.** Leaving superseded entries marked `active`. When a new entry supersedes, flip the old status.
8. **Upgrade-rule evasion.** Logging a high-stakes contested decision as a one-liner to avoid writing the memo. The triggers exist to catch exactly this.

---

## Output Format

```
### [YYYY-MM-DD] — [Decision title]   `id: YYYY-MM-DD-short-slug`

**Status:** active | superseded by `[id]` | abandoned
**Decider:** [name / role]
**Review date:** [YYYY-MM-DD or n/a]

**Decision:** [one sentence — what was decided]

**Context:**
- [what prompted this]
- [situation / constraint / deadline]

**Rationale:**
- [reason 1]
- [reason 2]
- [reason 3]

**Alternatives considered:**
- [alternative A] — not chosen because [reason]
- [alternative B] — not chosen because [reason]

**Supersedes:** `[prior id]` (flip that entry's status to "superseded by [this id]") — or n/a
```

If the upgrade rule fired, prepend:

```
> UPGRADE RECOMMENDED: This decision trips [trigger(s)]. Write a full options memo
> (decisiondoc_options_memo.md). Log entry below may serve as the index pointer to it.
```

---

## Verification

- [ ] Entry fits on one screen.
- [ ] Upgrade rule checked first; flagged if any trigger fired.
- [ ] All core fields present: date, decision, context, rationale, alternatives, decider, review date, status.
- [ ] Alternatives recorded as one-liners with why-not.
- [ ] Status set ( active / superseded / abandoned ); default active.
- [ ] Stable entry id assigned.
- [ ] Append-only respected — no past entry rewritten; supersession is a new entry + old-status flip.
- [ ] Decider named.
- [ ] Rationale gives reasons, not a restatement of the decision.
