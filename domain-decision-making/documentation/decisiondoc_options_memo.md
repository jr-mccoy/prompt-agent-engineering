---
title: "Options Memo — Multi-Option Decision Memo with Recommendation"
category: decision-making/documentation
description: "Standard structure for a decision memo that presents 2–4 options against shared criteria, makes a recommendation with reasoning, names the strongest objections to the recommendation, and specifies what would have to be true to revisit. Designed to make decisions auditable and to focus discussion on the load-bearing tradeoffs rather than presentation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-documentation
  - options-memo
  - decision-record
  - executive-communication
  - structured-writing
updated: "2026-05-10"
reasoning:
  styles: [structured, comparative, persuasive]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: pair_or_team
  output_format: structured_memo
  user_role: [pm, executive, founder, consultant, analyst, policy]
  mode: [synthesize, document, decide]
related_prompts:
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-deep-analysis/deepthink_decision.md
---

# Options Memo

**Objective:** Produce a decision memo that presents 2–4 options against shared criteria, makes a recommendation with reasoning, names the strongest objections to the recommendation, and specifies the conditions under which the decision should be revisited. The structure is rigid by design — readers should be able to find the recommendation, the tradeoffs, and the dissent in predictable places.

This is a documentation prompt, not a deliberation prompt. The deliberation should already be done (perhaps via `tradeoff_multi_criteria_decision_analysis.md` or `deepthink_decision.md`); the memo captures and communicates it. A good memo lets a reader who wasn't in the room reconstruct the decision logic and challenge it.

**When to use:**
- A decision is about to be made, made, or has been made and needs documentation for stakeholders, posterity, or audit.
- A team needs to align before a meeting; sending the memo in advance focuses discussion.
- Architecture decisions, vendor decisions, hiring decisions, strategic decisions, policy decisions.
- Personal high-stakes decisions where you want to lock in the reasoning before motivated revisionism kicks in.
- Decision history for an organization (decision log).

**When NOT to use:**
- The decision is so small that the memo would weigh more than the decision itself.
- The decision is purely operational and follows from existing policy.
- The user wants persuasive rhetoric, not auditable structure. Use a different format.

**Audience:** PMs, executives, founders, consultants, policy analysts — anyone whose decisions need to survive scrutiny by people who weren't in the original conversation.

---

## Inputs / Context

1. **The decision question.** As a question with named options.
2. **Background.** What led to the decision being on the table now.
3. **Constraints.** Hard constraints (budget, time, regulation, ethics) that bound the option space.
4. **Criteria.** Dimensions on which options are evaluated.
5. **Stakeholders.** Whose decision this is, who's consulted, who's informed.
6. **Existing analysis.** MCDA, scenario work, research — to be summarized in the memo, not redone.

---

## Memo structure (mandatory sections)

1. **TL;DR / Recommendation** — one paragraph at the top.
2. **Context** — what led to the decision; why now.
3. **Decision question** — sharp.
4. **Options considered** — 2–4 options.
5. **Criteria** — what we're judging on; weights if applicable.
6. **Comparison** — option × criteria matrix or per-option summary.
7. **Recommendation** — restated with reasoning.
8. **Strongest objections** — to the recommendation, with responses.
9. **Risks and mitigations** — for the recommended option.
10. **Reversibility / stakes** — classification.
11. **Tripwires / revisit conditions** — what would prompt re-opening this.
12. **Decision and decision-maker** — who decided / will decide, by when.
13. **Appendix (optional)** — deeper analysis, sources, alternatives considered and ruled out early.

---

## Constraints

### Must
- Lead with the recommendation. Readers should not have to scroll for the answer.
- Present 2–4 options minimum. Single-option memos are not decisions, they're announcements.
- Include the option of "do nothing" / "wait" / "status quo" if it's plausible. Often it's the disguised winner.
- Show comparison structure (matrix or per-option) — not buried prose.
- Surface the **strongest** objections, not the easiest-to-dismiss ones. The strongest-objection section is the audit value of the memo.
- For each strong objection: respond. The response can be "we accept this risk," "we believe X mitigates it," or "we considered and rejected this critique because Y."
- Specify reversibility, stakes, and tripwires explicitly.
- Name the decision-maker. Memos that don't name a decider don't drive decisions.

### Must Not
- Over-recommend. The memo informs; the decider decides.
- Hide options the user dislikes by burying them or strawmanning. Steelman every option you present.
- Skip the "do nothing" option without stating why it's not viable.
- Use weasel objections ("some might argue") instead of strong ones.
- Append all the reasoning without TL;DR. A reader should be able to read the first 200 words and know the recommendation, the runner-up, and the main reason.
- Treat the memo as the decision. The memo proposes; a person decides.

---

## Instructions

### Step 1 — TL;DR
One paragraph at the top:
- Decision question (one sentence)
- Recommendation
- Top 1–2 reasons
- Top 1 risk or objection
- Decision-maker and timeline

If a reader stops here, they should know what's being recommended, why, and what the main concern is.

### Step 2 — Context
2–4 paragraphs:
- What led to this decision
- Why now
- What changes if we don't decide

### Step 3 — Decision question
Sharply stated, with hard constraints listed.

### Step 4 — Options considered
For each (2–4 options):
- Name and one-sentence description
- How it works (1–2 paragraphs)
- Who would be affected
- Indicative cost / time / effort

Include "do nothing" / status quo unless explicitly justified.

