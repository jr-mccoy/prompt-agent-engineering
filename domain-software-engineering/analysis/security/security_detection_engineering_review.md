---
title: "Detection Engineering Review — Detection-as-Code, ATT&CK Mapping, True/False-Positive Tuning, and Tested Detections"
category: analysis/security
description: "Review a team's security detections as engineered software: whether each rule lives in version control with a written strategy, maps honestly to the ATT&CK technique it actually observes, has a measured precision and alert volume, is tested by replaying the behaviour it claims to catch, and earns its place in an analyst's queue — then rank fixes by coverage gained per unit of alert load."
techniques:
  - RT-02
  - QA-10
  - QA-12
  - QA-21
  - QA-24
difficulty: advanced
tags:
  - detection-engineering
  - detection-as-code
  - mitre-attack
  - siem-rules
  - alert-tuning
  - false-positive-rate
  - too-many-security-alerts
  - alerts-nobody-trusts
  - would-we-catch-an-attack
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/analysis/security/security_soc_alert_triage_runbook.md
  - domain-software-engineering/analysis/security/security_threat_hunting_plan.md
  - domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md
---

# Detection Engineering Review

**Objective:** Audit an existing set of security detections (SIEM/EDR/cloud rules) the way
you would audit production code — ownership, tests, measured precision, honest coverage —
and produce a ranked fix list that raises real coverage without raising alert load.

**When to Use:**
- The SIEM has hundreds of rules, analysts close most alerts as noise, and nobody can say
  which rules would fire on a real intrusion.
- Leadership shows an ATT&CK heat map as "coverage" and you suspect it is optimistic.
- You are moving rules from a console into a repository (detection-as-code) and want to
  know which ones are worth migrating.
- A red-team or incident exposed a technique that no rule caught.
- **Not this prompt if** you are designing model-assisted or autonomous triage and SOAR —
  use `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md`; that prompt
  automates the queue, this one fixes what feeds it. For the human steps an analyst takes
  when an alert fires, use `security_soc_alert_triage_runbook.md`. For rule *syntax* in a
  specific engine, use the tool skills `domain-agentic-resources/skills/security/semgrep-rule-creator/`
  or `domain-agentic-resources/skills/security/yara-rule-authoring/`. Application uptime alerting is
  `domain-software-engineering/devops/devops_monitoring_observability.md`.

## Inputs / Context

1. **Rule inventory export**: rule id, name, query/logic, data source, severity, owner,
   created/modified dates, enabled state.
2. **90 days of alert outcomes** per rule: count fired, analyst dispositions (true positive
   malicious, true positive benign, false positive, undetermined), median time to close.
3. **Log source inventory**: which sources are ingested, retention, parsing health, gaps
   (e.g. "EDR on 70% of laptops, none on Linux servers").
4. **Claimed ATT&CK mapping** and any heat map used in reporting.
5. **Testing assets**: emulation tooling (e.g. Atomic Red Team tests, purple-team scripts),
   recorded attack logs, CI pipeline for rules if one exists.
6. **Threat priorities**: the 5–10 techniques that matter most for this environment (from
   threat modelling, incidents, sector reports).

## Method

1. **Inventory as code (RT-02).** For each rule record five attributes: in version control
   (y/n), peer-reviewed change history, a written strategy (Palantir's Alerting and Detection
   Strategy fields are a good minimum: goal, technical context, blind spots, known false
   positives, validation, response), an owner, and a linked triage runbook. Rules missing
   three or more are "unowned" regardless of how well they perform.
2. **Measure each rule.** Precision = TP ÷ (TP + FP), counting *true positive benign* as
   neither — report it separately, because "admin ran the tool on purpose" is a tuning
   signal, not a hit. Record weekly volume and analyst minutes consumed
   (volume × median handle time). Flag: precision < 10% with > 20 alerts/week (noise),
   zero fires in 90 days (silent — broken or simply quiet?), > 30% undetermined (runbook or
   data gap).
3. **Audit the ATT&CK mapping honestly (QA-21).** For each claimed technique ask: does the
   rule observe the *behaviour* or one tool's artefact? A hash or filename match sits at the
   bottom of the Pyramid of Pain and covers one tool, not the technique. Grade each mapping
   *behavioural*, *tool-specific*, or *nominal* (mapped but would not fire). Coverage = count
   of priority techniques with at least one tested behavioural rule — not cells coloured.
4. **Test the rules (QA-10).** For priority techniques, replay the behaviour (emulation test
   or stored logs) in a non-production tenant and record fire / no fire / fired late. Then
   add each passing test to CI so a parser change or field rename that silently breaks the
   rule fails a build. A rule with no test is "claimed", not "covered".
5. **Tune false positives without blinding (QA-12).** For each noisy rule, classify the FP
   cause: environment-specific benign activity (allow-list by entity + expiry), logic too
   broad (add a behavioural condition), or wrong severity (downgrade to a correlation-only
   signal that never pages). Never suppress by the field an attacker controls (process
   name, user-agent string).
6. **Record what you checked and cleared (QA-24).** List rules reviewed and judged sound,
   with the evidence, so "no finding" is distinguishable from "not reviewed".
7. **Rank fixes** by (priority techniques gained to tested-behavioural) ÷ (alert-minutes
   added per week). Retiring a 2%-precision rule is a positive-value fix.

## Output Format

