---
title: "Cross-Jurisdiction Policy Comparison — How Other Jurisdictions Handle the Problem, What Drove Their Results, and Whether It Transfers"
category: policy/comparative-analysis
description: "Compare how several countries, states or cities have tackled the same policy problem: select comparators on stated criteria rather than fame, describe each design on a common grid, separate reported outcomes from attributable effects, name the context conditions that drove each result, and run a transferability test against the home jurisdiction's legal, institutional, fiscal and political context before recommending what to borrow, adapt or avoid — distinct from case-law jurisdiction splits (legal_jurisdiction_split_analysis)."
techniques:
  - RT-02
  - DP-06
  - RT-05
  - QA-02
difficulty: advanced
tags:
  - comparative-policy
  - policy-transfer
  - international-comparison
  - lesson-drawing
  - benchmarking-jurisdictions
  - evidence-review
  - how-do-other-countries-do-it
  - would-it-work-here
  - learn-from-other-states
updated: "2026-10-02"
reasoning:
  styles: [comparative, analytic, causal, adversarial]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [matrix, structured]
  user_role: [policy, analyst, researcher, legislative_staff, advocate]
  mode: [synthesize, diagnose, decide]
related_prompts:
  - domain-policy/policy_problem_framing.md
  - domain-policy/policy_options_memo.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

# Cross-Jurisdiction Policy Comparison

**Objective:** Learn from other jurisdictions without copying their success story
into a context where it will fail: compare designs on a common grid, separate what
happened after adoption from what the policy caused, identify the conditions each
result depended on, and test whether those conditions hold at home.

**Audience:** Policy analysts, legislative researchers, think-tank and NGO staff,
ministry international units, and advocates preparing "other places do this"
arguments that must survive scrutiny.

**When to Use:**
- A sponsor says "Country X solved this" and you need to know whether that is true
  and whether it would work here.
- Options for a policy memo should be informed by what comparable jurisdictions tried,
  including failures.
- A study tour, peer-learning exchange, or evidence review needs a structured output.
- You must explain why the home jurisdiction is an outlier on an indicator.
- **Not this prompt if** the question is how courts in different circuits or states
  have ruled on a legal doctrine — `domain-legal/research/legal_jurisdiction_split_analysis.md`
  maps case-law splits; this prompt compares *policy designs and their results*. If
  the comparison is done and you are choosing among options, use
  `domain-policy/policy_options_memo.md`. If the problem itself is still contested,
  frame it first with `domain-policy/policy_problem_framing.md` — comparators are
  chosen against a framed problem.

## Inputs / Context

1. **The problem**, framed and measured in the home jurisdiction.
2. **Candidate comparators** the user has in mind, and any the principal insists on.
3. **Evidence on each**: statutes or program rules, evaluations, official statistics,
   academic studies, implementation reports — supplied or cited by the user.
4. **Home-jurisdiction context**: legal powers and constitutional limits, level of
   government responsible, administrative capacity, fiscal room, relevant
   institutions (e.g. a single-payer system, a land registry), political settlement.
5. **Purpose**: borrow a design, justify a position, or explain a gap.

No comparator's rules or results are reconstructed from memory as fact; a missing
detail is `[NOT PROVIDED — verify]`, and recalled background is labelled `[unverified]`.

## Method

1. **Select comparators on criteria.** Similar problem, similar outcome measure,
   and variation in design — including at least one jurisdiction that tried and
   abandoned or reversed the approach. Note why famous cases were included or left out.
2. **Describe each on a common grid (RT-02).** Instrument, target group, level of
   government, funding, enforcement, start date, and the main design parameters
   (rates, thresholds, eligibility). Same rows for every jurisdiction.
3. **Outcomes vs effects (RT-05).** For each: the trend in the outcome measure, and
   the best available causal evidence (evaluation design and size of effect).
   Mark **reported outcome**, **evaluated effect**, or **no evaluation**.
   Harmonise definitions before comparing levels.
4. **Name the dominant drivers (DP-06).** For each result, the 2–3 context
   conditions the evidence suggests it depended on — institutional capacity,
   complementary policies, market structure, enforcement culture, timing.
5. **Transferability test (QA-02).** For each driver, does the home jurisdiction
   have it? Rate legal fit, institutional capacity, fiscal fit, political fit,
   and complementary-policy fit as present / partial / absent, with evidence.
   Then argue against transfer: what is the strongest reason it would fail here?
6. **Draw lessons.** Borrow (transferable as is), adapt (which parameter changes
   and why), avoid (failure that would recur), or monitor (too early to judge).
   Each lesson cites the comparator rows it rests on.

## Output Format

