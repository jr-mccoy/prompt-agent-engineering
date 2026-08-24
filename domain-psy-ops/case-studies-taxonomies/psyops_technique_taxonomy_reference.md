---
title: "Technique Taxonomy Mapping — Reconciling the Competing Frameworks"
category: psy-ops/case-studies-taxonomies
description: "Map the named public frameworks for influence and propaganda technique against each other — which describe the same move under different names, which operate at different levels of analysis, and where each was built for a purpose that limits its transfer. Requires every framework attribution to be verified rather than recalled, since misattributed taxonomy is the characteristic error in this literature."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - taxonomy
  - frameworks
  - reference
  - education
updated: "2026-07-28"
reasoning:
  styles: [analytic, comparative, synthetic]
  stakes: moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: framework_crosswalk
  user_role: [analyst, educator, researcher, student]
  mode: [synthesize, teach, audit]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_propaganda_technique_identification.md
  - domain-psy-ops/case-studies-taxonomies/psyops_media_literacy_curriculum_designer.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
---

# Technique Taxonomy Mapping

**Objective:** Build a crosswalk between the named public frameworks used to classify influence and propaganda technique, so that an analyst or teacher can see **which frameworks describe the same move under different names**, **which operate at incompatible levels of analysis**, and **where each was built for a purpose that limits how far it transfers**. The field has accumulated overlapping vocabularies from wartime propaganda analysis, social psychology, marketing, platform integrity, and security research, and practitioners routinely mix terms from frameworks with different units of analysis without noticing.

The level problem is the substantive one. Some frameworks classify **rhetorical devices inside a message**, some classify **compliance mechanisms operating on a person**, some classify **campaign-level behavior across a network**, and some classify **analytic axes for an investigation**. A device, a mechanism, a behavior, and an axis are not the same kind of thing, and a crosswalk that lines them up in one table produces confident nonsense.

The prompt's hard constraint is **verification**. Misattributed taxonomy — the wrong author, an invented category, a framework credited with a list it never contained — is the characteristic error in writing about this field, and it propagates because the attributions sound authoritative. Every framework detail here must be checked against the primary source or marked unverified.

**When to use:**
- You are teaching this and need a coherent vocabulary rather than five overlapping ones.
- You are reading across literatures and cannot tell whether two terms name the same thing.
- You are choosing a framework for an analysis and want to know what it was built for.
- You are writing something that cites a taxonomy and want the attribution right.

**When NOT to use:**
- You want to analyze a specific artifact — use `../technique-analysis/psyops_propaganda_technique_identification.md`.
- You want to build a teaching sequence — use `psyops_media_literacy_curriculum_designer.md`.
- You want the operational analytic framework for a live assessment — use `../influence-operations/psyops_influence_operation_analysis.md`.

**Audience:** Educators, researchers, analysts, and students working across more than one literature.

---

## Inputs / Context

1. **The frameworks in scope.** Which ones you are working with, and where you encountered each.
2. **Your purpose.** Teaching, analysis, writing, or building an instrument — this determines which level of analysis you need.
3. **Access to primary sources.** Which frameworks you can check directly, and which you know only through secondary description. This bounds what can be asserted.
4. **The audience.** Specialists tolerate multiple vocabularies; beginners need one.
5. **Known confusions.** Terms you have seen used inconsistently.

---

## Constraints

### Must
- Assign every framework a **level of analysis**: rhetorical device, compliance mechanism, campaign behavior, or analytic axis. Do not cross levels in a single mapping table.
- Record for each framework its **origin purpose and period**, since that determines what it handles well and what it cannot see.
- Mark every attribution as **verified against a primary source** or **unverified**. Unverified attributions must be labeled inline, not in a footnote.
- Identify **genuine synonyms** — different names for the same move — separately from **near-neighbors** that differ in an important respect.
- Note **coverage gaps**: what each framework has no category for, which is usually a function of when it was built.
- Flag frameworks whose categories are **not mutually exclusive** or **not collectively exhaustive**, since most are neither and users assume both.
- Recommend a **single working vocabulary** for the user's purpose, and say what it gives up.

### Must Not
- State a framework's author, date, category list, or definitions from memory as established. Every specific must be verified or marked unverified.
- Invent categories, or attribute a category to a framework that does not contain it. This is the field's signature error.
- Present a framework as authoritative or standard when the field has no agreed standard.
- Merge levels of analysis into one table for tidiness.
- Treat older frameworks as superseded. Wartime propaganda analysis handles rhetorical device better than most modern platform-derived frameworks.
- Imply consensus where the literature is contested.

