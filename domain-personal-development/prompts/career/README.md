---
title: "AI Career Assessments"
category: personal-development
description: "17 interactive career qualification assessments for AI-related roles — each provides a structured interview, skill evaluation, gap analysis, and personalized development roadmap"
updated: "2026-10-08"
---

# AI Career Assessments

This directory contains 17 interactive career qualification assessments covering the full spectrum of AI-related roles, from accessible entry points (Data Annotator) to highly specialized positions (AI Research Scientist).

## How These Assessments Work

Every assessment follows a common **interaction protocol**:

1. **Introduction** -- The AI advisor explains the process and confirms readiness.
2. **Structured Interview** -- 8 targeted questions asked one at a time, covering background, skills, experience, and goals.
3. **Assessment & Roadmap** -- After all 8 answers, the advisor delivers:
   - **Qualification Verdict** -- one of four tiers (Qualified Now, Nearly Qualified, Significant Gaps, Not Currently Viable). The percentage-match bands are the assessment's own scoring rubric, not market data.
   - **Personalized Roadmap** -- time-phased action items with checkboxes (typically 30 days / 3-6 months / 6-12 months; horizons vary by role).
   - **Top 5 Resources** -- tailored to the candidate's specific gaps; any named course, certification, platform, or community is flagged for the candidate to confirm it still exists.
   - **Salary (or Earning) Reality Check** -- *estimated* ranges by experience level and location, explicitly labeled as estimates the candidate must verify against live sources (levels.fyi, Glassdoor, BLS, freelance-platform rate data, current postings). No figure is presented as current fact.
   - **Single Next Action** -- one concrete step to take within 7 days (3 days for Data Annotator).

Paste any assessment into a conversation with a capable AI chat assistant and it will conduct the full interview interactively.

## Assessment Index

| # | Career Path | File | Entry Barrier |
|---|------------|------|---------------|
| 1 | ML Engineering | [career_ml_engineering.md](career_ml_engineering.md) | High |
| 2 | AI Prompt Engineering | [career_ai_prompt_engineering.md](career_ai_prompt_engineering.md) | Low-Medium |
| 3 | AI Ethics Officer | [career_ai_ethics_officer.md](career_ai_ethics_officer.md) | Medium-High |
| 4 | AI Product Management | [career_ai_product_management.md](career_ai_product_management.md) | Medium-High |
| 5 | AI Data Annotator / Trainer | [career_ai_data_annotator_trainer.md](career_ai_data_annotator_trainer.md) | Low |
| 6 | Computer Vision Engineering | [career_computer_vision_engineering.md](career_computer_vision_engineering.md) | High |
| 7 | NLP Engineering | [career_nlp_engineering.md](career_nlp_engineering.md) | High |
| 8 | AI Research Scientist | [career_ai_research_scientist.md](career_ai_research_scientist.md) | Very High |
| 9 | Deep Learning Engineering | [career_deep_learning_engineering.md](career_deep_learning_engineering.md) | High |
| 10 | AI Content Creator | [career_ai_content_creator.md](career_ai_content_creator.md) | Low-Medium |
| 11 | AI Governance | [career_ai_governance.md](career_ai_governance.md) | Medium-High |
| 12 | AI Coach | [career_ai_coach.md](career_ai_coach.md) | Medium |
| 13 | AI Strategist | [career_ai_strategist.md](career_ai_strategist.md) | High |
| 14 | AI Change Management | [career_ai_change_management.md](career_ai_change_management.md) | Medium |
| 15 | AI Compliance | [career_ai_compliance.md](career_ai_compliance.md) | Medium-High |
| 16 | Conversational AI & UX Designer | [career_conversational_ai_ux.md](career_conversational_ai_ux.md) | Medium |
| 17 | AI Product Adoption & CS | [career_product_adoption_cs.md](career_product_adoption_cs.md) | Medium |

## Choosing an Assessment

**By accessibility (easiest entry first):**
- **Low barrier:** Data Annotator (5), Prompt Engineering (2), Content Creator (10)
- **Medium barrier:** AI Coach (12), Change Management (14), Conversational AI (16), Product Adoption (17)
- **High barrier:** ML Engineering (1), Computer Vision (6), NLP (7), Deep Learning (9), Strategist (13)
- **Very high barrier:** AI Research Scientist (8)

