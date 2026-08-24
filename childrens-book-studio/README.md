# Children's Book Studio

A self-contained **agentic system** that takes a children's-writing idea and walks it to a *finished, publishable product* — a manuscript plus the submission package an author needs to query it. It covers the whole shelf: board/concept books, picture books, early readers, chapter books, middle-grade and upper-MG/young-teen-crossover novels, verse novels, graphic novels, short stories, and narrative + expository/STEM nonfiction.

This toolkit was **designed with the [`agentic-system-factory/`](../agentic-system-factory/)** (the repo's agentic authoring discipline) and **orchestrates the existing [`domain-childrens-writing/`](../domain-childrens-writing/)** prompts rather than rebuilding them. The factory design bundle that justifies and specifies the system lives in [`design-bundle/`](design-bundle/).

---

## What it produces

A run ends with a **deliverable bundle** sized to the form:

- The **manuscript** in final form (prose, verse, or graphic-novel script), locked to the form's word-count band and reading level.
- **Art notes / a 32-page dummy map** for illustrated forms.
- **Back matter** (sources, author's note, further reading) for nonfiction.
- A **submission package**: logline + comps, query letter, one-page synopsis, formatted sample.
- A **representation-audit summary** (risk flags + questions for a human sensitivity reader — never a certification).

---

## What it will NOT do

These are hard boundaries, enforced at the gates (see [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md)):

- **Never invents nonfiction fact.** Every specific traces to a source or is bracketed `VERIFY`. No made-up dates, quotes, or scenes.
- **Never certifies representation.** The across-difference audit surfaces risks and questions; it never declares a portrayal "authentic" or "safe." It does not replace an own-voices author or a paid sensitivity reader.
- **Never fabricates publishing facts.** No invented comp titles, agent/publisher names, sales figures, or submission rules — all unverifiable items are bracketed `[AUTHOR TO VERIFY]`.
- **Never writes mature-content YA.** Explicit content and adult themes (ages 14+) redirect to [`domain-creative-writing/`](../domain-creative-writing/).
- **Never preaches.** Theme is carried by action; stated morals get cut.

---

## How to use it (four modes)

| Mode | Entry point | For |
|------|-------------|-----|
| **Guided** (default) | [`orchestrator_childrens_book.md`](orchestrator_childrens_book.md) | First-timers — it interviews you, classifies your starting stage, routes you through the pipeline, and critiques each output against the stage's gate before advancing. |
| **Commands** | `/write-childrens-book`, `/revise-manuscript`, `/calibrate-reading-level`, `/build-submission-package` (see [`commands/`](commands/)) | Claude Code users who prefer slash commands. |
| **Manual** | Walk [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) yourself | Power users / Codex — pick a stage from [`prompts/`](prompts/) and run it. |
| **Surgical** | Jump to one stage prompt | You already have a draft and only need one piece (e.g., a submission package). |

**Start guided:** paste [`orchestrator_childrens_book.md`](orchestrator_childrens_book.md) and answer the five intake questions.

---

## The pipeline (idea → finished product)

```
Stage 0  Project setup ........ form + age band + fiction/NF + concept   ──GATE 0 (age boundary)
Stage 1  Concept foundation ... protagonist + agency, theme, NF sources
Stage 2  Structure & beat map . form-specific outline
Stage 3  Draft generation ..... full manuscript (+ art notes if illustrated)
Stage 4  Revision triage ...... diagnose → fix-queue → revise (loops)     ──GATE A (craft integrity)
Stage 5  Polish & accuracy .... illustrator/dummy, rhyme, accessibility;
                                  NF accuracy + back matter                ──GATE B (truth & representation)
Stage 6  Publishing package ... pitch/comps → query → synopsis            ──GATE C (publishing honesty)
            │
            └─→ Deliverable bundle (manuscript + package + audit summary)
```

Stages branch by form: a board book skips most of Stage 4–5; a verse novel adds rhyme polish; nonfiction adds accuracy verification + back matter; illustrated forms add illustrator collaboration. Full I/O table in [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md).

---

## How the gates work

Gates are enforced by **orchestrator critique**, not scripts: every stage prompt ends with a Verification Checklist, and the orchestrator checks each item PASS/FAIL and **refuses to advance on any FAIL**. The four hard gates map to the factory's Gate 0/A/B/C:

- **Gate 0 — Age boundary:** valid form + age band; mature-YA redirects out.
- **Gate A — Craft integrity:** child drives the climax; theme not preached; read-aloud rhythm where the form demands it; reading level on target.
- **Gate B — Truth & representation:** nonfiction fully sourced + back matter; the representation audit emits flags, never certifications; no age-inappropriate content.
- **Gate C — Publishing honesty:** no invented comps/agents; deliverable manifest complete.

Why critique and not code: the system's blast radius is low (it writes the author's own draft files), so the rigor lives in the checklists. The rationale is recorded in [`design-bundle/GATE_DESIGN.md`](design-bundle/GATE_DESIGN.md).

---

## Conventions inherited from the domain

This studio enforces the nine load-bearing conventions of [`domain-childrens-writing/`](../domain-childrens-writing/README.md): child agency, no preaching, respect the reader, trust the illustrator, read aloud, nonfiction accuracy, representation humility, publishing anti-fabrication, and the age boundary.

---

## Directory map

- [`orchestrator_childrens_book.md`](orchestrator_childrens_book.md) — the conductor (guided mode)
- [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) — flow, stage I/O, gate map, branching
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — design rationale + pointer to the factory bundle
- [`AGENTS.md`](AGENTS.md) — Codex / coding-agent entry point
- [`DRY_RUN.md`](DRY_RUN.md) — a worked run showing each gate firing
- [`prompts/`](prompts/) — the 7 stage prompts
- [`agents/`](agents/) — 3 agents (orchestrator, craft reviewer, nonfiction accuracy checker)
- [`commands/`](commands/) — 4 slash commands
- [`design-bundle/`](design-bundle/) — the factory-produced design spec (proof of rigor)
- [`referenced-prompts/`](referenced-prompts/README.md) — stage → domain-prompt routing index
