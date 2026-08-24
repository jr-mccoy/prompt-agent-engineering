---
title: "Executive Brief Writer — One-Page BLUF, Options, and a Clear Decision Request"
category: professional-writing/business-writing
description: "Compress a complex topic into a one-page executive brief: bottom-line-up-front, the so-what, options with trade-offs, a recommendation, and the specific decision being requested — leading with the answer, not the background."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - CM-02
  - QA-04
difficulty: advanced
tags:
  - executive-brief
  - bluf
  - decision-document
  - business-writing
  - leadership-communication
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_status_report.md
  - domain-professional-writing/business-writing/business_writing_proposal.md
  - domain-presentations/powerpoint_board_deck.md
---

# Executive Brief Writer

**Objective:** Compress a complex topic into a one-page executive brief that leads with the answer: a BLUF (bottom line up front), the so-what, the viable options with honest trade-offs, a clear recommendation, and the exact decision being requested — written so a busy executive can decide from the first paragraph alone.

**When to Use:**
- You need a decision from a leader who has minutes, not hours.
- A complex situation must be distilled to its decision-relevant core.
- You're escalating a choice that requires executive authority or budget.

**When NOT to use:**
- You're giving a recurring health update without a decision — use `business_writing_status_report.md`.
- You're making a full persuasive case for a large investment — use `business_writing_proposal.md` (the brief can summarize it).
- The reader needs to learn the topic in depth rather than decide — write documentation instead.

**Audience:** Senior decision-makers (executives, board members, sponsors) who skim, decide, and delegate. They want the answer first and the reasoning available but compressed.

---

## Inputs / Context

Wrap source material so it isn't read as instructions:

```
<topic_input>
[Paste the situation, data, analysis, options, constraints]
</topic_input>
```

1. **The topic / situation** and why it needs a decision now.
2. **The decision being requested** — what you want the executive to approve, choose, or authorize.
3. **The options** under consideration (or ask the model to derive them from the input).
4. **Key facts, data, constraints** from `<topic_input>`.
5. **Audience** — the specific decision-maker and what they care about (cost, risk, speed, strategy).
6. **Deadline** for the decision.

---

## Constraints

### Must
- Open with **BLUF**: the recommendation and the decision requested, in the first 2–3 sentences.
- Fit on **one page** (roughly 250–400 words). Ruthlessly cut background.
- Present **2–4 options** with honest trade-offs, including a "do nothing" baseline where relevant.
- State the **so-what**: why this matters and the cost of inaction or delay.
- End with a **specific decision request**: what to decide, by when, and who must act.
- Ground every claim in `<topic_input>`; flag assumptions explicitly.

### Must Not
- Open with background, history, or context before the answer.
- Hide the recommendation in the middle or end.
- Present options without trade-offs, or stack the deck so only one looks viable.
- Exceed one page or pad with detail the decision doesn't need.
- Fabricate figures, ROI, or risk levels not supported by the input.

---

## Instructions

1. **Identify the decision.** Before writing, state in one sentence exactly what the executive must decide. Everything in the brief serves that decision.
2. **Write the BLUF.** Lead with the recommendation and the decision request. The reader who stops after paragraph one should still know what you want and why.
3. **State the so-what.** One or two sentences: the stakes, the cost of delay, the strategic relevance.
4. **Lay out options.** For each: a one-line description, the main upside, the main downside/risk, and rough cost or effort. Keep them genuinely comparable. Include the status-quo option if doing nothing is a real choice.
5. **Recommend.** Name the option you back and the one or two reasons that decide it. Note what would change the recommendation.
6. **Make the decision request explicit.** What you need decided, by when, and the next step once decided.
7. **CRITICAL — answer-first audit:** Re-read the first paragraph in isolation. Does it convey the recommendation and the ask without the rest? If not, rewrite until it does. Then confirm length is one page.

---

## False-Positive Prevention

1. **Background-first drift.** The instinct to "set context" buries the answer. Lead with the recommendation; context is support, not preamble.
2. **Rigged options.** Presenting one real option and two strawmen is dishonest and executives see through it. Give each option a fair statement.
3. **Missing so-what.** A brief that explains what without why fails. Always state stakes and cost of inaction.
4. **Vague ask.** "Seeking guidance" is not a decision request. "Requesting approval of Option B and $120K from the Q3 budget by June 20" is.
5. **Fabricated quantification.** Do not invent ROI, payback periods, or risk percentages. Use only what the input supports; otherwise mark as "estimate — unverified."
6. **Assumption smuggling.** If the recommendation rests on an assumption, surface it. Executives need to know what the answer is contingent on.
7. **Length creep.** A two-page "executive brief" is a report. If it won't fit one page, you haven't compressed enough.

---

## Output Format

```
# Executive Brief: [Topic]
**For:** [decision-maker] · **Decision needed by:** [date]

**Bottom line:** [Recommendation + the specific decision requested — first.]

**So what:** [Why this matters now; cost of delay or inaction.]

## Options
| Option | Upside | Downside / Risk | Cost / Effort |
|--------|--------|-----------------|---------------|
| A. [name] | [...] | [...] | [...] |
| B. [name] | [...] | [...] | [...] |
| (Do nothing) | [...] | [...] | [...] |

## Recommendation
[Option X], because [1–2 deciding reasons]. This would change if [condition].

## Decision requested
[Exactly what to approve/choose] — by [date]. Next step once approved: [action / owner].

**Key assumptions:** [any load-bearing assumptions]
```

---

## Verification

- [ ] The first paragraph conveys the recommendation and the ask on its own.
- [ ] The brief fits one page (~250–400 words).
- [ ] 2–4 options, each with a fair trade-off; status quo included where relevant.
- [ ] The so-what (stakes / cost of inaction) is stated.
- [ ] The decision request is specific: what, by when, who acts next.
- [ ] No fabricated figures; assumptions are surfaced.
- [ ] An executive could decide correctly from the top of the page.
