---
title: "Job Posting Fit Decoder — Real Requirements, Hidden Signals, and an Apply/Skip Call"
category: personal-development/job-search
description: "Read one job posting from the candidate's side: separate the requirements that will actually screen from the wish-list, surface what the wording implies about the team and the role's hard parts, map each real requirement to the candidate's evidence, and return apply, apply-with-angle, or skip — the candidate-side reading of a posting, not the employer-side writing of one."
techniques:
  - DT-05
  - RT-05
  - QA-23
  - DS-06
  - QA-12
difficulty: beginner
tags:
  - job-search
  - job-posting
  - fit-assessment
  - requirements
  - application-strategy
  - candidate
  - should-i-apply
  - am-i-qualified
  - too-many-requirements
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-personal-development/job-search/jobsearch_target_role_and_market_map.md
  - domain-personal-development/job-search/jobsearch_cover_letter_builder.md
---

# Job Posting Fit Decoder

**Objective:** For one posting, produce a requirement-by-requirement fit map
against the candidate's evidence, a short list of what the posting implies but
does not say, the questions to answer before investing more time, and one
decision: apply, apply with a stated angle, or skip.

**When to Use:**
- A posting looks close and you want to know whether to spend two hours
  tailoring for it.
- You meet 60% of the list and cannot tell whether the missing 40% is fatal.
- You want the angle for a cover letter or recruiter message grounded in the
  posting's actual emphasis.
- **Not this prompt if** you are the employer writing or auditing a job
  description — that is `domain-hr-management/hiring/hr_job_description_writer.md`.
  This prompt reads a posting as the candidate does, with no access to the
  hiring manager's intent beyond the text.
- **Not this prompt if** you are still choosing which kind of role to target;
  decode postings after `jobsearch_target_role_and_market_map.md` has picked
  a family.

## Inputs / Context

**Required:**
1. **The full posting text**, including the "about us", benefits and
   location lines — those carry signal.
2. **The candidate's current résumé** (or the rewritten one).
3. **Hard constraints**: location, level floor, visa, hours.

**Optional:**
- Anything known about the company: size, stage, recent news, a contact
  inside.
- How the candidate found the posting (referral, board, recruiter).

## Method

1. **Split the list into three tiers (DT-05).** For each stated requirement:
   - **Screening** — likely to be filtered on: a licence, clearance,
     language, degree stated as required, years stated with "minimum", or a
     skill repeated in title, summary and list.
   - **Core** — the work the role clearly exists to do, evidenced by the
     responsibilities section.
   - **Wish-list** — "nice to have", "bonus", tools listed once at the end,
     or a list so long no single person meets it.
   State *why* each item landed in its tier, citing the posting text.

2. **Map evidence to each Screening and Core item (RT-05).** For each: the
   specific résumé line or experience that meets it, marked **Meets**,
   **Partial**, or **Gap**. A Meets without a résumé line to point at is a
   Partial.

3. **Decode what the wording implies.** Read for signals, and quote the line
   that carries each:
   - "Fast-paced", "wear many hats", "comfortable with ambiguity" → thin
     team or unclear scope.
   - A responsibility that belongs to a different role → a gap the hire will
     absorb.
   - "Build from scratch" vs "scale" vs "maintain" → which stage the function
     is in.
   - Reporting line, or its absence.
   - Compensation disclosed or not, where local law requires it.
   These are hypotheses, not facts.

4. **Separate what you can see from what you can't (QA-23).** Anything that
   depends on information the posting does not contain — team size, whether
   the role is a backfill, whether an internal candidate exists — becomes an
   explicit question with the answer that would change the decision, not an
   assumption.

5. **Decide (DS-06).**
   - Any **Screening** Gap that cannot be argued (licence, clearance, work
     authorisation) → **Skip**, unless a referral could get past the filter.
   - All Screening met, Core mostly Meets → **Apply**.
   - Screening met, Core Partial in one or two items the candidate can speak
     to → **Apply with angle**: name the angle in one sentence.
   - Constraint conflict → **Skip**, whatever the fit.

6. **Hand off the angle.** State the two requirements to lead with in the
   cover letter or recruiter note, and the one Gap to address head-on or
   leave alone.

## Output Format

