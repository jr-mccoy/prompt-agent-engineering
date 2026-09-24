---
title: "Appellate Oral Argument Prep — Question Anticipation, Concession Map, and Hot-Bench Drills"
category: legal/appellate
description: "Prepare appellate counsel for oral argument: a one-sentence ask, a roadmap, an anticipated-question bank tied to the briefs and record, a concession map (what to give, what never to give, and the fallback), timed hot-bench drill rounds with a simulated panel, and a time and rebuttal strategy — using only the briefs, record, and authority supplied."
techniques:
  - ST-01
  - RP-01
  - QA-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - appellate
  - oral-argument
  - moot-court
  - hot-bench
  - concessions
updated: "2026-09-24"
related_prompts:
  - domain-legal/appellate/legal_issue_selection_memo.md
  - domain-legal/appellate/legal_statement_of_facts_builder.md
  - domain-legal/depositions/legal_expert_deposition_prep.md
  - domain-legal/research/legal_precedent_comparison_table.md
---

**Objective:** Get counsel ready to answer the panel's hardest questions directly and return to the theme: produce the core ask and roadmap, a ranked bank of anticipated questions with short answers anchored to the briefs and record, a concession map that decides in advance what can be conceded without losing the case, and live drill rounds in which the model plays a skeptical panel.

**When to Use:** After briefing closes and argument is calendared; before a moot court; when the panel composition is known and the user supplies the judges' relevant published opinions; when preparing for a rebuttal-heavy appellee argument or a cross-appeal.

**Distinct from:**
- `domain-legal/depositions/legal_expert_deposition_prep.md` — prepares a witness to answer an adversary's questions under oath; this prompt prepares an advocate to answer a court.
- `domain-legal/research/legal_precedent_comparison_table.md` — compares authorities; its output can feed the "distinguish this case" answers here.
- `domain-legal/litigation/` trial prompts — jury-facing advocacy; this prompt is bench-facing and question-driven.

---

## Your Input

