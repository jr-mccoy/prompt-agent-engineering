# Evaluation — Adversarial

**Purpose:** Red-team test sets, injection probes, and bypass ladders for measuring model robustness against adversarial inputs.

Use these prompts to build test sets that actively try to break a system — jailbreaks, persona attacks, data exfiltration attempts, prompt injections, and refusal bypasses. Each prompt produces structured, machine-testable cases with binary pass/fail rules.

---

## Prompt Catalog

| File | What it does |
|------|--------------|
| `adv_jailbreak_corpus_builder.md` | Assemble a categorized jailbreak test corpus — taxonomy, severity, attack vector, reproduction phrasing — for red-team evaluation of a system prompt |
| `adv_prompt_injection_test_set.md` | Generate direct and indirect injection cases for tool-calling agents, RAG pipelines, and multi-turn systems with containment verification |
| `adv_edge_case_generator.md` | Produce edge inputs from a task spec across boundary, malformed, and hostile axes for exhaustive input-coverage testing |
| `adv_persona_attack_battery.md` | Generate a graded battery of role-play and identity-override attempts ordered by bypass sophistication |
| `adv_data_exfil_probe.md` | Generate probes targeting system prompt content, user data, or internal context using six extraction strategies |
| `adv_refusal_bypass_audit.md` | Build a graded bypass ladder for a specific refusal policy to identify whether the refusal is robust or brittle |

---

## How to Use These Together

**Full pre-deployment adversarial review:**
1. `adv_jailbreak_corpus_builder.md` — broad jailbreak coverage across taxonomy
2. `adv_persona_attack_battery.md` — targeted persona durability test
3. `adv_data_exfil_probe.md` — extraction resistance
4. `adv_refusal_bypass_audit.md` — per-policy hardness measurement

**RAG or tool-agent deployment:**
1. `adv_prompt_injection_test_set.md` — injection cases for all data surfaces
2. `adv_edge_case_generator.md` — boundary and hostile inputs for the input schema

**After a bypass incident:**
1. `adv_refusal_bypass_audit.md` — map the bypass gradient to find the breakpoint
2. `adv_jailbreak_corpus_builder.md` — expand corpus with new taxonomy cases

---

## Related Folders

- `../regression/` — regression test sets and A/B testing for prompt changes
- `../rubrics/` — scoring rubrics for evaluating model outputs
- `../eval-datasets/` — dataset curation, synthesis, and stratification
