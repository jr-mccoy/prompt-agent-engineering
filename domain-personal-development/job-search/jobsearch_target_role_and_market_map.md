---
title: "Target Role and Market Map — Pick One Primary Role Family Before You Apply Anywhere"
category: personal-development/job-search
description: "Turn a vague 'I'm looking for something new' into one primary target role family and one fallback, each with real posting titles, the employer segments actually hiring for it, the evidence gap between the candidate and a typical posting, and a kill signal — the market-facing step that comes after deciding to leave and before writing a single application."
techniques:
  - ST-01
  - RT-02
  - RT-23
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - job-search
  - target-role
  - labor-market
  - role-families
  - career-change
  - candidate
  - what-job-next
  - too-many-options
  - want-something-new
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/career-transformation/career_internal_vs_external_move.md
  - domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md
  - domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md
---

# Target Role and Market Map

**Objective:** Produce one primary target role family and one fallback, each
defined by the titles employers actually post, the segments that hire for it,
the candidate's evidence gap against a typical posting, and the signal that
would say the target is wrong — so every later résumé, profile and outreach
message is aimed at something specific.

**When to Use:**
- You have decided to look externally and your answer to "what are you looking
  for?" is still three unrelated things.
- You have applied broadly for weeks and cannot tell which kind of role is
  responding, because every application was aimed differently.
- You are changing function or industry and do not know what the target is
  *called* in postings.
- **Not this prompt if** you have not yet decided whether to move internally or
  externally — that is `domain-personal-development/career-transformation/career_internal_vs_external_move.md`,
  which compares the two moves. This prompt assumes the external decision is
  made and maps the market for it.
- **Not this prompt if** the question is whether your role is structurally at
  risk (`career-transformation/career_role_structural_vulnerability.md`) or what
  your durable skills are (`career_residual_skills_inventory.md`). Use those
  first if you have not; their outputs are good inputs here.

## Inputs / Context

**Required:**
1. **Current and last two roles**: title, what you actually did, scale (team,
   budget, volume, users), industry.
2. **Three to six candidate directions** you are considering, in your own words.
3. **Ten to twenty real postings** you have saved or would click on — pasted or
   linked. If you have none, the first task is to collect them; do not map a
   market from imagination.
4. **Hard constraints**: location or remote, minimum level, visa or clearance,
   hours, travel, earliest start.

**Optional:**
- Outputs from the career-transformation prompts (residual skills inventory,
  positioning statement).
- Who you know inside any target companies.

**If postings are missing:** stop and give the candidate a 45-minute collection
brief (which boards, which search strings, how many per direction) instead of
proceeding.

## Method

1. **Cluster postings into role families (ST-01).**
   Group the pasted postings by what the job *does*, not by title. Name each
   family by its most common posted title and list the title variants seen
   ("Implementation Manager", "Onboarding Lead", "Customer Launch Manager").
   A direction the user named that matches no posting is flagged: either the
   title is different in the market or the role is rare.

2. **Profile each family on five dimensions (RT-02).**

   | Dimension | What to record |
   |---|---|
   | Posted titles | the variants, most common first |
   | Hiring segments | company size, industry, stage that posted it |
   | Recurring must-haves | requirements appearing in ≥ half the postings |
   | Level signal | years asked, scope, reporting line |
   | Volume | how many of the user's postings fell here, and whether that reflects the market or just what they clicked |