---

## Instructions

### Step 1 — List the frameworks and their access status
For each: can you check the primary source, or do you know it only secondhand? Everything you cannot check is provisional and must be labeled.

### Step 2 — Assign each a level of analysis
Rhetorical device (inside a message), compliance mechanism (operating on a person), campaign behavior (across a network), or analytic axis (structuring an investigation). Group by level before comparing anything.

### Step 3 — Record origin and purpose
When was it built, by whom, and for what? A framework built to analyze wartime radio broadcasts, one built from compliance experiments, and one built to classify platform enforcement cases are answering different questions.

### Step 4 — Build within-level crosswalks
Within each level only, map genuine synonyms. Note where the underlying concept differs even though the label matches, which is common and is where most confusion originates.

### Step 5 — Identify near-neighbors and their distinctions
Terms that are close but not identical. State the distinguishing feature precisely — this is the most useful output for a working analyst.

### Step 6 — Map coverage gaps
What has no category in each framework? Pre-digital frameworks have no vocabulary for algorithmic amplification; platform frameworks often have none for rhetorical structure.

### Step 7 — Flag structural weaknesses
Which frameworks have overlapping categories, no exhaustive coverage, or categories at inconsistent levels of abstraction. Most have at least one; users generally assume none.

### Step 8 — Recommend a working vocabulary and state the tradeoff
For the user's stated purpose, one vocabulary, with what it cannot express. Then verify every attribution in the output once more.

---

## False-Positive Prevention

1. **Attribution from memory.** Stating an author, date, or category list without checking. It sounds authoritative, propagates freely, and is the field's characteristic error.
2. **Invented categories.** Adding a plausible-sounding category to a framework that never had it. Verify the actual list.
3. **Cross-level mapping.** Lining up a rhetorical device against a campaign behavior. Tidy, and wrong.
4. **False standardization.** Presenting any framework as the accepted standard. There is no agreed standard and implying one misleads.
5. **Superseded-by-recency.** Assuming newer frameworks improve on older ones. Older propaganda analysis often handles message-level device better.
6. **Exhaustiveness assumed.** Treating a category list as covering the space. Most were built for a specific corpus and inherit its limits.
7. **Label-match without concept-match.** Two frameworks using the same word for different concepts, mapped as synonyms. Check the definitions, not the labels.
8. **Consensus implied.** Presenting contested distinctions as settled.

---

## Output Format

```
# Framework crosswalk — [purpose]

## Frameworks in scope
| Framework | Origin period | Built for | Primary source checked? |
|---|---|---|---|
| [name] | [period] | [original purpose] | **verified** / **UNVERIFIED — treat as provisional** |

## Level of analysis
| Level | Frameworks operating here |
|---|---|
| Rhetorical device (inside a message) | |
| Compliance mechanism (on a person) | |
| Campaign behavior (across a network) | |
| Analytic axis (structuring an investigation) | |

## Within-level crosswalks
### Level: [level]
| Concept | Framework A term | Framework B term | Same concept? |
|---|---|---|---|
| [move] | [term] | [term] | yes / **label matches, concept differs** |

## Near-neighbors (close but distinct)
| Term A | Term B | The distinguishing feature |
|---|---|---|

## Coverage gaps
| Framework | Has no category for |
|---|---|

## Structural weaknesses
| Framework | Overlapping categories? | Exhaustive? | Consistent abstraction level? |
|---|---|---|---|

## Recommended working vocabulary
[One vocabulary for the stated purpose] — **what it cannot express:** [...]

## Unverified attributions in this document
[Every item not checked against a primary source, listed explicitly]
```

---

## Verification

- [ ] Every framework is assigned a level of analysis, and no mapping table crosses levels.
- [ ] Every attribution is marked verified or unverified, with unverified items labeled inline and listed at the end.
- [ ] No author, date, category, or definition was stated from memory as established fact.
- [ ] No category was attributed to a framework that does not contain it.
- [ ] Genuine synonyms are distinguished from label-matches whose underlying concepts differ.
- [ ] Coverage gaps are identified for each framework.
- [ ] Structural weaknesses — overlap, non-exhaustiveness, inconsistent abstraction — are flagged.
- [ ] No framework is presented as the field's standard, and contested distinctions are not presented as settled.
- [ ] Older frameworks are not treated as superseded by recency alone.
- [ ] A single working vocabulary is recommended with its tradeoff stated.
