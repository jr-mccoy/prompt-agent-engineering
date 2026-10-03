---
title: "Spreadsheet Model Audit — Formula Errors, Hard-Codes, Broken Ranges, External Links, and Version Control in an Operating Workbook"
category: data-analytics/analysis-and-sql
description: "Audit an operational or business spreadsheet — a capacity plan, pricing calculator, commission sheet, budget tracker — for whether it computes what its owner thinks: map inputs, calculations, and outputs; scan for inconsistent formulas, hard-coded overrides, ranges that miss new rows, lookup and sign errors, circularity, and external links; reproduce key outputs independently; and rank findings by how much they move the answer."
techniques:
  - QA-18
  - DT-05
  - DS-06
  - AG-02
difficulty: intermediate
tags:
  - spreadsheet-audit
  - excel
  - google-sheets
  - formula-errors
  - model-review
  - end-user-computing
  - spreadsheet-gives-wrong-total
  - inherited-a-spreadsheet
  - can-i-trust-this-excel
updated: "2026-10-02"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_auditor.md
  - domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
---

# Spreadsheet Model Audit

**Objective:** Find every way an operating spreadsheet could return a plausible but
wrong number, prove each suspected error with a cell reference and a recomputation,
and rank the findings by their effect on the outputs people actually use.

**When to Use:**
- A spreadsheet drives a real decision — staffing, pricing, commissions, a budget —
  and nobody but its author has checked it.
- You inherited a workbook and are about to change it or rely on it.
- Two versions of "the model" give different totals.
- A total "looks off" and you want to rule out the mechanics before blaming the inputs.

**When NOT to use:**
- The workbook is a **DCF or valuation model** and the question is whether the
  methodology and assumptions are sound — use
  `domain-finance/valuation/finance_dcf_model_auditor.md`. This prompt audits the
  *mechanics* of any business spreadsheet (do the formulas compute what is intended),
  not whether a discount rate or terminal value is reasonable.
- The calculation lives in SQL — `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md`.
- The dispute is over what the metric *means* — settle the definition first with
  `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md`.
- You are building a new spreadsheet; this reviews an existing one.

## Inputs / Context

1. **The workbook** (or exported formulas: a sheet with formulas shown, or a formula
   listing per sheet). Values alone cannot be audited.
2. **Its purpose in one sentence**, and the 3–5 output cells that people act on.
3. **Who maintains it, how it is updated** (manual paste, linked file, data
   connection), and how often.
4. **Known history**: versions in circulation, recent changes, past errors.
5. **An independent figure** for at least one output (a system report, last period's
   actual), if available.

If formulas are not available, the first finding is "formulas not provided — audit
limited to output reasonableness", and the audit says what it cannot see.

## Method

1. **Map the model (DT-05).** For each sheet: role (input, calculation, output,
   lookup, scratch), and for each key output, trace precedents back to inputs. Flag
   inputs mixed into calculation sheets and outputs computed in more than one place.
2. **Scan for inconsistent formulas.** In each block that should hold one formula
   copied across, find cells whose formula differs from their neighbours (R1C1 view
   makes this obvious). One different cell in a column of 200 is the classic error.
3. **Find hard-codes and overrides.** Numbers typed inside formulas (`=B4*1.08`,
   `=SUM(C2:C40)+1250`), and formula cells overwritten with values. Each needs a
   labelled input or a removal.
4. **Check ranges and references.** `SUM`/`SUMIF`/`COUNTIF` ranges that stop short of
   the data; absolute vs. relative references that break when copied; references to
   the wrong row after a sort; whole-column references that catch totals and so
   double-count.
5. **Check lookups and logic.** `VLOOKUP` with approximate match on unsorted data,
   hard-coded column index that shifts when a column is inserted, `IFERROR` hiding
   lookup failures as zero, nested `IF` missing a case, sign conventions (costs
   positive in one sheet and negative in another), unit mismatches (hours vs. FTE,
   thousands vs. units, monthly vs. annual).
6. **Check structure.** Circular references and whether iteration is switched on;
   external links (to which files, do they still resolve, are values stale); hidden
   rows, columns, or sheets that feed outputs; volatile functions (`INDIRECT`,
   `OFFSET`) that defeat tracing; macros.
7. **Reproduce key outputs independently.** Recompute each key output from inputs by
   a different route (pivot, a quick script, a hand calculation). Report the
   difference.
8. **Rank (DS-06)** each finding: **Critical** (changes a decision-relevant output by
   more than the stated tolerance), **Major** (wrong but immaterial today, or will
   break on the next update), **Minor** (hygiene). Quantify the effect in output units.
9. **Version control and ownership.** Where is the master, who may edit, how are
   changes logged, are copies in circulation? Recommend the minimum: one master
   location, a change log tab, locked formula cells, an inputs sheet.
10. **Read skeptically (AG-02).** "It has always worked" is not evidence; the
    reproduction in step 7 is.

