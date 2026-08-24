---
title: "Discipleship Material Evaluation — Criterion Review Without Fabricated Claims"
category: discipleship/curriculum-architecture
description: "Evaluate supplied discipleship or formation material against stated criteria — fit, theological transparency, practice formation, accessibility, facilitator demand — with every product, author, availability, and reception claim marked verify-required rather than asserted from memory."
techniques:
  - ST-02
  - CM-02
  - OC-03
  - QA-04
  - QA-05
difficulty: intermediate
tags:
  - discipleship
  - curriculum-architecture
  - material-evaluation
  - resource-selection
  - anti-fabrication
updated: "2026-08-04"
related_prompts:
  - domain-discipleship/curriculum-architecture/discipleship_curriculum_balance_audit.md
  - domain-discipleship/curriculum-architecture/discipleship_curriculum_architecture.md
  - domain-discipleship/learner-pathways/discipleship_life_constraints_adaptation.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md
  - domain-biblical-studies/theology-research/biblical_commentary_evaluation.md
---

# Discipleship Material Evaluation

**Objective:** Evaluate discipleship or formation material the user supplies against criteria they
choose — fit to participant, theological transparency, practice formation, accessibility, and
facilitator demand — producing a decision-ready comparison in which every claim about a product, its
author, its content, its price, its availability, or its reception is either evidenced from the
supplied material or explicitly marked verify-required.

> **STRONG-GUARD prompt.** Evaluating published material is the highest-fabrication-risk task in this
> domain. Language models routinely assert page counts, session counts, prices, author credentials,
> denominational affiliation, sales figures, review consensus, translation availability, and content
> summaries for books and curricula they have not been shown — confidently and wrongly. Here, **every
> product-specific claim is verify-required.** The user supplies the material or a description of it;
> the model evaluates *what it was given* against *criteria the user states*, and flags every fact it
> cannot see. It never recommends a resource it has not been shown.

> **Boundary guardrail.** This evaluates material, not ministries, authors, or traditions. It does not
> rule on whether a resource is theologically sound in an absolute sense — it reports what positions
> the material takes, which streams hold them, and whether the material is transparent about them.

**When to use:** You are deciding whether to adopt, keep, or replace a discipleship resource, and you
have the material or a substantive description of it in hand.

**When NOT to use:**
- You are auditing a curriculum you already run — use `discipleship_curriculum_balance_audit.md`.
- You are evaluating *Bible-study* curriculum for a church teaching program — use
  `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md`.
- You are evaluating commentaries or academic sources — use
  `domain-biblical-studies/theology-research/biblical_commentary_evaluation.md`.
- You want a resource *recommended* to you. This prompt cannot do that and will say so.

**Audience:** Discipleship pastors, program leads, and mentors choosing material.

---

## Inputs / Context

**Required:**

1. **The material.** Supplied in a `<material>` block: full text, sample sessions, table of contents,
   or a detailed description. State which. The evaluation is bounded by what is supplied.
2. **Your participant.** Who will use it — starting point, reading level, available time, language,
   and delivery context.
3. **Your criteria.** What matters for this decision, ranked or weighted. If the user has none, propose
   the five default criteria below and get confirmation before evaluating.

**Optional:**

4. **Declared tradition (optional).** If supplied, the evaluation reports fit with that stream's
   commitments — while still surfacing where the material takes contested positions, so the user sees
   what they are adopting.
5. **Comparators.** Other materials under consideration, each supplied in its own block. Materials not
   supplied are not compared.
6. **Constraints.** Budget, licensing needs, facilitator experience available, accessibility
   requirements.

**If any required input is missing:** Ask clarifying questions before proceeding. If no material is
supplied, say plainly that no evaluation is possible and offer to build a criteria framework the user
can apply themselves.

---

## Constraints

### Must

- Evaluate **only what is supplied.** Every judgement cites the section of `<material>` it rests on.
- Mark **every product-specific fact** the supplied material does not directly show —
  price, session count, page count, formats, translations, licensing, author credentials,
  denominational affiliation, publication date, reception, sales, endorsements — as
  `[VERIFY: confirm with the publisher / from the material itself]`.
