---
title: "School Counselor College Recommendation Letter — Sourced Anecdotes, Consented Context"
category: professional-writing/domain-specific
description: "Draft a high school counselor's college recommendation letter in which every strength is carried by a sourced anecdote, comparisons rest on school data rather than 'top 1%', sensitive context appears only as far as the student consented, and no sentence could be pasted into another student's letter. Distinct from a grant letter of support (science_letter_of_support_drafter) and from attorney-guided expert letters (legal_eb1_extraordinary_ability_petition)."
techniques:
  - ST-46
  - RT-05
  - CM-09
  - QA-18
difficulty: intermediate
tags:
  - counselor-recommendation
  - college-recommendation-letter
  - school-counselor
  - college-admissions
  - student-consent
  - write-a-letter-of-recommendation
updated: "2026-10-06"
related_prompts:
  - domain-science/grants-funding/science_letter_of_support_drafter.md
  - domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md
  - domain-professional-writing/writing/writing_unsourced_claim_disposition.md
---

# School Counselor College Recommendation Letter

**Objective:** Draft a 400–500 word counselor recommendation that an admissions reader can
trust: specific, sourced, consented, and impossible to mistake for another student's letter.

**When to Use:**
- Senior-year recommendation season, working from a student brag sheet, teacher notes,
  the transcript, and your own meeting notes.
- A student's record has a dip or a circumstance the reader should understand, and you
  need to give context without disclosing more than the student agreed to.
- Your draft has strong adjectives and few examples, or comparisons you cannot source.
- A large caseload means you know the student less well than a teacher does and need to
  say so honestly while still being useful.
- **Not this prompt if** you are writing a letter that commits resources to a grant
  proposal — use `domain-science/grants-funding/science_letter_of_support_drafter.md`,
  which audits commitments rather than character. Recommender letters for an immigration
  petition are attorney-directed; see `domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md`.
  A repository search found no counselor or college-application prompt in
  `domain-education-teaching/`.

**Audience:** An admissions reader with minutes per file, reading the letter beside the
transcript and the school profile. They need what the transcript cannot show (how the
student works, what context explains the numbers) and they discount praise without
evidence. The counselor signs the letter and is accountable for every statement in it.

## Inputs / Context

Paste source material inside named tags and refer to it by tag name:

1. **Student and programs** — name, intended programs or schools, any program-specific
   emphasis (engineering, nursing, arts).
2. **Your relationship** — years known, number of individual meetings, caseload size.
3. **Key strengths** — the stub's field: academic abilities and personal qualities you
   want to claim.
4. **Specific examples** in `<counselor_notes>`, `<teacher_notes>`, and `<brag_sheet>` —
   concrete moments, each with who observed it.
5. **Record** in `<transcript>` and `<school_profile>` — courses, grades, course-enrollment
   counts, whether the school ranks.
6. **Growth or challenges** — what happened and when.
7. **Consent record** in `<consent>` — for each sensitive item (disability or health,
   family circumstances, finances, immigration status, discipline), what the student
   agreed may be said, in what words.
8. **Draft** in `<draft_letter>` (optional).
9. **Form requirements** — the application platform's counselor form fields and any
   length guidance `[VERIFY: platform's current counselor recommendation instructions]`.

## Method

1. **Map each strength to evidence (ST-46, RT-05).** For every claim you want to make,
   name the anecdote that proves it and tag its source: `[observed]` by you,
   `[teacher: name]`, `[record]`, or `[student-reported]`. A strength with no anecdote is
   cut or merged; a `[student-reported]` item is attributed or corroborated, never told
   as if you witnessed it.
2. **Rebuild comparative claims from school data.** "Top 1%", "best I've seen", "one of
   the strongest" need a comparison group and a number. Replace them with what
   `<school_profile>` or enrollment counts support ("one of six seniors in a class of 412
   in this course"). If the school does not rank, say so rather than implying a rank.
3. **Apply the consent boundary (CM-09).** For each sensitive item, use only the words
   `<consent>` permits. No consent means it is absent from the letter, even if it would
   help. Discipline disclosure follows the school's policy and the form's questions
   `[VERIFY: school disclosure policy]`; this letter does not volunteer it.
4. **Place context where it explains the record.** Tie a circumstance to the specific
   grade or gap it explains, then show what followed. Context that explains nothing on
   the transcript is cut.
5. **Write in the stub's structure.** Introduction (relationship and how well you know
   the student); two or three strengths, each led by its anecdote; growth or context;
   closing endorsement that names what the program gains.
