---
title: "Affinity Clustering — Group Many Ideas or Notes Bottom-Up into Named Themes"
category: ideation/sensemaking
description: "Take a pile of 30–200 raw ideas, sticky notes, or observations and cluster them bottom-up, without predefined categories: atomise the notes, group by felt similarity, name each cluster with a statement rather than a label, form super-groups, and keep the outliers visible. Produces a structured map of what the pile contains, not a ranking. Distinct from ideation_idea_convergence_dot_voting.md (which scores and shortlists) and domain-business-strategy/research/user_research_synthesis.md (which codes interview transcripts toward decisions)."
techniques:
  - DS-04
  - DS-37
  - RT-05
  - OC-03
  - QA-01
difficulty: beginner
tags:
  - ideation
  - affinity-diagram
  - clustering
  - kj-method
  - synthesis
  - workshop
  - sticky-note-pile
  - open-text-answers
  - messy-brainstorm
updated: "2026-09-24"
reasoning:
  styles: [inductive, convergent, synthesising]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, facilitator, researcher, strategist]
  mode: [converge]
related_prompts:
  - domain-ideation/ideation_idea_convergence_dot_voting.md
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-agentic-resources/skills/non-coding/creative/idea-divergence-convergence/SKILL.md
---

# Affinity Clustering — Group Many Ideas or Notes Bottom-Up into Named Themes

**Objective:** Turn an unstructured pile of ideas, workshop sticky notes, or observations into a map of themes that emerged from the material itself. The method descends from Jiro Kawakita's KJ method: categories are not decided in advance; notes are grouped by similarity first and the groups are named afterwards. The deliverable is structure — what is in the pile, how the parts relate, what is missing — so that a later convergence step can choose from coherent themes instead of from a hundred loose items.

---

## When to Use

- A divergence session produced 30–200 ideas and the list is too long to read as a whole.
- A workshop wall of sticky notes needs to be written up faithfully.
- Retro notes, open-text survey answers, or field observations need a first-pass structure.
- You suspect the team's existing categories are hiding what the material says.

**Distinct from:**
- `domain-ideation/ideation_idea_convergence_dot_voting.md` — ranks and shortlists. Affinity clustering does not rank; run it first when the list is large and repetitive, then vote on themes or on the best note per theme.
- `domain-business-strategy/research/user_research_synthesis.md` — codes 10–30 interview transcripts with quote IDs and ends in decisions. Use it for formal research synthesis; use this for idea piles and workshop output.
- `domain-agentic-resources/skills/non-coding/creative/idea-divergence-convergence/SKILL.md` — includes a short affinity step inside a full cycle. This prompt is the full method.

**When NOT to use:**
- Fewer than about fifteen items — just read them.
- You already have a validated taxonomy and only need to sort into it; that is classification, not affinity work.

---

## Inputs / Context

1. **The notes.** The raw items, one per line, with an ID if available.
2. **Source.** Where they came from (brainstorm, retro, survey) and the question that produced them.
3. **Purpose.** What the clusters will feed — voting, a roadmap, a report.
4. **Existing categories (optional).** Recorded only to compare against at the end, never used to seed clusters.

---

## Method

### Step 1 — Atomise
Split any note containing more than one idea into separate notes; merge exact duplicates and record the merge (duplicates are a signal, so keep the count). Give every note an ID.

### Step 2 — Group by similarity, not by category
Place notes together when they "feel like they belong", working note by note. Do not name groups yet. A note that fits nowhere starts its own group or stays alone.

### Step 3 — Split and merge
Split groups larger than about a fifth of all notes; merge groups of one or two into a neighbour only if the fit is genuine. Leftovers go to an **outliers** set — they are kept, not forced.

### Step 4 — Name each cluster with a statement
Write a header that says what the notes collectively claim or want: "People want to try the product before giving any data", not "Onboarding". A header that could only be a noun label means the group may not share a claim; re-examine it.

### Step 5 — Form super-groups
Group the named clusters into 3–6 higher-level themes, again with statement headers. Note relationships between themes (causes, conflicts with, depends on).

### Step 6 — Trace and count
For every cluster, list its note IDs and count. Confirm every note appears exactly once (in a cluster or in outliers).

