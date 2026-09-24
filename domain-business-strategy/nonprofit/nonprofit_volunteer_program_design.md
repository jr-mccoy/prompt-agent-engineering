---
title: "Volunteer Program Design — Roles, Risk-Tiered Screening, Retention, and Honest Hours Valuation"
category: business-strategy/nonprofit
description: "Design or repair a nonprofit volunteer program as an operating system: role descriptions sized in hours, recruitment targets from capacity and attrition, screening proportional to each role's risk with safeguarding gates, retention practice, and a volunteer-hours value that is labelled for what it is; distinct from biblical_churchstaff_volunteer_recruitment_role_design, which fills church ministry roles, and from discipleship_safeguarding_and_conduct_policy, which is the full safeguarding policy this prompt defers to."
techniques:
  - QA-08
  - NE-11
  - DS-06
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - nonprofit
  - volunteer-management
  - screening
  - safeguarding
  - retention
  - operations
  - volunteers-keep-quitting
  - need-more-volunteers
  - background-checks
updated: "2026-09-24"
related_prompts:
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md
  - domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md
  - domain-discipleship/program-operations/discipleship_program_design_blueprint.md
---

# Volunteer Program Design

**Objective:** Produce a volunteer program a nonprofit can actually run — roles with
real time commitments, a recruitment number derived from capacity and attrition,
screening that matches each role's risk, a retention plan, and a volunteer-hours
figure presented honestly.

**When to Use:**
- A program's growth depends on volunteers and nobody knows how many are needed.
- Volunteers leave within months and nobody knows why.
- Screening is the same for every role — either too heavy for event helpers or too
  light for one-to-one work.
- The annual report needs a value for volunteer time.

**Not this prompt if:**
- You are staffing church ministry roles — `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md`.
- You need the full safeguarding and conduct policy for work with minors or
  vulnerable adults — `domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md`
  is the serious version. This prompt sets screening tiers and points there; it does
  not replace it.
- You are designing a mentoring-pair program end to end —
  `domain-discipleship/program-operations/discipleship_program_design_blueprint.md`.

## Inputs

1. The program(s) volunteers serve and the service capacity target.
2. Current volunteers: count, roles, hours logged, tenure, exits in the last year
   and exit reasons if known.
3. Who volunteers work with (adults, minors, people who may be vulnerable), where,
   and whether supervised.
4. Staff time available to recruit, train and supervise.
5. Insurance and any legal screening requirements known for the jurisdiction.

## Method

1. **Design roles in hours (CM-02).** Each role: purpose, tasks, weekly hours, minimum
   commitment period, skills, supervisor, and what the role is *not*. A role with no
   hour estimate cannot be recruited for honestly.

2. **Derive the recruitment number (NE-11).**
   `needed = capacity target ÷ service per volunteer`
   `expected exits = current volunteers × annual attrition rate`
   `recruit = needed − (current − expected exits)`
   Then gross up for the drop-off between applying and serving (use the program's own
   rate, or mark `[estimate]`).

3. **Tier screening by risk (QA-08).** Screening is a gate a volunteer passes before
   the role begins:

   | Tier | Role profile | Gate |
   |---|---|---|
   | 1 | Supervised group tasks, no one-to-one contact | Application, orientation, conduct agreement |
   | 2 | One-to-one with adults in a public or supervised setting | Tier 1 + interview + two references + role training |
   | 3 | Contact with minors or adults who may be vulnerable; unsupervised; access to money or personal data | Tier 2 + background check as the jurisdiction requires + safeguarding training + the safeguarding policy's conduct rules |

   Which checks are legally required — and how records are kept — is a question for
   counsel or the insurer. The prompt flags it; it does not answer it.

4. **Plan retention (DS-06).** Prioritise by exit reasons. The usual order of impact:
   a clear role and a named supervisor; being used well on the day; being thanked
   specifically; seeing results; a path to more responsibility. Schedule a 30-day
   check-in and an annual conversation.

5. **Value volunteer hours honestly.** `hours logged × published hourly value` —
   using the current published figure for the jurisdiction, stated with its source
   and year. Label it "equivalent value of volunteer time" in reports. Whether any
   volunteer service can be recognised in the financial statements is an accounting
   question (rules generally limit it to specialised services) — flag it for the
   accountant; do not book it.

6. **Check (QA-01).** Recruitment arithmetic, staff supervision hours, and every
   Tier 3 role linked to the safeguarding policy.

## Output Format