```
# Posting fit — [role] at [company]

## Requirements by tier
| Requirement (quoted) | Tier | Why this tier | Your evidence | Meets / Partial / Gap |

## What the posting implies
- [signal] — from "[quote]" — hypothesis: [...]

## Questions before investing more
- [question] — changes the decision if: [...]

## Decision
[Apply | Apply with angle | Skip] — [one-line reason]
Angle: [one sentence, if applicable]

## Hand-off
Lead with: [requirement 1], [requirement 2]
Gap to address or leave: [...]
```

## Verification

- [ ] Every requirement is quoted and tiered with a reason tied to the text.
- [ ] Every Meets points to a specific résumé line.
- [ ] Every implied signal quotes its source line and is labelled a hypothesis.
- [ ] Unknowns are questions with a flip condition, not assumptions.
- [ ] Constraint conflicts were checked before fit.
- [ ] The decision follows the stated rule; any override is explained.

## False-Positive Prevention

1. **"Requirements" is not a single tier.** Treating a ten-item list as ten
   hard filters talks strong candidates out of applying; treating it as all
   wish-list talks weak ones into wasted applications. Tier it.
2. **Keyword overlap is not fit.** A posting that names your tools but wants
   them used at a scale you have never worked at is a Partial, not a Meets.
3. **A signal is a hypothesis.** "Fast-paced" does not prove a chaotic team;
   present it as a question for the screen, not a verdict.
4. **Years are a proxy.** "5+ years" with four years of directly matching
   scope is usually arguable; with seven years of adjacent work it may not be.
   Judge the scope, not the count.
5. **Do not decode intent you cannot see.** Whether the role is already
   earmarked for an internal candidate is unknowable from the text; do not
   discourage an application on a guess.
6. **Referral changes the screening tier.** A referred candidate often skips
   the automated filter; re-run the decision if a referral exists.
7. **Skip is a valid, useful output.** A decoder that always says "apply"
   has not decoded anything.

## Example Output

```
# Posting fit — Senior Product Analyst at a 600-person fintech (remote US)

## Requirements by tier
| Requirement (quoted) | Tier | Why this tier | Your evidence | Status |
|---|---|---|---|---|
| "Advanced SQL" | Screening | In title line, summary and list; likely a take-home | 4 yrs daily SQL on Snowflake (résumé, role 1) | Meets |
| "4+ years in product or growth analytics" | Screening | "Minimum" wording | 3 yrs product analytics + 2 yrs ops analytics | Partial |
| "Design and read A/B tests" | Core | Three responsibilities reference experiments | Ran 6 pricing-page tests with the growth PM (résumé, role 1) | Meets |
| "Own the activation metric" | Core | Named as the role's primary outcome | Built the onboarding funnel dashboard; did not own the metric | Partial |
| "Experience with dbt" | Wish-list | Listed once, under "bonus" | None | Gap |
| "Payments domain" | Wish-list | "Nice to have" | None | Gap |

## What the posting implies
- The function is being scaled, not built — from "join a team of five analysts" — hypothesis: established tooling, clear review process.
- Activation is a known problem — from "turn around activation" — hypothesis: the hire will be measured on it within two quarters.

## Questions before investing more
- Is "own the activation metric" shared with a PM? — if the analyst is solely accountable, the Partial becomes a stronger concern.

## Decision
Apply with angle — screening met on SQL, years are arguable on scope, both Core items have real evidence.
Angle: "I've already built and run the kind of onboarding-funnel experiments this role needs to move activation."

## Hand-off
Lead with: experiment design (6 tests), onboarding funnel dashboard.
Gap to leave: dbt and payments — wish-list; do not apologise for them.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — each requirement tiered and assessed on its own row.
- **RT-05 Evidence-Based Reasoning** — every tier and every Meets cites the posting or résumé line.
- **QA-23 Partial-Visibility Question Tier** — what the text cannot show becomes a question, not an assumption.
- **DS-06 Prioritization Guidance** — the decision rule weighs Screening over Core over Wish-list.
- **QA-12 False Positives Identification** — names the readings that look like fit or misfit but are not.

## Related Prompts

- `domain-hr-management/hiring/hr_job_description_writer.md` — the employer-side counterpart.
- `domain-personal-development/job-search/jobsearch_target_role_and_market_map.md` — choose the family before decoding postings.
- `domain-personal-development/job-search/jobsearch_cover_letter_builder.md` — turn the angle into a letter.
