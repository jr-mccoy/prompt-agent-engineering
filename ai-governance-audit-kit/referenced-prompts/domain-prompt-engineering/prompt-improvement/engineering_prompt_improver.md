---
title: "Engineering Prompt Improver"
category: prompt-engineering/prompt-improvement
description: "Transform a vague engineering-focused prompt into a specific, well-structured one — diagnosing clarity/structure/specification gaps, applying an enhancement framework, and producing an improved prompt with explained changes, platform tips, and a verification test."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - prompt-improvement
  - prompt-engineering
  - specification
  - output-format
  - code-prompts
updated: "2026-06-07"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
---

# Engineering Prompt Improver

**Objective:** Transform a vague or underperforming engineering prompt into a specific, well-structured one that reliably produces the output the user needs.

**When to use:**
- Your AI prompts for code review, architecture analysis, or technical documentation aren't giving you the outputs you need.
- A prompt produces inconsistent results across runs and you want to stabilize it.
- You have a one-line ask and want to turn it into a self-contained, specified prompt.
- You want to learn *why* a prompt underperforms, not just get a rewrite.

**When NOT to use:**
- The prompt already works reliably and you only need minor wording tweaks.
- The task is non-technical — use `promptcraft_rewrite_vague_ask.md` or a domain-specific improver.
- You need a full specification/eval harness — use `correctness_prompt_specification_audit.md`.

**Audience:** Developers, engineers, and technical writers who prompt LLMs for coding and technical tasks.

---

## Inputs / Context

Supply the following. Paste your current prompt wrapped in an `<original_prompt>` tag so it can be referenced by name; improve only what is supplied and ask for the intended outcome if it is missing.

- **Original Prompt:** the current prompt, exactly as written.
- **Intended Outcome:** what you want the AI to produce.
- **Target Platform:** ChatGPT / Claude / Gemini / other.
- **What's Not Working:** the current issues with responses (vague, inconsistent, missing edge cases, etc.).

---

## Constraints

### Must
- Diagnose concrete gaps before rewriting: name a clarity issue, a structure issue, and a specification issue.
- Ground improvements in established prompt-engineering practice (explicit context, structured instructions, output specification, success criteria); name the technique applied.
- Produce a **self-contained** improved prompt — runnable without the surrounding conversation.
- Specify exact **output format**, **constraints**, and **success criteria** in the rewrite.
- Preserve the user's original intent and target platform; do not silently change the task.

### Must Not
- Do not return a rewrite without explaining what changed and why.
- Do not add requirements the user did not ask for (scope creep) — surface them as optional instead.
- Do not produce a longer prompt that is no clearer; length is not the goal.
- Do not fabricate platform behaviors or capabilities you cannot support.

---

## Instructions

### Step 1 — Prompt Analysis
Identify three concrete issues with the current prompt:
1. **Clarity issue:** what is ambiguous or undefined.
2. **Structure issue:** what is disorganized (context mixed with instructions, no steps, no headers).
3. **Specification issue:** what is missing (language, format, constraints, examples, success criteria).

### Step 2 — Apply the Enhancement Framework
Transform the prompt using:
- **A. Add clear structure** — separate context from instructions; numbered steps for complex tasks; section headers.
- **B. Specify output requirements** — exact format, length constraints, style/tone.
- **C. Include helpful context** — background, examples of good output, constraints to honor.
- **D. Clarify success criteria** — what makes a good response, what to avoid, quality indicators.

### Step 3 — Create the Enhanced Version
Write the improved prompt with clear section divisions, a specific output format, step-by-step instructions (if needed), and explicit success criteria.

### Step 4 — Explain Key Changes
List the top 5 improvements: **Change → Impact** for each.

### Step 5 — Provide Usage Tips
Give 3 tips: platform-specific best practices, how to customize further, and common variations to try.

### Step 6 — Self-Check (verification)
Before delivering, confirm the rewrite is self-contained, preserves intent, specifies output format and success criteria, and is genuinely clearer than the original.

---

## False-Positive Prevention

❌ **DON'T:**
- Hand back a rewrite with no diagnosis of what was actually wrong.
- Pad the prompt with boilerplate ("be thorough, be helpful") that adds no specification.
- Quietly expand the task scope beyond what the user requested.
- Invent platform-specific tricks or model capabilities you can't substantiate.
- Optimize for length or formality instead of clarity and testability.

✅ **DO:**
- Name the specific clarity, structure, and specification gaps you found.
- Apply named prompt-engineering techniques and explain each change's impact.
- Keep the rewrite self-contained, intent-preserving, and testable.
- Mark genuinely-useful additions the user didn't request as optional.
- Provide a concrete before/after verification test so the user can confirm improvement.

---

## Output Format

Present the response as:
- **Issues with Original Prompt** (clarity / structure / specification)
- **Enhanced Prompt** (clearly formatted, self-contained)
- **Key Improvements Explained** (top 5, Change → Impact)
- **Platform-Specific Tips**
- **Quick Test to Verify Improvement** (before/after comparison)
- **Customization Tips**

---

## Example Output

