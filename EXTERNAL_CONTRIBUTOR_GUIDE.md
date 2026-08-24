# External Contributor Guide

Welcome! 👋 This repository is a large, organized collection of AI prompts, coding-agent resources, and prompt-engineering techniques (4,400+ prompts across 42 domains, plus a 289-technique catalog). This guide is the friendly, end-to-end starting point for contributing. For the detailed rules, see [`CONTRIBUTING.md`](CONTRIBUTING.md); for community expectations, see [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Why contribute

- Add prompts for use cases or domains we don't cover well yet.
- Improve existing prompts (clearer constraints, better examples, stronger verification).
- Propose new prompt-engineering **techniques** backed by real usage.
- Fix documentation, cross-references, or metadata.

Every contribution is credited, and merged work is licensed under the project's [MIT License](LICENSE).

---

## Step 1 — What are you contributing?

```
What do you want to add?
│
├─ A single reusable instruction set ............... a PROMPT      → Step 2
│
├─ A reusable multi-step capability with bundled
│  scripts / templates / references ................ a SKILL       → authoring/skill-patterns/README.md
│
├─ A task-specific agent definition ................ an AGENT      → authoring/agent-patterns/AGENT_QUICK_START.md
│
├─ A slash-command workflow ........................ a COMMAND     → authoring/command-patterns/COMMAND_QUICK_START.md
│
├─ A new prompt-engineering technique .............. a TECHNIQUE   → authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md
│
└─ A fix to docs / examples / metadata ............. DOCS          → just open a PR
```

When in doubt, a **prompt** is the right unit. Skills/agents/commands are for reusable, tool-integrated capabilities.

---

## Step 2 — Find the right home

Prompts live in `domain-*/` directories. To place yours:

1. Skim the **Repository Structure** table in [`README.md`](README.md#repository-structure).
2. For the most complete "what goes where" routing, see the **Category Mapping** section of [`CLAUDE.md`](CLAUDE.md).
3. Search [`PROMPT_INDEX.md`](PROMPT_INDEX.md) for similar prompts and place yours alongside them.

If genuinely nothing fits, propose a new domain in your PR and explain why existing ones don't work.

---

## Step 3 — Write it

Use the canonical template: [`authoring/NEW_PROMPT_TEMPLATE.md`](authoring/NEW_PROMPT_TEMPLATE.md). Every repository prompt has:

- **YAML frontmatter** (`title`, `category`, `description`, `techniques`, `difficulty`, `tags`, `updated`, `related_prompts`) — it feeds the index and discovery tooling.
- A structured body: Objective → Inputs/Context → Constraints (Must / Must Not) → Steps → Output Format → Verification.

Reference 3–5 **canonical** technique IDs from [`techniques/MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md) — never invent IDs. Quality bar and patterns: [`PROMPT_QUALITY_STANDARDS.md`](PROMPT_QUALITY_STANDARDS.md).

Naming: `lowercase_with_underscores.md`, descriptive, ≤55 chars (enforced by the naming validator).

---

## Step 4 — Validate locally

```bash
python3 domain-agentic-resources/commands/validate_command_frontmatter.py   # command frontmatter
python3 scripts/validate_naming_conventions.py  # file naming
python3 scripts/validate_technique_catalog.py   # technique IDs exist
python3 scripts/generate_prompt_index.py        # refresh the index
```

(If you use [`pre-commit`](https://pre-commit.com/): `pre-commit run --all-files`.) CI runs these on every PR, so checking locally first saves round-trips.

---

## Step 5 — Open a PR

Follow the checklist in [`CONTRIBUTING.md`](CONTRIBUTING.md#pull-request-process). Use the PR template, describe what you added, and note how you tested it.

---

## For researchers 🔬

If you work in AI/ML, prompt engineering, or evaluation, here's where the more rigorous, research-flavored material lives — and where new work of that kind belongs:

| Interest | Where it lives |
|----------|----------------|
| Empirical research practice (lit review, methodology, instruments, replication) | [`domain-research-academic/`](domain-research-academic/) |
| Reasoning craft (Bayesian updating, forecasting & calibration, systems thinking, epistemics) — content-agnostic, with machine-readable `reasoning:` frontmatter | [`domain-reasoning-craft/`](domain-reasoning-craft/) |
| Prompt evaluation & correctness (eval design, task difficulty, calibration, production monitoring) | [`domain-prompt-engineering/evaluation/`](domain-prompt-engineering/evaluation/) |
| Designing autonomous agents & multi-agent systems (architecture, tools, memory, safety, observability) | [`domain-AI-ML/agentic-ai-systems/`](domain-AI-ML/agentic-ai-systems/) |

Good first contributions for a researcher:
- **Propose a technique** you can show generalizes — see [`authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md`](authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md).
- **Strengthen evaluation prompts** with sharper, testable success criteria and adversarial checks.
- **Add reasoning-craft prompts** (mind the `reasoning:` frontmatter block — copy it from an existing sibling so the metadata stays consistent and indexable).
- **Contribute eval harnesses or rubrics** that make prompt quality measurable rather than subjective.

A note on rigor: the project values **false-positive prevention** and explicit verification (see [`PROMPT_QUALITY_STANDARDS.md`](PROMPT_QUALITY_STANDARDS.md)). Contributions that make a prompt's claims testable — rather than just longer — are exactly what we're looking for.

---

## Questions?

Open an issue (there are templates for bugs, feature/prompt requests, and prompt improvements) or ask in your PR. Thanks for helping make this resource better.
