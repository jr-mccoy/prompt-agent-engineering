# Learning AI/ML

The learner track: twelve standalone generators that adapt to whatever you are learning, plus four sequenced series that instantiate that depth for specific paths. The generators produce a plan; the series *are* the plan.

**12 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Learning ML, reading papers, or preparing for interviews.
- Building a portfolio or a study path.
- Taking a notebook to production as a learning exercise rather than a platform project.

**Not here:**
- You need to do the work rather than learn it — use the lifecycle subdirectories.
- The question is curriculum design for teaching *others* → `domain-education-teaching/`.
- You want a domain-general learning method rather than an ML-specific one → `domain-learning/`.

## Prompts


**Understand concepts**

| Prompt | Use it to |
|---|---|
| [`mllearn_concept_explainer.md`](mllearn_concept_explainer.md) | Explain any ML/AI concept at a chosen level using intuition first, then math, then a worked example — adapting depth to the learner and building from what they already know. |
| [`mllearn_math_for_ml_explainer.md`](mllearn_math_for_ml_explainer.md) | Explain the linear algebra, calculus, or probability behind an ML concept, always tied to its ML use — so the math is learned as a tool, not as decontextualized abstraction. |
| [`mllearn_glossary_builder.md`](mllearn_glossary_builder.md) | Build a leveled, personalized glossary of ML/AI terms for the learner's specific context — each entry tied to where they'll meet it, with the common confusion flagged. |
| [`mllearn_understanding_debugger.md`](mllearn_understanding_debugger.md) | Diagnose where a learner's mental model of an ML concept is wrong via Socratic probing, then repair the specific misconception rather than re-teaching the whole topic. |

**Read research**

| Prompt | Use it to |
|---|---|
| [`mllearn_paper_reading_guide.md`](mllearn_paper_reading_guide.md) | Guide a structured, critical read of an ML paper — what to extract, in what order, and how to interrogate claims — building the learner's ability to read papers independently. |
| [`mllearn_paper_digest_generator.md`](mllearn_paper_digest_generator.md) | Produce a structured digest of a paper the user provides — problem, method, results, limitations, and relevance — grounded strictly in the paper's content with no fabricated numbers. |
| [`mllearn_reproduce_paper_plan.md`](mllearn_reproduce_paper_plan.md) | Plan a faithful reproduction of an ML paper — scoping what to reproduce, surfacing ambiguities, defining baselines and success criteria, and budgeting realistically. |

**Plan and practise**

| Prompt | Use it to |
|---|---|
| [`mllearn_study_path_designer.md`](mllearn_study_path_designer.md) | Design a personalized ML/AI study path for a stated goal, current level, and time budget — sequencing prerequisites and projects with checkpoints, not just listing courses. |
| [`mllearn_portfolio_project_designer.md`](mllearn_portfolio_project_designer.md) | Design an ML portfolio project that demonstrates targeted skills end-to-end — scoped to be finishable, differentiated from tutorials, and legible to the audience evaluating it. |
| [`mllearn_kaggle_competition_strategy.md`](mllearn_kaggle_competition_strategy.md) | Build a disciplined strategy for an ML competition — trustworthy validation, EDA, modeling, ensembling, and leaderboard discipline — that avoids the overfitting traps that sink competitors. |

**Interview**

| Prompt | Use it to |
|---|---|
| [`mllearn_ml_interview_prep.md`](mllearn_ml_interview_prep.md) | Coach ML interview prep across concepts, coding, and stats by quizzing and teaching through misses — never just handing over answers — so the learner builds durable recall and reasoning. |
| [`mllearn_ml_system_design_interview.md`](mllearn_ml_system_design_interview.md) | Practice ML system design interviews with a structured framework, prompting the learner to drive the design while critiquing their choices like a real interviewer. |

### Sequenced series

Four subdirectories put *instantiated* depth on top of the generators above. Use a generator when your path is unusual; use a series when it matches.

| Series | Prompts | What it is |
|---|---|---|
| [`study-tracks/`](study-tracks/README.md) | 4 | Full specialization curricula — CV, NLP/LLM, RL, MLOps — sequenced by prerequisite with a build and a demonstrable checkpoint per phase |
| [`paper-reproductions/`](paper-reproductions/README.md) | 4 | Landmark-paper reproduction guides — ResNet, Transformer, word2vec, DQN — under a strict no-fabrication convention |
| [`interview-bank/`](interview-bank/README.md) | 5 | Graded system-design question banks by problem class, plus a universal scoring rubric |
| [`notebook-to-production/`](notebook-to-production/README.md) | 4 | A sequenced arc: refactor → reproducible pipeline → serve → deploy, monitor, CI/CD |

## Conventions

- **Prefix:** `mllearn_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/learning-ai-ml`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Resource types, not resource names.** The generators describe *kinds* of resource and tell the learner to verify the current canonical one; they do not invent course, book, or benchmark facts.
- **The paper-reproduction series carries the domain's strictest anti-fabrication rule** — see its own README.

## What lives elsewhere

- Domain-general learning craft — curriculum design, deliberate practice, reading lists → `domain-learning/`.
- Teaching others rather than learning yourself → `domain-education-teaching/`.
- Coding education specifically → `domain-learning-coding/`.
