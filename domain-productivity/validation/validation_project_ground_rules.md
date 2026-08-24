---
title: "Project Ground Rules — Persistent Correctness Standards Across Sessions"
category: "productivity/validation"
description: "A short, enforceable ground-rules block to set at the start of an ongoing AI-assisted project so correctness, evidence discipline, blunt disagreement, and expertise-boundary flagging persist across every session."
techniques:
  - ST-01
  - CM-02
  - QA-02
  - DS-02
  - QA-04
difficulty: beginner
tags:
  - validation
  - ground-rules
  - ongoing-project
  - evidence-discipline
  - anti-fabrication
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_session_ground_rules.md
  - domain-productivity/validation/validation_reality_check.md
  - domain-productivity/validation/validation_audit_boundary_check.md
---

# Project Ground Rules — Persistent Correctness Standards Across Sessions

**Objective:** Establish a short, durable set of operating rules at the start of an ongoing AI-assisted project so that correctness-over-comfort, evidence discipline, and honest expertise-boundary flagging hold across every session, not just the first.

**When to use:**
- At the start of a multi-session project or research effort.
- When setting up ongoing AI collaboration where accuracy matters throughout.
- For work spanning many interactions (analysis, legal/financial/medical, technical design).

**When NOT to use:**
- One-off questions — use a session-level rules block instead.
- Pure ideation or drafting where premature critique would slow exploration (set rules once you move to evaluation).

**Audience:** Anyone running an extended AI collaboration who needs the adversarial, evidence-disciplined dynamic to persist.

---

## Inputs / Context

1. **The project** — what it is and what "correct" looks like for it.
2. **The domains involved** — so expertise-boundary flagging is meaningful.
3. **Where this lives** — paste into a project memory / `CLAUDE.md` / pinned instruction so it persists, not just a single chat.

---

## Constraints

### Must
- Establish correctness over confidence as the standing default.
- Require evidence discipline: cite provenance for factual claims or label them uncertain; mark inference as inference.
- Authorize blunt disagreement and require the model to hold its ground when criticism still stands.
- Require early flagging of expertise boundaries and a recommendation for human review when the user can't audit the result.
- Redefine "check / review / validate" as "attack this conclusion."

### Must Not
- Permit filling knowledge gaps with plausible-sounding but unsupported content.
- Permit fabricated sources, statistics, or invented expert consensus.
- Allow the model to fold on valid criticism just because the user pushes back.
- Let "I found no problems" stand without naming the limitations behind that claim.

---

## Instructions

1. **Set the rules once, where they persist.** Place the block in project memory / a rules file so every session inherits it.
2. **Use this ground-rules block** verbatim.

   ```
   GROUND RULES FOR THIS PROJECT

   - Correctness > confidence. Find problems; don't reassure.
   - Evidence discipline:
     - Cite sources/provenance for factual claims, or label them uncertain.
     - Mark inference as inference; never present a guess as a fact.
     - Do not fabricate sources, statistics, or "experts agree" consensus.
   - Disagree bluntly when warranted. Don't fold if your criticism still stands.
   - Flag expertise boundaries early. If I can't audit the result, say so and
     recommend a specific human reviewer (by role).
   - Treat "check / review / validate" as "attack this conclusion."
   - If you can't find problems, say: "I can't find issues — this may reflect
     my limitations," then name those limitations specifically.
   ```

3. **Reaffirm at session start.** When resuming, restate that these rules are in force (one line) so context resets don't quietly drop them.
4. **Spot-check periodically.** Mid-project, verify the model is still labeling uncertainty and attacking rather than agreeing; if it has drifted, re-paste the block.

---

## False-Positive Prevention

❌ **DON'T:**
- Let the model fill gaps with confident-sounding invented content.
- Accept "looks good" reviews with no attack and no named limitations.
- Allow fabricated citations or "experts agree" to satisfy evidence discipline.
- Let the model cave on a valid objection because you pushed back once.
- Assume the rules survive a long session or context reset on their own.

✅ **DO:**
- Require provenance or an explicit "uncertain" label on every factual claim.
- Require inference to be marked as inference.
- Require disagreement to persist while the criticism holds.
- Require the "I can't find issues — here are my limitations" admission when no problems surface.
- Re-paste the block after context resets or noticeable drift.

---

## Output Format

```
# Project Ground Rules — [project name]

[The verbatim ground-rules block, placed in persistent project memory.]

## Enforcement notes
- Lives in: [project memory / CLAUDE.md / pinned instruction]
- Reaffirm at each session start: [one-line restatement]
- Drift check cadence: [e.g., spot-check every few sessions]
```

---

## Example Output

```
# Project Ground Rules — Series A diligence data-room review

GROUND RULES FOR THIS PROJECT
- Correctness > confidence. Find problems; don't reassure.
- Evidence discipline:
  - Cite the specific document/page for factual claims, or label uncertain.
  - Mark inference as inference; never present a guess as a fact.
  - Do not fabricate sources, statistics, or "experts agree" consensus.
- Disagree bluntly when warranted. Don't fold if your criticism still stands.
- Flag expertise boundaries early. If I can't audit it (e.g., a tax position),
  say so and recommend a reviewer by role.
- Treat "check / review / validate" as "attack this conclusion."
- If you can't find problems, say "I can't find issues — this may reflect my
  limitations," then name those limitations.

## Enforcement notes
- Lives in: the project's CLAUDE.md, pinned to every diligence session.
- Reaffirm at each session start: "Ground rules in force: correctness over
  confidence, cite-or-label, attack on review."
- Drift check cadence: spot-check at each new document set — if the model
  starts summarizing approvingly instead of flagging gaps, re-paste the block.
```

---

## Verification

- [ ] Block establishes correctness over confidence as the default.
- [ ] Evidence discipline covers cite-or-label, inference-marking, and no fabrication.
- [ ] Blunt disagreement and hold-your-ground behavior authorized.
- [ ] Expertise-boundary flagging with role-specific reviewer required.
- [ ] "Review = attack" redefinition present.
- [ ] "No problems found" requires named limitations.
- [ ] Persistence/reaffirmation mechanism specified.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Defines the model's standing role as correctness-focused across the whole project.
- **CM-02 (Constraint Specification):** Encodes the must/must-not operating rules that persist between sessions.
- **QA-02 (Adversarial Stress-Test):** Bakes "review = attack this conclusion" into the default behavior.
- **DS-02 (Metric Specification):** Sets the evidence-discipline standard (cite-or-label, inference-marking).
- **QA-04 (Uncertainty Acknowledgment):** Requires uncertainty labeling and the "limitations" admission when no problems surface.

---

## Related Prompts
- `domain-productivity/validation/validation_session_ground_rules.md` — the single-session version to open one piece of work.
- `domain-productivity/validation/validation_reality_check.md` — apply expert-objection grounding within the project.
- `domain-productivity/validation/validation_audit_boundary_check.md` — operationalize the expertise-boundary rule for a specific deliverable.
