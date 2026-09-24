---
title: "Heuristic Evaluation — Expert Usability Review of a Web or App Interface Against Named Heuristics"
category: frontend-development/ux-research
description: "Run a structured expert usability review of a visual web or app interface: fix the heuristic set (Nielsen's ten by default), walk defined user flows screen by screen, record each violation with its location, the heuristic, the evidence, and a severity, and mark which findings need user testing to confirm — distinct from the WCAG conformance audit (accessibility success criteria) and the voice-UX audit (spoken interfaces)."
techniques:
  - DS-01
  - DT-05
  - RT-05
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - ux-research
  - heuristic-evaluation
  - usability
  - expert-review
  - nielsen-heuristics
  - audit
  - no-users-yet
  - confusing-interface
  - before-redesign
updated: "2026-09-24"
related_prompts:
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-voice-conversational-ui/voice-ux/voice_ux_best_practices_audit.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
---

# Heuristic Evaluation

**Objective:** Find likely usability problems in an interface cheaply, before
or between user studies, by reviewing defined flows against an agreed set of
heuristics — and report each finding with enough evidence that another
evaluator could locate it and disagree with it.

**When to Use:**
- A design or build needs a quick usability pass and no users are available yet.
- You want to clean up obvious problems *before* a usability test, so sessions
  are spent on the hard questions.
- A redesign needs a before/after comparison on the same flows.

**Not this prompt if:**
- The question is accessibility conformance (contrast, keyboard, ARIA, WCAG
  success criteria) → `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md`.
  Accessibility barriers found here are noted and handed off, not scored.
- The interface is voice or conversational → `domain-voice-conversational-ui/voice-ux/voice_ux_best_practices_audit.md`.
- You have user-session evidence to rate → `frontend_ux_usability_findings_severity_log.md`.
- You need an opinionated critique of visual direction → `frontend_ux_design_critique_facilitator.md`.

## Inputs

1. **The interface**: URL, prototype, or screenshots in flow order.
2. **2–4 flows** to walk, each stated as a user goal.
3. **Primary users** and their context (first-time vs expert, device).
4. **Heuristic set**, if the team uses one other than Nielsen's ten.
5. **Number of evaluators.** One evaluator finds a fraction of problems;
   3–5 independent evaluators, merged afterwards, is the standard practice.

## Method

1. **Fix the framework (DS-01).** Default: Nielsen's ten — visibility of system
   status; match with the real world; user control and freedom; consistency
   and standards; error prevention; recognition over recall; flexibility and
   efficiency; aesthetic and minimalist design; help users recognise, diagnose
   and recover from errors; help and documentation. State any additions (e.g.
   domain conventions) before starting, not during.
2. **Walk each flow twice.** First pass as the user, attempting the goal.
   Second pass screen by screen, assessing each element against the set
   (DT-05). Record the state (empty, loading, error, success) — most
   violations live in non-happy states.
3. **Record each finding with evidence (RT-05).** Location (screen + element),
   heuristic, what happens, why it will cost a user, and a confidence level.
   One finding per problem; one problem may cite two heuristics.
4. **Rate severity (DS-06)** on 0–4: 0 not a problem; 1 cosmetic; 2 minor;
   3 major; 4 catastrophic (blocks the goal). Weigh frequency, impact, and
   persistence. Where evaluators are several, rate independently, then merge.
5. **Separate what needs users (QA-12).** Mark each finding *confirmable by
   inspection* (e.g. no undo exists) or *needs user evidence* (e.g. a label
   might be misunderstood). List near-misses you considered and dismissed.
6. **Report strengths.** Name what works and must survive a redesign.

## Output Format

```
# Heuristic evaluation — [product / flows] — [date], evaluators: [n]
Heuristic set: [...]   Flows: [...]   States covered: [...]

## Findings
| ID | Flow · screen · element | Heuristic(s) | What happens | User cost | Sev 0–4 | Confidence | Confirm by |

## Considered and dismissed
| Candidate | Why it is not a violation |

## Handed off
Accessibility: [...] → WCAG audit    Content/copy: [...]

## Strengths to keep
## Top 3 to fix first, with rationale
```

