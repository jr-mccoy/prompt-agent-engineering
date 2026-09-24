---
title: "Cover Letter Builder — One Posting, One Angle, Three Proof Points"
category: personal-development/job-search
description: "Write a cover letter for one specific posting that opens with the candidate's angle on the role's main problem, backs it with two or three substantiated proof points mapped to the posting's core requirements, addresses at most one gap directly, and fits on half a page — refusing the reusable template letter and any claim not on the résumé."
techniques:
  - ST-01
  - RP-02
  - ST-46
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - job-search
  - cover-letter
  - application
  - professional-writing
  - candidate
  - applying-for-jobs
  - stand-out-applicant
  - explain-a-gap
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md
  - domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md
  - domain-personal-development/career-transformation/career_positioning_statement.md
---

# Cover Letter Builder

**Objective:** Produce a cover letter of 180–280 words for one named posting
that a hiring manager can read in under a minute and come away knowing why
this candidate, for this problem, with what proof.

**When to Use:**
- The application asks for a letter, or you are applying to a small company
  where a letter will actually be read.
- You are changing function and the résumé alone will not explain why you fit.
- You have decoded the posting and have an angle, and need it written.
- **Distinct from** letters elsewhere in the repo: `domain-science/writing-communication/science_cover_letter_to_editor.md`
  is a manuscript-submission letter to a journal, and the professional-writing
  domain covers general business correspondence. No existing prompt writes a
  candidate's job-application letter.
- **Not this prompt if** you need a cold message to someone who has not posted
  a role — that is outreach, in `jobsearch_networking_outreach_plan.md`.

## Inputs / Context

**Required:**
1. **The posting**, full text.
2. **The candidate's résumé** — the letter may not claim anything that is not
   on it or confirmed in conversation.
3. **The angle**, ideally from `jobsearch_job_posting_fit_decoder.md`: the two
   requirements to lead with and the gap to address or leave.

**Optional:**
- Who to address it to, if known.
- A referral name, with that person's permission to use it.
- A genuine, specific reason for this company (a product used, a public talk,
  a problem they wrote about). If none exists, the letter does not fake one.

## Constraints

**Must:**
- Name the role and, if there is one, the referral in the first two sentences.
- Contain two or three proof points, each traceable to a résumé line.
- Stay within 280 words and three to four short paragraphs.

**Must Not:**
- Open with "I am writing to apply for…", "I am excited to…", or a restatement
  of the candidate's name and title.
- Repeat the résumé in prose.
- Invent enthusiasm for the company, or a connection to its mission, that the
  candidate did not supply.
- Apologise for a gap, or mention more than one.

## Method

