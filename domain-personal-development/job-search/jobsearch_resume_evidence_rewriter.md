---
title: "Résumé Evidence Rewriter — Bullets That Survive a Reference Check"
category: personal-development/job-search
description: "Rewrite résumé bullets for one target role family as action–scope–result statements built only from facts the candidate can substantiate, tagging every number as verified, estimated or missing, flagging any claim that would not survive a reference check, and reordering content toward the target — a rewrite of the document, not an inventory of skills."
techniques:
  - DD-02
  - ST-46
  - RT-23
  - QA-26
  - QA-01
difficulty: intermediate
tags:
  - job-search
  - resume
  - cv
  - accomplishments
  - honesty
  - candidate
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md
  - domain-personal-development/job-search/jobsearch_linkedin_profile_audit.md
---

# Résumé Evidence Rewriter

**Objective:** Produce a rewritten résumé for one target role family in which
every bullet states what the candidate did, at what scope, with what result —
using only facts they can substantiate — plus a flag list of claims that
need a source, a softer verb, or deletion.

**When to Use:**
- Your bullets describe duties ("Responsible for vendor management") rather
  than results.
- You are applying to a new role family and the résumé is still ordered for
  the old one.
- You have numbers in your head but are unsure which you can defend.
- **Not this prompt if** you do not yet know what you are good at — that is
  `domain-personal-development/career-transformation/career_residual_skills_inventory.md`,
  which inventories judgment and context with evidence. This prompt consumes
  such an inventory and rewrites the *document*.
- **Not this prompt if** you have no target role family yet. Run
  `jobsearch_target_role_and_market_map.md` first; a résumé rewritten for
  "anything" is optimised for nothing.

## Inputs / Context

**Required:**
1. **The current résumé**, pasted in full.
2. **The target role family** and two or three representative postings.
3. **For each role in the last 10 years**: what changed because you were there,
   and how you know. Rough is fine; the prompt will ask follow-ups.

**Optional:**
- Performance reviews, launch notes, dashboards, emails of thanks — anything
  that would let a number be checked.
- Constraints: page limit, country convention (US résumé vs UK/EU CV), ATS
  portal the employer uses.

## Constraints