```
# Volunteer program — [organisation / program]

## Roles
| Role | Hours/week | Min. term | Screening tier | Supervisor | Not this role |

## Recruitment arithmetic
needed / expected exits / recruit / gross-up → target

## Screening gates
| Tier | Roles | Gate steps | Records kept | Legal check flagged |

## Retention plan
| Exit reason (count) | Change | Owner |

## Supervision load
[staff hours/week required vs available]

## Volunteer-hours value
[hours] × [rate, source, year] = [value] — labelled, not booked

## Flags for qualified review
```

## Verification

- [ ] Every role has hours, a term, a tier and a supervisor.
- [ ] Recruitment arithmetic reproduces from the stated inputs.
- [ ] Every role touching minors or possibly vulnerable adults is Tier 3.
- [ ] Legal screening requirements are flagged, not asserted.
- [ ] Supervision hours fit staff time available.
- [ ] The hours value states its rate source and year and is not booked as revenue.

## False-Positive Prevention

1. **"We always need more volunteers" is not a target.** Derive the number, or the
   recruiting never ends and supervision collapses.
2. **Heavy screening for every role drives away low-risk help.** Tier by risk; a
   background check for a one-off event helper is friction without protection.
3. **Light screening for one-to-one work is the real danger.** Adults with literacy,
   language or disability barriers may be vulnerable; default such roles to Tier 3
   until the safeguarding lead decides otherwise.
4. **Do not state what the law requires.** Screening, records and reporting duties
   vary by jurisdiction; flag for counsel.
5. **Volunteer-hours value is not income.** Present it as an equivalent value, with
   its source, never as money raised.
6. **Recognition events do not fix a bad role.** If exits cite "unclear what to do",
   fix the role before planning the dinner.
7. **Dual failure:** a program so procedural nobody can start within a month loses
   the volunteers it screened.

## Example Output

```
# Volunteer program — Riverbend Adult Literacy Tutoring, 2027

## Roles
| Role | Hrs/wk | Term | Tier | Supervisor | Not this role |
| Literacy tutor | 2 | 9 months | 3 | Tutor coordinator | Not a counsellor or caseworker |
| Intake greeter | 3 (monthly) | 6 months | 1 | Program director | No learner records access |
| Assessment assistant | 4 | 6 months | 3 | Coordinator | Does not score assessments alone |

## Recruitment arithmetic (tutors)
Needed: 120 learners ÷ 2 learners per tutor = 60
Expected exits: 41 × 20% attrition (2025 roster) = 8
Recruit: 60 − (41 − 8) = 27
Gross-up: 60% of applicants reach first session (2025 intake) → 27 ÷ 0.6 = 45 applicants

## Screening gates
| Tier | Roles | Gate | Records | Legal check flagged |
| 1 | Intake greeter | Application, orientation, conduct agreement | Application file | — |
| 3 | Tutor, assessment assistant | + interview, 2 references, background check, safeguarding training | Secure file, retention per policy | Check type and retention — counsel/insurer |

## Retention plan
| Exit reason (8 exits, 2025) | Change | Owner |
| Unclear expectations (3) | Written role + 30-day check-in | Coordinator |
| Schedule conflict (3) | Offer evening slots at library branch | Coordinator |
| Felt unused on arrival (2) | Pair every new tutor with a learner by week 2 | Program director |

## Supervision load
45 applicants to process + 60 active tutors ≈ 9 hrs/week in Q1, 6 thereafter;
coordinator has 8 → Q1 gap of 1 hr/week: program director covers intake interviews.

## Volunteer-hours value
3,280 hours (2,880 session + 400 training/prep, 2025 log) × [current published
hourly value for the state, source, year] = [value]. Illustration at $30.00/hr:
$98,400 — replace with the published figure before use. Labelled "equivalent value".

## Flags for qualified review
- Background-check type and record retention — counsel / insurer
- Whether any volunteer service qualifies for financial-statement recognition — accountant
```

## Techniques Used

- **QA-08 Gate-Based Verification:** screening tiers as gates before a role starts.
- **NE-11 Embedded Calculation Formulas:** recruitment and hours-value arithmetic.
- **DS-06 Prioritization Guidance:** retention changes ranked by exit reason.
- **CM-02 Constraint Specification:** roles bounded by hours, term and "not this role".
- **QA-01 Self-Verification:** arithmetic, supervision load and Tier 3 links checked.

## Related Prompts

- `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md` — church ministry roles
- `domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md` — the safeguarding policy Tier 3 relies on
- `domain-discipleship/program-operations/discipleship_program_design_blueprint.md` — end-to-end pairing program design
