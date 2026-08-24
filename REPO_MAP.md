# Repository Map

**Purpose:** Visual overview of folder structure for quick navigation.

---

## Top-Level Structure

```
prompting-guides/
│
├── START_HERE_FOR_AI.md     # AI assistant entry point
├── AI_AGENT_QUICK_START.md  # Build coding/technical prompts
├── NON_CODING_QUICK_START.md # Build non-coding prompts
├── CLAUDE.md                 # Detailed agent instructions
├── README.md                 # Full documentation
│
├── techniques/               # Prompt engineering reference
│   ├── MASTER_TECHNIQUE_INDEX.md  # Canonical technique catalog (250)
│   └── USE_CASE_LOOKUP.md         # Find techniques by task type
│
├── authoring/                # Resource creation guides
│   ├── skill-patterns/       # How to create skills
│   ├── agent-patterns/       # How to create agents
│   └── command-patterns/     # How to create commands
│
└── domain-*/                 # 20 domain directories (see below)
```

---

## Domain Directories

### Technical Domains

```
domain-software-engineering/     (~483 prompts)
├── analysis/
│   ├── security/               # Vulnerability scanning, SQL injection, XSS
│   ├── performance/            # Bottleneck identification, optimization
│   ├── quality/                # Code complexity, duplication, smells
│   ├── architecture/           # Layer identification, patterns, coupling
│   └── evolution/              # Tech debt, churn, hotspots
├── testing/                    # Unit, E2E, accessibility tests
├── devops/                     # CI/CD, Docker, Kubernetes, GitOps
├── cloud/                      # AWS, Azure, GCP, serverless
├── api/                        # REST, GraphQL design
├── mobile/                     # iOS, Android, React Native, Flutter
└── algorithms/                 # Algorithm design and analysis

domain-frontend-development/     (~33 prompts)
├── react/                      # Component patterns, hooks, state, testing
├── vue/                        # Composition API, Pinia, testing
├── accessibility/              # WCAG, ARIA, screen readers
├── performance/                # Core Web Vitals, bundle optimization
└── testing/                    # Jest, Playwright
```

### Coding Agent Resources

```
domain-agentic-resources/        (~821 resources)
├── skills/                     # 186 reusable capabilities
│   ├── cloud-infrastructure/   # Helm, Terraform, K8s, AWS, GCP
│   ├── developer-tools/        # GitHub ops, git workflows
│   ├── testing-qa/             # Test generation, E2E, performance
│   ├── security/               # Audits, vulnerability scanning
│   ├── documentation/          # API docs, technical writing
│   └── ...                     # 10+ more categories
├── agents/                     # 99 task-specific agents
├── commands/                   # 80 multi-agent workflows
└── personas/                   # 52 pipeline identities
```

### Business & Strategy

```
domain-business-strategy/        (~124 prompts)
├── analysis/                   # SWOT, BCG, competitive, financial, OKR
├── startup/                    # Naming, branding, go-to-market
├── research/                   # Competitive landscape, market sizing
└── organization/               # Content audit, gap analysis, project status

domain-productivity/             (~84 prompts)
├── validation/                 # Decision validation, sanity checks
├── career/                     # Career development, exploration
├── deep-work/                  # Focus strategies
├── automation/                 # Zapier, Make workflows
└── prototyping/                # App building with AI

domain-decision-making/          (~28 prompts)
└── [decisioning frameworks, tradeoff analyzers, blind spot checks]
```

### Professional Communication

```
domain-professional-communication/ (~29 prompts)
├── prompts/                    # PRDs, market sizing, stakeholder updates
└── design/                     # Design-related prompts

domain-presentations/            (~24 prompts)
# Executive and board presentations (PowerPoint formats)

domain-professional-writing/     (~46 prompts)
├── domain-specific/            # CPAs, attorneys, contractors (26 fields)
└── writing/                    # Business writing
```

### Specialized Domains

