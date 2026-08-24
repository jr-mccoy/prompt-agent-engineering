---
title: "Statistical and Visual Distortion Scan — Where the Number Stops Meaning What It Says"
category: psy-ops/technique-analysis
description: "Audit a statistic, chart, or data claim for the distortions that survive technical accuracy: truncated axes, base-rate omission, relative-risk inflation, denominator swaps, cherry-picked baselines, survivorship bias, and misleading aggregation. Assumes incompetence before design, because most bad charts are made by people in a hurry. Produces the honest restatement of the same underlying data."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - statistics
  - data-visualization
  - numeracy
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, quantitative, evaluative]
  stakes: moderate
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: single_domain
  collaboration: solo_or_pair
  output_format: distortion_inventory_with_honest_restatement
  user_role: [analyst, journalist, researcher, educator, individual]
  mode: [assess, audit, teach]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_propaganda_technique_identification.md
  - domain-psy-ops/technique-analysis/psyops_provenance_and_transmission_trace.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
---

# Statistical and Visual Distortion Scan

**Objective:** Audit a statistic, chart, or data claim for distortions that **survive technical accuracy** — the ones where every number is correct and the impression is still wrong. Truncated axes, missing base rates, relative risk presented without absolute risk, denominator swaps, baselines chosen at a local extreme, survivorship-filtered samples, and aggregation that hides or invents a pattern. The output is not just an inventory but the **honest restatement**: the same underlying data presented so the impression matches what it supports.

The operating assumption is **incompetence before design**. Most misleading charts are produced by people under deadline using a default template, and most misleading statistics are repeated by people who did not compute them. Treating every distortion as deliberate is both usually wrong and analytically lazy — and it lets you skip the harder work of establishing what the data actually shows.

**When to use:**
- A number or chart is being used to settle an argument and you want to check it.
- A statistic seems too clean, too large, or too convenient.
- You are checking your own analysis or slide before publishing it.
- You are teaching numeracy and need a worked example.

**When NOT to use:**
- The question is where the claim came from — use `psyops_provenance_and_transmission_trace.md`.
- You want to grade a study's overall evidentiary weight — use `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md`.
- You are designing a chart rather than auditing one — use `dataviz` guidance.
- The distortion is rhetorical rather than quantitative — use `psyops_propaganda_technique_identification.md`.

**Audience:** Analysts, journalists, researchers, educators, and anyone about to repeat a number.

---

## Inputs / Context

1. **The claim or chart.** The exact statistic as stated, or the chart with its axes, labels, caption, and title.
2. **The underlying source.** The study, dataset, or release it came from — and whether you have actually seen it or only the summary.
3. **The comparison being invited.** What the reader is meant to conclude from it.
4. **What you know about the domain.** Typical magnitudes and base rates, which is what makes a number surprising.
5. **The stakes of the claim.** How consequential acting on it would be, which sets appropriate scrutiny.

---

## Constraints

### Must
- Check whether the **base rate** is present. Its absence is the single most common and most consequential distortion.
- Convert **relative to absolute** wherever a relative change is presented, and report both.
- Check the **denominator**: what population, over what period, and whether it changed between compared figures.
- Inspect **axes**: truncation, dual axes, non-linear scales, inverted orientation, and inconsistent intervals.
- Check the **baseline and endpoints**: whether the start point sits at a local extreme, and whether the window was chosen after seeing the data.
- Check for **survivorship and selection filtering** in how the sample was assembled.
- Test **aggregation**: whether grouping hides subgroup reversal, or whether disaggregation manufactures a pattern from noise.
- Produce the **honest restatement** of the same data, and state whether the original conclusion survives it.

### Must Not
- Assert deliberate deception. Default-template truncated axes and repeated-without-checking statistics are the norm. Say "misleading," not "falsified," unless you can show the data were altered.
- Compute figures you do not have. If absolute risk cannot be derived from what is presented, say so — that absence is itself the finding.
- Fabricate a base rate, a denominator, a sample size, or a source. Unknown values stay `[VERIFY]`.
- Dismiss a finding solely because its presentation is poor. Bad charts routinely depict real effects.
- Treat statistical significance as effect size, or a large sample as a guarantee of relevance.
- Accept a summary as the source. If you have not seen the underlying study, say the audit is of the summary only.

---

## Instructions

