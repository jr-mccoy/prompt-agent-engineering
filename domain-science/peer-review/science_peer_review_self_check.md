---
title: "Peer Review Self-Check"
category: science/peer-review
description: "Audit your own draft peer review before submitting it: test whether each criticism is evidence-based and located, screen for bias, scope creep, conflict of interest, and tone, and confirm correct major/minor triage and reporting-standard coverage."
techniques:
  - ST-01
  - QA-01
  - QA-02
  - CM-02
  - RT-01
difficulty: advanced
tags:
  - peer-review
  - reviewer-bias
  - self-audit
  - scope-creep
  - conflict-of-interest
  - cope
  - constructive-critique
  - calibration
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_drafter.md
  - domain-science/peer-review/science_editorial_decision_drafter.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_threats_to_validity_walkthrough.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
---

# Peer Review Self-Check

**Objective:** Take a reviewer's own draft review and adversarially audit it before it is submitted. For each criticism, determine whether it rests on located manuscript evidence or on taste/preference; screen the review as a whole for scope creep, confirmation/prestige/disconfirmation bias, undisclosed conflict of interest, and hostile tone; and confirm that major-vs-minor triage, reporting-standard coverage, and Open-Science coverage are present. Output a per-criticism self-audit table with a keep/revise/drop verdict.

**When to use:** After drafting a peer review (e.g., with the Peer Review Drafter) and before sending it to the editor. Use whenever you want to catch the failure modes that make reviews unfair, unhelpful, or unethical.

**Required inputs:**
- **Discipline.** The field and subfield of the manuscript under review.
- **Study type.** Observational / experimental / RCT / computational / theoretical / systematic review / meta-analysis / qualitative / mixed-methods.
- **The draft review.** The reviewer's own comments-to-authors, confidential comments-to-editor, and recommendation.

**Optional inputs:**
- The manuscript text or the specific locations each criticism refers to (enables verifying that cited locations exist).
- Any conflict-of-interest disclosure already prepared `[user-supplied]`.
- The journal's review criteria and recommendation categories `[user-supplied]`.

**Constraints — Must:**
- Apply the COPE Ethical Guidelines for Peer Reviewers as the audit standard: objectivity, evidence-basis, confidentiality, declared conflicts, and constructive tone.
- Evaluate every individual criticism for evidentiary basis (manuscript location, reporting standard, or explicit reasoning) and classify it as evidence-based vs preference/taste.
- Test the review for scope creep (asking for a different paper rather than strengthening this one).
- Screen for reviewer biases by name: confirmation bias, disconfirmation/contrarian bias, prestige/halo bias, methodological-orthodoxy bias, and language/origin bias.
- Confirm major-vs-minor triage is correct and that confirmatory vs exploratory claims are handled appropriately.
- Confirm the draft checked the relevant EQUATOR reporting checklist and the TOP Open-Science dimensions (data/code/materials availability, preregistration adherence).
- Assess tone sentence-by-sentence where flagged and rewrite hostile phrasing into specific, actionable, neutral phrasing.

**Constraints — Must Not:**
- Do not invent citations, data, or manuscript facts; if a criticism asserts something about the manuscript that cannot be confirmed from supplied inputs, flag it as unverifiable rather than endorsing it.
- Do not introduce new substantive criticisms — the job is to audit the existing review, not to re-review the paper.
- Do not soften a genuinely fatal, evidence-based flaw to appear "nicer"; constructiveness is about tone and actionability, not about suppressing valid concerns.
- Do not retain promotional language in any rewritten text — ban "novel," "groundbreaking," "first-ever," and "gold standard."

**Instructions:**

