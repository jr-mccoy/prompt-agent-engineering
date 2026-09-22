# Stage 7 — Close-out and Remediation Plan

*An audit that ends at findings has sold a diagnosis and no treatment. A
remediation plan that the client cannot run without you has sold a dependency.*

**Objective:** Hand over a remediation plan the client's own team can execute,
sequenced by what it costs to leave alone, and close the engagement with the
handback proven and the limits stated.

**When to Use:** After Gate C passes.

**When NOT to use:** To scope the next engagement. Write the plan the client
can run; if some of it needs you, say which parts and why, separately.

## Method

1. **Sequence the findings by cost of inaction**, not by ease of fix:
   1. blocking security findings — a credential in an artifact is today's work;
   2. contested membership — the scope disagreement outlasts every other item;
   3. exact clusters — a decision, then a delete;
   4. confirmed candidate clusters — a decision each, in similarity order;
   5. structural findings — batched by check, not by artifact.
2. **Name an owner and a check for each item.** "Fix the metadata" is not a
   plan; "run `observed_score.py` over `skills/` and clear `cat1_metadata`
   findings" is, because it has a stopping condition.
3. **Hand over the tooling, not just the output.** The client has a registry;
   show them `pae search` and `pae route` against their own corpus, and where
   `config/audit.json` lives so they can re-run the audit themselves.
4. **Write the re-audit trigger.** What change to the corpus should prompt
   running this again, and how they will know.
5. **Close the loop on Stage 0's disputes.** Anything unresolved goes into the
   close-out explicitly, not into a footnote.
6. **Record what the engagement did not cover**, in the same words as the
   report's limitations. A client who later believes content was reviewed will
   be right to be annoyed.

## Remediation that this kit deliberately cannot do for them

- **Choosing a canonical.** Every cluster's canonical is `null` by design. The
  organisation decides which artifact it stands behind.
- **Judging content.** 46 of 100 rubric points are human work, and
  `meta/adr/0041-author-reviewer-separation.md` says the author should not be
  the one doing it.
- **Resolving licensing.** The registry says `unresolved` because that is the
  truth after this audit.

Say all three out loud at close-out. They are the boundary of the engagement,
and a boundary stated at the end reads as an excuse.

## Output

- `audit/remediation.md` — sequenced, owned, each item with a stopping check.
- The close-out note: what was covered, what was not, what is unresolved.
- A short demo transcript of the client running the Engine on their own corpus.

## Verification

- [ ] Every remediation item names an owner and a check that ends it.
- [ ] Blocking security findings are first, and dated.
- [ ] The client has run `pae search` on their own corpus themselves.
- [ ] Stage 0's disputed items appear, unresolved and visible.
- [ ] The close-out repeats the report's limitations rather than softening them.

## False-Positive Prevention

1. **Do not sequence by ease.** Clearing forty missing sections looks like
   progress and retires no risk; the credential does.
2. **Do not promise a number.** "This will cut your library by a third" is a
   claim Gate B would block in the report and should not survive in a plan.
3. **A remediation plan only you can run is a finding about the plan.** If a
   step needs the kit, say so, and say what it costs.
4. **Do not treat an unresolved dispute as closed by shipping.** It is the item
   most likely to come back.

## Related

- `stage-5-report-and-claim-safety.md` for how any of this may be phrased.
- `client-services-studio/prompts/stage-9-closeout-case-study-and-referral.md`
  for the commercial close-out — margin post-calc, case study, referral — which
  this stage deliberately does not duplicate.
