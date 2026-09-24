---
title: "Phishing Awareness Program — Reporting Culture, Short Training, Fair Simulations, and Metrics That Cannot Be Gamed"
category: risk
description: "Design a year-one phishing awareness program for a small or mid-sized organisation that treats people as the detection layer rather than the weak link: a one-click reporting path, short role-specific training, simulations run under published rules with no shaming, and metrics led by reporting rate and time-to-report rather than click rate alone; distinct from `domain-software-engineering/analysis/security/security_soc2_type2_preparation.md`, which only needs the training evidence, and `risk_payment_fraud_bec_controls.md`, which makes a successful lure fail at the payment step."
techniques:
  - RP-02
  - DS-02
  - QA-21
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - phishing
  - security-awareness
  - training
  - reporting-culture
  - metrics
  - small-business
updated: "2026-09-24"
reasoning:
  styles: [systems, empathic, evaluative, adversarial]
  stakes: moderate
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [operator, hr, team-lead, executive]
  mode: [design, plan, audit]
related_prompts:
  - domain-software-engineering/analysis/security/security_soc2_type2_preparation.md
  - domain-risk/risk_payment_fraud_bec_controls.md
  - domain-risk/risk_security_incident_response_playbook.md
---

# Phishing Awareness Program

**Objective:** Produce a twelve-month program — reporting path, training modules,
simulation rules, metrics and a quarterly review — whose success measure is that
suspicious messages get reported quickly, not that nobody ever clicks.

**When to Use:**
- You have no awareness program, or one annual video nobody remembers.
- Someone clicked, it cost money or time, and leadership wants "training".
- A client questionnaire or SOC 2 readiness asks for awareness training and simulation results.
- Past simulations produced resentment, public naming, or a click rate nobody could act on.

**Not this prompt if:**
- You need audit evidence formats and control mapping for SOC 2 — `domain-software-engineering/analysis/security/security_soc2_type2_preparation.md`.
- You need the finance-side controls that stop a fooled person's payment — `risk_payment_fraud_bec_controls.md`.
- Someone has already been compromised — `risk_security_incident_response_playbook.md` first.

**Boundary:** Simulations are defensive exercises run by the organisation on its own staff,
with leadership approval and HR sign-off. This prompt does not write lures that impersonate
real external brands, government bodies or specific named individuals, and never uses
lures built on staff welfare (bonuses, layoffs, health results) that damage trust.

## Inputs / Context

1. **Headcount, roles, and who handles money, credentials or personal data.**
2. **Email platform and whether it has a "report phishing" button** (or can add one).
3. **Who receives reports today**, and how fast they respond.
4. **Past incidents and near-misses**, anonymised.
5. **Culture signals:** has anyone been disciplined or named for clicking?
6. **External requirements:** client contracts, insurer, audit (ask for the wording).

## Method

1. **Build the reporting path first (CM-02).** Before any training or simulation:
   - one-click report button, or a single named address;
   - an acknowledgement to the reporter within a stated time, with thanks, **every time**,
     including false alarms;
   - a named triage owner (feeds `risk_security_alert_triage_runbook.md`).
   A program that trains people to report into a void teaches them to stop reporting.

2. **Segment by role, not by seniority (RP-02).** Three tracks are usually enough:
   everyone; people who move money or change bank details; people with admin or data access.
   Each track gets 10–15 minutes per quarter, built on real examples from this organisation's
   own inbox (with names removed), not generic slides.

3. **Write simulation rules and publish them.** Staff know simulations happen (not when).
   Rules state: frequency (e.g. quarterly), what counts as a pass (**reporting** it), what
   happens on a click (a short just-in-time explainer, nothing else), who sees individual
   results (the program owner only), and what is off-limits (welfare lures, real brands,
   named colleagues). Must-nots: no public leaderboards of clickers, no discipline for
   simulation clicks, no "gotcha" emails from the CEO's real account.

4. **Choose metrics, reporting first (DS-02).**

   | Metric | Definition | Why it matters |
   |---|---|---|
   | Report rate | % of simulation recipients who reported | The behaviour you want |
   | Time to first report | Minutes from send to first report | How fast the "sensor" fires |
   | Click-without-report | % who clicked and did not report | The genuinely dangerous group |
   | Real reports per month | Non-simulation reports received | Transfers to real life |
   | Click rate | % who clicked | Context only; varies with lure difficulty |

5. **Enumerate how each metric can be gamed (QA-21).** Click rate falls if lures get easier
   or are sent at quiet times; report rate rises if staff forward everything; real reports fall
   if acknowledgement is slow. Hold lure difficulty roughly constant and record it with each
   campaign, or trend lines are meaningless.