### Step 5 — Criteria
4–8 criteria, with weights if MCDA was used. State why each criterion matters for this decision.

### Step 6 — Comparison
Either:
- **Matrix:** options × criteria with per-cell scores or qualitative ratings.
- **Per-option summary:** for each option, a short paragraph of pros and cons against the criteria.

Pick whichever communicates the tradeoff most clearly.

### Step 7 — Recommendation
- Recommended option
- Reasoning: which criteria favored it, which it lost on, why net-positive
- Confidence: high / medium / low (link to MCDA sensitivity if applicable)

### Step 8 — Strongest objections
For each (3–5 objections):
- Objection (steelmanned, in language a critic would sign)
- Response (rebut / accept-with-mitigation / accept-as-known-cost)

### Step 9 — Risks and mitigations
For the recommended option:
- Top 3–5 risks
- Mitigation per risk
- Owner of each mitigation

### Step 10 — Reversibility / stakes
- Reversibility: two-way / one-way (with reversal cost)
- Stakes: low / high
- Quadrant per `tradeoff_reversibility_stakes_grid.md`

### Step 11 — Tripwires / revisit conditions
What observable would trigger re-opening the decision:
- [Tripwire 1] → revisit by [date]
- [Tripwire 2] → revisit by [date]

### Step 12 — Decision and decision-maker
- Decision-maker: [name and role]
- Consulted: [names]
- Informed: [names]
- Decision deadline: [date]

### Step 13 — Appendix (optional)
- Detailed analysis
- Options ruled out early (and why)
- Sources / data
- Linked documents

---

## False-Positive Prevention

1. **Buried recommendation.** Reader has to scroll past 5 sections to find the answer. Lead with TL;DR.
2. **Single-option memo.** Presenting one option with hand-waved alternatives is announcement, not decision support. Force 2–4.
3. **Status-quo invisibility.** "Do nothing" often wins; if it's not even on the table, the comparison is rigged.
4. **Strawmanned alternatives.** Presenting non-recommended options weakly. Steelman each.
5. **Weak objection list.** "Some might argue this is bad." Use the actual strongest critic's actual best argument.
6. **Decision-by-memo.** The memo proposes; the decision-maker decides. Don't cast the memo as the decision.
7. **No tripwires.** A decision without revisit conditions becomes lock-in. Always specify what would prompt re-opening.
8. **No decision-maker named.** Memos without a decider don't drive action. Name the role and the deadline.
9. **Confidence inflation.** Marking everything "high confidence" weakens the signal. Reserve high for genuine high.
10. **Appendix dump.** If everything matters, nothing matters. Push detail to appendix; keep main memo lean.

---

## Output Format

```
# DECISION MEMO — [decision question]

## TL;DR
**Recommendation:** [option]
**Decision-maker:** [name] | **By:** [date]
**Top reasons:** [1–2 sentences]
**Top concern:** [1 sentence]

---

## Context
[2–4 paragraphs]

## Decision question
> [Question]
- Hard constraints: [list]

## Options considered

### Option 1: [name]
[1–2 paragraphs: how it works, who's affected, indicative cost / time]

### Option 2: [name]
[Same]

### Option 3: [name (or "do nothing")]
[Same]

### Option 4: [name, optional]

## Criteria
| Criterion | Why it matters | Weight (if applicable) |
|-----------|----------------|------------------------|
| [...]     | [...]          | 25                     |
| [...]     | [...]          | 20                     |
| …         |                |                        |

## Comparison

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 |
|-----------|----------|----------|----------|----------|
| C1 (w=25) | strong   | medium   | weak     | strong   |
| C2 (w=20) | medium   | strong   | strong   | weak     |
| …         |          |          |          |          |

(Or per-option summary if matrix isn't best fit.)

## Recommendation
- Recommended: **Option [N]**
- Reasoning: [paragraph]
- Confidence: [high / medium / low]
- Sensitivity: [if MCDA, what would flip the recommendation]

## Strongest objections
1. **Objection:** [steelmanned in critic's language]
   **Response:** [rebut / accept-with-mitigation / accept-as-known-cost]
2. **Objection:** [...]
   **Response:** [...]
3. …

## Risks and mitigations (recommended option)
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [...]| medium     | high   | [...]      | [name]|
| …    |            |        |            |       |

## Reversibility / stakes
- Reversibility: [two-way / one-way], reversal cost: [...]
- Stakes: [low / high]
- Quadrant: [A / B / C / D]

## Tripwires / revisit conditions
- [Observable] → revisit by [date]
- [Observable] → revisit by [date]

## Decision and decision-maker
- Decision-maker: [name, role]
- Consulted: [names]
- Informed: [names]
- Decision deadline: [date]

## Appendix
- Options ruled out early: [list with reasons]
- Sources: [...]
- Linked: [docs]
```

---

## Verification

- [ ] TL;DR at the top with recommendation, decision-maker, top reason, top concern.
- [ ] 2–4 options including "do nothing" (or justified omission).
- [ ] Each option steelmanned, not strawmanned.
- [ ] Criteria stated with reasons (and weights if applicable).
- [ ] Comparison structure (matrix or per-option) is visible, not buried.
- [ ] Recommendation has confidence and sensitivity note.
- [ ] At least 3 strongest objections with explicit responses.
- [ ] Risks have mitigation and owner.
- [ ] Reversibility, stakes, and tripwires specified.
- [ ] Decision-maker named with deadline.
- [ ] No buried recommendation.
- [ ] No memo-as-decision framing.