- **Court, panel, and argument date:** [Required; judges' names only if the user supplies them]
- **Time allotted and rebuttal plan:** [As set by the court's notice]
- **Posture:** [Appellant / appellee / cross-appeal; who argues first]
- **Briefs:** [Opening, response, reply — text or key excerpts]
- **Record excerpts:** [With record cites]
- **Key authorities:** [Cases both sides rely on, with holdings as the user has verified them]
- **Panel material (optional):** [Published opinions or questions from prior arguments that the user supplies — the model will not characterize judges from memory]
- **Known weaknesses:** [Counsel's own list]

---

## Constraints

**Must:**
- Open with a **one-sentence ask** (what the court should do and why) and a **roadmap** of no more than three points.
- Build a question bank ranked by likelihood and danger, covering: jurisdiction/standing/preservation; standard of review; the weakest point in each issue; the opposing side's best case; the limiting principle ("where does your rule stop?"); remedy ("what exactly should we do?"); record ("where is that in the record?"); hypotheticals.
- For each question: a **short direct answer** (first sentence answers yes/no/it depends-with-reason), a record or brief cite, and a **pivot** back to the theme.
- Build a **concession map**: points to concede readily, points to concede only in a stated narrower form, and points never to concede because they end the case — each with the reason.
- Run drill rounds with the model playing a panel of skeptical judges; interrupt, press follow-ups, and score answers.
- Plan time: opening minute, issue allocation, cut list if questions consume time, and rebuttal points reserved for the opponent's likely themes.

**Must Not:**
- Invent judges' views, voting records, or quotations; use only panel material the user supplies.
- Invent case holdings, record cites, or statutory text; use `[CITE]`, `[NEED HOLDING]`, `[NEED RECORD CITE]`.
- Draft answers that dodge the question or promise to "get to that later."
- Script a speech; argument is a conversation and the prep must reflect that.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Distill.** One-sentence ask, theme, and three-point roadmap.
2. **Weakness audit.** From the briefs, list the opponent's three strongest points and counsel's three weakest; each becomes a top-tier question.
3. **Question bank.** Generate and rank questions; draft direct answer + cite + pivot.
4. **Concession map.** Classify each potential concession; write the exact words of each permitted concession.
5. **Hypotheticals.** Write hypotheticals testing the limiting principle; draft answers that accept the hypo's premise where possible and distinguish on stated facts.
6. **Drill rounds.** Round 1: cold questions across issues. Round 2: hot bench — rapid follow-ups on the two weakest points. Round 3: time pressure — the model cuts counsel off and counsel must land the ask. After each round, score: directness, accuracy to record, pivot, composure; list fixes.
7. **Time and rebuttal plan.** Minute-by-minute allocation, the cut list, and two to three rebuttal targets.
8. **Pocket card.** One page: ask, roadmap, top concessions, never-concede list, five record cites counsel must know by page.

---

## Output Format

```markdown
# ORAL ARGUMENT PREP — {Case} — {Court} — {Date}

## 1. The Ask & Roadmap
- Ask: {one sentence}
- Roadmap: (1) ... (2) ... (3) ...

## 2. Question Bank
| Rank | Question | Category | Direct answer | Cite | Pivot |

## 3. Concession Map
| Point | Concede? (Yes / Narrowly / Never) | Exact words | Why |

## 4. Hypotheticals
| Hypo | Answer | Distinguishing fact |

## 5. Drill Rounds
### Round {n} — {type}
- Q (Judge A): ...
- [Counsel answers; model follows up]
- Score: Directness {1–5} · Record accuracy {1–5} · Pivot {1–5} · Composure {1–5}
- Fixes: ...

## 6. Time & Rebuttal Plan
| Minute | Content | Cut if short on time? |
Rebuttal targets: ...

## 7. Pocket Card
{One page}
```

---

## Worked Example (abbreviated)

**Input:** Appellee (government) defending a denial of suppression; 15 minutes; opponent's best point is that the stop was prolonged beyond the traffic mission. User supplies the briefs, the suppression order, and hearing excerpts.

**Output excerpt:**
- Ask: "Affirm, because the district court's finding that the dog sniff began before the citation was complete is supported by the record and dispositive."
- Question #1 (danger: high): "Counsel, the officer's report says the citation was finished at 1:19. Why isn't that the end of your case?" → Answer: "Because the district court credited the dash-cam time stamp over the report, finding the citation was still being written (JA 94), and that finding is reviewed deferentially `[VERIFY SoR: authority supplied in brief at 18]`." → Pivot to the finding.
- Concession map: concede "the report's time entry is inconsistent" (Yes); concede "a sniff after completion would require reasonable suspicion" (Narrowly — "on these facts the sniff began before completion"); never concede "the stop was prolonged," which ends the case.
- Round 2 hot bench: the model, as Judge B, presses: "If we disagree about the finding, do you have an independent reasonable-suspicion argument, and was it preserved?" — counsel's answer scored 2/5 for directness; fix: lead with "Yes, at pages 22–25 of our brief" or "No" before explaining.

---

## Verification

- [ ] Court, time allotment, and posture locked.
- [ ] Ask is one sentence; roadmap has at most three points.
- [ ] Question bank covers jurisdiction, standard of review, weakest points, limiting principle, remedy, record, and hypotheticals.
- [ ] Every answer starts with a direct response and carries a cite.
- [ ] Concession map includes exact words and a never-concede list.
- [ ] Drill rounds scored with specific fixes.
- [ ] No invented judicial views, holdings, or record cites.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Preparing a speech instead of answers | Build the question bank and drills first; the opening is two sentences |
| Answers that begin with context instead of yes/no | First sentence answers the question; explanation follows |
| Characterizing judges from general reputation | Use only user-supplied panel material; otherwise treat judges as unknown skeptics |
| No limiting principle for the rule advocated | Draft the limiting principle and test it with hypotheticals |
| Treating every concession as fatal | Concession map separates harmless, narrow, and fatal concessions |
| Losing the remedy question | Prepare the exact disposition requested (affirm, reverse, remand with instructions) |
| Record cites counsel cannot locate at the podium | Pocket card lists the key cites by page |
| Softball drills | Hot-bench round focuses on the two weakest points with repeated follow-ups |
