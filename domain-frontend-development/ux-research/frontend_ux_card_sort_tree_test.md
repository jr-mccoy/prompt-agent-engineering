---
title: "Card Sort and Tree Test — Generate an Information Architecture from Users, Then Test Whether They Can Find Things in It"
category: frontend-development/ux-research
description: "Plan, run, and analyse the two information-architecture methods as a pair: an open or closed card sort to learn how users group and name content, and a tree test on a text-only hierarchy to measure whether they can find specific items — with card selection, task wording, sample sizes, the analyses to run (similarity matrix, success, directness, first click), and a revised tree — distinct from the site-architecture skill, which designs sitemaps and URLs from business needs rather than from user data."
techniques:
  - CM-03
  - ST-02
  - DS-02
  - RT-06
  - QA-04
difficulty: intermediate
tags:
  - ux-research
  - information-architecture
  - card-sorting
  - tree-testing
  - navigation
  - findability
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/site-architecture/SKILL.md
  - domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
---

# Card Sort and Tree Test

**Objective:** Ground a navigation structure in how users actually group and
look for content — generate candidate groupings with a card sort, then prove
or disprove findability with a tree test before any visual design exists.

**When to Use:**
- Navigation is being created or reorganised and the team disagrees on labels.
- Support tickets or search logs show people cannot find things that exist.
- A site or app is merging two content sets with different vocabularies.

**Not this prompt if:**
- You need a sitemap, URL scheme, or internal-linking plan designed from
  business and SEO needs → `domain-agentic-resources/skills/marketing/site-architecture/`.
  Use that skill to draft the tree, and this prompt to test it.
- The problem is layout, visual hierarchy, or interaction, not labels and
  grouping → `frontend_ux_usability_test_plan.md`.
- You only need expert judgement without users → `frontend_ux_heuristic_evaluation.md`.

## Inputs

1. **Content inventory**: the items that navigation must hold (pages, features,
   settings), with current labels.
2. **Current or proposed tree**, if one exists.
3. **Evidence of findability problems**: top search queries, ticket themes.
4. **Audience segments** whose mental models may differ.
5. **Tooling** (a card-sort/tree-test platform or paper) and recruiting budget.

## Method

1. **Choose which method(s) and state why (CM-03).**
   | Situation | Method |
   |---|---|
   | No structure yet; vocabulary unknown | Open card sort (users create and name groups) |
   | Categories fixed; placement uncertain | Closed card sort |
   | A tree exists; is it findable? | Tree test |
   | Redesign | Open sort → draft tree → tree test (old vs new) |
2. **Select cards (ST-02).** 30–60 cards; every card a real item written in
   plain words; remove cards that share a keyword with a likely group name
   (a card called "Billing settings" will be grouped by the word "settings").
   Include items that are known to be hard.
3. **Write tree-test tasks.** 8–10 tasks per participant, each a scenario
   with a single correct destination (or a declared set of acceptable ones).
   Never use the label of the target node in the task.
4. **Size the sample (DS-02).** Card sorts typically stabilise around 15–30
   participants per segment; tree tests usually use 50+ per tree to report
   success rates with a usable margin. State the margin you will report.