1. **State context.** Record discipline and study type, and confirm the audit will treat COPE as the governing standard.
2. **Conflict-of-interest gate.** Check whether the review or its tone suggests a competing interest (collaboration, rivalry, financial, ideological). If any plausible COI exists and is undisclosed, flag it as a stop-and-disclose item before submission.
3. **Decompose the review into discrete criticisms.** List each comment-to-authors as a separate atomic criticism.
4. **Audit each criticism's evidentiary basis.** For each, identify whether it is anchored to a manuscript location, a reporting-standard item, or explicit reasoning — or whether it is preference/taste/"I'd have done it differently." Mark unverifiable assertions.
5. **Triage check.** Confirm each criticism is correctly placed as major (validity threat) or minor (degree), and that no preference was elevated to "major." Verify confirmatory vs exploratory framing is fair.
6. **Scope-creep check.** For each request, ask whether it strengthens the manuscript's own claims or demands a fundamentally different study; flag scope creep.
7. **Bias and tone screen.** Run the named-bias screen across the whole review, then scan for hostile, dismissive, or ad hominem phrasing; propose neutral, actionable rewrites for flagged sentences.
8. **Coverage check.** Confirm the draft addressed the relevant EQUATOR reporting checklist and the TOP Open-Science dimensions; note any missing coverage to add.
9. **Emit the self-audit table and verdict.** For each criticism output a keep/revise/drop decision, then give an overall go / revise-before-submitting verdict and a short list of required fixes.

**Output format (locked):**

```
## Audit Context
- Discipline: [...]
- Study type: [...]
- Governing standard: COPE Ethical Guidelines for Peer Reviewers

## Conflict-of-Interest Gate
[None apparent | Possible COI — describe + disclose-before-submitting]

## Per-Criticism Self-Audit
| # | Criticism (paraphrased) | Evidentiary basis (location/standard/reasoning) | Evidence-based or preference? | Major/Minor correct? | Scope creep? | Verdict (keep/revise/drop) |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |

## Bias and Tone Screen
- Confirmation bias: [finding]
- Disconfirmation/contrarian bias: [finding]
- Prestige/halo bias: [finding]
- Methodological-orthodoxy bias: [finding]
- Language/origin bias: [finding]
- Hostile/ad hominem phrasing → neutral rewrite:
  - "[flagged sentence]" → "[rewritten]"

## Coverage Check
- Reporting-standard (EQUATOR) addressed: [yes/no — which checklist; what to add]
- Open-Science (TOP) addressed: [data/code/materials/preregistration — gaps to add]

## Overall Verdict
[Ready to submit | Revise before submitting] — [required fixes, ordered]
```

**Reporting-standard alignment:** COPE Ethical Guidelines for Peer Reviewers (objectivity, confidentiality, COI, constructive conduct); ICMJE reviewer responsibilities; EQUATOR checklist matching the study type (CONSORT/STROBE/PRISMA/ARRIVE) for the coverage check; TOP guidelines for the Open-Science coverage check.

**Verification checklist (before delivering):**
- [ ] Discipline and study type are recorded up front.
- [ ] A COI gate was applied and either cleared or flagged for disclosure.
- [ ] Every criticism appears as a discrete row with its evidentiary basis evaluated.
- [ ] Each row classifies evidence-based vs preference and confirms major/minor triage.
- [ ] Scope creep is checked per request.
- [ ] All five named biases are screened, and hostile phrasing has neutral rewrites.
- [ ] Reporting-standard and Open-Science coverage gaps are identified.
- [ ] No new substantive criticisms were added; unverifiable claims are flagged, not endorsed; no banned promotional terms remain.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Politeness over rigor | "Drop" verdicts on valid fatal flaws to make the review gentler | Constructiveness governs tone/actionability only; never drop an evidence-based validity threat |
| Hidden preference passing audit | A taste comment with a plausible-sounding reason marked "evidence-based" | Require a concrete location or reporting-standard item, not just a rationale, to count as evidence-based |
| Re-reviewing instead of auditing | Adding fresh criticisms during the self-check | Restrict scope to the existing draft; route new substantive issues back to the drafter |
| Bias screen as box-ticking | Marking all biases "none" without testing asymmetric standards | For each bias, ask whether the review would read the same had origin/prestige/method been different |
| Missed undisclosed COI | Treating rivalry/collaboration tone as ordinary critique | Any plausible competing interest triggers a stop-and-disclose flag before submission |
