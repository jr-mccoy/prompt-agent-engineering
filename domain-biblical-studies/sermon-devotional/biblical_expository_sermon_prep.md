---
title: "Expository Sermon Preparation Workflow — From Exegesis to Text-Driven Outline"
category: biblical-studies/sermon-devotional
description: "Move from exegesis to a preachable expository outline: establish the text's meaning in context, distill the big idea, build points that come from the text's own structure, and bridge to application — without overclaiming what the text says or fabricating support. Neutral on contested doctrine; routes illustrations to the guarded illustration prompt."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-05
difficulty: advanced
tags:
  - sermon
  - expository
  - homiletics
  - preaching
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_illustration_finder.md
  - domain-biblical-studies/sermon-devotional/biblical_application_bridge_builder.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_series_planner.md
---

# Expository Sermon Preparation Workflow

**Objective:** Help a preacher build an expository sermon whose structure and content come *from the text* — a clear big idea, points grounded in the passage, honest application — without saying more than the text says.

**When to use:**
- Preparing to preach a specific passage expositionally.
- You have done (or will do) exegesis and need to shape it into a sermon.

**When NOT to use:**
- You haven't yet understood the passage — do `biblical_passage_exegesis_workflow.md` first.
- You're planning a multi-week arc — use `biblical_sermon_series_planner.md`.

**Audience:** Pastors/preachers (P).

---

## Inputs / Context

1. **The passage.** Reference and text in a named translation (pasted by the user).
2. **Exegetical findings.** From prior study, or to be summarized here (meaning in context, key terms, structure).
3. **Congregation.** Who they are, the occasion, sermon length.
4. **Declared tradition (optional).** May shape application and framing; contested readings still acknowledged, not preached as the only option without noting it.

---

## Constraints

### Must
- Derive the **big idea** from the passage's own point (one clear sentence).
- Build points from the text's structure/flow, not imposed on it.
- Keep claims within what the exegesis supports; distinguish "the text says" from application/inference.
- Where the passage is contested, either preach the well-supported core or acknowledge the range honestly rather than asserting a disputed reading as certain.
- Bridge to specific, honest application.

### Must Not
- Overclaim ("this verse proves…") beyond what the text supports.
- Invent illustrations-as-fact, statistics, quotes, cross-references, or original-language claims — route illustrations to `biblical_sermon_illustration_finder.md` and language to the word-study prompt.
- Use the sermon to assert a contested doctrine as settled without acknowledgment.

### Tradition-neutral stance (Must / Must Not)
- **Must:** acknowledge where faithful interpreters differ on a contested text.
- **Must Not:** present a contested reading as the indisputable meaning.

---

## Instructions

### Step 1 — Anchor in the text
Summarize the passage's meaning in context (from exegesis). Note genre, structure, and key terms (route language questions out).

### Step 2 — Big idea
State the sermon's big idea in one sentence — the text's main point, not a topic.

### Step 3 — Outline from the text
Build 2–4 points that arise from the passage's structure/flow, each tied to specific verses (by address) and serving the big idea.

### Step 4 — Application
For each point or for the whole, derive specific application honestly (route deeper work to the application-bridge prompt).

### Step 5 — Illustration & introduction/conclusion notes
Note where an illustration would serve (hand off to the guarded illustration prompt), and sketch an intro that raises the need and a conclusion that lands the big idea.

### Step 6 — Honesty check
Confirm nothing in the outline overclaims; flag any contested point and how it's handled.

---

## Output Format

```
# Expository Sermon — [reference]

## Text anchor
- Meaning in context: [..] | Genre/structure: [..] | Key terms (→ word study): [..]

## Big idea
> [one sentence]

## Outline
1. [point] ([verses]) → serves big idea by [..]
2. [point] ([verses]) ...

## Application
- [specific, honest application per point/whole]

## Illustration / intro / conclusion notes
- Illustration slots (→ guarded illustration prompt): [..]
- Intro: [..] | Conclusion: [lands big idea]

## Honesty check
- Overclaim check: [pass/flags] | Contested points handled: [..]
```

---

## Verification

- [ ] Big idea is the text's point, in one sentence.
- [ ] Points arise from the text's structure and tie to verses by address.
- [ ] No overclaiming beyond the exegesis.
- [ ] Illustrations routed out; no fabricated facts/quotes/stats/lexical claims.
- [ ] Contested readings acknowledged, not asserted as settled.
- [ ] Application specific and honest.

---

## False-Positive Prevention

❌ **DON'T:**
- Make the passage say more than it does to land a point.
- Insert a moving "true story" or statistic without verification.
- Preach a disputed interpretation as beyond question.
- Build points the text's structure doesn't actually support.

✅ **DO:**
- Let the big idea and points come from the text itself.
- Route illustrations to the guarded prompt and language to the word study.
- Acknowledge contested readings honestly.
- Keep application specific and text-derived.
