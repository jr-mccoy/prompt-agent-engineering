---
title: "Rhetorical Analysis — Devices and Persuasive Strategy"
category: biblical-studies/exegesis-interpretation
description: "Identify and analyze rhetorical devices (chiasm, anaphora, antithesis, inclusio, hyperbole, rhetorical question, irony) and the author's persuasive strategy in a biblical passage — covering Greco-Roman oratorical conventions (for epistles) and Hebrew rhetorical patterns (for prophetic and wisdom texts) — without over-reading structure or claiming devices not supported by the text."
techniques:
  - ST-02
  - RT-02
  - ED-03
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - rhetoric
  - literary-analysis
  - persuasion
  - devices
  - exegesis
updated: "2026-06-07"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/exegesis-interpretation/biblical_genre_aware_reading.md
---

# Rhetorical Analysis — Devices and Persuasive Strategy

**Objective:** Identify the rhetorical devices active in a passage and analyze how they serve the author's communicative strategy — so the reader grasps not just *what* is said but *how* the text persuades, moves, or teaches.

**When to use:**
- A passage uses repeated structures, vivid contrasts, or escalating patterns that seem designed to do something rhetorically.
- Analyzing an epistle whose argument follows a discernible persuasive shape (deliberative, forensic, epideictic).
- Studying how Hebrew poetry or prophetic speech uses repetition, inversion, and climax to create emphasis.
- Preparing a sermon or lesson that wants to honor how the text itself seeks to persuade, not just what it states.

**When NOT to use:**
- You need macro-level discourse structure (how the passage fits the book) — use `biblical_literary_context_structure.md`.
- You need genre identification before rhetorical analysis — start with `biblical_genre_aware_reading.md`.
- You're studying the passage's historical setting — use `biblical_historical_cultural_context.md`.

**Audience:** Pastors (P), seminary/academic (A), equipped group leaders (G).

---

## Inputs / Context

1. **The passage.** Reference and text in a named translation (pasted by the user).
2. **Rhetorical question (optional).** A specific focus: "Is there a chiasm here?" or "What is Paul trying to achieve rhetorically?"
3. **Declared tradition (optional).** May shape emphasis; default is to cover both Greco-Roman and Hebrew conventions where relevant.
4. **Genre (if known).** Epistle, prophecy, wisdom/poetry, narrative, apocalyptic — different genres activate different rhetorical conventions.

---

## Constraints

### Must
- Identify devices by name and locate them precisely in the text with the wording that demonstrates each one.
- Distinguish devices that are **clearly present** (strong textual evidence), **possible** (plausible but not certain), or **proposed/contested** (worth noting, but debated in scholarship).
- Explain what each identified device *does* — what emphasis, contrast, emotional effect, or logical move it creates.
- Cover the relevant rhetorical tradition for the genre: Greco-Roman conventions (species of rhetoric, dispositio, elocutio) for NT epistles; Hebrew conventions (parallelism types, inclusio, chiasm, merism) for OT poetry and prophecy.
- Where a device identification is contested — especially chiasm, which is frequently over-read — say so and name the debate.

### Must Not
- Invent a chiasm by cherry-picking non-adjacent terms without continuous, parallel structure.
- Claim a device is present without showing the specific wording that demonstrates it.
- Use rhetorical analysis to pre-decide a contested theological interpretation; route those to `biblical_multiview_interpretation_map.md`.
- Invent citations, cross-references, or original-language claims; reference by address and route language questions to `biblical_word_study_original_language.md`.
- Impose Greco-Roman rhetorical categories (inventio, dispositio, elocutio) onto Hebrew poetry where they do not apply.

### Tradition-neutral stance (Must / Must Not)
- **Must:** acknowledge that rhetorical conventions are tradition-specific in some applications; note contested device identifications.
- **Must Not:** present a tradition-favored rhetorical reading as the established scholarly one.

---

## Instructions

### Step 1 — Identify the rhetorical tradition
Name the applicable rhetorical tradition(s) for this passage — Greco-Roman, Hebrew, or both — based on genre, author, and audience. Briefly note which categories are relevant.

### Step 2 — Catalogue the devices
List each rhetorical device you can identify, with:
- The device name and a one-line definition.
- The specific wording from the user's supplied text (by address/line) that demonstrates it.
- A confidence label: **clearly present** / **possible** / **proposed/contested**.

### Step 3 — Interpret each device's function
For each clearly present device, state what rhetorical work it does: what it emphasizes, how it structures the reader's attention, what emotional or logical effect it creates.

### Step 4 — Analyze the persuasive strategy
Step back from individual devices and characterize the passage's overall rhetorical goal: What is the author trying to achieve? How do the devices work together to achieve it?

### Step 5 — Caveats and contested identifications
Name any device you identified as possible or contested, explain the alternative reading, and note what would confirm or disconfirm it.

---

## Output Format

```
# Rhetorical Analysis — [reference]

## Rhetorical tradition(s) in play
- [Greco-Roman / Hebrew / both]: [why this applies] | Relevant categories: [..]

## Devices catalogue
| Device | Where in text (address/line) | Confidence | What it does |
|--------|------------------------------|-----------|--------------|
| [name] | [wording/address] | clearly present / possible / contested | [function] |

## Persuasive strategy
- Goal: [what the author is trying to achieve]
- How the devices work together: [..]

## Caveats
- Possible/contested identifications: [device] — [alternative reading] — [what would confirm/disconfirm]
```

---

## Verification

- [ ] Each device located with specific wording from the supplied text, not asserted in the abstract.
- [ ] Confidence labeled for each device: clearly present / possible / contested.
- [ ] Device function explained — not just named.
- [ ] Rhetorical tradition matched to the genre; Greco-Roman categories not imposed on Hebrew poetry.
- [ ] Persuasive strategy characterized as a whole, beyond the device list.
- [ ] No invented chiasms, cross-references, or original-language claims.
- [ ] Contested identifications flagged with the alternative reading.

---

## False-Positive Prevention

❌ **DON'T:**
- Manufacture a chiasm by selecting non-adjacent terms and rearranging them.
- Name a device (e.g., "anaphora") without quoting the actual wording that demonstrates it.
- Treat a rhetorical reading as settling a disputed interpretation.
- Impose Greco-Roman dispositio onto a Hebrew psalm or prophetic oracle.
- Over-identify devices to make the analysis look richer — "possible" and "contested" are honest labels.

✅ **DO:**
- Show the specific wording that demonstrates each device.
- Label each identification clearly present / possible / contested.
- Explain what the device accomplishes, not just what it is called.
- Match the rhetorical tradition to the genre.
- Reserve interpretive weight for devices that are clearly present.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 5-step workflow (Rhetorical tradition → Catalogue devices → Interpret function → Analyze strategy → Caveats) moves from identification to interpretation to overall assessment in a disciplined sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across multiple dimensions — device type, textual location, confidence level, rhetorical function, and overall persuasive strategy — preventing a flat list of device names without explanation.
- **ED-03 (Guided Discovery):** Rather than asserting rhetorical labels, the instructions guide identification from the text's own wording, making device recognition a learnable, transferable skill.
- **QA-01 (Self-Verification):** The Verification checklist confirms that each device is located in specific wording, that confidence is labeled, that functions are explained rather than merely named, and that the rhetorical tradition matches the genre.
- **QA-04 (Uncertainty Acknowledgment):** A confidence label (clearly present / possible / contested) is required for every identified device, with contested identifications flagged in a dedicated Caveats section — protecting against the common tendency to over-read rhetorical structure.
