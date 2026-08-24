---
title: "Executive One-Pager — Whole Decision in 60 Seconds"
category: decision-making/documentation
description: "Compress a decision into a single page (or single screen) for an audience that will not read more: a TL;DR block (decision asked, recommendation, top reason, top risk, decision-maker, deadline) plus 3–5 bullets each for context, options, recommendation reasoning, and key risks. Distinct from the TL;DR of an options memo — this is the standalone artifact for a board, CEO, or principal who needs the entire picture in under a minute, with nothing else to fall back on."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-documentation
  - one-pager
  - executive-communication
  - brief
  - summary
updated: "2026-05-10"
reasoning:
  styles: [compression, structured]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: org
  output_format: structured
  user_role: [executive, pm, founder, chief_of_staff, analyst]
  mode: [synthesize, document, decide]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-decision-making/documentation/decisiondoc_narrative_memo_bezos.md
  - domain-decision-making/documentation/decisiondoc_log_entry.md
---

# Executive One-Pager

**Objective:** Compress a whole decision onto a **single page (or single screen)** for a reader who will not read more — a board member, CEO, or principal who needs the complete picture in under a minute and has nothing else to fall back on. The discipline is **ruthless compression without omission of the load-bearing parts**: the decision being asked, the recommendation, the single best reason, the single biggest risk, who decides, by when — then just enough supporting structure (3–5 bullets per section) to make the recommendation legible and challengeable.

This is **not** the TL;DR section of a longer memo. The TL;DR assumes the rest of the memo exists behind it. The one-pager is **standalone**: it is the entire artifact, and it must carry the full decision on its own. That changes what goes in — every choice about what to cut is a choice the reader can't recover from by reading on.

**When to use:**
- The decision-maker reads one page and acts (board, CEO, investor, busy principal).
- A pre-read where you have one screen of attention and no more.
- A cover sheet on top of a longer memo for readers who want the whole thing fast (but the one-pager must still stand alone).
- Rapid alignment: circulate the one-pager to confirm everyone sees the same decision before investing in deeper docs.

**When NOT to use:**
- The decision is contested enough to need steelmanned objections and full reasoning — use the options memo or narrative memo (and optionally a one-pager on top).
- The audience will read deeply and interrogate — write the narrative six-pager.
- The decision is small enough for a log entry.
- You haven't actually decided what to recommend. The one-pager has no room to hedge.

**Audience:** Executives, founders, chiefs of staff, and PMs briefing a board, CEO, or principal who decides off a single page.

---

## Inputs / Context

1. **The decision asked** — the specific question requiring a yes/choice.
2. **The recommendation** — what you're advising.
3. **Context** — the 3–5 facts that frame why this is on the table.
4. **Options** — the realistic paths, one line each, including status quo.
5. **The reasoning** — why the recommendation wins (3–5 points).
6. **Key risks** — the top risks and their mitigations (3–5).
7. **Decision-maker and deadline.**

---

## Constraints

### Must
- Fit on **one page / one screen.** This is a hard constraint; if it doesn't fit, cut, don't shrink the font.
- Open with a **TL;DR block** containing all six anchors: **decision asked, recommendation, top reason, top risk, decision-maker, deadline.** A reader who reads only the TL;DR can act.
- Provide **3–5 bullets each** for: context, options (one line per option, including status quo), recommendation reasoning, key risks (with mitigation).
- Make every bullet **load-bearing.** On one page there is no room for a bullet that doesn't change the reader's understanding.
- Name the **single top reason** and the **single top risk** — not a list. Forcing the singular is the compression discipline.
- Stand **alone.** Assume the reader has and will read nothing else. No "see attached for the real argument."
- Name the **decision-maker** and a **dated deadline**.

### Must Not
- Spill onto a second page. Two pages is a different document.
- Hedge the recommendation ("we could do A or B"). The one-pager recommends one thing; alternatives appear in the options line, not the recommendation.
- List five "top" reasons or risks. Singular top reason, singular top risk in the TL;DR; the 3–5 bullet sections carry the rest.
- Depend on an attached memo to carry the argument. If the one-pager needs the memo to make sense, it has failed its job.
- Drop the status-quo option from the options line. Even at one-page weight, "do nothing" belongs on the board.
- Pad with background the decision-maker already knows.

