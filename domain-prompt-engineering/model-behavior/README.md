# Model Behavior Diagnostics

**Purpose:** Diagnose and correct how a specific model (Claude, GPT, Gemini, or another instruction-following LLM) actually behaves versus how you intended it to behave. These prompts sit between the prompt and the model — they treat the prompt's behavior as a first-class object and help you fix it.

**When to use this subfolder:**
- You wrote a prompt, the model is not doing what you asked, and you want to fix the *right* thing — not just rewrite the whole prompt.
- A model is drifting mid-conversation and you want to correct it now and preserve the correction for next time.
- You have an existing system prompt that is fighting the model's base training and needs to be refactored, not replaced.
- You're building a new system prompt and want it to cooperate with the model's base tendencies from the start.

**When not to use:**
- The output is low-quality but no specific instruction was violated. That's a quality critique, not a behavior diagnosis — use a prompt-improvement or correctness prompt instead.
- You want to escape the model's *default opinion* on a topic (as opposed to the default shape of its output). Use `escape-median/` for that.
- You need to decide whether AI is the right tool for the task. Use `goal-orientation/` for that.

---

## Prompts

| File | Use when... |
|------|-------------|
| `modelbehavior_instruction_deviation_diagnostic.md` | A specific instruction in your prompt is not being followed and you need to locate the root cause (instruction conflict, ambiguity, specification gap, context crowding, base-model prior, etc.) before fixing. |
| `modelbehavior_active_coaching_in_session.md` | The model is drifting in a live conversation, you don't want to lose session context, and you want to correct behavior *and* capture the correction for next time. |
| `modelbehavior_refactor_system_prompt.md` | You have an existing system prompt that mostly works but produces persistent drift. You want to keep the logic but stop fighting the model's base training. |
| `modelbehavior_system_prompt_from_scratch.md` | You're authoring a new system prompt and want to start from principles + ranked operational rules rather than a rough draft you patch over time. |

---

## How the prompts chain

Typical workflow when debugging a misbehaving production prompt:

1. **Diagnose** the specific deviation (`modelbehavior_instruction_deviation_diagnostic.md`).
2. If it's a live session, **coach in-session** (`modelbehavior_active_coaching_in_session.md`) and persist the rule.
3. If the diagnosis shows the prompt is fighting the model systemically, **refactor** the whole system prompt (`modelbehavior_refactor_system_prompt.md`).
4. If the prompt is past refactor, **rebuild from scratch** with principle-first design (`modelbehavior_system_prompt_from_scratch.md`).

Most behavior problems are resolved at step 1 or 2. Steps 3 and 4 are for accumulated drift.

---

## Design principles shared across these prompts

- **Require real artifacts, not hypotheticals.** These are diagnostic prompts — they refuse to run on imagined misbehavior. Supply the actual prompt and actual output.
- **Root cause over symptom.** Each prompt names *where* the deviation originated before proposing a fix. A fix that doesn't target the cause produces new drift elsewhere.
- **Falsifiable tests after the fix.** Every prompt ends with an observable post-fix check. If the check fails, the diagnosis was wrong — don't stack more fixes on a wrong diagnosis.
- **Model family matters.** Every prompt asks for the target model and version. Base-training tendencies differ, and a fix tuned for one family may not transfer to another.

---

## Related

- `domain-prompt-engineering/escape-median/` — for steering the model off its default *position* on a topic (complementary; different failure mode).
- `domain-prompt-engineering/prompt-improvement/` — for general prompt quality improvement when no specific behavior is the target.
- `domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md` — for authoring the broader CLAUDE.md that persistent rules live inside.
