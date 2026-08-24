---
title: "Testable Problem-Hypothesis Sharpener"
category: startup/marketing
description: "Turn a vague problem observation into a sharp, falsifiable hypothesis and a customer-discovery plan built on past-behavior questions, with adversarial disconfirmation built in to fight confirmation bias."
techniques:
  - RT-02
  - DS-02
  - QA-12
  - DS-06
  - NE-02
difficulty: beginner
tags:
  - hypothesis
  - problem-validation
  - customer-discovery
  - idea-stage
  - startup
updated: "2026-06-19"
related_prompts:
  - domain-business-strategy/startup/startup_ai_native_lifecycle_navigator.md
  - domain-business-strategy/startup/startup_pmf_pivot_diagnostic.md
  - domain-idea-to-product/orchestrator_idea_to_product.md
---

# Testable Problem-Hypothesis Sharpener

**Objective:** Convert a fuzzy "this is annoying / takes too long" observation into a specific, falsifiable problem hypothesis, then design a customer-discovery plan — a precise interviewee profile plus a past-behavior interview guide — and bake in adversarial disconfirmation so the founder tests the hypothesis rather than confirming a hope.

**When to Use:**
- You have a problem hunch and want to test it before building anything.
- Your "validation" so far is enthusiasm and a few "yeah, I'd use that" replies.
- You are about to talk to potential customers and want to ask the right questions.

**When NOT to Use:**
- The problem is already validated with strong past-behavior evidence and you are choosing a business model (use the lifecycle navigator or product pipeline).
- You need full product-market-fit or pivot diagnosis post-launch (use `startup_pmf_pivot_diagnostic.md`).

**Source:** Frameworks and figures are drawn from a vendor report, Anthropic's *The Founder's Playbook: Building an AI-Native Startup* (2026) — attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the output degrades gracefully if some are missing:
- **The raw observation** — the problem as you currently phrase it.
- **Who you think has it** — any sense of the affected people or organizations.
- **Current behavior** — what those people do about the problem today (workarounds, tools, spend).
- **Your bias risk** — are you emotionally attached to a particular solution?
- **Access** — who you can realistically reach to interview.

## Constraints

**Must:**
- Rewrite the observation into a falsifiable hypothesis naming WHO, HOW OFTEN, HOW SEVERELY, and WHAT THEY CURRENTLY DO.
- Build the interview guide from past-behavior questions, not future-hypotheticals.
- Include an adversarial step that argues against the hypothesis and seeks disconfirming evidence.

**Must Not:**
- Leave the hypothesis unfalsifiable ("people want better X") with no measurable claim.
- Include leading, future-facing, too-broad, or socially-desirable questions without flagging and rewriting them.
- Let an evidence asymmetry pass unexamined as if support automatically means truth.

**Instructions:**

1. **Sharpen the hypothesis.** Rewrite "X takes too long / is annoying" into a specific, falsifiable claim naming WHO experiences it, HOW OFTEN, HOW SEVERELY, and WHAT THEY CURRENTLY DO about it. Example: "Contract review takes too long" → "In-house legal teams at mid-market companies spend 3+ days per contract-review cycle because redlines are managed across email threads rather than a single version-controlled document."

2. **Define WHO to talk to.** Produce a precise target profile (job titles, company types, team structures, seniority) — a sharp profile beats a long contact list. Prioritize interviewees by closeness to the problem.

3. **Design WHAT to ask.** Build past-behavior questions, not future-hypotheticals: "Tell me about the last time you dealt with this," NOT "Would you use something like this?" Have the AI flag any leading, future-facing, too-broad, or socially-desirable questions and rewrite them, and design follow-up probes that dig into the most recent concrete instance.

4. **Build per-persona question sets.** If more than one persona is in scope, tailor a question set per persona so each line of inquiry matches that persona's actual workflow.

5. **Set the synthesis cadence.** After every 5 interviews, produce two lists — evidence SUPPORTING vs. evidence CHALLENGING the hypothesis. The report's warning is load-bearing: if support far outweighs challenge, check whether that asymmetry is in the data or in your hopes — confirmation bias "now comes with a research engine."

6. **Run adversarial disconfirmation.** Ask the AI to argue AGAINST the hypothesis and actively surface disconfirming evidence and alternative explanations for what you have heard so far.

