# Repository Map

**Purpose:** Every top-level directory, with a real file count, for quick navigation.

Counts are Markdown files per tree (prompts plus that tree's own READMEs and
guides), taken from the filesystem. For routing by *task* — "I need X, where do I
go" — use [`CLAUDE.md`](CLAUDE.md); this file answers "what exists and how big is it."

---

## Entry points

| File | For |
|---|---|
| [`START_HERE_FOR_AI.md`](START_HERE_FOR_AI.md) | AI assistant entry point |
| [`CLAUDE.md`](CLAUDE.md) | Full routing table and agent instructions |
| [`README.md`](README.md) | Human-facing documentation |
| [`AI_AGENT_QUICK_START.md`](AI_AGENT_QUICK_START.md) | Build a new coding/technical prompt |
| [`NON_CODING_QUICK_START.md`](NON_CODING_QUICK_START.md) | Build a new non-coding prompt |
| [`PROMPT_INDEX.md`](PROMPT_INDEX.md) / [`PROMPT_INDEX.json`](PROMPT_INDEX.json) | Machine-readable catalog of every prompt |
| [`PROMPT_QUALITY_STANDARDS.md`](PROMPT_QUALITY_STANDARDS.md) | What a Tier 1 prompt looks like |

---

## Technical

| Directory | Files | Holds |
|---|---|---|
| [`domain-software-engineering/`](domain-software-engineering/) | 611 | Analysis (security, performance, quality, architecture, evolution, **business**, feature-design), testing, devops, cloud, api, mobile, algorithms, bug-bounty, vibe-coding-rescue, improvement, prototyping |
| [`domain-AI-ML/`](domain-AI-ML/) | 356 | The full ML lifecycle: framing, data, features, modelling, deep learning, evaluation, optimization, MLOps, monitoring, governance, GenAI/LLM, agentic systems, model security, verticals, leadership, learning |
| [`domain-frontend-development/`](domain-frontend-development/) | 68 | Frameworks, styling, TypeScript, forms, animation, architecture, build tooling, a11y, performance, testing, design-direction |
| [`domain-voice-conversational-ui/`](domain-voice-conversational-ui/) | 29 | Voice UI, chatbots, dialog architecture, NLU training, multimodal, analytics |
| [`domain-game-development/`](domain-game-development/) | 25 | Design, architecture, engines, testing, multiplayer, performance, graphics, audio, level design, economy |
| [`domain-learning-coding/`](domain-learning-coding/) | 18 | Learning to code |

## Agentic resources & authoring

| Directory | Files | Holds |
|---|---|---|
| [`domain-agentic-resources/`](domain-agentic-resources/) | 1565 | Skills, agents, commands, personas — the implementation library you *use* |
| [`domain-prompt-engineering/`](domain-prompt-engineering/) | 242 | Meta-prompts: improvement, model behavior, escaping the median, goal orientation, skill development, delegation, evaluation |
| [`continuity-kit/`](continuity-kit/) | 186 | Project Continuity Memory — a repo-local ledger of durable project state (self-contained package with its own tests) |
| [`agentic-system-factory/`](agentic-system-factory/) | 118 | Use case → production-ready agentic system design bundle |
| [`portable-prompt-system/`](portable-prompt-system/) | 99 | Self-contained, drop-in export of the technique library and authoring guides |
| [`authoring/`](authoring/) | 64 | The authoring systems: skill, agent, command, and system patterns — how to *create* resources |
| [`techniques/`](techniques/) | 44 | Canonical technique catalog and use-case lookup |

## Work — the five audience tracks

One axis: whose work is it, at what scope. Subject stays orthogonal (code goes to
software-engineering, money to finance, contracts to legal).

| Track | Directory | Files | Holds |
|---|---|---|---|
| Self | [`domain-personal-development/`](domain-personal-development/) | 177 | Identity, values, habits, goals, resilience, relationships, agency, life transitions, emotional fitness, career, stakeholder |
| Individual execution | [`domain-productivity/`](domain-productivity/) | 121 | Daily planning, deep work, reviews, operating cadence, automation, bottlenecks, workplace, validation, home life, school |
| Team delivery | [`domain-engineering-workflows/`](domain-engineering-workflows/) | 59 | Workflows, definition-of-done, AI patterns, AI-native rollouts |
| Product | [`domain-product-management/`](domain-product-management/) | 10 | PRDs, market sizing, competitor teardown, sprint planning (renamed from `domain-professional-communication`) |
| Org / company | [`domain-business-strategy/`](domain-business-strategy/) | 68 | AI strategy, ambition & leverage, go-to-market, research, startup |

## Thinking & decisions

| Directory | Files | Holds |
|---|---|---|
| [`domain-negotiation/`](domain-negotiation/) | 48 | Preparation, at-the-table, channels, multi-party, after-the-deal, contexts, difficult conversations, craft |
| [`domain-decision-making/`](domain-decision-making/) | 45 | Decision frameworks, scenario planning, tradeoff analysis, decision documentation |
| [`domain-reasoning-craft/`](domain-reasoning-craft/) | 42 | Reasoning moves, forecasting, systems thinking, epistemics |
| [`domain-psy-ops/`](domain-psy-ops/) | 34 | Cognitive security: influence analysis and manipulation defense (analytic/defensive only) |
| [`domain-deep-analysis/`](domain-deep-analysis/) | 22 | Multi-phase deep-think systems for problems, decisions, plans, designs |
| [`domain-ideation/`](domain-ideation/) | 13 | Divergent and convergent ideation |
| [`domain-risk/`](domain-risk/) | 8 | Register, FMEA, heat map, tail risk, dependency chains, AAR |
| [`domain-policy/`](domain-policy/) | 5 | Policy options, framing, stakeholder maps, feasibility |

