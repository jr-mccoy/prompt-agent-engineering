# Stage 4 — Governance Findings

*Every finding is a fact with a location. Anything without one is an opinion,
and opinions go in the recommendations section clearly labelled as such.*

**Objective:** Turn three machine outputs — the inventory partition, the
clusters, the scores — into a ranked findings list the client can act on,
without adding a single claim the evidence does not carry.

**When to Use:** After Stages 1–3, before any report is drafted.

**When NOT to use:** As the report. This is the evidence table the report is
written from.

## Method

1. **Collate.** One row per finding: what, where (path and line where
   available), which stage produced it, and the evidence field that supports it.
2. **Classify by severity, using observable criteria only:**

   | Severity | Criterion |
   |---|---|
   | blocking | a credential, an absolute user path, or a contact detail in an artifact |
   | structural | a rubric check that failed, with its location |
   | duplication | an exact cluster, or a candidate the owner confirmed |
   | membership | an exclusion the owner disputed, or a contested root |

3. **Rank by what it costs to leave alone**, not by count. One credential in
   one skill outranks forty missing "Related" sections.
4. **Attribute every row.** A finding whose evidence you cannot point at gets
   deleted, not softened.
5. **Separate findings from recommendations.** A finding is observed. A
   recommendation is your judgement, and the report must not blur them.
6. **State what was not examined.** Content quality, correctness, security of
   anything the artifacts *do*, and the 46 unobservable rubric points.

## Governance questions worth asking, answered from the evidence

- Does anyone own this corpus? (Membership disputes tell you.)
- Is there a review step? (`review_status: unknown` across the board says no
  recorded one — say that, not "there is no review".)
- Do duplicates indicate two teams solving the same problem? (Ask; do not
  infer from the clusters.)
- Are credentials being pasted into artifacts? (Blocking findings say yes,
  with locations.)

## Output

`audit/findings.md` — a ranked table, plus:

- a "what this audit did not examine" section;
- a separate, labelled recommendations section;
- the disputed items from Stage 0, unresolved and visible.

## Verification

- [ ] Every finding names a path, and a line where one exists.
- [ ] Every finding names the stage and evidence field that produced it.
- [ ] Findings and recommendations are in separate sections.
- [ ] "What was not examined" is written before the recommendations, not after.
- [ ] No finding asserts a tier, a copy relationship, or a licence.

## False-Positive Prevention

1. **Count is not severity.** A long tail of missing sections reads as a crisis
   in a bar chart and is usually the cheapest thing in the report.
2. **Absence of a record is not absence of the practice.** `review_status:
   unknown` means nothing was recorded, not that nobody reviews.
3. **A disputed exclusion is a finding, not a config bug.** Resolve it with the
   owner or ship it as unresolved; do not silently pick a side.
4. **Do not infer intent from structure.** Two similar prompts are two similar
   prompts. Why they exist is a question for a person.

## Related

- Next: `stage-5-report-and-claim-safety.md`, which governs how any of this may
  be phrased.
