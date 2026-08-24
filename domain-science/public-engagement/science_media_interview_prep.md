---
title: "Science Media Interview Prep"
category: science/public-engagement
description: "Build a message map, Q&A bank with bridge phrases, and traps-to-avoid list so a researcher can discuss a finding accurately under interview pressure."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - media-training
  - interview-prep
  - science-communication
  - bridge-phrases
  - uncertainty-communication
  - overclaim-avoidance
  - message-map
  - analogies
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_explainer_for_general_audience.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Science Media Interview Prep

**Objective:** Prepare a researcher to discuss a finding with journalists accurately and confidently. Produce a tight message map (3 messages max), a Q&A bank with bridge phrases and honest answers to the hardest questions, non-misleading analogies, and an explicit list of claims not to make — so uncertainty is expressed plainly without sounding evasive.

**When to use:** Before a print, radio, podcast, or on-camera interview about a published or preprinted study, especially when the result is preliminary, contested, easily sensationalized, or carries policy stakes.

**Required inputs:**
- **Discipline.** The scientific field of the work.
- **Study type.** Observational / experimental / RCT / meta-analysis / modeling / animal / in vitro / preprint, etc.
- **The finding(s)** (user-supplied; never invented) and the audience/outlet (general public via TV, science podcast, trade press, etc.).
- **Interview format and length** (live vs recorded; minutes available).

**Optional inputs:**
- Known limitations, effect size, and sample details.
- The angle the journalist is likely pursuing.
- Prior coverage or controversy on the topic.
- Funding/COI the reporter may raise.

**Constraints — Must:**
- Hold to three key messages or fewer; each must be defensible from the user-supplied data.
- Provide bridge phrases that redirect to a message without dodging the question.
- Give an honest answer to each hard/"gotcha" question, including "we don't know yet" where true.
- Express uncertainty in plain, confident language (state what is known, the bound of what is not, and the next step).
- Offer analogies only if they do not distort the mechanism or the certainty level.
- Calibrate to the evidence: correlation is not causation; a single study is not settled; pair effect size with a limitation.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, or certainty. Draft only from user-supplied results; mark gaps `[user-supplied]`.
- Do not script hype: "novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves." Substitute calibrated phrasing.
- Do not coach answers that imply human applicability from animal/in-vitro work or causation from associational designs.
- Do not coach evasion; "I don't know" or "that's outside what this study can tell us" is the prescribed move when applicable.

**Instructions:**

1. **Intake and classify.** Capture discipline, study type, the finding, outlet/audience, and format/length. Note whether the design supports causal language.
2. **Distill the message map.** Write up to three key messages, each a sentence the data support exactly, ordered by what the audience most needs to hear.
3. **Build bridge phrases.** Draft transitions ("What matters here is…," "The key point is…," "That's a common question, and what the study actually shows is…") that move from a question to a message without ignoring it.
4. **Anticipate hard questions.** Generate the toughest, most sensationalizing, and most adversarial questions a journalist could ask, including ones that invite overclaiming, and write honest, calibrated answers.
5. **Draft the uncertainty playbook.** Provide ready phrasings for expressing limits confidently and a standing rule: if you don't know, say so and say what would answer it.
6. **Vet analogies.** Offer one or two analogies and explicitly note where each breaks down so it is not over-applied.
7. **List what not to claim.** Enumerate the specific overclaims (causation, cure, human leap, settledness) most likely to be tempting for this finding.
8. **Deliver.** Output the message map, Q&A bank, uncertainty playbook, vetted analogies, and traps-to-avoid list.

**Output format (locked):**

```
## Message Map (max 3)
1. [message — data-supported]
2. [...]
3. [...]

## Bridge Phrases
- [phrase] → [message it routes to]
- [...]

## Q&A Bank
| # | Likely question | Honest, calibrated answer | Note (trap / why) |
|---|---|---|---|
| 1 | [hard / gotcha] | [...] | [...] |

## Uncertainty Playbook
- Standing rule: "If I don't know, I say so — and say what would tell us."
- Phrasings: [confident statements of limits]

## Analogies (use with care)
- [analogy] — works because [...]; breaks down at [...]

## Traps to Avoid (do NOT claim)
- [ ] [causal language not supported by design]
- [ ] [human applicability from animal/in-vitro work]
- [ ] [cure / breakthrough / proves / first-ever]
- [ ] [single study framed as settled]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication and media-training best practice — message-mapping, bridging without dodging, overclaim/"churnalism" avoidance, plain-language uncertainty, and the "what this does and does NOT show" + "if I don't know, I say so" framing.

**Verification checklist (before delivering):**
- [ ] No more than three key messages, each supported by user-supplied data.
- [ ] Every bridge phrase redirects without dodging the question.
- [ ] Each hard question has an honest answer, including "we don't know" where true.
- [ ] Uncertainty phrasings sound confident, not evasive.
- [ ] Analogies include an explicit "breaks down at" note.
- [ ] Traps list names causation, human-leap, cure, and settledness risks specific to this finding.
- [ ] No banned hype words appear in any scripted answer.
- [ ] No invented statistics, quotes, or citations; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Confident dodge | A smooth bridge that ignores the actual question | Each bridge must first acknowledge the question, then redirect |
| Misleading analogy | A vivid comparison that overstates certainty or mechanism | Require a "breaks down at" caveat for every analogy |
| Hedge-as-evasion | "I can't comment" where an honest limit exists | Replace with stated bound + next step that would resolve it |
| Pressure overclaim | Caving to a "so this could cure X?" prompt | Pre-scripted "that's beyond what this study shows" answer |
| Species/causal leap | Coaching human/causal phrasing from non-human/associational data | Tag the design in intake; audit every answer against it |