## Verification

- [ ] Every finding names a location precise enough for another evaluator to find.
- [ ] Every finding cites a heuristic from the declared set.
- [ ] Empty, loading, and error states were reviewed for each flow.
- [ ] Severity uses the 0–4 scale with its definitions, not "high/medium".
- [ ] Findings needing user evidence are marked, not asserted.
- [ ] At least one dismissed candidate is listed.

## False-Positive Prevention

1. **Personal taste is not a heuristic violation.** "I'd prefer a darker
   header" cites no heuristic; drop it or move it to a design critique.
2. **Inconsistency with *another* product is not inconsistency.** Heuristic 4
   concerns this product's internal and platform conventions.
3. **Minimalism does not mean fewer features.** Flag irrelevant *information*
   competing for attention, not capability the user needs.
4. **A single evaluator's severity is an estimate.** Mark confidence and do not
   present one person's ratings as consensus.
5. **Accessibility defects are not "aesthetic" findings.** Hand them to the
   WCAG audit with their location instead of scoring them here.
6. **Documented, intentional friction is not an error-prevention failure.**
   A confirmation step on "delete workspace" is the heuristic working.
7. **Do not predict user behaviour you have not observed.** "Users will not
   see this" is a hypothesis; phrase it as one and mark *needs user evidence*.

## Example Output

```
# Heuristic evaluation — Project settings (web app) — 2026-09-24, evaluators: 1
Heuristic set: Nielsen 10.  Flows: rename project; invite member; delete project.
States covered: default, saving, validation error, success.

## Findings
| ID | Location | Heuristic | What happens | User cost | Sev | Conf | Confirm by |
|---|---|---|---|---|---|---|---|
| H1 | Rename · General tab · Save | 1 Visibility of status | Save shows no feedback; name updates only after reload | User re-clicks, or leaves believing it failed | 3 | High | Inspection |
| H2 | Invite · email field | 9 Error recovery | Invalid email error reads "Error 422" | Cannot tell what to fix | 3 | High | Inspection |
| H3 | Invite · role dropdown | 2 Real-world match | Roles "Maintainer / Reporter" with no description | Wrong permissions granted | 2 | Medium | User test (T-role) |
| H4 | Delete · danger zone | 3 User control | Deletion is immediate, no undo, no grace period | Irreversible loss | 4 | High | Inspection |
| H5 | All tabs · left nav | 6 Recognition over recall | Current tab not highlighted | Disorientation after save | 1 | Medium | Inspection |

## Considered and dismissed
| Candidate | Why not |
|---|---|
| Delete asks to type the project name | Deliberate friction for a destructive act (heuristic 5 working) |
| Settings split across 4 tabs | Grouping matches task frequency; no evidence of cost |

## Handed off
Accessibility: H5's missing current-tab indicator also lacks aria-current → WCAG audit.

## Strengths to keep
Invite flow pre-fills the team domain; role defaults to least privilege.

## Top 3 to fix first
H4 (irreversible, sev 4) · H1 (affects every save) · H2 (blocks invites).
H3 goes into the next usability test as a task rather than a fix.
```

## Techniques Used

- **DS-01 Framework Application** — a declared heuristic set applied consistently.
- **DT-05 Element-by-Element Assessment Matrix** — screen-by-screen second pass.
- **RT-05 Evidence-Based Reasoning** — location and observed behaviour per finding.
- **DS-06 Prioritization and Severity Guidance** — 0–4 severity with definitions.
- **QA-12 False Positives Identification** — dismissed candidates and "needs user evidence".

## Related Prompts

- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` — accessibility conformance.
- `domain-voice-conversational-ui/voice-ux/voice_ux_best_practices_audit.md` — the voice-interface equivalent.
- `frontend_ux_usability_findings_severity_log.md` — rating problems observed with users.
