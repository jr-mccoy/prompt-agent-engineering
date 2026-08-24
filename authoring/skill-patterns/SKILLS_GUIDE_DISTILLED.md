# Building Skills — Upstream Guide, Distilled

A condensed, vendor-neutral reference distilled from Anthropic's **"The Complete Guide to Building Skills for Claude" (2026)**. It captures the rules and methods that aren't already spelled out in `SKILL_PATTERN_INDEX.md`, `SKILL_USE_CASE_LOOKUP.md`, and `SKILL_QUALITY_RUBRIC.md`, and cross-links to them. Specific limits and figures are attributed to the source; no source text is reproduced.

**Use this when:** authoring or reviewing a Skill and you want the authoritative limits, the description/triggering rules, the testing ladder, and the named anti-patterns in one place.

---

## 1. What a Skill is (and how it relates to tool connectors)

- A Skill is **instructions packaged as a folder** that teach the model how to handle a specific task or workflow — "teach once, benefit every time."
- **Tool connectors vs. Skills:** connectors provide *connectivity* (what the model *can do* — access to tools/data); Skills provide *knowledge* (how the model *should do it* — the workflow and best practices). The kitchen analogy: connectors are the kitchen; Skills are the recipes. If you already have a working connector, the Skill is the knowledge layer on top.
- **Three design principles:** progressive disclosure, composability (works alongside other skills, doesn't assume it's the only one), portability (same skill across surfaces, given the environment supports its dependencies).

## 2. Hard limits and structural rules (the parts most often gotten wrong)

| Rule | Limit / requirement |
|---|---|
| `SKILL.md` filename | **Exactly** `SKILL.md` (case-sensitive). Not `skill.md`/`SKILL.MD`. |
| Skill folder name | **kebab-case**, no spaces/underscores/capitals; should match the skill `name`. |
| `name` field | kebab-case; no `claude`/`anthropic` prefix (reserved). |
| `description` field | Must state **WHAT it does AND WHEN to use it** (trigger conditions + sample user phrases). **Under 1024 characters.** No XML angle brackets (frontmatter is in the system prompt → injection risk). |
| `compatibility` field (optional) | 1–500 chars; declares environment requirements (platform, system packages, network). |
| `allowed-tools` (optional) | Restricts tool access, e.g. `Bash(python:*) WebFetch`. |
| `SKILL.md` body size | Keep **under ~5,000 words**; move detail to `references/` and link. |
| README | **No `README.md` inside the skill folder** (a repo-level README for human distribution is fine and separate). |
| Enabled-skill load | Re-evaluate when **more than ~20–50 skills** are enabled at once; recommend selective enablement / skill "packs." |

**Progressive disclosure (3 levels):** (1) frontmatter — always loaded, just enough to decide *when* to load; (2) `SKILL.md` body — loaded when judged relevant; (3) linked files in `references/`/`scripts/`/`assets/` — navigated only as needed.

**Folder contents:** `SKILL.md` (required) + optional `scripts/` (executable), `references/` (load-as-needed docs), `assets/` (templates/fonts/icons).

## 3. The description is the trigger (cross-ref AG-37/AG-38)

The `description` is the *only* signal used to decide whether to load the skill — get it right (this repo already catalogs it as **AG-37 Description-as-Trigger** and **AG-38 Sibling-Skill Cross-Reference**). Add to those:

- **Description formula:** `[What it does] + [When to use it] + [key user phrases] + [key capabilities]`.
- **Negative triggers** fix over-triggering: `Do NOT use for X — use the {other} skill instead.`
- **Debug trick:** ask the model *"When would you use the {skill} skill?"* — it quotes the description back; adjust based on what's missing or wrong.

## 4. Authoring methodology — iterate on one task, then extract (technique AG-46)

The most effective method: **pick one challenging instance, iterate until the model reliably succeeds, then extract the winning approach into the skill** — leveraging in-context learning for faster, higher-signal feedback than designing broadly and testing wide before anything works once. *Then* expand to a small suite of varied cases for coverage and triggering tests. (Registered in the master index as **AG-46 Single-Task Iterate-then-Extract**.)

Other authoring notes:
- **Code over language for critical validation:** for must-not-fail checks, bundle a script that performs the check programmatically — "code is deterministic; language interpretation isn't."
- **Encouragement belongs in the user prompt, not `SKILL.md`:** anti-"laziness" nudges ("take your time, don't skip validation") are reported to work better in the user prompt than baked into the skill.

