---
title: "Science Press Release Drafter"
category: science/public-engagement
description: "Draft an accurate-first institutional press release from user-supplied results, calibrated against overclaim risk with a built-in self-audit."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - press-release
  - science-communication
  - overclaim-avoidance
  - uncertainty-disclosure
  - churnalism
  - embargo
  - plain-language
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_explainer_for_general_audience.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Science Press Release Drafter

**Objective:** Draft an institutional press release that communicates a scientific finding clearly without outrunning the data. The release pairs a plain-language summary with its study type, limitations, funding/COI disclosure, and a link to the primary source, then runs an overclaim self-audit so no sentence implies causation, cure, or settledness the evidence does not support.

**When to use:** After a study is accepted, posted as a preprint, or otherwise cleared for public release, and you need a press release that the communications office, the researchers, and downstream journalists can all stand behind.

**Required inputs:**
- **Discipline.** The scientific field (e.g., oncology, climate science, social psychology).
- **Study type.** Observational / experimental / RCT / meta-analysis / modeling / animal / in vitro / preprint, etc.
- **The finding(s)** (user-supplied; never invented) and the audience (general public, science journalists, trade press, donors).
- **The primary source link** (DOI, preprint URL, or "[user-supplied]").

**Optional inputs:**
- Researcher quote(s) (verbatim and attributed) or permission to draft a quote marked for approval.
- Sample size, effect size, and key limitations.
- Funding sources and conflict-of-interest statements.
- Embargo date/time and contact details.
- Data/code availability links.

**Constraints — Must:**
- Open the headline and lede with claims that the data actually support; lead with what was observed, not what it might mean someday.
- State the study type and population in plain language early (e.g., "in mice," "in 80 volunteers," "an association, not proof of cause").
- Pair every claim of benefit or effect with its principal limitation in the same paragraph.
- Disclose funding sources and any conflicts of interest.
- Link to the peer-reviewed paper, preprint, and/or data so readers can verify.
- Calibrate certainty to the evidence: correlation is not causation; a single study is not settled; report effect size and a limitation together.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, or certainty. Draft only from user-supplied results; mark gaps `[user-supplied]`.
- Do not use hype words in the drafted release: "novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves." Substitute calibrated claims.
- Do not imply human applicability from animal or in-vitro work, or causation from associational designs.
- Do not present a single study, preprint, or unreplicated result as definitive or consensus.

**Instructions:**

1. **Intake and classify.** Capture discipline, study type, the finding, audience, and the source link. If the study type is associational or non-human, flag it as a recurring caveat to thread through the whole release.
2. **State the core claim at the right altitude.** Reduce the finding to one sentence that the data support exactly — no extrapolation. This becomes the spine of the headline and lede.
3. **Write the headline and lede.** Make them accurate before catchy. The headline must not assert causation, cure, or finality the data lack; the lede answers who/what/where and names the study type.
4. **Explain the finding in plain language.** Translate one layer below the abstract, preserving the confirmatory-vs-exploratory and association-vs-causation distinctions. State effect size in human terms where possible.
5. **Place the caveats.** Surface sample limits, animal-vs-human gap, correlation, preliminary/unreplicated status, and generalizability. Do not bury them at the bottom.
6. **Add the quote.** Use a user-supplied verbatim quote, or draft one marked `[DRAFT — researcher to approve]` that stays within the calibrated claim and avoids hype.
7. **Disclose funding, COI, and open-science links.** Add funder(s), conflicts, and links to the paper/preprint/data/code. Note embargo if supplied.
8. **Run the overclaim self-audit.** Re-read each sentence and ask: does it imply causation, human applicability, cure, or settledness the data don't support? Flag and rewrite offenders.
9. **Deliver.** Output the release followed by the audit table.

**Output format (locked):**

```
## Press Release

FOR [IMMEDIATE RELEASE | EMBARGOED UNTIL <date/time>]

### Headline
[accurate, hype-free]

### Subhead (optional)
[one line of calibrated context]

[CITY, DATE] — [Lede: finding + study type + population, in plain language.]

[Paragraph 2: what the finding means and does NOT mean; effect size; confirmatory vs exploratory.]

[Paragraph 3: caveats — sample, animal-vs-human, correlation, preliminary status, generalizability.]

"[Quote]," said [Name, role, institution]. [verbatim or DRAFT — to approve]

[Paragraph 4: what comes next / open questions.]

### Study details
- Study type: [...]
- Sample / model: [...]
- Funding: [user-supplied]
- Conflicts of interest: [user-supplied]
- Paper / preprint: [link or user-supplied]
- Data / code availability: [link or user-supplied]

### Media contact
[user-supplied]

## Overclaim Self-Audit
| Sentence / phrase | Risk flagged | Calibrated rewrite |
|---|---|---|
| [...] | [causation implied / human leap / cure / settledness / hype word] | [...] |

Audit verdict: [PASS / REVISE — reasons]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication best practice — the press-release-overclaim literature (exaggeration in releases drives exaggerated news, "churnalism"), overclaim avoidance, uncertainty disclosure, embargo/Ingelfinger norms, and "what this does and does NOT show" framing.

**Verification checklist (before delivering):**
- [ ] Headline and lede do not assert causation, cure, or finality the data lack.
- [ ] Study type and population are stated in plain language near the top.
- [ ] Every benefit/effect claim sits beside its principal limitation.
- [ ] No banned hype words ("breakthrough," "cure," "proves," etc.) appear in the drafted text.
- [ ] Animal/in-vitro results are not implied to apply to humans.
- [ ] Effect size and at least one limitation are reported together.
- [ ] Funding, COI, and a primary-source link are present (or marked `[user-supplied]`).
- [ ] The overclaim self-audit table is completed with a PASS/REVISE verdict.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Causal creep | "Drug X reduces risk" from an observational association | Force association language ("was linked to") unless the design is causal |
| Species leap | A mouse result phrased as a human benefit | Require "in mice" in the lede; audit for implied human applicability |
| Settledness | One preprint framed as established fact | Label as single-study/preliminary; require replication caveat |
| Quiet hype | Polished prose that smuggles "first" or "breakthrough" | Banned-word scan plus calibrated-rewrite column in the audit |
| Buried caveat | Limitations relegated to the final line | Require each effect claim to carry its limitation in-paragraph |