6. **Run the swap test before output (QA-18).** For each sentence, ask whether it could
   appear unchanged in another student's letter. If yes, replace it with a detail only
   this student has, or delete it. Then confirm every number traces to `<transcript>`,
   `<school_profile>`, or a note, and the word count is 400–500.

## Output Format

```
## Evidence ledger
| # | Claim in letter | Anecdote | Source tag | Status |

## Comparative claims
| Draft claim | Basis in school data | Used as |

## Consent check
| Sensitive item | Consent (words permitted) | In letter as |

## Letter  ([n] words)

## Swap-test log
| Draft sentence | Why generic | Replacement |

## Notes for the counselor
```

## Verification

- [ ] Every strength in the letter has an anecdote with a source tag.
- [ ] No `[student-reported]` item is narrated as the counselor's own observation.
- [ ] Every comparison names its group and number from school data; no "top X%" without one.
- [ ] Every sensitive item matches the wording in `<consent>`; unconsented items are absent.
- [ ] Context is tied to a specific grade or gap in `<transcript>`.
- [ ] No sentence survives the swap test unchanged.
- [ ] 400–500 words; form fields handled separately.

## False-Positive Prevention

1. **The polished invented anecdote.** Models fill gaps with plausible scenes ("she stayed
   after class to help a struggling classmate"). If it is not in a note, it did not happen
   for this letter's purposes, however true it sounds.
2. **Embellishment by one degree.** "Helped at the tutoring table" becoming "founded and
   ran a tutoring program serving dozens" turns a fact into a claim the student's other
   recommenders may contradict.
3. **"Top 1% of students I have worked with."** Counselors write it often and readers
   discount it; without a caseload count and a basis it is unsupportable, and from a
   school that does not rank it reads as inflation.
4. **Sensitive context that helps the case but was not consented.** A parent's illness,
   a 504 plan, or a financial hardship can make a record make sense, and disclosing it
   without the student's agreement is a breach of trust with consequences beyond this
   application.
5. **Generic praise that passes for warmth.** "Hardworking, kind, and a natural leader"
   is interchangeable across every letter in the stack; the swap test catches it.
6. **Teacher material relabelled as yours.** Quoting a teacher's lab story as something
   you watched overstates your knowledge; attribute it ("her physics teacher describes").
7. **Context with no transcript anchor.** A paragraph about hardship that does not explain
   a specific grade or gap reads as special pleading; anchor it or cut it.

## Example Output

Scenario: Dana Reyes, counselor at Lakeview High School (caseload 290), for Maya Torres,
applying to mechanical engineering programs. `<school_profile>`: class of 412; school does not
rank. `<transcript>`: AP Calculus BC (junior); dual-enrollment Multivariable Calculus at Lakeview
Community College (senior; enrollment report: 6 seniors); one grade below A-minus — B-minus in
AP Chemistry, fall of junior year; all A/A-minus since. `<teacher_notes>`: Mr. Abel (physics):
group truss failed at 18 kg; Maya redesigned the joints, second version held 41 kg; she handed
in an unrequested one-page failure analysis. `<counselor_notes>`: 7 individual meetings since
grade 9; she brought a spreadsheet comparing programs by co-op availability and first-year
design courses and asked which columns were missing. Librarian's sign-in sheets: Tuesday math
help table started January of junior year, average 9 students per session that spring, mostly
in courses Maya had completed; two classmates recruited to cover absences. `<brag_sheet>`: works
~20 h/week at the family restaurant since October of junior year. `<consent>`: may say
"significant family responsibilities, including about twenty hours a week of work in her
family's restaurant"; may NOT mention her father's injury; may NOT mention her 504 plan.
`<draft_letter>` contains "top 1% of students I have ever worked with", "a natural leader who
lights up every room", "Maya is hardworking and dedicated", "overcame her father's injury".

```
## Evidence ledger
| # | Claim in letter             | Anecdote                                  | Source tag          | Status |
| 1 | Seeks the hardest math      | BC as junior; multivariable via dual enr. | [record]            | Used |
| 2 | Learns from failure         | Truss 18 kg → 41 kg + failure write-up    | [teacher: Abel]     | Used, attributed |
| 3 | Plans systematically        | Program-comparison spreadsheet            | [observed]          | Used |
| 4 | Builds for others           | Tuesday help table, avg 9/session         | [record: sign-ins]  | Used |
| 5 | Manages a heavy load        | ~20 h/week work; grades A/A- since        | [student-reported] + [record] | Used per consent |
| 6 | "Natural leader"            | none beyond #4                            | —                   | Cut; #4 shows it |

## Comparative claims
| Draft claim                       | Basis in school data                  | Used as |
| Top 1% of students I've worked with | none (no ranking, no caseload basis) | "Six seniors in our class of 412 are taking that course." |

## Consent check
| Sensitive item    | Consent (words permitted)                          | In letter as |
| Work hours        | "significant family responsibilities… restaurant" | verbatim, ¶5 |
| Father's injury   | not permitted                                      | absent |
| 504 plan          | not permitted                                      | absent |

## Letter  (402 words)
I am writing in support of Maya Torres, who is applying to mechanical engineering programs. I
have been Maya's counselor since ninth grade and have met with her individually seven times; I
also draw on her teachers' observations, which I identify as theirs.

Maya has taken the most demanding mathematics sequence Lakeview offers and then gone beyond it.
After AP Calculus BC as a junior, she enrolled this year in Multivariable Calculus through dual
enrollment at Lakeview Community College. Six seniors in our class of 412 are taking that
course. Lakeview does not rank students, so I will let that number stand on its own.

What distinguishes Maya is what she does when something fails. Her physics teacher, Mr. Abel,
describes a bridge-building lab in which her group's truss collapsed at 18 kilograms. Maya
redesigned the joints, the second version held 41 kilograms, and she handed in a one-page
explanation of why the first design failed, which no one had asked for. I saw the same habit
in our college-planning meetings: she arrived at one with a spreadsheet comparing engineering
programs by co-op availability and first-year design courses, and asked me which columns she
was missing.

Maya also builds things for other people. In January of her junior year she started a Tuesday
math help table in the library. The librarian's sign-in sheets show an average of nine students
per session that spring, most of them in courses Maya had already finished. She recruited two
classmates to cover the table on days she could not be there, so it kept running.

Maya's record should be read with her circumstances in mind. Since October of her junior year
she has carried significant family responsibilities, including about twenty hours a week of
work in her family's restaurant. Her one grade below an A-minus, a B-minus in AP Chemistry that
fall, came in the first months of that schedule; every grade since has been an A or A-minus
while the hours continued. I offer that context not as an excuse but as evidence of how she
manages a heavy load.

I recommend Maya with enthusiasm. She chooses the hardest available work, she studies her own
failures until she understands them, and she has built something at Lakeview that outlasts her
own schedule. An engineering program will get a student who already treats a collapsed truss as
information. Please contact me if I can add anything.

## Swap-test log
| Draft sentence                                | Why generic                  | Replacement |
| "A natural leader who lights up every room"   | fits any student             | help-table paragraph (ledger #4) |
| "Maya is hardworking and dedicated"           | fits any student             | B-minus → A/A- under 20 h/week (ledger #5) |
| "Overcame her father's injury"                | unconsented (Consent check)  | consented wording only |

## Notes for the counselor
- Rating grids and checkboxes on the counselor form are separate from this letter; complete
  them from the same evidence [VERIFY: platform's current counselor form].
- Confirm Mr. Abel is comfortable being quoted, or paraphrase without his name.
- Ask Maya whether her own essay mentions the work hours, so the two documents agree.
```

## Techniques Used

- **ST-46 Assertion-Evidence Content Structure** — each strength is stated once and carried by its anecdote in the same paragraph.
- **RT-05 Evidence-Based Reasoning** — the evidence ledger gates every claim on a sourced example and every comparison on school data.
- **CM-09 Authority Boundary Specification** — the consent record sets the outer boundary of what the counselor may disclose, item by item.
- **QA-18 Domain-Specific Smell Tests** — the swap test removes sentences that could sit in any other student's letter.

## Related Prompts

- `domain-science/grants-funding/science_letter_of_support_drafter.md` — the commitment-auditing letter for grant applications.
- `domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md` — recommender letters inside an attorney-led immigration petition.
- `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` — deciding keep/soften/cut for claims you believe but cannot source.
