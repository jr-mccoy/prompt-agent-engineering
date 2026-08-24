---
title: "Social Media Thread Drafter"
category: science/public-engagement
description: "Drafts a calibrated social-media thread about a scientific finding that leads with the takeaway, links the primary source, flags uncertainty, and avoids hype and dunking."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - social-media
  - science-communication
  - calibrated-certainty
  - primary-source
  - overclaim-avoidance
  - thread
  - uncertainty
  - public-engagement
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_explainer_for_general_audience.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Social Media Thread Drafter

**Objective:** Draft a short, numbered social-media thread that communicates a scientific finding to a general audience with calibrated certainty. The thread leads with the accurate takeaway, states the finding and its limits, links the primary source, flags what the result does NOT show, and includes a correction plan — while avoiding hype, dunking, and overclaim. The deliverable also includes a self-check that asks whether each post is "dunkable-but-wrong."

**When to use:** You want to post about a study, dataset, or scientific claim (your own or someone else's, supplied by you) on a threaded platform and need a draft that informs without overstating, oversimplifying, or inviting a viral-but-wrong correction.

**Required inputs:**
- **Discipline.** <field, e.g., nutrition science, materials, ecology>
- **Study type.** <observational / experimental / modeling / review / preprint>
- **The finding(s) / claim** (user-supplied; never invented) and the audience/forum — the result you want to share, and the platform and who you expect to read it.
- **Primary-source link.** URL/DOI of the paper, preprint, dataset, or registration (user-supplied).

**Optional inputs:**
- Key limitations or caveats from the paper.
- Effect size, sample size, confidence interval, or other numbers (user-supplied).
- Conflicts of interest or funding to disclose.
- A specific misreading you want to preempt.
- Platform post-length limit and desired thread length.

**Constraints — Must:**
- Lead the first post with the single most accurate takeaway, calibrated (not the most clickable version).
- State both the finding and at least one concrete limitation.
- Link the primary source (paper/preprint/data/registration) explicitly in the thread.
- Flag uncertainty and include an explicit "what this does NOT show" post.
- Keep empirical claims separate from value or policy opinion; label opinion as opinion.
- Include a correction plan: how the author will visibly correct the thread if something turns out wrong.
- Disclose conflicts of interest or funding where relevant.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, opponents' positions, or certainty. Draft only from user-supplied facts; mark gaps `[user-supplied]`.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves") in the drafted posts.
- Do not "dunk" — no ridicule, no quote-tweet pile-ons, no implying bad faith in people who disagree.
- Do not imply causation from an associational/observational result, or treat a single study as settled science.

**Instructions:**

1. **Confirm the core.** Restate discipline, study type, the user-supplied finding, the primary-source link, and the audience. Mark anything missing `[user-supplied]` (especially a missing source link — flag that the thread should not post without it).
2. **Write the takeaway post.** Compose post 1 as the calibrated headline: accurate, plain, and not more certain than the evidence. Avoid hype and clickbait framing.
3. **State finding + limit.** In the next post(s), give the finding with any user-supplied numbers, then immediately a concrete limitation (sample, design, generalizability, single study).
4. **Add the "does NOT show" post.** Explicitly name the conclusions readers might wrongly draw and state that the result does not support them.
5. **Link and disclose.** Add the primary-source link and, where relevant, a COI/funding disclosure post.
6. **Separate fact from opinion.** If the thread includes any interpretation or policy view, isolate it in its own post and label it as opinion.
7. **Set tone.** Keep the register informative and non-condescending; remove any dunking, sarcasm at people, or bad-faith implication.
8. **Write the correction plan.** Add a short note (for the author, plus optional pinned-reply language) describing how a correction will be issued if the thread is wrong.
9. **Run the overclaim / dunkable self-check.** For each post, ask: is this more certain than the evidence? Could a knowledgeable reader screenshot this as "confidently wrong"? Am I dunking? Revise any post that fails.

**Output format (locked):**

```
## Thread Core (confirmed)
- Discipline / study type:
- Finding (user-supplied):
- Primary-source link (user-supplied):
- Audience / platform:

## Drafted Thread
1/ [calibrated takeaway]
2/ [finding + user-supplied numbers]
3/ [concrete limitation]
4/ [what this does NOT show]
5/ [primary-source link]
6/ [COI / funding disclosure, if any]
n/ [opinion, labeled — if any]

## Correction Plan
- If wrong, I will: [visible-correction approach]
- Pinned-reply language (optional): [...]

## Overclaim / "Dunkable-but-Wrong" Self-Check
| Post | More certain than evidence? | Could be screenshotted as confidently wrong? | Dunking? | Fix applied |
|---|---|---|---|---|
| 1/ |  |  |  |  |
| ... |  |  |  |  |
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication best practice for social media — lead with the accurate takeaway, link the primary source, flag uncertainty and the limits of the result, separate empirical claims from opinion, and avoid hype and dunking.

**Verification checklist (before delivering):**
- [ ] Post 1 is the calibrated takeaway, not the most clickable framing.
- [ ] At least one concrete limitation is stated.
- [ ] A primary-source link is present (or its absence is flagged as blocking).
- [ ] There is an explicit "what this does NOT show" post.
- [ ] No hype words appear in any post.
- [ ] Causation is not implied from associational/observational data; single study not framed as settled.
- [ ] No dunking, ridicule, or bad-faith implication.
- [ ] Correction plan and overclaim/dunkable self-check are completed; no invented numbers.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Clickbait takeaway | A punchy post 1 that's technically defensible but implies more than the data show | Calibrate post 1 to the evidence; run the "more certain than evidence?" self-check |
| Causal leap | "X causes Y" from an observational study, phrased confidently | Force associational language for non-experimental designs; "does NOT show" post names the causal misread |
| Missing source | A persuasive thread with no link, so readers can't check it | Block posting without a primary-source link; mark `[user-supplied]` if absent |
| Dunk for engagement | Ridiculing a bad take to score reach, which invites pile-ons and distortion | Tone pass removes ridicule; correct claims, not people |
| Hidden opinion | A policy preference woven into "the science says" posts | Isolate and label opinion; keep empirical posts free of value judgments |
```
