# Proposed Additions to MASTER_TECHNIQUE_INDEX.md

Five techniques harvested from the Fable prompt batch (PR-review, prioritization, sunk-cost,
DoD/AC, concurrency audit). Each was independently invented by a separate prompt and is
reusable well beyond its origin. **IDs below are provisional** — assign final numbers against
the live index to avoid collisions; suggested family placement is given for each.

A unifying observation ties four of the five together and belongs in the index preamble:

> **Negative-space accounting.** A rigorous analysis is judged as much by what it makes
> visible about its *own limits* as by its findings. Four of these five techniques are tools
> for surfacing negative space — what was checked and cleared, what could not be verified,
> what was deliberately excluded, and how trustworthy each input is — so that every omission
> is a recorded decision rather than a silent gap. Prefer whichever instance fits the task.

---

## 1. Partial-Visibility Question Tier
**Suggested ID:** QA-21 (Self-Verification family) · **Origin:** PR diff review

**What it is.** When an analysis runs on incomplete context (a diff without its callers, a
snippet without its callees, a plan without a named alternative), any finding that depends on
the unseen part is emitted as an explicit **Question** — a named item stating exactly what to
check and what answer would flip the conclusion — never as an asserted finding and never
silently dropped.

**When to use.** Any prompt that analyzes a fragment of a larger system: code review,
security review of pasted code, architecture review of a partial design, decision audits
where a key input is unknown.

**How to apply.**
- Give incomplete-context findings their own output tier, separate from confirmed findings.
- Each Question names (a) the specific thing to verify and (b) the answer that changes the verdict.
- Confidence is capped: a concern that exists *only if* unseen code behaves a certain way can
  never be a top-severity (Blocking) finding.

**Example.** "Q2. Is there an index on `(created_at, id)`? Schema isn't in the diff. If it
exists, no action; if not, keyset pagination degrades to a full scan — becomes Blocking."

