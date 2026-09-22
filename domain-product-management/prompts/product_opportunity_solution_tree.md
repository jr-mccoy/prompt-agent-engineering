---
title: "Opportunity Solution Tree — Outcome to Opportunities to Solutions, With the Tree Pruned"
category: product-management/prompts
description: "Build an opportunity solution tree from a single product outcome: opportunities expressed as customer needs rather than feature requests, siblings checked for mutual exclusivity, solutions generated only for a chosen opportunity, and explicit pruning with recorded reasons. Refuses trees whose opportunities are disguised solutions and trees that branch everywhere at once."
techniques:
  - ST-02
  - CM-03
  - RT-05
  - NE-09
  - OC-03
difficulty: intermediate
tags:
  - product-discovery
  - opportunity-mapping
  - outcome-driven
  - continuous-discovery
  - prioritization
updated: "2026-09-22"
related_prompts:
  - domain-product-management/prompts/product_north_star_metric_definition.md
  - domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md
  - domain-product-management/prompts/product_create_prd.md
---

# Opportunity Solution Tree

**Objective:** Build the structure that connects **one** product outcome to the customer
needs that could move it, and only then to solutions — with sibling opportunities checked
for overlap, exactly one branch chosen for solution work, and every pruned branch
recorded with its reason. The prompt refuses trees whose "opportunities" are feature
requests in disguise, and trees that grow solutions under every branch at once.

**When to Use:**
- You have a target outcome and a backlog of feature requests, and no way to relate them.
- Discovery is producing interview notes that never become decisions.
- Stakeholders each have a pet feature and there is no shared structure for adjudicating.
- You need to show *why* the thing you are building is the thing to build.

**When NOT to use:**
- You need a name collision resolved: `domain-presentations/board-decks/boarddeck_opportunity_solution_tree.md`
  is an **image-generation** prompt that renders a tree diagram for a slide. It draws the
  picture; this one does the thinking.
- You need to run the customer interviews — that is
  `../../domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md`.
  This prompt consumes their output.
- You need to write the spec for a chosen solution — that is `product_create_prd.md`.
- You need to sequence agreed work — that is `product_planning_coding_roadmap.md`.
- You need to choose between prioritisation frameworks — that is
  `../../domain-decision-making/decisioning_prioritization_framework_selector.md`.

---

## Context Gathering

1. **The outcome**
   - "What single outcome are you trying to move? What is its current value?"
   - "Who owns that number, and where is it measured?"
   - "Is it a product outcome, or a business outcome one step removed?"

2. **The evidence base**
   - "What customer research do you have — interviews, tickets, session recordings,
     survey text?"
   - "How many customers, from which segments, how recently?"
   - "Which needs came from customers unprompted, and which were asked about?"

3. **The existing demands**
   - "What features are people asking for, and who is asking?"
   - "What is already committed that you cannot unwind?"

If the outcome is a business outcome — revenue, retention as a lagging aggregate — push
one step down to the product outcome the team can actually influence. A tree rooted in
"increase ARR" branches into marketing, pricing and sales, and the product team cannot
act on most of it.

If there is no customer evidence, say so plainly in the output. A tree built from
internal opinion is a map of what the team believes, which is worth drawing and must be
labelled as such.

---

## Method

### Step 1 — One outcome at the root

Exactly one, measurable, with a current value and a target. Two outcomes means two
trees; sharing a root between them produces opportunities that serve one and harm the
other with no way to see it.

### Step 2 — Generate opportunities as needs, not solutions

This is the step that decides whether the tree is useful. An opportunity is a customer
**need, pain, or desire** — something true about the customer independent of anything
you might build.

| Refused (solution in disguise) | Rewritten as an opportunity |
|---|---|
| "Add bulk export" | "I can't get my data into the format my finance team requires" |
| "Improve onboarding" | "I set the product up wrong and only found out three weeks later" |
| "Build an API" | "I have to re-enter the same data in two systems every week" |
| "Faster search" | "I know the record exists and I can't find it while the customer is on the phone" |
| "Better mobile app" | Not an opportunity — no need is stated. Go back to the evidence |

The test: does the sentence describe something the customer experiences, phrased so that
**several different solutions** could address it? If only one solution fits, it is a
solution.

Each opportunity carries its evidence: how many customers, which segment, verbatim
where available. An opportunity with no evidence is a hypothesis and is labelled one.

### Step 3 — Structure the tree, and check the siblings

Group opportunities into a hierarchy — broad needs above, specific instances below.
Then run the two structural checks that make a tree trustworthy:

- **Mutual exclusivity of siblings.** Two siblings describing the same need under
  different words will split the evidence and make both look smaller. Merge them.
- **Collective coverage at each level.** Do the children of a node account for the
  parent? If a large slice of the parent need has no child, there is unexamined
  territory — which is frequently where the best opportunity is.