```
domain-image-generation/         (~15 prompts)
├── branding/                   # Logos, icons, illustrations
├── coloring-book/              # Coloring book illustrations
└── healthcare/                 # Medical infographics

domain-healthcare-clinical/      (~55 prompts)
└── prompts/                    # Clinical decision support, patient comm

domain-discipleship/             (73 prompts — TRADITION-NEUTRAL, FORMATION IS NOT A METRIC)
├── curriculum-architecture/    # Multi-stage blueprint, outcomes, sequence, balance audit, materials, multiplication, multi-generation governance (7)
├── learner-pathways/           # Self-assessment, growth plan, practices, stalls, returning, life constraints (6)
├── mentor-equipping/           # Readiness, training, conversation skill, boundaries & referral, sustainability, debrief, case consultation, doubt & deconstruction posture (8)
├── pairing-and-relationship/   # Matching criteria, covenant, first meeting, cadence, ending well, re-contracting, informal pairing, mentee expectations (8)
├── session-and-lesson/         # Session shape, lessons, question bank, hard disclosures, small groups, accessibility design (6)
├── program-operations/         # Program blueprint, safeguarding, onboarding, health review, mentor pipeline, minimum viable program, control-drift audit (7)
├── topical-modules/            # Money, work, sexuality (STRONG-GUARD), forgiveness, suffering, anger, digital, hostile witness (8)
├── life-stage-tracks/          # Youth (STRONG-GUARD), college/young adult, married couples, parents, seniors (5)
├── context-variants/           # Prison & re-entry, campus, workplace, remote & diaspora (4)
├── initiation-and-catechesis/  # Baptism prep, membership prep, catechesis design — multi-view (3)
├── cross-cultural/             # Cross-cultural discipling, oral-preference learners, translated material (3)
├── peer-and-accountability/    # Mentor peer cohort (curriculum + facilitation), accountability partnership (design + conversation) (4)
└── after-harm/                 # Harmed by a previous relationship (STRONG-GUARD), dependency, mentor's own rupture, after a removal (STRONG-GUARD) (4)

domain-research-academic/        (~15 prompts)
└── prompts/                    # Literature review, methodology

domain-personal-development/     (~43 prompts)
└── prompts/                    # Goals, habits, career, self-improvement

domain-learning-coding/          (~17 prompts)
└── [coding education, tutorials, exercises]

domain-education-teaching/       (Guide)
└── [lesson plans, worksheets, assessments]

domain-creative-writing/         (Guide)
└── [fiction, essays, narrative, poetry]

domain-specialized-fields/       (Guide)
└── [legal, trades, real estate, marketing]

domain-finance/                  (Guide)
└── [finance & economics field guide]

domain-psychology/               (Library)
└── [psychology, therapy & behavioral health (~99)]

domain-psy-ops/                  (32 prompts — ANALYTIC / DEFENSIVE ONLY)
├── technique-analysis/         # Propaganda technique, emotional levers, framing, pressure, provenance, stats (7)
├── influence-operations/       # ABCDE assessment, coordination, astroturf, laundering, attribution (7)
├── personal-defense/           # Manipulation, coercive control, high-control groups, pretexting (7, safety-gated)
├── organizational-red-team/    # Threat model, narrative vulnerability, personnel exposure, community (4)
├── counter-messaging/          # Prebunking, corrections, response triage, crisis integrity (4)
└── case-studies-taxonomies/    # Framework crosswalk, historical case study, media literacy (3)

domain-written-advocacy/         (35 prompts — LAYPERSON SELF-ADVOCACY LETTERS)
├── cross-cutting/              # Request-letter architect, channel & record strategy, escalation ladder, log, response analyzer, follow-up (6)
├── accounts-and-billing/       # Cancellation, account closure, recurring charge, utility/telecom, price increase (5)
├── privacy-and-data/           # Deletion, access (DSAR), marketing opt-out, broker removal, escalation (5)
├── products-and-warranty/      # Warranty claim, defect remedy, service non-performance, safety defect report (4)
├── financial-hardship/         # Hardship, payment plan, fee waiver, goodwill, rate reduction, credit dispute (6)
├── insurance-and-medical/      # Denial appeal, external review, medical bill dispute, charity care (4)
└── institutions-and-records/   # Public records, benefits appeal, regulator complaint, workplace, school (5)
```

### Engineering Workflows

```
domain-engineering-workflows/    (~58 prompts)
├── workflows/                  # Sprint planning, debugging, postmortems
├── tasks/                      # Task management, prioritization
├── improvement/                # Refactoring guidance
└── ai-patterns/                # AI-specific development workflows
```

### Meta & Reference

```
domain-prompt-engineering/       (~22 prompts)
├── prompt-improvement/         # Improve existing prompts
├── model-optimization/         # GPT/model-specific optimization
└── evaluation/                 # AI correctness, eval design

techniques/                      (Reference)
├── MASTER_TECHNIQUE_INDEX.md   # 327 active techniques (canonical)
└── USE_CASE_LOOKUP.md          # Find by task type
```

---

## Quick Navigation by Intent

| I want to... | Go to... |
|--------------|----------|
| Use an existing prompt | `domain-*/` matching my need |
| Build a new coding prompt | `AI_AGENT_QUICK_START.md` |
| Build a new non-coding prompt | `NON_CODING_QUICK_START.md` |
| Build an image generation prompt | `domain-image-generation/IMAGE_GENERATION_GUIDE.md` |
| Create a reusable skill | `authoring/skill-patterns/` |
| Find technique definitions | `techniques/MASTER_TECHNIQUE_INDEX.md` |
| Find techniques by use case | `techniques/USE_CASE_LOOKUP.md` |
| Use Claude Code skills/agents | `domain-agentic-resources/` |

---

**Last Updated:** 2026-04-20