**Must:**
- Use only facts the candidate supplied or confirmed in follow-up.
- Tag every figure `[verified]` (a document or system shows it),
  `[estimate]` (the candidate's defensible approximation, with basis), or
  `[missing]` (a result exists but no number is known).
- Keep titles, dates, employers and credentials exactly as held.

**Must Not:**
- Invent or round up a metric, title, team size, credential or tool.
- Upgrade a verb beyond what happened ("led" for "contributed to", "built"
  for "configured", "managed" when no one reported to them).
- Claim a team result as individual without saying the candidate's part.

## Method

1. **Dry-run the first bullet (QA-26).** Rewrite the most recent role's top
   bullet. The first fact you would have to invent to finish it — a number,
   a scope, an outcome — becomes the first follow-up question. Ask all such
   questions in one batch before rewriting anything else.

2. **Translate duties into results (DD-02).** For each bullet: what was the
   state before, what did the candidate specifically do, what was the state
   after? "Handled escalations" becomes "Resolved 14 enterprise escalations
   in 2025; 12 accounts renewed" — if, and only if, the candidate confirms
   those facts.

3. **Lead with the result (ST-46).** Bullet shape: *verb + what + scope +
   result*. Put the result the target posting cares about first when it is
   the strongest element.

4. **Tag provenance (RT-23).** Every number gets its tag and, for
   `[estimate]`, a one-line basis ("~30% — ticket backlog went from ~600 to
   ~420 per the weekly report I sent"). A bullet with a `[missing]` result
   stays qualitative; it is not given a plausible-sounding number.

5. **Reorder toward the target.** Within each role, order bullets by relevance
   to the target family's recurring must-haves. Cut bullets that serve only
   the old function when space is short. Move a buried relevant project up.

6. **Run the reference-check test (QA-01).** For each bullet ask: if the
   hiring manager called the candidate's former manager and read it aloud,
   would the manager agree? Anything that would draw "well, sort of" is
   flagged with a fix: add the candidate's specific part, soften the verb,
   or cut.

7. **ATS and format pass.** Standard section headings, no text in images or
   tables, target-family keywords present where they are true, dates
   consistent. Keywords that are not true of the candidate are not added.

## Output Format

```
# Résumé rewrite — [name] → [target family]

## Follow-up questions (answer before final)
1. [...]

## Rewritten résumé
[Summary line — 1–2 sentences, target-facing]
[Role, employer, dates — unchanged]
- [bullet] {tags on each figure}

## Provenance ledger
| Bullet | Figure | Tag | Basis / source |

## Reference-check flags
| Original claim | Problem | Fix |

## Cut or moved
- [bullet] — [cut / moved up / moved down] because [...]
```

## Verification

- [ ] No figure lacks a tag; every `[estimate]` has a stated basis.
- [ ] No title, date, employer, credential or tool differs from the input.
- [ ] Every "led / managed / owned" is backed by the candidate's confirmation of that scope.
- [ ] Team results name the candidate's part.
- [ ] Bullets in each role are ordered by relevance to the target family.
- [ ] Keywords added for ATS are all true of the candidate.
- [ ] Follow-up questions were asked before invented detail was needed.

## False-Positive Prevention

1. **A number is not evidence because it is specific.** "Improved efficiency
   by 37%" with no basis is more dangerous than "cut weekly reporting from two
   days to half a day": it invites a question the candidate cannot answer.
2. **Result-shaped is not result.** "Drove alignment across stakeholders" has
   the grammar of an accomplishment and none of the content. If nothing
   observable changed, it is a duty.
3. **Plausible scope is still invented scope.** Do not infer "team of 8" from
   "ran the night shift". Ask.
4. **The strongest verb is not the best verb.** A reference call that
   contradicts "led" costs more than "co-led" ever would.
5. **ATS keyword stuffing is a false positive for fit.** A keyword the
   candidate cannot discuss for two minutes in a screen gets them the screen
   and loses the interview.
6. **Removing the old function entirely can read as a gap.** Cut its bullets,
   not the role; the dates must still account for the time.
7. **A clean rewrite that silently dropped a flag is worse than a messy one.**
   Every flagged claim must appear in the flags table with its resolution.

## Example Output

```
# Résumé rewrite — Marcus T. → Operations analyst (logistics)

## Follow-up questions (answered)
1. "Improved pick accuracy" — from what to what, and where is it recorded? → 97.1% to 99.2%, monthly WMS quality report.
2. "Managed a team" — how many reported to you directly? → 11 associates on nights; no hiring authority.
3. "Created dashboards" — in what tool, used by whom? → Excel + Power Query, used by the site GM in the Monday review.

## Rewritten résumé
Warehouse shift supervisor moving into operations analysis; four years turning WMS exports into decisions a site GM acted on.

Night Shift Supervisor, [3PL employer], Reno NV — 2022–present
- Raised pick accuracy from 97.1% to 99.2% {verified} in 9 months by re-slotting the 40 highest-error SKUs using WMS error exports.
- Built the Monday site-review workbook (Excel, Power Query) the GM used to set weekly labour plans; cut prep from ~6 hrs to ~1 hr {estimate}.
- Supervised 11 associates on nights; ran daily safety huddles; zero recordable incidents in 2025 {verified}.

## Provenance ledger
| Bullet | Figure | Tag | Basis / source |
|---|---|---|---|
| 1 | 97.1% → 99.2% | verified | Monthly WMS quality report, Jan–Sep 2025 |
| 2 | ~6 hrs → ~1 hr | estimate | Marcus's own timing; GM can confirm |
| 3 | 11 associates | verified | Shift roster |
| 3 | zero recordables | verified | Site OSHA log |

## Reference-check flags
| Original claim | Problem | Fix |
|---|---|---|
| "Managed a team of 11" | No hiring or review authority; "managed" overstates | "Supervised 11 associates" |
| "Expert in Power BI" | Used Power Query in Excel; never Power BI | Removed; Power Query stated instead |
| "Reduced costs significantly" | No figure, no source | Cut; re-slotting bullet carries the result |

## Cut or moved
- Forklift certification bullet — moved to Certifications section.
- "Trained new hires" — cut for space; less relevant to analyst postings than the workbook.
```

## Techniques Used

- **DD-02 Vague-to-Concrete Translation** — duties become checkable before/after statements.
- **ST-46 Assertion-Evidence Structure** — each bullet leads with the result.
- **RT-23 Input Provenance Tagging** — every figure labelled verified, estimate or missing.
- **QA-26 First-Invented-Fact Test** — finds the gaps and asks before inventing.
- **QA-01 Self-Verification** — the reference-check pass on every bullet.

## Related Prompts

- `domain-personal-development/career-transformation/career_residual_skills_inventory.md` — what you hold, before how you write it.
- `domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md` — which must-haves the rewrite must surface.
- `domain-personal-development/job-search/jobsearch_linkedin_profile_audit.md` — keep the public profile consistent with this document.