## Writing & communication

| Directory | Files | Holds |
|---|---|---|
| [`domain-professional-writing/`](domain-professional-writing/) | 64 | Business writing, **content quality**, per-profession writing |
| [`domain-presentations/`](domain-presentations/) | 49 | Board decks, visual planning |
| [`domain-written-advocacy/`](domain-written-advocacy/) | 36 | Layperson self-advocacy letters |
| [`domain-creative-writing/`](domain-creative-writing/) | 28 | Adult fiction, craft tools, genre, creative nonfiction, poetry, script, publishing |
| [`domain-childrens-writing/`](domain-childrens-writing/) | 24 | Authoring for young readers |
| [`domain-advertising/`](domain-advertising/) | 18 | Industry-specific advertising creative |

## Education & research

| Directory | Files | Holds |
|---|---|---|
| [`domain-education-teaching/`](domain-education-teaching/) | 317 | Three audience tracks: `instructor/`, `program/`, `learner/` |
| [`domain-medical-education/`](domain-medical-education/) | 215 | Health-professions education: `educator-*` and `learner-*` tracks, plus `profession-specific/` |
| [`domain-science/`](domain-science/) | 155 | The practice of science: methods, bench, computational, statistics, writing, peer review, grants, ethics, lab ops, engagement, disciplines |
| [`domain-research-academic/`](domain-research-academic/) | 18 | Cross-field research methodology |
| [`domain-learning/`](domain-learning/) | 6 | Self-directed skill acquisition |

## Regulated & professional

| Directory | Files | Holds |
|---|---|---|
| [`domain-healthcare-clinical/`](domain-healthcare-clinical/) | 344 | Clinical decision support, specialties, pharmacy, nursing, allied health |
| [`domain-psychology/`](domain-psychology/) | 270 | Documentation, risk/crisis, modalities, client self-use, practice operations |
| [`domain-legal/`](domain-legal/) | 175 | Practitioner legal work, family law, and two litigant-facing self-advocacy sections |
| [`domain-finance/`](domain-finance/) | 148 | Corporate finance, markets, valuation, tax, risk, crypto, options, quant |
| [`domain-hr-management/`](domain-hr-management/) | 8 | Performance reviews, hiring |
| [`domain-specialized-fields/`](domain-specialized-fields/) | 3 | Legal research planning and IP landscape (hub; finance and psychology were promoted out) |

## Life & faith

| Directory | Files | Holds |
|---|---|---|
| [`domain-biblical-studies/`](domain-biblical-studies/) | 142 | Exegesis, study methods, sermon, theology, learner, ministry, church staff, languages, apologetics |
| [`domain-parenting/`](domain-parenting/) | 110 | Ages 4–8, neurodivergence, divorce/custody/co-parenting |
| [`domain-discipleship/`](domain-discipleship/) | 88 | One-to-one formation and the programs that pair people |
| [`domain-conversation-practice/`](domain-conversation-practice/) | 9 | Language conversation practice |

## Visual

| Directory | Files | Holds |
|---|---|---|
| [`domain-image-generation/`](domain-image-generation/) | 186 | Model guides plus branding, coloring, healthcare, e-commerce, social, covers, events, merch, illustration, comics, scientific |

## Pipelines & toolkits

Self-contained bundles. Several deliberately vendor copies of prompts that live
elsewhere; those copies are registered in [`meta/VENDORED.tsv`](meta/VENDORED.tsv)
and checked for drift by `scripts/check_vendored_copies.py`.

| Directory | Files | Holds |
|---|---|---|
| [`ai-investment-research-toolkit/`](ai-investment-research-toolkit/) | 74 | Paper-first investment research loop |
| [`domain-idea-to-product/`](domain-idea-to-product/) | 63 | Idea → shippable software, 11 stages |
| [`childrens-book-studio/`](childrens-book-studio/) | 35 | Idea → finished children's book |
| [`sourced-nonfiction-studio/`](sourced-nonfiction-studio/) | 27 | Uncited expertise → sourced, publishable nonfiction |
| [`financial-records-toolkit/`](financial-records-toolkit/) | 19 | Statements → verified, categorized spreadsheets |

## Repository infrastructure

| Directory | Holds |
|---|---|
| [`scripts/`](scripts/) | Index generation, naming and link validation, reorg tooling, vendored-copy drift check |
| [`tests/`](tests/) | Integration tests and the prompting-technique comparison harness |
| [`meta/`](meta/) | [`REORG_MAP.tsv`](meta/REORG_MAP.tsv) (every move and deletion) and [`VENDORED.tsv`](meta/VENDORED.tsv) (canonical → copy) |

---

## Keeping this file honest

Counts drift. To regenerate them:

```bash
for d in */; do d=${d%/}; [ "$d" = ".git" ] && continue
  printf "%-38s %s\n" "$d" "$(find "$d" -name '*.md' | wc -l)"
done
```

CI (`.github/workflows/structure.yml`) enforces the top-level naming shape:
`domain-*`, `*-toolkit`, `*-kit`, `*-studio`, `*-library`, `*-system`, `*-factory`,
plus `authoring`, `scripts`, `techniques`, `tests`, `meta`.
