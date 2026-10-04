---
title: "Field Core Web Vitals Regression Triage — Confirming the Shift, Separating Traffic Mix from Real Slowdown, Localising by Template and Sub-Part, and Tying It to a Change"
category: frontend-development/performance
description: "Triage a drop in real-user Core Web Vitals: confirm the shift is beyond noise and CrUX lag, decompose it into traffic-mix change versus within-segment slowdown, localise it to a page template and to an LCP or INP sub-part using attribution data, line it up against deploys, flags and third-party changes, and verify the fix in field data rather than in a lab score."
techniques:
  - RT-06
  - NE-11
  - RT-09
  - QA-12
difficulty: advanced
tags:
  - core-web-vitals
  - real-user-monitoring
  - crux
  - inp-attribution
  - lcp-subparts
  - performance-regression
  - site-got-slower-after-release
  - search-console-says-pages-failing
  - page-speed-score-dropped
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-agentic-resources/skills/seo-marketing/core-web-vitals-audit/SKILL.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
---

# Field Core Web Vitals Regression Triage

**Objective:** When real-user LCP, INP or CLS gets worse, establish whether the change is
real, how much of it is a change in *who* visited rather than *how fast* the site was,
which template and which sub-part moved, and which change caused it — then confirm the fix
in field data with a stated detection window.

**When to Use:**
- RUM dashboards or CrUX show p75 LCP, INP or CLS worse than last month.
- Search Console moves URL groups from "Good" to "Needs improvement".
- A release went out and someone says "the site feels slower" but lab scores look fine.
- Leadership asks whether a regression was caused by engineering or by a campaign.
- **Not this prompt if** you are optimising a page whose vitals have always been poor —
  use `domain-frontend-development/performance/frontend_performance_core_web_vitals.md`
  (lab and field diagnosis and fixes per metric). For a site-wide SEO-oriented audit with
  budgets and monitoring setup, use
  `domain-agentic-resources/skills/seo-marketing/core-web-vitals-audit/SKILL.md`. If the
  cause turns out to be JavaScript weight, continue with
  `domain-frontend-development/performance/frontend_performance_bundle_optimization.md`.

## Inputs / Context

1. **Field data**: own RUM (e.g. the `web-vitals` library, ideally its attribution build)
   with per-page-load records, and/or CrUX (origin and URL level, p75, 28-day rolling).
2. **Dimensions per record**: page template/route, device class, connection type,
   country, browser, logged-in state, app version.
3. **Change log**: deploys with timestamps, feature-flag changes, A/B tests, tag-manager
   and third-party script changes, CDN/config changes, marketing campaigns.
4. **Attribution fields** where collected: LCP sub-parts (time to first byte, resource
   load delay, resource load duration, element render delay) and element; INP sub-parts
   (input delay, processing duration, presentation delay) and interaction target; CLS
   largest-shift target.
5. **Thresholds** (p75): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 are "good".

## Method

1. **Confirm the shift is real.** Compare like windows (same weekdays, ≥7 days each).
   For own RUM, bootstrap a confidence interval on the p75 difference; with fewer than a
   few thousand loads per segment, treat small moves as noise. For CrUX, remember the
   28-day rolling window: a change on day 0 is only fully visible ~28 days later, and a
   fix shows up just as slowly. Use own RUM to date the change.
2. **Separate mix from rate (NE-11).** Percentiles do not decompose, but the share of
   loads that are "good" does. With segment weights `w_s` and good-rates `g_s`:
   `good = Σ w_s·g_s`; the change splits into
   `mix = Σ (w_s,new − w_s,old)·g_s,old` and
   `rate = Σ w_s,new·(g_s,new − g_s,old)`.
   If most of the change is *mix*, the site did not get slower — the audience changed
   (a campaign, a new market, an app-store referral) (RT-06).
3. **Localise (RT-06).** Within the *rate* component, rank segments by contribution:
   template × device first, then browser, country, logged-in state. Most regressions sit
   in one or two templates.
4. **Find the sub-part that moved.** For LCP: which of TTFB, resource load delay, load
   duration, render delay grew — and did the LCP element itself change (a hero image
   replaced by a text block, or vice versa)? For INP: which interaction targets regressed
   and in which sub-part (input delay → main thread busy before handling; processing →
   handler cost; presentation → rendering after the handler). For CLS: which element
   shifts and when.
5. **Line it up with changes (RT-09).** Overlay the dated shift on deploys, flags, tests
   and third-party changes for the affected template. Write the hypothesis as root cause
   → symptom → mechanism → fix, and test it: revert behind a flag, or reproduce in the
   lab with conditions matched to the regressed segment (CPU throttling for low-end
   Android, not a desktop default).
6. **Say what to ignore (QA-12).** Lighthouse score swings without field movement,
   desktop movement when the regression is mobile, single-day spikes, and segments too
   small to measure.
7. **Verify in the field.** State the expected effect of the fix in the affected segment,
   the date own RUM should show it, and the date CrUX should reflect it. Rate each
   conclusion: High = shift confirmed with interval, cause reproduced and fix verified in
   RUM; Medium = cause correlated but not reproduced; Low = CrUX only, no own RUM.

## Output Format