### Step 1 — State the claim precisely and the invited conclusion
Write the number exactly as presented, then what a reader is meant to take from it. Distortion lives in the gap between these.

### Step 2 — Locate the base rate
Is it present? If not, find or estimate it and note which. A doubled risk means nothing until the starting risk is known.

### Step 3 — Convert relative to absolute
Restate every relative change in absolute terms. If the data to do so are not provided, record that the presentation cannot be evaluated as given.

### Step 4 — Interrogate the denominator
What population, what time window, and is it the same across every compared figure? Watch for silent swaps between per-capita, per-user, per-incident, and raw counts.

### Step 5 — Inspect the chart mechanics
Axis start values, truncation, dual axes with independent scaling, log versus linear without labeling, inconsistent bin widths, area used to encode a linear quantity, and any 3D effect distorting comparison.

### Step 6 — Test the window and the baseline
Move the start and end points a reasonable distance. If the conclusion reverses under small window changes, the finding is a window artifact.

### Step 7 — Check sampling and aggregation
Who is missing from the sample and why. Then test aggregation both ways — collapse subgroups and split them — and check whether any relationship reverses.

### Step 8 — Write the honest restatement and run the adversarial check
Present the same data so the impression matches the support. Then argue that the original presentation is fair and you are nitpicking, and say whether the underlying conclusion survives.

---

## False-Positive Prevention

1. **Deception assumed.** Attributing a template default to intent. Most truncated axes come from software defaults and most bad statistics from copying.
2. **Baby with the bathwater.** Dismissing a real effect because the chart is bad. Presentation quality and effect reality are independent.
3. **Fabricated base rates.** Supplying a plausible-sounding starting risk to complete the analysis. If it is unknown, the finding is that it is missing.
4. **Truncation reflex.** Treating every non-zero axis as manipulation. For many series — temperature, bond yields, approval — a zero baseline destroys the information. Judge by whether the truncation exaggerates the effect being claimed.
5. **Significance-as-size.** Reading a small p-value as a large effect. Large samples make trivial differences significant.
6. **Summary audited as source.** Auditing a press release and reporting on the study. Say which you actually read.
7. **Reverse cherry-picking.** Choosing your own window to make the effect vanish. Apply the same standard to your restatement.
8. **Precision theater.** Repeating decimal places the underlying measurement cannot support, then treating the precision as accuracy.

---

## Output Format

```
# Distortion scan — [claim / chart]

## The claim, exactly as stated
"[verbatim]" — invited conclusion: [what the reader is meant to take away]

## Source status
[Underlying study/dataset seen? Or summary only? — audit scope stated accordingly]

## Distortion inventory
| Check | Finding | Severity | Incompetence-first reading |
|---|---|---|---|
| Base rate | absent — starting risk not given | high | omitted for space in a summary |
| Relative vs absolute | "doubles risk" = [x]% → [y]% absolute | high | standard in the field's press releases |
| Denominator | [population / window / consistent?] | | |
| Axes | [truncation / dual / scale] | | |
| Baseline & window | [start at local extreme?] | | |
| Sampling | [who is missing] | | |
| Aggregation | [subgroup reversal?] | | |

## Window sensitivity test
[What happens to the conclusion when start/end points move by a reasonable amount]

## Honest restatement
[The same underlying data, presented so the impression matches the support]

## Does the original conclusion survive?
[Yes / partly / no] — because [one line]

## Adversarial check
[The case that the presentation is fair and I am nitpicking]

## Unknowns
[Every [VERIFY] — base rates, denominators, sample details not available]
```

---

## Verification

- [ ] Base rate presence is checked explicitly, and absence is reported as a finding rather than filled in.
- [ ] Every relative figure is converted to absolute, or the conversion is marked impossible from what was given.
- [ ] Denominator consistency across compared figures is checked.
- [ ] Axis truncation is judged by whether it exaggerates the specific claim, not by a zero-baseline rule.
- [ ] The window-sensitivity test was run and reported.
- [ ] Aggregation was tested in both directions for subgroup reversal.
- [ ] An incompetence-first reading is offered for every distortion found.
- [ ] The audit states whether the underlying source or only a summary was examined.
- [ ] The honest restatement is present, and the survival of the original conclusion is stated plainly.
- [ ] No base rate, denominator, sample size, or source was invented; unknowns are marked `[VERIFY]`.