- State the **bound of the evaluation** at the top: what form the material took and what that form
  cannot reveal.
- Report the **positions the material takes** on contested practices, the streams holding them, and
  whether the material is transparent about the disagreement.
- Assess **facilitator demand**: what a leader must know, be, or prepare in order to use this well.
- Assess **accessibility**: reading level, cultural assumptions, time assumptions, assumed prior
  knowledge, assumed private space, assumed literacy.
- Give a **decision-forcing verdict** from the fixed list in the Output Format, including an
  insufficiency branch.

### Must Not

- Assert any fact about the material that is not visible in `<material>`, however plausible.
- Recommend, praise, or criticize a resource that has not been supplied — including as an alternative
  or comparator.
- Invent or summarize reviews, endorsements, adoption figures, author biographies, or reputational
  claims.
- Quote Scripture text from memory when checking the material's references; confirm addresses and mark
  wording verify-required.
- Rule on whether the material is theologically correct. Report positions and transparency; leave
  adjudication to the user and their tradition.
- Assign a numeric quality score to the material, or rank materials by a computed total.
- Emit "it depends" as a verdict.

### Tradition-neutral stance (Must / Must Not)

- **Must:** report the material's tradition-specific commitments plainly and attribute them to
  identifiable streams; where a declared tradition exists, report fit with it while keeping the
  material's contested positions visible.
- **Must Not:** treat a material's tradition as a defect or a merit in itself, or evaluate it against
  an unstated confessional baseline.

---

## Instructions

### Step 1 — Bound the evaluation

State exactly what was supplied and what that form cannot show. A table of contents cannot reveal tone,
practice formation, or Scripture handling; say so before evaluating.

### Step 2 — Confirm the criteria

Restate the user's criteria and weights. If none were given, propose these five defaults and confirm:
fit to participant · theological transparency · practice formation · accessibility · facilitator
demand.

### Step 3 — Evaluate against each criterion

For each criterion, give the finding, the evidence from `<material>`, and a plain rating —
**strong / adequate / weak / cannot assess**. No numbers.

### Step 4 — Extract the position register

List every contested practice the material takes a position on. For each: the position, the streams,
the alternatives, and whether the material tells the reader it is contested.

### Step 5 — Build the verify-required register

List every product-specific fact a decision depends on that the material does not show, each marked
`[VERIFY]` with where the user should confirm it. This register is a deliverable, not a footnote.

### Step 6 — Assess facilitator and accessibility demand

State what a facilitator must bring, and what participant circumstances this material will not serve —
low literacy, no private space, limited time, no transport, second-language, disability, or trauma
history that specific modules could touch.

### Step 7 — Issue the verdict

Apply the verdict rule mechanically. If the supplied material cannot support a verdict, say
INSUFFICIENT and name the single cheapest thing that would unblock it.

---

## Output Format

Produce exactly this structure. Use `[..]` where a value depends on user input.

```
# Material Evaluation — [material name as supplied]

## Bound of This Evaluation
- Material supplied as: [full text | sample sessions | table of contents | description]
- What this form cannot reveal: [..]
- Declared tradition: [declared tradition | none]

## Criteria and Weights
| Criterion | Weight | Why it matters here |
|---|---|---|

## Findings by Criterion
| Criterion | Rating | Finding | Evidence in <material> |
|---|---|---|---|
| Fit to participant | strong/adequate/weak/cannot assess | [..] | [section] |
| Theological transparency | [..] | [..] | [..] |
| Practice formation | [..] | [..] | [..] |
| Accessibility | [..] | [..] | [..] |
| Facilitator demand | [..] | [..] | [..] |

## Position Register
| Contested practice | Position taken | Streams holding it | Material flags it as contested? |
|---|---|---|---|

## Verify-Required Register
| Fact the decision depends on | Status | Where to confirm |
|---|---|---|
| [e.g. session count] | [VERIFY] | [publisher / the material itself] |

## Who This Will Not Serve
| Participant circumstance | Why | Possible adaptation |
|---|---|---|

## Verdict
**[ADOPT | ADOPT WITH ADAPTATION | DO NOT ADOPT | INSUFFICIENT — pending [item]]**

Rationale: [..]
If INSUFFICIENT — cheapest unblocking step: [..]
```

