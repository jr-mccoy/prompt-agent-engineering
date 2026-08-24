---
title: "Trial Theme and Narrative Designer"
category: legal/litigation
description: "Build a unifying trial theme, opening-statement architecture, witness order, exhibit narrative arc, and closing framework — anchored to record evidence and the controlling jury instructions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - litigation
  - trial-strategy
  - opening-statement
  - witness-order
updated: "2026-05-11"
related_prompts:
  - domain-legal/litigation/legal_jury_instruction_drafter.md
  - domain-legal/litigation/legal_motion_in_limine_set.md
  - domain-legal/depositions/legal_deposition_outline_witness.md
---

**Purpose:** Produce a trial theme and narrative architecture: the one-sentence theme, the opening-statement structure, the order of witnesses, the exhibit progression that lets the jury see the story unfold, and the closing-argument call-back map.

**When to use:** 60–120 days before trial; after the pretrial order locks witness and exhibit lists; after dispositive motions have narrowed issues; when preparing for mock or focus-group testing.

---

## Your Input

- **Case type:** [Civil / criminal; substantive area]
- **Posture:** [Plaintiff / defendant / prosecution / defense]
- **Jurisdiction:** [Federal/state, court]
- **Issues remaining for trial:** [List]
- **Jury instructions (controlling):** [Pattern instructions to be given, or `[NEED: pattern]`]
- **Witnesses available:**
  - Name, role, what they prove, vulnerabilities (impeachment risk, demeanor, prior inconsistent statements)
- **Exhibits available:**
  - Number, description, source witness, weight
- **Key opposing evidence the jury will hear:**
- **Damages or punishment theory:** [Compensatory categories, statutory, punitive; or sentencing exposure]
- **Demographic and venue notes:** [Jury pool composition, prior verdict patterns where supplied]
- **Mock trial / focus group findings:** [If any]

---

## Constraints

**Must:**
- Anchor the theme to **record evidence** — every claim made in opening must be provable by an identified witness or exhibit.
- Tie the theme to **the jury instructions** the jury will receive. The narrative carries the burden of proof or burden of persuasion the instructions impose.
- Build the **witness order** to advance the story, not to follow chronology blindly.
- For each witness, specify what story-beat they advance, what evidence they introduce, and what risk they carry on cross.
- Identify **promises made in opening that must be kept** by a specific witness/exhibit — the "promise ledger."
- Build a **closing-argument call-back map**: each theme element maps to specific witness testimony and exhibits.

**Must Not:**
- Promise evidence in opening that the witness list cannot deliver.
- Build a theme that contradicts a stipulated fact or controlling instruction.
- Use arguments that violate the rules of opening statement (no argument, no inadmissible evidence references).
- Invent witness statements or exhibit content not supplied.
- Default to clichéd themes ("This is a case about greed") without tying them to record proof.

---

## Instructions

1. **Distill the theme.** Write three candidate one-sentence themes. Select the one that (a) tracks the controlling jury instruction, (b) is provable by available evidence, and (c) survives a "what would opposing counsel say" stress test.
2. **Build the opening-statement skeleton.**
   - Hook (60–90 seconds): the central image or moment
   - Roadmap of the evidence ("You will hear...")
   - Promises ledger (explicit list of "you will hear/see X")
   - Why this case matters (without argument)
   - Verdict ask
3. **Order the witnesses.** Build a "primacy / recency" lineup:
   - Primacy witness: strong, credible, sets the frame
   - Middle witnesses: introduce documents, build elements
   - Recency witness: strong closer, often damages or summary witness
   - Adverse witnesses: place where impeachment is contained
4. **Map exhibits to witnesses.** Build the chain — each key document enters through a witness whose testimony lays foundation, then re-appears in closing.
5. **Identify the cross-examination gauntlet.** For each of the user's witnesses, identify the 3–5 cross-examination attacks and the defensive plan.
6. **Anticipate opposing themes.** Write the opposing party's three best theme candidates and the rebuttal for each.
7. **Build the closing call-back map.** Each opening promise → witness that delivered → exhibit that proved it → jury-instruction element it satisfies.
8. **Stress test.** Identify the single biggest piece of opposing evidence and confirm the theme accommodates (not denies) it.

---

## Output Format

```markdown
# TRIAL THEME & NARRATIVE — {Matter}

## Theme
**One-sentence theme:** "{Theme}"
- Tracks jury instruction: {citation to pattern}
- Provable by: {top 3 witnesses + 3 exhibits}
- Survives opposing rebuttal: {brief}

## Opening Statement Architecture
1. **Hook (90s):** {moment / image}
2. **Roadmap:** {what jury will see}
3. **Promises Ledger:**
   - You will hear from {Witness} that {fact}.
   - You will see {Exhibit} showing {fact}.
   - ...
4. **Why It Matters:** {non-argumentative significance}
5. **Verdict Ask:** {one sentence}

## Witness Order

| # | Witness | Role | Story Beat | Exhibits Introduced | Cross Risks | Mitigation |
|---|---|---|---|---|---|---|
| 1 | {Primacy} | | | | | |
| 2 | | | | | | |
| ... | | | | | | |
| Last | {Recency} | | | | | |

## Exhibit Narrative Arc

| Exhibit | Beat | Sponsoring Witness | Foundational Predicate | Closing Call-back |
|---|---|---|---|---|

## Opposing Theme Anticipation

| Opposing Theme | Likely Evidence | Our Rebuttal |
|---|---|---|

## Closing Call-Back Map

| Opening Promise | Witness Delivered | Exhibit Proved | Instruction Element Satisfied |
|---|---|---|---|

## Theme Stress Test
- Single hardest opposing fact: {item}
- How theme accommodates: {brief}
```

---

## Verification

- [ ] Theme is one sentence and tracks a controlling jury instruction.
- [ ] Every promise in opening has a named witness and exhibit on the order list.
- [ ] Witness order has explicit primacy and recency choices with rationale.
- [ ] Every key exhibit has a sponsoring witness with foundation laid.
- [ ] Cross-examination risks are identified for each user witness.
- [ ] Opposing themes anticipated with rebuttals.
- [ ] Closing call-back map closes every opening promise.
- [ ] Theme accommodates, rather than denies, the strongest opposing fact.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Theme that argues rather than frames | Themes should be evidentiary frames, not legal conclusions ("Promises broken" not "Breach of contract") |
| Promises in opening that no witness can deliver | Every promise must trace to a named witness on the order list with deposition or interview support |
| Witness order by chronology | Chronology is for the witnesses; primacy/recency is for the jury — order around impact, not the calendar |
| Ignoring the strongest opposing fact | Themes that pretend bad facts don't exist collapse on cross — accommodate explicitly |
| Generic "this is a case about X" themes | The theme should be evidentiary-specific and survive the "so what?" test |
| Stipulated facts that contradict the theme | Audit stipulations before drafting; revise theme if necessary |
| Closing that ignores opening promises | The promises ledger is a contract with the jury — the closing must redeem it |
| Theme that violates an MIL ruling | Cross-check against MIL grants and motions filed |