```
# Cross-jurisdiction comparison — [problem]   Home: [..]   Purpose: [..]

## Comparator selection
| Jurisdiction | Why included | Design variation it adds |
Excluded / considered: [..]

## Design grid
| Element | J1 | J2 | J3 | Home (current) |

## Outcomes and evidence
| Jurisdiction | Outcome trend | Evidence type | Effect size | Status |

## Drivers of each result
## Transferability
| Driver | J1 needs | Home has? (present/partial/absent) | Evidence |
Strongest reason transfer would fail: [..]

## Lessons
| Lesson | Borrow / adapt / avoid / monitor | Based on | Parameter change |
```

## Verification

- [ ] Comparators are chosen on stated criteria and include a failure or reversal.
- [ ] Every jurisdiction is described on the same grid rows.
- [ ] Each result is labelled reported outcome, evaluated effect, or no evaluation.
- [ ] Definitions of the outcome measure are harmonised or the mismatch is stated.
- [ ] Each result names its context drivers; each driver is tested against home.
- [ ] The strongest argument against transfer is stated.
- [ ] Every lesson cites the rows it rests on.

## False-Positive Prevention

1. **Success-story selection.** Comparing only the jurisdictions held up as
   models guarantees a positive finding; include failures and reversals.
2. **Post hoc as effect.** An outcome that improved after adoption may reflect a
   regional trend; check comparators that did not adopt.
3. **Definition drift.** "Homelessness", "uninsured" and "recidivism" are measured
   differently across jurisdictions; harmonise before comparing levels.
4. **Design without context.** A policy that worked with a strong tax authority or
   universal ID may fail without one; the driver, not the law, travelled.
5. **Recalled facts as current.** Rates, thresholds and program rules change; label
   anything not from a supplied source.
6. **Averaging incompatible cases.** "On average, jurisdictions that did X saw Y"
   across very different systems hides the conditions that matter.

## Example Output

```
# Cross-jurisdiction comparison — Vacant residential property in a tight housing market
Home: mid-sized city (pop. 650 k), 2.1% rental vacancy, est. 3,800 long-term
vacant units [data: utility-use proxy]   Purpose: should the council adopt a vacancy tax?

## Comparator selection
| Vancouver (Empty Homes Tax, 2017) | tight market, city-level tax | rate escalated 1%→3% |
| Melbourne (state vacant residential land tax, 2018) | state-level, self-declaration | low-rate design |
| France (taxe sur les logements vacants, 1999) | national, long record | applies only in tense-market areas |
| City considered and rejected: one with no property-registry link (no admin data) |

## Design grid
| Element | Vancouver | Melbourne | France | Home |
| Level | city (special charter powers) | state | national | city — no taxing power over vacancy [legal: verify] |
| Rate | 1% → 3% of assessed value [unverified] | 1% of capital improved value [unverified] | % of rental value, rising after yr 1 [unverified] | — |
| Detection | mandatory annual declaration + audit | self-declaration, data matching | tax-authority records | utility proxy only |

## Outcomes and evidence
| Vancouver | declared-vacant units fell substantially after yr 1 | city annual reports | not causally evaluated | reported outcome |
| Melbourne | low declarations; revenue below forecast | state budget papers | — | reported outcome |
| France | modest increase in units returned to market | quasi-experimental study (areas phased in) | small positive effect | evaluated effect |

## Drivers
Vancouver: mandatory declaration for every owner + audit capacity; city charter
power to levy. France: national tax authority's housing records.
Melbourne: weak detection → low compliance.

## Transferability
| Taxing power at city level | absent — needs state enabling act | legal memo needed |
| Owner declaration + audit capacity | partial — assessor has 6 FTE | assessor budget |
| Data to detect vacancy | partial — utility data, privacy approval required | DPIA |
Strongest reason it fails here: 3,800 vacant units may be mostly between-tenant
or estate-held; if exemptions cover 70%, yield is ~1,100 units.

## Lessons
| Mandatory declaration + audit, not self-report | borrow | Vancouver vs Melbourne | — |
| Seek state enabling legislation first | adapt | Vancouver charter power | legal route |
| Low flat rate with self-declaration | avoid | Melbourne | — |
| Commission a vacancy-composition study before setting rate | monitor | all | — |
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — every jurisdiction on the same design grid and transferability dimensions.
- **DP-06 Dominant Driver Identification** — the context conditions each result depended on are named explicitly.
- **RT-05 Evidence-Based Reasoning** — outcomes labelled by evidence type, with sources.
- **QA-02 Adversarial Stress-Test** — the strongest reason transfer would fail is argued before lessons are drawn.

## Related Prompts

- `domain-policy/policy_problem_framing.md` — frame and measure the home problem before choosing comparators.
- `domain-policy/policy_options_memo.md` — the lessons become options compared on seven criteria.
- `domain-legal/research/legal_jurisdiction_split_analysis.md` — case-law splits across courts, not policy designs.
