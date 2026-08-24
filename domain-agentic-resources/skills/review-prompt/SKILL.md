---
name: review-prompt
description: Review a reusable prompt the way a rigorous senior prompt engineer would — find its real weaknesses, separate blocking gaps from nitpicks, give the minimal fix for each, and end with a clear verdict. Use when a prompt needs a pre-ship review, when a prompt produces inconsistent or hallucinated output, or when authoring a new prompt and wanting a pre-ship pass. Not for creative/open-ended prompts, multi-turn system prompts, or agentic/tool-use prompts (see "When NOT to use").
metadata:
  tags:
    - prompt-engineering
    - review
    - quality
    - authoring
    - critique
  updated: "2026-07-08"
---

# Review Prompt

**Objective:** Review a reusable prompt as a senior prompt engineer would — surface its real weaknesses, separate **blocking** gaps (which change *what findings a run produces*) from **minor** ones (which change only *how findings are presented*), give the smallest fix for each, and end with a verdict. A clean prompt gets a clean verdict; do not manufacture issues.

## When to use
- A reusable prompt needs a pre-ship review.
- A running prompt produces inconsistent, hallucinated, or unusable output and you want the cause.
- You just authored a prompt and want a rigorous second pass before shipping.

## When NOT to use (scope boundary)
Tuned for **task prompts with checkable inputs** (review, analysis, transformation). It misleads or wastes effort on:
- **Creative / open-ended prompts** — the stability test (step 3) would "fix" latitude that is the point.
- **Multi-turn or system prompts** — a single-shot dry-run (step 1) doesn't represent emergent behavior.
- **Prompts already near the quality ceiling** — only empirical A/B evals can rank variants; more verbal review is noise.
- **Agentic / tool-use prompts** — the binding constraints are tool schemas and environment, not prose.
- **Prompts feeding pipelines with cheap downstream validation** — some underspecification is harmless there.

## Inputs
1. **The prompt under review (required)** — wrapped in `<prompt-under-review>…</prompt-under-review>`.
2. **Intended use (optional)** — who runs it, on what input, to produce what. If absent, infer and label the inference.

## The method (run in order)

1. **Dry-run before judging (first-invented-fact test).** Try to write the first sentence of the output the prompt demands. **The first fact you must invent to proceed is the first blocking gap.**
2. **Decompose into verb–object pairs** ("check endpoints," "make sure fast," "give list") and mark each **verifiable / partial / unverifiable** from the stated input. Any "make sure X" where X is not observable → blocking (it forces speculation, i.e. hallucinated findings).
3. **Stability-test every evaluative term (two-executor divergence test).** For "best practices," "important," "good," ask: *would two competent executors select materially the same things?* Verify by writing down two divergent readings before asserting the flaw. Diverge → underspecified → blocking.
4. **Scan for fabrication pressure, then the counterweight (pressure-minus-counterweight rule).** Presupposed findings ("tell them what's wrong") and volume rewards ("check everything") are flaws **only when no honesty valve exists** (evidence requirement, permission to pass, severity gate). Pressure without a counterweight → blocking.
5. **Check the output contract:** format, per-item fields, ordering criterion, stopping rule. Absent → blocking; present but ambiguous → minor.
6. **Triage with one rule (findings-vs-presentation triage):** a flaw is **blocking iff it changes *which findings exist*** (input contract, verifiability, rubric, incentives); **minor iff it only changes *how findings are presented*** (format, ordering, verdict wording).
7. **Gate every criticism (quote-and-consequence).** Keep a criticism only with a verbatim quote of the offending words **and** the concrete bad output they cause. If you can't produce both, cut or merge it.
8. **Write each fix as the smallest edit** — a replacement sentence or one added line. If a fix demands restructuring, the flaw is probably mislocalized; return to step 6.
9. **Close with what's sound**, so "checked and fine" is distinguishable from "not checked."

## Output format
```
# Review: [prompt name]

**Verdict:** [SHIP AS-IS | SHIP AFTER BLOCKING FIXES | REWORK] — [one line]

## Blocking (changes which findings a run produces)
### B1. [title]
- Quote: "[verbatim offending words]"
- Bad output it causes: [concrete failure]
- Fix: [smallest edit]

## Minor (changes only how findings are presented)
- M1. [quote → fix, one line each]

## What's sound
- [what to keep — 1–3 lines]
```

## Verification (before returning)
- [ ] Every Blocking item changes *which findings exist*, not just presentation (step 6 applied).
- [ ] Every criticism carries a verbatim quote + the concrete bad output (step 7).
- [ ] Each fix is a minimal edit, not a rewrite (step 8).
- [ ] A genuinely clean prompt received a clean verdict — no manufactured issues.
- [ ] If the target is creative / multi-turn / agentic / near-ceiling, the review said so and stopped.

## Related
- `domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md` — checklist-driven audit of a single prompt's spec gaps (complements this procedure; that audits coverage, this is the reviewer's method).
- `PROMPT_QUALITY_STANDARDS.md` — the Tier-1 bar a reviewed prompt should meet.
