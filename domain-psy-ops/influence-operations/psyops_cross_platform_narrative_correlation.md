---
title: "Cross-Platform Narrative Correlation — The Same Story Across Platforms You Cannot See Equally"
category: psy-ops/influence-operations
description: "Assess whether a narrative's appearance across several platforms reflects connected activity or independent convergence, when each platform exposes different data, at different resolutions, with different retention. Builds a visibility map before any correlation is claimed, treats absence on a low-visibility platform as unknown rather than absent, and requires cross-platform links to rest on more than shared wording and similar timing."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-02
difficulty: advanced
tags:
  - psy-ops
  - cross-platform
  - narrative-analysis
  - data-access
  - influence-operations
  - is-this-coordinated
updated: "2026-09-24"
reasoning:
  styles: [analytic, systems, evidential, adversarial]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: visibility_map_with_graded_correlation
  user_role: [analyst, researcher, trust_and_safety, journalist]
  mode: [assess, map, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_narrative_lifecycle_tracker.md
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
---

# Cross-Platform Narrative Correlation

**Objective:** Assess whether a narrative appearing on several platforms reflects **connected activity** — shared origin, coordinated seeding, deliberate cross-posting — or **independent convergence**, where different communities arrive at the same story because the same event, grievance, or viral post reached all of them. Much cross-platform spread is the second kind. Content moves between platforms constantly through ordinary users screenshotting, reposting, and linking, and the same wording appears everywhere because people copy what they saw.

The problem that makes this a separate skill is **unequal visibility**. Each platform exposes different data: some offer research access to posts and timestamps, some expose little beyond what a logged-in user can scroll, some are closed messaging spaces visible only through what members choose to share, and retention varies from permanent to hours. A narrative that seems to *originate* on the most visible platform often only *surfaced* there first to the analyst. Absence on a platform you cannot see well is not absence — it is an unknown, and the analysis must carry it as one.

So this prompt builds a **visibility map** before any correlation is asserted, and it requires every cross-platform link to rest on evidence stronger than matching phrases and close timestamps — both of which organic spread produces in abundance.

**When to use:**
- A narrative appears on several platforms and you need to know whether that reflects a connected effort.
- A report claims a narrative "originated" on one platform and spread to others, and you need to test the claim.
- You are scoping a multi-platform investigation and need to know what your data can and cannot support.
- Your team holds strong data on one platform and weak data on others, and you need to prevent that asymmetry from shaping the conclusion.

**When NOT to use:**
- You are tracking a narrative's stages from seeding to mainstreaming on its own terms — use `psyops_narrative_lifecycle_tracker.md`.
- You are assessing coordination among accounts on one platform — use `psyops_coordinated_inauthentic_behavior_indicators.md`.
- You have not yet established that anything beyond organic activity is present — start with `psyops_influence_operation_analysis.md`.

**Audience:** Analysts, researchers, trust-and-safety staff, and journalists working with multi-platform data.

---

## Inputs / Context

1. **The narrative.** Its core claim, framing, and any distinctive phrasing, imagery, or links, stated precisely enough to match.
2. **Platforms in scope.** Every platform where it has been observed, and every plausible one where it has not been looked for.
3. **Data access per platform.** What you can see on each: full post data, sampled data, logged-in browsing only, member-shared screenshots, or nothing. Include retention and deletion.
4. **Observations per platform.** Earliest observed appearance, volume, and the kinds of accounts or communities carrying it. Mark estimates and unknowns `[VERIFY]`.
5. **Cross-platform traces.** Links, watermarks, screenshots carrying another platform's interface, identical media files, shared handles or profile elements.
6. **The triggering event.** Any real-world event, publication, or viral post that could have reached all platforms independently.
7. **The existing claim, if any.** What someone has asserted about origin or coordination, and on what basis.

---

## Constraints

### Must
- Build a **visibility map first**: for each platform, what can be observed, at what resolution, over what retention window.
- Carry **absence on a low-visibility platform as unknown**, never as a finding of absence.
- Distinguish **first observed** from **first appeared**. Your earliest observation is bounded by where you can see.
- Identify any **common upstream trigger** that could explain simultaneous appearance without any connection.
- Require cross-platform links to rest on **traceable artifacts** — shared files, carried interface elements, outbound links, reused infrastructure — rather than wording and timing alone.
- Grade each proposed link, and the overall correlation, **low / moderate / high** with the basis stated.
- Assess **behavior and content**, and describe communities by type rather than naming private individuals.
- Run an **alternative-explanation pass** built on ordinary cross-posting and shared exposure.

### Must Not
- Assert an origin platform because it is the one with the best data.
- Treat matching phrases as evidence of coordination. People copy what they read, and slogans travel by design.
- Treat near-simultaneous appearance as coordination when a shared trigger could explain it.
- Fill a low-visibility platform's gap with inference presented as observation.
- Invent account handles, post counts, timestamps, or platform data.
- Name private individuals as operators, or treat an account's presence on several platforms as evidence of covert affiliation.
- Produce guidance on seeding or moving content between platforms.

---

## Instructions

### Step 1 — Fix the narrative precisely
State the core claim, framing, and any distinctive elements. Separate what is distinctive enough to match (a specific fabricated statistic, a particular image file) from what is generic (a slogan, a common grievance). Only distinctive elements can carry a correlation.

### Step 2 — Build the visibility map
For every platform in scope, record data access, resolution, retention, and the window you actually examined. Mark the platforms where you cannot see at all. This map bounds every later claim.

### Step 3 — Record observations against visibility
Tabulate earliest observed appearance, volume, and community type per platform — each annotated with the visibility limit that applies. An early timestamp on a high-visibility platform and a missing one on a closed platform are not comparable.

### Step 4 — Identify common triggers
List every event, publication, broadcast, or viral post that could have reached all these platforms independently. If one exists and precedes the appearances, independent convergence becomes the leading explanation until something rules it out.

### Step 5 — Trace artifacts across platforms
Look for evidence that content physically moved: identical media files, screenshots carrying another platform's interface, outbound links, shared watermarks, reused infrastructure. Each is a candidate link; note its direction and whether ordinary users could have produced it.

### Step 6 — Grade each link and the overall correlation
For each candidate link, state what it shows (content moved / content moved deliberately / content moved in a coordinated way) and at what confidence. Most links show only that content moved, which ordinary sharing does constantly.

### Step 7 — Alternative-explanation pass
Construct the fully organic account: a shared trigger, ordinary cross-posting, screenshots, and communities with overlapping membership. State what, specifically, it fails to explain. If it explains everything, that is the finding.

### Step 8 — Adversarial check and judgment
Argue that your visibility asymmetry produced the pattern you see. Then state the judgment — connected / independent convergence / **insufficient visibility to determine** — with confidence, basis, and the data access that would change it.

---

## False-Positive Prevention

1. **Visibility mistaken for origin.** The platform with the best data looks like the source because it is the one you can see first.
2. **Absence treated as absence.** Concluding a narrative was not present on a closed or low-retention platform because you found nothing there.
3. **Shared wording as coordination.** Identical phrases produced by ordinary copying, slogans, and quotation of a single viral post.
4. **Simultaneity without a trigger check.** Reading near-simultaneous appearance as orchestration when a broadcast or public event reached everyone at once.
5. **Content movement read as coordination.** Screenshots and links prove content moved; ordinary users move content between platforms all day.
6. **Overlapping audiences read as networks.** The same communities exist on several platforms; the same people carrying a story in both places is membership, not an operation.
7. **Inference filling gaps.** A plausible reconstruction of what "must have" happened on a platform you could not see, presented as observation.
8. **Account presence as affiliation.** Treating an account's activity on several platforms as evidence of covert organization rather than ordinary multi-platform use.

---

## Output Format

```
# Cross-platform correlation — [narrative]

## Narrative definition
Core claim: [...]
Distinctive (matchable) elements: [...]
Generic (non-matchable) elements: [...]

## Visibility map
| Platform | Data access | Resolution | Retention | Window examined |
|---|---|---|---|---|
| [...] | [full / sampled / browse-only / member-shared / none] | [...] | [...] | [...] |

## Observations (annotated with visibility)
| Platform | Earliest observed | Volume | Community type | Visibility limit |
|---|---|---|---|---|

## Common triggers
[Events or viral posts that could have reached all platforms independently, with timing]

## Cross-platform artifacts
| Artifact | From → to | Shows | Could ordinary users produce it? | Confidence |
|---|---|---|---|---|

## Alternative-explanation pass
[The fully organic account, and what — if anything — it fails to explain]

## Adversarial check
[The case that my visibility asymmetry produced this pattern]

## Judgment
[Connected / independent convergence / **insufficient visibility to determine**]
Confidence: [low / moderate / high] — basis: [...]
Would change with: [specific data access]
Outstanding [VERIFY] items: [...]
```

---

## Verification

- [ ] The narrative is defined with distinctive elements separated from generic ones.
- [ ] A visibility map was built before any correlation was asserted.
- [ ] Absence on a low-visibility platform is carried as unknown.
- [ ] "First observed" is distinguished from "first appeared."
- [ ] Common upstream triggers were identified and tested before coordination was considered.
- [ ] Every cross-platform link rests on a traceable artifact, graded for what it actually shows.
- [ ] The alternative-explanation pass was run on ordinary cross-posting and shared exposure.
- [ ] "Insufficient visibility to determine" was available and was not avoided.
- [ ] No handles, counts, timestamps, or platform data were invented.
- [ ] No private individual is named as an operator, and no content-seeding guidance appears.
