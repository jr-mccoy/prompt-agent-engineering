---
title: "Generate a Handoff Briefing So a Real Engineer Can Take Over"
category: software-engineering/vibe-coding-rescue
description: "Produce a handoff briefing that lets a competent engineer who has never seen the codebase take ownership safely: what the code does, what it actually does (when that differs), what works, what's fragile, where AI-generated risk sits, what the new engineer should change first, and what NOT to touch until they've earned the context."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - handoff
  - documentation
  - engineer-briefing
  - takeover
updated: "2026-04-21"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
  - domain-productivity/operating-cadence/cos_memory_scaffold_claude_md.md
---

# Generate a Handoff Briefing So a Real Engineer Can Take Over

**Purpose:** A vibe-coded project passing to a new engineer — contract, internal hire, or long-term owner — needs a briefing the current author often isn't ready to write. The new engineer must be able to: understand intent, spot fragile areas, avoid the footguns the original author internalized, and know what not to touch until context accrues. This prompt produces that briefing. It is written for the new engineer, not for the original author's ego.

**When to use:**
- A project is being handed off to a new owner (you're leaving, or you've decided to stop being the sole maintainer).
- A wall diagnosis recommended handoff instead of in-place rescue.
- A freelancer / contractor is being brought in and needs to ramp fast.
- A project is being donated to a team that will assess whether to keep it.

**Don't use when:** The user is staying on the project and wants documentation for their own reference. Use a memory scaffold instead (`airollout_long_running_project_memory.md`).

**Audience:** The new engineer is the reader. The current author is the input. Output is a document handed over with the repo.

---

## Inputs Required

1. **Project purpose and intended behavior.** 2–5 sentences. What the project does; who or what uses it; what the definition of "working" is.
2. **Honest map of what the code does vs what it's supposed to do.** Specific divergences the author knows about. Features partially done, paths not exercised, TODOs not written down.
3. **5–10 things the author is confident work.** Features or flows the author has personally verified working recently.
4. **5–10 things the author suspects are fragile or wrong.** Where bugs live. Where tests are missing or self-confirming. Where the AI produced "plausible-looking" code the author hasn't deeply verified.
5. **Repo shape.** Language, framework, build/test commands, dependencies, external services, data sensitivity.
6. **Deployment.** Where the project runs (local / cloud / internal service). Who deploys. Secrets location.
7. **AI-assistance history.** Rough share AI-assisted. Which files / modules are most AI-generated.
8. **Any existing audit or rules file output.** If `viberescue_security_audit.md` or `viberescue_rules_file_design.md` has been run, cite the outputs.
9. **The first task the new engineer should pick up.** Something small and unrelated to the fragile zones — to build context before editing load-bearing code.
10. **What the author asks the new engineer NOT to do in the first 2 weeks.** Areas off-limits until context is earned.

---

## Instructions

### Step 1 — Write to the reader, not about the project

The briefing addresses the new engineer directly: "When you open this repo, you'll see…" Not "This project was started in…" The voice changes the utility.

### Step 2 — Section 1: What this project is

2–5 sentences. Answer:

- What it does (one sentence).
- Who or what uses it.
- What "working" means (operational definition).
- How the author knows it's working (tests, manual check, customer signal).

If any of these can't be answered, say so — the new engineer needs to know that too.

### Step 3 — Section 2: What the code actually does vs what it's supposed to do

A table of divergences from input 2:

| Area | Intended behavior | Actual behavior | How the author knows |
|------|-------------------|-----------------|---------------------|
| [module] | | | |

If the author discovers divergences while writing this briefing, note them honestly. The goal is "fewer surprises for the new engineer," not "looks-good handoff."

### Step 4 — Section 3: What works (confidence: high)

Bulleted list from input 3. Each item:

- What it does.
- Where it lives (file / module).
- How to verify it still works (command, URL, test name).

This gives the new engineer a platform of trust to stand on.

### Step 5 — Section 4: What's fragile (confidence: low)

