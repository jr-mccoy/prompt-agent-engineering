---
title: "Dual-Use Research Assessment (DURC Self-Screen)"
category: science/ethics-integrity
description: "A governance-level self-screen that walks a researcher through the recognized categories of experiments of concern, classifies likely level of dual-use concern, and routes the work to the proper biosafety/biosecurity committee with a mitigation and communication plan — without providing any operational detail."
techniques:
  - ST-01
  - RT-01
  - CM-02
  - QA-02
  - NE-10
  - ST-03
difficulty: advanced
tags:
  - dual-use-research
  - durc
  - biosecurity
  - research-governance
  - responsible-disclosure
  - p3co
  - risk-screening
  - research-ethics
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/ethics-integrity/science_authorship_and_credit_resolver.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Dual-Use Research Assessment (DURC Self-Screen)

**Objective:** Help a researcher RECOGNIZE that their work may be dual-use research of concern (DURC) and ROUTE it, with appropriate framing, to the people and committees empowered to make a determination. This prompt operates strictly at the governance and process level: it walks the recognized categories of experiments of concern at a recognition level, asks the screening questions, classifies likely concern, and produces a notification, mitigation, and communication plan. It provides no methods, no agent-enhancement techniques, and no operational detail of any kind.

**When to use:** At project conception, before submitting a grant, before generating data that could raise concern, and again before drafting any manuscript or sharing data/methods publicly — whenever the work touches pathogens, toxins, or capabilities that could be misused.

**Required inputs:**
- **Discipline.** <field; e.g., microbiology, synthetic biology, virology, public-health modeling, chemistry>
- **Study / manuscript context.** <plain-language description of the research aim and what is being studied, in the user's own words; `[user-supplied]` for anything not stated. Do not request or include operational/technical methods.>
- **Agents / systems involved.** <general categories the user names — e.g., a category of pathogen, toxin, or computational capability; user-supplied, never inferred toward greater hazard>

**Optional inputs:**
- Funder and national framework that applies (e.g., US Government DURC/P3CO policy, institutional policy, WHO guidance).
- Whether an Institutional Biosafety Committee (IBC) or biosafety officer has already reviewed the work.
- Intended dissemination route (open publication, preprint, dataset release, software release).
- Any prior dual-use determination already made.

**Constraints — Must:**
- Frame the seven recognized **categories of experiments of concern** at a recognition level only: (1) enhances harmful consequences of an agent/toxin; (2) disrupts immunity or vaccine effectiveness; (3) confers resistance to useful interventions (e.g., therapeutics) or facilitates evasion of detection; (4) increases stability, transmissibility, or ability to disseminate; (5) alters host range or tropism; (6) enhances susceptibility of a host population; (7) generates or reconstitutes an eradicated/extinct agent or one of significant concern. Name the category; never describe how any of it is done.
- Reference the governance framing of the agents/toxins of concern and the P3CO (potential pandemic pathogen care and oversight) review pathway at the policy level only.
- Classify likely concern as **none indicated / possible / likely** and tie the classification to which screening questions were triggered.
- Produce a routing plan naming the correct human/committee contacts (PI, IBC, institutional biosafety officer, research-integrity/biosecurity office, funder program officer, national review body).
- Present mitigation options as governance/process choices and frame the openness-vs-biosecurity tradeoff responsibly, naming responsible disclosure and restricted/controlled sharing as the considered exception to an Open Science default.

