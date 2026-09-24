---
title: "LinkedIn Profile Audit — Section by Section Against One Target Role"
category: personal-development/job-search
description: "Audit a LinkedIn profile section by section against one target role family and how recruiters actually search — headline, about, experience, skills, and consistency with the résumé — returning a pass/fix verdict per section, rewritten text for the fixes, and a list of claims that differ from the résumé or cannot be substantiated."
techniques:
  - DT-05
  - DD-02
  - RP-02
  - RT-05
  - QA-12
difficulty: beginner
tags:
  - job-search
  - linkedin
  - professional-profile
  - recruiter-search
  - personal-brand
  - candidate
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/career-transformation/career_positioning_statement.md
  - domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md
  - domain-personal-development/job-search/jobsearch_networking_outreach_plan.md
---

# LinkedIn Profile Audit

**Objective:** Produce a section-by-section verdict on a LinkedIn profile —
pass or fix, with the reason — plus rewritten text for each fix and a
consistency table against the résumé, so the profile is findable for one
target role and says nothing the résumé cannot back.

**When to Use:**
- You are about to start outreach and people will look you up before
  replying.
- Recruiters are not finding you, or the ones who do are pitching the job you
  are leaving.
- You rewrote your résumé for a new role family and the profile still
  describes the old one.
- **Not this prompt if** you do not yet have a one-line answer to "what do you
  do and for whom" — write that first with
  `domain-personal-development/career-transformation/career_positioning_statement.md`.
  That prompt produces the positioning core; this one audits the whole public
  profile against it and against recruiter search.
- **Not this prompt if** you want a content or posting strategy to build an
  audience; this is a profile audit for a job search, not creator growth.

## Inputs / Context

**Required:**
1. **The profile text**: headline, about, each experience entry, skills list,
   featured section, open-to-work settings. Paste it; screenshots lose text.
2. **The target role family** and the titles recruiters search for it.
3. **The current résumé** — the consistency check depends on it.

**Optional:**
- Positioning statement.
- Whether the search is confidential from the current employer (changes the
  open-to-work and headline advice).
- Location and remote preference.

## Method

1. **Audit each section on its own row (DT-05).** Sections: headline, about,
   current experience, prior experience, skills, featured, open-to-work,
   location. For each, a verdict — **Pass** or **Fix** — and the one reason.

2. **Read the headline as a recruiter's search result (RP-02).** The headline
   is what appears next to the name in search results and connection
   requests. Test it: does it contain a title recruiters search for in the
   target family, and does it say what kind of problem the candidate works
   on? A clever tagline with no searchable title fails. If the search is
   confidential, the headline names the target title without "seeking".

3. **Translate the about section into concrete claims (DD-02).** Replace
   adjectives with the pattern of work and two or three results. First two
   lines matter most — they are what shows before "see more". Length: short
   enough to read on a phone.

4. **Check experience entries for target relevance.** Each current and recent
   entry leads with the work relevant to the target family. Entries need not
   duplicate the résumé bullet for bullet, but must not contradict it.

5. **Run the consistency check (RT-05).** For titles, dates, employers, team
   sizes, figures and credentials: quote the profile and the résumé side by
   side. Any mismatch is flagged. Any figure on the profile that is not on the
   résumé and not substantiated is flagged for removal or sourcing.

6. **Prune and order skills.** Put the target family's recurring must-have
   skills that the candidate truly has in the top positions. Remove skills
   the candidate would not want to be interviewed on.

7. **Settings pass.** Open-to-work (recruiter-only vs public), location,
   custom URL, contact visibility — each with the reason for the choice given
   the confidentiality input.

## Output Format

```
# LinkedIn audit — [name] → [target family]

## Verdicts
| Section | Pass / Fix | Reason |

## Rewrites
### Headline
Before: [...]
After: [...]
### About (first two lines shown before "see more" in bold)
[...]
### [Other fixed sections]

## Consistency with résumé
| Item | Profile says | Résumé says | Action |

## Unsubstantiated claims
- [claim] — [remove / add source / soften to ...]

## Settings
- Open to work: [recruiter-only / public / off] — because [...]
```