1. **State the letter's single job (ST-01).** Write, for internal use only,
   one sentence: "This letter must make the reader believe [candidate] can
   [solve the posting's central problem] because [proof]." Everything that
   does not serve that sentence is cut.

2. **Write for the likely reader (RP-02).** A recruiter at a large company
   scans for the role match and the must-haves in 10 seconds; a hiring
   manager at a 40-person company reads for judgment and whether the
   candidate understood the problem. Adjust the opening and density
   accordingly and say which reader was assumed.

3. **Open with the angle (ST-46).** First paragraph: the role, the referral if
   any, and the angle — what the candidate sees as the role's main problem and
   why they are placed to solve it.

4. **Prove it in two or three points.** Second paragraph: each proof point is
   a result in one or two sentences, mapped to a Core requirement from the
   posting. Use the résumé's verified or estimated figures with the same
   wording; do not inflate them for prose.

5. **Handle at most one gap.** Only if the gap is a Screening item a reader
   will notice. One sentence: what the candidate has instead, stated as fact,
   not apology. Wish-list gaps are left alone.

6. **Close with a specific next step.** One or two sentences: what the
   candidate would like to discuss, and nothing about "any opportunity".

7. **Run the substantiation pass (CM-02, QA-01).** Check every factual clause
   against the résumé; check the word count; check the banned openers;
   check that the company-specific line is one the candidate supplied.

## Output Format

```
# Cover letter — [role], [company]

Assumed reader: [recruiter scan | hiring-manager read] — because [...]
Internal job sentence: [...]

---
[Letter, 180–280 words]
---

## Proof-point trace
| Claim in letter | Résumé line | Posting requirement served |

## Checks
Word count: [n] | Banned openers: none | Gaps addressed: [0 or 1] | Company line source: [candidate-supplied / omitted]
```

## Verification

- [ ] Role (and referral, if any) named in the first two sentences.
- [ ] Two or three proof points, each traced to a résumé line and a posting requirement.
- [ ] No figure differs from the résumé's figure.
- [ ] At most one gap addressed, and only a Screening-tier one.
- [ ] 180–280 words.
- [ ] No banned opener; no generic "any opportunity" close.
- [ ] Any company-specific line was supplied by the candidate.

## False-Positive Prevention

1. **Specific-sounding flattery is still flattery.** "I've long admired your
   commitment to innovation" names nothing. If the candidate has no real
   reason, leave the line out; its absence costs less than its falseness.
2. **A résumé in paragraphs is not a letter.** If the proof points could be
   swapped for the résumé's bullets with no loss, the letter adds nothing.
   Each proof point must connect a result to *this* posting's problem.
3. **Confidence is not inflation.** Turning "co-led" on the résumé into "led"
   in the letter creates an inconsistency a reader will catch in the screen.
4. **Addressing every gap signals every gap.** One Screening gap, handled in a
   sentence, reads as self-awareness; three reads as a list of reasons to
   reject.
5. **Reusable is the failure mode.** If swapping the company name makes the
   letter work elsewhere, it has not been written for this posting.
6. **Length does not show effort to the reader.** Past half a page, the second
   half is not read.

## Example Output

```
# Cover letter — Instructional Designer, K-12 math platform (Series B, 120 staff)

Assumed reader: hiring-manager read — small company; posting signed by the Head of Learning.
Internal job sentence: This letter must make the reader believe Aisha can design lessons that hold students through the hard middle of a unit, because she has done it with 140 real students and measured it.

---
Dear Ms. Okafor,

I'm applying for the Instructional Designer role. Your posting says the hardest part of the job is keeping students engaged through multi-step problems; that is the problem I have spent six years solving in a Grade 7 classroom.

In 2024–25 I redesigned our ratios unit around worked examples that fade step by step. Across my 140 students, unit-test completion rose from 71% to 89%, from the school's assessment records. I built those materials in Google Slides and Desmos and shared them with the four other teachers in my department, who adopted them the next term. I also wrote the department's rubric for multi-step word problems, which is still in use, and I revise my units each term from item-level results rather than from how a lesson felt.

I have not yet worked in an authoring tool like Articulate; I've completed the Articulate 360 trial course and built one sample module, linked on my résumé.

I'd welcome the chance to walk through how I'd approach one of your middle-school units, starting with where students currently drop off.

Aisha Rahman
---

## Proof-point trace
| Claim in letter | Résumé line | Posting requirement served |
|---|---|---|
| Ratios unit, 71% → 89% completion | Teacher, role 1, bullet 1 {verified} | "Design engaging multi-step learning sequences" |
| Adopted by four teachers | Teacher, role 1, bullet 2 {verified} | "Collaborate with subject-matter experts" |
| Department rubric | Teacher, role 1, bullet 3 | "Develop assessment criteria" |

## Checks
Word count: 181 | Banned openers: none | Gaps addressed: 1 (authoring tool, Screening) | Company line source: posting's own statement of the problem
```

## Techniques Used

- **ST-01 Clear Objective Statement** — the internal job sentence governs every cut.
- **RP-02 Audience-Specific Framing** — recruiter scan and hiring-manager read get different openings.
- **ST-46 Assertion-Evidence Structure** — angle first, proof second.
- **CM-02 Constraint Specification** — word limit, banned openers, one-gap rule.
- **QA-01 Self-Verification** — every clause traced back to the résumé.

## Related Prompts

- `domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md` — supplies the angle and the gap decision.
- `domain-personal-development/job-search/jobsearch_resume_evidence_rewriter.md` — the source of every proof point.
- `domain-personal-development/career-transformation/career_positioning_statement.md` — the one-line positioning the angle can draw on.