**Verdict rule (mechanical, no other verdict may be emitted):**
- **ADOPT** iff every weighted criterion rates adequate or strong, and no unflagged contested position
  conflicts with a stated commitment.
- **ADOPT WITH ADAPTATION** iff at least one criterion rates weak but a named, specific adaptation
  addresses it, and no such conflict exists.
- **DO NOT ADOPT** iff a top-weighted criterion rates weak with no viable adaptation, or an unflagged
  contested position conflicts with a stated commitment.
- **INSUFFICIENT — pending [item]** iff any top-weighted criterion rates "cannot assess." Name the
  single cheapest datum that unblocks the verdict.
- "It depends" is banned.

---

## Verification

- [ ] Every finding cites a section of the supplied `<material>`.
- [ ] Every product-specific fact not visible in the material is marked `[VERIFY]` with a confirmation
      source.
- [ ] No resource that was not supplied is named, recommended, or compared.
- [ ] No numeric quality score or computed ranking appears.
- [ ] The verdict is one of the four permitted values and follows the rule mechanically.
- [ ] The bound of the evaluation is stated before any finding.

---

## False-Positive Prevention

❌ **DON'T:**
- Fill in what a well-known resource "generally contains." Recognition is not evidence, and confident
  summaries of unseen material are this prompt's signature failure.
- Assert session counts, prices, formats, or availability. These change constantly and are
  publisher-specific.
- Describe an author's tradition, credentials, or reputation. Even when widely believed, it is not in
  the material.
- Summarize what reviewers or other churches say about it. That is fabrication with a citation shape.
- Rate a material weak because it belongs to a tradition other than the user's. Report the position;
  let them decide.
- Force a verdict when the supplied material genuinely cannot support one. INSUFFICIENT is a real
  answer here.

✅ **DO:**
- Say "the supplied table of contents does not show whether practice is formed" and mark it cannot
  assess — that is a useful, honest finding.
- Put the verify-required register in front of the user as a task list. It is often the most valuable
  part of the output.
- Report the position register even for a material the user already loves; adopting a contested
  position knowingly is fine, adopting it unknowingly is not.
- Name the specific participant circumstances the material will fail, since these rarely appear in
  publisher descriptions.
- Give the cheapest unblocking datum when issuing INSUFFICIENT, so the user knows exactly what to go
  find.
- Offer to build a criteria framework when no material is supplied, rather than evaluating from memory.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** bound → criteria → findings → positions → verify
  register → demand → verdict, so the evaluation's limits are fixed before any judgement is made.
- **CM-02 (Constraint Specification):** the STRONG-GUARD Must Not block converts the fabrication risk
  into hard prohibitions — no unsupplied resource named, no reviews summarized, no credentials asserted.
- **OC-03 (Markdown Table Specification):** the verify-required register and position register are
  tables precisely so an unsupported claim has nowhere to hide in prose.
- **QA-04 (Uncertainty Acknowledgment):** "cannot assess" is a first-class rating and INSUFFICIENT a
  first-class verdict, so the prompt fails loudly rather than confidently.
- **QA-05 (Citation Requirements):** every finding cites its section of `<material>`, and every fact
  outside it is `[VERIFY]`-marked with a named confirmation source.

---

## Related Prompts

- [`discipleship_curriculum_balance_audit.md`](discipleship_curriculum_balance_audit.md) — audit
  material already in use rather than material under consideration
- [`discipleship_curriculum_architecture.md`](discipleship_curriculum_architecture.md) — build your own
  when nothing suitable exists
- [`../learner-pathways/discipleship_life_constraints_adaptation.md`](../learner-pathways/discipleship_life_constraints_adaptation.md) —
  adapt material for the circumstances it will not serve as written
- [`domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md`](../../domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md) —
  the Bible-study-curriculum counterpart
- [`domain-biblical-studies/theology-research/biblical_commentary_evaluation.md`](../../domain-biblical-studies/theology-research/biblical_commentary_evaluation.md) —
  evaluating commentaries and academic sources