**Constraints — Must Not:**
- Do not invent facts, results, image data, institutional/journal policies, or biosecurity determinations. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not give a final biosecurity, legal, or editorial determination, and does not replace the IBC / institutional biosafety / DURC committee / journal editor / COPE process. Route formal decisions there.
- Do not provide, request, or reconstruct any operational method, protocol, enhancement technique, troubleshooting detail, or step that could give misuse uplift. If the described work sounds genuinely hazardous, the correct output is "stop and route to your IBC / institutional biosafety officer / national framework," not analysis.
- Do not produce an agent list paired with enhancement techniques, gain-of-function methodology, or anything that increases capability.
- Do not reassure a user out of escalation; when in doubt, escalate.
- Do not use "novel," "groundbreaking," or "first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope at the governance level.** Restate discipline and the plain-language aim. Explicitly note that you will not discuss methods. Mark missing context `[user-supplied]`.
2. **Run the recognition screen.** For each of the seven categories of experiments of concern, ask a yes / no / unsure recognition question phrased so the user answers without supplying technical detail. Record which categories are triggered.
3. **Hard-stop check.** If any answer indicates the work could enhance harm, transmissibility, host range, resistance, or reconstitute an agent of concern, route immediately — do not continue to fine-grained analysis. Output the stop-and-route result.
4. **Classify likely concern.** Map triggered categories to **none indicated / possible / likely**, stating which questions drove the level. Treat "unsure" as escalation-worthy, not as "none."
5. **Build the routing plan.** Name who must be notified and in what order (PI → IBC / biosafety officer → institutional biosecurity/integrity office → funder → national framework), and note any pre-publication review obligation.
6. **Lay out mitigation options (governance only).** Offer process-level choices: study redesign or scope reduction discussed with the committee, restricted/abbreviated methods sections, controlled or tiered data access, responsible disclosure timing, pre-publication biosecurity review, and decline-to-publish-as-is. Describe the purpose of each, not the technical content.
7. **Frame the openness tradeoff (probability-weighted).** Sketch plausible benefit and misuse scenarios at a high level, weight the openness-vs-biosecurity balance qualitatively, and state that the committee — not this prompt — owns the call. Default to Open Science except where a recognized concern justifies restricted sharing/responsible disclosure.
8. **Draft the communication package.** Produce a neutral notification note to the IBC/biosafety officer that states the aim, the triggered categories, and the requested review — with no operational detail — plus a documentation log entry.
9. **Self-check (adversarial).** Re-read the output as if you were trying to extract misuse uplift from it; if any line provides method, capability, or technique, remove it. Confirm every gap is `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation (governance level)
[discipline, plain-language aim, agents/systems as named; "methods intentionally excluded"; gaps flagged]

## Experiments-of-Concern Recognition Screen
| # | Category (recognition level) | Triggered? (Y / N / Unsure) | Note (no methods) |
| 1 | Enhances harmful consequences of an agent/toxin | | |
| 2 | Disrupts immunity / vaccine effectiveness | | |
| 3 | Confers resistance to useful interventions / evades detection | | |
| 4 | Increases stability / transmissibility / dissemination | | |
| 5 | Alters host range or tropism | | |
| 6 | Increases host-population susceptibility | | |
| 7 | Generates/reconstitutes an eradicated or significant-concern agent | | |

## Concern Classification
[none indicated / possible / likely] — driven by categories: [...]
[If any hard-stop trigger: "STOP — route now; analysis halted by design."]

## Routing Plan (who to notify, in order)
- PI / supervisor
- IBC / institutional biosafety officer
- Institutional biosecurity / research-integrity office
- Funder program officer / national framework (e.g., DURC/P3CO pathway)
- Pre-publication review obligation? [Y / N / [user-supplied]]

## Mitigation Options (governance/process only)
- [option] — purpose, who decides
...

## Openness vs. Biosecurity Tradeoff
[high-level benefit scenario] | [high-level misuse scenario] | qualitative weighting | "committee owns the determination"
Default: Open Science, except restricted sharing / responsible disclosure where a recognized concern applies.

## Draft Notification to IBC / Biosafety Officer
[neutral note: aim, triggered categories, requested review — NO operational detail]

## Documentation Log Entry
[date, who screened, result, routing taken]

## Open Items
- [ ] [user-supplied gap]
```

**Standard alignment:** US Government Policy for Dual Use Research of Concern (DURC) and the P3CO oversight framework; the seven categories of experiments of concern and the agents/toxins-of-concern framing (governance level only); WHO guidance on responsible life-sciences research and biosecurity; NIH/OSTP dual-use frameworks; responsible-disclosure norms as the considered exception to an Open Science default.

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured before screening; methods explicitly excluded.
- [ ] All seven experiment-of-concern categories screened at recognition level only.
- [ ] No operational method, enhancement technique, agent-uplift detail, or troubleshooting present anywhere.
- [ ] Any "could enhance harm/transmissibility/host range/resistance/reconstitution" answer triggered an immediate route, not deeper analysis.
- [ ] "Unsure" treated as escalation-worthy, not "none."
- [ ] Routing plan names the correct human contacts and committees.
- [ ] Mitigation framed as governance/process options; openness-vs-biosecurity tradeoff handed to the committee.
- [ ] Notification draft contains the aim and categories but no technical detail.
- [ ] No facts, agents, or policies invented; gaps marked `[user-supplied]`; drafted text free of "novel/groundbreaking/first-ever."

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Operational uplift | "Helpful" detail on how an experiment is done | Hard rule: recognition-level only; strip any method, capability, or technique |
| False "all clear" | Classifying as "none" because the user sounds confident | Treat "unsure"/triggered categories as escalation; default to routing |
| Self-adjudication | Telling the user their work is fine to publish | Only the IBC/DURC committee/funder determines; this structures and routes |
| Openness absolutism | Defaulting to full open release on concerning work | Name restricted sharing / responsible disclosure as the considered exception |
| Hazard reconstruction | Re-deriving the concerning method to "assess" it | Never reconstruct; assess at the category level from user's words only |