## 5. Three common use-case categories

1. **Document & asset creation** — consistent high-quality output (docs, decks, designs, code). Techniques: embedded style guides, template structures, pre-finalize quality checklists.
2. **Workflow automation** — multi-step processes needing consistent methodology (incl. multi-connector coordination). Techniques: step-by-step workflow with validation gates, built-in review loops.
3. **Connector/tool enhancement** — workflow guidance layered on a tool connector. Techniques: sequence multiple tool calls, embed domain expertise, handle common tool errors.

## 6. Five reusable orchestration patterns

Each = **Use when** + **Key techniques** (complements the pattern catalog in `SKILL_PATTERN_INDEX.md`):

1. **Sequential workflow orchestration** — ordered multi-step processes; explicit step order, dependencies, per-stage validation, rollback on failure.
2. **Multi-connector coordination** — workflows spanning services; clear phase separation, data passing between services, validate before next phase, centralized error handling.
3. **Iterative refinement** — quality improves with iteration; explicit quality criteria, improvement loop, validation scripts, **and a stop condition**.
4. **Context-aware tool selection** — same outcome, different tool by context; decision criteria, fallbacks, transparency about the choice.
5. **Domain-specific intelligence** — adds specialized knowledge beyond tool access; domain logic, compliance-before-action, governance.

## 7. Testing ladder and success criteria

- **Three rigor levels:** (1) manual testing (fast iteration); (2) scripted/repeatable tests; (3) programmatic evaluation suites against a defined test set. Match rigor to audience (internal team vs. thousands of users).
- **Three test areas:** **triggering** (loads on obvious + paraphrased requests; does NOT load on unrelated topics — build explicit should/should-not suites); **functional** (valid outputs, calls succeed, error handling, edge cases — Given/When/Then); **performance comparison** (beats baseline on measurable criteria, e.g. fewer tool calls, fewer failures, fewer tokens).
- **Targets (explicitly "aspirational / partly vibes-based"):** ~90% trigger on relevant queries (run 10–20 test queries); workflow completes without user correction (run 3–5 times for consistency); 0 failed tool calls per workflow.

## 8. Named anti-patterns

- **Vague description** ("Helps with projects"), **missing triggers**, or **too-technical** description (no user phrases).
- **Non-actionable instructions** ("validate properly") instead of explicit checklists/commands.
- **Frontmatter mistakes:** missing `---` delimiters, unclosed quotes, spaces/capitals in name, XML tags in frontmatter.
- **Instructions ignored — four causes:** too verbose → bullet/trim; buried → put critical items at top under `## Important`/`## Critical`; ambiguous → explicit CRITICAL checklist; model "laziness" → encouragement in the *user prompt*.
- **Large-context issues:** SKILL.md too big, too many skills enabled, no progressive disclosure → cap size, move docs to `references/`, prune enabled set.
- **Over-triggering:** add negative triggers, be more specific, clarify scope.

## 9. Quick checklist (four phases)

- **Before you start:** 2–3 concrete use cases identified; tools (built-in or connector) identified; folder structure planned.
- **During development:** folder kebab-case; `SKILL.md` exact spelling; YAML has `---`; `name` kebab-case; description states WHAT + WHEN + phrases; no XML tags anywhere; instructions actionable; error handling + examples; references linked.
- **Before release:** triggering tested (obvious + paraphrased + negative); functional tests pass; tool integration works.
- **After release:** test in real use; monitor under/over-triggering; iterate description/instructions; bump `version` in metadata. Skills are **living documents**.

---

**See also:** `SKILL_PATTERN_INDEX.md` (41 patterns), `SKILL_USE_CASE_LOOKUP.md` (pattern selection), `SKILL_QUALITY_RUBRIC.md` (scoring), `templates/GOLD_STANDARD_SKILL.md`. Master-index techniques: **AG-37** (Description-as-Trigger), **AG-38** (Sibling-Skill Cross-Reference), **AG-39** (Foundation Context Document), **AG-40** (Numbered Phase Discipline), **AG-43** (Iterative Skill-Improver Loop), **AG-46** (Single-Task Iterate-then-Extract).

**Source:** Distilled from Anthropic, "The Complete Guide to Building Skills for Claude" (2026) — a vendor guide; limits/figures attributed inline, no source text reproduced.