**Guards against.** Both the false positive (asserting a bug in code you can't see) and the
false negative (silently ignoring a real risk because it wasn't fully visible).

---

## 2. Input Provenance Tagging (+ sensitivity-on-guesses, + constraint Overrides)
**Suggested ID:** EV-10 (Evidence Requirements family) · **Origin:** prioritization framework selector

**What it is.** Every input to a computed result is tagged by source — `[data]` (supplied or
cited), `[estimate]` (reasoned from supplied facts), `[guess]` (invented to proceed) — guesses
are counted per row, and output precision is rounded to input quality (no three-decimal scores
built on guesses). Two companion rules travel with it:
- **Sensitivity on the consequential guesses:** for the top results only, test whether a
  plausible alternative value for a guessed input changes the *tier*, and state the flip
  condition ("Export becomes #1 if Impact ≥ 1.7").
- **Constraint Overrides lane:** hard constraints a scoring model has no field for (deadlines,
  dependencies, contractual obligations) ride in a visible section *above* the scored output —
  never silently absorbed into or buried by the score.

**When to use.** Any prompt that emits computed numbers or rankings: MCDA, market sizing
(TAM/SAM/SOM), unit economics (LTV/CAC), risk scoring, effort estimation, forecasting.

**How to apply.** Tag at write-time in the scoring table; total guesses per row; add a
sensitivity block for the top N; keep an Overrides section that outranks the ranking.

**Guards against.** A guess laundering itself into fact by sitting in a table next to real
data; false precision; a framework's blind spot burying a real constraint.

---

## 3. Two-Axis Verdict — Decouple the Answer from the Reasoning
**Suggested ID:** OC-07 (Output Specification family) · **Origin:** sunk-cost audit (and the severity×confidence split in PR review)

**What it is.** The output reports **two independent axes** and never collapses them: (axis 1)
the substantive answer, and (axis 2) a meta-quality dimension about that answer. The recurring
insight is that *the conclusion can be right even when a stated reason is wrong* — so the
prompt fixes the reasoning and keeps the conclusion, saying so plainly.

Instances across the batch:
- PR review: finding **severity** × **confidence** in the finding.
- Prioritization: the **rank** × the **provenance** of its inputs.
- Sunk-cost: which way the **forward case** points × whether the **stated reasoning** is distorted.

**When to use.** Any audit or evaluation where "your reasoning is flawed" and "your conclusion
is wrong" are separable — most of them.

**How to apply.** Define the two axes up front; report both for every finding/verdict; add the
explicit rule that a correct conclusion reached by a bad argument is flagged on axis 2 while
axis 1 stands.

**Guards against.** Conflating a bad argument with a bad decision (and vice versa) — the most
common error in bias-audit and review outputs.

---

## 4. Exhaustive Sweep with a Proportionality Budget
**Suggested ID:** DS-07 (Scope Management family) · **Origin:** Definition-of-Done / acceptance-criteria builder

**What it is.** Two opposing forces held in deliberate tension: (a) a **mandatory sweep** of
every category that could matter (for DoD: empty states, errors, loading, edge volumes, a11y,
perf, security, platform, l10n, observability, data integrity), where each category must be
marked *Applicable → item* or **N/A → one-word reason**; and (b) a **hard budget** sized to the
task (quick fix 3–6, standard 6–12, feature ≤15; above → split), with any demotion named rather
than silent. Completeness and proportionality check each other.

**When to use.** Any checklist/spec/audit prompt at risk of *either* missing categories *or*
gold-plating: security review, a11y audit, test-coverage design, resilience audit, spec authoring.

**How to apply.** Publish the category list; force an Applicable/N-A mark on each; cap the
included set by a size-based budget; when over budget, demote/cut and name what was dropped.

**Companion rule — N/A requires a reason.** A silent "not applicable" is how empty states get
forgotten; every excluded category carries a one-word justification.

**Guards against.** Both the forgotten-edge-case incident and the thirty-criterion fortress
that trains a team to ignore the document.

---

## 5. Dismissed-Candidates Coverage Table (+ adjacent-prompt scope fencing)
**Suggested ID:** SV-09 (Self-Verification family) · **Origin:** concurrency correctness audit

**What it is.** The audit reports not only confirmed findings but a **Dismissed** table: each
candidate that looked like a defect, why it looked wrong, the **guard that cleared it (with
location)**, and any hardening worth adding. This proves the audit actually checked, and it
flags fragile implicit guards worth documenting. It pairs with two rules the same prompt models:
- **No finding without concrete evidence in the domain's currency** — here, a schedulable
  step-numbered interleaving ending in a violated invariant; "this looks unsynchronized" is a
  candidate, not a finding. (The domain-general form is the house-style *evidence-or-drop* move.)
- **Adjacent-prompt scope fencing** — when a sibling prompt owns a neighboring concern
  (here, concurrency *performance* vs *correctness*), the prompt fences itself off explicitly in
  objective, constraints, and routing, so the two don't overlap. Reusable across any
  near-neighbor pair in a large library.

**When to use.** Any audit prompt (security, a11y, resilience, concurrency); the fencing rule
applies whenever a prompt has a close sibling.

**How to apply.** Emit a Dismissed table alongside findings; require a located guard per
dismissal; require domain-appropriate concrete evidence per confirmed finding; add explicit
scope-boundary statements against the sibling prompt.

**Guards against.** Audits that look thorough but only report positives; a confident "all
clear" over code whose guards were never actually checked; silent overlap with a sibling prompt.

---

## Final-assignment checklist (for whoever ingests)
- [ ] Replace provisional IDs with real ones against the live index; check for collisions.
- [ ] Add the "Negative-space accounting" note to the index preamble or the relevant family header.
- [ ] Add each technique to the family tables and the Quick-Reference-by-Use-Case section.
- [ ] Cross-reference the exemplar prompt in each entry once the batch is ingested.