```
# Detection engineering review — [org/team], [date], [n] rules reviewed

## Summary
Rules: [n] · as code: [%] · with written strategy: [%] · with test: [%]
Alert load: [alerts/week] · [analyst-hours/week] · overall precision [%]
Priority-technique coverage (tested, behavioural): [x of y]

## Rule scorecard
| Rule | Owner | As code | Strategy | Test | Fires/wk | Precision | TPB | Undet. | Verdict |

## ATT&CK mapping audit
| Technique (priority) | Claimed rules | Grade (behavioural / tool / nominal) | Tested? | Real coverage |

## Test results
| Technique | Emulation | Fired? | Latency | Gap cause (data / logic / parser) |

## Tuning actions
| Rule | FP cause | Change | Expected volume after | Blind-spot risk introduced |

## Checked and cleared
## Ranked fix list (coverage gained ÷ alert-minutes)
## Data-source gaps that no rule change can fix
```

## Verification

- [ ] Precision excludes true-positive-benign from both numerator and FP count, and TPB is reported.
- [ ] Every "covered" technique has a passing replay test, not just a mapping.
- [ ] Every tuning change states the blind spot it creates.
- [ ] Silent rules are tested before being called healthy.
- [ ] Coverage is reported as priority techniques tested, not total ATT&CK cells.
- [ ] Fixes are ranked with both coverage and alert-load numbers shown.
- [ ] Data-source gaps are separated from rule-logic gaps.

## False-Positive Prevention

1. **Heat map as coverage.** One untested rule colouring a cell green is a reporting
   artefact; grade the mapping and require a test.
2. **Zero fires read as "no attacks".** A rule can be silent because a log source stopped
   parsing. Replay before concluding.
3. **Precision on tiny counts.** 1 TP of 2 alerts is not 50% precision you can rely on;
   report counts alongside percentages and pool quiet rules for judgement.
4. **Suppression by attacker-controlled fields.** Allow-listing `psexec.exe` by name also
   allow-lists a renamed attacker binary. Suppress by signed hash, host group, or account,
   with an expiry.
5. **Tuning to zero.** A rule tuned until it never fires has stopped detecting; keep a
   replay test that proves it still fires on the behaviour.
6. **Treating every detection as a page.** Low-fidelity signals are useful as correlation
   inputs; their fault is being routed to a human alone, not existing.
7. **Vendor rule packs counted as owned.** Imported content still needs an owner, tests,
   and tuning for this environment.

## Example Output

```
# Detection engineering review — Platform Security, 2026-09-30, 212 rules reviewed

## Summary
Rules: 212 · as code: 41% · with strategy: 18% · with test: 9%
Alert load: 1,640/week · ~68 analyst-hours/week (median 2.5 min) · precision 6.1%
Priority-technique coverage (tested, behavioural): 4 of 12

## Rule scorecard (excerpt)
| R-017 Impossible travel     | IAM team | y | n | n | 410 | 1.2% | 22% | 9%  | Retire → correlation signal |
| R-044 New AWS access key    | CloudSec | y | y | y | 35  | 14%  | 71% | 3%  | Keep; TPB is CI bots        |
| R-102 LSASS memory read     | EDR team | n | n | n | 0   | n/a  | n/a | n/a | Test failed — see below     |
| R-131 Encoded PowerShell    | none     | n | n | n | 260 | 0.8% | 4%  | 31% | Rewrite + owner            |

## ATT&CK mapping audit (priority excerpt)
| T1003.001 LSASS Memory   | R-102, R-103 | R-102 behavioural, R-103 tool (mimikatz hash) | R-102 fails | 0 |
| T1078.004 Cloud Accounts | R-044, R-051 | behavioural | yes | 1 |
| T1567 Exfil to Web Svc   | R-160        | nominal (field absent from proxy logs) | no | 0 |

## Test results
| T1003.001 | Atomic test #1 (procdump) | no | — | parser: EDR field TargetImage renamed in July agent update |
| T1059.001 | Atomic #1 encoded cmd     | yes | 4 min | — |

## Tuning actions
| R-017 | VPN egress in 3 countries flags as travel | drop to correlation-only; page only with new-device + MFA push denied | 410 → ~6/wk | single-signal impossible travel no longer pages |
| R-131 | admin scripts in SCCM | allow-list by signed script hash, 90-day expiry | 260 → ~40/wk | unsigned admin scripts still alert |

## Checked and cleared
R-044, R-051, R-077 (sudo to root on bastion): strategy present, test passes, precision ≥ 12%.

## Ranked fix list
1. Fix EDR parser mapping, add CI replay for R-102 → +1 priority technique, +0 alert load.
2. Retire R-017 as a page → −404 alerts/week (~17 analyst-hours) at minimal coverage cost.
3. Add DNS + proxy fields for R-160 → +1 technique once data exists.
## Data-source gaps: no EDR on 38 Linux build servers; proxy logs lack request body size.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — each rule scored on ownership, strategy, test, volume, and precision separately.
- **QA-10 Test Battery Protocol** — replaying technique behaviour and wiring passing tests into CI.
- **QA-12 False Positives Identification** — classifying FP causes and tuning without suppressing on attacker-controlled fields.
- **QA-21 Metric Gaming Vector Enumeration** — exposing heat-map coverage that can rise without detection improving.
- **QA-24 Dismissed-Candidates Coverage Table** — listing rules reviewed and cleared, with evidence.

## Related Prompts

- `security_soc_alert_triage_runbook.md` — the analyst steps each surviving rule should link to.
- `security_threat_hunting_plan.md` — hunts that confirm a gap and graduate into new detections.
- `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md` — automating triage once the detections feeding it are sound.