### Step 7 — Read the map
State: largest clusters (with the caveat that size is not importance), surprising clusters, tensions between clusters, and what is conspicuously absent given the source question. Compare with any pre-existing categories supplied in the inputs.

---

## Output Format

```
# Affinity map — [source]

## Notes processed: [N raw] → [N atomic] ([N] duplicates merged)

## Super-group A: [statement]
### Cluster A1: [statement]  ([count])
- [ID] note
- ...
### Cluster A2: ...

## Super-group B: ...

## Outliers ([count])
- [ID] note — why it did not fit

## Relationships
| From | Relation | To |

## Reading the map
- Largest (size ≠ importance):
- Surprising:
- Tensions:
- Absent:
- Versus existing categories:

## Coverage check: [N atomic] notes = [sum of clusters + outliers]
```

---

## Verification

- [ ] Multi-idea notes split; duplicates merged with counts preserved.
- [ ] No predefined categories used to seed groups.
- [ ] Every cluster header is a statement, not a noun label.
- [ ] Every note appears exactly once; coverage sum matches.
- [ ] Outliers listed with reasons, not absorbed.
- [ ] Map reading distinguishes size from importance and names what is absent.

---

## False-Positive Prevention

1. **Top-down disguised as bottom-up.** Starting with "Pricing, UX, Marketing" and sorting into them produces the team's existing categories back. Group first; name after.
2. **Label headers.** "Onboarding" tells nobody what the notes say. If the header cannot be a sentence, the cluster may be a bin of unrelated notes.
3. **Forcing outliers.** Pushing the odd note into the nearest cluster erases the one idea that did not fit the pattern — often the interesting one.
4. **Size as salience.** A cluster of twenty similar notes may reflect one loud participant. Report size, but do not call it priority.
5. **Silent note loss.** Dropping notes during grouping is easy with large piles. The coverage check must balance.
6. **Mega-clusters.** A cluster holding a third of all notes is a super-group that was never split.
7. **Paraphrasing notes into agreement.** Rewriting notes so they fit a cluster changes the data. Quote them as given.

---

## Example

**Source:** 64 sticky notes from a workshop answering "What slows down a new hire's first month?" at a 200-person software company. Purpose: pick themes for an onboarding project.

**Processing:** 64 raw → 76 after splitting 7 multi-idea notes → 71 atomic after merging 5 duplicates (counts kept). Five of nine clusters shown.

- **Super-group A: New hires cannot get to real work because access and tools arrive late.**
  - A1: *Accounts and permissions take days, and nobody owns chasing them* (14) — "waited 4 days for repo access", "didn't know who to ask for VPN"…
  - A2: *Local environment setup depends on tribal knowledge* (9)
- **Super-group B: New hires do not know what "good" looks like in their first weeks.**
  - B1: *No one says what the first deliverable should be* (11)
  - B2: *Feedback arrives only at the 90-day review* (6)
- **Super-group C: Social connection depends on luck.**
  - C1: *Remote hires meet their team only in meetings* (8)
- **Outliers (4):** "the coffee machine is confusing" (no fit, low stakes); "I'd like to shadow a customer call" (a wish, not a blocker — possibly valuable).

**Reading:** A1 is largest, but 9 of its 14 notes came from one team's table. Surprising: nobody mentioned documentation quality. Tension: B1 asks for more structure while C1 asks for less scheduled time. Absent: nothing from managers' perspective — the workshop only included recent hires. Coverage: 71 = 67 clustered + 4 outliers.

---

## Techniques Used

- **DS-04 Pattern Recognition Requests** — similarity grouping surfaces patterns in the pile.
- **DS-37 Progressive Abstraction Transformation** — notes → clusters → super-groups, each level a complete representation.
- **RT-05 Evidence-Based Reasoning** — every cluster statement traced to note IDs.
- **OC-03 Markdown Table Specification** — relationships table and structured map.
- **QA-01 Self-Verification** — coverage balance and header-as-statement checks.

---

## Related Prompts

- `domain-ideation/ideation_idea_convergence_dot_voting.md` — vote on themes or their best notes after clustering.
- `domain-ideation/ideation_forced_quantity_100_ideas.md` — the kind of large list this prompt structures.
- `domain-agentic-resources/skills/non-coding/creative/idea-divergence-convergence/SKILL.md` — the full diverge/converge cycle.