---

## Instructions

### Step 1 — Write the TL;DR block first
Six anchors, each one line:
- **Decision asked:** [the question]
- **Recommendation:** [the one thing]
- **Top reason:** [single best reason]
- **Top risk:** [single biggest risk]
- **Decision-maker:** [name/role]
- **Deadline:** [date]

If you can't fill all six crisply, the decision isn't ready for a one-pager.

### Step 2 — Context (3–5 bullets)
The few facts that explain why this decision is live now. Cut anything the reader already knows.

### Step 3 — Options (one line each)
Each realistic path in a single line, including status quo. Just enough to show the recommendation was a choice among real alternatives.

### Step 4 — Why this recommendation (3–5 bullets)
The reasoning, compressed. The strongest points only; the marginal ones don't earn space.

### Step 5 — Key risks (3–5 bullets, each with mitigation)
Top risks of the recommended path, each with its one-line mitigation. A risk without a mitigation reads as unmanaged.

### Step 6 — Fit check
Confirm it's one page. If over, cut the weakest bullet in each section before touching formatting. Compression is editorial, not typographic.

### Step 7 — Standalone test
Read it as someone who has seen nothing else. Can they act? If they'd need the attached memo to understand the recommendation, revise until the page stands alone.

---

## False-Positive Prevention

1. **Two-page creep.** "One-pager" running to two pages. Hard cut to one; trim the weakest bullets first.
2. **Hedged recommendation.** "We recommend A or possibly B." One recommendation. Alternatives live in the options line.
3. **Plural "top."** Five top reasons, five top risks in the TL;DR. Force the singular for each in the TL;DR; the rest go in the bullet sections.
4. **Dependency on the attachment.** A one-pager that only makes sense if you read the 10-page memo behind it. It must stand alone.
5. **Status-quo omission.** Dropping "do nothing" to save a line. Keep it; it's often the real competitor.
6. **Filler bullets.** Bullets that restate the obvious or repeat known background. Every bullet must change the reader's understanding.
7. **Unmitigated risks.** Listing risks with no mitigation. Each key risk gets a one-line mitigation or it reads as ignored.
8. **Missing decision mechanics.** No named decider or deadline. Both are mandatory — a one-pager exists to drive a decision.

---

## Output Format

```
# ONE-PAGER — [decision title]

## TL;DR
- **Decision asked:** [the question]
- **Recommendation:** [the one thing]
- **Top reason:** [single best reason]
- **Top risk:** [single biggest risk]
- **Decision-maker:** [name / role]   |   **Deadline:** [date]

## Context
- [fact 1]
- [fact 2]
- [fact 3]
( 3–5 bullets )

## Options
- **A — [name]:** [one line]
- **B — [name]:** [one line]
- **C — Status quo / do nothing:** [one line]

## Why we recommend [A]
- [reason 1]
- [reason 2]
- [reason 3]
( 3–5 bullets )

## Key risks
- **[Risk 1]** → mitigation: [one line]
- **[Risk 2]** → mitigation: [one line]
- **[Risk 3]** → mitigation: [one line]
( 3–5 bullets )
```

---

## Verification

- [ ] Fits on one page / one screen.
- [ ] TL;DR carries all six anchors (decision asked, recommendation, top reason, top risk, decision-maker, deadline).
- [ ] Single top reason and single top risk in the TL;DR (not lists).
- [ ] 3–5 bullets each for context, options, reasoning, risks.
- [ ] Options line includes status quo / do-nothing.
- [ ] Each key risk has a mitigation.
- [ ] Recommendation is singular, not hedged.
- [ ] Document stands alone (no dependence on an attached memo).
- [ ] Decision-maker and dated deadline present.
- [ ] No filler bullets; every bullet is load-bearing.