6. **Quarterly review.** Trend the metrics, read a sample of real reports, retire modules
   that no longer match real lures, and publish a short all-staff note that thanks reporters
   and shows one real catch.

## Output Format

```
# Phishing awareness program — [organisation], [year]
Owner: [role] · Triage owner: [role] · HR sign-off: [role, date]

## Reporting path
Button/address: ... · Acknowledgement within: ... · Triage owner: ...

## Training tracks
| Track | Who | Topics (from our own examples) | Length | Cadence |

## Simulation rules (published to staff on [date])
Frequency · What counts as a pass · What happens on a click · Who sees results · Off-limits lures

## Metrics
| Metric | Definition | Baseline | Target (year 1) | Gaming vector | Control |

## Campaign log
| Campaign | Date | Lure type | Difficulty (1–3) | Report rate | TTFR | Click-w/o-report |

## Quarterly review agenda
## Confidence: High / Medium / Low on each target, with reason
```

## Verification

- [ ] The reporting path works and acknowledges reporters before any simulation runs.
- [ ] Report rate and time-to-report are primary metrics; click rate is context.
- [ ] Every metric has at least one named gaming vector and a control.
- [ ] Simulation rules are published and include what is off-limits.
- [ ] No individual results are shared beyond the program owner; no discipline for simulation clicks.
- [ ] Money-movers have a track tied to the payment controls.
- [ ] Lure difficulty is recorded per campaign.

## False-Positive Prevention

1. **Click rate as the headline.** It falls when lures get easier and rises when they get
   realistic; alone it measures the simulator, not the staff.
2. **Shaming as motivation.** Public naming or discipline suppresses reporting — including
   reporting of real clicks, which is the one report you most need.
3. **A report button with no acknowledgement.** Unanswered reports extinguish the behaviour.
4. **Generic content.** Stock slides about foreign princes do not resemble the invoice-change
   and shared-document lures this organisation actually receives.
5. **Training as the only control.** A well-trained person still gets fooled on a bad day;
   the payment and account controls must hold regardless.
6. **Welfare-bait lures.** "Your bonus letter" simulations win the metric and lose trust.
7. **Trend without difficulty.** A falling click rate across campaigns of unrecorded difficulty
   proves nothing.

## Example Output

```
# Phishing awareness program — Northfield Architects (38 staff), 2027
Owner: Operations Lead · Triage owner: MSP (NorthIT), fallback Ops Lead · HR sign-off: HR Manager, 2026-10-02

## Reporting path
"Report" add-in in the mail client → NorthIT queue · Auto-acknowledge + human reply within 4 working hours

## Training tracks
| All staff | 38 | Shared-doc lures, fake e-signature, MFA-fatigue prompts | 12 min | Quarterly |
| Money movers | 4 (finance + 2 PMs approving fees) | Invoice/bank-change requests, urgency from "partners" | 15 min | Quarterly |
| Admins | 3 | Fake vendor-support calls, consent-grant prompts | 15 min | Quarterly |

## Metrics
| Report rate | reported / delivered | 9% (2026 Q3 baseline) | ≥ 40% | Staff forward everything | Also track false-report share |
| TTFR | send → first report | 3h 10m | < 30 min | Early-bird reporter only | Track median too |
| Click-w/o-report | clicked ∧ ¬reported | 14% | < 5% | Easier lures | Hold difficulty at 2 |
| Real reports/month | non-sim reports | ~2 | ≥ 8 | Slow acks suppress | Ack SLA above |

## Campaign log
| Q1 | 2027-02 | Shared drawing set | 2 | [measure] | [measure] | [measure] |

## Confidence
Report-rate target: Medium (depends on ack SLA holding). Click-w/o-report target: Low until Q2 data.
```

## Techniques Used

- **RP-02 Audience-Specific Framing** — tracks by what a role can lose, not by rank.
- **DS-02 Metric Specification** — defined, reporting-led metrics with baselines.
- **QA-21 Metric Gaming Vector Enumeration** — each metric's gaming route and its control.
- **CM-02 Constraint Specification** — published must/must-not rules for simulations.
- **QA-12 False Positives Identification** — naming what not to read into click rate.

## Related Prompts

- `risk_payment_fraud_bec_controls.md` — controls that hold when training fails.
- `risk_security_alert_triage_runbook.md` — what happens to a report once it arrives.
- `risk_security_incident_response_playbook.md` — when a report turns out to be real.
- `../domain-software-engineering/analysis/security/security_soc2_type2_preparation.md` — training evidence for audit.