**Output Format:**

A markdown discovery kit:
- **Sharpened Hypothesis** — the falsifiable claim with WHO / HOW OFTEN / HOW SEVERELY / CURRENT BEHAVIOR
- **Target Interviewee Profile** — titles, company types, team structures, prioritized by closeness
- **Past-Behavior Interview Guide** — questions + follow-up probes, with leading/future/broad questions flagged and rewritten
- **5-Interview Synthesis Template** — supporting vs. challenging evidence lists + bias check
- **Adversarial Brief** — the strongest case against the hypothesis

## Verification

- [ ] The hypothesis is falsifiable and names WHO, HOW OFTEN, HOW SEVERELY, and CURRENT BEHAVIOR.
- [ ] The interviewee profile is specific (not "people in legal") and prioritized by closeness to the problem.
- [ ] Every interview question is past-behavior; future-hypotheticals are flagged and rewritten.
- [ ] The synthesis template forces a supporting/challenging split plus a bias check.
- [ ] An adversarial brief argues against the hypothesis.

## False-Positive Prevention

❌ **DON'T:**
- Accept "would you use this?" answers as evidence — people are agreeable about hypotheticals.
- Call a hypothesis tested because 5 friendly contacts nodded along.
- Read a one-sided evidence list as confirmation without asking if you steered the questions.
- Define the target as a broad category that lets you count almost anyone as validation.

✅ **DO:**
- Anchor every question in the last concrete instance of the behavior.
- Treat a lopsided supporting/challenging split as a prompt to re-examine your questions and your hopes.
- Force the AI to build the disconfirming case, not just the supporting one.
- Make the target profile narrow enough that a "no" actually counts.

## Example Output

```markdown
## Discovery Kit: Contract-Review Friction

### Sharpened Hypothesis
In-house legal teams at mid-market companies (200–2,000 employees) run 3+ day contract-review cycles, several times per week, because redlines move across email threads rather than one version-controlled document — costing rework and missed deadlines.

### Target Interviewee Profile
- In-house counsel / legal ops leads at mid-market companies (closest to the problem — interview first)
- Paralegals who manage redline threads (high frequency, ground-truth behavior)
- (Lower priority) outside-counsel contacts — adjacent, not the buyer

### Past-Behavior Interview Guide
- "Walk me through the last contract you reviewed end to end." → probe: where did versions live? how many threads?
- "When did a redline last get lost or duplicated? What happened?"
- FLAGGED (future-hypothetical): "Would you use a version-controlled redline tool?" → REWRITTEN: "Last time versions got tangled, what did you do to untangle them?"
- FLAGGED (leading): "Isn't email a terrible way to manage redlines?" → REWRITTEN: "How do you currently keep track of which redline is current?"

### 5-Interview Synthesis Template
| Supporting | Challenging |
|---|---|
| 4/5 described multi-day cycles | 2/5 already use a contract tool and don't feel the pain |
| 3/5 lost a redline in last month | 1/5 says email is fine at their volume |
Bias check: support skewed because I led with the email question in interviews 1–2. Re-run neutral.

### Adversarial Brief
Strongest case against: the real bottleneck may be approval latency, not version control — two interviewees waited days on a signer, not on redlines. Test whether the pain is tooling or workflow before building.
```

**Techniques Used:**
- **RT-02 (Role-Based Expertise):** reasons as a customer-discovery coach.
- **DS-02 (Specificity & Detail Enforcement):** forces the hypothesis and target profile to be concrete and falsifiable.
- **QA-12 (False Positives Identification):** flags leading/hypothetical questions and confirmation-biased synthesis.
- **DS-06 (Prioritization & Severity Guidance):** prioritizes interviewees by closeness to the problem.
- **NE-02 (Adversarial / Devil's-Advocate Framing):** the disconfirmation step argues against the hypothesis.

**Related Prompts:**
- `startup_ai_native_lifecycle_navigator.md` — where this fits in the broader founder lifecycle.
- `startup_pmf_pivot_diagnostic.md` — diagnose product-market fit and pivots after launch.
- `domain-idea-to-product/orchestrator_idea_to_product.md` — carry a validated hypothesis into the product pipeline.