### Step 4 — Size each opportunity on three axes, and do not aggregate them

For each leaf opportunity:

| Axis | Question |
|---|---|
| **Prevalence** | How many customers, in which segments, have this need? |
| **Severity** | How much does it cost them? What are they doing instead? |
| **Outcome leverage** | If this need were fully met, how would the root outcome move — and by what mechanism? |

Do **not** collapse these into a score. An opportunity affecting a few customers
severely and an opportunity mildly annoying everyone are different bets, and a single
number hides which one you are making. Scoring belongs in
`../../domain-decision-making/decisioning_prioritization_framework_selector.md` if you
want it; the tree's job is to keep the shape visible.

The outcome-leverage question is the one that most often kills a popular opportunity:
a widely-felt pain whose resolution does not move the root outcome is a support
problem, not this quarter's product work.

### Step 5 — Choose one opportunity, and prune out loud

Select **one** opportunity to take into solution space. This is the discipline the
structure exists to enforce: a tree with solutions growing under every branch is a
backlog with extra diagram.

Record the pruning:

| Pruned | Reason | Revisit when |
|---|---|---|

"Revisit when" is what makes pruning acceptable to the person whose branch was cut. An
opportunity pruned because the segment is too small today has a stated condition under
which it returns.

### Step 6 — Generate solutions only for the chosen branch

Three or more, genuinely different in approach rather than three variations of one
design. For each: what it assumes, and the smallest test that would falsify the riskiest
assumption.

Then stop. The tree's job is done when one opportunity has candidate solutions and a
test for each. Specification is `product_create_prd.md`.

---

## Output Format

```markdown
## Opportunity solution tree — [product area]

### Outcome (root)
**[Outcome]** — current [value], target [value] by [date]
Owned by [role] · measured in [system]
*Product outcome, not a business outcome one step removed:* [confirm]

### Evidence base
[n] interviews across [segments], [date range] · [n] tickets · [other]
**Opportunities with no customer evidence are marked HYPOTHESIS.**

### Tree
```
[Outcome]
├── [Opportunity — a need, in the customer's terms]
│   ├── [Sub-opportunity]  ev: 7/12 enterprise
│   └── [Sub-opportunity]  ev: 2/12  HYPOTHESIS
└── [Opportunity]
    └── [Sub-opportunity]
```

### Structural checks
- Siblings mutually exclusive: [pass / merged X and Y]
- Children cover the parent: [pass / unexamined territory: ...]
- No opportunity is a solution in disguise: [pass / rewritten: ...]

### Sizing
| Opportunity | Prevalence | Severity | Outcome leverage (and mechanism) |
|---|---|---|---|
*Not aggregated into a score, deliberately.*

### Chosen
**[Opportunity]** — because [reason referencing the three axes]

### Pruned
| Pruned | Reason | Revisit when |
|---|---|---|

### Solutions for the chosen opportunity
| Solution | Approach | Riskiest assumption | Smallest test |
|---|---|---|---|
```

---

## Verification

- [ ] Exactly one outcome at the root, measurable, with current value and target
- [ ] The root is a product outcome the team can influence
- [ ] Every opportunity is a customer need that several solutions could address
- [ ] No opportunity names a feature
- [ ] Every opportunity carries evidence, or is marked HYPOTHESIS
- [ ] Sibling exclusivity and parent coverage checks are run and recorded
- [ ] Three sizing axes recorded separately, not aggregated
- [ ] Outcome leverage names a mechanism, not just a direction
- [ ] Exactly one opportunity chosen for solution work
- [ ] Every pruned branch has a reason and a revisit condition
- [ ] Solutions differ in approach, each with a riskiest assumption and a test

**False-positive prevention.** The dominant failure is a tree of solutions wearing
opportunity labels. It looks like discovery and is a backlog, because every node admits
exactly one answer — the one the author already wanted. Apply the several-solutions test
to every node, and expect to rewrite most of them the first time.

The second failure is branching everywhere. A tree with solutions under all six
opportunities has made no decision, and the diagram's apparent thoroughness disguises
that. One branch, and the pruning written down.

The third is aggregating the sizing axes. A composite score makes an opportunity
affecting eleven customers severely look identical to one mildly affecting a hundred,
and those are different bets with different risks. Keep the three numbers visible.

The fourth is an outcome-leverage claim with no mechanism. "This would improve
retention" is a hope; "these users churn in month two citing setup errors, and 7 of 12
interviewed described the same wrong-configuration path" is a mechanism. Where the
mechanism cannot be stated, the leverage is unknown and should say so.

---

## Related

- `product_north_star_metric_definition.md` — defines the outcome at the root
- `../../domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md` — produces the evidence
- `product_create_prd.md` — specifies the chosen solution
- `product_planning_coding_roadmap.md` — sequences the work after the choice
- `../../domain-decision-making/decisioning_prioritization_framework_selector.md` — if you want a scoring framework