```
# Field vitals regression triage — [site]   Metric(s): [..]   Window: [old] vs [new]

## Is it real?
| Metric | Segment | p75 old | p75 new | Δ | 95% CI | Samples | Verdict |
## Mix vs rate decomposition (% good loads)
| Total Δ | Mix component | Rate component | Interpretation |
## Localisation
| Segment (template × device) | Weight | Good-rate old → new | Contribution to rate Δ |
## Sub-part attribution
| Sub-part / target | p75 old | p75 new | Δ |
## Change correlation
| Date | Change | Affects segment? | Hypothesis |
## Root cause → symptom → mechanism → fix
## Ignored on purpose
## Verification plan
Expected effect: [..]  Own RUM confirmation date: [..]  CrUX reflects by: [..]
## Confidence
```

## Verification

- [ ] Old and new windows cover the same weekdays and are at least 7 days.
- [ ] The decomposition uses % good loads, and mix + rate equals the total change.
- [ ] Localisation names the template and device class carrying most of the rate change.
- [ ] The sub-part that moved is identified from attribution data, not guessed.
- [ ] The cause was reproduced or reverted, or the conclusion is rated Medium or Low.
- [ ] The verification plan accounts for the 28-day CrUX window.

## False-Positive Prevention

1. **Lab score as field truth.** A Lighthouse drop with flat RUM is not a user-facing
   regression; a flat Lighthouse with worse RUM can be.
2. **Aggregate p75 as the story.** A cheaper-device audience from a campaign can move the
   aggregate with no code change. Decompose before blaming a release.
3. **Averaging percentiles.** p75s of segments cannot be weighted together; use good-rate
   shares or recompute from records.
4. **CrUX dates as change dates.** The rolling window smears the change across four
   weeks; date it with own RUM.
5. **The last deploy as the cause.** Third-party tags, flags and A/B tests change without
   deploys; check them all for the affected template.
6. **Small segments as signals.** A 40 ms INP move on 300 loads is noise.
7. **Fix declared on lab evidence.** Close the regression only when field data in the
   affected segment recovers.

## Example Output

```
# Field vitals regression triage — "Pellmark" homeware e-commerce   Metric: INP (mobile)
Window: 1–14 Sep vs 15–28 Sep 2026 (Mon–Sun ×2 each)

## Is it real?
| INP | mobile, all | 176 ms | 238 ms | +62 | [+51, +73] | 1.9M loads | real |
| INP | desktop     |  88 ms |  91 ms |  +3 | [−2, +8]   | 0.8M       | no change |

## Mix vs rate decomposition (% good INP loads, mobile)
| −9.6 pts (81.0% → 71.4%) | −1.2 pts | −8.4 pts | 87% is within-segment slowdown |
Mix: low-end Android share rose 31% → 35% (autumn sale emails) — real but minor.

## Localisation (rate component, −8.4 pts)
| Product listing × low-end Android | 0.14 | 64% → 31% | −4.6 pts |
| Product listing × mid/high mobile | 0.22 | 88% → 77% | −2.4 pts |
| Product detail × all mobile       | 0.30 | 86% → 84% | −0.6 pts |
| Other templates                   | 0.34 | ~flat     | −0.8 pts |
Listing pages carry 83% of the rate change.

## Sub-part attribution (listing, mobile, p75)
| target: filter checkbox | processing 46 → 171 ms | input delay 38 → 44 | presentation 52 → 61 |
| target: "Load more"     | processing 60 → 66 ms  | — | — |

## Change correlation
| 15 Sep 10:20 | release 8.31 — new filter analytics (sync JSON.stringify of full product grid
  state on every change + getBoundingClientRect per tile) | yes | H1 |
| 16 Sep | tag manager: chat widget version bump | all templates | ruled out — desktop flat,
  PDP flat |

## Root cause → symptom → mechanism → fix
Root cause: filter handler serialises 1.4 MB state and reads layout for 96 tiles synchronously.
Symptom: filter taps feel stuck; INP processing +125 ms. Mechanism: long task inside the event
handler before the next paint. Fix: update UI first, defer analytics to idle/after paint,
send only the changed filter. Reproduced: 4× CPU throttle, processing 39 → 168 ms → 44 ms after fix.

## Ignored on purpose
Lighthouse mobile score unchanged (no filter interaction in lab run); desktop; one-day spike 21 Sep
(CDN incident, LCP only, resolved).

## Verification plan
Expected: listing × mobile good-rate back to ≥85%. Own RUM: visible within 2 days of 8.33 release.
CrUX: fully reflected ~28 days after release.

## Confidence
High — shift confirmed with interval, cause reproduced under throttling, flag-off test restored
p75 processing to 49 ms on 5% of traffic.
```

## Techniques Used

- **RT-06 Correlation and Cross-Analysis** — field shifts are correlated with traffic mix, segments and the change log.
- **NE-11 Embedded Calculation Formulas** — the mix/rate shift-share decomposition on good-load shares.
- **RT-09 Root Cause Explanation Pattern** — root cause → symptom → mechanism → fix, with a reproduction.
- **QA-12 False Positives Identification** — lab swings, small segments, CrUX dating and unrelated spikes are named and set aside.

## Related Prompts

- `frontend_performance_core_web_vitals.md` — per-metric diagnosis and fixes once the regressed template and sub-part are known.
- `domain-agentic-resources/skills/seo-marketing/core-web-vitals-audit/SKILL.md` — site-wide CWV audit, budgets and monitoring setup.
- `frontend_performance_bundle_optimization.md` — when the localised cause is JavaScript weight.