3. **Tag every claim's provenance (RT-23).**
   Mark each profile cell `[postings]` (seen in the pasted set), `[user]` (the
   candidate's own knowledge), or `[estimate]` (reasoned, not observed). A
   family whose "hiring segments" row is all `[estimate]` has not been mapped;
   say so rather than presenting it as fact.

4. **Score the candidate's evidence gap per family.**
   For each recurring must-have, mark **Have (with evidence)**, **Adjacent**
   (done something close; needs translating), or **Missing**. Count Missing
   must-haves. Two or more Missing must-haves means the family is a
   reskilling project, not a search target — route to
   `career-transformation/career_reskilling_roadmap.md`.

5. **Rank and pick one primary, one fallback (DS-06).**
   Rank on: gap (fewest Missing), constraint fit, and market volume. Pick
   **one** primary family and **one** fallback. Do not present a menu. The
   fallback must be genuinely different in risk (e.g. a lateral role in the
   current function), not a synonym of the primary.

6. **Name the kill signal.**
   State the observable result that would mean the primary target is wrong —
   e.g. "fewer than 2 first-round screens from 25 tailored applications in
   four weeks". A target without a kill signal is never abandoned, only
   resented.

7. **Hand off.** One line each: what the résumé rewrite should lead with, which
   posting to decode first, and who in the network sits in the primary family.

## Output Format

```
# Target role map — [name], [date]

## Role families found in your postings
| Family | Posted titles | Hiring segments | Recurring must-haves | Level | Volume |
|---|---|---|---|---|---|
(each cell tagged [postings] / [user] / [estimate])

## Directions with no market match
- [direction] — [why: different title / rare / not a role]

## Evidence gap
| Family | Must-have | Have / Adjacent / Missing | Evidence or note |

## Decision
Primary: [family] — because [gap, fit, volume]
Fallback: [family] — different in risk because [...]
Dropped: [family] — [reason]

## Kill signal
If [observable result] by [date], revisit the primary.

## Hand-offs
- Résumé leads with: [...]
- Decode first: [posting]
- Network in primary family: [names or "none yet"]
```

## Verification

- [ ] Every family is built from pasted postings, not from the user's descriptions alone.
- [ ] Every profile cell carries a provenance tag, and `[estimate]`-only rows are called out.
- [ ] Must-haves are ones appearing in at least half the family's postings.
- [ ] Exactly one primary and one fallback; the fallback differs in risk.
- [ ] Any family with ≥ 2 Missing must-haves is routed to reskilling, not picked.
- [ ] The kill signal is observable and dated.
- [ ] Constraints (location, level, visa) were applied before ranking, not after.

## False-Positive Prevention

1. **What you clicked is not the market.** Twenty saved postings reflect the
   candidate's attention. Label volume as "in your set" and do not claim a
   family is hot because it dominates a biased sample.
2. **Titles lie in both directions.** "Analyst" at one company is "Associate"
   at another and "Specialist" at a third. Cluster on duties; a map built on
   titles double-counts one family and misses another.
3. **Adjacent is not Have.** "I sat in on vendor calls" is Adjacent to
   "managed vendor contracts", not equivalent. Promoting Adjacent to Have is
   how a map picks a target the résumé cannot support.
4. **A preferred qualification is not a must-have.** Only requirements that
   recur across postings count; one posting's wish-list is not the family's bar.
5. **Two targets is zero targets.** If the output hedges with co-primaries,
   every downstream document will be written for neither.
6. **A fallback that is the primary with a different title is not a fallback.**
   It fails under exactly the same conditions.
7. **Do not solve a skill gap with positioning.** A Missing must-have that is a
   licence, clearance or degree requirement cannot be "reframed"; say so.

## Example Output

```
# Target role map — Dana R., 2026-09-24

## Role families found in your postings (18 pasted)
| Family | Posted titles | Hiring segments | Recurring must-haves | Level | Volume |
|---|---|---|---|---|---|
| Implementation / onboarding | Implementation Manager; Onboarding Lead; Customer Launch Mgr [postings] | B2B SaaS, 200–2,000 staff, Series C+ [postings] | Project-managing customer go-lives; SQL or CSV data migration; cross-functional with Sales/Eng [postings] | 4–7 yrs, IC or lead [postings] | 9 of 18 in your set |
| Support operations | Support Ops Manager; CX Operations Lead [postings] | Same segment plus e-commerce [postings] | Zendesk/Salesforce admin; workforce forecasting; KPI dashboards [postings] | 5+ yrs, manages 0–3 [postings] | 6 of 18 |
| Customer success (book of business) | CSM; Senior CSM [postings] | Mixed [estimate] | Named-account retention quota; renewal ownership [postings] | 3–6 yrs [postings] | 3 of 18 |

## Directions with no market match
- "Customer experience strategy" — no postings in your set; at your level the work sits inside Support Ops titles.

## Evidence gap
| Family | Must-have | Status | Evidence or note |
|---|---|---|---|
| Implementation | Customer go-lives | Adjacent | Ran 14 enterprise escalations to resolution; not framed as launches |
| Implementation | Data migration | Have | Led 2023 Zendesk→Salesforce ticket migration, 400k records |
| Implementation | Cross-functional | Have | Weekly escalation sync with Eng for 3 years |
| Support ops | Admin | Have | Zendesk admin 5 yrs |
| Support ops | Forecasting | Adjacent | Built staffing spreadsheet; no formal WFM tool |
| CS | Renewal quota | Missing | Never carried a number |

## Decision
Primary: Implementation / onboarding — 0 Missing, fits remote constraint (7 of 9 remote), largest share of your set.
Fallback: Support operations — lateral from current function, lower change risk; recruiters will read it without translation.
Dropped: Customer success — renewal quota Missing and it is the core of the job, not a gap to reframe.

## Kill signal
If fewer than 2 first-round screens from 25 tailored Implementation applications by 2026-10-22, shift weight to Support Ops.

## Hand-offs
- Résumé leads with: the 400k-record migration, rewritten as a go-live.
- Decode first: the Launch Manager posting at the 800-person HR-tech company (closest to your stack).
- Network in primary family: former colleague Theo, now Implementation Lead at a payroll SaaS.
```

## Techniques Used

- **ST-01 Clear Objective Statement** — the output is one primary and one fallback, not an exploration.
- **RT-02 Multi-Dimensional Analysis** — each family profiled on the same five dimensions so they compare.
- **RT-23 Input Provenance Tagging** — separates what postings show from what the candidate assumes.
- **DS-06 Prioritization Guidance** — ranks on gap, constraint fit and volume and forces a pick.
- **QA-12 False Positives Identification** — names what looks like a viable target but is not.

## Related Prompts

- `domain-personal-development/career-transformation/career_internal_vs_external_move.md` — decide internal vs external first.
- `domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md` — decode one posting in the primary family.
- `domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md` — rewrite the résumé toward the primary.