## Output Format

```
# Spreadsheet audit — [workbook name, version/date]   Owner: [..]   Auditor: [..]

## Purpose and key outputs
| Output | Cell | Used for | Tolerance |

## Model map
| Sheet | Role | Feeds | Notes |

## Findings
| # | Severity | Location | Issue | Evidence | Effect on output | Fix |

## Independent reproduction
| Output | Workbook value | Recomputed | Difference | Explained by finding # |

## Structure and controls
External links: [..]  Circularity: [..]  Hidden content: [..]  Macros: [..]
Version control: [..]

## Verdict
[fit for use | fit after critical fixes | do not rely on] — [one sentence why]
```

## Verification

- [ ] The audit was performed on formulas, not values only, or says it was not.
- [ ] Every key output was traced to inputs and independently recomputed.
- [ ] Every finding cites a cell or range and quantifies its effect in output units.
- [ ] Severity is relative to the stated tolerance on decision-relevant outputs.
- [ ] External links, hidden content, and circularity are each reported, even if "none".
- [ ] The verdict follows from the critical findings.

## False-Positive Prevention

1. **Every hard-code as an error.** A labelled constant (`VAT_RATE` on an inputs
   sheet) is good practice; an unlabelled `1.2` inside a formula is the problem.
2. **Inconsistency that is intended.** A different formula in a total row or a
   first-period cell can be correct. Confirm intent before calling it an error.
3. **Style findings ranked as critical.** Colour coding and naming matter, but they
   do not change a number; keep them Minor.
4. **Reproducing with the same logic.** Recomputing by copying the workbook's own
   formula re-creates its errors. Use a different route.
5. **Assuming the inputs are right.** Mechanics can be perfect on stale inputs.
   Report input freshness as a separate finding.
6. **Over-precision on the effect.** Where an error's effect depends on future data,
   give a range and mark it `[estimate]`.

## Example Output

```
# Spreadsheet audit — Contact-centre staffing plan v14 (2026-09-18)   Owner: WFM lead

## Purpose and key outputs
| FTE required, Oct–Dec   | Plan!F40:H40 | hiring requisitions | ±0.5 FTE |
| Overtime budget, Q4     | Plan!J44     | finance accrual     | ±$2,000  |

## Model map
| Inputs   | volumes, AHT, shrinkage | Calc | pasted weekly from ACD export |
| Calc     | workload → FTE          | Plan | 52 rows per month block       |
| Plan     | outputs                 | —    | 2 hidden columns (K:L) feed J44 |
| Rates    | wage lookup             | Plan | external link to HR_rates_2025.xlsx |

## Findings
| 1 | Critical | Calc!E2:E401 | E212 = D212*AHT_2025 while all others use AHT_2026 (copied from old block) | R1C1 scan | Nov FTE understated 1.8 | point to AHT_2026 |
| 2 | Critical | Plan!F40 | =SUM(F2:F35) — rows 36–39 (new queues added Sep) excluded | range check | Oct FTE understated 3.1 | extend to F39 or use a table |
| 3 | Major    | Calc!G:G | shrinkage typed as 0.3 in 14 cells, 0.32 on Inputs!B6 | hard-code scan | +0.9 FTE if 0.32 applied | reference Inputs!B6 |
| 4 | Major    | Rates link | HR_rates_2025.xlsx; 2026 rates +4% not applied | link list | OT budget understated ~$3,400 [estimate] | update link or paste values with date |
| 5 | Minor    | Plan!K:L | hidden columns feed J44 | unhide | none | unhide and label |

## Independent reproduction (Python from Inputs sheet; shrinkage held at 0.30 pending owner answer on #3)
| Oct FTE | 46.2 | 49.3 | −3.1 | #2 |
| Nov FTE | 44.0 | 45.8 | −1.8 | #1 |
| Dec FTE | 47.5 | 47.5 | 0.0  | — |

## Structure and controls
External links: 1 (stale). Circularity: none. Hidden: K:L. Macros: none.
Version control: v12, v13, v14 all circulating by email; no change log.

## Verdict
Do not rely on v14 for requisitions until findings 1–2 are fixed: Oct and Nov
FTE are understated by 3.1 and 1.8 — both beyond the ±0.5 tolerance.
```

## Techniques Used

- **QA-18 Domain-Specific Smell Tests** — the spreadsheet-specific error checklist (inconsistent formulas, short ranges, overrides, approximate lookups).
- **DT-05 Element-by-Element Assessment Matrix** — every sheet mapped by role and every key output traced.
- **DS-06 Prioritization and Severity Guidance** — Critical/Major/Minor by effect against tolerance.
- **AG-02 Skeptical Default Stance** — trust established by independent reproduction, not history.

## Related Prompts

- `domain-finance/valuation/finance_dcf_model_auditor.md` — methodology and assumption review of a valuation model.
- `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` — the same correctness discipline for SQL.
- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — settling what a number should mean before checking how it is computed.