```markdown
## Prompt Improvement Analysis

### Original Prompt
```
Write a function to validate emails
```

### Intended Outcome
A robust email validation function for a Node.js signup form

### Target Platform
Claude

### What's Not Working
- Getting overly simple regex that misses edge cases
- No error handling
- Different responses each time

---

### Issues with Original Prompt

1. **Clarity Issue:** "validate emails" is ambiguous - RFC 5322 compliance? Basic format? DNS verification?
2. **Structure Issue:** Single sentence with no context about use case, language, or constraints
3. **Specification Issue:** Missing: language, framework, what constitutes "valid", error handling expectations, examples

---

### Enhanced Prompt

```markdown
## Task: Create Email Validation Function

### Context
I'm building a user registration system in Node.js/TypeScript for a B2B SaaS application. I need a robust email validation function that will be used in the signup form.

### Requirements
Create an email validation function with these characteristics:

**Validation Rules:**
1. Must follow basic RFC 5322 format (local@domain)
2. Must have valid TLD (no made-up extensions)
3. Must not allow disposable email domains (mailinator, tempmail, etc.)
4. Should handle plus addressing (user+tag@example.com)

**Technical Requirements:**
- Language: TypeScript
- No external dependencies (must work offline)
- Return detailed error messages, not just true/false
- Handle edge cases gracefully

**Input/Output Spec:**
```typescript
interface ValidationResult {
  isValid: boolean;
  email: string;         // Normalized email (lowercase, trimmed)
  errors: string[];      // List of validation failures
  suggestions?: string;  // Optional fix suggestions
}

function validateEmail(input: string): ValidationResult;
```

### Examples

**Valid Inputs:**
- `user@example.com` → valid
- `user.name+tag@company.co.uk` → valid
- `  User@Example.COM  ` → valid (normalized to user@example.com)

**Invalid Inputs:**
- `user@mailinator.com` → invalid: "Disposable email addresses not allowed"
- `user@.com` → invalid: "Invalid domain format"
- `user@example` → invalid: "Missing or invalid TLD"
- `@example.com` → invalid: "Missing local part"

### Output Format
Provide:
1. The TypeScript function with inline comments
2. A list of disposable domains to block (top 20)
3. Unit test examples covering edge cases
4. Brief explanation of regex pattern used

### Constraints
- Do NOT use external validation libraries
- Do NOT make network calls (no DNS/MX lookups)
- MUST be synchronous (no async)
```

---

### Key Improvements Explained

| # | Change | Impact |
|---|--------|--------|
| 1 | Added explicit context (B2B SaaS, signup form) | AI understands real-world constraints |
| 2 | Specified TypeScript interface for return type | Gets exact output format needed |
| 3 | Listed specific validation rules with priorities | No ambiguity about "valid" definition |
| 4 | Provided concrete examples (valid + invalid) | AI can test against expected behavior |
| 5 | Added explicit constraints (no deps, sync) | Prevents solutions that won't work |

---

### Platform-Specific Tips

**For Claude:**
- Use XML-like section headers for better parsing
- Include TypeScript interfaces - Claude excels at typed code
- "Brief explanation" prompts better than "explain everything"

**For ChatGPT:**
- Add "Think step by step" for complex logic
- Use numbered lists instead of nested bullets
- Explicitly say "don't apologize or add disclaimers"

**For Gemini:**
- Include more examples (3-5 each category)
- Be more explicit about output structure
- Add "Be concise" to avoid verbosity

---

### Quick Test to Verify Improvement

Run both prompts and compare:

| Criteria | Original | Enhanced |
|----------|----------|----------|
| Handles plus addressing? | ❓ Maybe | ✓ Yes |
| Blocks disposable emails? | ❌ No | ✓ Yes |
| Returns structured errors? | ❌ No | ✓ Yes |
| Includes test cases? | ❌ No | ✓ Yes |
| Consistent across runs? | ❌ No | ✓ Yes |

---

### Customization Tips

**For stricter validation:** Add MX record checking requirement
```markdown
Add async variant that performs DNS MX lookup to verify domain accepts email
```

**For internationalization:** Specify Unicode support
```markdown
Must support internationalized email addresses (RFC 6531) with Unicode local parts
```

**For different languages:** Replace TypeScript section
```markdown
**Technical Requirements:**
- Language: Python 3.10+
- Use dataclasses for return type
- Include type hints
```
```

---

## Verification

- [ ] Three concrete issues (clarity, structure, specification) named before the rewrite.
- [ ] Enhanced prompt is self-contained and preserves the original intent and platform.
- [ ] Output format, constraints, and success criteria are explicit in the rewrite.
- [ ] Top-5 changes explained as Change → Impact.
- [ ] Platform-specific tips and a before/after verification test included.
- [ ] No unrequested scope creep (optional additions marked as optional).
- [ ] The rewrite is genuinely clearer, not merely longer.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Forces the improved prompt to open with a single, unambiguous objective.
- **ST-02 (Structured Sequential Instructions):** Applies a numbered diagnose → enhance → explain → verify workflow.
- **DS-02 (Evidence-Based Standards):** Grounds changes in established prompt-engineering practice rather than ad-hoc wording.
- **CM-01 (Explicit Context Framing):** Separates context from instructions and injects the missing background the model needs.
- **QA-01 (Self-Verification):** Built-in self-check and a before/after verification test confirm the improvement.

---

## Related Prompts

- `domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md` — sharpens a single vague instruction so the model can't default.
- `domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md` — audits a prompt for specification gaps at greater depth.
- `domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md` — rewrites a vague chat opener into a self-contained prompt (general-purpose).