**By domain:**
- **Technical / Engineering:** 1, 6, 7, 8, 9
- **Product & Strategy:** 4, 13, 17
- **Governance, Ethics & Compliance:** 3, 11, 15
- **People & Change:** 12, 14
- **Creative & Content:** 2, 10, 16
- **Entry-level / Accessible:** 5

## Related Directories

- **[../agency/](../agency/)** -- Prompts for building personal agency, initiative, and self-direction in your career.
- **[../solo-dev/](../solo-dev/)** -- Prompts for solo developers and independent builders working with AI tools.

These directories complement the career assessments: use the **career assessments** to identify your path, the **agency prompts** to build the mindset for pursuing it, and the **solo-dev prompts** if you are building independently along the way.

## Techniques Used

Each assessment declares its techniques in frontmatter. Two sets are in use (names per `techniques/MASTER_TECHNIQUE_INDEX.md`):

| Code | Technique | Used by | Purpose in these assessments |
|------|-----------|---------|------------------------------|
| ST-01 | Clear Objective Statement | All 17 | Fixes the job as a readiness assessment ending in a tiered verdict and roadmap |
| RT-01 | Chain-of-Thought | All 17 | Calibrates the advisor's reasoning about the bar for the role |
| QA-04 | Uncertainty Acknowledgment | All 17 | Forces salary/demand figures to be labeled estimates-to-verify and thin answers to be flagged |
| RT-02 | Multi-Dimensional Analysis Framework | 1, 3, 5, 6, 7, 9, 10, 12, 14, 16, 17 | Scores readiness across the eight interview dimensions |
| DS-02 | Metric Specification | 1, 3, 5, 6, 7, 9, 10, 12, 14, 16, 17 | Anchors the verdict in must-have/advantage criteria and percentage bands |
| DS-01 | Framework Application | 2, 4, 8, 11, 13, 15 | Defines the eight dimensions the interview must elicit before judging |
| CM-02 | Constraint Specification | 2, 4, 8, 11, 13, 15 | Enforces one-question-at-a-time flow, the four-tier verdict, and anti-fabrication rules |

## Refresh status (2026-10-08)

**What was checked.** All 17 assessments were read in full for stale or unverifiable claims: named tools, products, platforms, frameworks, and certifications; salary, rate, demand, and growth statements; degree or skill requirements stated as what employers "now" require; regulation status (e.g., EU AI Act application dates); and dated "as of" language. The 2026-06-19 hardening (salary figures framed as estimates to verify) was kept as is. Assessments with nothing stale were left unchanged and keep their earlier `updated` date.

**What changed.**
- Named product lists were replaced with generic categories (the candidate names their own tools), or kept as examples flagged for confirmation.
- Demand and market claims ("high demand", "regulation intensifies", "niche commands a premium") were reworded so they are not stated as fact.
- Degree requirements stated as fact ("PhD effectively mandatory", "MS often preferred") were reworded as things to confirm in target postings.
- Regulation status may not be stated from memory (compliance, governance).
- The dated "FAANG" label was replaced with "large tech companies".
- The Prompt Engineering assessment now has the candidate check whether the standalone job title still appears in their market.

**How `[VERIFY: ...]` markers work.** A marker sits next to a claim that was not confirmed at the last review and says what to check against which source type, e.g. `[VERIFY: degree requirements in current postings for the candidate's target labs/settings]`. Inside the pasted interview prompt, the model is told never to present a marked item as fact and to tell the candidate what to check and where. Each edited assessment's Verification checklist has a line requiring every slot to be resolved against a live source or left visibly open. Never replace a marker with a figure, date, or product name from memory.

**Retirement candidates.** None. Ethics Officer (3), AI Governance (11), and AI Compliance (15) overlap, but they serve different entry backgrounds (ethics/philosophy/policy vs. GRC frameworks vs. audit/regulatory compliance), so each is kept. Any future retirement will be recorded in `meta/REORG_MAP.tsv`.