5. **Analyse the card sort.** Similarity matrix (how often pairs were grouped),
   dendrogram or cluster view, frequent group labels, and the cards with no
   stable home (these are the IA's real problems).
6. **Analyse the tree test (RT-06).** Per task: success rate, directness
   (success without backtracking), first-click correctness, and time. Cross the
   two methods: a card with no stable home in the sort that also fails in the
   tree test is a label or placement problem, not a user problem.
7. **Revise and re-test.** Propose the revised tree with each change traced to
   evidence; state which tasks must be re-run.
8. **State uncertainty (QA-04).** Report margins, segment differences, and what
   a text-only tree cannot tell you (visual prominence, search behaviour).

## Output Format

```
# IA study — [product/section]
Method(s) and reason: [...]

## Card sort plan
Type · n cards · participants/segment · card list (with removed-keyword notes)

## Tree test plan
Tree version(s) · tasks (scenario → correct node(s)) · participants

## Card sort results
Stable groups (with top user labels) · cards with no stable home

## Tree test results
| Task | Correct node | Success | Directness | First click correct | Notes |

## Cross-analysis
| Item | Card-sort signal | Tree-test signal | Diagnosis |

## Revised tree (changes traced to evidence)
## Uncertainty and what to re-test
```

## Verification

- [ ] No card and no task contains the label of a candidate group or target node.
- [ ] Every tree-test task has a declared correct node (or set).
- [ ] Success is reported with n, not only as a percentage.
- [ ] Every change in the revised tree cites a sort or test result.
- [ ] Items with no stable home are listed, not averaged away.

## False-Positive Prevention

1. **A similarity matrix is not a navigation design.** Users grouping cards
   together shows association, not the best labels or depth.
2. **Keyword matching fakes agreement.** Cards that share a word with a group
   cluster by string matching, not meaning; fix the cards before trusting results.
3. **Low directness with high success is still a finding.** Users got there by
   wandering; label clarity is the likely cause.
4. **Tree-test success does not mean the live navigation works.** Visual
   design, search, and page content are absent in a tree test.
5. **Do not merge segments whose models differ.** If admins and end users sort
   differently, one averaged tree serves neither; report both.
6. **Open-sort labels are raw material.** Users' group names are vocabulary
   evidence, not final labels to copy verbatim.

## Example Output

```
# IA study — Help centre (B2B analytics tool)
Method: open card sort → draft tree → tree test old vs new. Ticket volume shows
"where do I export data?" as the #2 question.

## Card sort plan
Open · 42 cards · 20 admins, 20 analysts. Removed "Export settings" → "Download
data as CSV" (shared keyword with a likely "Settings" group).

## Tree test plan
Trees A (current) and B (draft). 9 tasks, e.g. "Your manager wants last month's
numbers in a spreadsheet" → correct: Data › Export › CSV download. 60 per tree.

## Card sort results
Stable groups: Connecting data (labels: "Integrations", "Sources"), Building
reports, Sharing & access, Billing. No stable home: "Download data as CSV"
(split across Reports 45%, Sharing 35%), "Scheduled emails".

## Tree test results
| Task | Correct node | Success A | Success B | Directness B | First click B |
|---|---|---|---|---|---|
| Export to spreadsheet | Data › Export | 21/60 | 44/60 | 31/60 | 40/60 |
| Add a teammate | Sharing › Members | 50/60 | 52/60 | 47/60 | 51/60 |
| Scheduled email | Reports › Schedules | 18/60 | 27/60 | 15/60 | 22/60 |

## Cross-analysis
| Item | Sort | Tree | Diagnosis |
|---|---|---|---|
| CSV download | no stable home | B improves, low directness | Placement fixed; label still weak |
| Scheduled emails | no stable home | fails in A and B | Users see it as sharing, not reports |

## Revised tree
Move "Scheduled emails" to Sharing › Scheduled deliveries (sort: 35% grouped
with sharing; tree: 27/60 in Reports). Cross-link CSV download from Reports.

## Uncertainty
Margins at n=60 are roughly ±12 points; re-test the scheduled-email task on
tree C. A tree test cannot show whether the export button is visible on the page.
```

## Techniques Used

- **CM-03 Scope Definition** — choosing open sort, closed sort, or tree test for the question.
- **ST-02 Structured Sequential Instructions** — card selection → tasks → analysis → revision.
- **DS-02 Metric Specification** — success, directness, first click, sample per method.
- **RT-06 Correlation and Cross-Analysis** — sort signal crossed with tree-test signal.
- **QA-04 Uncertainty Acknowledgment** — margins and what a text-only tree cannot show.

## Related Prompts

- `domain-agentic-resources/skills/marketing/site-architecture/SKILL.md` — sitemap and URL design.
- `frontend_ux_usability_test_plan.md` — task-based testing of the rendered interface.
- `frontend_ux_usability_findings_severity_log.md` — rating the problems you confirm.