## Verification

- [ ] Every section has a verdict and a reason.
- [ ] The headline contains at least one title recruiters search for in the target family.
- [ ] The about section's first two lines state the kind of work and one result.
- [ ] Every title, date, employer, figure and credential matches the résumé or is flagged.
- [ ] Top skills are target must-haves the candidate actually has.
- [ ] Settings advice reflects whether the search is confidential.

## False-Positive Prevention

1. **A memorable headline is not a findable one.** "Turning chaos into
   clarity" appears in no recruiter search. Pass only headlines with a
   searchable title.
2. **Profile–résumé drift is a credibility problem, not a style one.**
   A recruiter who sees "Manager" on the profile and "Senior Associate" on
   the résumé asks which is true. Flag every mismatch, however small.
3. **More skills is not more signal.** Fifty skills bury the five that match
   the target, and each one listed is something a screen may probe.
4. **Endorsement counts are not evidence.** Do not cite them to justify a
   skill's position; they measure network size.
5. **Public open-to-work is not always right.** For a confidential search,
   recommending the public banner is a harmful default.
6. **A polished about section can still be generic.** If the text would fit
   anyone in the function, it fails the audit even if it reads well.
7. **Do not add claims to make the profile competitive.** The profile may be
   *less* detailed than the résumé; it may not be *more* impressive.

## Example Output

```
# LinkedIn audit — Priya S. → Reliability engineering (manufacturing)

## Verdicts
| Section | Verdict | Reason |
|---|---|---|
| Headline | Fix | "Mechanical Engineer | Problem Solver | Lifelong Learner" — no target title, two filler phrases |
| About | Fix | Opens with a quote; first result appears in paragraph 3 |
| Current experience | Fix | Leads with CAD design work; the FMEA and downtime work is bullet 5 |
| Prior experience | Pass | Short, consistent with résumé |
| Skills | Fix | 43 skills; "Reliability Engineering" and "FMEA" not in top 10 |
| Featured | Pass | Links a conference poster on bearing-failure analysis |
| Open to work | Fix | Public banner on; search is confidential |

## Rewrites
### Headline
Before: Mechanical Engineer | Problem Solver | Lifelong Learner
After: Mechanical Engineer → Reliability | FMEA, root-cause analysis, and downtime reduction on packaging lines
### About
**I find out why production lines stop and make them stop less. On two packaging lines at a food manufacturer, I cut unplanned downtime from 9.4% to 6.1% over 2025.**
I run FMEAs with maintenance and operations, lead root-cause investigations after failures, and turn the findings into PM schedule changes that stick. Before that, five years of equipment design, which is why I read failure data the way a designer does.

## Consistency with résumé
| Item | Profile says | Résumé says | Action |
|---|---|---|---|
| Title, current | "Senior Mechanical Engineer" | "Mechanical Engineer II" | Use the résumé title; "Senior" was never held |
| Downtime result | "cut downtime by 40%" | 9.4% → 6.1% {verified} | Use the résumé figure (a 35% relative reduction, stated as the absolute figures) |

## Unsubstantiated claims
- "Six Sigma Black Belt" — résumé shows Green Belt; change to Green Belt.

## Settings
- Open to work: recruiter-only — public banner is visible to the current employer; search is confidential.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — one verdict per profile section.
- **DD-02 Vague-to-Concrete Translation** — adjectives in the about section become work and results.
- **RP-02 Audience-Specific Framing** — the headline is read as a recruiter's search result.
- **RT-05 Evidence-Based Reasoning** — the consistency table quotes both documents.
- **QA-12 False Positives Identification** — polished-but-useless patterns named and failed.

## Related Prompts

- `domain-personal-development/career-transformation/career_positioning_statement.md` — the positioning core the headline and about draw on.
- `domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md` — the document the profile must match.
- `domain-personal-development/job-search/jobsearch_networking_outreach_plan.md` — outreach that sends people to this profile.