Bulleted list from input 4. Each item:

- The fragile or wrong area.
- Why the author suspects (specific symptom, test gap, weird pattern, AI-generated code that looked right but wasn't verified).
- What would break if the new engineer naively changed it.
- Any workarounds currently compensating.

Fragility notes should be specific. "The auth logic is sketchy" is not enough. "The `verify_token` function in `auth/middleware.py` was AI-generated and uses `hmac.compare_digest` wrapper that I haven't validated against the library version; token expiry check is on line 47 and uses `datetime.now()` without timezone — I don't know if that matches the issuer's timezone" is useful.

### Step 6 — Section 5: Known AI-generated risk areas

From input 7 and input 8. List the modules where AI wrote most of the code, and specifically flag:

- Auth / permissions logic.
- Data access layers (SQL, ORM usage).
- External API clients.
- Deserialization / ingestion.
- Any reimplemented primitives (crypto, caching, retry).

Pair each with any security audit findings (input 8). If no audit has been run, recommend running `viberescue_security_audit.md` in the first week.

### Step 7 — Section 6: How to run it

Concrete. Not "follow the README" unless the README is genuinely sufficient:

- Local setup (step by step).
- Environment variables required.
- External dependencies (databases, queues, services, API keys).
- Build / test / run commands, exact.
- Known first-time setup gotchas.

### Step 8 — Section 7: Deployment and operational posture

From input 6:

- Where it runs.
- Who deploys.
- Secrets source.
- Monitoring / alerting / paging posture.
- On-call, if any.

If any of these don't exist, say so. "No alerting" is critical context.

### Step 9 — Section 8: First task for the new engineer

From input 9. Specifically:

- What the task is.
- Why it's a good first task (low-risk, off the fragile zones, touches 1–2 files, has a testable success criterion).
- Acceptance criteria (observable).
- A reviewer if one exists, or an instruction to self-review with the rules file.

### Step 10 — Section 9: Don't-touch-yet

From input 10. A short list. Areas the author is asking the new engineer not to modify in the first 2 weeks, with a reason per entry. "Because it's fragile" is allowed; "because I say so" is not.

The new engineer can choose to override, but they're doing so informed.

### Step 11 — Section 10: Open questions and unknowns

Explicit list of things the author genuinely doesn't know:

- Decisions they made in haste and aren't sure about.
- Features half-built with no clear target.
- External dependencies they've never tested failure modes for.
- Conventions that might not actually be conventions.

This is often the most valuable section. Fight the urge to make the project look complete.

### Step 12 — Section 11: Artifacts

Point to (not embed):

- Rules file (`viberescue_rules_file_design.md` output).
- Memory / architecture / state files (`airollout_long_running_project_memory.md` output).
- Any security audit (`viberescue_security_audit.md` output).
- Issue / backlog.
- Past decisions (decisions directory or equivalent).

If these artifacts don't exist, recommend creating them in the first 2–4 weeks.

### Step 13 — Run the "unknown reader" test

Re-read the document assuming you are a mid-level engineer who has never seen this code. Mark every sentence that requires unstated context; either explain or cut. The document fails its purpose if it requires knowing what the author knows.

### Step 14 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Address the new engineer directly.
- Explicitly separate what works (high confidence) from what's fragile (low confidence).
- Flag AI-generated risk areas.
- Provide a specific, low-risk first task.
- Include an honest open-questions / unknowns section.
- Run the unknown-reader test before delivering.

### Must Not
- Claim confidence the author doesn't have.
- Hide known fragility or divergence.
- Use insider shorthand or unexplained names.
- Produce a pure marketing summary. The handoff exists to transfer context, not to impress.
- Recommend the new engineer "just talk to me if they have questions" as the support plan. Write the briefing so they don't need to.
- Skip the don't-touch-yet section if fragile areas exist.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Inherit the author's confidence about fragile areas. If the author isn't sure, the briefing says "confidence: low" or "unknown."
- Let the happy-path description skip error modes. A feature that works when everything is well is a "works if optimistic" note, not an unreserved "works."
- Claim tests cover a flow unless you've named the test and verified it's not trivially self-confirming.
- Bury the don't-touch-yet list at the bottom. It belongs near the top, right after what-works.
- Skip deployment posture because "it's obvious." If alerting / secrets / on-call are missing, the new engineer must know.

✅ **DO:**
- Write fragility notes with the specific function / file / line where possible.
- Use "I haven't verified X" freely. Honesty accelerates takeover.
- Name external dependencies explicitly: which service, which endpoint, which region, which rate limit.
- Flag patterns the author is aware are non-idiomatic, especially if AI-generated.
- Pair each fragile area with the rules-file entry (if one exists) meant to prevent similar issues.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Briefing reads well but hides fragility; new engineer changes something in a "works" zone that is actually fragile; regression ships.

❌ **UNHELPFUL failure:** Briefing is 40 pages of every detail, and the new engineer never reads it; first task is undertaken on no context; same outcome as no briefing.

✅ **Quality check:** A mid-level engineer with the stated experience can, after reading, answer: "What does this do? What do I trust? What don't I trust? What should I pick up first? What should I leave alone?" without asking the original author.

---

## Output Format

```markdown
# Handoff Briefing — [Project]

> For the new engineer taking this over. Read this before opening the repo.

## 1. What This Project Is
[2–5 sentences, operational.]

## 2. Intended vs Actual
| Area | Intended | Actual | How we know |
|------|----------|--------|-------------|
| | | | |

## 3. What Works (confidence: high)
- [Feature / flow] — [file / module] — verify with: [command / test / URL]

## 4. What's Fragile (confidence: low)
- [Area] — [why suspect] — [what breaks if touched naively] — [workarounds]

## 5. Don't Touch Yet (first 2 weeks)
- [Area] — [reason]

## 6. AI-Generated Risk Areas
- [Module / file] — [risk] — [audit status]

## 7. How to Run It
[Setup, env, commands, gotchas.]

## 8. Deployment and Operational Posture
- Runs: 
- Deployer: 
- Secrets: 
- Alerting: 
- On-call: 

## 9. First Task
- Task: 
- Why it's a good first: 
- Acceptance: 
- Reviewer: 

## 10. Open Questions and Unknowns
- [Specific, honest items.]

## 11. Artifacts
- Rules file: [path]
- Memory / architecture / state: [path]
- Security audit: [path or "not yet run — recommend running in week 1"]
- Decisions: [path]

## 12. Who to Ask When Stuck
- [Author contact; scope of availability]
- [Other humans who know parts]
- [What's genuinely not known by anyone — and that's OK]
```

---

## Verification

- [ ] Document addresses the new engineer directly.
- [ ] Section 2 table exists and is honest.
- [ ] What-works and what's-fragile are separated with confidence labels.
- [ ] AI-generated risk areas flagged.
- [ ] First task is low-risk, off fragile zones, with acceptance.
- [ ] Don't-touch-yet section has specific reasons per entry.
- [ ] Open questions include things the author doesn't know.
- [ ] Unknown-reader test run; insider shorthand removed.
- [ ] Artifacts pointed to, not embedded.
- [ ] No marketing language.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a context-transfer briefing for a specific reader — the new engineer.
- **ST-02 (Structured Sequential Instructions):** Fourteen steps force purpose → divergence table → works → fragile → AI risk → ops → first task → don't-touch → unknowns → artifacts → unknown-reader test → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids hidden fragility, insider shorthand, and "just ask me" support plans.
- **DS-01 (Framework Application):** Eleven-section structure is the framework; ordering puts don't-touch and fragile near the top where a new engineer actually reads.
- **RT-07 (Cascade Effect Analysis):** Separating "works" from "fragile" prevents the cascade where the new engineer touches something that looked working and wasn't.
- **QA-01 (Self-Verification):** Unknown-reader test + verification checklist catch insider shorthand and hidden gaps before the new engineer is handed the doc.
