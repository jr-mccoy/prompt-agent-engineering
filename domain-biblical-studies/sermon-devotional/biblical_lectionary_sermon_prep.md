---
title: "Lectionary Sermon Prep — Preach from Assigned Readings"
category: biblical-studies/sermon-devotional
description: "Prepare a sermon from lectionary-assigned readings (user supplies the readings) — weaving multiple texts into a unified message with a shared theological thread, while handling the unique challenges of lectionary preaching: texts chosen for you, multiple readings, and the tension between the lectionary's logic and your congregation's context."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: intermediate
tags:
  - lectionary
  - sermon
  - preaching
  - liturgical
  - readings
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/sermon-devotional/biblical_expository_sermon_prep.md
  - domain-biblical-studies/sermon-devotional/biblical_liturgical_calendar_devotional_series.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_series_planner.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_manuscript_draft.md
---

# Lectionary Sermon Prep

> **STRONG-GUARD prompt.** The model must not assert lectionary readings from memory. The user supplies the readings (by address) and identifies the lectionary (RCL, Roman Lectionary, etc.). Every lectionary-assignment claim is verify-required. The model works with the texts the user provides.

**Objective:** Help a preacher prepare a sermon from lectionary-assigned readings — finding the theological thread that connects the readings, choosing a primary text (or weaving multiple), and producing a sermon plan that is faithful to the texts and responsive to the congregation — without the model asserting which readings are assigned.

**When to use:**
- You preach from a lectionary and have this week's assigned readings.
- You want help finding the connection between the OT, Psalm, Epistle, and Gospel readings.
- You are new to lectionary preaching and want a workflow.

**When NOT to use:**
- You choose your own text (not lectionary-based) — use `biblical_expository_sermon_prep.md`.
- You are designing a devotional for a liturgical season — use `biblical_liturgical_calendar_devotional_series.md`.

**Audience:** Pastors (P) who preach from a lectionary.

---

## Inputs / Context

1. **The readings.** The user supplies the assigned readings by address (OT, Psalm, Epistle, Gospel) and identifies the lectionary and year/cycle.
2. **Liturgical season.** Where this Sunday falls in the church year.
3. **Congregation context.** Size, tradition, current series or emphasis, and any pastoral concerns for this week.
4. **Preaching approach.** Will the preacher focus on one text (with others supporting), weave all four, or pair two?
5. **Time target.** How long the sermon should be.

---

## Constraints

### Must
- Work only with the readings the user supplies — never assert or correct lectionary assignments.
- Help the preacher find the theological thread connecting the readings (the lectionary's logic).
- Support multiple approaches: single-text focus, paired-text, or all-four weaving.
- Produce a sermon plan (big idea, structure, moves) — not just exegetical notes.
- Note where a reading touches contested ground and handle with multi-view honesty.

### Must Not
- Assert lectionary readings from memory — the user supplies them. If the user asks "what are this Sunday's readings," respond: "Please supply the readings or consult [lectionary name]. I cannot assert them from memory."
- Fabricate commentary claims, scholar attributions, or liturgical-tradition assertions.
- Force all four readings into the sermon if the preacher's approach is single-text.
- Pre-decide a contested passage's reading as the sermon's settled position.

### Tradition-neutral stance (Must / Must Not)
- **Must:** respect the preacher's declared tradition and its lectionary emphases.
- **Must Not:** privilege one lectionary tradition over another (RCL vs. Roman vs. other).

---

## Instructions

### Step 1 — Confirm readings and context
Restate the four readings (by address), the lectionary and cycle, the liturgical season, the congregation context, and the preaching approach. Flag any reading that is textually complex or pastorally sensitive.

### Step 2 — Exegetical scan of each reading
For each text the user supplied, provide a brief scan: genre, context in its book, key interpretive questions, and how it has been read in different traditions. Note contested issues. All claims about the text are verify-required against the user's translation.

### Step 3 — Find the theological thread
Identify the thread (or threads) the lectionary seems to be drawing between the readings. Name the shared theme, tension, or movement. If the readings don't obviously connect, note that — some Sundays the connection is looser.

### Step 4 — Build the sermon plan
Based on the preacher's approach:
- **Big idea:** one sentence that captures the sermon's claim.
- **Structure:** 3–4 moves with transitions.
- **Text engagement:** which reading(s) are primary, and how the others support or complicate.
- **Application:** concrete and congregationally specific.
- **Illustration placement:** [ILLUSTRATION: topic] placeholders — do not fabricate.

### Step 5 — Liturgical integration notes
Suggest how the sermon connects to the liturgical season, any responsive elements (communion, prayer, confession), and how the readings might be introduced or read in the service.

---

## Output Format

```
# Lectionary Sermon Plan — [Sunday / occasion] ([lectionary, cycle])

## Readings (user-supplied — VERIFY)
- OT: [address] | Psalm: [address] | Epistle: [address] | Gospel: [address]

## Exegetical scan
### [Reading 1]
- Genre: [..] | Context: [..] | Key question: [..] | Contested: [..]
[repeat for each reading]

## Theological thread
- Connection: [..] | Tension: [..] | Lectionary logic: [..]

## Sermon plan
- Big idea: [one sentence]
- Structure:
  1. [Move 1 — text engagement + transition]
  2. [Move 2]
  3. [Move 3]
- Application: [..] | [ILLUSTRATION: topic]

## Liturgical integration
- Season connection: [..] | Responsive element: [..] | Reading introduction: [..]
```

---

## Verification

- [ ] Only user-supplied readings are used — no lectionary assignments from memory.
- [ ] The theological thread between readings is identified.
- [ ] The sermon plan has a big idea, structure, and application.
- [ ] Contested passages are handled with multi-view honesty.
- [ ] No fabricated commentary, scholar claims, or illustrations.
- [ ] Liturgical integration is addressed.

---

## False-Positive Prevention

DON'T:
- Assert lectionary readings from memory.
- Force all four readings into the sermon if the preacher chose a single-text approach.
- Fabricate illustrations or commentary claims.

DO:
- Work with the readings the user supplies.
- Find the lectionary's theological thread — that's the unique value of lectionary preaching.
- Flag contested passages for honest handling.
