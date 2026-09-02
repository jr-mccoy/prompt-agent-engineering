# PAE Routing Reference (fallback tables)

**This file is the long-form fallback for `pae route` / `pae search`.** It was split
out of `CLAUDE.md` so the always-loaded agent guide stays small. Nothing here is
loaded into context automatically — grep it, or read the one section you need.

Prefer the executable router when the PAE Engine is installed:

```bash
pae route  "<task>"     # which scope and kind should handle this, and why
pae search "<task>"     # ranked resources, with the matched terms shown
```

Use these tables when the Engine is not installed, or for the things the registry
cannot represent: negative boundaries ("X lives here, **not** there"), load-bearing
domain conventions and safety guards, and ordered workflows.

**Contents:** Repository Structure · Category Mapping (coding) · Non-Coding Domain
Mapping · Workflows for Common Scenarios · Quick Reference table.

---

## Repository Structure

```
prompt-agent-engineering/
├── domain-software-engineering/    # Code analysis, testing, DevOps, cloud, API, mobile, .NET, Java/Spring, embedded, Electron/SmartTV, localization, algorithms, vibe-coding rescue (~452)
│   ├── analysis/                   # Security, performance, quality, architecture
│   ├── testing/                    # Unit, E2E, accessibility testing
│   ├── devops/                     # CI/CD, Docker, infrastructure
│   ├── cloud/                      # AWS, GCP, Azure, serverless
│   ├── api/                        # REST, GraphQL design
│   ├── mobile/                     # iOS, Android, cross-platform
│   ├── algorithms/                 # Algorithm design
│   └── vibe-coding-rescue/         # Wall diagnosis, rules file, task decomposition, AI-code audit, handoff briefing
│       └── android/                # Android-specific vibe-rescue: wall diagnosis, codebase audit, security/privacy audit, fix prioritization, fix executor, rules file (6 prompts)
│
├── domain-frontend-development/    # Frontend: frameworks (React/Vue/Angular/Next.js/Svelte/Astro/SolidJS/Qwik/Remix), styling, TypeScript, forms, animation, architecture, build-tooling, a11y, performance, testing (~47)
│   ├── react/                      # React patterns, hooks, state, testing, performance
│   ├── vue/                        # Vue 3 Composition API, Pinia, testing
│   ├── accessibility/              # WCAG audits, ARIA patterns, screen readers
│   ├── performance/                # Core Web Vitals, bundle optimization
│   └── testing/                    # Jest unit testing, Playwright E2E
│
├── domain-agentic-resources/       # Resources for Claude Code (~731)
│   ├── skills/                     # Skills with progressive disclosure
│   ├── agents/                     # Task-specific agents
│   ├── commands/                   # Task-scoped commands (accessibility, architecture, code-quality, database, deployment, devops, documentation, framework-migration, git-workflows, mobile-development, non-coding, orchestration, performance, security, testing, troubleshooting, other)
│   └── personas/                   # Pipeline identities
│
├── domain-business-strategy/       # Business analysis & strategy (~121)
│   ├── analysis/                   # SWOT, BCG, competitive, financial
│   ├── startup/                    # Naming, branding, go-to-market
│   ├── research/                   # Competitive landscape, market sizing
│   └── organization/               # Content audit, knowledge base gap analysis, project status
│
├── domain-engineering-workflows/   # Project management & workflows (~84)
│   ├── workflows/                  # Sprint planning, debugging, postmortem
│   ├── tasks/                      # Task sorting, prioritization
│   ├── improvement/                # Refactoring guidance
│   ├── ai-patterns/                # AI-specific workflows
│   └── ai-native-rollouts/         # Team / org AI adoption (ambient review, tiered rollout, delegation brief, project memory, bottleneck migration)
│
├── domain-productivity/            # Productivity & career (~99)
│   ├── automation/                 # Workflow automation
│   ├── bottlenecks/                # Personal constraint diagnostics
│   ├── career/                     # Career exploration
│   ├── deep-work/                  # Personal focus systems
│   ├── prototyping/                # App prototyping
│   └── validation/                 # Decision validation
│
├── domain-image-generation/        # Image generation prompts (~75)
│   ├── branding/                   # Logos, icons, illustrations
│   ├── coloring-book/              # Coloring book illustrations
│   ├── healthcare/                 # Medical infographics
│   ├── worksheet-generators/       # Printable K-12 worksheet prompt generators
│   └── visualizations/             # Cross-role no-UI visualization prompt generators
│
├── domain-presentations/           # Presentations & decks (~48)
│   ├── board-decks/                # Board-deck image visual prompts (20, 16:9 format)
│   └── visual-planning/            # Frontier maps, visual QA harness, modality routing, cascade effects
│
├── domain-prompt-engineering/      # Meta-prompts about prompts (~47)
│   ├── prompt-improvement/         # Improve existing prompts
│   ├── model-behavior/             # Diagnose and correct model behavior vs. instructions
│   ├── escape-median/              # Move output off the model's default position/shape
│   ├── goal-orientation/           # Right-problem diagnostics, constraints, team audit
│   ├── skill-development/          # Four-discipline diagnostics, spec writing, eval harness, constraint architecture
│   ├── delegation/                 # Decide whether/how to delegate to AI
│   ├── prompt-optimization/        # Prompt optimization
│   ├── model-optimization/         # GPT/model-specific optimization
│   ├── utilities/                  # Prompt utilities
│   └── evaluation/                 # AI correctness, eval design, AI task difficulty
│
├── domain-decision-making/         # Decision frameworks (~27), scenario planning (scenario_*.md, 7), tradeoff analysis (tradeoff_*.md, 4)
│   └── documentation/              # Decision records: options memo, one-pager, narrative six-pager, log entry, post-decision review, AAR (6)
│
├── domain-reasoning-craft/         # Domain-general reasoning tools (41) — content-agnostic reasoning moves with machine-readable `reasoning:` frontmatter
│   ├── reasoning-moves/            # Named inference moves: Bayes update, Fermi, reference class, steelman, inversion, counterfactual, Toulmin, synthesis (14)
│   ├── forecasting/                # Forecasting practice loop: question design, decomposition, base rates, tripwires, calibration, Brier tracking (9)
│   ├── systems/                    # Feedback loops, causal loop diagrams, stocks/flows, archetypes, leverage points, unintended consequences (8)
│   └── epistemic/                  # Bias audits, motivated reasoning, evidence against yourself, red team, fallacy scan, source credibility (10)
│
├── domain-ideation/                # Divergent + convergent ideation: 100 ideas, SCAMPER, crazy eights, analogy mining, kill list, dot voting (12)
├── domain-risk/                    # Risk practice: register, FMEA, heat map, tail-risk scan, dependency chains, non-technical threat model, AAR (7)
├── domain-policy/                  # Policy analysis (4): options memo, problem framing, stakeholder/coalition map, implementation feasibility
├── domain-negotiation/             # Negotiation practitioner library (46 across 8 subdirs): preparation/ (10), at-the-table/ (7), channels/ (4), multi-party/ (4), after-the-deal/ (4), contexts/ (8), difficult-conversations/ (5, own prefix), craft/ (4)
├── domain-psy-ops/                 # Cognitive security: influence analysis & manipulation defense (32 across 6 subdirs, ANALYTIC/DEFENSIVE ONLY): technique-analysis/ (7), influence-operations/ (7), personal-defense/ (7, safety-gated), organizational-red-team/ (4), counter-messaging/ (4), case-studies-taxonomies/ (3)
├── domain-written-advocacy/        # LAYPERSON self-advocacy letters — cancellations, refunds, data deletion, warranty, hardship, appeals (35 across 7 subdirs): cross-cutting/ (6), accounts-and-billing/ (5), privacy-and-data/ (5), products-and-warranty/ (4), financial-hardship/ (6), insurance-and-medical/ (4), institutions-and-records/ (5). Non-adversarial sibling of domain-legal/personal-self-advocacy/
│
├── domain-deep-analysis/           # Multi-phase, multi-perspective deep-think systems for problems, decisions, plans, designs (8 prompts + 8 slash commands: each scope ships in rigorous and plain-English versions)
│   ├── deepthink_problem_analysis.md
│   ├── deepthink_problem_analysis_plain.md
│   ├── deepthink_decision.md
│   ├── deepthink_decision_plain.md
│   ├── deepthink_plan.md
│   ├── deepthink_plan_plain.md
│   ├── deepthink_design.md
│   ├── deepthink_design_plain.md
│   └── commands/                   # Slash commands: /deepthink-problem(-plain), /deepthink-decision(-plain), /deepthink-plan(-plain), /deepthink-design(-plain)
│
├── domain-idea-to-product/         # Self-contained idea-to-shippable-software pipeline (~63 prompts across 11 stages, AI-coding-agent build handoff)
│   ├── orchestrator_idea_to_product.md      # Master orchestrator (interview → classify → route → critique)
│   ├── README.md                            # How to use the domain (guided / manual / surgical modes)
│   ├── PIPELINE_OVERVIEW.md                 # Visual flow + branching logic + terminal artifacts
│   ├── stage-1-ideation/                    # Concept-legs test + divergent ideation prompts
│   ├── stage-2-problem-validation/          # JTBD + customer-discovery interview protocol
│   ├── stage-3-market-research/             # TAM/SAM/SOM + unit-economics designer (LTV/CAC/cohort)
│   ├── stage-4-business-model/              # Canvas + pricing + monetization model selection
│   ├── stage-5-strategy-positioning/        # SWOT + orchestrated 90-day GTM plan
│   ├── stage-6-decision-validation/         # Pre-mortem + blind-spot scan + am-i-being-nuts
│   ├── stage-7-prd-authoring/               # PRD + PRD-to-epic/feature decomposer with MVP/V1/V2 cuts
│   ├── stage-8-architecture-design/         # Deep-design + tech-stack selector (AI-agent friendliness scored)
│   ├── stage-9-phased-build-plan/           # Phased plan + sprint breakdown
│   ├── stage-10-ai-agent-handoff/           # PRD→agent-brief bridge + per-task acceptance specs + rules file + work loop + project memory
│   └── stage-11-build-risk-premortem/       # Failure-mode pre-mortem with verification attached
│
├── domain-professional-writing/    # Professional domain guides (~44)
│   ├── domain-specific/            # CPAs, attorneys, contractors, etc.
│   └── writing/                    # Business writing
│
├── domain-product-management/ # PRDs, stakeholder updates (~29)
│   ├── prompts/                    # Product management prompts
│   └── design/                     # Design-related prompts
│
├── domain-personal-development/    # Goals, habits, identity, agency, career, decisions, relationships, resilience, life-transitions, emotional-fitness (~166; see EXPANSION_ROADMAP.md)
│   ├── prompts/                    # Self-improvement prompts: agency/, identity/, goals/, habits/, resilience/, relationships/, productivity/, thinking/, stakeholder/, solo-dev/, career/ (AI-role assessments), life-transitions/ (navigating a change already underway), emotional-fitness/ (everyday NON-CLINICAL emotional skills — routes distress to domain-psychology/)
│   ├── career-transformation/      # Coordination-tax audit, structural vulnerability, residual skills, 90-day repositioning + AI-era skill moat, positioning statement, internal-vs-external move, reskilling roadmap
│   └── major-decisions/            # High-stakes personal decisions BEFORE the change (job offer, relocation, quit/persist, education, family, finance, health, purchase, cofounder, relationship, marriage/commitment, aging-parent care, sabbatical, start-business-vs-employment)
│
├── domain-healthcare-clinical/     # Clinical decision support, specialties, pharmacy, nursing, allied health (~41); medical education/HPE (~22)
│   └── prompts/                    # Healthcare prompts + medical-education/ subdirectory (22 HPE prompts)
│
├── domain-learning/                # Self-directed skill acquisition (5, domain-agnostic): curriculum designer, deliberate-practice loop, reading-list curator, concept-explanation (Feynman) audit, skill-gap-to-curriculum — DISTINCT from domain-learning-coding/
├── domain-learning-coding/         # Coding education (~17)
│
├── domain-research-academic/       # Research practice (15 prompts: question formulation → search → synthesis → instruments) + framework & field guide
│
├── domain-conversation-practice/   # Language conversation practice (~9)
│
├── domain-game-development/        # Game design, engines, multiplayer, graphics (~24)
│   ├── design/                     # GDD, core loops, mechanics, progression
│   ├── architecture/               # State machines, scene management, save systems
│   ├── engines/                    # Unreal Engine, Unity, Godot reviews
│   ├── testing/                    # Gameplay QA, automated testing, certification
│   ├── multiplayer/                # Netcode, state sync, matchmaking
│   ├── performance/                # Frame budgets, rendering optimization
│   ├── graphics/                   # Shaders, lighting strategy
│   ├── audio/                      # Audio system architecture
│   ├── level-design/               # Procedural generation
│   └── economy/                    # Game economy design
│
├── domain-creative-writing/        # Adult/mature creative writing across 7 subdirs (fiction, craft-tools, genre-workshops, creative-nonfiction, poetry, script-stage, publishing-career): story structure, scene/POV/pacing, character/voice/dialogue, show-don't-tell, description, theme, openings/endings, revision, beta-reader synthesis, genre + mystery/speculative deep-dives, memoir + narrative nonfiction, poetry/imagery, screenplay, query/synopsis/pitch (27). Adult only — kids → domain-childrens-writing; business prose → domain-professional-writing
├── domain-childrens-writing/       # Authoring kid-friendly material across 5 subdirs (fiction-workshops, nonfiction-workshops, craft-tools, representation-collaboration, publishing-business): board→picture→early/chapter→middle-grade→YA-crossover fiction, verse novel, graphic novel, narrative + STEM nonfiction, craft tools (openings, dialogue, character, revision, reading-level, rhythm, sensitive topics), representation/illustrator, query/synopsis/pitch (22)
├── domain-education-teaching/      # 267 prompts in 3 audience tracks — instructor/ (104: lesson planning, explanation craft, response cycle, assessment items/design/analysis, grading, reporting, student support, classroom ops, ed-tech, higher-ed & corporate, subject pedagogy), program/ (41: curriculum design, outcomes assessment, accreditation, faculty development, evaluation analytics), learner/ (122: note-taking, memory & recall, self-assessment, exam prep, study by discipline, tutoring, stuck-and-confused, writing, reading, math/science, language, research, time & discussion, adult learners, chained guides)
├── domain-parenting/               # Parenting prompts ages 4-8, ADHD/autism/strong-willed adaptations (~18)
├── domain-legal/                   # Practitioner legal prompts: research, litigation, discovery, depositions,
│                                   # contracts/transactional, M&A, employment, IP, client intake, in-house/legal-ops (~67);
│                                   # divorce (22), custody (20); family-self-advocacy/ (23, LITIGANT-FACING layperson prep)
├── domain-biblical-studies/        # Bible study & research (129, TRADITION-NEUTRAL, anti-fabrication-first):
│   ├── exegesis-interpretation/    # passage exegesis, word study, genre, context, narrative/rhetorical/ANE analysis, multi-view, translation + genre deep-dives (parable, prophecy/apocalyptic, poetry, wisdom, law, epistle) (18)
│   ├── study-methods-teaching/     # inductive/SOAP, book overview, discussion guides, lesson plans, reading/memorization (8)
│   ├── sermon-devotional/          # expository/topical/evangelistic/occasional sermon prep, illustrations, devotionals, meditation, application, manuscript draft, delivery coaching, lectionary prep, liturgical-calendar devotionals (14)
│   ├── theology-research/          # topical/systematic synthesis, doctrine, view comparison, typology, hard passages, historical theology, biblical ethics, book theology, source map, position stress-test, exegetical-fallacy detector, commentary evaluation, creed/confession analysis, worship-practice biblical basis, church government/polity (17)
│   ├── learner-self-study/         # SELF-DIRECTED LEARNER (S): study plan, character study, self-quiz, doctrine self-exploration, doubt explorer, study-tool skills, comprehension check, application, journaling, reading habit builder, single-book deep dive, tradition comparison on practices (12) — boundary guardrail: not counseling/crisis
│   ├── ministry-contexts/          # MINISTRY-CONTEXT TEACHER (M): kids' lessons, youth study, new-believer discipleship, seeker intro, family devotions, special programs, care-conversation foundations, men's/women's study, college/young-adult study, seniors' study + cross-domain bridges: grief/loss Scripture guide, marriage enrichment, parenting Scripture guide (13) — child-safety + care guardrails
│   ├── church-staff-ministry-ops/  # CHURCH STAFF (P/G): curriculum scope & sequence, curriculum evaluation, teacher training, multi-service coordination, annual calendar, volunteer roles, small-group launch, discipleship pathway, midweek programs, sermon debrief (10)
│   ├── group-leader-facilitation/  # GROUP LEADER (G/P): facilitation dynamics, hard questions, heretical-claim response (STRONG-GUARD), mixed-maturity leveling, conflict resolution, hybrid/online format, apprentice development (7)
│   ├── original-languages/         # Greek/Hebrew/Aramaic tooling (18, all STRONG-GUARD, highest fabrication risk): parsing/morphology, Greek syntax, Hebrew syntax, Greek verbal aspect, Greek voice/deponency, discourse analysis, idiom/figures of speech, semantic domains (Louw-Nida), OT-in-NT usage, Septuagint usage, textual criticism, Masorah/Qere-Ketiv, cantillation/accentuation, Aramaic analysis, canon/versification differences, comparative Semitics/cognates, Koine papyri/inscriptions register, vocabulary builder
│   ├── biblical-theology-method/   # METHOD-LEVEL (A/P): biblical vs systematic theology, redemptive-historical reading (STRONG-GUARD), author theology comparison (STRONG-GUARD), center-of-theology debate (STRONG-GUARD) (4)
│   └── apologetics-engagement/     # APOLOGETICS (P/A): objection engagement, Bible reliability, comparative worldview, faith & science, conversation prep, problem of evil/theodicy, biblical contradictions, interfaith dialogue (8) — all STRONG-GUARD except conversation prep; custom banner for fabricated arguments, misrepresented worldviews, invented evidence
│
├── domain-discipleship/            # One-to-one discipleship & mentorship (73, TRADITION-NEUTRAL, FORMATION IS NOT A METRIC).
│   │                               # Orchestrates domain-biblical-studies/ for all Scripture work; never duplicates it.
│   ├── curriculum-architecture/    # Multi-stage curriculum blueprint (flagship), formation outcomes (anti-scoring), module scope & sequence, balance audit, material evaluation (STRONG-GUARD), multiplication design, multi-generation governance & material drift (7)
│   ├── learner-pathways/           # LEARNER-VOICE: growth self-assessment, personal growth plan, spiritual practices (seven streams), stalled-growth diagnostic (clinical screen first), returning believer, life-constraints adaptation (6)
│   ├── mentor-equipping/           # THE DISCIPLER: readiness assessment, training curriculum, conversation skills, boundaries & referral (LOAD-BEARING SAFETY), support & sustainability, season debrief, case consultation, doubt & deconstruction posture (STRONG-GUARD) (8)
│   ├── pairing-and-relationship/   # Pairing criteria (3 tiers, safety never traded), covenant (confidentiality limits before disclosure), first meeting, cadence, ending well (5 ending types), long-relationship re-contracting, informal pairing with no program (STRONG-GUARD), what to expect as a mentee (8)
│   ├── session-and-lesson/         # Session shape, lesson builder, question bank (3 depth tiers + too-far lines), hard-conversation navigation (event-triggered), small-group format, accessibility design (6)
│   ├── program-operations/         # Program blueprint (safeguarding gate), safeguarding & conduct policy (STRONG-GUARD, no statute from memory), onboarding, health review, mentor pipeline, minimum viable program, control-drift audit (STRONG-GUARD) (7)
│   ├── topical-modules/            # Module DESIGNERS for the hard topics: money, work, sexuality & singleness (STRONG-GUARD), forgiveness, suffering & lament, anger & conflict, digital life, witness in a hostile setting (8)
│   ├── life-stage-tracks/          # Youth & teen (STRONG-GUARD, safeguarding-gated), college/young adult, married couples (abuse screen first), parents, seniors (5)
│   ├── context-variants/           # Someone else's rules govern: prison & re-entry, campus ministry, workplace/marketplace, remote & diaspora (4)
│   ├── initiation-and-catechesis/  # Baptism prep, membership prep (full disclosure before commitment), catechesis design — highest tradition divergence, multi-view (3)
│   ├── cross-cultural/             # Ask-don't-assert: cross-cultural discipling, oral-preference learners, translated-material audit (3)
│   ├── peer-and-accountability/    # Sideways relationships: mentor peer cohort (curriculum + facilitation), accountability partnership (design + conversation), anti-surveillance (4)
│   └── after-harm/                 # AFTER IT WENT WRONG (never adjudicates, disciplines, or treats): harmed by a previous discipling relationship (STRONG-GUARD), dependency & over-attachment, mentor's own mistake repair, after a mentor is removed (STRONG-GUARD) (4)
│
├── domain-specialized-fields/      # Legal, trades, real estate, marketing (guide hub; finance + psychology promoted to top-level domains)
├── domain-finance/                 # Finance & economics field guide (promoted from domain-specialized-fields/finance)
├── domain-psychology/              # Psychology, therapy & behavioral health (~99; promoted from domain-specialized-fields/psychology)
│
├── domain-medical-education/       # Health-professions education (213): educator-* tracks (case writing, assessment items,
│                                   # rubrics/WBA, simulation, curriculum, remediation) + learner-* tracks (clinical reasoning,
│                                   # foundational sciences, OSCE skills, clinical rotation, boards, procedures, study systems)
│                                   # + profession-specific/ (nursing, pharmacy, EMS, dental, PA, allied).
│                                   # Teaches and assesses clinicians; real-patient questions → domain-healthcare-clinical/
├── domain-voice-conversational-ui/ # Voice & conversational UI (28): voice design, chatbot design, dialog architecture,
│                                   # NLU training, voice UX, multimodal, platform-specific, analytics
│
├── techniques/                     # Prompt engineering reference
│   ├── MASTER_TECHNIQUE_INDEX.md
│   └── USE_CASE_LOOKUP.md
│
├── authoring/                      # Resource creation guides
│   ├── skill-patterns/             # Skill authoring system
│   ├── agent-patterns/             # Agent authoring patterns
│   ├── command-patterns/           # Command authoring patterns
│   └── system-patterns/            # Agentic-system authoring manual
│
├── portable-prompt-system/         # Self-contained, drop-in export of the technique library + authoring guides.
│                                   # Copy the folder into any project to author prompts at this repo's quality.
│                                   # Vendors copies of techniques/ and authoring/ — registered in meta/VENDORED.tsv
│
├── continuity-kit/                 # Project Continuity Memory: a repo-local, human-readable ledger of durable project
│                                   # state (decisions, failures, open threads) so agents and humans resume across
│                                   # sessions. Installable package with its own CLI and test suite.
│
├── scripts/                        # Index generation, naming/link validation, reorg tooling, vendored-copy drift check
│
└── meta/                           # REORG_MAP.tsv (every move and deletion) + VENDORED.tsv (canonical → copy)
```

---

## Category Mapping: User Intent → Repository Location

When users need **help with tasks** (not asking for new prompts), map their request to existing prompts:

### Code & Technical Analysis
- **Security issues** → `domain-software-engineering/analysis/security/` (~22 prompts)
  - Example: "Find security vulnerabilities" → `security_vulnerability_analysis.md`
  - Example: "Check for SQL injection" → `security_sql_injection_analysis.md`
  - Example: "LLM / AI application security review" → `security_llm_application_review.md`
  - Example: "SBOM / supply chain review" → `security_sbom_supply_chain_review.md`

- **Bug bounty hunting (offensive, AUTHORIZED, live targets)** → `domain-software-engineering/bug-bounty/` (20 prompts + README)
  - **Distinct from `analysis/security/`:** that directory is DEFENSIVE (review code you own); this is the bug-bounty HUNTER workflow — black-box testing of in-scope assets you've been granted permission to test, ending in a paid disclosure report.
  - **Load-bearing convention** (see [README](../domain-software-engineering/bug-bounty/README.md)): every prompt enforces an authorization/scope gate + responsible disclosure (no out-of-scope, destructive, DoS, or mass-targeting content).
  - Example: "I'm new to bug bounties — orient me + first 90 days" → `bug-bounty/bugbounty_getting_started_orientation.md`
  - Example: "Parse a program's scope into a compliant test plan" → `bug-bounty/bugbounty_program_scope_analyzer.md`
  - Example: "Which programs are worth my time (ROI)?" → `bug-bounty/bugbounty_program_selection_roi.md`
  - Example: "Map and prioritize a target's attack surface" → `bug-bounty/bugbounty_recon_attack_surface_map.md`
  - Example: "Turn a fingerprinted stack into a threat profile" → `bug-bounty/bugbounty_tech_stack_threat_profile.md`
  - Example: "Hunt broken access control / IDOR" → `bug-bounty/bugbounty_access_control_idor_hunt.md`
  - Example: "Hunt auth / session / OAuth / JWT / MFA flaws" → `bug-bounty/bugbounty_authentication_session_hunt.md`
  - Example: "Hunt SSRF" → `bug-bounty/bugbounty_ssrf_hunt.md`
  - Example: "Hunt injection (SQLi / command / SSTI / NoSQL)" → `bug-bounty/bugbounty_injection_hunt.md`
  - Example: "Hunt XSS (reflected / stored / DOM)" → `bug-bounty/bugbounty_xss_hunt.md`
  - Example: "Hunt business-logic flaws" → `bug-bounty/bugbounty_business_logic_hunt.md`
  - Example: "Test a REST / GraphQL API (BOLA/BFLA, mass assignment)" → `bug-bounty/bugbounty_api_graphql_hunt.md`
  - Example: "Test a mobile app + its backend" → `bug-bounty/bugbounty_mobile_app_hunt.md`
  - Example: "Hunt cloud/infra (subdomain takeover, exposed secrets, CORS)" → `bug-bounty/bugbounty_cloud_infra_hunt.md`
  - Example: "Validate a finding before reporting (go/no-go)" → `bug-bounty/bugbounty_finding_triage_validation.md`
  - Example: "Score severity (CVSS) + articulate impact" → `bug-bounty/bugbounty_severity_cvss_impact.md`
  - Example: "Build a safe, minimal proof of concept" → `bug-bounty/bugbounty_poc_builder.md`
  - Example: "Write a disclosure report" → `bug-bounty/bugbounty_disclosure_report_writer.md`
  - Example: "Build a skill-development plan" → `bug-bounty/bugbounty_skill_development_plan.md`
  - Example: "Post-mortem an accepted/rejected/duplicate report" → `bug-bounty/bugbounty_report_postmortem.md`

- **Code quality** → `domain-software-engineering/analysis/quality/` (~7 prompts)
  - Example: "Code is too complex" → `quality_code_complexity_analysis.md`
  - Example: "Find duplicated code" → `quality_code_duplication_analysis.md`

- **Performance** → `domain-software-engineering/analysis/performance/` (~7 prompts)
  - Example: "App is slow" → `performance_bottleneck_identification.md`
  - Example: "Optimize this" → `performance_code_optimization_suggestions.md`

- **Architecture** → `domain-software-engineering/analysis/architecture/` (~9 prompts)
  - Example: "Review architecture" → `architecture_layer_identification.md`
  - Example: "Find design patterns" → `architecture_design_pattern_identification.md`

- **Code evolution** → `domain-software-engineering/analysis/evolution/` (~6 prompts)
  - Example: "Where's the tech debt?" → `evolution_technical_debt_estimation.md`
  - Example: "Find hotspots" → `evolution_code_churn_analysis.md`

### Testing
- **Any testing task** → `domain-software-engineering/testing/` (~16 prompts)
  - Example: "Generate unit tests" → `testing_unit_test_generation.md`
  - Example: "E2E test plan" → `testing_e2e_test_scenario_creation.md`
  - Example: "Check accessibility" → `testing_accessibility_wcag.md`
  - Example: "Contract testing (Pact / OpenAPI / AsyncAPI)" → `testing_contract_test_design.md`
  - Example: "Property-based / fuzz tests" → `testing_property_based_fuzzing.md`
  - Example: "Chaos engineering plan" → `testing_chaos_engineering_plan.md`

### DevOps & Infrastructure
- **DevOps/Infrastructure** → `domain-software-engineering/devops/` (~21 prompts)
  - Example: "Review Dockerfile" → `devops_dockerfile_optimization.md`
  - Example: "CI/CD pipeline help" → `devops_cicd_pipeline_analysis.md`
  - Example: "Terraform review" → `devops_terraform_best_practices.md`
  - Example: "GitOps / ArgoCD / Flux review" → `devops_gitops_workflow_review.md`
  - Example: "OpenTelemetry instrumentation review" → `devops_opentelemetry_instrumentation.md`

### Cloud
- **Cloud infrastructure** → `domain-software-engineering/cloud/` (~22 prompts)
  - Example: "AWS architecture review" → `cloud_aws_architecture_review.md`
  - Example: "Reduce cloud costs" → `cloud_cost_optimization.md`
  - Example: "Review Lambda functions" → `cloud_serverless_analysis.md`
  - Example: "FinOps cost allocation / showback" → `cloud_finops_cost_allocation.md`

### API Design
- **API tasks** → `domain-software-engineering/api/` (~6 prompts)
  - Example: "REST API review" → `api_rest_design_review.md`
  - Example: "GraphQL schema help" → `api_graphql_schema_analysis.md`
  - Example: "gRPC service design review" → `api_grpc_service_design.md`
  - Example: "OpenAPI linting / governance" → `api_openapi_linting_governance.md`

### Mobile Development
- **Mobile apps** → `domain-software-engineering/mobile/` (~255 prompts)
  - Example: "Review iOS app" → `mobile_ios_architecture_review.md`
  - Example: "Android best practices" → `mobile_android_kotlin_best_practices.md`
  - Example: "React Native performance" → `mobile_react_native_optimization.md`

### Frontend Development
**Domain guide:** [`domain-frontend-development/README.md`](../domain-frontend-development/README.md) — 47 prompts across 18 categories (frameworks + cross-cutting craft + build tooling + quality concerns). All Tier 1, fully cross-referenced via `related_prompts`.

**Frameworks:**
- **React** → `domain-frontend-development/react/` (6): component patterns, hooks, state, testing, performance, `frontend_react_server_components_streaming.md` (RSC & streaming SSR)
- **Vue** → `domain-frontend-development/vue/` (4): Composition API, Pinia state, testing, `frontend_vue_advanced_reactivity_performance.md`
- **Angular** → `domain-frontend-development/angular/` (4): architecture, reactive patterns, testing, `frontend_angular_signals_advanced.md` (advanced signals / zoneless)
- **Next.js** → `domain-frontend-development/nextjs/` (4): App Router, data fetching, performance, `frontend_nextjs_server_actions_mutations.md`
- **Svelte / SvelteKit** → `domain-frontend-development/svelte/` (3): component patterns/runes, state, full-stack
- **Astro** → `domain-frontend-development/astro/` (2): `frontend_astro_islands_architecture.md`, `frontend_astro_content_collections.md`
- **SolidJS** → `domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md`
- **Qwik** → `domain-frontend-development/qwik/frontend_qwik_resumability.md`
- **Remix / React Router** → `domain-frontend-development/remix/frontend_remix_data_loading.md`

**Cross-cutting craft (framework-agnostic):**
- **Styling** → `domain-frontend-development/styling/` (3): `frontend_styling_css_architecture.md`, `frontend_styling_tailwind_design_system.md`, `frontend_styling_css_in_js_review.md`
- **TypeScript** → `domain-frontend-development/typescript/` (2): `frontend_typescript_component_typing.md`, `frontend_typescript_type_safety_audit.md`
- **Forms** → `domain-frontend-development/forms/` (2): `frontend_forms_validation_design.md`, `frontend_forms_accessibility_ux.md`
- **Animation** → `domain-frontend-development/animation/frontend_animation_motion_performance.md`
- **Architecture** → `domain-frontend-development/architecture/` (3): `frontend_error_boundary_resilience.md`, `frontend_state_management_selection.md`, `frontend_i18n_localization.md`
- **Build tooling** → `domain-frontend-development/build-tooling/` (3): `frontend_build_vite_optimization.md`, `frontend_build_micro_frontends_module_federation.md`, `frontend_build_bundler_migration.md`

**Quality concerns:**
- **Accessibility** → `domain-frontend-development/accessibility/` (3): WCAG audit, ARIA patterns, screen reader testing
- **Frontend performance** → `domain-frontend-development/performance/` (2): Core Web Vitals, bundle optimization
- **Frontend testing** → `domain-frontend-development/testing/` (2): Jest, Playwright E2E

### Vibe Coding Rescue (AI-Assisted Project Recovery)
- **Rescue an AI-assisted project that's hit a wall** → `domain-software-engineering/vibe-coding-rescue/` (5 general prompts)
  - Example: "Diagnose why my vibe-coded project isn't progressing" → `viberescue_wall_diagnosis.md`
  - Example: "Build a rules file for this codebase" → `viberescue_rules_file_design.md`
  - Example: "The AI keeps failing at this task — decompose it" → `viberescue_decompose_stuck_task.md`
  - Example: "Audit AI-generated code for security issues" → `viberescue_security_audit.md`
  - Example: "Generate a handoff briefing for a new engineer" → `viberescue_engineer_handoff_briefing.md`
- **Rescue a vibe-coded Android app** → `domain-software-engineering/vibe-coding-rescue/android/` (6 prompts + README — run in sequence)
  - Example: "Diagnose what's wrong with my vibe-coded Android app" → `android/android_viberescue_wall_diagnosis.md`
  - Example: "Audit my Android codebase for AI-fragility patterns" → `android/android_viberescue_codebase_audit.md`
  - Example: "Android security/privacy audit (manifest, WebView, deeplinks, auth)" → `android/android_viberescue_security_privacy_audit.md`
  - Example: "Turn audit findings into a ranked fix queue" → `android/android_viberescue_fix_prioritization.md`
  - Example: "Safely execute one fix from the queue (test-first, one-per-commit)" → `android/android_viberescue_fix_executor.md`
  - Example: "Generate a project rules file (CLAUDE.md) from audit evidence" → `android/android_viberescue_rules_file.md`

### AI-Native Rollouts (Team / Org AI Adoption)
- **Roll out AI tools, agentic workflows, or team-level AI practice** → `domain-engineering-workflows/ai-native-rollouts/` (6 prompts)
  - Example: "Design an ambient AI code-review system" → `airollout_ambient_code_review.md`
  - Example: "Design a tiered AI-adoption rollout" → `airollout_tiered_adoption_rollout.md`
  - Example: "Ship a real change without writing code" → `airollout_ship_without_writing_code.md`
  - Example: "Delegate to AI like a parallel coworker" → `airollout_delegate_like_parallel_coworker.md`
  - Example: "Set up long-running project memory" → `airollout_long_running_project_memory.md`
  - Example: "Plan migration of an organizational bottleneck to AI" → `airollout_bottleneck_migration_plan.md`

### Game Development
- **Game design** → `domain-game-development/design/` (~4 prompts)
  - Example: "Create a GDD" → `design_game_design_document.md`
  - Example: "Analyze core loop" → `design_core_loop_analysis.md`
  - Example: "Design progression system" → `design_player_progression.md`

- **Game architecture** → `domain-game-development/architecture/` (~3 prompts)
  - Example: "Design state machine" → `architecture_state_machine_design.md`
  - Example: "Scene loading system" → `architecture_scene_management.md`
  - Example: "Save system design" → `architecture_save_system.md`

- **Engine-specific review** → `domain-game-development/engines/` (~4 prompts)
  - Example: "Review Unreal Blueprints" → `engines_unreal_blueprint_review.md`
  - Example: "Unreal C++ review" → `engines_unreal_cpp_patterns.md`
  - Example: "Unity architecture review" → `engines_unity_architecture_review.md`
  - Example: "Godot project review" → `engines_godot_architecture_review.md`

- **Game testing** → `domain-game-development/testing/` (~3 prompts)
  - Example: "Game test plan" → `testing_gameplay_test_plan.md`
  - Example: "Automated game testing" → `testing_automated_game_testing.md`
  - Example: "Platform certification" → `testing_platform_certification.md`

- **Multiplayer/networking** → `domain-game-development/multiplayer/` (~3 prompts)
  - Example: "Netcode architecture" → `multiplayer_netcode_architecture.md`
  - Example: "State sync design" → `multiplayer_state_sync.md`
  - Example: "Matchmaking system" → `multiplayer_matchmaking_lobby.md`

- **Game performance** → `domain-game-development/performance/` (~2 prompts)
  - Example: "Frame budget analysis" → `performance_frame_budget_analysis.md`
  - Example: "Rendering optimization" → `performance_rendering_optimization.md`

- **Graphics/shaders** → `domain-game-development/graphics/` (~2 prompts)
  - Example: "Shader review" → `graphics_shader_review.md`
  - Example: "Lighting strategy" → `graphics_lighting_strategy.md`

- **Game audio** → `domain-game-development/audio/` (~1 prompt)
  - Example: "Audio system design" → `audio_system_architecture.md`

- **Level design** → `domain-game-development/level-design/` (~1 prompt)
  - Example: "Procedural generation" → `level_procedural_generation.md`

- **Game economy** → `domain-game-development/economy/` (~1 prompt)
  - Example: "Economy design" → `economy_system_design.md`

### Learning & Teaching
- **Teaching/Learning to code** → `domain-learning-coding/` (~17 prompts)
  - Example: "Teach me this code" → `learning_teach_me_to_code.md`
  - Example: "Create code exercises" → `learning_code_refactoring_exercises.md`

### Engineering Workflows
- **Project planning** → `domain-engineering-workflows/workflows/` (~51 prompts)
  - Example: "Plan sprint" → `engineering_delivery_sprint_planner.md`
  - Example: "Debug this issue" → `engineering_prompt_for_debugging_code.md`
  - Example: "Postmortem" → `engineering_post_mortem_root_cause_ladder.md`

### Career & Work Transformation
- **Career-level diagnostics & repositioning** → `domain-personal-development/career-transformation/` (4 prompts)
  - Example: "Audit my work week against coordination-tax categories" → `career_coordination_tax_audit.md`
  - Example: "Assess my role's structural vulnerability" → `career_role_structural_vulnerability.md`
  - Example: "Inventory my residual skills that survive automation" → `career_residual_skills_inventory.md`
  - Example: "Build a 90-day repositioning plan" → `career_90_day_repositioning_plan.md`

### Identity (Values, Self-Talk, Comparison, Confidence, Purpose, Life Audit, Taste)
- **The third axis** — not action (agency), not cognition (thinking), but identity work → `domain-personal-development/prompts/identity/` (7 prompts)
  - Example: "Surface my values from past decisions" → `identity_values_clarification.md`
  - Example: "Audit the inner critic's specific sentences" → `identity_self_talk_audit.md`
  - Example: "Diagnose what my envy is pointing at" → `identity_comparison_envy_diagnostic.md`
  - Example: "Calibrate confidence — impostor or overconfidence" → `identity_confidence_calibration.md`
  - Example: "Diagnose loss of purpose ('why')" → `identity_purpose_reignition.md`
  - Example: "Structured audit at a major life inflection" → `identity_life_audit_reckoning.md`
  - Example: "Develop taste / discernment in a specific domain" → `identity_taste_development.md`
- **Burnout recovery + decision post-mortem** (paired with the identity set) → `domain-personal-development/prompts/agency/`
  - Example: "Diagnose burnout stage and choose recovery path" → `agency_burnout_recovery.md`
  - Example: "Post-decision regret analysis (was I right?)" → `agency_decision_post_mortem.md`

### Productivity Reviews (Cadence)
- **Time audit, weekly systems review, monthly/quarterly cadence** → `domain-productivity/reviews/` (3 prompts)
  - Example: "Reconcile last week's plan with what actually happened" → `reviews_time_audit_evidence_based.md`
  - Example: "Weekly systems-health review" → `reviews_weekly_systems_review.md`
  - Example: "Monthly or quarterly cadence review" → `reviews_monthly_quarterly_cadence.md`

### Productivity Bottlenecks (New Additions)
- **Procrastination, capture/triage, perfectionism, PKM** → `domain-productivity/bottlenecks/`
  - Example: "Diagnose procrastination on a specific task" → `bottleneck_procrastination_systems_diagnostic.md`
  - Example: "Design a personal capture/triage system" → `bottleneck_capture_triage_system_design.md`
  - Example: "Set a ship threshold / stop polishing" → `bottleneck_perfectionism_ship_threshold.md`
  - Example: "Design a personal knowledge system" → `bottleneck_pkm_second_brain_architecture.md`

### Deep Work (New Additions)
- **Environment friction + future-self handoff** → `domain-productivity/deep-work/`
  - Example: "Engineer defaults and friction in my workspace" → `deepwork_environment_friction_design.md`
  - Example: "Write a handoff to my future self" → `deepwork_future_self_handoff.md`

### Visual / Frontier Planning (Upstream of Presentations)
- **Plan, route, and QA visual work before producing it** → `domain-presentations/visual-planning/` (4 prompts)
  - Example: "Map the frontier of what a capability unlocks" → `visualplan_capability_frontier_map.md`
  - Example: "Design a QA harness for visual work" → `visualplan_visual_qa_harness.md`
  - Example: "Route this task to the right modality" → `visualplan_modality_router.md`
  - Example: "Scan for cascade effects of this capability" → `visualplan_cascade_effects_scan.md`

### Business & Strategy
- **Company strategy** → `domain-business-strategy/` (64 prompts across ai-strategy, ambition-leverage, go-to-market, research, startup)
- **Business frameworks applied to a codebase** → `domain-software-engineering/analysis/business/` (20 prompts)
  - These take a *repository* as input and infer business meaning from code; every one is titled "… for Codebase".
  - Example: "SWOT analysis of this codebase" → `swot_analysis.md`
  - Example: "Business model canvas from the code" → `business_model_canvas_analysis.md`
  - Example: "Infer OKRs from what the code does" → `okr_analysis.md`

### Chief-of-Staff / Personal Operating Cadence
- **Self-directed exec-level operating rhythm** → `domain-productivity/operating-cadence/` (11 prompts)
  - Example: "Clarify a fuzzy goal into actionable intent" → `cos_clarify_fuzzy_goals.md`
  - Example: "Parse a brain dump into tasks / decisions / worries / waiting-fors" → `cos_brain_dump_to_tasks.md`
  - Example: "Spec a delegation brief for a sub-agent" → `cos_specify_subagent_task.md`
  - Example: "Morning briefing from calendar + commitments + waiting-fors" → `cos_morning_briefing.md`
  - Example: "Pre-meeting brief + post-meeting note processor" → `cos_meeting_prep_and_process.md`
  - Example: "End-of-day reconciliation with reload capture" → `cos_end_of_day_reconciliation.md`
  - Example: "Weekly review: close state + set up next week" → `cos_weekly_review.md`
  - Example: "Author a personal / role CLAUDE.md memory scaffold" → `cos_memory_scaffold_claude_md.md`
  - Example: "Define sub-agent authority (Can do / Ask first / Never)" → `cos_authority_boundaries.md`

### AI Strategy & Context Accumulation
- **Enterprise AI strategy framing and analysis** → `domain-business-strategy/ai-strategy/` (4 prompts)
  - Example: "Map where organizational understanding accumulates" → `aistrategy_context_accumulation_map.md`
  - Example: "Estimate AI vendor switch cost at a future date" → `aistrategy_vendor_switch_cost.md`
  - Example: "Evaluate whether a capability compounds or stays flat" → `aistrategy_capability_compounding_evaluation.md`
  - Example: "Enterprise AI platform strategy brief (board-ready)" → `aistrategy_platform_brief.md`

### Ambition & Leverage
- **Leadership ambition conversations in the AI era** → `domain-business-strategy/ambition-leverage/` (4 prompts)
  - Example: "Leadership audit: stated vs revealed ambition" → `ambition_leadership_audit.md`
  - Example: "Roadmap for turning domain experts into builders" → `ambition_experts_to_builders_roadmap.md`
  - Example: "Expansion vs pocketing AI savings (board brief)" → `ambition_expansion_vs_savings_brief.md`
  - Example: "Compress insight-to-action lead time in a workflow" → `ambition_insight_to_action_workflow.md`

### Browser / Workflow Automation Readiness
- **Per-user or per-team browser-automation operating cycle** → `domain-productivity/automation/` (4 `browserauto_*` prompts)
  - Example: "Weekly automation audit of repetitive browser tasks" → `browserauto_weekly_audit.md`
  - Example: "Design a recording blueprint before opening a recorder" → `browserauto_recording_blueprint.md`
  - Example: "Design a multi-tab intelligence-gathering operation" → `browserauto_multi_tab_intel.md`
  - Example: "Pre-flight safety check before activating an automation" → `browserauto_safety_check.md`

### Task Management
- **Prioritizing your own work** → `domain-productivity/daily-planning/` (`daily_priority_triage.md`, `daily_task_list_builder.md`) or `domain-productivity/workplace/work_deadline_juggler.md`
- **Choosing a prioritization framework** (RICE / ICE / WSJF / MoSCoW / Kano) → `domain-decision-making/decisioning_prioritization_framework_selector.md`
- **Building a task-sorting *feature*** → `domain-software-engineering/analysis/feature-design/` (3 prompts)
  - Example: "Design the sorting algorithm for my to-do app" → `task_sorting_algorithm_designer.md`

### Improvement
- **General code improvement** → `domain-software-engineering/improvement/` (4 prompts)
  - Example: "Refactor this" → `improvement_refactoring.md`
  - Example: "Audit this repo end to end" → `improvement_repo_audit_master_prompt.md`

### Validation & Self-Check
- **Decision validation** → `domain-productivity/validation/` (~35 prompts)
  - Example: "Check my reasoning" → `validation_adversarial_mini_check.md`
  - Example: "Am I being nuts?" → `validation_am_i_being_nuts.md`
  - Example: "Verify before shipping" → `validation_final_gate.md`

### Business Research
- **Web research** → `domain-business-strategy/research/` (~7 prompts)
  - Example: "Research competitors" → `research_competitive_landscape.md`
  - Example: "Company deep dive" → `research_company_deep_dive.md`
  - Example: "Prepare for meeting" → `research_person_background.md`

### Workspace Organization
- **Document organization** → `domain-business-strategy/organization/` (3 prompts)
  - Example: "Content audit" → `domain-productivity/bottlenecks/bottleneck_content_audit.md`
  - Example: "Knowledge base gap analysis" → `domain-productivity/bottlenecks/bottleneck_knowledge_base_gap_analysis.md`
  - Example: "Project status summary" → `domain-engineering-workflows/workflows/engineering_project_status_summary.md`

### App Prototyping
- **Build apps** → `domain-software-engineering/prototyping/` (6 prompts)
  - Example: "Build a CRM" → `prototyping_personal_crm.md`
  - Example: "Create landing page" → `prototyping_landing_page.md`
  - Example: "Event registration" → `prototyping_event_registration.md`

### Workflow Automation
- **Automation workflows** → `domain-productivity/automation/` (~6 prompts)
  - Example: "Daily check-in" → `automation_daily_accountability.md`
  - Example: "Route leads" → `automation_lead_routing.md`
  - Example: "Sync data" → `automation_data_sync.md`

### Decision Making
- **Decisioning prompts** → `domain-decision-making/`
  - Example: "Blind spot check" → `decisioning_blind_spot_identifier.md`
  - Example: "Rapid weighted tradeoff analysis" → `decisioning_comprehensive_rapid_tradeoff_analyzer.md`
  - Example: "Ask-don't-answer interrogation / question generator" → `decisioning_interrogative_mode.md`
  - Additional tradeoff-analysis prompts live in `domain-decision-making/tradeoff_*.md` (see below)
- **Scenario planning** → `domain-decision-making/scenario_*.md` (7 prompts)
  - Example: "2x2 scenario matrix" → `scenario_two_by_two_matrix.md`
  - Example: "Backcast from a desired/feared future" → `scenario_backcasting.md`
  - Example: "Test a strategy against every scenario" → `scenario_robustness_test.md`
  - Example: "Early-warning signposts and triggers" → `scenario_signposts_and_triggers.md`
  - Example: "Pre-mortem the whole strategy at year 3" → `scenario_strategic_pre_mortem.md`
  - Example: "Three-horizons roadmap" → `scenario_multi_horizon_roadmap.md`
  - Example: "Stress-test with wild cards" → `scenario_wild_card_injection.md`
- **Tradeoff analysis** → `domain-decision-making/tradeoff_*.md` (4 prompts)
  - Example: "MCDA / weighted scoring with sensitivity analysis" → `tradeoff_multi_criteria_decision_analysis.md`
  - Example: "Compare options against a baseline (Pugh)" → `tradeoff_pugh_matrix.md`
  - Example: "Reframe an irreversible commit as staged options" → `tradeoff_real_options_framing.md`
  - Example: "Reversibility × stakes triage (one-way vs two-way doors)" → `tradeoff_reversibility_stakes_grid.md`
- **Decision documentation** → `domain-decision-making/documentation/` (6 prompts)
  - Example: "Options memo / decision memo" → `decisiondoc_options_memo.md`
  - Example: "One-page decision summary" → `decisiondoc_one_pager.md`
  - Example: "Narrative six-pager (Bezos-style)" → `decisiondoc_narrative_memo_bezos.md`
  - Example: "Decision log entry" → `decisiondoc_log_entry.md`
  - Example: "Post-decision review at a pre-committed checkpoint" → `decisiondoc_post_decision_review.md`
  - Example: "After-action report" → `decisiondoc_after_action_report.md`

### Reasoning Craft (Domain-General Reasoning Tools)
- **Single named reasoning moves, forecasting practice, systems thinking, epistemics** → `domain-reasoning-craft/` (41 prompts; see [README](../domain-reasoning-craft/README.md)). Content-agnostic: the same move works on product, policy, or personal questions. Every prompt carries a machine-readable `reasoning:` frontmatter block (styles, stakes, horizon, uncertainty, mode) indexed in PROMPT_INDEX.json.
  - **Reasoning moves** → `reasoning-moves/` (14): Bayesian update, abduction, analogy, counterfactual, Fermi, first principles, inversion, steelman, dialectical synthesis, Toulmin map, claim/evidence/warrant audit, premise audit, reference-class forecast, outside-vs-inside view.
  - **Forecasting** → `forecasting/` (9): probabilistic question design, decomposition, base rates, scenario probabilities, signal-vs-noise triage, what-would-change-my-mind tripwires, calibration self-audit, Brier tracker design, long-horizon radical uncertainty.
  - **Systems** → `systems/` (8): feedback loop identification, causal loop diagrams, stock-and-flow models, archetype recognition, dependency maps, leverage points (Meadows), unintended consequence scan, intervention pre-mortem.
  - **Epistemic** → `epistemic/` (10): named-bias audit, motivated-reasoning check, evidence against yourself, red-team briefing, logical fallacy scan, claim/inference separation, source credibility triangulation, evidence quality score, uncertainty acknowledgment audit, disagreement diagnosis.

### Ideation (Divergent & Convergent)
- **Generate more/better ideas, then converge defensibly** → `domain-ideation/` (12 prompts)
  - Example: "Force 100 ideas" → `ideation_forced_quantity_100_ideas.md`
  - Example: "8 ideas in 8 minutes" → `ideation_crazy_eights.md`
  - Example: "SCAMPER an existing design" → `ideation_scamper.md`
  - Example: "Mine other domains for mechanisms" → `ideation_cross_domain_analogy_mining.md`
  - Example: "Invert the problem" → `ideation_inverse_problem.md`
  - Example: "Worst ideas first, then extract the insight" → `ideation_worst_idea_first.md`
  - Example: "Random stimulus injection" → `ideation_random_stimulus.md`
  - Example: "What would a contrarian/beginner/regulator do?" → `ideation_persona_what_would_x_do.md`
  - Example: "Reframe around the job-to-be-done" → `ideation_jobs_to_be_done_reframe.md`
  - Example: "Drop/tighten constraints to reopen the space" → `ideation_constraint_flip.md`
  - Example: "Kill 80% of the idea list with reasons" → `ideation_idea_kill_list.md`
  - Example: "Converge to a shortlist (dot voting)" → `ideation_idea_convergence_dot_voting.md`

### Risk Management
- **Operational risk artifacts and reviews** → `domain-risk/` (7 prompts)
  - Example: "Build a risk register" → `risk_register_builder.md`
  - Example: "Likelihood × impact heat map" → `risk_heat_map.md`
  - Example: "FMEA on a process/product" → `risk_fmea_analysis.md`
  - Example: "Hunt tail risks / black swans" → `risk_tail_risk_scan.md`
  - Example: "Audit dependency chains (vendors, key people, infra)" → `risk_dependency_chain_audit.md`
  - Example: "Threat-model a non-software situation" → `risk_threat_model_non_technical.md`
  - Example: "After-action review of a risk event" → `risk_after_action_review.md`

### Major Personal Decisions
- **High-stakes personal decisions (research/structuring aids, not professional advice)** → `domain-personal-development/major-decisions/` (10 prompts)
  - Example: "Evaluate a job offer" → `personal_career_offer_evaluation.md`
  - Example: "Relocation decision" → `personal_relocation_decision.md`
  - Example: "Quit or persist?" → `personal_quit_or_persist.md`
  - Example: "Degree vs bootcamp vs certification" → `personal_education_program_choice.md`
  - Example: "Family planning tradeoffs" → `personal_family_planning_tradeoffs.md`
  - Example: "Major financial decision (mortgage, allocation, early retirement)" → `personal_financial_decision_framework.md`
  - Example: "Research a non-emergency health decision" → `personal_health_decision_research.md`
  - Example: "Major purchase research (house, vehicle)" → `personal_major_purchase_research.md`
  - Example: "Vet a cofounder / business partner" → `personal_partnership_cofounder_selection.md`
  - Example: "Audit a difficult relationship before acting" → `personal_difficult_relationship_audit.md`

### Policy & Negotiation (Expanding Domains)
- **Policy analysis** → `domain-policy/` (4 prompts)
  - Example: "Policy options memo" → `policy_options_memo.md`
  - Example: "Frame a policy problem before generating options" → `policy_problem_framing.md`
  - Example: "Map stakeholders / coalitions / blockers / swing actors" → `policy_stakeholder_coalition_map.md`
  - Example: "Assess implementation feasibility (authority, capacity, funding, failure modes)" → `policy_implementation_feasibility.md`
### Negotiation (Practitioner Library — 46 prompts across 8 subdirectories)
- **Negotiation as a working discipline across the full arc** → `domain-negotiation/` — see [README](../domain-negotiation/README.md). **Entry point:** run `preparation/negotiation_prep_depth_triage.md` first; it scores the negotiation into one of four prep tiers and emits an ordered prompt sequence, so the domain is consumed by tier rather than exhaustively.
- **Convention:** the domain keeps one `negotiation_` prefix across all subdirectories (the `domain-legal/` precedent), with the single exception of `difficult-conversations/difficultconvo_*.md`, a distinct audience track for relationship-primary conversations where the goal is to be understood rather than to claim value. `uncertainty: ambiguity` is a domain invariant. One prompt (`channels/negotiation_cross_cultural.md`) carries the domain's only explicit guard: it refuses to generate or accept generalizations about how people of a nationality, ethnicity, or region negotiate.
  - **Preparation** → `preparation/` (10): prep-depth triage, BATNA, leverage audit (eight sources, not just alternatives), interest mapping, package/MESO design, opening offer, concession ladder, counterpart simulation, information plan, rehearsal
  - **At the table** → `at-the-table/` (7): live question sequencing, reading signals & testing bluffs, hard-bargainer defense, impasse diagnosis (five types), authority & mandate limits, emotional flooding, closing & final concession
  - **Channels** → `channels/` (4): written/async, counter-offer email, remote & video, cross-cultural
  - **Multi-party** → `multi-party/` (4): coalition alignment, team roles, coalition defense, third-party facilitation (the repo's only neutral-role prompt)
  - **After the deal** → `after-the-deal/` (4): deal debrief, implementation & relationship, renegotiating a live agreement, no-deal recovery
  - **Contexts** → `contexts/` (8): salary/raise, vendor buy-side, freelance rates, sales objections, equity split, internal budget, customer escalation, major purchase
  - **Difficult conversations** → `difficult-conversations/` (5): pre-brief, post-review, delivering bad news, receiving hard feedback, saying no upward
  - **Craft** → `craft/` (4): style self-assessment, deliberate practice loop, pattern library, ethics line
  - **Expansion roadmap:** [`domain-negotiation/EXPANSION_ROADMAP.md`](../domain-negotiation/EXPANSION_ROADMAP.md) — includes an "Explicitly not gaps" table recording which adjacent prompts (mediation prep, boundary scripts, stakeholder navigation, offer evaluation, live role-play) are deliberately cross-linked rather than duplicated.

### Psy-Ops (Cognitive Security — 32 prompts, ANALYTIC / DEFENSIVE ONLY)
- **Recognizing, analyzing, and defending against psychological influence** — from a single manipulative message to a coordinated campaign to a controlling relationship → `domain-psy-ops/` — see [README](../domain-psy-ops/README.md).
- **Load-bearing convention (output-side, not a permission gate).** The `bug-bounty/` precedent does not transfer: a bounty program is a verifiable grant of permission from a consenting target, whereas an influence operation's targets by definition do not know it is happening. So every prompt's deliverable is an **assessment, a defense, or a resilience plan** — never propaganda, covert personas, inauthentic engagement, targeting packages, or CIB playbooks (red-team prompts emit findings and countermeasures only). Supporting rules: **no manufactured accusations** (confidence-graded assessments with a mandatory alternative-explanation pass, attached to behavior and content — never naming a private individual as a covert operative), **no fabricated evidence** (`[VERIFY]`, never a plausible fill-in), **attribution humility** (low/moderate/high with stated basis; "unattributed" is the default), **safety routing** (no hotline number or service name is ever stated from memory — always verify from an official source), and **counter-messaging stays overt** (named sender, truthful, attributed).
- **The failure mode the domain is designed against:** paranoid over-attribution — organic convergence read as coordination, sincere belief read as a script, incompetence read as deception. Every False-Positive Prevention block targets it.
- **Route by what you are holding:** one artifact → `technique-analysis/`; a pattern across accounts/outlets/weeks → `influence-operations/`; something aimed at you or someone you love → `personal-defense/`; your org or community → `organizational-red-team/`; you need to respond publicly → `counter-messaging/`; you are teaching or studying a case → `case-studies-taxonomies/`.
  - Example: "Is this a coordinated campaign?" (flagship, returns 'insufficient evidence' as a first-class result) → `influence-operations/psyops_influence_operation_analysis.md`
  - Example: "Dissect this post/ad/speech into named techniques" → `technique-analysis/psyops_propaganda_technique_identification.md`
  - Example: "Which emotions is this recruiting, and for what?" → `technique-analysis/psyops_emotional_manipulation_decoder.md`
  - Example: "Is this urgency real? (dark patterns / compliance mechanics)" → `technique-analysis/psyops_persuasion_pressure_audit.md`
  - Example: "What does this frame make invisible?" → `technique-analysis/psyops_framing_and_narrative_analysis.md`
  - Example: "Motte-and-bailey / gish gallop / JAQing" → `technique-analysis/psyops_rhetorical_deception_scan.md`
  - Example: "Where did this image/claim actually come from?" → `technique-analysis/psyops_provenance_and_transmission_trace.md`
  - Example: "Is this chart or statistic distorted?" → `technique-analysis/psyops_statistical_and_visual_distortion_scan.md`
  - Example: "Coordinated, or just people who agree?" → `influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md`
  - Example: "Are these accounts bots?" (heaviest false-positive discipline in the repo) → `influence-operations/psyops_inauthentic_account_signal_assessment.md`
  - Example: "Is this grassroots or astroturf?" (burden sits on the astroturf finding) → `influence-operations/psyops_astroturf_vs_organic_assessment.md`
  - Example: "How did this claim become citable?" → `influence-operations/psyops_information_laundering_chain_map.md`
  - Example: "How sure can we honestly be about who did this?" → `influence-operations/psyops_attribution_confidence_assessment.md`
  - Example: "Is what I'm experiencing manipulation?" → `personal-defense/psyops_manipulation_recognition_personal.md`
  - Example: "Coercive control patterns / does my situation count?" → `personal-defense/psyops_coercive_control_pattern_recognition.md`
  - Example: "Is this group high-control?" (assesses structure, never beliefs) → `personal-defense/psyops_high_control_group_dynamics_assessment.md`
  - Example: "Is this call/message a scam?" → `personal-defense/psyops_social_engineering_pretext_recognition.md`
  - Example: "What's actually shaping what I believe?" → `personal-defense/psyops_information_diet_audit.md`
  - Example: "Personal rules that hold under pressure" → `personal-defense/psyops_cognitive_security_hygiene_plan.md`
  - Example: "I'm worried my kid/friend is being radicalized" → `personal-defense/psyops_concern_for_someone_radicalizing.md`
  - Example: "Who would target our organization, and how?" → `organizational-red-team/psyops_org_influence_threat_model.md`
  - Example: "Which true things about us are exploitable?" → `organizational-red-team/psyops_narrative_vulnerability_assessment.md`
  - Example: "How exposed are our key staff?" (consent-first, never a dossier) → `organizational-red-team/psyops_personnel_targeting_exposure_review.md`
  - Example: "Is our community brigadable by design?" → `organizational-red-team/psyops_community_moderation_resilience_review.md`
  - Example: "Prebunk a claim before it arrives" → `counter-messaging/psyops_prebunking_inoculation_design.md`
  - Example: "Write a correction that actually displaces the belief" → `counter-messaging/psyops_debunk_and_correction_design.md`
  - Example: "Would responding just amplify it?" → `counter-messaging/psyops_rumor_response_triage.md`
  - Example: "Communicate honestly while under attack" → `counter-messaging/psyops_crisis_communication_integrity_plan.md`
  - Example: "Reconcile the competing technique taxonomies" → `case-studies-taxonomies/psyops_technique_taxonomy_reference.md`
  - Example: "Study a documented historical operation" → `case-studies-taxonomies/psyops_historical_operation_case_study.md`
  - Example: "Teach media literacy without producing cynics" → `case-studies-taxonomies/psyops_media_literacy_curriculum_designer.md`
- **Boundary:** general fallacy/source/evidence work → `domain-reasoning-craft/epistemic/`; persuasion-vs-manipulation inside a deal → `domain-negotiation/craft/negotiation_ethics_line.md`; therapy and the aftermath of abuse → `domain-psychology/`; technical phishing defense → `domain-software-engineering/analysis/security/`; commercial persuasion craft → `domain-advertising/`. Full boundary table + permanently-out-of-scope list: [`EXPANSION_ROADMAP.md`](../domain-psy-ops/EXPANSION_ROADMAP.md).

### Written Advocacy (Layperson Self-Advocacy Letters — 35 prompts)
- **A person acting for themselves who needs something from a company, agency, insurer, school, or landlord — in writing, dated, on the record** → `domain-written-advocacy/` — see [README](../domain-written-advocacy/README.md). Every prompt produces the user's **own first-person letter**, built only from facts they supply, designed to still make sense months later to a regulator, an attorney, or a judge.
- **Why this is separate from `domain-legal/`.** `domain-legal/personal-self-advocacy/` covers adversarial harm (harassment, defamation, IP theft, identity theft, debt collection) and carries a mandatory crisis Safety Block on every prompt. That posture is right there and wrong for a gym-membership cancellation. This domain covers the ordinary life admin that merely works better in writing, and routes to `domain-legal/` at the point a matter turns adversarial.
- **Four load-bearing conventions.** (1) **Written-record-first** — every output is dated, names one specific ask, sets a response window, and closes with a **Sending Log** capturing delivery method and proof of receipt. (2) **No invented law** — the domain's highest fabrication risk: no statute, article, section number, regulation, deadline, or penalty is ever asserted from memory (GDPR articles, CCPA/FCRA sections, state deposit and lemon-law statutes are the named hazards); where a user has personally verified a law applies, it appears as *their own stated basis in their own words*. (3) **No named bodies from memory** — regulators, ombudsmen, credit bureaus, safety authorities, data protection authorities, and hotlines are never named and their addresses/URLs never supplied; each is flagged `[VERIFY: identify the correct body from an official source]`. (4) **Proportionate tone ladder** — firm and neutral by default; legal-threat and cease-and-desist language is **refused** and routed to an attorney.
- **Cross-cutting spine** → `cross-cutting/` (6): request-letter architect (flagship), channel & record strategy, escalation ladder, correspondence log, response analyzer, follow-up tracker.
  - Example: "Turn this situation into a sendable written request" → `cross-cutting/advocacy_request_letter_architect.md`
  - Example: "Confirm in writing what was said on a call" → `cross-cutting/advocacy_channel_and_record_strategy.md`
  - Example: "They replied — what did they actually commit to?" → `cross-cutting/advocacy_response_analyzer.md`
  - Example: "Plan the rungs from frontline to regulator" → `cross-cutting/advocacy_escalation_ladder_designer.md`
- **Accounts & billing** → `accounts-and-billing/` (5): cancellation, account closure, recurring-charge dispute, utility/telecom dispute, price-increase/retention.
- **Privacy & data** → `privacy-and-data/` (5): deletion, access (DSAR), marketing opt-out & do-not-sell, data-broker removal (safety-gated), privacy-request escalation.
- **Products & warranty** → `products-and-warranty/` (4): warranty claim, defect remedy, service non-performance, safety defect report (evidence-preservation first).
- **Financial hardship** → `financial-hardship/` (6): hardship assistance, payment arrangement, fee waiver, goodwill adjustment, rate reduction, credit-report dispute.
- **Insurance & medical** → `insurance-and-medical/` (4): denial appeal, external review, medical bill dispute, financial assistance/charity care.
- **Institutions & records** → `institutions-and-records/` (5): public records/FOIA, benefits appeal, regulator complaint, workplace request (non-clinical), school request.
- **Boundary:** adversarial harm → `domain-legal/personal-self-advocacy/`; refunds/chargebacks, debt validation, security deposits, HR complaints, DMCA, and fraud-scoped credit disputes already live there and are **cross-linked, not duplicated**; family court → `domain-legal/family-self-advocacy/`; mental-health-scoped accommodation requests → `domain-psychology/client-self-use/communication-system/`; attorney-side demand letters → `domain-legal/client-intake-communications/legal_demand_letter_drafter.md`; school *meeting* prep → `domain-parenting/`.

### Learning (Self-Directed Skill Acquisition)
- **Domain-agnostic learning craft** → `domain-learning/` (5 prompts) — DISTINCT from `domain-learning-coding/` (code-specific)
  - Example: "Design an N-week curriculum to a target level" → `learning_curriculum_designer.md`
  - Example: "Build a deliberate-practice loop for one sub-skill" → `learning_deliberate_practice_designer.md`
  - Example: "Curate a layered reading list (foundations → frontier)" → `learning_reading_list_curator.md`
  - Example: "Feynman-test my understanding of a concept" → `learning_concept_explanation_audit.md`
  - Example: "Translate a skill gap into a sequenced learning plan" → `learning_skill_gap_to_curriculum.md`

### Specialized-Fields Research Workflows (Legal / IP)
- **Plan legal research before Westlaw/Lexis** → `domain-specialized-fields/legal/legal_research_plan.md`
- **Patent landscape scan / IP whitespace analysis** → `domain-specialized-fields/ip/patent_landscape_scan.md`

### Business-Strategy Research (Additions)
- **Technical due diligence plan (acquisition / investment / procurement)** → `domain-business-strategy/research/technical_due_diligence_plan.md`
- **Synthesize 10–30 user interviews into themes / tensions / decisions** → `domain-business-strategy/research/user_research_synthesis.md`
- **Structured competitor teardown (product / strategy / org)** → `domain-business-strategy/research/competitor_teardown.md`
- **Decision-forcing meeting pre-read** → `domain-productivity/operating-cadence/meeting_pre_read_drafter.md`

### Idea-to-Product Pipeline (full idea → shippable software → AI-agent build)
- **End-to-end pipeline** for taking a software/platform idea from raw brainstorm to a Claude-Code-ready build package → `domain-idea-to-product/` (~63 prompts in 11 stages, self-contained directory; copies of upstream prompts + 8 net-new gap-fill prompts + master orchestrator).
- **Local domain guide:** [`domain-idea-to-product/README.md`](../domain-idea-to-product/README.md). Pipeline flow: [`PIPELINE_OVERVIEW.md`](../domain-idea-to-product/PIPELINE_OVERVIEW.md).
- **Three modes:**
  - **Guided** — start with `domain-idea-to-product/orchestrator_idea_to_product.md`; it interviews you, classifies your starting stage, recommends ≤3 next prompts, critiques each output against the stage's verification checklist, enforces hard gates before stages 7 and 10.
  - **Manual** — walk `PIPELINE_OVERVIEW.md` yourself; pick stage prompts as needed.
  - **Surgical** — jump to a specific stage subdirectory if you only need that piece.
- **Hard gates enforced:** stage 2 → 4 requires ≥5 rubric-scored interviews; stage 6 → 7 requires pre-mortem; stage 11 + all upstream → 10 required before AI-agent handoff.
- **Terminal artifact:** day-1 file bundle for Claude Code / Cursor — CLAUDE.md, sequenced task list, per-task acceptance specs, work-loop spec, project-memory scaffolding.
- **The 8 net-new gap-fill prompts in this domain:**
  - `stage-1-ideation/ideation_concept_legs_test.md` — GO/KILL/RESHAPE on a raw idea
  - `stage-2-problem-validation/validation_customer_discovery_interview_protocol.md` — JTBD + Mom Test interview guide with rubric
  - `stage-3-market-research/market_unit_economics_designer.md` — LTV/CAC/cohort with sensitivity bands
  - `stage-5-strategy-positioning/strategy_gtm_orchestrated_plan.md` — 90-day GTM plan
  - `stage-7-prd-authoring/prd_to_epic_feature_decomposer.md` — feature tree + MVP/V1/V2 cut lines
  - `stage-8-architecture-design/architecture_tech_stack_selector.md` — component decision matrix with AI-agent friendliness scoring
  - `stage-10-ai-agent-handoff/prd_to_agent_brief_bridge.md` — produces the day-1 agent bundle (the critical bridge)
  - `stage-10-ai-agent-handoff/agent_task_acceptance_test_writer.md` — per-task verification with false-success traps

### Deep Analysis (Multi-Perspective Deep-Think Systems)
- **Five-phase, gated, multi-perspective analysis systems** for working through hard things one-on-one with an AI at a depth that compensates for the absence of a human team. Pick by terminal artifact, not topic.
- Shared backbone: Frame → Decompose → Multi-perspective (6 core lenses + scope-specific) → Stress-test → Synthesize. `AskUserQuestion` is the primary I/O at every gate.
- **Each scope ships in two equivalent versions:** a **rigorous** version (`/deepthink-*`) using business / engineering vocabulary, and a **plain-English** version (`/deepthink-*-plain`) for non-technical users. Same rigor, same five phases, same six core perspectives, same output-format requirements — only vocabulary and framing differ. Recommend the plain version for parents, teachers, freelancers, small business owners, or anyone unfamiliar with terms like "orthogonal," "load-bearing assumption," "tripwire," or "critical path."
- **All four prompts + slash commands** → `domain-deep-analysis/` (see [`domain-deep-analysis/README.md`](../domain-deep-analysis/README.md))
  - Example: "Diagnose what's actually going on with X" (no fixed deliverable) → `deepthink_problem_analysis.md` / `/deepthink-problem` (plain English: `deepthink_problem_analysis_plain.md` / `/deepthink-problem-plain`)
  - Example: "Decide between A or B with reversibility + tripwires" → `deepthink_decision.md` / `/deepthink-decision` (plain English: `deepthink_decision_plain.md` / `/deepthink-decision-plain`)
  - Example: "Sequence the path from here to a chosen goal" → `deepthink_plan.md` / `/deepthink-plan` (plain English: `deepthink_plan_plain.md` / `/deepthink-plan-plain`)
  - Example: "Design what to build (system / feature / structure / process)" → `deepthink_design.md` / `/deepthink-design` (plain English: `deepthink_design_plain.md` / `/deepthink-design-plain`)

### Product Management
- **PRDs and product work** → `domain-product-management/prompts/`
  - Example: "Build a PRD via interrogation (MVP-first)" → `product_create_prd.md`
  - Example: "Score a PRD against a rigorous rubric" → `product_rigorous_prd_evaluation_and_scoring.md`
  - Example: "Plan a cross-functional delivery sprint" → `product_delivery_sprint_planner.md`
  - Example: "Market sizing (TAM/SAM/SOM) — rapid or comprehensive" → `product_market_size_calculator.md`
  - For adjacent product work, see also `domain-idea-to-product/stage-7-prd-authoring/` and `domain-business-strategy/research/`

### Presentations
- **Board decks and presentations** → `domain-presentations/` (~23 prompts)
  - Example: "Board deck" → `powerpoint_board_deck.md`
  - Example: "Quarterly business review" → `powerpoint_quarterly_business_review.md`

### Image Generation
- **Image prompts for AI image models** → `domain-image-generation/` (~146 prompts)
  - Example: "Logo/branding" → `branding/`
  - Example: "Coloring page / KDP coloring book" → `coloring-book/` (9 prompts)
  - Example: "Healthcare/medical (badge buddy, patient handout, medical diagram)" → `healthcare/` (14 prompts, anti-fabrication first)
  - Example: "Product / e-commerce photography" → `ecommerce-product/` (5 prompts)
  - Example: "Social-media graphic pack" → `social-media/` (5 prompts)
  - Example: "Book / album / podcast cover" → `publishing-covers/` (5 prompts)
  - Example: "Event poster / flyer" → `events-print/` (3 prompts)
  - Example: "T-shirt / sticker / POD pattern" → `merch-print-on-demand/` (3 prompts)
  - Example: "Children's book illustration" → `childrens-illustration/` (3 prompts)
  - Example: "Comic / manga / webtoon" → `comic-sequential/` (3 prompts)
  - Example: "Scientific illustration / exploded diagram / data-viz image" → `scientific-technical/` (3 prompts, accuracy-gated)
  - Example: "OpenAI gpt-image-2 prompts" → `gpt-image-2/` (12 production prompts)
  - Example: "Google Nano Banana prompts" → `nano-banana/` (5 production prompts)
  - **Start with:** `domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md` to choose the right model for the task.
  - **Then:** `domain-image-generation/GPT_IMAGE_2_GUIDE.md` if targeting OpenAI's `gpt-image-2`.
  - **Or:** `domain-image-generation/NANO_BANANA_GUIDE.md` if targeting Google's Nano Banana family (`gemini-2.5-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-image`).
  - **Or:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` for the 8 core print-ready techniques.

### gpt-image-2 (OpenAI, April 2026)
- **Comprehensive prompting guide** → `domain-image-generation/GPT_IMAGE_2_GUIDE.md`
- **12 production-ready prompts** → `domain-image-generation/gpt-image-2/` covering:
  - Example: "Convert a brief into a structured gpt-image-2 prompt" → `gptimage2_meta_prompt_builder.md`
  - Example: "Photorealistic editorial portrait" → `gptimage2_photorealistic_portrait.md`
  - Example: "E-commerce product hero" → `gptimage2_product_hero_shot.md`
  - Example: "Logo with 4 batch variations" → `gptimage2_logo_batch_variations.md`
  - Example: "Campaign-grade ad with verbatim copy" → `gptimage2_advertising_creative_brief.md`
  - Example: "Dense-text infographic with web-search grounding" → `gptimage2_dense_text_infographic.md`
  - Example: "Realistic UI mockup as artifact spec" → `gptimage2_ui_mockup_specification.md`
  - Example: "Verbatim marketing copy in image" → `gptimage2_in_image_text_marketing.md`
  - Example: "Executive deck slide with chart" → `gptimage2_executive_slide_artifact.md`
  - Example: "Surgical edit (object removal / lighting / text translation)" → `gptimage2_surgical_edit_change_preserve.md`
  - Example: "Multi-reference composite (up to 16 refs)" → `gptimage2_multi_reference_composite.md`
  - Example: "Character consistency anchor + reuse" → `gptimage2_character_consistency_anchor.md`

### Nano Banana (Google Gemini Image Models)
- **Comprehensive prompting guide** → `domain-image-generation/NANO_BANANA_GUIDE.md`
- Covers all three models: Nano Banana (`gemini-2.5-flash-image`), Nano Banana Pro (`gemini-3-pro-image`), Nano Banana 2 (`gemini-3.1-flash-image`)
  - Example: "Nano Banana model selection (which of the 3 models)" → NANO_BANANA_GUIDE.md Section 2
  - Example: "Narrative prompt structure for Gemini" → NANO_BANANA_GUIDE.md Section 4
  - Example: "Reference image allocation (14 refs by role)" → NANO_BANANA_GUIDE.md Section 5
  - Example: "System prompts for style consistency" → NANO_BANANA_GUIDE.md Section 7
  - Example: "Google Search grounding for factual visuals" → NANO_BANANA_GUIDE.md Section 8
  - Example: "JSON schema prompting (community practice)" → NANO_BANANA_GUIDE.md Section 9
  - Example: "Character bible pipeline for Nano Banana" → NANO_BANANA_GUIDE.md Section 11
  - Example: "Storyboard keyframes → Veo video pipeline" → NANO_BANANA_GUIDE.md Section 12
  - Example: "Medical imaging two-bucket framework" → NANO_BANANA_GUIDE.md Section 13

### Advertising (Image Generation)
- **Industry-specific advertising image prompts** → `domain-advertising/` (17 prompts)
  - Example: "Automotive campaign creative" → `advertising_automotive_vehicle.md`
  - Example: "SaaS ad creative system" → `advertising_tech_product_saas.md`
  - Example: "Travel/hospitality promotion" → `advertising_travel_hospitality.md`
  - **Workflow:** interview intake (product, audience, key message, palette, CTA) + print/screen lock + anti-UI/anti-mockup constraints.

---

## Non-Coding Domain Mapping

> **For building NEW non-coding prompts:** Use [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md)

When users need help with **non-coding tasks**, first determine the domain:

### Education & Teaching (267 prompts, 3 audience tracks)
**Route by who is holding the prompt**, then by subdirectory — see [`domain-education-teaching/README.md`](../domain-education-teaching/README.md). If it produces something you hand to students it is `instructor/`; something you hand to a committee, `program/`; something only you will use to learn, `learner/`. One prefix per track (`teaching_`, `program_`, `learn_`); the subdirectory carries the finer signal.

- **`instructor/` (104)** — teacher, lecturer, corporate trainer. `lesson-planning/` (6), `explanation-craft/` (9), `response-cycle/` (5), `assessment-items/` (8), `assessment-design/` (9), `assessment-analysis/` (7), `grading-feedback/` (8), `reporting-communication/` (2), `student-support/` (8), `classroom-ops/` (3), `ed-tech/` (6), `higher-ed-corporate/` (11), `subject-pedagogy/` (22, split `ela/` `math/` `science/` `social-studies/` `world-languages/`)
  - Example: "I need a lesson for Tuesday" → `instructor/lesson-planning/teaching_lesson_plan_generator.md`
  - Example: "Half the class didn't get it" → `instructor/response-cycle/teaching_misconception_diagnoser.md` → `teaching_reteach_intervention_planner.md`
  - Example: "Explain this so a 7-year-old gets it" → `instructor/explanation-craft/teaching_concept_explorer_kids.md`
  - Example: "Quiz with real distractors" → `instructor/assessment-items/teaching_mc_item_writer_with_distractors.md`
  - Example: "90 essays to grade by Friday" → `instructor/grading-feedback/teaching_speed_grading_triage.md`
  - Example: "IEP goals that survive review" → `instructor/student-support/teaching_iep_goal_writer.md`
- **`program/` (41)** — dean, curriculum director, accreditation liaison. See the section below.
- **`learner/` (122)** — the student, studying alone. Socratic stance throughout: these coach and refuse to produce submittable work. `note-taking/` (4), `memory-and-recall/` (8), `self-assessment/` (8), `exam-prep/` (8), `study-by-discipline/` (13), `tutoring/` (9), `stuck-and-confused/` (8), `writing/` (9), `reading/` (5), `math-science/` (7), `language/` (5), `research/` (4), `time-and-discussion/` (4), `adult-learner/` (9), `guides/` (21 chained workflows)
  - Example: "Teach me this, don't just tell me" → `learner/tutoring/learn_socratic_tutor.md`
  - Example: "I got it wrong and don't know why" → `learner/stuck-and-confused/learn_wrong_answer_forensics.md`
  - Example: "I read it four times and remember nothing" → `learner/memory-and-recall/learn_retrieval_drill_designer.md`
  - Example: "Finals are in a week" → `learner/exam-prep/learn_finals_week_plan.md`
  - Example: "Help me write this essay without writing it for me" → `learner/writing/learn_thesis_with_critique.md`
  - Example: "I'm 38 and going back to school" → `learner/adult-learner/learn_cold_start_return_to_school.md`
  - Example: "Just tell me what to run, in what order" → `learner/guides/` (pick audience, then workflow)
- **Boundary:** self-directed skill acquisition with no institution → `domain-learning/`; programming → `domain-learning-coding/`; health-professions education incl. its own learner track → `domain-medical-education/`; teaching research methods → `domain-science/teaching-research-methods/`; the parent's side of school → `domain-parenting/`.
  - **Domain guide:** [domain-education-teaching/README.md](../domain-education-teaching/README.md) · **Craft reference & templates:** [field_guide.md](../domain-education-teaching/field_guide.md) · **Roadmap:** [EXPANSION_ROADMAP.md](../domain-education-teaching/EXPANSION_ROADMAP.md)

### Curriculum Design & Program-Level Educational Planning (2026-05-15)
- **Program-level curriculum, standards alignment, outcomes, accreditation, faculty development, program evaluation** → `domain-education-teaching/` subdirectories (45 new prompts):
  - **Curriculum design** → `domain-education-teaching/program/curriculum-design/` (18 prompts):
    - Example: "Build a curriculum map (course → outcome → standard → assessment)" → `teaching_curriculum_map_builder.md`
    - Example: "K-12 multi-year scope and sequence" → `teaching_scope_sequence_k12.md`
    - Example: "Higher-ed program scope and sequence" → `teaching_scope_sequence_he.md`
    - Example: "Workforce / CTE / apprenticeship scope and sequence" → `teaching_scope_sequence_workforce.md`
    - Example: "HE course design (constructive alignment)" → `teaching_course_design_he.md`
    - Example: "Backward program design (UbD at program scale)" → `teaching_backward_program_design.md`
    - Example: "Build a competency framework" → `teaching_competency_framework_designer.md`
    - Example: "Audit curriculum against a standards framework" → `teaching_standards_alignment_audit.md`
    - Example: "Crosswalk between two standards frameworks" → `teaching_standards_crosswalk_generator.md`
    - Example: "Vertical alignment audit (across grades / levels)" → `teaching_vertical_alignment_auditor.md`
    - Example: "Horizontal alignment (cross-disciplinary, same level)" → `teaching_horizontal_alignment_mapper.md`
    - Example: "Write Bloom's-aligned learning objectives (ABCD)" → `teaching_learning_objectives_writer_blooms.md`
    - Example: "Calibrate existing objectives or items to Bloom's + DOK" → `teaching_blooms_taxonomy_calibrator.md`
    - Example: "Learning progression with waypoints and misconceptions" → `teaching_progression_map_designer.md`
    - Example: "Milestone / checkpoint architecture" → `teaching_milestone_alignment_designer.md`
    - Example: "Remediation pathway (MTSS/RTI or competency-based)" → `teaching_remediation_pathway_designer.md`
    - Example: "Advanced unit design (UbD + UDL + accessibility)" → `teaching_unit_design_advanced.md`
    - Example: "Workforce competency mapping (O*NET + credentials)" → `teaching_competency_mapping_workforce.md`
  - **Program outcomes & assessment** → `domain-education-teaching/program/outcomes-assessment/` (8 prompts):
    - Example: "Build PSLO / ISLO / CSLO architecture" → `teaching_program_outcomes_framework.md`
    - Example: "Map outcomes to assessment evidence" → `teaching_outcomes_to_assessment_mapper.md`
    - Example: "Build assessment blueprint (test specification)" → `teaching_assessment_blueprint_builder.md`
    - Example: "Program gap analysis (taught vs required)" → `teaching_program_gap_analysis.md`
    - Example: "Signature assignment design (HE program evidence)" → `teaching_signature_assignment_designer.md`
    - Example: "Capstone assessment design" → `teaching_capstone_assessment_designer.md`
    - Example: "Audit rubric for outcomes alignment" → `teaching_rubric_alignment_to_outcomes.md`
    - Example: "Competency-based assessment evidence plan (CBME)" → `teaching_competency_assessment_evidence_design.md`
  - **Accreditation & program review** → `domain-education-teaching/program/accreditation-review/` (5 prompts, parameterized):
    - Example: "Build a regional HE accreditation self-study (HLC / MSCHE / SACSCOC / WSCUC / NWCCU)" → `teaching_accreditation_self_study_he.md`
    - Example: "Programmatic accreditation self-study (ABET / AACSB / CAEP / CCNE / ACPE / etc.)" → `teaching_accreditation_self_study_programmatic.md`
    - Example: "Med-ed accreditation self-study (LCME / ACGME / COCA / CODA)" → `teaching_accreditation_self_study_meded.md`
    - Example: "Program review cycle designer" → `teaching_program_review_cycle_designer.md`
    - Example: "Compile criteria + evidence into response drafts" → `teaching_accreditation_evidence_compiler.md`
  - **Faculty development** → `domain-education-teaching/program/faculty-development/` (5 prompts):
    - Example: "Multi-semester faculty development plan" → `teaching_faculty_development_plan_designer.md`
    - Example: "Professional learning community design" → `teaching_professional_learning_community_designer.md`
    - Example: "Instructional coaching program design" → `teaching_instructional_coaching_program.md`
    - Example: "Assessment literacy faculty curriculum" → `teaching_assessment_literacy_curriculum.md`
    - Example: "New faculty onboarding program" → `teaching_faculty_onboarding_program.md`
  - **Program evaluation & analytics** → `domain-education-teaching/program/evaluation-analytics/` (5 prompts):
    - Example: "Build a program evaluation framework (Kirkpatrick / CIPP / logic model / theory of change)" → `teaching_program_evaluation_framework.md`
    - Example: "Logic model / theory of change with assumptions" → `teaching_logic_model_designer.md`
    - Example: "Interpret LMS / formative / dashboard data" → `teaching_learning_analytics_interpreter.md`
    - Example: "Early-warning system designer" → `teaching_early_warning_system_designer.md`
    - Example: "PDSA / continuous improvement cycle" → `teaching_continuous_improvement_cycle.md`
  - **Medical-education program-level (CBME, EPAs, ACGME)** → `domain-medical-education/educator-curriculum-design/` (4 prompts):
    - Example: "CBME implementation roadmap (program-level)" → `domain-medical-education/educator-curriculum-design/curric_cbme_implementation_program.md`
    - Example: "Residency curriculum mapper (ACGME Milestones + EPAs)" → `domain-medical-education/educator-curriculum-design/curric_residency_curriculum_mapper.md`
    - Example: "EPA implementation designer (entrustment + evidence)" → `domain-medical-education/educator-curriculum-design/curric_epa_implementation_designer.md`
    - Example: "Program competency framework (ACGME six core competencies)" → `domain-medical-education/educator-curriculum-design/curric_program_competency_framework_acgme.md`

### Creative Writing (Adult/Mature — 27 prompts across 7 subdirs)
- **Fiction, essays, poetry, scripts (adult)** → `domain-creative-writing/` — see [README](../domain-creative-writing/README.md) for the full routing table. **Audience boundary:** kids/teens → `domain-childrens-writing/`; professional/business prose → `domain-professional-writing/`.
  - **Fiction craft** → `domain-creative-writing/fiction/`: story structure, novel outlining, short story, worldbuilding, scene construction, POV & narrative distance, pacing & tension
  - **Cross-cutting craft tools** → `domain-creative-writing/craft-tools/`: character, voice, dialogue, revision, beta-reader synthesis, show-don't-tell, description/sensory setting, theme & motif, opening pages/hook, endings/resolution
  - **Genre workshops** → `domain-creative-writing/genre-workshops/`: multi-genre overview, mystery/crime craft, speculative (SF/fantasy) craft
  - **Creative nonfiction** → `domain-creative-writing/creative-nonfiction/`: memoir & personal essay, narrative nonfiction & literary journalism (no-fabrication guard)
  - **Poetry** → `domain-creative-writing/poetry/`: poetic forms & craft, imagery & figurative language
  - **Script & stage** → `domain-creative-writing/script-stage/`: screenplay/teleplay/stage framework
  - **Publishing & career** → `domain-creative-writing/publishing-career/`: query letter & synopsis, pitch/logline/comp titles (no-fabrication guard on agents, comps, sales)
  - **Domain guide:** [domain-creative-writing/README.md](../domain-creative-writing/README.md)

### Children's Writing (Authoring for Young Readers)
- **Writing kid-friendly material — children's fiction & nonfiction** for aspiring/working authors → `domain-childrens-writing/` (22 prompts across 5 subdirs: `fiction-workshops/`, `nonfiction-workshops/`, `craft-tools/`, `representation-collaboration/`, `publishing-business/`). This is about *creating content for child audiences*, NOT teaching kids (`domain-education-teaching/`) or talking to your own child (`domain-parenting/`). Core conventions: child agency, no preaching, respect the reader, trust the illustrator, read-aloud rhythm, strict no-fabrication for nonfiction; extended with **representation humility** (never a substitute for a sensitivity reader / own-voices author), **publishing anti-fabrication** (no invented comps/agents/figures — flag VERIFY), and an **age boundary** (board books 0-3 → upper-MG/young-teen crossover 11-14; mature teen YA → `domain-creative-writing/`).
  - **Domain guide:** [domain-childrens-writing/README.md](../domain-childrens-writing/README.md)
  - **Fiction forms:** "picture book (2-8)" → `fiction-workshops/childrens_picture_book_workshop.md`; "board / concept / ABC / counting book (0-3)" → `fiction-workshops/childrens_board_concept_book_workshop.md`; "early reader / chapter book (5-10)" → `fiction-workshops/childrens_early_reader_chapter_book_workshop.md`; "middle-grade novel (8-12)" → `fiction-workshops/childrens_middle_grade_fiction_workshop.md`; "upper-MG / young-teen crossover (11-14)" → `fiction-workshops/childrens_ya_crossover_workshop.md`; "novel in verse" → `fiction-workshops/childrens_verse_novel_workshop.md`; "graphic novel / comic for kids" → `fiction-workshops/childrens_graphic_novel_comics_workshop.md`
  - **Nonfiction:** "kids' biography / true-history story" → `nonfiction-workshops/childrens_narrative_nonfiction_workshop.md`; "STEM / concept / how-it-works book" → `nonfiction-workshops/childrens_expository_stem_concept_workshop.md`
  - **Craft tools:** "strengthen my opening / first line" → `craft-tools/childrens_opening_pages_hook.md`; "fix my kid dialogue" → `craft-tools/childrens_kid_dialogue_workshop.md`; "build / audit my character" → `craft-tools/childrens_character_creation.md`; "revise my draft (layered pass)" → `craft-tools/childrens_revision_self_edit_pass.md`; "hit a specific age / reading level" → `craft-tools/childrens_age_reading_level_calibrator.md`; "fix the meter / rhyme" → `craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md`; "handle death / divorce / hard topics" → `craft-tools/childrens_sensitive_topics_framing.md`
  - **Representation & illustrator:** "writing across a culture/identity I don't share" → `representation-collaboration/childrens_writing_across_difference_audit.md`; "art notes / working with an illustrator" → `representation-collaboration/childrens_illustrator_collaboration.md`; "make it accessible (dyslexia / neurodivergent)" → `representation-collaboration/childrens_accessible_inclusive_design.md`
  - **Publishing & business:** "agent query letter" → `publishing-business/childrens_query_letter_kidlit.md`; "synopsis / submission package" → `publishing-business/childrens_synopsis_submission_package.md`; "logline / comp titles / positioning" → `publishing-business/childrens_pitch_comps_market_positioning.md`

### Healthcare & Clinical
- **Patient communication, clinical decision support, specialties, pharmacy, nursing, allied health** → `domain-healthcare-clinical/` (~41 prompts)
  - Example: "Clinical reasoning" → `medicine_clinical_decision_support.md` (Gold Standard)
  - Example: "Differential diagnosis" → `medicine_differential_diagnosis_generator.md`
  - Example: "Which imaging study?" → `medicine_imaging_ordering_rationale.md`
  - Example: "Incidentaloma follow-up" → `medicine_incidental_findings_management.md`
  - Example: "Tumor board case" → `medicine_oncology_case_framer.md`
  - Example: "HFrEF GDMT titration" → `medicine_heart_failure_titration_advisor.md`
  - Example: "Anticoagulation decision" → `medicine_anticoagulation_decision_support.md`
  - Example: "Prenatal risk assessment" → `medicine_prenatal_risk_stratification.md`
  - Example: "Substance use disorder / MAT" → `medicine_addiction_medicine_assessment.md`
  - Example: "Sepsis recognition" → `medicine_sepsis_recognition_framework.md`
  - Example: "Renal / hepatic dosing" → `medicine_renal_hepatic_dose_adjustment.md`
  - Example: "Medication reconciliation" → `medicine_medication_reconciliation.md`
  - Example: "E/M coding level" → `medicine_em_coding_level_justification.md`
  - Example: "Prior auth / appeal letter" → `medicine_prior_authorization_letter.md`
  - Example: "Nurse SBAR escalation" → `nursing_sbar_clinical_escalation.md`
  - Example: "Medication admin safety" → `nursing_medication_administration_safety.md`
  - Example: "SDOH screen response" → `allied_health_sdoh_screening_response.md`
  - **Domain guide:** [domain-healthcare-clinical/](../domain-healthcare-clinical/)

- **Medical education (HPE) — clinical educators, faculty, preceptors, curriculum designers** → `domain-medical-education/` (~22 prompts)
  - Example: "Write a PBL case" → `case-scenario-design/meded_pbl_case_writer.md`
  - Example: "Design an OSCE station" → `case-scenario-design/meded_osce_station_designer.md`
  - Example: "Simulation scenario" → `case-scenario-design/meded_simulation_scenario_designer.md`
  - Example: "Write NBME-style MCQs" → `assessment-tools/meded_nbme_style_mcq_writer.md`
  - Example: "Write a milestone narrative" → `assessment-tools/meded_milestone_narrative_writer.md`
  - Example: "Feedback for a resident" → `feedback-remediation/meded_learner_feedback_composer.md`
  - Example: "Debriefing guide" → `feedback-remediation/meded_debriefing_guide_designer.md`
  - Example: "Remediation plan" → `feedback-remediation/meded_remediation_plan_designer.md`
  - Example: "Preceptor teaching script (OMP/SNAPPS)" → `teaching-methods/meded_preceptor_teaching_script_writer.md`
  - Example: "Lecture redesign / active learning" → `teaching-methods/meded_lecture_redesign_planner.md`
  - Example: "Faculty development module" → `teaching-methods/meded_faculty_development_module_designer.md`
  - **Routing guide + competency frameworks:** `domain-medical-education/README.md`

- **Medical education (HPE) — LEARNERS themselves (medical, nursing, PA, pharmacy, EMS, allied health, dental students/residents) using these prompts for study, practice, rehearsal, and self-assessment** → `domain-medical-education/` (37 prompts, added 2026-05-15)
  - **Boundary:** these are study/practice tools, NOT real-time clinical decision support. Every prompt redirects real-patient questions to clinical resources / supervisor.
  - Example: "Build me an illness script for [disease]" → `clinical-reasoning/learner_illness_script_builder.md`
  - Example: "Quiz me on differentials for chest pain" → `clinical-reasoning/learner_differential_diagnosis_drill.md`
  - Example: "Sharpen my one-liner / problem representation" → `clinical-reasoning/learner_problem_representation_rehearsal.md`
  - Example: "What's the next-best test?" / hypothesis-driven workup → `clinical-reasoning/learner_hypothesis_driven_workup_drill.md`
  - Example: "Walk me through an interactive case" → `clinical-reasoning/learner_clinical_case_walkthrough.md`
  - Example: "Pick a reasoning schema for [chief complaint]" → `clinical-reasoning/learner_clinical_reasoning_schema_practice.md`
  - Example: "Run me through an OSCE station" → `clinical-skills/learner_osce_self_rehearsal.md`
  - Example: "Be my simulated patient — let me practice history-taking" → `clinical-skills/learner_history_taking_rehearsal.md`
  - Example: "Coach my oral presentation for rounds" → `clinical-skills/learner_oral_presentation_practice.md`
  - Example: "Critique my SOAP note" → `clinical-skills/learner_soap_note_writing_practice.md`
  - Example: "Critique my admission H&P" → `clinical-skills/learner_h_and_p_writing_practice.md`
  - Example: "Give me a [knee / cardiac / abdominal] exam checklist" → `clinical-skills/learner_physical_exam_checklist_generator.md`
  - Example: "Drill me on anatomy of [region]" → `foundational-sciences/learner_anatomy_drill_generator.md`
  - Example: "Explain [physiology concept] — I don't get it" → `foundational-sciences/learner_physiology_concept_clarifier.md`
  - Example: "Build the pathophys chain for [disease]" → `foundational-sciences/learner_pathophysiology_chain_builder.md`
  - Example: "How do [ACE inhibitors / beta-blockers] work?" → `foundational-sciences/learner_pharmacology_mechanism_explainer.md`
  - Example: "Quiz me on [Staph aureus / Pseudomonas]" → `foundational-sciences/learner_microbiology_bug_drill.md`
  - Example: "Hypersensitivity types / MHC / complement" → `foundational-sciences/learner_immunology_concept_clarifier.md`
  - Example: "Coach me through a board question I got wrong" → `exam-prep/learner_board_style_question_review.md`
  - Example: "Why do I fall for distractors?" → `exam-prep/learner_distractor_analysis_drill.md`
  - Example: "Debrief my qbank session" → `exam-prep/learner_qbank_session_debriefer.md`
  - Example: "Compress this topic into a high-yield sheet" → `exam-prep/learner_high_yield_topic_compressor.md`
  - Example: "Pre-brief me before a procedure" → `procedures-emergencies/learner_procedure_prep_briefing.md`
  - Example: "Run ACLS / PALS / NRP / ATLS rehearsal" → `procedures-emergencies/learner_code_algorithm_rehearsal.md`
  - Example: "Prep me mentally for sim" → `procedures-emergencies/learner_simulation_pre_briefing.md`
  - Example: "Drill me on anaphylaxis / sepsis / tension pneumo recognition" → `procedures-emergencies/learner_critical_event_recognition_drill.md`
  - Example: "Help me pre-round on inpatients" → `clinical-prep/learner_pre_rounding_prep.md`
  - Example: "Help me pre-chart for clinic" → `clinical-prep/learner_pre_clinic_patient_prep.md`
  - Example: "Practice handoff / sign-out / SBAR" → `clinical-prep/learner_handoff_practice.md`
  - Example: "Turn notes into Anki cards" → `study-planning/learner_spaced_repetition_deck_generator.md`
  - Example: "Build a board-exam study plan (USMLE/NCLEX/NAPLEX/PANCE/NREMT/NBDE)" → `study-planning/learner_study_plan_designer.md`
  - Example: "End-of-week study review" → `study-planning/learner_weekly_study_review.md`
  - Example: "Write a NANDA nursing care plan" → `discipline-specific/learner_nursing_care_plan_practice.md`
  - Example: "Pharmacy SOAP / MTM recommendation" → `discipline-specific/learner_pharmacy_therapeutics_soap_practice.md`
  - Example: "EMS protocol drill / NREMT scenario" → `discipline-specific/learner_ems_protocol_decision_drill.md`
  - Example: "Dental treatment-plan practice" → `discipline-specific/learner_dental_treatment_planning_practice.md`
  - Example: "PT/OT/SLP/RT/RD/SW scope + plan" → `discipline-specific/learner_allied_health_scope_and_reasoning_drill.md`
  - **Routing guide:** `domain-medical-education/README.md`

### Research & Academic
- **Literature review, methodology, analysis** → `domain-research-academic/` (15 prompts + framework & field guide)
  - **Domain guide:** [domain-research-academic/](../domain-research-academic/) — templates, quality indicators, and field guide for research prompt authoring
  - Example: "Turn a topic into researchable questions" → `research_question_formulation.md`
  - Example: "Plan a literature review" → `research_literature_review_plan.md`
  - Example: "Design a defensible search strategy" → `research_search_strategy_designer.md`
  - Example: "PRISMA/Cochrane systematic review protocol" → `research_systematic_review_protocol.md`
  - Example: "Is a meta-analysis feasible here?" → `research_meta_analysis_scoping.md`
  - Example: "Map evidence for/against a claim by quality" → `research_evidence_map.md`
  - Example: "Check one claim against 3+ source types" → `research_source_triangulation.md`
  - Example: "Synthesize 5–20 sources, preserving disagreement" → `research_secondary_source_synthesis.md`
  - Example: "Will this published finding replicate?" → `research_replication_audit.md`
  - Example: "Generate competing hypotheses for a pattern" → `research_hypothesis_generator.md`
  - Example: "Map a research field for a newcomer" → `research_field_landscape_map.md`
  - Example: "Design a semi-structured interview guide" → `research_interview_guide_designer.md`
  - Example: "Build a qualitative codebook" → `research_qualitative_coding_scheme.md`
  - Example: "Design a survey instrument with bias controls" → `research_survey_instrument_designer.md`
  - Example: "Draft a research memo from findings" → `research_research_memo_drafter.md`

### Science (Practitioner Library — the *doing* of bench / field / computational science)
- **Working-scientist research practice** → `domain-science/` (**141 prompts — the Phase 2 roadmap is fully built across all 12 subdirectories**: Phase 1 + Phase 2A `methods-foundations/` 17 + Phase 2B `bench-and-wetlab/` 12 + Phase 2C `computational/` 14 + Phase 2D `statistics/` 12 + Phase 2E `writing-communication/` 14 + Phase 2F `peer-review/` 6 + Phase 2G `grants-funding/` 10 + Phase 2H `ethics-integrity/` 8 + Phase 2I `lab-operations-mentorship/` 10 + Phase 2K `public-engagement/` 8 + Phase 2L `teaching-research-methods/` 6 + Phase 2J `disciplines/` 24). **Boundary:** generic, cross-field research methodology (lit-search strategy, qualitative coding, survey instruments) stays in `domain-research-academic/`; **scientific judgment specific to a bench / field / instrument / discipline lives here.** See [`domain-science/README.md`](../domain-science/README.md) and [`domain-science/EXPANSION_ROADMAP.md`](../domain-science/EXPANSION_ROADMAP.md).
  - **Methods foundations** → `domain-science/methods-foundations/` (17): question refinement, preregistration / Registered Reports, power & sample size (frequentist + Bayesian), controls, blinding/randomization, confound & validity audits, replicability premortem, reproducibility (FAIR) self-audit, methods-section drafter, methodology & qual-vs-quant decision trees + the 3 relocated Phase 1 prompts. See [`methods-foundations/README.md`](../domain-science/methods-foundations/README.md).
  - Example: "Refine a vague idea into a testable, scoped question (FINER/PICO)" → `methods-foundations/science_research_question_refiner.md`
  - Example: "Draft an OSF preregistration / Stage-1 Registered Report" → `methods-foundations/science_preregistration_drafter.md` / `science_registered_report_stage1_drafter.md`
  - Example: "Power & sample size with assumptions surfaced + sensitivity grid" → `methods-foundations/science_power_and_sample_size_calculator.md`
  - Example: "Design controls / blinding & randomization" → `methods-foundations/science_negative_and_positive_control_designer.md` / `science_blinding_and_randomization_protocol.md`
  - Example: "Confound & bias audit / Cook-Campbell four-validity walkthrough" → `methods-foundations/science_confound_and_bias_audit.md` / `science_threats_to_validity_walkthrough.md`
  - Example: "Replicability premortem / FAIR reproducibility self-audit" → `methods-foundations/science_replicability_premortem.md` / `science_reproducibility_self_audit.md`
  - **Statistics** → `domain-science/statistics/` (12): test selection, effect-size + uncertainty reporting, multiple-comparisons strategy, results interpretation, pre-specified analysis plan (ICH E9 estimands), outlier handling, p-hacking/forking-paths self-check, Bayesian analysis plan, mixed models, survival analysis, causal inference (DAG/IV/RDD/DiD), PRISMA meta-analysis. See [`statistics/README.md`](../domain-science/statistics/README.md).
  - Example: "Which statistical test, with assumption checks?" → `statistics/science_statistical_test_selector.md`
  - Example: "FWER vs FDR vs hierarchical multiplicity decision" → `statistics/science_multiple_comparisons_strategy.md`
  - Example: "Lock a pre-specified analysis plan / SAP with estimands" → `statistics/science_pre_specified_analysis_plan.md`
  - Example: "Mixed models / survival / causal-inference (DAG) design" → `statistics/science_mixed_models_design.md`
  - Example: "PRISMA-aligned meta-analysis protocol" → `statistics/science_meta_analysis_protocol.md`
  - **Writing & communication** → `domain-science/writing-communication/` (14): IMRaD / figure-first drafting, abstract compression, figure/table legend + design critique, journal selection, cover letter, point-by-point reviewer response, post-rejection appeal, conference abstract, poster spec, preprint release plan, lay summary. Drafts only from user-supplied results (no fabricated data/citations/journal metrics). See [`writing-communication/README.md`](../domain-science/writing-communication/README.md).
  - Example: "Draft an IMRaD / figure-first manuscript from my results" → `writing-communication/science_imrad_paper_drafter.md` / `science_figure_first_paper_skeleton.md`
  - Example: "Write a point-by-point response to reviewers" → `writing-communication/science_response_to_reviewers.md`
  - Example: "Pick a target journal / write a cover letter" → `writing-communication/science_journal_target_selector.md` / `science_cover_letter_to_editor.md`
  - Example: "Plan a preprint release / write a lay summary" → `writing-communication/science_preprint_release_plan.md` / `science_lay_summary_translator.md`
  - **Bench / wet lab** → `domain-science/bench-and-wetlab/` (12): lab-protocol drafter + 5-Whys optimizer, reagent/dilution calculator, buffer designer, cell-culture (authentication + mycoplasma), IACUC (ARRIVE 2.0 + 3Rs) / IRB (Belmont/Common Rule) / biosafety (RG/BSL + IBC scaffold, governance-level) protocols, sample chain-of-custody, failed-experiment post-mortem, ELN entry writer, reagent-validation workflow. Oversight prompts draft + route to the committee (never approve). See [`bench-and-wetlab/README.md`](../domain-science/bench-and-wetlab/README.md).
  - Example: "Draft / troubleshoot a bench protocol; reagent or buffer math" → `bench-and-wetlab/science_lab_protocol_drafter.md` / `science_lab_protocol_optimizer.md` / `science_reagent_and_supply_calculator.md` / `science_buffer_recipe_designer.md`
  - Example: "IACUC / IRB / biosafety (IBC) protocol scaffold" → `bench-and-wetlab/science_animal_protocol_iacuc_drafter.md` / `science_human_subjects_irb_protocol_drafter.md` / `science_biosafety_risk_assessment.md`
  - Example: "Cell-culture protocol / reagent (antibody/primer/cell-line) validation" → `bench-and-wetlab/science_cell_culture_protocol_designer.md` / `science_reagent_validation_workflow.md`
  - Example: "Sample chain-of-custody / ELN entry / failed-experiment post-mortem" → `bench-and-wetlab/science_sample_logging_chain_of_custody_designer.md` / `science_lab_notebook_entry_writer.md` / `science_failed_experiment_post_mortem.md`
  - **Computational / dry lab** → `domain-science/computational/` (14): bioinformatics pipeline design, genomics QC, single-cell & proteomics analysis plans, simulation V&V, numerical-convergence (GCI) audit, computational-reproducibility environment, research-software repo layout (bridge to `domain-software-engineering/`), data-management plan, data dictionary, metadata schema, synthetic-data design, ML-for-science leakage audit + benchmark design. See [`computational/README.md`](../domain-science/computational/README.md).
  - Example: "Design a reproducible bioinformatics pipeline / genomics QC protocol" → `computational/science_bioinformatics_pipeline_designer.md` / `science_genomics_qc_protocol.md`
  - Example: "Validate a simulation (V&V) / numerical-convergence audit" → `computational/science_simulation_validation_protocol.md` / `science_numerical_convergence_audit.md`
  - Example: "Make a study computationally reproducible / lay out a research-software repo" → `computational/science_computational_reproducibility_environment.md` / `science_open_source_research_software_repo_layout.md`
  - Example: "Draft a DMP / data dictionary / metadata schema / synthetic data" → `computational/science_data_management_plan_drafter.md` (+ data_dictionary, metadata_schema, synthetic_data_generator_design)
  - Example: "Audit an ML-for-science pipeline for leakage / design a benchmark" → `computational/science_ml_for_science_validation_audit.md` / `science_ml_for_science_benchmark_design.md`
  - **Funding & grants** → `domain-science/grants-funding/` (10): NIH Specific Aims + R01 outline, NSF (IM+BI) + ERC outlines, the Significance / Innovation / Approach section drafters, resubmission response, budget justification, letter of support. Drafts from the user's own science; funder rules/figures are `[user-supplied]`/verify. See [`grants-funding/README.md`](../domain-science/grants-funding/README.md).
  - Example: "Draft NIH Specific Aims / R01 Research Strategy outline" → `grants-funding/science_specific_aims_drafter.md` / `science_nih_r01_outline_drafter.md`
  - Example: "Outline an NSF or ERC proposal" → `grants-funding/science_nsf_proposal_outliner.md` / `science_erc_grant_outliner.md`
  - Example: "Draft Significance / Innovation / Approach section" → `grants-funding/science_grant_significance_section_drafter.md` (+ innovation, approach)
  - Example: "Resubmission response / budget justification / letter of support" → `grants-funding/science_grant_resubmission_response.md` / `science_grant_budget_justification_drafter.md` / `science_letter_of_support_drafter.md`
  - **Peer review** → `domain-science/peer-review/` (6): structured review drafter + pre-submission self-check, editorial decision letter, reviewer-disagreement arbitration memo, PubPeer-style post-publication critique, replication/robustness review lens. COPE-aligned; evidence-based, non-ad-hominem; suspected misconduct routes via `ethics-integrity/`. See [`peer-review/README.md`](../domain-science/peer-review/README.md).
  - Example: "Draft / self-check a peer review" → `peer-review/science_peer_review_drafter.md` / `science_peer_review_self_check.md`
  - Example: "Editorial decision letter / arbitrate divergent reviews" → `peer-review/science_editorial_decision_drafter.md` / `science_review_disagreement_arbitration_memo.md`
  - Example: "Post-publication critique / review a replication study" → `peer-review/science_post_publication_critique_drafter.md` / `science_review_for_replication_or_robustness.md`
  - **Ethics & integrity** → `domain-science/ethics-integrity/` (8): authorship/credit (CRediT+ICMJE), COI disclosure, FFP/QRP pre-submission self-audit, image-integrity self-check, responsible-AI-use audit, FAIR/CARE/TRUST open-science audit, dual-use (DURC) governance self-screen, correction-vs-retraction walkthrough. These structure / disclose / self-audit and route formal matters to the institution / IBC / editor / COPE — they never adjudicate. See [`ethics-integrity/README.md`](../domain-science/ethics-integrity/README.md).
  - Example: "Resolve authorship / draft a COI disclosure" → `ethics-integrity/science_authorship_and_credit_resolver.md` / `science_conflict_of_interest_disclosure_drafter.md`
  - Example: "Pre-submission misconduct / image-integrity self-audit" → `ethics-integrity/science_misconduct_self_audit.md` / `science_image_integrity_self_check.md`
  - Example: "Dual-use (DURC) self-screen / correction-vs-retraction" → `ethics-integrity/science_dual_use_research_assessment.md` / `science_retraction_or_correction_decision_walkthrough.md`
  - **Lab operations & mentorship** → `domain-science/lab-operations-mentorship/` (10): IDP, lab-meeting + 1:1 + onboarding design, thesis-committee prep, qual question bank, postdoc→PI transition, lab-culture charter, undergrad-mentoring + internship scoping. Trainee dignity / psychological safety first-class; well-being routes to professional support. See [`lab-operations-mentorship/README.md`](../domain-science/lab-operations-mentorship/README.md).
  - Example: "Trainee IDP / 1:1 / onboarding packet / lab-meeting design" → `lab-operations-mentorship/science_individual_development_plan_drafter.md` (+ one_on_one, lab_onboarding_packet_designer, lab_meeting_agenda_designer)
  - Example: "Thesis-committee prep / qual question bank / postdoc→PI transition" → `lab-operations-mentorship/science_thesis_committee_meeting_prep.md` / `science_qualifying_exam_question_bank.md` / `science_postdoc_to_pi_transition_plan.md`
  - **Public engagement & science communication** → `domain-science/public-engagement/` (8): press release, media-interview prep, op-ed, policy brief, legislative testimony, social-media thread, lay explainer, misinformation response. Core theme = overclaim avoidance (calibrated certainty, primary-source links, no fabricated findings). See [`public-engagement/README.md`](../domain-science/public-engagement/README.md).
  - Example: "Press release / media prep / op-ed / policy brief / testimony" → `public-engagement/science_press_release_drafter.md` (+ media_interview_prep, op_ed_drafter, policy_brief_drafter, congressional_or_parliamentary_testimony_prep)
  - Example: "Social-media thread / lay explainer / misinformation response" → `public-engagement/science_social_media_thread_drafter.md` / `science_explainer_for_general_audience.md` / `science_misinformation_response_drafter.md`
  - **Teaching research methods** → `domain-science/teaching-research-methods/` (6): CURE undergrad lab course, research-methods syllabus, journal-club facilitation, science-specific code review, Carpentries-style data-analysis workshop, reproducibility workshop. Teaches research craft itself (distinct from `domain-education-teaching/`). See [`teaching-research-methods/README.md`](../domain-science/teaching-research-methods/README.md).
  - Example: "Design an authentic-research lab course / methods syllabus / journal club" → `teaching-research-methods/science_undergraduate_lab_course_designer.md` / `science_research_methods_syllabus_designer.md` / `science_journal_club_facilitation_guide.md`
  - Example: "Science-specific code review / data-analysis or reproducibility workshop" → `teaching-research-methods/science_code_review_for_science_software.md` / `science_data_analysis_workshop_designer.md` / `science_reproducibility_workshop_designer.md`
  - **Discipline-specific** → `domain-science/disciplines/` (24): biology, chemistry, physics-astronomy, earth-climate, neuroscience, materials-engineering. See [`disciplines/README.md`](../domain-science/disciplines/README.md).
  - Example: "Genomics / microscopy / clinical-trial / omics-metadata / field-ecology design" → `disciplines/biology/`
  - Example: "Synthesis-route critique / characterization battery / reaction kinetics" → `disciplines/chemistry/`

### Personal Development
- **Goals, habits, identity, agency, career, decisions, relationships, resilience, life-transitions, emotional-fitness, self-improvement** → `domain-personal-development/` (~166 prompts; see `EXPANSION_ROADMAP.md`)
  - Example: "Career planning / reposition my career" → `domain-personal-development/career-transformation/career_90_day_repositioning_plan.md`
  - Example: "Skill building" → `domain-personal-development/prompts/goals/goals_skill_breakdown_blueprint.md`
  - **Goals & planning (`prompts/goals/`, 10 prompts):** goal system, reflection cadence, skill-breakdown, annual planning & theme, goal-conflict resolver, anti-goals list, values→goals derivation, progress-stall diagnostic, scope right-sizer. See `prompts/goals/README.md`.
  - **Habits & behavior change (`prompts/habits/`, 10 prompts):** habit design, break a bad habit, stacking, streak recovery, keystone, environment design, identity-based habits, implementation intentions, tracking-system design, temptation bundling. See `prompts/habits/README.md`.
  - **Resilience & motivation (`prompts/resilience/`, 11 prompts, non-clinical):** setback recovery, motivation diagnosis, self-discipline, failure reframe, anti-fragility, momentum rebuild, rejection recovery, criticism processing, confidence rebuild, uncertainty tolerance, comeback-after-dip. See `prompts/resilience/README.md`.
  - **Relationships & social (`prompts/relationships/`, 11 prompts, personal/non-clinical):** boundary script, hard-conversation prep, network cultivation, social-skill development, conflict repair, relationship audit, making friends as an adult, deepening a friendship, difficult-family strategy, apology that lands, loneliness diagnostic. See `prompts/relationships/README.md`.
  - **Thinking & cognitive tools (`prompts/thinking/`, 12 prompts):** blind-spot mirror, fresh perspective, interrogative/question modes, mindset reframe, regret minimization, memory palace, explain-like-I'm-nine, tight-constraint analyzer, decision-journal designer, mental-models application, assumption surfacing. See `prompts/thinking/README.md`.
  - **Productivity (`prompts/productivity/`, 8 prompts):** automation gold mine, meeting killer, zombie-meeting detector, open-loop audit, energy audit, overcommitment/saying-no, energy-by-task-type, focus-ritual design (overlaps `domain-productivity/deep-work/` — cross-link). See `prompts/productivity/README.md`.
  - **Solo-dev / solopreneur (`prompts/solo-dev/`, 10 prompts):** automation audit, burnout prevention, context-switching, network building, skill-gap, pricing-value confidence, deciding alone, accountability system, sustainable-pace design, isolation-motivation. See `prompts/solo-dev/README.md`.
  - **Stakeholder & org politics (`prompts/stakeholder/`, 7 prompts):** navigation guide, politics navigator, managing up, manager-relationship builder, visibility & credit, mentor/sponsor cultivation, cross-team alliance (overlaps `domain-negotiation/` + `domain-product-management/` — cross-link). See `prompts/stakeholder/README.md`.
  - **Life transitions (`prompts/life-transitions/`, 10 prompts, non-clinical):** living through a change already underway — new role, relocation adjustment, new-parenthood identity, empty nest, retirement purpose, job-loss recovery, post-breakup rebuild, return-from-leave, identity-after-change, transition map. The DURING/AFTER complement to `major-decisions/` (BEFORE). Clinical grief/depression/trauma → `domain-psychology/`. See `prompts/life-transitions/README.md`.
  - **Emotional fitness (`prompts/emotional-fitness/`, 10 prompts, NON-CLINICAL everyday skills):** emotion labeling, disappointment processing, jealousy channeling, worry-vs-action sorter, reactivity-trigger audit, ambivalence, self-compassion reset, emotional reset ritual, shame-vs-guilt sorter, charged-event debrief. **Boundary:** not therapy — anyone in/considering therapy, in distress, or with a safety concern → `domain-psychology/client-self-use/` + professional help. See `prompts/emotional-fitness/README.md`.
  - **AI-role career assessments (`prompts/career/`, 17 prompts):** interactive qualification assessments for AI/ML roles (ML eng, prompt eng, product, ethics, research scientist, CV, NLP, etc.). See `prompts/career/README.md`.
  - **Agency, Ownership & Execution (`prompts/agency/`, 13 prompts):**
    - Example: "Convert vague goal into a project I own" → `domain-personal-development/prompts/agency/agency_project_ownership_converter.md`
    - Example: "What's my next concrete action today?" → `domain-personal-development/prompts/agency/agency_next_action_spec.md`
    - Example: "Am I planning instead of executing?" → `domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md`
    - Example: "Design a ship-this-weekend sprint" → `domain-personal-development/prompts/agency/agency_ship_sprint_design.md`
    - Example: "End-of-session review / capture momentum" → `domain-personal-development/prompts/agency/agency_end_of_session_review.md`
    - Example: "Plan a 6-month proof-of-work portfolio" → `domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md`
    - Example: "Extract signal from feedback on my shipped work" → `domain-personal-development/prompts/agency/agency_feedback_extraction.md`
    - Example: "Weekly review that compounds" → `domain-personal-development/prompts/agency/agency_weekly_review.md`
    - Example: "Diagnose stuckness" → `domain-personal-development/prompts/agency/agency_stuck_diagnosis.md`
    - Example: "I need to learn X before I can build Y" → `domain-personal-development/prompts/agency/agency_skill_gap_reframe.md`
    - Example: "Repair a broken habit" → `domain-personal-development/prompts/agency/agency_habit_loop_repair.md`
    - Example: "Run a foundation-building session" → `domain-personal-development/prompts/agency/agency_foundation_session.md`
    - Example: "Rapid-start mode — no warm-up" → `domain-personal-development/prompts/agency/agency_rapid_start_mode.md`
  - **Domain guide:** [domain-personal-development/](../domain-personal-development/)

### Professional Communication
- **PRDs, presentations, proposals, stakeholder communication** → `domain-product-management/`
  - Example: "Interrogative PRD builder (MVP-first)" → `domain-product-management/prompts/product_create_prd.md`
  - Example: "Score a PRD against a rubric" → `domain-product-management/prompts/product_rigorous_prd_evaluation_and_scoring.md`
  - Example: "Cross-functional sprint planner" → `domain-product-management/prompts/product_delivery_sprint_planner.md`
  - Example: "Market size (TAM/SAM/SOM) rapid or comprehensive" → `domain-product-management/prompts/product_market_size_calculator.md`
  - Stakeholder-navigation and org-politics prompts → `domain-personal-development/prompts/stakeholder/` (7 prompts)
  - **Presentations** → `domain-presentations/` (~23 prompts)
  - **Domain guide:** [domain-product-management/](../domain-product-management/)

### Parenting (Ages 4–8, with Neurodivergence Support)
- **Parenting children ages 4–8 (including ADHD, strong-willed, autistic / ASD Level 1 / "HFA")** → `domain-parenting/` (~18 prompts)
  - Example: "Tantrum / meltdown response" → `parenting_meltdown_response_script.md`
  - Example: "Why is she doing this?" → `parenting_behavior_function_decoder.md`
  - Example: "Is this normal for a 5-year-old?" → `parenting_developmental_expectations_4_to_8.md`
  - Example: "I lost it and yelled" → `parenting_repair_conversation_after_rupture.md`
  - Example: "I'm about to lose it" → `parenting_parent_coregulation_reset.md`
  - Example: "Should I talk to the pediatrician?" → `parenting_when_to_seek_professional_help.md`
  - Example: "ADHD kid can't start homework" → `parenting_adhd_executive_function_scaffold.md`
  - Example: "Strong-willed, everything is a fight" → `parenting_strong_willed_power_struggle_defuser.md`
  - Example: "Autistic kid confused by social situation" → `parenting_hfa_social_situation_decoder.md`
  - Example: "Sensory meltdown at the store" → `parenting_sensory_at_home_toolkit.md`
  - Example: "Am I too strict / too soft?" → `parenting_parenting_style_self_assessment.md`
  - Example: "How do I tell my kid grandma died?" → `parenting_hard_topics_age_appropriate_scripts.md`
  - Example: "Our mornings are chaos" → `parenting_daily_routine_designer.md`
  - Example: "Every transition is a meltdown" → `parenting_transitions_and_warnings_protocol.md`
  - Example: "I want to practice before the real moment" → `parenting_scenario_simulator.md`
  - Example: "My kids keep fighting" → `parenting_sibling_conflict_coach.md`
  - Example: "Need to email the teacher" → `parenting_teacher_partnership_email_composer.md`
  - Example: "504 / accommodation meeting prep" → `parenting_school_accommodation_conversation_prep.md`
  - Example: "Sticker chart / allowance / behavior contract pre-mortem" → `parenting_reward_system_premortem.md`
  - **Domain guide:** [domain-parenting/](../domain-parenting/)

### HR & People Management
- **Performance reviews, self-assessment, peer / 360 feedback, calibration** → `domain-hr-management/` (6 prompts)
  - Example: "Write an employee performance review" → `performance-reviews/hr_manager_writing_employee_review.md`
  - Example: "Prepare to give a performance review" → `performance-reviews/hr_reviewer_approach_guide.md`
  - Example: "Role-tailored review scaffold (meta-prompt)" → `performance-reviews/hr_performance_review_meta_prompt.md`
  - Example: "Write my self-review" → `performance-reviews/hr_self_review_assessment.md`
  - Example: "Draft 360 / peer feedback" → `performance-reviews/hr_peer_360_feedback.md`
  - Example: "Run or prep for calibration" → `performance-reviews/hr_calibration_facilitator.md`
  - **Domain guide:** [domain-hr-management/](../domain-hr-management/)

### Specialized Professional Fields
- **Legal, trades, real estate, marketing** → `domain-specialized-fields/` (finance and psychology are now their own top-level domains: `domain-finance/`, `domain-psychology/`)
  - **Professional writing by field** → `domain-professional-writing/domain-specific/` (~26 prompts)
  - Files cover: CPAs, veterinarians, attorneys, contractors, real estate agents, and 21 more fields
  - **Domain guide:** [domain-specialized-fields/](../domain-specialized-fields/)

### Legal (Practitioner Library — Phase 1 + 2A + Family Law, 109 prompts)
- **Live legal workflows for attorneys, paralegals, in-house counsel, legal ops, contract managers** → `domain-legal/`
  - **Domain guide:** [`domain-legal/README.md`](../domain-legal/README.md)
  - **Roadmap:** [`domain-legal/EXPANSION_ROADMAP.md`](../domain-legal/EXPANSION_ROADMAP.md)
  - **Convention:** every prompt requires jurisdiction input, includes a no-fabrication clause for citations and contract terms, locks output format, and ends with a verification checklist + false-positive matrix. No generic "consult counsel" disclaimers.
  - **Research** → `domain-legal/research/` (issue spotting, IRAC memos, statutory interpretation, case briefs, precedent comparison, jurisdiction splits)
  - **Litigation** → `domain-legal/litigation/` (complaints, answers, MTDs, MSJs, MILs, case strategy, settlement valuation, jury instructions, trial themes, budgets)
  - **Discovery** → `domain-legal/discovery/` (RFPs, interrogatories, responses, privilege logs, privilege review protocols, meet-and-confer, custodian interviews, review taxonomies)
  - **Depositions** → `domain-legal/depositions/` (fact + 30(b)(6) outlines, deposition summaries, witness prep, expert deposition prep)
  - **Contracts / Transactional** → `domain-legal/contracts-transactional/` (full and targeted redlines, risk heatmaps, MSA/SOW/NDA/DPA/SaaS/license drafting, term-sheet translation, clause library, negotiation position papers)
  - **Corporate / M&A** → `domain-legal/corporate-ma/` (DD request lists and findings memos, disclosure schedules, board resolutions, §409A/QSBS spotters, post-closing integration)
  - **Employment / Labor** → `domain-legal/employment-labor/` (offer/separation, workplace investigations, PIP/termination risk, wage-hour classification, non-compete enforceability, EEOC position statements)
  - **IP** → `domain-legal/ip/` (patent claim charts, trademark clearance, copyright fair use, DMCA, OSS license compatibility)
  - **Client Intake & Communications** → `domain-legal/client-intake-communications/` (intake summary, engagement letters, demand letters, client status updates)
  - **In-House / Legal Ops** → `domain-legal/in-house-legalops/` (executive matter summary, legal-spend anomaly review, contract playbooks, intake triage, board legal updates)
  - **Divorce / Dissolution** → `domain-legal/divorce/` (22 prompts: intake/case assessment, petition, response/counterpetition, temporary/pendente lite orders, financial affidavit/disclosure, property characterization, property division/equalization, business valuation, retirement/QDRO, hidden-asset/dissipation, divorce tax, spousal support/alimony, settlement/mediation prep, mediation brief, post-mediation term sheet/MOU, marital settlement agreement, prenup/postnup drafting + enforceability, discovery, trial prep, post-judgment modification/enforcement, DV protective order)
  - **Custody / Parenting** → `domain-legal/custody/` (20 prompts: best-interests analysis, UCCJEA jurisdiction, custody petition, temporary/emergency custody, parenting plan, holiday/vacation schedule, high-conflict provisions, child support, modification, relocation/move-away, custody-evaluation prep/response, GAL report response, grandparent/third-party custody/visitation, supervised visitation/safety, parenting-time enforcement/contempt, custody trial prep, paternity/parentage, settlement/mediation prep, custody mediation brief, mediation impasse/package strategy)
  - **Family-law convention:** jurisdiction is load-bearing (community vs. equitable distribution; state best-interests factors; support guidelines; relocation standards all differ); no-fabrication targets enumerated factors, guideline figures, and case names; child support and custody are never bargained non-modifiable; DV/safety is screened, not ignored.
  - **Family law — Self-Advocacy (LITIGANT-FACING)** → `domain-legal/family-self-advocacy/` (23 prompts: this is the **one subsection that inverts the attorney-only, disclaimer-free convention** — it is for a **self-represented or self-organizing layperson** putting together their own side for their lawyer and family court. (It is now **one of two** litigant-facing subsections that invert the convention — the other is `personal-self-advocacy/`, for non-family personal legal matters.) Strong not-legal-advice boundary, mandatory Safety Block, required jurisdiction, no fact fabrication. The prompts **organize/document/prepare only** — they never give advice, predict outcomes, cite statutes, draft filings, or characterize the other party; all of that routes to the attorney. Covers: attorney handoff brief (flagship), case chronology, evidence/exhibit index, communication/incident records, witness/source map, financial-disclosure organizer, asset/debt inventory, budget worksheet, financial-document checklist, allegation-response organizer, neutral factual account, concerns-about-other-party organizer, hearing prep, testimony-practice roleplay, deposition prep, court-process explainer, mediation prep, post-mediation follow-up, mediation-agreement review before signing, consultation-question builder, custody-evaluation/GAL prep, best-interests self-map. Complements — does not duplicate — the emotional/relational `domain-parenting/caregiver-facing/` sets. **Local guide:** [`domain-legal/family-self-advocacy/README.md`](../domain-legal/family-self-advocacy/README.md).)
  - **Personal Legal Self-Advocacy — NON-FAMILY (LITIGANT-FACING)** → `domain-legal/personal-self-advocacy/` (36 prompts across 10 matter subdirectories; the **second** subsection that inverts the attorney-only, disclaimer-free convention). For a **layperson handling their own side** of a non-family personal legal matter: **workplace** (harassment/discrimination/retaliation/wage), **harassment & stalking** (heaviest Safety Block), **defamation/reputation**, **IP theft**, **consumer/scams**, **landlord–tenant**, **identity theft**, **debt collection**, **small claims**, plus **cross-cutting** anchors (professional/authority router, incident organizer, evidence-preservation & digital organizer, chronology builder, professional handoff brief, consultation-question builder). Same load-bearing conventions as `family-self-advocacy/`: required jurisdiction, mandatory Safety Block (verified resources only), no fact fabrication, and **no legal conclusions / no citations / no outcome prediction / no court pleadings** — organize/document/prepare only, routing legal questions to an attorney or authority. Adds a **self-submit variant**: where a channel is built for non-lawyers, it helps draft the user's *own* factual account/letter (HR complaint, police-report account, DMCA notice, FTC/agency report, dispute letters), labeled "NOT A LEGAL FILING," with any statutory certification presented as the user's own attestation to read, verify, and sign. Attorney-side counterparts stay in `employment-labor/`, `ip/`, `litigation/`. **Local guide:** [`domain-legal/personal-self-advocacy/README.md`](../domain-legal/personal-self-advocacy/README.md).

### Discipleship & Mentorship (One-to-One Formation — 60 prompts, TRADITION-NEUTRAL)
- **Walking one person toward maturity in Christ, and running the program that pairs people who need that with people able to give it** (73 prompts across 13 subdirectories) → `domain-discipleship/` — see [README](../domain-discipleship/README.md).
- **This is not a Bible-study domain.** All Scripture engagement, exegesis, doctrine, and lesson-level biblical teaching routes to `domain-biblical-studies/`, which this domain *orchestrates* and never duplicates. Curriculum-architecture patterns are adapted from `domain-education-teaching/`.
- **Eight load-bearing conventions**, enforced as Must/Must-Not constraints in every prompt. Three are inherited or shared, five are this domain's own:
  1. **Tradition-neutral by default; the user may declare** — inherited verbatim from `domain-biblical-studies/`, including the `**Declared tradition (optional).**` input item and the `### Tradition-neutral stance (Must / Must Not)` constraints subsection present in all 60 prompts.
  2. **Anti-fabrication** — Scripture by address only (never quoted from memory), no invented citations, and specifically **no fabricated discipleship research, spiritual-maturity instruments, or growth statistics**.
  3. **Formation is not a metric** — *the failure mode this domain is designed against.* Growth is described as observable practice and self-reported pattern, never as a score, level, tier, percentage, or leaderboard. No prompt emits a number purporting to measure anyone's walk with God, and no stage gate may rank people or withhold belonging.
  4. **A lay mentor is not a counselor, a pastor, or an authority** — mandatory boundary guardrail; mental health, abuse, self-harm, suicidality, addiction, and crisis route to licensed professionals and, where there is danger, to authorities.
  5. **No hotline, agency, or service is named from memory** — always `[VERIFY: identify the correct service from an official source]`.
  6. **No spiritual coercion** — no guilt, fear, shame, urgency, or manufactured deadlines; withdrawal is always available without penalty or explanation.
  7. **Safeguarding is first-class and legal requirements are never stated from memory** — no statute, reporting threshold, age, check requirement, or retention period; all `[VERIFY]` and routed to `domain-legal/`.
  8. **Complements, never replaces, Scripture study and the local church.**
  - **Curriculum architecture** → `domain-discipleship/curriculum-architecture/` (7): multi-stage curriculum blueprint (flagship), formation-outcomes framework (anti-scoring, with a mandatory "what this evidence cannot see"), module scope & sequence, curriculum balance audit, material evaluation (STRONG-GUARD — every product/author/reception claim verify-required), multiplication design (core/local/incidental split, no-cost off-ramp).
  - **Learner pathways** → `domain-discipleship/learner-pathways/` (6): the only learner-voice prompts. Growth self-assessment, personal growth plan, spiritual-practices designer (seven streams, mandatory five-minute no-privacy fallback), stalled-growth diagnostic (seven causes, clinical screen first, bans "insufficient discipline" and "unconfessed sin" as defaults), returning-believer re-engagement (harm screened first), life-constraints adaptation (twelve-axis assumption audit).
  - **Mentor equipping** → `domain-discipleship/mentor-equipping/` (8): readiness assessment (four non-aggregated dimensions, boundary-holding non-compensable), training curriculum (boundaries in session 1, half the time rehearsal), conversation skills, **boundaries & referral (LOAD-BEARING SAFETY** — confidentiality limits declared before disclosure; bans "I'll keep whatever you say between us"**)**, support & sustainability, season debrief.
  - **Pairing & relationship** → `domain-discipleship/pairing-and-relationship/` (8): pairing criteria (safety / fit / preference tiers, bias audit, no-match protocol), relationship covenant (confidentiality limits placed before any invitation to disclose; no vows or submission language), first-meeting guide, cadence design, ending or transition (five ending types; harm endings never get a closing conversation).
  - **Session & lesson** → `domain-discipleship/session-and-lesson/` (6): session-plan builder (works with zero preparation; explicit yield rule), lesson builder (one question, Scripture by address, questions tested against a surprise standard), conversation question bank (three depth tiers with too-far lines), **hard-conversation navigation (event-triggered** — danger check first, verbatim first-sixty-seconds words**)**, small-group format.
  - **Program operations** → `domain-discipleship/program-operations/` (7): program blueprint (safeguarding gate before matching; cohort sized to capacity not demand), **safeguarding & conduct policy (STRONG-GUARD** — states no statute, threshold, or agency; bans internal-assessment-before-referral and exemption by reputation**)**, participant onboarding (every question justified by a decision), program health review (meeting counts explicitly do not measure formation), mentor pipeline (absorbs capacity pressure so the readiness bar never bends).
  - **Topical modules (Wave 2)** → `domain-discipleship/topical-modules/` (8): module *designers*, never doctrinal position papers — money & generosity (tithe left contested; conflict of interest declared; every practice scalable to zero income), work & vocation (two strands: where work can change and where it cannot; no vocation ranked), **sexuality & singleness (STRONG-GUARD** — run/don't-run decision, no disclosure pressure, no orientation-change effort, singleness as a strand that is not about waiting**)**, forgiveness & reconciliation (three things held apart; safety screen before content; reconciliation never owed), suffering & lament (lament as practice, theodicy as a range, explicit refusal to explain anyone's pain), anger & conflict (anger as information; conflict passages taught with their power-imbalance limits attached), digital life (judgment not screen rules; no invented technology statistics; no mentor-held monitoring), witness in a hostile setting (graded hostility; third-party risk; **no security guidance and no country/group characterization, ever**).
  - **Life-stage tracks (Wave 2)** → `domain-discipleship/life-stage-tracks/` (5): **youth & teen (STRONG-GUARD** — structural sheet settled before content; subordinate to the safeguarding policy and returns "cannot be designed yet" without one; response moments carry anti-pressure guards**)**, college & young adult (designed backwards from the exit against a 3-4 year residence window; handoff as a deliverable), married couples (abuse screen run **separately with each spouse** before any joint work; roles question left contested with the abuse guard bound to it), parents (refuses to treat a child's faith as the parent's report card; floor practice that survives the worst week), seniors (access designed before content; giving strand with real recipients; screen that does not become surveillance).
  - **Context variants (Wave 2)** → `domain-discipleship/context-variants/` (4): each restates **someone else's rules as that body states them**, with source and date, and designs inside them — prison & re-entry (facility governs; promise register; release cliff planned before any inside session), campus ministry (institution governs; risk-to-students map; no undeclared supervisory pairings; annual rebuild), workplace & marketplace (employer governs; **no pairing across any reporting or influence line**; protection for colleagues who do not join), remote & diaspora (risk posture and minimal data first; crisis plan made with each participant in advance; **no security guidance or platform recommendation**).
  - **Initiation & catechesis (Wave 2)** → `domain-discipleship/initiation-and-catechesis/` (3): the domain's highest tradition divergence, resolved by nobody — baptism preparation (community's practice run as its own; divergence shown; every pressure mechanism audited out; no counting), membership preparation (**full disclosure before commitment** — authority, discipline with appeal, giving, and how membership ends; safeguarding never inside discipline), catechesis design (three-tier **shared / ours / contested** marking; nothing quoted from memory; no pass mark).
  - **Cross-cultural (Wave 2)** → `domain-discipleship/cross-cultural/` (3): **ask rather than assert** — cross-cultural discipling (refuses all generalizations about nationality, ethnicity, region, or religious background; mentor's own culture written down first; language advantage named as power), oral-preference learners (an oral pathway equal in outcome rather than remedial; assesses nobody's literacy; every Scripture wording sourced, never told from memory), translated-material pitfalls (produces a checking brief for bilingual readers; **never judges translation quality or claims what a word means in a language it cannot read**).
  - **Peer & accountability (Wave 2)** → `domain-discipleship/peer-and-accountability/` (4): the relationships that run sideways — mentor peer cohort curriculum (mentors' own formation; standing risks scheduled to recur; **mentees are not in the room**) and facilitation (meeting shape, four verbatim interventions, power named at the start), accountability partnership design (**every surveillance mechanism banned by name**; no streak, score, or tally; exit requires no explanation) and conversation structure (questions answerable without confession; verbatim response to "I didn't"; scheduled drift checks).
  - **After harm (Wave 3)** → `domain-discipleship/after-harm/` (4): the domain's thirteenth subdirectory, sharing one constraint — **none of these determines what happened, adjudicates it, disciplines anyone, brokers reconciliation, or treats anyone**, and each can return "this is not ours — route it." Four vantage points on one event class: harmed by a previous discipling relationship (**STRONG-GUARD** — learner-voice; safety and clinical screen before any design; "not now" and "not this" kept as complete answers; never characterizes what happened or urges forgiveness), dependency & over-attachment (rules out safeguarding, clinical need, and an unset cadence first; direction established before remedy, including the mentor-is-dependent case; withdrawal banned as a remedy), mentor's own mistake repair (a conduct **gate** that returns a reporting route instead of an apology; every explanatory clause stripped; nothing asked in return), after a mentor is removed (**STRONG-GUARD** — begins only after the responsible body has acted and a referral has been made; care ordered by proximity to harm; refuses investigation, discipline, and communications strategy).
  - **Wave 3 additions to existing subdirectories (9):** mentor case consultation (frame and de-identification **before** disclosure; a standing check that consulting is not replacing a referral; the bounded exception the peer cohort's no-case-conference rule creates) · **doubt & deconstruction posture (STRONG-GUARD** — the mentor's own fear worked first; relationship unconditional on the outcome; no counter-argument, no deadline, and **never a verdict on whether anyone is still a believer**) · **informal pairing without a program (STRONG-GUARD** — returns **"not like this"** for a minor, a vulnerable adult, or an authority line, with no consolation plan attached; cannot manufacture protection that does not exist) · what to expect as a mentee (learner-held; ordinary vs concerning side by side; what is never owed; who to tell, including where there is nobody internal) · long-relationship re-contracting (renew / change shape / release, release requiring no justification) · minimum viable program (floor / deferred / not-attempted against real monthly hours; **safeguarding never scales down**; solves the route past a sole leader) · **program control-drift audit (STRONG-GUARD** — the compliance check load-bearing convention 6 previously lacked; audits your own artifacts, produces changes and **never a verdict**; routes the personal question to `domain-psy-ops/`) · session accessibility design (six axes as defaults offered to everyone; **never assesses whether anyone is disabled or neurodivergent**) · multiplication governance & material drift (local adaptation is the default reading; **no licence, approval process, or fidelity score**).
  - **Boundary with `domain-biblical-studies/`:** four prompts there sit adjacent and are cross-linked, never duplicated — `ministry-contexts/biblical_ministry_new_believer_discipleship_path.md` (a teacher designs a staged path), `church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md` (congregation scale), `church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md` (teaching-program scope), `group-leader-facilitation/biblical_groupleader_apprentice_development.md` (grows a group leader, not a discipler).
  - **Expansion roadmap:** [`domain-discipleship/EXPANSION_ROADMAP.md`](../domain-discipleship/EXPANSION_ROADMAP.md) — includes a permanently-out-of-scope list (no doctrinal adjudication, no maturity scoring, no assessment of whether someone is genuinely converted, no clinical work, no named services, no legal statements, no church discipline).

### Biblical Studies (Bible Study & Research — 129 prompts, TRADITION-NEUTRAL)
- **Bible study, exegesis, sermon prep, and biblical research for six audiences** (laypeople/devotional, small-group & Sunday-school leaders, pastors/preachers, seminary/academic, self-directed learners, ministry-context teachers; 129 prompts across 11 subdirectories) → `domain-biblical-studies/`
  - **Domain guide:** [`domain-biblical-studies/README.md`](../domain-biblical-studies/README.md)
  - **Two load-bearing conventions:** (1) **Tradition-neutral** — prompts describe rather than endorse; they present the text, scholarly consensus, and where traditions differ they attribute readings to identifiable streams (Protestant/Catholic/Orthodox/Jewish/academic-critical) without ruling. A user may *optionally* declare a tradition to shift emphasis, but alternatives are always preserved. (2) **Anti-fabrication first** — every prompt forbids invented citations, misquotes, fabricated scholar/commentary attributions, invented cross-references, and made-up original-language or historical data; verses are referenced by address and verified against named real resources. Higher-risk prompts (word study, translation/variant, historical-cultural, multi-view, doctrine, sermon illustrations) carry heavier STRONG-GUARD language.
  - **Exegesis & Interpretation** → `domain-biblical-studies/exegesis-interpretation/` (passage exegesis workflow, original-language word study, genre-aware reading, historical-cultural & literary context, narrative analysis, rhetorical analysis, ANE comparative context, canonical/intertextual reading, beginner observation, multi-view interpretation map, translation comparison)
  - **Study Methods & Teaching** → `domain-biblical-studies/study-methods-teaching/` (inductive/OIA, SOAP, whole-book overview, small-group discussion guide, lesson plan builder, memorization & reading plans, thematic/topical study)
  - **Sermon & Devotional** → `domain-biblical-studies/sermon-devotional/` (expository sermon prep, illustration developer, daily devotional, meditation, prayer/journaling, series planner, application bridge, manuscript draft, delivery coaching, lectionary prep, liturgical-calendar devotionals)
  - **Theology & Research** → `domain-biblical-studies/theology-research/` (topical/systematic synthesis, multi-tradition doctrine study, interpretive-views comparison, cross-reference/typology mapper, difficult-passage analysis, background research brief, canonical theme trajectory, historical-theology development, biblical-ethics framework, theology of a single book, theological research source map, own-position stress-test, exegetical-fallacy detector, commentary evaluation, creed/confession analysis, worship-practice biblical basis, church government/polity)
  - **Genre-specific reading guides** (in `exegesis-interpretation/`, routed to by the generic genre prompt): parable, prophecy/apocalyptic (STRONG-GUARD), Hebrew poetry/Psalms, wisdom literature, Old Testament law, epistle argument tracing
  - **Learner Self-Study** → `domain-biblical-studies/learner-self-study/` (audience **S** = self-directed individual learner): self-directed study plan, character study, self-quiz/recall, doctrine self-exploration, honest-questions/doubt explorer, study-tool skill builder, comprehension self-check, personal application, reflection journaling, Bible reading habit builder, single-book deep dive, tradition comparison on practices. **Boundary guardrail:** personal study/formation only — NOT pastoral counseling or crisis support; acute distress routes to a pastor, licensed counselor, or emergency services.
  - **Ministry Contexts** → `domain-biblical-studies/ministry-contexts/` (audience **M** = ministry-context teacher): kids' Bible lesson, youth study, new-believer discipleship, seeker intro, family devotions, special-program (VBS/camp/retreat) session, biblical care-conversation foundations (STRONG-GUARD: not therapy; mental-health/abuse/self-harm/crisis routes to professionals), men's/women's study, college/young-adult study, seniors' study, grief/loss Scripture guide (STRONG-GUARD + boundary), marriage enrichment study, parenting Scripture guide. Child-safety guardrails on kids/youth/family/program prompts. Cross-domain links to `domain-psychology/` and `domain-parenting/`.
  - **Church Staff & Ministry Ops** → `domain-biblical-studies/church-staff-ministry-ops/` (audience **P/G**): curriculum scope & sequence, curriculum selection/evaluation, teacher training, multi-service teaching coordination, annual teaching calendar, volunteer recruitment & role design, small-group launch system, discipleship pathway design, midweek program design, sermon feedback/debrief.
  - **Group-Leader Facilitation** → `domain-biblical-studies/group-leader-facilitation/` (audience **G/P**): facilitation dynamics (silence, dominance, tangents, conflict), handling hard questions, heretical-claim response (STRONG-GUARD: "orthodox" = ecumenical-creed level), mixed-maturity leveling, conflict resolution, hybrid/online format, apprentice development.
  - **Original Languages** → `domain-biblical-studies/original-languages/` (highest fabrication risk; **all eighteen carry STRONG-GUARD**, everything verify-required): parsing/morphology helper, Greek syntax, Hebrew syntax, Greek verbal aspect & Aktionsart, Greek voice & deponency, discourse analysis, original-language idiom/figures of speech, semantic domains & componential analysis (Louw-Nida), OT-in-NT usage, Septuagint usage, textual criticism primer, Masorah & Qere/Ketiv, Hebrew cantillation & Greek accentuation, Aramaic analysis, canon/versification differences, comparative Semitics & cognates, Koine register/papyri & inscriptions, Greek/Hebrew vocabulary builder. Cross-links the word-study prompt in `exegesis-interpretation/`.
  - **Biblical Theology Method** → `domain-biblical-studies/biblical-theology-method/` (audience **A/P**): biblical vs. systematic theology (worked example), redemptive-historical reading (STRONG-GUARD), author theology comparison (STRONG-GUARD), center-of-biblical-theology debate (STRONG-GUARD). Method-level prompts above exegesis, below systematics.
  - **Apologetics & Engagement** → `domain-biblical-studies/apologetics-engagement/` (audience **P/A**): objection engagement, Bible reliability, comparative worldview, faith & science, conversation prep, problem of evil/theodicy, biblical contradictions, interfaith dialogue. All STRONG-GUARD except conversation prep. Custom banner addresses fabricated philosophical arguments, misrepresented worldview positions, and invented historical/archaeological evidence.
  - **Expansion roadmap:** [`domain-biblical-studies/EXPANSION_ROADMAP.md`](../domain-biblical-studies/EXPANSION_ROADMAP.md)

### Psychology, Therapy & Behavioral Health
- **Provider and client-facing prompts for psychology / therapy / mental-health workflows** → `domain-psychology/`
  - **Local index & subdirectory map:** [`domain-psychology/PROMPT_INDEX.md`](../domain-psychology/PROMPT_INDEX.md)
  - **Field guide (techniques + ethical considerations):** [`domain-psychology/field_guide.md`](../domain-psychology/field_guide.md)
  - Note: prompts in this domain are authored at full clinical fidelity for model-testing purposes; frontmatter sets `intended_use: model-testing`. They are not meant for live clinical use.
- **Documentation & note formats** → `domain-psychology/documentation/` (15 prompts)
  - Example: "SOAP progress note" → `psychology_soap_progress_note.md`
  - Example: "DAP / BIRP / GIRP / PIRP note" → `psychology_dap_progress_note.md` / `..._birp_...` / `..._girp_...` / `..._pirp_...`
  - Example: "Biopsychosocial intake (CPT 90791/90792)" → `psychology_intake_assessment_note.md`
  - Example: "Initial treatment plan with golden thread" → `psychology_initial_treatment_plan.md`
  - Example: "90-day treatment plan update" → `psychology_treatment_plan_update.md`
  - Example: "Discharge / termination / group / collateral / telehealth / supervision notes" → `psychology_discharge_summary.md` etc.
- **Risk & crisis** → `domain-psychology/risk-crisis/` (10 prompts)
  - Example: "Columbia C-SSRS suicide risk assessment" → `psychology_columbia_suicide_risk_assessment.md`
  - Example: "Stanley-Brown safety plan" → `psychology_stanley_brown_safety_plan.md`
  - Example: "CALM lethal-means counseling script" → `psychology_lethal_means_counseling_script.md`
  - Example: "Homicidal ideation triage with HCR-20 frame" → `psychology_homicidal_ideation_triage.md`
  - Example: "NSSI four-function analysis + replacement-skill plan" → `psychology_self_harm_functional_assessment.md`
  - Example: "Post-attempt re-engagement (90-day window)" → `psychology_post_attempt_reengagement_plan.md`
  - Example: "Mandated-reporter (CPS/APS) decision walkthrough" → `psychology_mandated_reporter_decision_walkthrough.md`
  - Example: "Tarasoff / duty-to-protect four-element analysis" → `psychology_tarasoff_duty_to_warn_analysis.md`
  - Example: "Civil commitment / involuntary hold narrative (DTS/DTO/GD)" → `psychology_civil_commitment_narrative.md`
  - Example: "In-session crisis de-escalation & disposition plan" → `psychology_crisis_de_escalation_session_plan.md`
- **Pre-existing prompts (relocated 2026-05-08):**
  - Intake / assessment → `intake-assessment/` (behavioral observation FBA, psychometric instrument evaluator)
  - Diagnostic formulation → `diagnostic-formulation/` (case conceptualization framework)
  - Treatment planning → `treatment-planning/` (behavior change plan, psychoeducation material)
  - Modalities — CBT → `modalities/cbt/` (cognitive distortion identifier)
  - Practice operations → `practice-operations/` (informed-consent template)
  - Supervision / professional → `supervision-professional/` (therapeutic technique explainer)
  - Research / organizational → `research-organizational/` (org culture diagnostic, qualitative theme analyzer, research interview protocol)
- **Future waves planned** (modalities expansion, populations, psychiatric prescriber, care coordination, client self-use): see [`PROMPT_INDEX.md`](../domain-psychology/PROMPT_INDEX.md) for the full expansion plan.

### Prompt Engineering
- **Meta-prompts about creating/improving prompts** → `domain-prompt-engineering/` (~47 prompts)
  - Example: "Improve my prompt" → `prompt-improvement/`
  - Example: "Diagnose why the model isn't following my instructions" → `model-behavior/`
  - Example: "Move the model off its default / median output" → `escape-median/`
  - Example: "Am I solving the right problem? Workshop the constraints" → `goal-orientation/`
  - Example: "Build my prompt-engineering skill over months" → `skill-development/`
  - Example: "Delegate this task to AI" → `delegation/`
  - Example: "GPT optimization" → `model-optimization/`
  - Example: "Evaluate AI correctness / task difficulty" → `evaluation/`

---

### Financial Records Processing (Statements → Verified, Categorized, Flagged Spreadsheets)
- **Process bank/credit-card statements into organized spreadsheets for review (e.g. divorce/custody prep)** → `domain-agentic-resources/skills/financial-records/` (4 skills) + 2 agents + 1 command. A staged, tool-agnostic pipeline (Claude Code + Codex). A self-contained copy lives at repo root: `financial-records-toolkit/`.
  - **Local guide:** [`domain-agentic-resources/skills/financial-records/README.md`](../domain-agentic-resources/skills/financial-records/README.md)
  - **Convention:** organizes facts only (no legal advice / no intent claims); verification is a hard gate before categorize/flag; no fabricated merchants (unknowns are queued, not guessed); sensitive PII stays local and out of version control.
  - Example: "Extract my bank statement PDFs into Excel" → `financial-records/pdf-statement-extractor/`
  - Example: "Verify every transaction transferred correctly" → `financial-records/statement-reconciliation-verifier/`
  - Example: "Categorize transactions / identify unknown merchants" → `financial-records/transaction-categorizer/`
  - Example: "Flag transactions for my divorce attorney" → `financial-records/divorce-financial-flagger/`
  - Example: "Run the whole pipeline over a folder of statements" → command `/process-financials` (agent `financial-records-orchestrator`)

---

### AI Investment Research Toolkit (Paper-First Research Loop — Patterns, Screen, Monitor, Paper Action, Calibration)
- **Run a paper-first AI investment research loop** — deep research → pattern discovery → screen → monitor → paper decision → journal/calibrate, with every high-risk surface gated → `ai-investment-research-toolkit/` (8 stage prompts + orchestrator + 4 commands + 3 agents + 4 skills). A self-contained, local-first bundle (Claude Code + Codex) at repo root; it **orchestrates** the existing `domain-finance/` analytical prompts rather than rebuilding them.
  - **Master blueprint:** [`ai-investment-research-toolkit/ARCHITECTURE.md`](../ai-investment-research-toolkit/ARCHITECTURE.md) · **Flow / build status:** [`PIPELINE_OVERVIEW.md`](../ai-investment-research-toolkit/PIPELINE_OVERVIEW.md) · **Codex entry point:** [`AGENTS.md`](../ai-investment-research-toolkit/AGENTS.md)
  - **Convention:** paper-first (no real-money path — `LiveBrokerAdapter` ships **disabled** behind Gate C); no fabricated data (unknowns are queued `UNAVAILABLE`, never guessed); gates + kill switch enforced as **code-not-trust**: Gate A (only out-of-sample-`validated` patterns score), Gate B (no order without sizing + pre-mortem + risk-limit check), Gate C (real-money lock), and the `mandate.yaml: halt` kill switch that stops action Stages 4–6.
  - **Three modes:** *guided* (run the orchestrator) · *commands* (Claude Code slash commands) · *manual* (walk the stage prompts).
  - Example: "Run a full cadence pass (Stages 0→7)" → `orchestrator_investment_research.md` or command `/investment-run` (agent `research-orchestrator`)
  - Example: "Validate my config before a run (mandate/risk/scope/data sources)" → `prompts/stage-0-mandate-config.md`
  - Example: "Source a point-in-time universe snapshot" → `prompts/stage-1-universe-data-sourcing.md`
  - Example: "Build a per-candidate research dossier" → `prompts/stage-2-deep-research.md`
  - Example: "Discover / validate / retire a pattern (Gate A, anti-overfitting)" → `prompts/stage-3-pattern-knowledge-base.md` (agent `pattern-miner`)
  - Example: "Screen the universe into a ranked watchlist" → `prompts/stage-4-screening.md` or command `/screen`
  - Example: "Daily monitor / tripwire sweep ('see the train coming')" → `prompts/stage-5-monitoring-tripwires.md` or command `/monitor` (agent `monitor-agent`)
  - Example: "Decide and place a PAPER order behind Gate B/C" → `prompts/stage-6-decision-paper-action.md` or command `/decide <ticker>`
  - Example: "Journal a prediction + score Brier / calibration" → `prompts/stage-7-journaling-calibration.md`
  - Example: "Net-new finance prompts it relies on" → `domain-finance/crypto/`, `domain-finance/options/`, `domain-finance/quant-fintech-data/` (token valuation, on-chain metrics, smart-contract risk, options structure, IV/Greeks, pattern pre-registration, out-of-sample validation, signal-decay monitor)

---

### Agentic System Factory (Use Case → Production-Ready Agentic System Design Bundle)
- **Produce a production-ready agentic workflow from a stated use case** — the way this repo produces prompts/skills/agents — gating every step on the verified engineering/security/eval/governance rigor → `agentic-system-factory/` (master orchestrator + stages 0–7 + 5 commands + 3 agents + code-not-trust gate scripts). A self-contained, dual-audience (repo curator + external dev) bundle at repo root. It **orchestrates** the existing `domain-AI-ML/agentic-ai-systems/` design prompts and is built on the `authoring/system-patterns/` manual rather than rebuilding either.
  - **Master blueprint:** [`agentic-system-factory/ARCHITECTURE.md`](../agentic-system-factory/ARCHITECTURE.md) · **Flow / build status:** [`PIPELINE_OVERVIEW.md`](../agentic-system-factory/PIPELINE_OVERVIEW.md) · **Codex entry point:** [`AGENTS.md`](../agentic-system-factory/AGENTS.md) · **Worked run:** [`GOLD_STANDARD_RUN.md`](../agentic-system-factory/GOLD_STANDARD_RUN.md)
  - **The manual it operationalizes:** [`authoring/system-patterns/`](../authoring/system-patterns/) — the fourth authoring system (6-step process, 9-topology pattern index, 100-pt rubric, gate/eval/architecture templates, gold-standard design).
  - **Convention:** Gate 0 (complexity-ladder justification — agent vs deterministic workflow), Gate A (OWASP-ASI security), Gate B (ABC-valid eval + OpenAgentSafety real-tool safety), Gate C (disclosure manifest + observability + rollback) enforced as **code-not-trust** by stdlib-only `scripts/`; always produces the framework-agnostic design bundle first, optional Stage-7 code-gen (all six stacks: Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex) stays version-neutral.
  - **Three modes:** *guided* (run the orchestrator) · *commands* (slash commands) · *manual* (walk the stage prompts) · *surgical* (jump to one stage).
  - Example: "Take my use case and design a production-ready agentic system" → `agentic-system-factory/orchestrator_agentic_system.md` or command `/author-agentic-system`
  - Example: "Does this even need an agent? (Gate 0)" → `prompts/stage-0-justify.md` or command `/justify-agent`
  - Example: "Pick the lowest-complexity topology" → `prompts/stage-2-topology.md` or command `/topology-pick`
  - Example: "Design enforced security/eval/governance gates + kill switch" → `prompts/stage-4-gates.md`
  - Example: "Design an ABC-valid eval + real-tool safety harness" → `prompts/stage-5-eval.md` or command `/agent-eval`
  - Example: "Emit stack-specific runnable scaffolding (any of the 6 supported stacks)" → `prompts/stage-7-codegen.md` or command `/emit-stack-code`

---

### Children's Book Studio (Idea → Finished, Publishable Children's Book)
- **Take a children's-writing idea to a finished, queryable manuscript + submission package** — a runnable agentic pipeline that **orchestrates** the existing `domain-childrens-writing/` prompts (referenced in place, not duplicated) and was **designed with `agentic-system-factory/`** → `childrens-book-studio/` (master orchestrator + 7 stage prompts + 3 agents + 4 commands + factory design bundle). A self-contained toolkit at repo root. Covers all 13 forms (board book → upper-MG/young-teen crossover; fiction + narrative/expository nonfiction; short stories).
  - **Entry points:** [`README.md`](../childrens-book-studio/README.md) · flow [`PIPELINE_OVERVIEW.md`](../childrens-book-studio/PIPELINE_OVERVIEW.md) · rationale [`ARCHITECTURE.md`](../childrens-book-studio/ARCHITECTURE.md) · proof-of-rigor [`design-bundle/`](../childrens-book-studio/design-bundle/) · worked run [`DRY_RUN.md`](../childrens-book-studio/DRY_RUN.md)
  - **Convention:** four hard gates enforced by **orchestrator critique** (not scripts — low blast radius): Gate 0 age-boundary (mature-YA → `domain-creative-writing/`), Gate A craft integrity (child agency · no preaching · read-aloud rhythm · reading level), Gate B truth & representation (nonfiction no-fabrication + back matter · representation audit = flags-only, never certified · no age-inappropriate content), Gate C publishing honesty (no invented comps/agents — all bracketed `[AUTHOR TO VERIFY]`). Inherits the 9 load-bearing conventions of `domain-childrens-writing/`.
  - **Four modes:** *guided* (run the orchestrator) · *commands* (slash commands) · *manual* (walk `PIPELINE_OVERVIEW.md`) · *surgical* (jump to one stage).
  - Example: "Write me a finished children's book (full pipeline)" → `childrens-book-studio/orchestrator_childrens_book.md` or command `/write-childrens-book`
  - Example: "Revise my existing kids' draft (craft-integrity gate)" → `prompts/stage-4-revision-triage.md` or command `/revise-manuscript`
  - Example: "Retarget my draft to an age band / reading level" → command `/calibrate-reading-level`
  - Example: "Build a submission package (query/synopsis/comps) for my finished manuscript" → `prompts/stage-6-publishing-package.md` or command `/build-submission-package`

---

### Sourced Nonfiction Studio (Uncited Expertise → Sourced, Publishable Nonfiction)
- **Take a domain expert's uncited knowledge (learned over years, no sources) and turn it into a legally-screened, publishable nonfiction product** — a runnable agentic pipeline that **orchestrates** existing repo prompts (research / epistemic / legal / writing, referenced in place) → `sourced-nonfiction-studio/` (orchestrator + 7 stage prompts + 4 agents + 5 commands + a stdlib citation gate). Self-contained toolkit at repo root. Separates verifiable facts from professional judgment, runs **live** web/PubMed/Consensus searches for real sources, maps every claim to a reference, honestly reframes what can't be sourced, and screens for copyright/defamation/plagiarism. Terminal artifacts: **fact→source matrix + cited manuscript + risk report**.
  - **Entry points:** [`README.md`](../sourced-nonfiction-studio/README.md) · flow [`PIPELINE_OVERVIEW.md`](../sourced-nonfiction-studio/PIPELINE_OVERVIEW.md) · rationale [`ARCHITECTURE.md`](../sourced-nonfiction-studio/ARCHITECTURE.md) · worked run w/ a real live citation [`DRY_RUN.md`](../sourced-nonfiction-studio/DRY_RUN.md) · portable variant [`PROMPT_PACK_PLAN.md`](../sourced-nonfiction-studio/PROMPT_PACK_PLAN.md)
  - **Cardinal rule:** a citation is real or it does not exist — never fabricated/guessed. Unsourceable claims are **softened, reframed as the author's labeled judgment, or cut**, never asserted as fact.
  - **Convention:** gates enforced by **orchestrator critique** (content-integrity blast radius) + one thin stdlib script. Gate A sourcing-integrity (no orphan/fabricated/unverified-as-fact citations; `scripts/check_citations.py` is the mechanical floor) **blocks assembly**; Gate B legal-safety (fair-use + defamation/publicity + plagiarism, flagged & routed to counsel — **not legal advice, clears nothing**); Gate C publish-readiness. Field-pluggable via `config/source-standards-profiles.yaml`.
  - **Four modes:** *guided* (run the orchestrator) · *commands* (slash commands) · *manual* (walk `PIPELINE_OVERVIEW.md`) · *surgical* (one stage; jump between gates, never through Gate A).
  - Example: "Source my uncited draft into a cited, publishable piece (full pipeline)" → `sourced-nonfiction-studio/orchestrator_sourced_nonfiction.md` or command `/source-my-draft`
  - Example: "Extract and type the claims in my braindump (fact vs judgment)" → `prompts/stage-1-claim-extraction-typing.md` or command `/extract-claims`
  - Example: "Find real sources for these factual claims" → `prompts/stage-2-source-discovery.md` + `stage-3-claim-source-matching.md` or command `/find-sources`
  - Example: "Fact-check my finished cited draft against its sources" → command `/fact-check-manuscript`
  - Example: "Run a legal-risk pass (copyright/defamation/plagiarism)" → `prompts/stage-5-legal-risk-integrity.md` or command `/risk-pass`
  - **Net-new reusable prompts it added (indexed in their domains):** `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` (KEEP/SOFTEN/REFRAME/QUOTE/CUT for uncitable claims), `domain-research-academic/research_manuscript_fact_check_reconciler.md` (reconcile draft vs sources), `domain-legal/ip/legal_defamation_publicity_risk_screen.md` (defamation/right-of-publicity screen).

---

### Multi-Agent Workflows
- **Agent orchestration** → `domain-agentic-resources/personas/` (52 personas)
  - Example: "Run development pipeline" → `specialized/agents_orchestrator.md`
  - Example: "Quality gate" → `testing/testing_reality_checker.md`
- **Multi-agent architecture design** → `domain-agentic-resources/commands/multi-agent/` (8 prompts)
  - Example: "Should I split to multi-agent?" → `multiagent_scaling_vs_single_agent_diagnosis.md`
  - Example: "Design planner / worker / judge" → `multiagent_two_tier_architecture_template.md`
  - Example: "Lock down a worker's scope" → `multiagent_worker_isolation_boundaries.md`
  - Example: "Minimize an agent's tool set" → `multiagent_tool_set_minimization.md`
  - Example: "Checkpoint + restart design" → `multiagent_graceful_session_endings.md`
  - Example: "Define good-enough gates" → `multiagent_good_enough_gate_design.md`
  - Example: "Find coordination choke points" → `multiagent_coordination_choke_point_analysis.md`
  - Example: "Coordinate agents via tests + policy" → `multiagent_coordination_via_tests_and_policy.md`
- **Auto-improving agent systems & agent task design** → `domain-engineering-workflows/ai-patterns/`
  - Example: "Audit task set / metrics / traces" → `ai_pattern_auto_improving_triplet_diagnostic.md`
  - Example: "Metric-gaming pre-mortem" → `ai_pattern_auto_improving_metric_gaming_premortem.md`
  - Example: "Trace infrastructure audit" → `ai_pattern_auto_improving_trace_infrastructure_audit.md`
  - Example: "Spec a first agent-delegated task" → `ai_pattern_agent_task_first_delegation_spec.md`
  - Example: "Score task's code distance" → `ai_pattern_agent_task_code_distance_scorer.md`
  - Example: "Design an agent work loop" → `ai_pattern_agent_work_loop_design.md`
  - Example: "Scan agent code for footguns" → `ai_pattern_agent_code_footgun_detector.md`
  - Example: "Translate agent jargon for stakeholders" → `ai_pattern_agent_autonomy_jargon_translator.md`

### AI / ML Engineering (`domain-AI-ML/`) — the full practitioner lifecycle

**326 prompts across 16 subdirectories** — the canonical home for *doing* AI/ML work: framing, data, features, modelling, evaluation, optimization, MLOps, monitoring, governance, GenAI/LLM engineering, agentic systems, specialized verticals, product leadership, and learning. See [`domain-AI-ML/README.md`](../domain-AI-ML/README.md) for the full routing table and [`EXPANSION_ROADMAP.md`](../domain-AI-ML/EXPANSION_ROADMAP.md) for the shipping record and the authoritative boundary table.

**Boundary (tie-break rule).** ML/AI engineering judgment about *the model itself* — its data, training, evaluation, serving, security, governance — lives here. The surrounding discipline's judgment lives in that discipline's domain: causal inference and survival analysis → `domain-science/statistics/`; prompt patterns and RAG prompt templates → `domain-prompt-engineering/`; regulated-finance model validation → `domain-finance/`; statutory interpretation → `domain-legal/`; clinical validity → `domain-healthcare-clinical/`; whole-system agentic authoring → `agentic-system-factory/` + `authoring/system-patterns/`; runnable skills → `domain-agentic-resources/skills/`.

**Conventions.** One filename prefix per subdirectory (`mlframe_`, `mldata_`, `mlfeature_`, `mlmodel_`, `dl_`, `mleval_`, `mlopt_`, `mlops_`, `mlmonitor_`, `genai_`, `aiagent_`, `rai_`, `aipm_`, `mllearn_`, plus `cv_`/`nlp_`/`recsys_`/`ts_`/`rl_`/`graphml_`/`mlmodal_`). Framework-neutral by default — the user names the stack. Every prompt carries a no-fabrication clause (no invented benchmarks, accuracy figures, SOTA claims, or dataset statistics) and an ML-specific False-Positive Prevention block.

- **1. Frame — before any modelling** (`problem-framing-scoping/`, 10): **"I don't know where to start / the model isn't working"** → `mlframe_domain_triage_router.md` (the front door — classifies the situation and emits an ordered prompt sequence); "is this even an ML problem?" → `domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md`; "turn my business problem into an ML task" → `mlframe_problem_to_ml_task_translator.md`; "scope the use case" → `mlframe_ml_use_case_canvas.md`; "what should success look like?" → `mlframe_success_metric_selection.md`; "do we have the data?" → `mlframe_data_readiness_assessment.md`; "is it feasible?" → `mlframe_feasibility_risk_assessment.md`; "what does a wrong prediction cost?" → `mlframe_cost_of_being_wrong_analysis.md`; "baseline first" → `mlframe_baseline_first_design.md`; "build, buy, or fine-tune?" → `mlframe_build_buy_finetune_decision.md`.
- **2. Data** (`data-for-ml/`, 19): "curate / audit the dataset" → `mldata_dataset_curation_plan.md`, `mldata_data_quality_audit.md`; "results look too good to be true" → `mldata_data_leakage_detector.md`; "how do I split train/test?" → `mldata_train_test_split_strategy.md`; "labeling guidelines / annotation quality" → `mldata_labeling_guideline_designer.md`, `mldata_annotation_quality_review.md`; "classes are imbalanced" → `mldata_class_imbalance_strategy.md`; "augment / synthesize data" → `mldata_data_augmentation_plan.md`, `mldata_synthetic_data_strategy.md`; "is my sample biased?" → `mldata_sampling_bias_audit.md`; "version data / lineage" → `mldata_data_versioning_lineage.md`; "data contract / schema evolution / enforce in CI" → `mldata_data_contract_design.md`, `mldata_schema_evolution_strategy.md`, `mldata_data_contract_enforcement_ci.md`; "document the dataset" → `mldata_datasheet_authoring.md`; "where should I spend labelling budget?" → `mldata_active_learning_strategy.md`; "derive labels instead of buying them" → `mldata_weak_supervision_strategy.md`.
- **3. Features** (`feature-engineering/`, 9): "what features should I build?" → `mlfeature_ideation_workshop.md`; "which features matter?" → `mlfeature_selection_strategy.md`, `mlfeature_importance_analysis.md`; "how do I encode these?" → `mlfeature_encoding_strategy.md`; "keep leakage out of the pipeline" → `mlfeature_leakage_safe_pipeline.md`; "features drifted" → `mlfeature_drift_audit.md`; "do I need a feature store?" → `mlfeature_store_design.md`.
- **4. Model — classical** (`classical-ml-modeling/`, 10): "which algorithm?" → `mlmodel_algorithm_selection_matrix.md`; "baseline plan" → `mlmodel_baseline_modeling_plan.md`; "cross-validation / hyperparameter tuning" → `mlmodel_cross_validation_design.md`, `mlmodel_hyperparameter_tuning_strategy.md`; "overfitting or underfitting?" → `mlmodel_overfitting_underfitting_diagnosis.md`; "regularize / ensemble / calibrate" → `mlmodel_regularization_strategy.md`, `mlmodel_ensembling_strategy.md`, `mlmodel_probability_calibration.md`; "imbalanced classification" → `mlmodel_imbalanced_classification_approach.md`; "model people can interpret" → `mlmodel_interpretability_first_modeling.md`.
- **5. Model — deep learning** (`deep-learning/`, 15): "pick a neural architecture" → `dl_architecture_selection.md`; "training loss won't go down" → `dl_training_not_converging_debug.md`; "exploding / vanishing gradients" → `dl_gradient_issue_debug.md`; "learning rate and optimizer" → `dl_learning_rate_optimizer_selection.md`; "fine-tune / transfer-learn" → `dl_fine_tuning_strategy.md`, `dl_transfer_learning_plan.md`; "multi-GPU / mixed precision" → `dl_distributed_training_plan.md`, `dl_mixed_precision_setup.md`; "data loader is the bottleneck" → `dl_data_loading_bottleneck_audit.md`; "make training reproducible" → `dl_reproducibility_setup.md`; "overfitting remedies" → `dl_overfitting_diagnosis_remedies.md`, `dl_regularization_strategy.md`; "pretrain on unlabelled domain data" → `dl_self_supervised_pretraining.md`; "add classes without forgetting" → `dl_continual_learning_strategy.md`; "is mixture-of-experts worth it?" → `dl_mixture_of_experts_design.md`.
- **6. Evaluate** (`model-evaluation-validation/`, 16): "what metric should I optimize?" → `mleval_metric_selection_guide.md`; "build an eval harness" → `mleval_evaluation_harness_design.md`; "where is my model failing?" → `mleval_error_analysis_slicing.md`; "is this improvement real?" → `mleval_statistical_significance_testing.md`, `mleval_baseline_comparison_protocol.md`; "my eval results look too good" → `mleval_eval_result_skepticism_audit.md`; "offline metrics don't match prod" → `mleval_offline_online_alignment.md`; "A/B test two models" → `mleval_ab_test_design_for_models.md`; "stress-test robustness / design a benchmark" → `mleval_robustness_stress_testing.md`, `mleval_benchmark_design.md`; "are my probabilities calibrated?" → `mleval_calibration_assessment.md`; "read this confusion matrix" → `mleval_confusion_matrix_interpretation.md`; "how sure is the model, and can I act on it?" → `mleval_uncertainty_quantification_design.md`; "I need a coverage guarantee" → `mleval_conformal_prediction_design.md`; "flag inputs the model shouldn't be trusted on" → `mleval_ood_detection_design.md`; "when should it decline to answer?" → `mleval_selective_prediction_abstention.md`.
- **7. Optimize — small, fast, cheap** (`model-optimization-efficiency/`, 11): "inference is too slow" → `mlopt_inference_latency_optimization.md`; "quantize / prune / distill" → `mlopt_quantization_plan.md`, `mlopt_pruning_strategy.md`, `mlopt_knowledge_distillation_plan.md`; "what do I give up by compressing?" → `mlopt_compression_tradeoff_analysis.md`; "run it on-device / at the edge" → `mlopt_edge_deployment_optimization.md`; "which accelerator?" → `mlopt_hardware_accelerator_selection.md`; "raise throughput / tune batching" → `mlopt_throughput_batching_optimization.md`; "LLM serving slow or expensive (KV cache, speculative decoding, continuous batching)" → `mlopt_llm_inference_serving_optimization.md`; "PTQ lost too much accuracy" → `mlopt_quantization_aware_training.md`; "route easy requests to a cheaper model" → `mlopt_model_routing_cascade_design.md`.
- **8. Ship — MLOps & infrastructure** (`mlops-infrastructure/`, 22): "experiment tracking" → `mlops_experiment_tracking_setup.md`; "model registry / packaging" → `mlops_model_registry_design.md`, `mlops_model_packaging_strategy.md`; "ML CI/CD" → `mlops_ml_cicd_pipeline_design.md`; "orchestrate training / feature pipelines" → `mlops_training_pipeline_orchestration.md`, `mlops_feature_pipeline_design.md`; "design model serving" → `mlops_model_serving_architecture.md`; "nobody can reproduce this run" → `mlops_reproducibility_audit.md`, `mlops_environment_dependency_management.md`; "ML bill is out of control" → `mlops_infra_cost_optimization.md`, `mlops_cost_attribution_showback.md`, `mlops_cost_budget_forecasting.md`; "carbon cost" → `mlops_carbon_accounting_deep_dive.md`; "how mature is our MLOps?" → `mlops_maturity_assessment.md`; "how many GPUs do we need?" → `mlops_gpu_capacity_planning.md`; "batch, streaming, or on-demand inference?" → `mlops_batch_vs_streaming_inference.md`; "update continuously from production feedback" → `mlops_online_learning_pipeline_design.md`.
- **9. Monitor — production** (`production-monitoring/`, 16): "detect drift" → `mlmonitor_drift_detection_design.md`; "model degraded in prod" → `mlmonitor_performance_degradation_triage.md`; "when should we retrain?" → `mlmonitor_retraining_trigger_strategy.md`; "dashboards / SLOs" → `mlmonitor_monitoring_dashboard_design.md`, `mlmonitor_slo_design_for_ml.md`; "roll out safely / roll back" → `mlmonitor_canary_shadow_deployment.md`, `mlmonitor_rollback_strategy.md`; "ML incident / postmortem / runbooks" → `mlmonitor_ml_incident_response.md`, `mlmonitor_incident_postmortem_template.md`, `mlmonitor_incident_runbook_library.md`; "GenAI or CV incident patterns" → `mlmonitor_genai_incident_patterns.md`, `mlmonitor_cv_incident_patterns.md`; "model influencing its own training data" → `mlmonitor_feedback_loop_detection.md`; "data-pipeline health" → `mlmonitor_data_pipeline_health_audit.md`; "run challengers against production continuously" → `mlmonitor_champion_challenger_design.md`; "how many models are we running and who owns them?" → `mlmonitor_model_portfolio_health_review.md`.
- **10. Govern — responsible AI & regulation** (`responsible-ai-governance/`, 25): "is my model biased?" → `rai_bias_detection_audit.md`; "fairness metric / mitigation" → `rai_fairness_metric_selection.md`, `rai_fairness_mitigation_strategy.md`; "explain / interpret the model" → `rai_explainability_plan.md`, `rai_interpretability_analysis.md`; "model card / doc suite / freshness" → `rai_model_card_authoring.md`, `rai_documentation_suite_orchestrator.md`, `rai_documentation_freshness_audit.md`; "AI governance / ethics review" → `rai_governance_framework_design.md`, `rai_ethics_review_protocol.md`; "model risk assessment / register" → `rai_model_risk_assessment.md`, `rai_model_risk_register.md`; "red-team / PII exposure" → `rai_red_teaming_plan.md`, `rai_privacy_pii_assessment.md`; "sustainability & carbon" → `rai_sustainability_carbon_assessment.md`. **Regulatory** (anti-fabrication is load-bearing — these map a system to a framework's *structure*, the user confirms classification/version, and any article text, threshold, or citation is flagged "verify against the current official source"; not legal advice): EU AI Act → `rai_eu_ai_act_compliance_assessment.md`; NIST AI RMF → `rai_nist_ai_rmf_assessment.md`; FDA AI/ML SaMD → `rai_fda_samd_compliance_assessment.md`; fair-lending/ECOA → `rai_fair_lending_ecoa_assessment.md`; GDPR Art. 22 → `rai_gdpr_automated_decisioning_assessment.md`; SR 11-7 banking MRM → `rai_model_risk_management_sr1107.md`. **Privacy engineering:** "which privacy technique do we need?" → `rai_privacy_technique_selection.md`; "design differential privacy" → `rai_differential_privacy_design.md`; "govern federated learning" → `rai_federated_learning_governance.md`; "a deletion request must reach our models" → `rai_machine_unlearning_deletion.md`.
- **11. GenAI & LLM engineering** (`genai-llm-engineering/`, 30): "design a RAG system" → `genai_rag_system_design.md`; "RAG retrieves the wrong things" → `genai_rag_retrieval_quality_debug.md`, `genai_chunking_strategy.md`, `genai_embedding_model_selection.md`; "evaluate my RAG / LLM / judge" → `genai_rag_evaluation_harness.md`, `genai_llm_evaluation_design.md`, `genai_llm_as_judge_design.md`; "fine-tune, RAG, or prompt?" → `genai_finetune_vs_rag_vs_prompt_decision.md`, `genai_fine_tuning_workflow.md`, `genai_retrieval_augmented_finetuning.md`; "guardrails / injection defense" → `genai_guardrails_design.md`, `genai_prompt_injection_defense.md`; "trace my LLM app" → `genai_llm_observability_tracing.md`; "cut LLM cost and latency" → `genai_llm_cost_latency_optimization.md`; "structured output / function calls" → `genai_structured_output_function_calling.md`, `genai_structured_extraction_at_scale.md`; "context window / long context" → `genai_context_window_strategy.md`, `genai_long_context_strategy.md`; "multilingual" → `genai_multilingual_design.md`; "synthetic data with an LLM" → `genai_synthetic_data_with_llms.md`. **Retrieval depth:** "retrieval misses what a human would find" → `genai_query_rewriting_expansion.md`; "right passage retrieved but ranked low" → `genai_reranking_strategy.md`; "tune the ANN index" → `genai_vector_index_tuning.md`; "make answers verifiably traceable" → `genai_citation_grounding_attribution.md`; "facts linked across documents (GraphRAG)" → `genai_graphrag_knowledge_graph_design.md`; "design tools/an MCP server a model can use" → `genai_mcp_tool_interface_design.md`.
- **12. Specialized verticals** (`specialized-ml/`, 50 across seven): **CV** (10) — "frame a CV task / annotate / augment" → `computer-vision/cv_task_framing.md`, `cv_annotation_strategy.md`, `cv_augmentation_strategy.md`; "detection / segmentation" → `cv_object_detection_eval.md`, `cv_segmentation_approach.md`; "pick a pretrained backbone" → `cv_transfer_learning_pretrained_selection.md`; "video / 3D point cloud / OCR / medical imaging" → `cv_video_understanding_design.md`, `cv_3d_point_cloud_design.md`, `cv_ocr_pipeline_design.md`, `cv_medical_imaging_considerations.md`. **Classical NLP** (6, non-LLM text) — "frame a non-LLM text task" → `nlp-classical/nlp_task_framing.md`; "text classification / NER / topic modeling without an LLM" → `nlp-classical/nlp_text_classification_design.md`, `nlp_ner_extraction_design.md`, `nlp_topic_modeling_approach.md`; "tokenization / preprocessing" → `nlp_tokenization_representation_strategy.md`, `nlp_text_preprocessing_pipeline.md`. **Recsys** (9) — `recommender-systems/recsys_architecture_design.md`, `recsys_cold_start_strategy.md`, `recsys_candidate_ranking_design.md`, `recsys_offline_evaluation.md`, `recsys_feedback_loop_bias_audit.md`, `recsys_objective_business_alignment.md`, `recsys_sequential_session_based_design.md`, `recsys_multi_objective_ranking.md`, `recsys_bandits_exploration.md`. **Time-series** (9) — `time-series/ts_forecasting_model_selection.md`, `ts_backtesting_design.md`, `ts_feature_engineering.md`, `ts_data_leakage_audit.md`, `ts_seasonality_decomposition.md`, `ts_anomaly_detection_design.md`, `ts_hierarchical_forecasting.md`, `ts_probabilistic_forecasting.md`, `ts_intermittent_demand_forecasting.md`. **RL** (8) — `reinforcement-learning/rl_problem_framing.md`, `rl_reward_function_design.md`, `rl_environment_design.md`, `rl_algorithm_selection.md`, `rl_evaluation_safety.md`, `rl_offline_rl_design.md`, `rl_rlhf_rlaif_pipeline_design.md`, `rl_multi_agent_rl_design.md`. **Graph ML** (4) — "frame a graph-ML task" → `graph-ml/graphml_task_framing.md`; then `graphml_link_prediction_design.md`, `graphml_fraud_graph_patterns.md`, `graphml_gnn_scalability.md`. **Other modalities** (4) — `other-modalities/mlmodal_multimodal_architecture.md`, `mlmodal_speech_asr_tts_framing.md`, `mlmodal_anomaly_outlier_detection.md`, and non-speech audio (sound events, machine and wildlife acoustics) → `mlmodal_audio_ml_design.md`.
- **13. Secure the model** (`model-security/`, 10 — **new in Wave 9**): security in this domain is deep on both sides — `model-security/` covers the model itself, `agentic-ai-systems/` covers the agent around it, and application-layer security stays in `domain-software-engineering/analysis/security/`. "Threat-model our deployed model" (**start here**) → `mlsec_ml_threat_model.md`; "can our model be fooled by crafted inputs?" → `mlsec_adversarial_robustness_assessment.md` then `mlsec_adversarial_defense_strategy.md`; "could our training data be poisoned or backdoored?" → `mlsec_data_poisoning_backdoor_defense.md`; "can someone steal the model through the API?" → `mlsec_model_extraction_defense.md`; "does the model reveal who was in its training set?" → `mlsec_membership_inference_defense.md`; "does it regurgitate training data?" → `mlsec_model_inversion_leakage_audit.md`; "where did these weights and datasets come from?" → `mlsec_ml_supply_chain_audit.md`; "prove a model or its output is ours" → `mlsec_model_watermarking_provenance.md`; "harden the inference endpoint" → `mlsec_secure_inference_endpoint_design.md`.
- **14. Lead — AI product & leadership** (`ai-product-leadership/`, 12): "which use cases first?" → `aipm_use_case_prioritization.md`, `aipm_ml_project_scoping.md`; "ROI case / exec risk brief" → `aipm_roi_business_case.md`, `aipm_model_risk_brief_for_execs.md`; "build, buy, or partner / which vendor?" → `aipm_build_buy_partner_decision.md`, `aipm_vendor_model_selection.md`; "structure and hire the ML team" → `aipm_ml_team_structure_hiring.md`; "AI roadmap / AI policy" → `aipm_ai_roadmap_design.md`, `aipm_ai_policy_authoring.md`; "translate the jargon" → `aipm_jargon_translator_for_stakeholders.md`; "our ML project failed" → `aipm_failed_ml_project_postmortem.md`; "MLOps maturity for leaders" → `aipm_mlops_maturity_for_leaders.md`.
- **15. Learn** (`learning-ai-ml/`, 29): "explain this ML concept / the math" → `mllearn_concept_explainer.md`, `mllearn_math_for_ml_explainer.md`, `mllearn_glossary_builder.md`; "I don't actually understand this" → `mllearn_understanding_debugger.md`; "read / digest this paper" → `mllearn_paper_reading_guide.md`, `mllearn_paper_digest_generator.md`; "plan how I learn ML" → `mllearn_study_path_designer.md`; "prep for an ML interview" → `mllearn_ml_interview_prep.md`, `mllearn_ml_system_design_interview.md`; "portfolio project / Kaggle" → `mllearn_portfolio_project_designer.md`, `mllearn_kaggle_competition_strategy.md`. "plan my own paper reproduction" → `domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md`. Four sequenced series: **study tracks** (`study-tracks/`) — `mllearn_study_track_computer_vision.md`, `mllearn_study_track_nlp_llm.md`, `mllearn_study_track_reinforcement_learning.md`, `mllearn_study_track_mlops.md`; **paper reproductions** (`paper-reproductions/`, strict no-fabrication convention — every paper-specific value is an `[extract from paper]` placeholder, see its `README.md`) — `mllearn_reproduce_resnet_image_classifier.md`, `mllearn_reproduce_transformer_attention.md`, `mllearn_reproduce_word2vec_embeddings.md`, `mllearn_reproduce_dqn_atari.md`; **interview bank** (`interview-bank/`) — `mllearn_interview_bank_recommendation_ranking.md`, `mllearn_interview_bank_search_systems.md`, `mllearn_interview_bank_nlp_llm_applications.md`, `mllearn_interview_bank_realtime_fraud_detection.md`, `mllearn_interview_scoring_rubric.md`; **notebook → production** (`notebook-to-production/`) — `mllearn_n2p_01_refactor_notebook_to_package.md` → `mllearn_n2p_02_reproducible_training_pipeline.md` → `mllearn_n2p_03_package_and_serve_model.md` → `mllearn_n2p_04_deploy_monitor_cicd.md`.

#### Platform-specific playbooks (route to the platform-neutral sibling first when the user hasn't picked a tool)

13 named-stack walkthroughs, version-neutral *inside* the named stack — API/pricing/quota facts are flagged "verify against current docs," never asserted.
  - **Experiment tracking:** MLflow → `mlops-infrastructure/mlops_mlflow_experiment_tracking_playbook.md`; Weights & Biases → `mlops_wandb_experiment_tracking_playbook.md`.
  - **Cloud training & deployment:** SageMaker → `mlops-infrastructure/mlops_sagemaker_deployment_playbook.md`; Vertex AI → `mlops_vertex_ai_deployment_playbook.md`; Databricks → `mlops_databricks_mlops_playbook.md`.
  - **Data versioning:** DVC → `data-for-ml/mldata_dvc_data_versioning_playbook.md`; lakeFS → `mldata_lakefs_data_versioning_playbook.md`.
  - **Feature stores:** Feast → `feature-engineering/mlfeature_feast_feature_store_playbook.md`; Tecton → `mlfeature_tecton_feature_store_playbook.md`.
  - **Vector databases** (cross-link `domain-software-engineering/devops/`): pgvector → `genai-llm-engineering/genai_pgvector_vector_db_playbook.md`; Pinecone → `genai_pinecone_vector_db_playbook.md`; Weaviate → `genai_weaviate_vector_db_playbook.md`; Milvus → `genai_milvus_vector_db_playbook.md`.

### Building Autonomous Agentic Systems (`domain-AI-ML/agentic-ai-systems/`, 42)

The domain's largest subdirectory, organized as a **build pipeline** — see [README](../domain-AI-ML/agentic-ai-systems/README.md) for sequencing. It owns the *AI/ML-engineering design decision* framing and cross-links — rather than duplicates — the prompt-level control-flow templates (`domain-prompt-engineering/agent-workflows/`, `tool-use/`), the multi-agent contract templates (`domain-agentic-resources/commands/multi-agent/`), and the single-agent lifecycle patterns (`domain-engineering-workflows/ai-patterns/`).

  - **Gate 0 — Justify the agent (before any design):** "does this need an agent at all vs a deterministic workflow?" → `aiagent_complexity_ladder_gate.md` (walk the use case down function → direct call → workflow → agent → multi-agent; stop at the lowest rung that works).
  - **Design the agent (foundations):** architecture (`aiagent_architecture_design.md`), tools (`aiagent_tool_design.md`), memory (`aiagent_memory_design.md`), per-task cost/budget (`aiagent_cost_token_budget_design.md`), evaluation (`aiagent_evaluation_design.md`), agentic safety/eval layer (ABC validity + OpenAgentSafety real-tool eval as a separate gate) (`aiagent_agentic_safety_eval_layer.md`), failure modes (`aiagent_failure_mode_analysis.md`), human-in-the-loop (`aiagent_human_in_the_loop_design.md`), safety/sandboxing (`aiagent_safety_sandboxing.md`).
  - **Coordinate a fleet:** "whether to split to multi-agent" → `aiagent_multi_agent_orchestration.md`; "design the planner / decomposition" → `aiagent_planning_decomposition_design.md`; "pick the coordination topology" → `aiagent_orchestration_topology_selection.md`; "design the inter-agent message protocol" → `aiagent_inter_agent_communication_protocol.md`; "route work across an agent pool" → `aiagent_task_routing_load_balancing.md`; "emit a guided/manual/surgical master orchestrator for a multi-stage system" → `aiagent_orchestrator_generator.md`.
  - **Run it durably:** "observe/trace in production" → `aiagent_observability_telemetry_design.md`; "survive crashes / long runs" → `aiagent_durable_execution_state_persistence.md`; "set up a long-running task" → `aiagent_long_running_task_setup.md`; "deploy & roll out safely" → `aiagent_deployment_serving_architecture.md`; "manage the context window at scale" → `aiagent_context_engineering_at_scale.md`.
  - **Survive across sessions (continuity & recovery):** "give it memory that outlives the session" → `aiagent_project_continuity_memory_design.md`; "what should it write down?" → `aiagent_project_memory_capture_protocol.md`; "re-check memory before acting on it" → `aiagent_project_memory_guard_before_action.md`; "share memory across tools" → `aiagent_project_memory_interop_adapter_design.md`; "audit memory decay and poisoning" → `aiagent_project_memory_security_decay_audit.md`; "a long task failed partway" → `aiagent_failure_recovery_rescope.md`; "hand off between agents" → `aiagent_cross_agent_handoff_recovery.md`.
  - **Secure it:** "threat-model the agent" → `aiagent_agentic_threat_model.md`; "define trust boundaries" → `aiagent_trust_boundary_design.md`; "scope its agency to the minimum" → `aiagent_least_agency_scoping.md`; "zero-trust maturity" → `aiagent_zero_trust_maturity_assessment.md`; "supply chain / AIBOM" → `aiagent_supply_chain_aibom.md`; "runtime guardrail/policy layer" → `aiagent_runtime_guardrails_policy.md`; "compose security/eval/governance into enforced Gate A/B/C + kill switch (code-not-trust)" → `aiagent_hard_gates_designer.md`; "prompt-injection / untrusted-content defense" → `aiagent_prompt_injection_untrusted_content_defense.md`; "memory poisoning defense" → `aiagent_memory_poisoning_defense.md`; "SecOps for an autonomous defender" → `aiagent_secops_autonomous_defense.md`; "agent privacy & data governance" → `aiagent_privacy_data_governance.md`.
  - **Improve it:** "pre-deployment simulation/testing" → `aiagent_simulation_staging_testing.md`; "self-improvement / online adaptation" → `aiagent_self_improvement_online_adaptation.md`; "fleet cost attribution & optimization" → `aiagent_fleet_cost_attribution_optimization.md`.
  - **Author a whole agentic system (meta-layer):** to *design* a production-ready agentic system from a use case (not just one decision), use the authoring system → `authoring/system-patterns/` (6-step process, 9-topology pattern index, 100-pt rubric, gate/eval/architecture templates), or run the guided factory → `agentic-system-factory/`. Both reference (never duplicate) these `aiagent_*` design prompts.

---

## Workflows for Common Scenarios

### Scenario 1: User Asks for Help with a Task

**Example:** "Help me find security vulnerabilities in my code"

```
1. Recognize: This is a TASK request, not a "new prompt" request
2. Map to category: Security → `domain-software-engineering/analysis/security/`
3. Browse directory and find: `security_vulnerability_analysis.md`
4. Read the prompt file
5. Execute the prompt against user's codebase
6. Customize findings for their specific context
```

### Scenario 2: User Asks for a New Prompt

**Example:** "Create a new prompt for reviewing database migrations"

```
1. Recognize: User explicitly wants a NEW prompt
2. Open AI_AGENT_QUICK_START.md
3. Follow 5-step process:
   - Step 1: Classify intent (ANALYZE)
   - Step 2: Select techniques (ST-01, ST-02, RT-02, RT-05, DS-02)
   - Step 3: Build structure using templates
   - Step 4: Add quality layers
   - Step 5: Customize and deliver
4. Build prompt from scratch
5. Provide complete prompt to user
```

### Scenario 3: User Request Maps to Multiple Prompts

**Example:** "Analyze my code for security AND performance issues"

```
1. Recognize: Multi-faceted request
2. Map to multiple categories:
   - Security → `domain-software-engineering/analysis/security/security_vulnerability_analysis.md`
   - Performance → `domain-software-engineering/analysis/performance/performance_bottleneck_identification.md`
3. Execute both prompts sequentially
4. Synthesize findings into single report
```

### Scenario 4: User Wants to Learn About Prompting

**Example:** "How do I write better prompts for code analysis?"

```
1. Recognize: Educational request about prompting
2. Reference appropriate guides:
   - Quick patterns: AI_AGENT_QUICK_START.md
   - Detailed techniques: techniques/MASTER_TECHNIQUE_INDEX.md
   - Examples: Browse relevant domain (domain-software-engineering/analysis/)
3. Explain with examples from repository
```

### Scenario 5: User Wants to Create a Skill

**Example:** "Create a skill for validating Kubernetes manifests"

```
1. Recognize: User wants a SKILL (reusable, modular capability)
2. Open authoring/skill-patterns/README.md
3. Follow skill creation process:
   - Step 1: Classify type (WORKFLOW for K8s validation)
   - Step 2: Determine structure (numbered steps with validation)
   - Step 3: Build SKILL.md (metadata + instructions)
   - Step 4: Add resources (scripts/, references/, assets/)
   - Step 5: Validate with quality rubric
4. Use patterns from SKILL_PATTERN_INDEX.md
5. Deliver complete skill directory structure
```

### Scenario 6: User Request Maps to Existing Skill

**Example:** "Help me set up Helm charts for my application"

```
1. Recognize: This matches an existing skill
2. Search domain-agentic-resources/skills/ for helm
3. Find: helm-chart-scaffolding skill
4. Load the skill's SKILL.md
5. Execute skill instructions against user's context
6. Reference skill's bundled resources as needed
```

---

## Quick Reference: Task → Resource Mapping

| User Says | First Check |
|-----------|-------------|
| "Find bugs/issues" | `domain-software-engineering/analysis/quality/` |
| "Security review" | `domain-software-engineering/analysis/security/` |
| **Bug bounty hunting (offensive, AUTHORIZED)** | **`domain-software-engineering/bug-bounty/` — see [README](../domain-software-engineering/bug-bounty/README.md). Every prompt has an authorization/scope gate.** |
| "New to bug bounties / first 90 days" | `domain-software-engineering/bug-bounty/bugbounty_getting_started_orientation.md` |
| "Read a program's scope into a test plan" | `domain-software-engineering/bug-bounty/bugbounty_program_scope_analyzer.md` |
| "Map a target's attack surface (recon)" | `domain-software-engineering/bug-bounty/bugbounty_recon_attack_surface_map.md` |
| "Hunt IDOR / broken access control" | `domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md` |
| "Hunt SSRF / injection / XSS / business logic" | `domain-software-engineering/bug-bounty/bugbounty_ssrf_hunt.md` (+ injection/xss/business_logic hunt prompts) |
| "Test a REST/GraphQL API or mobile app" | `domain-software-engineering/bug-bounty/bugbounty_api_graphql_hunt.md` / `bugbounty_mobile_app_hunt.md` |
| "Validate a finding / score CVSS / build PoC" | `domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md` (+ severity, poc) |
| "Write a vulnerability disclosure report" | `domain-software-engineering/bug-bounty/bugbounty_disclosure_report_writer.md` |
| "Performance problems" | `domain-software-engineering/analysis/performance/` |
| "Architecture review" | `domain-software-engineering/analysis/architecture/` |
| "Generate tests" | `domain-software-engineering/testing/` |
| "Review infrastructure" | `domain-software-engineering/devops/` |
| "Cloud optimization" | `domain-software-engineering/cloud/` |
| "API design help" | `domain-software-engineering/api/` |
| "Mobile app review" | `domain-software-engineering/mobile/` |
| "Vibe-coded project stuck / walled" | `domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md` |
| "Build a rules file / CLAUDE.md for this codebase" | `domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md` |
| "Decompose a stuck AI coding task" | `domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md` |
| "Security audit of AI-generated code" | `domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md` |
| "Handoff briefing for a new engineer" | `domain-software-engineering/vibe-coding-rescue/viberescue_engineer_handoff_briefing.md` |
| **Android Vibe-Rescue (vibe-coded Android app)** | **Use `domain-software-engineering/vibe-coding-rescue/android/` — see [README](../domain-software-engineering/vibe-coding-rescue/android/README.md). Run prompts in sequence.** |
| "Diagnose my vibe-coded Android app" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_wall_diagnosis.md` |
| "Audit my Android codebase for fragility / AI patterns" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md` |
| "Android security & privacy audit (manifest, WebView, deeplinks, auth, secrets)" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md` |
| "Rank Android audit findings into a fix queue" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_prioritization.md` |
| "Safely execute one Android fix (test-first, one-per-commit, rollback)" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_executor.md` |
| "Generate a CLAUDE.md / rules file for my Android app from audit evidence" | `domain-software-engineering/vibe-coding-rescue/android/android_viberescue_rules_file.md` |
| "Ambient AI code-review system" | `domain-engineering-workflows/ai-native-rollouts/airollout_ambient_code_review.md` |
| "Tiered AI adoption rollout" | `domain-engineering-workflows/ai-native-rollouts/airollout_tiered_adoption_rollout.md` |
| "Ship a real PR without writing code" | `domain-engineering-workflows/ai-native-rollouts/airollout_ship_without_writing_code.md` |
| "Delegate to AI like a parallel coworker" | `domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md` |
| "Long-running project memory" | `domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md` |
| "Migrate an org bottleneck from humans to AI" | `domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md` |
| "Surface my values from past decisions / stated vs revealed" | `domain-personal-development/prompts/identity/identity_values_clarification.md` |
| "Audit my self-talk / inner critic" | `domain-personal-development/prompts/identity/identity_self_talk_audit.md` |
| "Diagnose what my envy / comparison is pointing at" | `domain-personal-development/prompts/identity/identity_comparison_envy_diagnostic.md` |
| "Calibrate my confidence (impostor or overconfidence)" | `domain-personal-development/prompts/identity/identity_confidence_calibration.md` |
| "Diagnose loss of purpose / 'why'" | `domain-personal-development/prompts/identity/identity_purpose_reignition.md` |
| "Life audit at a major inflection / midlife reckoning" | `domain-personal-development/prompts/identity/identity_life_audit_reckoning.md` |
| "Develop taste / discernment in a specific domain" | `domain-personal-development/prompts/identity/identity_taste_development.md` |
| "Diagnose stage of burnout and choose recovery path" | `domain-personal-development/prompts/agency/agency_burnout_recovery.md` |
| "Post-decision regret analysis (was I right to choose that?)" | `domain-personal-development/prompts/agency/agency_decision_post_mortem.md` |
| "Reconcile last week's plan vs what actually happened" | `domain-productivity/reviews/reviews_time_audit_evidence_based.md` |
| "Weekly systems review (capture / calendar / blocks / backlog)" | `domain-productivity/reviews/reviews_weekly_systems_review.md` |
| "Monthly or quarterly cadence review of productivity systems" | `domain-productivity/reviews/reviews_monthly_quarterly_cadence.md` |
| "Diagnose procrastination on a specific task (systems-level)" | `domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md` |
| "Design a personal capture-and-triage system" | `domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md` |
| "Set a ship threshold / stop polishing an artifact" | `domain-productivity/bottlenecks/bottleneck_perfectionism_ship_threshold.md` |
| "Design a personal knowledge / second-brain system" | `domain-productivity/bottlenecks/bottleneck_pkm_second_brain_architecture.md` |
| "Engineer defaults and friction in my workspace" | `domain-productivity/deep-work/deepwork_environment_friction_design.md` |
| "Write a handoff to my future self (overnight / weekly / vacation)" | `domain-productivity/deep-work/deepwork_future_self_handoff.md` |
| "Audit my work week against coordination-tax" | `domain-personal-development/career-transformation/career_coordination_tax_audit.md` |
| "Assess my role's structural vulnerability" | `domain-personal-development/career-transformation/career_role_structural_vulnerability.md` |
| "Inventory my residual skills (judgment / taste / context)" | `domain-personal-development/career-transformation/career_residual_skills_inventory.md` |
| "Build a 90-day repositioning plan" | `domain-personal-development/career-transformation/career_90_day_repositioning_plan.md` |
| **Habits & behavior change** | **`domain-personal-development/prompts/habits/` — see README** |
| "Design a new habit (cue/routine/reward)" | `domain-personal-development/prompts/habits/habits_habit_design_blueprint.md` |
| "Break a bad habit" | `domain-personal-development/prompts/habits/habits_break_bad_habit_protocol.md` |
| "Stack a habit onto an existing routine" | `domain-personal-development/prompts/habits/habits_habit_stacking_designer.md` |
| "Recover after breaking a streak" | `domain-personal-development/prompts/habits/habits_streak_recovery_plan.md` |
| "Find the keystone habit that cascades" | `domain-personal-development/prompts/habits/habits_keystone_habit_identifier.md` |
| "Engineer my environment for a habit" | `domain-personal-development/prompts/habits/habits_environment_design_for_habits.md` |
| **Resilience & motivation (non-clinical)** | **`domain-personal-development/prompts/resilience/` — see README** |
| "Recover from a setback / failure" | `domain-personal-development/prompts/resilience/resilience_setback_recovery_framework.md` |
| "Diagnose what's killing my motivation" | `domain-personal-development/prompts/resilience/resilience_motivation_diagnosis.md` |
| "Build self-discipline without willpower" | `domain-personal-development/prompts/resilience/resilience_self_discipline_system.md` |
| "Reframe a failure (extract the lesson)" | `domain-personal-development/prompts/resilience/resilience_failure_reframe.md` |
| "Audit where I'm fragile vs antifragile" | `domain-personal-development/prompts/resilience/resilience_anti_fragility_audit.md` |
| "Rebuild momentum after a long stall" | `domain-personal-development/prompts/resilience/resilience_momentum_rebuild.md` |
| **Relationships & social (personal, non-clinical)** | **`domain-personal-development/prompts/relationships/` — see README** |
| "Set a boundary (script it)" | `domain-personal-development/prompts/relationships/relationships_boundary_setting_script.md` |
| "Prep a hard personal conversation" | `domain-personal-development/prompts/relationships/relationships_hard_conversation_prep.md` |
| "Cultivate / maintain personal relationships" | `domain-personal-development/prompts/relationships/relationships_network_cultivation_plan.md` |
| "Develop a specific social skill" | `domain-personal-development/prompts/relationships/relationships_social_skill_development.md` |
| "Repair a relationship after a rupture" | `domain-personal-development/prompts/relationships/relationships_conflict_repair_guide.md` |
| "Audit the health of a relationship" | `domain-personal-development/prompts/relationships/relationships_relationship_audit.md` |
| **AI-role career assessments** | **`domain-personal-development/prompts/career/` — 17 interactive role assessments; see README** |
| "Goals / habits / thinking / productivity / solo-dev / stakeholder tools" | `domain-personal-development/prompts/{goals,habits,thinking,productivity,solo-dev,stakeholder}/` — see each subdir README |
| **Life transitions (living through a change already underway — NOT deciding it)** | **`domain-personal-development/prompts/life-transitions/` — see README. Deciding whether to make the change → `major-decisions/`; clinical grief/depression/trauma → `domain-psychology/`** |
| "Just started a new job / promotion (first 90 days)" | `domain-personal-development/prompts/life-transitions/lifetransition_navigating_new_role.md` |
| "Adjusting after a move / relocation already made" | `domain-personal-development/prompts/life-transitions/lifetransition_relocation_adjustment.md` |
| "New parenthood identity / empty nest / retirement reorientation" | `domain-personal-development/prompts/life-transitions/lifetransition_{new_parenthood_identity,empty_nest_reorientation,retirement_purpose_redesign}.md` |
| "Recover after job loss / breakup / return from leave" | `domain-personal-development/prompts/life-transitions/lifetransition_{job_loss_recovery_plan,post_breakup_rebuild,returning_from_leave}.md` |
| "Who am I now / general transition map (ending→neutral zone→new beginning)" | `domain-personal-development/prompts/life-transitions/lifetransition_{identity_after_major_change,transition_map_and_timeline}.md` |
| **Everyday NON-CLINICAL emotional skills** | **`domain-personal-development/prompts/emotional-fitness/` — see README. In/considering therapy, in distress, safety concern → `domain-psychology/client-self-use/` + professional help** |
| "Name a vague feeling / process disappointment / channel jealousy" | `domain-personal-development/prompts/emotional-fitness/emotionalfitness_{emotion_labeling_practice,disappointment_processing,jealousy_channeling}.md` |
| "Sort worry vs action / audit what sets me off / hold two opposed feelings" | `domain-personal-development/prompts/emotional-fitness/emotionalfitness_{worry_vs_action_sorter,reactivity_trigger_audit,ambivalence_holding_two_feelings}.md` |
| "Self-compassion reset / cooldown ritual / shame vs guilt / debrief a charged event" | `domain-personal-development/prompts/emotional-fitness/emotionalfitness_{self_compassion_reset,emotional_reset_ritual,shame_vs_guilt_sorter,charged_event_debrief}.md` |
| "Marriage/commitment, aging-parent care, sabbatical, start-business-vs-employment decision" | `domain-personal-development/major-decisions/personal_{marriage_commitment_decision,caring_for_aging_parent,sabbatical_career_break,start_business_vs_employment}.md` |
| "AI-era skill moat / positioning statement / internal-vs-external move / reskilling roadmap" | `domain-personal-development/career-transformation/career_{ai_era_skill_moat,positioning_statement,internal_vs_external_move,reskilling_roadmap}.md` |
| "Map a capability's frontier" | `domain-presentations/visual-planning/visualplan_capability_frontier_map.md` |
| "QA harness for visual work" | `domain-presentations/visual-planning/visualplan_visual_qa_harness.md` |
| "Route a task to the right visual modality" | `domain-presentations/visual-planning/visualplan_modality_router.md` |
| "Scan for cascade effects from a capability" | `domain-presentations/visual-planning/visualplan_cascade_effects_scan.md` |
| "React review/patterns / RSC / streaming" | `domain-frontend-development/react/` |
| "Vue review/patterns / advanced reactivity" | `domain-frontend-development/vue/` |
| "Angular architecture / signals" | `domain-frontend-development/angular/` |
| "Next.js App Router / Server Actions" | `domain-frontend-development/nextjs/` |
| "Svelte / SvelteKit" | `domain-frontend-development/svelte/` |
| "Astro / SolidJS / Qwik / Remix" | `domain-frontend-development/{astro,solidjs,qwik,remix}/` |
| "CSS architecture / Tailwind / CSS-in-JS" | `domain-frontend-development/styling/` |
| "TypeScript component typing / type-safety audit" | `domain-frontend-development/typescript/` |
| "Form validation / accessible form UX" | `domain-frontend-development/forms/` |
| "Animation / motion performance" | `domain-frontend-development/animation/` |
| "Error boundaries / state-mgmt selection / i18n" | `domain-frontend-development/architecture/` |
| "Vite / micro-frontends / bundler migration" | `domain-frontend-development/build-tooling/` |
| "Accessibility audit" | `domain-frontend-development/accessibility/` |
| "Core Web Vitals / bundle size" | `domain-frontend-development/performance/` |
| "Frontend testing (Jest / Playwright)" | `domain-frontend-development/testing/` |
| "Game design/GDD" | `domain-game-development/design/` |
| "Game architecture" | `domain-game-development/architecture/` |
| "Unreal Engine review" | `domain-game-development/engines/` |
| "Unity review" | `domain-game-development/engines/` |
| "Godot review" | `domain-game-development/engines/` |
| "Game testing/QA" | `domain-game-development/testing/` |
| "Multiplayer/netcode" | `domain-game-development/multiplayer/` |
| "Game performance" | `domain-game-development/performance/` |
| "Shader review" | `domain-game-development/graphics/` |
| "Game audio" | `domain-game-development/audio/` |
| "Procedural generation" | `domain-game-development/level-design/` |
| "Game economy" | `domain-game-development/economy/` |
| "Teach me this" | `domain-learning-coding/` |
| "Plan project/sprint" | `domain-engineering-workflows/workflows/` |
| "Business analysis of a codebase" | `domain-software-engineering/analysis/business/` |
| "Company strategy / positioning / go-to-market" | `domain-business-strategy/` |
| "Create PRD" | `domain-product-management/prompts/` |
| "Make decision" | `domain-decision-making/` |
| "Multi-agent pipeline" | `domain-agentic-resources/personas/` |
| **Idea-to-Product Pipeline (idea → shippable software, AI-agent build)** | **Use `domain-idea-to-product/` — see [`README`](../domain-idea-to-product/README.md). Start with `orchestrator_idea_to_product.md` for guided mode.** |
| "Take my idea and turn it into a product (full pipeline)" | `domain-idea-to-product/orchestrator_idea_to_product.md` |
| "Stress-test a raw software idea before validation" | `domain-idea-to-product/stage-1-ideation/ideation_concept_legs_test.md` |
| "Structured customer-discovery interview protocol (JTBD + Mom Test)" | `domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md` |
| "Build a unit-economics model (LTV/CAC/payback/cohort)" | `domain-idea-to-product/stage-3-market-research/market_unit_economics_designer.md` |
| "Orchestrated 90-day GTM plan with first-100 playbook" | `domain-idea-to-product/stage-5-strategy-positioning/strategy_gtm_orchestrated_plan.md` |
| "Decompose a PRD into epic / feature / story with MVP/V1/V2 cuts" | `domain-idea-to-product/stage-7-prd-authoring/prd_to_epic_feature_decomposer.md` |
| "Pick a tech stack with AI-coding-agent friendliness scored" | `domain-idea-to-product/stage-8-architecture-design/architecture_tech_stack_selector.md` |
| "Bridge PRD → AI-agent day-1 file bundle (CLAUDE.md skeleton, task list, work-loop)" | `domain-idea-to-product/stage-10-ai-agent-handoff/prd_to_agent_brief_bridge.md` |
| "Write per-task acceptance spec for an AI-agent-delegated task" | `domain-idea-to-product/stage-10-ai-agent-handoff/agent_task_acceptance_test_writer.md` |
| **Children's Book Studio (idea → finished, publishable children's book + submission package)** | **Use `childrens-book-studio/` — see [README](../childrens-book-studio/README.md). Start with `orchestrator_childrens_book.md` or `/write-childrens-book` for guided mode.** |
| "Write me a finished children's book from an idea" | `childrens-book-studio/orchestrator_childrens_book.md` (or `/write-childrens-book`) |
| "Revise my existing children's-book draft" | `childrens-book-studio/prompts/stage-4-revision-triage.md` (or `/revise-manuscript`) |
| "Retarget my kids' draft to an age / reading level" | `childrens-book-studio/commands/calibrate-reading-level.md` (or `/calibrate-reading-level`) |
| "Build a submission package for my finished kids' manuscript" | `childrens-book-studio/prompts/stage-6-publishing-package.md` (or `/build-submission-package`) |
| **Deep-Think (Multi-Perspective Analysis Systems)** | **Use `domain-deep-analysis/` — see README. Each scope has a rigorous version and a plain-English version (`*-plain`) for non-technical users; same rigor, different vocabulary.** |
| "Diagnose / understand a hard problem from many angles" | `domain-deep-analysis/deepthink_problem_analysis.md` (or `/deepthink-problem`) |
| "Same, but in plain English for a non-technical user" | `domain-deep-analysis/deepthink_problem_analysis_plain.md` (or `/deepthink-problem-plain`) |
| "Work through a hard decision with red team / steel-man / etc." | `domain-deep-analysis/deepthink_decision.md` (or `/deepthink-decision`) |
| "Same, but in plain English for a non-technical user" | `domain-deep-analysis/deepthink_decision_plain.md` (or `/deepthink-decision-plain`) |
| "Sequence a multi-month plan with tripwires + abort conditions" | `domain-deep-analysis/deepthink_plan.md` (or `/deepthink-plan`) |
| "Same, but in plain English for a non-technical user" | `domain-deep-analysis/deepthink_plan_plain.md` (or `/deepthink-plan-plain`) |
| "Design a system / feature / structure with documented tradeoffs" | `domain-deep-analysis/deepthink_design.md` (or `/deepthink-design`) |
| "Same, but in plain English for a non-technical user" | `domain-deep-analysis/deepthink_design_plain.md` (or `/deepthink-design-plain`) |
| **Reasoning Craft (domain-general reasoning tools, 41 prompts)** | **Use `domain-reasoning-craft/` — see [README](../domain-reasoning-craft/README.md)** |
| "Bayesian update / belief update" | `domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md` |
| "Reference class / base rate forecast with adjustments" | `domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md` |
| "Outside view vs inside view reconciliation" | `domain-reasoning-craft/reasoning-moves/reasoning_outside_view_inside_view.md` |
| "Fermi estimate / order of magnitude" | `domain-reasoning-craft/reasoning-moves/reasoning_fermi_estimation.md` |
| "Steelman the opposing position" | `domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md` |
| "Argument map / Toulmin" | `domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md` |
| "Audit claims vs evidence vs unstated warrants" | `domain-reasoning-craft/reasoning-moves/reasoning_claim_evidence_warrant_audit.md` |
| "Test the premises an argument stands on" | `domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md` |
| "Counterfactual / what if X had been different" | `domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md` |
| "First principles reconstruction" | `domain-reasoning-craft/reasoning-moves/reasoning_first_principles_reconstruction.md` |
| "Invert the problem (guarantee failure, then avoid it)" | `domain-reasoning-craft/reasoning-moves/reasoning_inversion.md` |
| "Best explanation for a surprising observation" | `domain-reasoning-craft/reasoning-moves/reasoning_abductive_inference.md` |
| "Predict by analogy to a known case" | `domain-reasoning-craft/reasoning-moves/reasoning_analogical_inference.md` |
| "Thesis vs antithesis → genuine synthesis" | `domain-reasoning-craft/reasoning-moves/reasoning_dialectical_synthesis.md` |
| "Turn a fuzzy claim into a resolvable forecast question" | `domain-reasoning-craft/forecasting/forecasting_probabilistic_question_design.md` |
| "Forecast decomposition / sub-questions" | `domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md` |
| "What's the base rate for this event class?" | `domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md` |
| "Assign probabilities to a scenario set" | `domain-reasoning-craft/forecasting/forecasting_scenario_probability_assignment.md` |
| "Does this news change my forecast? (signal vs noise)" | `domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md` |
| "Tripwires / what would change my mind" | `domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md` |
| "Score my past predictions / calibration audit" | `domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md` |
| "Design a forecasting log / Brier tracker" | `domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md` |
| "10–30 year forecast with no base rates" | `domain-reasoning-craft/forecasting/forecasting_long_horizon_radical_uncertainty.md` |
| "Find the feedback loops in this situation" | `domain-reasoning-craft/systems/systems_feedback_loop_identifier.md` |
| "Causal loop diagram" | `domain-reasoning-craft/systems/systems_causal_loop_diagram.md` |
| "Stocks, flows, and delays model" | `domain-reasoning-craft/systems/systems_stock_and_flow_model.md` |
| "Which system archetype is this? (tragedy of commons, shifting the burden...)" | `domain-reasoning-craft/systems/systems_archetype_recognition.md` |
| "Map dependencies / single points of failure" | `domain-reasoning-craft/systems/systems_dependency_map.md` |
| "Where's the leverage point? (Meadows)" | `domain-reasoning-craft/systems/systems_leverage_point_analysis.md` |
| "Unintended consequences / second-order effects" | `domain-reasoning-craft/systems/systems_unintended_consequence_scan.md` |
| "Pre-mortem a systems intervention" | `domain-reasoning-craft/systems/systems_intervention_pre_mortem.md` |
| "Bias audit (named bias)" | `domain-reasoning-craft/epistemic/epistemic_bias_specific_audit.md` |
| "Am I motivated-reasoning? (asymmetric standards test)" | `domain-reasoning-craft/epistemic/epistemic_motivated_reasoning_check.md` |
| "Evidence against my own position" | `domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md` |
| "Red-team my thesis/memo before shipping" | `domain-reasoning-craft/epistemic/epistemic_red_team_briefing.md` |
| "Scan this text for logical fallacies" | `domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md` |
| "Separate observations from claims from inferences" | `domain-reasoning-craft/epistemic/epistemic_claim_inference_separator.md` |
| "Which sources should I trust? (triangulation)" | `domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md` |
| "Score this study/evidence quality" | `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md` |
| "Is my draft overclaiming certainty?" | `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` |
| "Why are we stuck disagreeing? (facts/definitions/values/trust)" | `domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md` |
| **Ideation (divergent + convergent, 12 prompts)** | **Use `domain-ideation/` — see [README](../domain-ideation/README.md)** |
| "100 ideas / forced quantity" | `domain-ideation/ideation_forced_quantity_100_ideas.md` |
| "Crazy eights / rapid-fire ideas" | `domain-ideation/ideation_crazy_eights.md` |
| "SCAMPER" | `domain-ideation/ideation_scamper.md` |
| "Cross-domain analogy ideation" | `domain-ideation/ideation_cross_domain_analogy_mining.md` |
| "Inverse problem" | `domain-ideation/ideation_inverse_problem.md` |
| "Worst idea first" | `domain-ideation/ideation_worst_idea_first.md` |
| "Random stimulus" | `domain-ideation/ideation_random_stimulus.md` |
| "What would X do? (persona ideation)" | `domain-ideation/ideation_persona_what_would_x_do.md` |
| "Reframe ideas around jobs-to-be-done" | `domain-ideation/ideation_jobs_to_be_done_reframe.md` |
| "Flip the constraints to reopen idea space" | `domain-ideation/ideation_constraint_flip.md` |
| "Kill most of the idea list with reasons" | `domain-ideation/ideation_idea_kill_list.md` |
| "Narrow ideas to a shortlist / dot voting" | `domain-ideation/ideation_idea_convergence_dot_voting.md` |
| **Risk Management (7 prompts)** | **Use `domain-risk/` — see [README](../domain-risk/README.md)** |
| "Risk register" | `domain-risk/risk_register_builder.md` |
| "Risk heat map" | `domain-risk/risk_heat_map.md` |
| "FMEA" | `domain-risk/risk_fmea_analysis.md` |
| "Tail risk / black swan scan" | `domain-risk/risk_tail_risk_scan.md` |
| "Dependency chain audit (vendors, key people)" | `domain-risk/risk_dependency_chain_audit.md` |
| "Threat model (non-software)" | `domain-risk/risk_threat_model_non_technical.md` |
| "After-action review of a risk event" | `domain-risk/risk_after_action_review.md` |
| **Scenario planning & tradeoff analysis** | **Use `domain-decision-making/scenario_*.md` and `tradeoff_*.md`** |
| "2x2 scenario matrix" | `domain-decision-making/scenario_two_by_two_matrix.md` |
| "Backcasting from a future" | `domain-decision-making/scenario_backcasting.md` |
| "Strategy robustness across scenarios" | `domain-decision-making/scenario_robustness_test.md` |
| "Signposts / early-warning triggers" | `domain-decision-making/scenario_signposts_and_triggers.md` |
| "Strategic pre-mortem (3-year)" | `domain-decision-making/scenario_strategic_pre_mortem.md` |
| "Three-horizons roadmap" | `domain-decision-making/scenario_multi_horizon_roadmap.md` |
| "Wild card injection" | `domain-decision-making/scenario_wild_card_injection.md` |
| "MCDA / weighted scoring" | `domain-decision-making/tradeoff_multi_criteria_decision_analysis.md` |
| "Pugh matrix vs baseline" | `domain-decision-making/tradeoff_pugh_matrix.md` |
| "Real options framing" | `domain-decision-making/tradeoff_real_options_framing.md` |
| "Reversibility × stakes triage" | `domain-decision-making/tradeoff_reversibility_stakes_grid.md` |
| **Decision documentation** | **Use `domain-decision-making/documentation/` — see [README](../domain-decision-making/documentation/README.md)** |
| "Options memo / decision memo" | `domain-decision-making/documentation/decisiondoc_options_memo.md` |
| "One-page decision summary" | `domain-decision-making/documentation/decisiondoc_one_pager.md` |
| "Narrative six-pager (Bezos-style)" | `domain-decision-making/documentation/decisiondoc_narrative_memo_bezos.md` |
| "Decision log entry" | `domain-decision-making/documentation/decisiondoc_log_entry.md` |
| "Post-decision review" | `domain-decision-making/documentation/decisiondoc_post_decision_review.md` |
| "After-action report" | `domain-decision-making/documentation/decisiondoc_after_action_report.md` |
| **Major personal decisions (10 prompts)** | **Use `domain-personal-development/major-decisions/` — see [README](../domain-personal-development/major-decisions/README.md)** |
| "Evaluate a job offer" | `domain-personal-development/major-decisions/personal_career_offer_evaluation.md` |
| "Relocation decision" | `domain-personal-development/major-decisions/personal_relocation_decision.md` |
| "Quit or persist?" | `domain-personal-development/major-decisions/personal_quit_or_persist.md` |
| "Degree vs bootcamp vs certificate" | `domain-personal-development/major-decisions/personal_education_program_choice.md` |
| "Family planning tradeoffs" | `domain-personal-development/major-decisions/personal_family_planning_tradeoffs.md` |
| "Major financial decision framework" | `domain-personal-development/major-decisions/personal_financial_decision_framework.md` |
| "Research a health decision (non-emergency)" | `domain-personal-development/major-decisions/personal_health_decision_research.md` |
| "Major purchase research (house, vehicle)" | `domain-personal-development/major-decisions/personal_major_purchase_research.md` |
| "Vet a cofounder / business partner" | `domain-personal-development/major-decisions/personal_partnership_cofounder_selection.md` |
| "Difficult relationship audit" | `domain-personal-development/major-decisions/personal_difficult_relationship_audit.md` |
| **Research practice (15 prompts)** | **Use `domain-research-academic/`** |
| "Formulate research questions" | `domain-research-academic/research_question_formulation.md` |
| "Plan a literature review" | `domain-research-academic/research_literature_review_plan.md` |
| "Design a search strategy" | `domain-research-academic/research_search_strategy_designer.md` |
| "Systematic review protocol (PRISMA)" | `domain-research-academic/research_systematic_review_protocol.md` |
| "Meta-analysis scoping" | `domain-research-academic/research_meta_analysis_scoping.md` |
| "Evidence map for a claim" | `domain-research-academic/research_evidence_map.md` |
| "Triangulate a claim across source types" | `domain-research-academic/research_source_triangulation.md` |
| "Synthesize sources, preserving disagreement" | `domain-research-academic/research_secondary_source_synthesis.md` |
| "Will this finding replicate?" | `domain-research-academic/research_replication_audit.md` |
| "Generate competing hypotheses" | `domain-research-academic/research_hypothesis_generator.md` |
| "Map a research field" | `domain-research-academic/research_field_landscape_map.md` |
| "Interview guide design" | `domain-research-academic/research_interview_guide_designer.md` |
| "Qualitative coding scheme / codebook" | `domain-research-academic/research_qualitative_coding_scheme.md` |
| "Survey instrument design" | `domain-research-academic/research_survey_instrument_designer.md` |
| "Research memo from findings" | `domain-research-academic/research_research_memo_drafter.md` |
| "Policy options memo" | `domain-policy/policy_options_memo.md` |
| "Frame a policy problem (before options)" | `domain-policy/policy_problem_framing.md` |
| "Policy stakeholder / coalition map" | `domain-policy/policy_stakeholder_coalition_map.md` |
| "Policy implementation feasibility" | `domain-policy/policy_implementation_feasibility.md` |
| **Negotiation (46 prompts, 8 subdirs)** | **Use `domain-negotiation/` — see [README](../domain-negotiation/README.md). Start with `preparation/negotiation_prep_depth_triage.md`, which routes by prep tier.** |
| "How much prep does this negotiation even need?" | `domain-negotiation/preparation/negotiation_prep_depth_triage.md` |
| "BATNA / reservation point / ZOPA" | `domain-negotiation/preparation/negotiation_batna_analysis.md` |
| "My BATNA is weak so I have no leverage" | `domain-negotiation/preparation/negotiation_leverage_audit.md` |
| "Positions vs interests mapping" | `domain-negotiation/preparation/negotiation_interest_mapping.md` |
| "Design offers that create value (log-rolling, MESOs, contingent terms)" | `domain-negotiation/preparation/negotiation_package_trade_design.md` |
| "Should I go first, and where do I anchor?" | `domain-negotiation/preparation/negotiation_opening_offer_design.md` |
| "Plan my concessions (ladder, decay curve, reciprocity rule)" | `domain-negotiation/preparation/negotiation_concession_anchoring_plan.md` |
| "Model the counterpart's brief, constraints, and likely moves" | `domain-negotiation/preparation/negotiation_counterpart_simulation.md` |
| "What do I ask, and what do I refuse to answer?" | `domain-negotiation/preparation/negotiation_information_plan.md` |
| "Rehearse a negotiation conversation" | `domain-negotiation/preparation/negotiation_pre_meeting_rehearsal.md` |
| "Question sequence to surface interests live" | `domain-negotiation/at-the-table/negotiation_question_sequencing_live.md` |
| "Is their 'final offer' real? / test a claimed constraint" | `domain-negotiation/at-the-table/negotiation_reading_signals_and_bluffs.md` |
| "They're using pressure tactics (exploding offer, nibble, false deadline)" | `domain-negotiation/at-the-table/negotiation_hard_bargainer_defense.md` |
| "Nothing has moved in three rounds — break the impasse" | `domain-negotiation/at-the-table/negotiation_impasse_breaker.md` |
| "They keep saying they need approval / who actually decides?" | `domain-negotiation/at-the-table/negotiation_authority_mandate_limits.md` |
| "It got heated — de-escalate without conceding" | `domain-negotiation/at-the-table/negotiation_emotional_flooding_at_the_table.md` |
| "We're nearly there — what do I give to close?" | `domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md` |
| "Negotiate by email / async" | `domain-negotiation/channels/negotiation_written_async_message.md` |
| "Write a counter-offer message" | `domain-negotiation/channels/negotiation_counteroffer_email.md` |
| "Negotiating over video / remote" | `domain-negotiation/channels/negotiation_remote_video_channel.md` |
| "Cross-cultural negotiation (no stereotypes — asks rather than asserts)" | `domain-negotiation/channels/negotiation_cross_cultural.md` |
| "Three-plus parties: coalitions and concession sequencing" | `domain-negotiation/multi-party/negotiation_multi_party_alignment.md` |
| "Our side has three people — who says what?" | `domain-negotiation/multi-party/negotiation_team_negotiation_roles.md` |
| "They've aligned into a bloc against me" | `domain-negotiation/multi-party/negotiation_coalition_defense.md` |
| "Run a negotiation between two other parties (neutral role)" | `domain-negotiation/multi-party/negotiation_facilitator_third_party.md` |
| "Debrief a finished negotiation (process vs outcome quality)" | `domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md` |
| "We signed and nothing has happened since" | `domain-negotiation/after-the-deal/negotiation_implementation_and_relationship.md` |
| "Reopen terms on a live agreement" | `domain-negotiation/after-the-deal/negotiation_renegotiate_existing_agreement.md` |
| "No deal — preserve the option and execute the alternative" | `domain-negotiation/after-the-deal/negotiation_no_deal_recovery.md` |
| "Ask for a raise / 'there's no budget'" | `domain-negotiation/contexts/negotiation_salary_raise_promotion.md` |
| "Negotiate with a vendor as the buyer (no procurement team)" | `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md` |
| "Defend my freelance rate / raise rates on existing clients" | `domain-negotiation/contexts/negotiation_freelance_rate_conversation.md` |
| "Handle sales objections (price, timing, authority, competitor)" | `domain-negotiation/contexts/negotiation_sales_objection_handling.md` |
| "Agree a founder / partner equity split" | `domain-negotiation/contexts/negotiation_partnership_equity_split.md` |
| "Compete internally for budget or headcount" | `domain-negotiation/contexts/negotiation_internal_budget_headcount.md` |
| "Angry customer wants compensation — what do I concede?" | `domain-negotiation/contexts/negotiation_customer_escalation_concession.md` |
| "Buying a car / house against a professional seller" | `domain-negotiation/contexts/negotiation_major_purchase_bargaining.md` |
| "Prep a difficult conversation (firing / breakup / hard feedback)" | `domain-negotiation/difficult-conversations/difficultconvo_pre_brief.md` |
| "Debrief a difficult conversation" | `domain-negotiation/difficult-conversations/difficultconvo_post_review.md` |
| "Deliver bad news I didn't decide (layoff, cancellation, denial)" | `domain-negotiation/difficult-conversations/difficultconvo_delivering_bad_news.md` |
| "Take hard feedback without defending" | `domain-negotiation/difficult-conversations/difficultconvo_receiving_hard_feedback.md` |
| "Say no to my manager / a client with power over me" | `domain-negotiation/difficult-conversations/difficultconvo_saying_no_upward.md` |
| "Why do my negotiations keep landing the same way?" | `domain-negotiation/craft/negotiation_style_self_assessment.md` |
| "Practise negotiating when I only do it twice a year" | `domain-negotiation/craft/negotiation_deliberate_practice_loop.md` |
| "Turn my debriefs into a pattern library that compounds" | `domain-negotiation/craft/negotiation_pattern_library_builder.md` |
| "Where's the line between persuasion and manipulation?" | `domain-negotiation/craft/negotiation_ethics_line.md` |
| **Psy-ops / cognitive security (32 prompts, ANALYTIC & DEFENSIVE ONLY)** | **Use `domain-psy-ops/` — see [README](../domain-psy-ops/README.md). Output is always an assessment, a defense, or a resilience plan; never campaign material.** |
| "Is this a coordinated influence campaign?" | `domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md` |
| "Break this post/ad/speech into named propaganda techniques" | `domain-psy-ops/technique-analysis/psyops_propaganda_technique_identification.md` |
| "Why did this message make me feel that way?" | `domain-psy-ops/technique-analysis/psyops_emotional_manipulation_decoder.md` |
| "Is this deadline / scarcity real?" (dark patterns) | `domain-psy-ops/technique-analysis/psyops_persuasion_pressure_audit.md` |
| "What is this framing hiding?" | `domain-psy-ops/technique-analysis/psyops_framing_and_narrative_analysis.md` |
| "Motte-and-bailey / gish gallop / just-asking-questions" | `domain-psy-ops/technique-analysis/psyops_rhetorical_deception_scan.md` |
| "Where did this image or claim originate?" | `domain-psy-ops/technique-analysis/psyops_provenance_and_transmission_trace.md` |
| "Is this statistic or chart misleading?" | `domain-psy-ops/technique-analysis/psyops_statistical_and_visual_distortion_scan.md` |
| "Coordinated, or just people who agree?" | `domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md` |
| "Are these accounts bots?" | `domain-psy-ops/influence-operations/psyops_inauthentic_account_signal_assessment.md` |
| "Is this movement astroturf?" | `domain-psy-ops/influence-operations/psyops_astroturf_vs_organic_assessment.md` |
| "How did this unsourced claim become citable?" | `domain-psy-ops/influence-operations/psyops_information_laundering_chain_map.md` |
| "Who is behind this, and how sure can we be?" | `domain-psy-ops/influence-operations/psyops_attribution_confidence_assessment.md` |
| "Is what I'm experiencing manipulation?" | `domain-psy-ops/personal-defense/psyops_manipulation_recognition_personal.md` |
| "Coercive control / does my situation even count?" | `domain-psy-ops/personal-defense/psyops_coercive_control_pattern_recognition.md` |
| "Is this group high-control?" (structure, never beliefs) | `domain-psy-ops/personal-defense/psyops_high_control_group_dynamics_assessment.md` |
| "Is this call, email, or message a scam?" | `domain-psy-ops/personal-defense/psyops_social_engineering_pretext_recognition.md` |
| "What's actually shaping what I believe?" | `domain-psy-ops/personal-defense/psyops_information_diet_audit.md` |
| "Personal rules that hold under pressure" | `domain-psy-ops/personal-defense/psyops_cognitive_security_hygiene_plan.md` |
| "I think someone I love is being radicalized" | `domain-psy-ops/personal-defense/psyops_concern_for_someone_radicalizing.md` |
| "Who would run an influence attack on us?" | `domain-psy-ops/organizational-red-team/psyops_org_influence_threat_model.md` |
| "Which true things about us are exploitable?" | `domain-psy-ops/organizational-red-team/psyops_narrative_vulnerability_assessment.md` |
| "How exposed are our executives / key staff?" | `domain-psy-ops/organizational-red-team/psyops_personnel_targeting_exposure_review.md` |
| "Can our community be brigaded by design?" | `domain-psy-ops/organizational-red-team/psyops_community_moderation_resilience_review.md` |
| "Prebunk a claim before it lands" | `domain-psy-ops/counter-messaging/psyops_prebunking_inoculation_design.md` |
| "Write a correction that actually works" | `domain-psy-ops/counter-messaging/psyops_debunk_and_correction_design.md` |
| "Should we respond at all, or amplify it?" | `domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md` |
| "Communicate with integrity under attack" | `domain-psy-ops/counter-messaging/psyops_crisis_communication_integrity_plan.md` |
| "Map the competing influence taxonomies" | `domain-psy-ops/case-studies-taxonomies/psyops_technique_taxonomy_reference.md` |
| "Study a documented historical operation" | `domain-psy-ops/case-studies-taxonomies/psyops_historical_operation_case_study.md` |
| "Teach media literacy without breeding cynics" | `domain-psy-ops/case-studies-taxonomies/psyops_media_literacy_curriculum_designer.md` |
| **Write a letter/request to a company, agency, insurer, school, or landlord (35 prompts, LAYPERSON)** | **Use `domain-written-advocacy/` — see [README](../domain-written-advocacy/README.md). Never cites statutes or names regulators from memory; legal threats route to an attorney.** |
| "Turn this situation into a written request I can send" | `domain-written-advocacy/cross-cutting/advocacy_request_letter_architect.md` |
| "Confirm in writing what was agreed on a phone call" | `domain-written-advocacy/cross-cutting/advocacy_channel_and_record_strategy.md` |
| "They replied — what did they actually commit to?" | `domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md` |
| "Plan escalation from frontline to supervisor to regulator" | `domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md` |
| "Keep a dated log of an ongoing dispute" | `domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md` |
| "Chase an unanswered request without weakening the record" | `domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md` |
| "Cancel a subscription in writing and get it confirmed" | `domain-written-advocacy/accounts-and-billing/advocacy_subscription_cancellation_request.md` |
| "Close my account entirely and settle the balance" | `domain-written-advocacy/accounts-and-billing/advocacy_account_closure_request.md` |
| "I cancelled and was charged anyway / free trial converted" | `domain-written-advocacy/accounts-and-billing/advocacy_recurring_charge_dispute.md` |
| "Dispute a utility, telecom, or broadband bill or outage" | `domain-written-advocacy/accounts-and-billing/advocacy_utility_telecom_service_dispute.md` |
| "My price went up — ask for a better rate" | `domain-written-advocacy/accounts-and-billing/advocacy_price_increase_retention_request.md` |
| "Ask a company to delete my personal data" | `domain-written-advocacy/privacy-and-data/advocacy_data_deletion_request.md` |
| "Find out what data they hold about me (DSAR)" | `domain-written-advocacy/privacy-and-data/advocacy_data_access_request.md` |
| "Stop marketing contact and stop them selling my data" | `domain-written-advocacy/privacy-and-data/advocacy_marketing_optout_do_not_sell_request.md` |
| "Remove my listing from a people-search / data broker" | `domain-written-advocacy/privacy-and-data/advocacy_data_broker_removal_request.md` |
| "My privacy request was ignored or refused" | `domain-written-advocacy/privacy-and-data/advocacy_privacy_request_escalation.md` |
| "Make a warranty claim" | `domain-written-advocacy/products-and-warranty/advocacy_warranty_claim_letter.md` |
| "Faulty / misdescribed product — repair, replace, or refund" | `domain-written-advocacy/products-and-warranty/advocacy_defective_product_remedy_demand.md` |
| "Contractor's work is unfinished, defective, or abandoned" | `domain-written-advocacy/products-and-warranty/advocacy_service_nonperformance_demand.md` |
| "Report a dangerous product (evidence preservation first)" | `domain-written-advocacy/products-and-warranty/advocacy_safety_defect_report.md` |
| "Ask for temporary hardship help (forbearance / deferment / pause)" | `domain-written-advocacy/financial-hardship/advocacy_hardship_assistance_request.md` |
| "Propose an instalment plan I can actually maintain" | `domain-written-advocacy/financial-hardship/advocacy_payment_arrangement_proposal.md` |
| "Ask for a fee to be waived" | `domain-written-advocacy/financial-hardship/advocacy_fee_waiver_request.md` |
| "Ask about an accurate late mark already reported (goodwill)" | `domain-written-advocacy/financial-hardship/advocacy_goodwill_adjustment_request.md` |
| "Ask a lender to lower my interest rate" | `domain-written-advocacy/financial-hardship/advocacy_interest_rate_reduction_request.md` |
| "Dispute an inaccurate entry on my credit report" | `domain-written-advocacy/financial-hardship/advocacy_credit_report_dispute.md` |
| "Appeal a denied insurance claim (internal)" | `domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md` |
| "Take an upheld denial to independent/external review" | `domain-written-advocacy/insurance-and-medical/advocacy_external_review_request.md` |
| "Get an itemized medical bill and dispute what's wrong" | `domain-written-advocacy/insurance-and-medical/advocacy_medical_bill_dispute.md` |
| "Ask about hospital financial assistance / charity care" | `domain-written-advocacy/insurance-and-medical/advocacy_financial_assistance_charity_care_request.md` |
| "Request public records / FOIA from a government body" | `domain-written-advocacy/institutions-and-records/advocacy_public_records_request.md` |
| "Appeal a benefits denial, reduction, or termination" | `domain-written-advocacy/institutions-and-records/advocacy_benefits_denial_appeal.md` |
| "Complain to a regulator, ombudsman, or licensing body" | `domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md` |
| "Request a workplace accommodation, leave, or policy exception" | `domain-written-advocacy/institutions-and-records/advocacy_workplace_written_request.md` |
| "Ask a school for an assessment, support, records, or a review" | `domain-written-advocacy/institutions-and-records/advocacy_school_written_request.md` |
| "Design an N-week curriculum to a target level" | `domain-learning/learning_curriculum_designer.md` |
| "Deliberate-practice loop for a skill" | `domain-learning/learning_deliberate_practice_designer.md` |
| "Layered reading list (foundations → frontier)" | `domain-learning/learning_reading_list_curator.md` |
| "Feynman-test my understanding of a concept" | `domain-learning/learning_concept_explanation_audit.md` |
| "Translate a skill gap into a learning plan" | `domain-learning/learning_skill_gap_to_curriculum.md` |
| "Plan legal research (before Westlaw/Lexis)" | `domain-specialized-fields/legal/legal_research_plan.md` |
| "Patent landscape scan / IP whitespace" | `domain-specialized-fields/ip/patent_landscape_scan.md` |
| "Technical due diligence plan" | `domain-business-strategy/research/technical_due_diligence_plan.md` |
| "Synthesize user interviews into themes" | `domain-business-strategy/research/user_research_synthesis.md` |
| "Competitor teardown" | `domain-business-strategy/research/competitor_teardown.md` |
| "Decision-forcing meeting pre-read" | `domain-productivity/operating-cadence/meeting_pre_read_drafter.md` |
| "Helm charts/K8s" | `domain-agentic-resources/skills/cloud-infrastructure/` |
| "GitHub operations" | `domain-agentic-resources/skills/developer-tools/github-ops/` |
| "Create a skill" | `authoring/skill-patterns/README.md` |
| "Create an agent" | `authoring/agent-patterns/AGENT_QUICK_START.md` |
| "Create a command" | `authoring/command-patterns/COMMAND_QUICK_START.md` |
| "Design an agentic system (manual)" | `authoring/system-patterns/README.md` |
| "Produce an agentic system from a use case (guided)" | `agentic-system-factory/orchestrator_agentic_system.md` |
| "Does this need an agent at all? (Gate 0)" | `domain-AI-ML/agentic-ai-systems/aiagent_complexity_ladder_gate.md` |
| **AI/ML engineering (full lifecycle)** | **Use `domain-AI-ML/` — see [README](../domain-AI-ML/README.md); routing is by lifecycle stage** |
| "Is this even an ML problem?" | `domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md` |
| "Turn my business problem into an ML task / scope the use case" | `domain-AI-ML/problem-framing-scoping/mlframe_problem_to_ml_task_translator.md`, `mlframe_ml_use_case_canvas.md` |
| "What metric should I optimize?" | `domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md` |
| "My eval results look too good to be true" | `domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md` + `domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md` |
| "Which algorithm should I use? / give me a baseline" | `domain-AI-ML/classical-ml-modeling/mlmodel_algorithm_selection_matrix.md`, `mlmodel_baseline_modeling_plan.md` |
| "My training loss won't go down" | `domain-AI-ML/deep-learning/dl_training_not_converging_debug.md` |
| "Make inference faster / cheaper / fit on-device" | `domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md`, `mlopt_edge_deployment_optimization.md` |
| "Set up experiment tracking / a model registry / ML CI-CD" | `domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md`, `mlops_model_registry_design.md`, `mlops_ml_cicd_pipeline_design.md` |
| "My model degraded in production / detect drift" | `domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md`, `mlmonitor_drift_detection_design.md` |
| "Is my model biased? / write a model card" | `domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md`, `rai_model_card_authoring.md` |
| "Assess against EU AI Act / NIST AI RMF / FDA SaMD / ECOA / GDPR Art. 22 / SR 11-7" | `domain-AI-ML/responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md` and siblings |
| "Design a RAG system / evaluate my LLM" | `domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md`, `genai_llm_evaluation_design.md` |
| "Text classification / NER / topic modeling **without** an LLM" | `domain-AI-ML/specialized-ml/nlp-classical/` |
| "Scope / prioritize / build the business case for an ML project" | `domain-AI-ML/ai-product-leadership/aipm_use_case_prioritization.md`, `aipm_roi_business_case.md` |
| "Explain an ML concept / read a paper / prep for an ML interview" | `domain-AI-ML/learning-ai-ml/mllearn_concept_explainer.md`, `mllearn_paper_reading_guide.md`, `mllearn_ml_interview_prep.md` |
| "I don't know where to start / the model isn't working" | `domain-AI-ML/problem-framing-scoping/mlframe_domain_triage_router.md` |
| "Threat-model our deployed model / adversarial, poisoning, extraction, inversion" | `domain-AI-ML/model-security/mlsec_ml_threat_model.md` and the `mlsec_*` cluster |
| "Which privacy technique do we need (DP, federated, synthetic)?" | `domain-AI-ML/responsible-ai-governance/rai_privacy_technique_selection.md` |
| "Fix RAG retrieval / reranking / citations / GraphRAG / MCP tools" | `domain-AI-ML/genai-llm-engineering/genai_query_rewriting_expansion.md`, `genai_reranking_strategy.md`, `genai_citation_grounding_attribution.md`, `genai_graphrag_knowledge_graph_design.md`, `genai_mcp_tool_interface_design.md` |
| "Find existing skills" | `domain-agentic-resources/skills/` |
| "Find existing agents" | `domain-agentic-resources/agents/` |
| "Find existing commands" | `domain-agentic-resources/commands/` |
| "PDF/document processing" | `domain-agentic-resources/skills/document-processing/` |
| "Check my decision" | `domain-productivity/validation/` |
| "Research competitors" | `domain-business-strategy/research/` |
| "Organize my notes" | `domain-business-strategy/organization/` |
| "Build an app" | `domain-software-engineering/prototyping/` |
| "Automate workflow" | `domain-productivity/automation/` |
| **Deep Work & Focus** | **Use `domain-productivity/deep-work/` — see README for full map** |
| "Estimate my focus parameters" | `domain-productivity/deep-work/deepwork_focus_parameters_estimator.md` |
| "Audit my calendar for focus destruction" | `domain-productivity/deep-work/deepwork_calendar_audit.md` |
| "Design an email / message triage" | `domain-productivity/deep-work/deepwork_message_triage_system.md` |
| "Convert a meeting to async" | `domain-productivity/deep-work/deepwork_meeting_to_async_converter.md` |
| "Estimate the true cost of a meeting" | `domain-productivity/deep-work/deepwork_meeting_cost_estimator.md` |
| "Audit self-interruption patterns" | `domain-productivity/deep-work/deepwork_self_interruption_audit.md` |
| "Capture context at end of a focus block" | `domain-productivity/deep-work/deepwork_block_end_context_capture.md` |
| "Synthesize project state for reload" | `domain-productivity/deep-work/deepwork_project_state_synthesis.md` |
| "Design a personal reload ritual" | `domain-productivity/deep-work/deepwork_reload_ritual_design.md` |
| "Digitize handwritten notes" | `domain-productivity/deep-work/deepwork_handwritten_notes_digitizer.md` |
| "Chunk a project to calendar blocks" | `domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md` |
| "Decompose a complex task" | `domain-productivity/deep-work/deepwork_decompose_complex_task.md` |
| "Match today's tasks to today's calendar" | `domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md` |
| "Team-level focus audit / norms" | `domain-productivity/deep-work/deepwork_team_focus_audit.md` |
| "Run a one-week focus experiment" | `domain-productivity/deep-work/deepwork_focus_experiment_week.md` |
| "Troubleshoot a lost focus day" | `domain-productivity/deep-work/deepwork_lost_focus_day_troubleshoot.md` |
| "Summarize a focus block for an async update" | `domain-productivity/deep-work/deepwork_focus_block_async_summary.md` |
| **Bottlenecks & Personal Constraints** | **Use `domain-productivity/bottlenecks/` — see README for full map** |
| "Locate my true bottleneck (clarity / execution / distribution)" | `domain-productivity/bottlenecks/bottleneck_locator.md` |
| "Surface what I actually want" | `domain-productivity/bottlenecks/bottleneck_clarity_ambition_surfacer.md` |
| "Design daily execution habits" | `domain-productivity/bottlenecks/bottleneck_daily_execution_habits.md` |
| "Find my real distribution / relationships constraint" | `domain-productivity/bottlenecks/bottleneck_distribution_constraint_finder.md` |
| "Image generation" | `domain-image-generation/` |
| "Which image model should I use?" | `domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md` |
| "gpt-image-2 prompt" | `domain-image-generation/gpt-image-2/` |
| "OpenAI image model guide" | `domain-image-generation/GPT_IMAGE_2_GUIDE.md` |
| "Nano Banana / Gemini image model prompt" | `domain-image-generation/NANO_BANANA_GUIDE.md` |
| "Nano Banana character consistency / storyboard / Veo pipeline" | `domain-image-generation/NANO_BANANA_GUIDE.md` |
| "JSON schema prompting for image generation" | `domain-image-generation/NANO_BANANA_GUIDE.md` (Section 9) |
| "Character bible / reference pack / identity across scenes" | `domain-image-generation/CHARACTER_BIBLE_PIPELINE.md` |
| "Storyboard grid / keyframes / video handoff" | `domain-image-generation/STORYBOARD_WORKFLOW.md` |
| "Healthcare/medical image (badge buddy, patient handout, medical diagram)" | `domain-image-generation/healthcare/` (anti-fabrication first — see [README](../domain-image-generation/healthcare/README.md)) |
| "Clinician reference card (lab values, ACLS, dosing, antibiogram)" | `domain-image-generation/healthcare/clinical_badge_buddy_*.md` |
| "Patient education handout (condition, discharge, meds, anatomy)" | `domain-image-generation/healthcare/patient_*.md` |
| "Medical/clinical diagram (anatomy, procedure steps, pathophysiology, algorithm)" | `domain-image-generation/healthcare/medical_*.md` |
| "Coloring page / coloring book (adult, kids, KDP, mandala, themed)" | `domain-image-generation/coloring-book/` |
| "Product / e-commerce photography (white-bg, lifestyle, flat lay, macro, variants)" | `domain-image-generation/ecommerce-product/` |
| "Social-media graphic (quote, carousel, announcement, story cover, banner)" | `domain-image-generation/social-media/` |
| "Book / ebook / album / podcast cover" | `domain-image-generation/publishing-covers/` |
| "Event poster / flyer / gig poster" | `domain-image-generation/events-print/` |
| "T-shirt graphic / sticker / print-on-demand pattern" | `domain-image-generation/merch-print-on-demand/` |
| "Children's book illustration (spread, character sheet, style series)" | `domain-image-generation/childrens-illustration/` |
| "Comic page / manga panel / webtoon strip" | `domain-image-generation/comic-sequential/` |
| "Scientific illustration / exploded diagram / data-viz image" | `domain-image-generation/scientific-technical/` (accuracy-gated) |
| **Uncited expertise → sourced, publishable nonfiction (find real sources, map claims→references, legal-safe)** | **Use `sourced-nonfiction-studio/` — see [README](../sourced-nonfiction-studio/README.md). `/source-my-draft` for the full pipeline.** |
| "Source my uncited draft into a cited, publishable piece" | `sourced-nonfiction-studio/orchestrator_sourced_nonfiction.md` or `/source-my-draft` |
| "Find real credible sources for my factual claims" | `sourced-nonfiction-studio/` `/find-sources` |
| "Decide what to do with a claim I know but can't cite (keep/soften/reframe/cut)" | `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` |
| "Reconcile my finished cited draft against its sources (fact-check)" | `domain-research-academic/research_manuscript_fact_check_reconciler.md` or `/fact-check-manuscript` |
| "Defamation / right-of-publicity risk screen for nonfiction naming real people" | `domain-legal/ip/legal_defamation_publicity_risk_screen.md` |
| "Rewrite source text into original wording (nonfiction, preserve facts)" | `domain-professional-writing/writing/writing_original_expression_rewriter.md` |
| "Improve my prompt" | `domain-prompt-engineering/prompt-improvement/` |
| **Model Behavior Diagnostics** | **Use `domain-prompt-engineering/model-behavior/` — see README** |
| "Diagnose why model isn't following my instruction" | `domain-prompt-engineering/model-behavior/modelbehavior_instruction_deviation_diagnostic.md` |
| "Coach the model mid-session to fix behavior" | `domain-prompt-engineering/model-behavior/modelbehavior_active_coaching_in_session.md` |
| "Refactor my system prompt to stop fighting the model" | `domain-prompt-engineering/model-behavior/modelbehavior_refactor_system_prompt.md` |
| "Build a new system prompt from principles" | `domain-prompt-engineering/model-behavior/modelbehavior_system_prompt_from_scratch.md` |
| **Escaping Default (Median) Output** | **Use `domain-prompt-engineering/escape-median/` — see README** |
| "Map the model's default stance on a topic" | `domain-prompt-engineering/escape-median/escapemedian_default_position_mapper.md` |
| "Sharpen a vague instruction so the model can't default" | `domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md` |
| "Compound in-session corrections into a rule block" | `domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md` |
| "Bootstrap a personal CLAUDE.md from observed preferences" | `domain-prompt-engineering/escape-median/escapemedian_bootstrap_instruction_file.md` |
| **Goal Orientation & Intent (before the prompt)** | **Use `domain-prompt-engineering/goal-orientation/` — see README** |
| "Am I solving the right problem?" | `domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md` |
| "Workshop constraints, escalation triggers, value hierarchy for an AI task" | `domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md` |
| "Audit my team's AI use for misalignment risk" | `domain-prompt-engineering/goal-orientation/goalorientation_team_ai_misalignment_map.md` |
| **Prompt Skill Development (build skill over months)** | **Use `domain-prompt-engineering/skill-development/` — see README** |
| "Off-screen thinking pass before I open a chat" | `domain-prompt-engineering/skill-development/promptcraft_pre_ai_thinking_exercise.md` |
| "Rapid diagnostic of my AI skill across four disciplines" | `domain-prompt-engineering/skill-development/promptcraft_rapid_four_discipline_diagnostic.md` |
| "Deep four-discipline diagnostic with multi-month roadmap" | `domain-prompt-engineering/skill-development/promptcraft_deep_four_discipline_roadmap.md` |
| "Rewrite my vague chat opener into a self-contained prompt" | `domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md` |
| "Build a reusable personal context document" | `domain-prompt-engineering/skill-development/promptcraft_personal_context_document.md` |
| "Write a spec that fully defines 'done'" | `domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md` |
| "Build an eval harness for my personal workflow" | `domain-prompt-engineering/skill-development/promptcraft_eval_harness.md` |
| "Design a reusable constraint architecture across a task class" | `domain-prompt-engineering/skill-development/promptcraft_constraint_architecture_design.md` |
| **AI Task Difficulty (is this task AI-shaped?)** | **Use `domain-prompt-engineering/evaluation/` (taskdifficulty_* prompts)** |
| "Decompose a task across orthogonal AI-difficulty axes" | `domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md` |
| "Optimize a workflow based on which axes are hardest" | `domain-prompt-engineering/evaluation/taskdifficulty_workflow_axis_optimizer.md` |
| "Build calibrated taste for AI output quality" | `domain-prompt-engineering/evaluation/taskdifficulty_calibrated_comparison.md` |
| **Correctness & Evaluation of AI Output** | **Use `domain-prompt-engineering/evaluation/` (correctness_* prompts)** |
| "Define what 'correct' actually means for a fuzzy task" | `domain-prompt-engineering/evaluation/correctness_discovery_prompt.md` |
| "Force tradeoff clarity across competing quality dimensions" | `domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md` |
| "Translate vague requirements into testable specs" | `domain-prompt-engineering/evaluation/correctness_vague_requirements_translator.md` |
| "Audit an existing prompt for specification gaps" | `domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md` |
| "Pre-mortem on correctness before shipping" | `domain-prompt-engineering/evaluation/correctness_pre_mortem.md` |
| "Design an evaluation set for correctness" | `domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md` |
| "Production monitoring for output correctness drift" | `domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md` |
| **Non-Coding Prompts** | **Use NON_CODING_QUICK_START.md** |
| **Education & teaching (267 prompts)** | **Route by audience: `domain-education-teaching/instructor/` (teaching a class), `program/` (running a programme), `learner/` (studying yourself) — see [README](../domain-education-teaching/README.md)** |
| "Lesson plan / unit / PBL / sub plan" | `domain-education-teaching/instructor/lesson-planning/` |
| "Explain this so a kid / teen / adult gets it" | `domain-education-teaching/instructor/explanation-craft/` |
| "Half the class didn't get it / reteach" | `domain-education-teaching/instructor/response-cycle/` |
| "Write quiz items / distractors / DOK / Bloom's stems" | `domain-education-teaching/instructor/assessment-items/` |
| "Test blueprint / performance task / rubric / portfolio" | `domain-education-teaching/instructor/assessment-design/` |
| "Item analysis / alignment audit / standards-based grading" | `domain-education-teaching/instructor/assessment-analysis/` |
| "Grade a stack of essays / write feedback" | `domain-education-teaching/instructor/grading-feedback/` |
| "Newsletter / conference notes / report card comments" | `domain-education-teaching/instructor/reporting-communication/` |
| "IEP / 504 / behaviour plan / UDL / ELL / advising" | `domain-education-teaching/instructor/student-support/` |
| "Classroom norms / routines / restorative conversation" | `domain-education-teaching/instructor/classroom-ops/` |
| "Slide deck / video script / choice board / LMS shell / AI literacy" | `domain-education-teaching/instructor/ed-tech/` |
| "Syllabus / online course conversion / microlearning / onboarding / compliance training" | `domain-education-teaching/instructor/higher-ed-corporate/` |
| "ELA / math / science / social studies / world language teaching moves" | `domain-education-teaching/instructor/subject-pedagogy/` |
| "Turn a lecture or textbook into study material" | `domain-education-teaching/learner/note-taking/` |
| "Retrieval practice / spaced review / flashcards / Feynman / mnemonics" | `domain-education-teaching/learner/memory-and-recall/` |
| "Self-quiz / confidence calibration / mistake log" | `domain-education-teaching/learner/self-assessment/` |
| "Practice test / finals week / test-day strategy / cert drill" | `domain-education-teaching/learner/exam-prep/` |
| "Drill maths proofs / pharmacology / legal issue-spotting / NCLEX" | `domain-education-teaching/learner/study-by-discipline/` |
| "Teach me this (Socratic, no answers given)" | `domain-education-teaching/learner/tutoring/` |
| "I'm stuck / I got it wrong and don't know why" | `domain-education-teaching/learner/stuck-and-confused/` |
| "Coach my essay without writing it / thesis / citations / integrity check" | `domain-education-teaching/learner/writing/` |
| "Annotate / summarize / analyse assigned reading" | `domain-education-teaching/learner/reading/` |
| "Word problems / my own error analysis / lab report / data interpretation" | `domain-education-teaching/learner/math-science/` |
| "L2 conversation / grammar / idiom / pronunciation" | `domain-education-teaching/learner/language/` |
| "Refine a research question / search strategy / synthesize sources" | `domain-education-teaching/learner/research/` |
| "Assignment tracking / big project / office hours / discussion prep" | `domain-education-teaching/learner/time-and-discussion/` |
| "Going back to school as an adult / prior learning / writing rust" | `domain-education-teaching/learner/adult-learner/` |
| "Just tell me what to run, in what order (chained workflows)" | `domain-education-teaching/learner/guides/` |
| **Program-level curriculum, standards, accreditation, faculty dev, program evaluation** | **See `domain-education-teaching/program/curriculum-design/` and sibling subdirectories** |
| "Curriculum map (course-outcome-standard-assessment)" | `domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md` |
| "K-12 multi-year scope & sequence" | `domain-education-teaching/program/curriculum-design/program_scope_sequence_k12.md` |
| "HE program scope & sequence" | `domain-education-teaching/program/curriculum-design/program_scope_sequence_he.md` |
| "Workforce / CTE / apprenticeship scope & sequence" | `domain-education-teaching/program/curriculum-design/program_scope_sequence_workforce.md` |
| "Backward program design (UbD at program scale)" | `domain-education-teaching/program/curriculum-design/program_backward_program_design.md` |
| "Standards alignment audit" | `domain-education-teaching/program/curriculum-design/program_standards_alignment_audit.md` |
| "Crosswalk between two standards frameworks" | `domain-education-teaching/program/curriculum-design/program_standards_crosswalk_generator.md` |
| "Competency framework (parameterized by sector)" | `domain-education-teaching/program/curriculum-design/program_competency_framework_designer.md` |
| "Workforce competency mapping (O*NET / industry creds)" | `domain-education-teaching/program/curriculum-design/program_competency_mapping_workforce.md` |
| "Vertical alignment audit" | `domain-education-teaching/program/curriculum-design/program_vertical_alignment_auditor.md` |
| "Horizontal alignment (cross-disciplinary, same level)" | `domain-education-teaching/program/curriculum-design/program_horizontal_alignment_mapper.md` |
| "HE course design (constructive alignment, Biggs)" | `domain-education-teaching/program/curriculum-design/program_course_design_he.md` |
| "Advanced unit design (UbD + UDL + accessibility)" | `domain-education-teaching/program/curriculum-design/program_unit_design_advanced.md` |
| "Learning objectives writer (Bloom's, ABCD, SMART)" | `domain-education-teaching/program/curriculum-design/program_learning_objectives_writer_blooms.md` |
| "Bloom's taxonomy calibrator (audit objectives or items)" | `domain-education-teaching/program/curriculum-design/program_blooms_taxonomy_calibrator.md` |
| "Learning progression map" | `domain-education-teaching/program/curriculum-design/program_progression_map_designer.md` |
| "Milestone / checkpoint architecture" | `domain-education-teaching/program/curriculum-design/program_milestone_alignment_designer.md` |
| "Remediation pathway (MTSS/RTI or competency-based)" | `domain-education-teaching/program/curriculum-design/program_remediation_pathway_designer.md` |
| "PSLO / ISLO / CSLO architecture" | `domain-education-teaching/program/outcomes-assessment/program_program_outcomes_framework.md` |
| "Outcomes-to-assessment evidence mapper" | `domain-education-teaching/program/outcomes-assessment/program_outcomes_to_assessment_mapper.md` |
| "Assessment blueprint (test specification)" | `domain-education-teaching/program/outcomes-assessment/program_assessment_blueprint_builder.md` |
| "Program gap analysis (taught vs required)" | `domain-education-teaching/program/outcomes-assessment/program_program_gap_analysis.md` |
| "Signature assignment design (HE)" | `domain-education-teaching/program/outcomes-assessment/program_signature_assignment_designer.md` |
| "Capstone assessment design" | `domain-education-teaching/program/outcomes-assessment/program_capstone_assessment_designer.md` |
| "Rubric alignment audit" | `domain-education-teaching/program/outcomes-assessment/program_rubric_alignment_to_outcomes.md` |
| "Competency-based assessment evidence plan" | `domain-education-teaching/program/outcomes-assessment/program_competency_assessment_evidence_design.md` |
| "Regional HE accreditation self-study (HLC/MSCHE/SACSCOC/WSCUC/NWCCU)" | `domain-education-teaching/program/accreditation-review/program_accreditation_self_study_he.md` |
| "Programmatic accreditation self-study (ABET/AACSB/CAEP/CCNE/ACPE/etc.)" | `domain-education-teaching/program/accreditation-review/program_accreditation_self_study_programmatic.md` |
| "Med-ed accreditation self-study (LCME/ACGME/COCA/CODA)" | `domain-education-teaching/program/accreditation-review/program_accreditation_self_study_meded.md` |
| "Program review cycle design" | `domain-education-teaching/program/accreditation-review/program_program_review_cycle_designer.md` |
| "Accreditation evidence compiler" | `domain-education-teaching/program/accreditation-review/program_accreditation_evidence_compiler.md` |
| "Multi-semester faculty development plan" | `domain-education-teaching/program/faculty-development/program_faculty_development_plan_designer.md` |
| "Professional learning community design" | `domain-education-teaching/program/faculty-development/program_professional_learning_community_designer.md` |
| "Instructional coaching program design" | `domain-education-teaching/program/faculty-development/program_instructional_coaching_program.md` |
| "Assessment literacy faculty curriculum" | `domain-education-teaching/program/faculty-development/program_assessment_literacy_curriculum.md` |
| "New faculty onboarding program" | `domain-education-teaching/program/faculty-development/program_faculty_onboarding_program.md` |
| "Program evaluation framework (Kirkpatrick/CIPP/logic model/ToC)" | `domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md` |
| "Logic model / theory of change designer" | `domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md` |
| "Learning analytics interpreter (LMS/dashboards)" | `domain-education-teaching/program/evaluation-analytics/program_learning_analytics_interpreter.md` |
| "Early warning system designer" | `domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md` |
| "PDSA / continuous improvement cycle" | `domain-education-teaching/program/evaluation-analytics/program_continuous_improvement_cycle.md` |
| "CBME implementation roadmap (program-level)" | `domain-medical-education/educator-curriculum-design/curric_cbme_implementation_program.md` |
| "Residency curriculum mapper (ACGME Milestones + EPAs)" | `domain-medical-education/educator-curriculum-design/curric_residency_curriculum_mapper.md` |
| "EPA implementation designer" | `domain-medical-education/educator-curriculum-design/curric_epa_implementation_designer.md` |
| "Program competency framework (ACGME six core)" | `domain-medical-education/educator-curriculum-design/curric_program_competency_framework_acgme.md` |
| "Creative writing/story (adult)" | `domain-creative-writing/` — see [README](../domain-creative-writing/README.md) routing table |
| "Build/fix a scene; POV; pacing" | `domain-creative-writing/fiction/` |
| "Show-don't-tell / description / theme / openings / endings" | `domain-creative-writing/craft-tools/` |
| "Mystery/crime or SF/fantasy craft deep-dive" | `domain-creative-writing/genre-workshops/` |
| "Memoir, essay, or narrative nonfiction" | `domain-creative-writing/creative-nonfiction/` |
| "Poetry forms / imagery & metaphor" | `domain-creative-writing/poetry/` |
| "Adult-fiction query, synopsis, pitch, comps" | `domain-creative-writing/publishing-career/` |
| **Children's Writing (authoring kid-friendly material, 22 prompts)** | **Use `domain-childrens-writing/` — see [README](../domain-childrens-writing/README.md)** |
| "Write a board / concept / ABC / counting book (0-3)" | `domain-childrens-writing/fiction-workshops/childrens_board_concept_book_workshop.md` |
| "Write a picture book (ages 2-8)" | `domain-childrens-writing/fiction-workshops/childrens_picture_book_workshop.md` |
| "Write an early reader / chapter book (ages 5-10)" | `domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md` |
| "Write a middle-grade novel (ages 8-12)" | `domain-childrens-writing/fiction-workshops/childrens_middle_grade_fiction_workshop.md` |
| "Write for the 11-14 / tween / young-teen reader" | `domain-childrens-writing/fiction-workshops/childrens_ya_crossover_workshop.md` |
| "Write a novel in verse" | `domain-childrens-writing/fiction-workshops/childrens_verse_novel_workshop.md` |
| "Write a graphic novel / comic for kids" | `domain-childrens-writing/fiction-workshops/childrens_graphic_novel_comics_workshop.md` |
| "Write a kids' biography / true-history story" | `domain-childrens-writing/nonfiction-workshops/childrens_narrative_nonfiction_workshop.md` |
| "Write a STEM / concept book for kids" | `domain-childrens-writing/nonfiction-workshops/childrens_expository_stem_concept_workshop.md` |
| "Strengthen my opening / first line" | `domain-childrens-writing/craft-tools/childrens_opening_pages_hook.md` |
| "Fix my kid dialogue (sounds adult / cheesy)" | `domain-childrens-writing/craft-tools/childrens_kid_dialogue_workshop.md` |
| "Build / audit my child protagonist" | `domain-childrens-writing/craft-tools/childrens_character_creation.md` |
| "Revise my draft (layered self-edit pass)" | `domain-childrens-writing/craft-tools/childrens_revision_self_edit_pass.md` |
| "Hit a specific kids' reading level / age band" | `domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md` |
| "Fix the rhyme / meter in my kids' verse" | `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md` |
| "Handle hard topics (death/divorce) in a kids' book" | `domain-childrens-writing/craft-tools/childrens_sensitive_topics_framing.md` |
| "Writing across a culture / identity I don't share" | `domain-childrens-writing/representation-collaboration/childrens_writing_across_difference_audit.md` |
| "Art notes / working with an illustrator" | `domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md` |
| "Make my book accessible (dyslexia / neurodivergent)" | `domain-childrens-writing/representation-collaboration/childrens_accessible_inclusive_design.md` |
| "Write my agent query letter (kidlit)" | `domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md` |
| "Write my synopsis / assemble submission package" | `domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md` |
| "Logline / comp titles / market positioning" | `domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md` |
| "Patient communication" | `domain-healthcare-clinical/` |
| "Write a PBL case / TBL exercise / OSCE station" | `domain-medical-education/` |
| "Simulation scenario / debriefing guide" | `domain-medical-education/` |
| "NBME MCQ / oral exam / milestone narrative" | `domain-medical-education/` |
| "Feedback for residents / remediation plan" | `domain-medical-education/` |
| "Faculty development module / lecture redesign" | `domain-medical-education/` |
| **Health-professions LEARNER (student/resident/PA/pharmacy/EMS/AH/dental) self-study tools** | **Use `domain-medical-education/` — see [README](../domain-medical-education/README.md)** |
| "Build me an illness script" / "atypical variants" | `learner-self-study/clinical-reasoning/learner_illness_script_builder.md` |
| "Quiz me on differentials for [complaint]" | `learner-self-study/clinical-reasoning/learner_differential_diagnosis_drill.md` |
| "Sharpen my one-liner / problem representation" | `learner-self-study/clinical-reasoning/learner_problem_representation_rehearsal.md` |
| "Hypothesis-driven workup / next-best test" | `learner-self-study/clinical-reasoning/learner_hypothesis_driven_workup_drill.md` |
| "Walk me through an interactive case" | `learner-self-study/clinical-reasoning/learner_clinical_case_walkthrough.md` |
| "Pick a reasoning schema" | `learner-self-study/clinical-reasoning/learner_clinical_reasoning_schema_practice.md` |
| "Run me through an OSCE station" | `learner-self-study/clinical-skills/learner_osce_self_rehearsal.md` |
| "Be my simulated patient — history practice" | `learner-self-study/clinical-skills/learner_history_taking_rehearsal.md` |
| "Coach my oral presentation" | `learner-self-study/clinical-skills/learner_oral_presentation_practice.md` |
| "Critique my SOAP note" | `learner-self-study/clinical-skills/learner_soap_note_writing_practice.md` |
| "Critique my admission H&P" | `learner-self-study/clinical-skills/learner_h_and_p_writing_practice.md` |
| "Physical exam checklist for [region]" | `learner-self-study/clinical-skills/learner_physical_exam_checklist_generator.md` |
| "Drill anatomy / physiology / pathophys / pharm / micro / immuno" | `learner-self-study/foundational-sciences/` |
| "Coach me through a board question I got wrong" | `learner-self-study/exam-prep/learner_board_style_question_review.md` |
| "Distractor analysis drill" | `learner-self-study/exam-prep/learner_distractor_analysis_drill.md` |
| "Debrief my qbank session" | `learner-self-study/exam-prep/learner_qbank_session_debriefer.md` |
| "High-yield topic compressor" | `learner-self-study/exam-prep/learner_high_yield_topic_compressor.md` |
| "Pre-brief me before a procedure" | `learner-self-study/procedures-emergencies/learner_procedure_prep_briefing.md` |
| "ACLS / PALS / NRP / ATLS rehearsal" | `learner-self-study/procedures-emergencies/learner_code_algorithm_rehearsal.md` |
| "Mental pre-brief before sim" | `learner-self-study/procedures-emergencies/learner_simulation_pre_briefing.md` |
| "Critical-event recognition drill (anaphylaxis, sepsis, etc.)" | `learner-self-study/procedures-emergencies/learner_critical_event_recognition_drill.md` |
| "Pre-rounding scaffold for inpatients" | `learner-self-study/clinical-prep/learner_pre_rounding_prep.md` |
| "Pre-clinic patient prep" | `learner-self-study/clinical-prep/learner_pre_clinic_patient_prep.md` |
| "Practice handoff / sign-out / SBAR" | `learner-self-study/clinical-prep/learner_handoff_practice.md` |
| "Spaced-repetition / Anki deck from notes" | `learner-self-study/study-planning/learner_spaced_repetition_deck_generator.md` |
| "Board-exam study plan (USMLE/NCLEX/NAPLEX/PANCE/NREMT/NBDE/BCPS/etc.)" | `learner-self-study/study-planning/learner_study_plan_designer.md` |
| "Weekly study review" | `learner-self-study/study-planning/learner_weekly_study_review.md` |
| "Nursing care plan (NANDA/NIC/NOC) practice" | `learner-self-study/discipline-specific/learner_nursing_care_plan_practice.md` |
| "Pharmacy therapeutics SOAP / MTM" | `learner-self-study/discipline-specific/learner_pharmacy_therapeutics_soap_practice.md` |
| "EMS protocol drill (NREMT)" | `learner-self-study/discipline-specific/learner_ems_protocol_decision_drill.md` |
| "Dental treatment-planning practice" | `learner-self-study/discipline-specific/learner_dental_treatment_planning_practice.md` |
| "Allied-health (PT/OT/SLP/RT/RD/SW/AuD) scope + plan drill" | `learner-self-study/discipline-specific/learner_allied_health_scope_and_reasoning_drill.md` |
| "Research synthesis" | `domain-research-academic/` |
| **Science practice (bench / field / computational — the *doing* of science)** | **Use `domain-science/` — see [README](../domain-science/README.md). Discipline-specific judgment here; generic methodology → `domain-research-academic/`.** |
| "Refine a vague idea into a testable, scoped scientific question" | `domain-science/methods-foundations/science_research_question_refiner.md` |
| "Draft a preregistration / Stage-1 Registered Report" | `domain-science/methods-foundations/science_preregistration_drafter.md` |
| "Power & sample size (frequentist + Bayesian, assumptions surfaced)" | `domain-science/methods-foundations/science_power_and_sample_size_calculator.md` |
| "Design controls / blinding & randomization for an experiment" | `domain-science/methods-foundations/science_negative_and_positive_control_designer.md` |
| "Confound/bias audit or Cook-Campbell validity walkthrough" | `domain-science/methods-foundations/science_confound_and_bias_audit.md` |
| "Replicability premortem / FAIR reproducibility self-audit" | `domain-science/methods-foundations/science_replicability_premortem.md` |
| "Which statistical test (with assumption checks)?" | `domain-science/statistics/science_statistical_test_selector.md` |
| "Effect sizes + intervals / multiple-comparisons strategy" | `domain-science/statistics/science_effect_size_and_uncertainty_reporter.md` / `science_multiple_comparisons_strategy.md` |
| "Pre-specified analysis plan (SAP) / p-hacking self-check" | `domain-science/statistics/science_pre_specified_analysis_plan.md` / `science_p_hacking_self_check.md` |
| "Mixed models / survival / causal inference (DAG) design" | `domain-science/statistics/science_mixed_models_design.md` / `science_survival_analysis_design.md` / `science_causal_inference_design.md` |
| "PRISMA-aligned meta-analysis protocol" | `domain-science/statistics/science_meta_analysis_protocol.md` |
| "Draft an IMRaD / figure-first manuscript from my results" | `domain-science/writing-communication/science_imrad_paper_drafter.md` |
| "Point-by-point response to reviewers / post-rejection appeal" | `domain-science/writing-communication/science_response_to_reviewers.md` / `science_appeal_to_editor_after_rejection.md` |
| "Pick a target journal / cover letter to editor" | `domain-science/writing-communication/science_journal_target_selector.md` / `science_cover_letter_to_editor.md` |
| "Abstract / conference abstract / poster spec / lay summary" | `domain-science/writing-communication/science_abstract_compressor.md` (+ conference_abstract, poster_designer, lay_summary_translator) |
| "Figure legend / figure or table design critique" | `domain-science/writing-communication/science_figure_legend_drafter.md` (+ figure_design_critique, table_design_critique) |
| "Plan a preprint release (server, license, versioning)" | `domain-science/writing-communication/science_preprint_release_plan.md` |
| "Resolve authorship (CRediT) / draft a COI disclosure" | `domain-science/ethics-integrity/science_authorship_and_credit_resolver.md` / `science_conflict_of_interest_disclosure_drafter.md` |
| "Pre-submission misconduct (FFP) / image-integrity self-audit" | `domain-science/ethics-integrity/science_misconduct_self_audit.md` / `science_image_integrity_self_check.md` |
| "Responsible-AI-use audit / FAIR-CARE-TRUST open-science audit" | `domain-science/ethics-integrity/science_responsible_ai_use_in_research_audit.md` / `science_open_science_practices_self_audit.md` |
| "Dual-use (DURC) governance self-screen" | `domain-science/ethics-integrity/science_dual_use_research_assessment.md` |
| "Correction vs retraction decision (COPE)" | `domain-science/ethics-integrity/science_retraction_or_correction_decision_walkthrough.md` |
| "Draft / troubleshoot a bench protocol; reagent or buffer math" | `domain-science/bench-and-wetlab/science_lab_protocol_drafter.md` (+ optimizer, reagent_and_supply_calculator, buffer_recipe_designer) |
| "IACUC / IRB / biosafety (IBC) protocol scaffold" | `domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md` / `science_human_subjects_irb_protocol_drafter.md` / `science_biosafety_risk_assessment.md` |
| "Cell-culture protocol / reagent (antibody/primer/cell-line) validation" | `domain-science/bench-and-wetlab/science_cell_culture_protocol_designer.md` / `science_reagent_validation_workflow.md` |
| "Sample chain-of-custody / ELN entry / failed-experiment post-mortem" | `domain-science/bench-and-wetlab/science_sample_logging_chain_of_custody_designer.md` / `science_lab_notebook_entry_writer.md` / `science_failed_experiment_post_mortem.md` |
| "Design a reproducible bioinformatics pipeline / genomics QC" | `domain-science/computational/science_bioinformatics_pipeline_designer.md` / `science_genomics_qc_protocol.md` |
| "scRNA-seq / proteomics analysis plan" | `domain-science/computational/science_single_cell_analysis_plan.md` / `science_proteomics_analysis_plan.md` |
| "Simulation V&V / numerical-convergence (GCI) audit" | `domain-science/computational/science_simulation_validation_protocol.md` / `science_numerical_convergence_audit.md` |
| "Computational-reproducibility environment / research-software repo layout" | `domain-science/computational/science_computational_reproducibility_environment.md` / `science_open_source_research_software_repo_layout.md` |
| "Data-management plan / data dictionary / metadata schema / synthetic data" | `domain-science/computational/science_data_management_plan_drafter.md` (+ data_dictionary, metadata_schema, synthetic_data_generator_design) |
| "ML-for-science leakage audit / benchmark design" | `domain-science/computational/science_ml_for_science_validation_audit.md` / `science_ml_for_science_benchmark_design.md` |
| "NIH Specific Aims / R01 outline; NSF or ERC outline" | `domain-science/grants-funding/science_specific_aims_drafter.md` / `science_nih_r01_outline_drafter.md` / `science_nsf_proposal_outliner.md` / `science_erc_grant_outliner.md` |
| "Grant Significance / Innovation / Approach section" | `domain-science/grants-funding/science_grant_significance_section_drafter.md` (+ innovation, approach) |
| "Grant resubmission response / budget justification / letter of support" | `domain-science/grants-funding/science_grant_resubmission_response.md` / `science_grant_budget_justification_drafter.md` / `science_letter_of_support_drafter.md` |
| "Draft / self-check a peer review; editorial decision letter" | `domain-science/peer-review/science_peer_review_drafter.md` (+ self_check, editorial_decision_drafter) |
| "Arbitrate divergent reviews / post-publication critique / review a replication" | `domain-science/peer-review/science_review_disagreement_arbitration_memo.md` / `science_post_publication_critique_drafter.md` / `science_review_for_replication_or_robustness.md` |
| "Trainee IDP / 1:1 / onboarding / lab-meeting; thesis-committee or qual prep; postdoc→PI" | `domain-science/lab-operations-mentorship/` (science_individual_development_plan_drafter, one_on_one_mentorship_session_plan, thesis_committee_meeting_prep, postdoc_to_pi_transition_plan, …) |
| "Lab-culture charter / undergrad-research or internship mentoring plan" | `domain-science/lab-operations-mentorship/science_lab_culture_charter.md` / `science_undergraduate_research_mentoring_plan.md` / `science_research_internship_project_scope.md` |
| "Press release / media prep / op-ed / policy brief / testimony" | `domain-science/public-engagement/science_press_release_drafter.md` (+ media_interview_prep, op_ed_drafter, policy_brief_drafter, congressional_or_parliamentary_testimony_prep) |
| "Social-media thread / lay explainer / misinformation response" | `domain-science/public-engagement/science_social_media_thread_drafter.md` / `science_explainer_for_general_audience.md` / `science_misinformation_response_drafter.md` |
| "Authentic-research lab course / methods syllabus / journal club" | `domain-science/teaching-research-methods/science_undergraduate_lab_course_designer.md` / `science_research_methods_syllabus_designer.md` / `science_journal_club_facilitation_guide.md` |
| "Science-specific code review / data-analysis or reproducibility workshop" | `domain-science/teaching-research-methods/science_code_review_for_science_software.md` / `science_data_analysis_workshop_designer.md` / `science_reproducibility_workshop_designer.md` |
| "Discipline-specific study design (genomics, chemistry, neuro, etc.)" | `domain-science/disciplines/` |
| "Career/self-improvement" | `domain-personal-development/` |
| "Vague goal → owned project" | `domain-personal-development/prompts/agency/agency_project_ownership_converter.md` |
| "What's my next concrete action?" | `domain-personal-development/prompts/agency/agency_next_action_spec.md` |
| "Diagnose stuckness" | `domain-personal-development/prompts/agency/agency_stuck_diagnosis.md` |
| "Planning instead of executing" | `domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md` |
| "Design a short ship sprint" | `domain-personal-development/prompts/agency/agency_ship_sprint_design.md` |
| "End-of-session review" | `domain-personal-development/prompts/agency/agency_end_of_session_review.md` |
| "Weekly review" | `domain-personal-development/prompts/agency/agency_weekly_review.md` |
| "Proof-of-work portfolio" | `domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md` |
| "Feedback on shipped work" | `domain-personal-development/prompts/agency/agency_feedback_extraction.md` |
| "Skill gap blocking a project" | `domain-personal-development/prompts/agency/agency_skill_gap_reframe.md` |
| "Repair a broken habit" | `domain-personal-development/prompts/agency/agency_habit_loop_repair.md` |
| "Foundation-building session" | `domain-personal-development/prompts/agency/agency_foundation_session.md` |
| "Rapid-start / 60-second start" | `domain-personal-development/prompts/agency/agency_rapid_start_mode.md` |
| "Presentation/proposal" | `domain-presentations/` |
| "Legal/trades/real estate" | `domain-specialized-fields/` or `domain-professional-writing/domain-specific/` |
| "Finance / economics field guide" | `domain-finance/` |
| **Paper-first AI investment research loop (research → patterns → screen → monitor → paper action → calibrate; gates as code-not-trust, no real-money path)** | **`ai-investment-research-toolkit/` — see [ARCHITECTURE.md](../ai-investment-research-toolkit/ARCHITECTURE.md) / [PIPELINE_OVERVIEW.md](../ai-investment-research-toolkit/PIPELINE_OVERVIEW.md)** |
| "Run a full investment-research cadence pass (Stages 0→7)" | `ai-investment-research-toolkit/orchestrator_investment_research.md` or `/investment-run` (agent `research-orchestrator`) |
| "Validate my investment config before a run" | `ai-investment-research-toolkit/prompts/stage-0-mandate-config.md` |
| "Discover / validate / retire an investment pattern (Gate A)" | `ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md` (agent `pattern-miner`) |
| "Screen the universe into a ranked watchlist" | `ai-investment-research-toolkit/prompts/stage-4-screening.md` or `/screen` |
| "Daily monitor / tripwire sweep on holdings + watchlist" | `ai-investment-research-toolkit/prompts/stage-5-monitoring-tripwires.md` or `/monitor` (agent `monitor-agent`) |
| "Decide + place a PAPER order (Gate B/C)" | `ai-investment-research-toolkit/prompts/stage-6-decision-paper-action.md` or `/decide <ticker>` |
| "Journal a prediction + Brier/calibration" | `ai-investment-research-toolkit/prompts/stage-7-journaling-calibration.md` |
| **Process bank/credit-card statements → verified, categorized, flagged spreadsheets (divorce/custody prep)** | **`domain-agentic-resources/skills/financial-records/` + `financial-records-toolkit/` — see [README](../domain-agentic-resources/skills/financial-records/README.md)** |
| "Statement PDF → Excel/CSV" | `financial-records/pdf-statement-extractor/` |
| "Verify every transaction transferred" | `financial-records/statement-reconciliation-verifier/` |
| "Categorize transactions / identify unknown merchants" | `financial-records/transaction-categorizer/` |
| "Flag transactions for divorce/custody review" | `financial-records/divorce-financial-flagger/` |
| "Run whole statement pipeline" | `/process-financials` (agent `financial-records-orchestrator`) |
| "Psychology / therapy / behavioral health" | `domain-psychology/` (see [PROMPT_INDEX.md](../domain-psychology/PROMPT_INDEX.md)) |
| **Medical / health-professions education (teach or study)** | **`domain-medical-education/` — see [README](../domain-medical-education/README.md). `educator-*` to teach and assess; `learner-*` to study. Real-patient questions → `domain-healthcare-clinical/`** |
| "Design a voice assistant, chatbot, or dialog system" | `domain-voice-conversational-ui/` — voice design, chatbot design, dialog architecture, NLU training, voice UX, multimodal, analytics |
| "Give my project memory that survives across sessions" | `continuity-kit/` — a repo-local ledger of decisions, failures, and open threads (see also `domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md` for the design decision) |
| "Drop this prompt system into another project" | `portable-prompt-system/` — self-contained export of the technique library and authoring guides |
| **Discipleship & mentorship (one-to-one formation, 73 prompts, TRADITION-NEUTRAL)** | **Use `domain-discipleship/` — see [README](../domain-discipleship/README.md). Formation is never scored; all Scripture work routes to `domain-biblical-studies/`.** |
| "Build me a full discipleship curriculum" | `domain-discipleship/curriculum-architecture/discipleship_curriculum_architecture.md` |
| "What should growth actually look like at each stage?" | `domain-discipleship/curriculum-architecture/discipleship_formation_outcomes_framework.md` |
| "What order should these discipleship topics go in?" | `domain-discipleship/curriculum-architecture/discipleship_module_scope_and_sequence.md` |
| "Is our discipleship curriculum lopsided / missing something?" | `domain-discipleship/curriculum-architecture/discipleship_curriculum_balance_audit.md` |
| "Should we use this published discipleship material?" | `domain-discipleship/curriculum-architecture/discipleship_material_evaluation.md` |
| "How do we make disciples who make disciples?" | `domain-discipleship/curriculum-architecture/discipleship_multiplication_design.md` |
| "Where am I actually at spiritually?" | `domain-discipleship/learner-pathways/discipleship_growth_self_assessment.md` |
| "What should I focus on this next season?" | `domain-discipleship/learner-pathways/discipleship_personal_growth_plan.md` |
| "I want spiritual rhythms I can actually keep" | `domain-discipleship/learner-pathways/discipleship_spiritual_practices_designer.md` |
| "I've stopped growing and I don't know why" | `domain-discipleship/learner-pathways/discipleship_stalled_growth_diagnostic.md` |
| "I've been away from church for years and want to come back" | `domain-discipleship/learner-pathways/discipleship_returning_believer_reengagement.md` |
| "I work nights / I'm a caregiver — none of these plans fit my life" | `domain-discipleship/learner-pathways/discipleship_life_constraints_adaptation.md` |
| "Am I ready to disciple someone?" | `domain-discipleship/mentor-equipping/discipleship_mentor_readiness_assessment.md` |
| "Train our mentors / disciplers" | `domain-discipleship/mentor-equipping/discipleship_mentor_training_curriculum.md` |
| "I keep trying to fix people instead of listening" | `domain-discipleship/mentor-equipping/discipleship_mentor_conversation_skills.md` |
| "When is something above my pay grade as a mentor?" | `domain-discipleship/mentor-equipping/discipleship_mentor_boundaries_and_referral.md` |
| "Our mentors are burning out / quietly dropping off" | `domain-discipleship/mentor-equipping/discipleship_mentor_support_and_sustainability.md` |
| "The discipling season is over — what did we learn?" | `domain-discipleship/mentor-equipping/discipleship_mentor_season_debrief.md` |
| "How do we match mentors with people well?" | `domain-discipleship/pairing-and-relationship/discipleship_pairing_criteria_design.md` |
| "What should a mentor and mentee agree up front?" | `domain-discipleship/pairing-and-relationship/discipleship_relationship_covenant.md` |
| "What do I say in the first mentoring meeting?" | `domain-discipleship/pairing-and-relationship/discipleship_first_meeting_guide.md` |
| "How often should we meet, and how?" | `domain-discipleship/pairing-and-relationship/discipleship_cadence_and_rhythm_design.md` |
| "This pairing isn't working / we're finished" | `domain-discipleship/pairing-and-relationship/discipleship_relationship_ending_or_transition.md` |
| "What do we actually do for an hour together?" | `domain-discipleship/session-and-lesson/discipleship_session_plan_builder.md` |
| "Build the lesson for this discipleship module" | `domain-discipleship/session-and-lesson/discipleship_lesson_builder.md` |
| "I run out of things to ask my mentee" | `domain-discipleship/session-and-lesson/discipleship_conversation_question_bank.md` |
| "My mentee just told me something heavy" | `domain-discipleship/session-and-lesson/discipleship_hard_conversation_navigation.md` |
| "We want to disciple as a group of three or four" | `domain-discipleship/session-and-lesson/discipleship_small_group_discipleship_format.md` |
| "Set up a whole discipleship pairing program" | `domain-discipleship/program-operations/discipleship_program_design_blueprint.md` |
| "What are our safeguarding and conduct rules?" | `domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md` |
| "How do we onboard people on both sides?" | `domain-discipleship/program-operations/discipleship_participant_onboarding_design.md` |
| "Half our discipleship pairs went quiet" | `domain-discipleship/program-operations/discipleship_program_health_review.md` |
| "More people want mentors than we have mentors" | `domain-discipleship/program-operations/discipleship_mentor_pipeline_and_capacity.md` |
| "Build the discipleship module on money and giving" | `domain-discipleship/topical-modules/discipleship_module_money_and_generosity.md` |
| "Build the module on work, calling, and vocation" | `domain-discipleship/topical-modules/discipleship_module_work_and_vocation.md` |
| "We have to teach on sexuality and singleness" | `domain-discipleship/topical-modules/discipleship_module_sexuality_and_singleness.md` |
| "They were badly hurt and everyone wants them to reconcile" | `domain-discipleship/topical-modules/discipleship_module_forgiveness_and_reconciliation.md` |
| "How do we handle suffering without explaining it away?" | `domain-discipleship/topical-modules/discipleship_module_suffering_and_lament.md` |
| "Our people either avoid conflict or blow up in it" | `domain-discipleship/topical-modules/discipleship_module_anger_and_conflict.md` |
| "Phones, feeds, and what they're forming in us" | `domain-discipleship/topical-modules/discipleship_module_digital_life.md` |
| "Being known as a Christian costs something real here" | `domain-discipleship/topical-modules/discipleship_module_witness_in_hostile_setting.md` |
| "Design our teen discipleship track" | `domain-discipleship/life-stage-tracks/discipleship_track_youth_and_teen.md` |
| "Students who leave after three years" | `domain-discipleship/life-stage-tracks/discipleship_track_college_and_young_adult.md` |
| "Disciple married couples without becoming their counselors" | `domain-discipleship/life-stage-tracks/discipleship_track_married_couples.md` |
| "Disciple parents without grading them by their kids" | `domain-discipleship/life-stage-tracks/discipleship_track_parents.md` |
| "Our older adults are treated as recipients of ministry" | `domain-discipleship/life-stage-tracks/discipleship_track_seniors.md` |
| "Discipleship inside a prison, and after release" | `domain-discipleship/context-variants/discipleship_context_prison_and_reentry.md` |
| "Run this on campus, inside the institution's rules" | `domain-discipleship/context-variants/discipleship_context_campus_ministry.md` |
| "A group at work — and I manage some of them" | `domain-discipleship/context-variants/discipleship_context_workplace_and_marketplace.md` |
| "Everyone's in a different country and time zone" | `domain-discipleship/context-variants/discipleship_context_remote_and_diaspora.md` |
| "Prepare someone for baptism" | `domain-discipleship/initiation-and-catechesis/discipleship_baptism_preparation.md` |
| "Prepare someone for membership — and tell them what they're agreeing to" | `domain-discipleship/initiation-and-catechesis/discipleship_membership_preparation.md` |
| "Build our catechesis" | `domain-discipleship/initiation-and-catechesis/discipleship_catechesis_design.md` |
| "I'm discipling someone whose culture and language I don't share" | `domain-discipleship/cross-cultural/discipleship_crosscultural_relationship.md` |
| "They don't read, or don't prefer to" | `domain-discipleship/cross-cultural/discipleship_oral_preference_learners.md` |
| "Our discipleship material is being translated" | `domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md` |
| "Our mentors need a peer group of their own" | `domain-discipleship/peer-and-accountability/discipleship_peer_cohort_curriculum.md` |
| "How do I actually run the mentors' meeting?" | `domain-discipleship/peer-and-accountability/discipleship_peer_cohort_facilitation.md` |
| "Two friends want to keep each other accountable" | `domain-discipleship/peer-and-accountability/discipleship_accountability_partnership_design.md` |
| "Our accountability has turned into interrogation" | `domain-discipleship/peer-and-accountability/discipleship_accountability_conversation_structure.md` |
| "I was badly hurt by a mentor before, and someone's asked me again" | `domain-discipleship/after-harm/discipleship_harmed_by_previous_discipling.md` |
| "She can't make a decision without checking with me first" | `domain-discipleship/after-harm/discipleship_dependency_and_over_attachment.md` |
| "I said something I shouldn't have and now he's gone quiet" | `domain-discipleship/after-harm/discipleship_mentor_own_mistake_repair.md` |
| "We've had to remove a mentor — what do we say to everyone else?" | `domain-discipleship/after-harm/discipleship_after_mentor_is_removed.md` |
| "I'm stuck with someone I'm discipling and need to talk to somebody" | `domain-discipleship/mentor-equipping/discipleship_mentor_case_consultation.md` |
| "He's losing his faith and I don't know how to be in the room" | `domain-discipleship/mentor-equipping/discipleship_mentor_posture_in_doubt_and_deconstruction.md` |
| "There's no program — we're just two people meeting" | `domain-discipleship/pairing-and-relationship/discipleship_informal_pairing_no_program.md` |
| "Someone's offered to disciple me and I don't know what's normal" | `domain-discipleship/pairing-and-relationship/discipleship_what_to_expect_as_mentee.md` |
| "We've been meeting for four years and nobody knows why any more" | `domain-discipleship/pairing-and-relationship/discipleship_long_relationship_recontracting.md` |
| "I'm bivocational with three pairs — what do I actually need?" | `domain-discipleship/program-operations/discipleship_minimum_viable_program.md` |
| "Is our own program putting pressure on people?" | `domain-discipleship/program-operations/discipleship_program_control_drift_audit.md` |
| "Our sessions don't work for everyone in the room" | `domain-discipleship/session-and-lesson/discipleship_session_accessibility_design.md` |
| "We've multiplied three generations out and nobody knows what's being taught" | `domain-discipleship/curriculum-architecture/discipleship_multiplication_governance_drift.md` |
| **Biblical Studies (Bible study & research, 129 prompts, TRADITION-NEUTRAL)** | **Use `domain-biblical-studies/` — see [README](../domain-biblical-studies/README.md)** |
| "Exegete / work through this passage" | `domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md` |
| "Do a Greek/Hebrew word study" | `domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md` |
| "What genre is this / how do I read it?" | `domain-biblical-studies/exegesis-interpretation/biblical_genre_aware_reading.md` |
| "Historical/cultural background of a passage" | `domain-biblical-studies/exegesis-interpretation/biblical_historical_cultural_context.md` |
| "Ancient Near Eastern parallels to this text" | `domain-biblical-studies/exegesis-interpretation/biblical_ane_comparative_context.md` |
| "How does this fit its context/structure?" | `domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md` |
| "How is this biblical story told? (character/plot/narrator)" | `domain-biblical-studies/exegesis-interpretation/biblical_narrative_analysis.md` |
| "Rhetorical devices / persuasive strategy in a passage" | `domain-biblical-studies/exegesis-interpretation/biblical_rhetorical_analysis.md` |
| "Trace canonical/intertextual connections" | `domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md` |
| "I'm new — what does this passage say?" | `domain-biblical-studies/exegesis-interpretation/biblical_passage_observation_beginner.md` |
| "What are the different interpretations of this verse?" | `domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md` |
| "Why do translations differ here?" | `domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md` |
| "Run an inductive (OIA) study" | `domain-biblical-studies/study-methods-teaching/biblical_inductive_study_method.md` |
| "SOAP / quick daily study method" | `domain-biblical-studies/study-methods-teaching/biblical_soap_devotional_method.md` |
| "Overview of a whole book" | `domain-biblical-studies/study-methods-teaching/biblical_book_overview_synthesis.md` |
| "Discussion questions for my small group" | `domain-biblical-studies/study-methods-teaching/biblical_smallgroup_discussion_guide.md` |
| "Build a lesson plan / Sunday-school class" | `domain-biblical-studies/study-methods-teaching/biblical_lesson_plan_builder.md` |
| "Help me memorize Scripture" | `domain-biblical-studies/study-methods-teaching/biblical_memorization_retention_plan.md` |
| "Study a theme/topic across passages" | `domain-biblical-studies/study-methods-teaching/biblical_thematic_topical_study.md` |
| "Design a Bible reading plan" | `domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md` |
| "Prep an expository sermon" | `domain-biblical-studies/sermon-devotional/biblical_expository_sermon_prep.md` |
| "Find an illustration for this point" | `domain-biblical-studies/sermon-devotional/biblical_sermon_illustration_finder.md` |
| "Write a daily devotional" | `domain-biblical-studies/sermon-devotional/biblical_daily_devotional_writer.md` |
| "Guide me in meditating on a passage" | `domain-biblical-studies/sermon-devotional/biblical_meditation_reflection_guide.md` |
| "Prayer / journaling prompts" | `domain-biblical-studies/sermon-devotional/biblical_prayer_journaling_prompts.md` |
| "Plan a sermon/teaching series" | `domain-biblical-studies/sermon-devotional/biblical_sermon_series_planner.md` |
| "How do I apply this text today?" | `domain-biblical-studies/sermon-devotional/biblical_application_bridge_builder.md` |
| "What does Scripture teach about [topic]?" | `domain-biblical-studies/theology-research/biblical_topical_theology_synthesis.md` |
| "Study a doctrine across traditions" | `domain-biblical-studies/theology-research/biblical_doctrine_study_neutral.md` |
| "Compare views on a disputed question" | `domain-biblical-studies/theology-research/biblical_interpretive_views_comparison.md` |
| "Map cross-references / typology" | `domain-biblical-studies/theology-research/biblical_crossreference_typology_map.md` |
| "Help with a difficult/'problem' passage" | `domain-biblical-studies/theology-research/biblical_difficult_passage_analysis.md` |
| "Build a background research brief" | `domain-biblical-studies/theology-research/biblical_background_research_brief.md` |
| "Trace a theme across the canon" | `domain-biblical-studies/theology-research/biblical_theme_canonical_trajectory.md` |
| "Check an interpretation for exegetical fallacies" | `domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md` |
| "Evaluate / compare commentaries" | `domain-biblical-studies/theology-research/biblical_commentary_evaluation.md` |
| "How do I interpret this parable?" | `domain-biblical-studies/exegesis-interpretation/biblical_parable_interpretation.md` |
| "How do I read prophecy / apocalyptic?" | `domain-biblical-studies/exegesis-interpretation/biblical_prophecy_apocalyptic_interpretation.md` |
| "How do I read this psalm / Hebrew poetry?" | `domain-biblical-studies/exegesis-interpretation/biblical_hebrew_poetry_psalms_reading.md` |
| "How do I read Proverbs / Job / Ecclesiastes?" | `domain-biblical-studies/exegesis-interpretation/biblical_wisdom_literature_reading.md` |
| "How do I read Old Testament law?" | `domain-biblical-studies/exegesis-interpretation/biblical_law_torah_reading.md` |
| "Trace the argument of an epistle" | `domain-biblical-studies/exegesis-interpretation/biblical_epistle_argument_tracing.md` |
| "Prep a topical / evangelistic / occasional sermon" | `domain-biblical-studies/sermon-devotional/biblical_topical_sermon_prep.md` (+ evangelistic, occasional) |
| "Convert a sermon outline to a full manuscript" | `domain-biblical-studies/sermon-devotional/biblical_sermon_manuscript_draft.md` |
| "Self-coach sermon delivery (pacing, nerves, self-assessment)" | `domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md` |
| "Devotional series following the liturgical calendar (Advent/Lent/Eastertide)" | `domain-biblical-studies/sermon-devotional/biblical_liturgical_calendar_devotional_series.md` |
| "Sermon from lectionary readings" | `domain-biblical-studies/sermon-devotional/biblical_lectionary_sermon_prep.md` |
| **Biblical Studies — self-directed learner (S)** | **`domain-biblical-studies/learner-self-study/` — not counseling/crisis support** |
| "Design my own multi-week study plan" | `domain-biblical-studies/learner-self-study/biblical_learner_self_directed_study_plan.md` |
| "Study a Bible character on my own" | `domain-biblical-studies/learner-self-study/biblical_learner_character_study_guide.md` |
| "Quiz me on my supplied text / check my comprehension" | `domain-biblical-studies/learner-self-study/biblical_learner_self_quiz_recall_drill.md` (+ comprehension_self_check) |
| "Explore a doctrine for myself across traditions" | `domain-biblical-studies/learner-self-study/biblical_learner_doctrine_self_exploration.md` |
| "Work through honest questions / doubts about a text" | `domain-biblical-studies/learner-self-study/biblical_learner_honest_questions_doubt_explorer.md` |
| "Learn to use study tools responsibly" | `domain-biblical-studies/learner-self-study/biblical_learner_study_tool_skill_builder.md` |
| "Derive personal application / reflective journaling" | `domain-biblical-studies/learner-self-study/biblical_learner_personal_application_worksheet.md` (+ reflection_journal_companion) |
| "Build a sustainable daily Bible reading habit" | `domain-biblical-studies/learner-self-study/biblical_learner_bible_reading_habit_builder.md` |
| "Extended multi-week deep dive into a single book" | `domain-biblical-studies/learner-self-study/biblical_learner_book_of_the_bible_deep_dive.md` |
| "Compare how traditions approach a practice (baptism, communion, etc.)" | `domain-biblical-studies/learner-self-study/biblical_learner_compare_traditions_on_practice.md` |
| **Biblical Studies — ministry-context teacher (M)** | **`domain-biblical-studies/ministry-contexts/` — child-safety + care guardrails** |
| "Build a kids' / youth Bible lesson" | `domain-biblical-studies/ministry-contexts/biblical_ministry_kids_bible_lesson_builder.md` (+ youth) |
| "New-believer discipleship path / seeker intro to the Bible" | `domain-biblical-studies/ministry-contexts/biblical_ministry_new_believer_discipleship_path.md` (+ seeker_intro) |
| "Family devotions / VBS-camp-retreat session" | `domain-biblical-studies/ministry-contexts/biblical_ministry_family_devotions_designer.md` (+ special_program) |
| "Frame a Scripture-rooted care conversation (NOT therapy)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_care_conversation_foundations.md` |
| "Design a men's or women's Bible study (tradition-neutral on gender roles)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_mens_womens_study_designer.md` |
| "Design a college / young-adult study (identity, doubt, vocation)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_college_young_adult_study.md` |
| "Design a seniors Bible study (legacy, loss, hope, accessibility)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_seniors_study_designer.md` |
| **Biblical Studies — church staff & ministry ops (P/G)** | **`domain-biblical-studies/church-staff-ministry-ops/` — operational workflows for teaching ministries** |
| "Multi-quarter curriculum scope and sequence" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md` |
| "Evaluate a published curriculum against criteria" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md` |
| "Design a teacher/volunteer training plan" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_teacher_training_plan.md` |
| "Coordinate teaching across services/campuses" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_multi_service_coordination.md` |
| "Map the annual preaching/teaching calendar" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_annual_teaching_calendar.md` |
| "Design volunteer roles with onboarding" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md` |
| "Design a small-group launch system" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md` |
| "Design a congregation-wide discipleship pathway" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md` |
| "Design a sustainable midweek program" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_midweek_program_design.md` |
| "Post-sermon debrief and feedback" | `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_sermon_feedback_debrief.md` |
| **Biblical Studies — group-leader facilitation (G/P)** | **`domain-biblical-studies/group-leader-facilitation/` — real facilitation challenges** |
| "Manage silence, dominance, tangents, conflict in group" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_facilitation_dynamics.md` |
| "Respond when you can't answer a question or topic is controversial" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_handling_hard_questions.md` |
| "Gracious response to a heretical claim in group" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_heretical_claim_response.md` |
| "Adapt study for mixed spiritual maturity" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_mixed_maturity_leveling.md` |
| "Navigate theological disagreement or personality clash" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_conflict_resolution.md` |
| "Adapt Bible study for hybrid or online delivery" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_hybrid_online_format.md` |
| "Develop an apprentice group leader" | `domain-biblical-studies/group-leader-facilitation/biblical_groupleader_apprentice_development.md` |
| **Biblical Studies — original languages (all STRONG-GUARD)** | **`domain-biblical-studies/original-languages/` — everything verify-required** |
| "Parse / verify a Greek or Hebrew form" | `domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md` |
| "Analyze Greek / Hebrew syntax" | `domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md` (+ hebrew_syntax) |
| "Greek verbal aspect vs. 'tense' / Aktionsart" | `domain-biblical-studies/original-languages/biblical_language_greek_verbal_aspect_analysis.md` |
| "Greek middle/passive voice / is this 'deponent'?" | `domain-biblical-studies/original-languages/biblical_language_greek_voice_deponency_analysis.md` |
| "Discourse / clause-flow analysis" | `domain-biblical-studies/original-languages/biblical_language_discourse_analysis.md` |
| "Is this phrase an idiom / figure of speech?" | `domain-biblical-studies/original-languages/biblical_language_idiom_and_figures_of_speech_analysis.md` |
| "Which sense fits / semantic domains (Louw-Nida)?" | `domain-biblical-studies/original-languages/biblical_language_semantic_domains_analysis.md` |
| "How does this NT text use the OT (MT/LXX/NT)?" | `domain-biblical-studies/original-languages/biblical_language_ot_in_nt_usage.md` |
| "MT vs. LXX divergences and theological significance" | `domain-biblical-studies/original-languages/biblical_language_septuagint_usage.md` |
| "How does textual criticism work for a specific variant?" | `domain-biblical-studies/original-languages/biblical_language_textual_criticism_primer.md` |
| "What does this Qere/Ketiv or Masoretic note mean?" | `domain-biblical-studies/original-languages/biblical_language_hebrew_masora_and_variants_analysis.md` |
| "Hebrew cantillation (te'amim) / Greek accentuation" | `domain-biblical-studies/original-languages/biblical_language_hebrew_greek_accentuation.md` |
| "Analyze Aramaic sections (Daniel 2-7, Ezra 4-7, etc.)" | `domain-biblical-studies/original-languages/biblical_language_aramaic_analysis.md` |
| "Where do canons and verse numbering diverge across traditions?" | `domain-biblical-studies/original-languages/biblical_language_canon_versification_differences.md` |
| "Does this Ugaritic/Akkadian/Arabic cognate argument hold up?" | `domain-biblical-studies/original-languages/biblical_language_comparative_semitics_cognate_analysis.md` |
| "Koine register / papyri / inscriptions evidence" | `domain-biblical-studies/original-languages/biblical_language_koine_papyri_register.md` |
| "Build a frequency-based Greek/Hebrew vocabulary study plan" | `domain-biblical-studies/original-languages/biblical_language_greek_hebrew_vocabulary_builder.md` |
| **Biblical Studies — biblical theology method (A/P)** | **`domain-biblical-studies/biblical-theology-method/` — method-level, above exegesis, below systematics** |
| "Clarify biblical vs. systematic theology with a worked example" | `domain-biblical-studies/biblical-theology-method/biblical_method_biblical_vs_systematic_theology.md` |
| "Read a passage within creation-fall-redemption-consummation" | `domain-biblical-studies/biblical-theology-method/biblical_method_redemptive_historical_reading.md` |
| "Compare two biblical authors' theologies" | `domain-biblical-studies/biblical-theology-method/biblical_method_author_theology_comparison.md` |
| "Survey the 'center of biblical theology' debate" | `domain-biblical-studies/biblical-theology-method/biblical_method_center_of_theology_debate.md` |
| **Biblical Studies — theology research additions** | **`domain-biblical-studies/theology-research/` — STRONG-GUARD on all three** |
| "Analyze a creed or confession against biblical texts" | `domain-biblical-studies/theology-research/biblical_theology_creed_confession_analysis.md` |
| "Biblical basis for a specific worship practice across traditions" | `domain-biblical-studies/theology-research/biblical_theology_worship_practice_biblical_basis.md` |
| "NT material on church government / how polity systems claim biblical warrant" | `domain-biblical-studies/theology-research/biblical_theology_church_government_polity.md` |
| **Biblical Studies — ministry-contexts cross-domain bridges** | **`domain-biblical-studies/ministry-contexts/` — cross-links domain-psychology/, domain-parenting/** |
| "Scripture for grief and loss (honest about lament; route-to-professional)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_grief_and_loss_scripture_guide.md` |
| "Couples' Bible study (patriarchal context, gender-role texts handled honestly)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_marriage_enrichment_study.md` |
| "Parenting passages contextualized (no proof-texting Proverbs)" | `domain-biblical-studies/ministry-contexts/biblical_ministry_parenting_scripture_guide.md` |
| **Biblical Studies — apologetics & engagement (P/A)** | **`domain-biblical-studies/apologetics-engagement/` — all STRONG-GUARD except conversation prep** |
| "Charitable engagement with a specific intellectual objection" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_objection_engagement.md` |
| "Evidence for/challenges to biblical reliability" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_bible_reliability.md` |
| "Compare biblical worldview with another on a specific question" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_comparative_worldview.md` |
| "Frame a faith-and-science question with believing-scholar positions" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_faith_and_science.md` |
| "Prepare for a real apologetic conversation" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_conversation_prep.md` |
| "Present major theodicies and strongest objections fairly" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_problem_of_evil_theodicy.md` |
| "Address an alleged biblical contradiction honestly" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_biblical_contradictions.md` |
| "Interfaith dialogue prep (never fabricate claims about another religion)" | `domain-biblical-studies/apologetics-engagement/biblical_apologetics_other_religions_dialogue.md` |
| **Legal (practitioner library, 109 prompts)** | **Use `domain-legal/` — see [README](../domain-legal/README.md)** |
| "Spot legal issues / IRAC memo / statutory interpretation" | `domain-legal/research/` |
| "Draft a complaint / answer / MTD / MSJ / jury instructions" | `domain-legal/litigation/` |
| "Motion in limine set / litigation budget / trial theme" | `domain-legal/litigation/` (Phase 2A) |
| "RFPs / interrogatories / privilege log / meet-and-confer / privilege review protocol" | `domain-legal/discovery/` |
| "Deposition outlines / summaries / witness prep / expert depositions" | `domain-legal/depositions/` |
| "Contract review / redline / risk heatmap" | `domain-legal/contracts-transactional/` |
| "Draft MSA / SOW / NDA / DPA / SaaS / License" | `domain-legal/contracts-transactional/` |
| "Term sheet to definitive / clause library / negotiation position" | `domain-legal/contracts-transactional/` |
| "Buy-side DD / findings memo / disclosure schedule / board resolutions" | `domain-legal/corporate-ma/` |
| "§409A or QSBS issue spotter / post-closing integration" | `domain-legal/corporate-ma/` |
| "Offer + separation / workplace investigation / PIP risk / EEOC" | `domain-legal/employment-labor/` |
| "Wage-hour classification / non-compete enforceability" | `domain-legal/employment-labor/` |
| "Patent claim chart / trademark clearance / fair use / DMCA / OSS license" | `domain-legal/ip/` |
| "Matter intake / engagement letter / demand letter / client status update" | `domain-legal/client-intake-communications/` |
| "Executive matter summary / legal spend review / playbook / intake triage / board update" | `domain-legal/in-house-legalops/` |
| **Divorce / dissolution (22 prompts)** | **Use `domain-legal/divorce/` — see [README](../domain-legal/README.md)** |
| "Divorce intake / case assessment" | `domain-legal/divorce/legal_divorce_intake_and_case_assessment.md` |
| "Draft a divorce petition / response / counterpetition" | `domain-legal/divorce/` |
| "Temporary / pendente lite orders" | `domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md` |
| "Financial affidavit / disclosure" | `domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md` |
| "Property characterization (marital vs. separate) / tracing" | `domain-legal/divorce/legal_marital_property_characterization_analysis.md` |
| "Property division / equalization proposal" | `domain-legal/divorce/legal_property_division_and_equalization_proposal.md` |
| "Business valuation & division / goodwill" | `domain-legal/divorce/legal_business_valuation_and_division_framework.md` |
| "Retirement division / QDRO" | `domain-legal/divorce/legal_retirement_division_and_qdro_framework.md` |
| "Hidden assets / dissipation / forensic" | `domain-legal/divorce/legal_hidden_asset_and_dissipation_investigation.md` |
| "Divorce tax consequences (§1041 / alimony / dependency)" | `domain-legal/divorce/legal_divorce_tax_consequences_analysis.md` |
| "Spousal support / alimony / maintenance" | `domain-legal/divorce/legal_spousal_support_alimony_analysis.md` |
| "Marital settlement agreement (MSA)" | `domain-legal/divorce/legal_marital_settlement_agreement_drafter.md` |
| "Divorce mediation / financial settlement prep" | `domain-legal/divorce/legal_divorce_settlement_and_mediation_prep.md` |
| "Divorce mediation brief / statement" | `domain-legal/divorce/legal_divorce_mediation_brief_drafter.md` |
| "Memorialize a mediated deal (term sheet / MOU)" | `domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md` |
| "Prenup / postnup drafting" | `domain-legal/divorce/legal_prenuptial_postnuptial_agreement_drafter.md` |
| "Prenup / postnup enforceability" | `domain-legal/divorce/legal_prenup_postnup_enforceability_analysis.md` |
| "Divorce discovery / trial prep / post-judgment" | `domain-legal/divorce/` |
| "DV protective / restraining order petition" | `domain-legal/divorce/legal_domestic_violence_protective_order_petition.md` |
| **Custody / parenting (20 prompts)** | **Use `domain-legal/custody/` — see [README](../domain-legal/README.md)** |
| "Best-interests custody analysis" | `domain-legal/custody/legal_custody_best_interests_analysis.md` |
| "Which state has custody jurisdiction (UCCJEA)" | `domain-legal/custody/legal_uccjea_jurisdiction_analysis.md` |
| "Draft a custody petition / motion" | `domain-legal/custody/legal_custody_petition_or_motion_drafter.md` |
| "Emergency / temporary custody motion" | `domain-legal/custody/legal_temporary_and_emergency_custody_motion.md` |
| "Parenting plan / holiday schedule / high-conflict provisions" | `domain-legal/custody/` |
| "Calculate child support" | `domain-legal/custody/legal_child_support_calculation_framework.md` |
| "Modify custody / parenting time" | `domain-legal/custody/legal_custody_modification_analysis_and_motion.md` |
| "Relocation / move-away analysis" | `domain-legal/custody/legal_relocation_move_away_analysis.md` |
| "Custody evaluation / GAL report response" | `domain-legal/custody/` |
| "Grandparent / third-party custody or visitation" | `domain-legal/custody/legal_third_party_custody_visitation_analysis.md` |
| "Supervised visitation / safety plan" | `domain-legal/custody/legal_supervised_visitation_and_safety_plan.md` |
| "Enforce parenting time / contempt" | `domain-legal/custody/legal_parenting_time_enforcement_and_contempt_motion.md` |
| "Custody trial prep / factor proof plan" | `domain-legal/custody/legal_custody_trial_prep_and_factor_proof_plan.md` |
| "Establish paternity / parentage" | `domain-legal/custody/legal_paternity_parentage_establishment_and_custody.md` |
| "Custody mediation / settlement prep" | `domain-legal/custody/legal_custody_settlement_and_mediation_prep.md` |
| "Custody mediation brief / statement" | `domain-legal/custody/legal_custody_mediation_brief_drafter.md` |
| "Custody mediation stalled — impasse / package strategy" | `domain-legal/custody/legal_custody_mediation_impasse_and_package_strategy.md` |
| **Family law — self-represented / self-organizing LITIGANT (organize your own side; NOT legal advice)** | **Use `domain-legal/family-self-advocacy/` — see [README](../domain-legal/family-self-advocacy/README.md)** |
| "Organize my whole divorce/custody case for my lawyer" | `domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md` |
| "Build a neutral dated timeline of events" | `domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md` |
| "Organize / index my evidence and exhibits" | `domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md` |
| "Compile texts/emails into a clean record for court" | `domain-legal/family-self-advocacy/legalprep_communication_record_compiler.md` |
| "Document a recalled incident factually" | `domain-legal/family-self-advocacy/legalprep_incident_documentation_organizer.md` |
| "Map witnesses/documents to the facts they support" | `domain-legal/family-self-advocacy/legalprep_witness_and_source_map.md` |
| "Get ready for my financial disclosure / affidavit" | `domain-legal/family-self-advocacy/legalprep_financial_disclosure_organizer.md` |
| "Inventory marital & separate assets and debts" | `domain-legal/family-self-advocacy/legalprep_asset_and_debt_inventory.md` |
| "Build a budget for support / needs discussions" | `domain-legal/family-self-advocacy/legalprep_monthly_budget_and_expense_worksheet.md` |
| "Checklist of financial documents to collect" | `domain-legal/family-self-advocacy/legalprep_financial_document_gathering_checklist.md` |
| "Respond to allegations with facts, not argument" | `domain-legal/family-self-advocacy/legalprep_allegation_response_organizer.md` |
| "Write a neutral factual account for my attorney" | `domain-legal/family-self-advocacy/legalprep_my_account_factual_statement.md` |
| "Organize genuine concerns about the other party for counsel" | `domain-legal/family-self-advocacy/legalprep_concerns_about_other_party_organizer.md` |
| "Prepare for a family-court hearing (as a litigant)" | `domain-legal/family-self-advocacy/legalprep_hearing_preparation_organizer.md` |
| "Practice answering questions truthfully and calmly" | `domain-legal/family-self-advocacy/legalprep_testimony_practice_factual_recall.md` |
| "Prepare for my deposition (as the litigant)" | `domain-legal/family-self-advocacy/legalprep_deposition_preparation_organizer.md` |
| "Explain the family-court process and roles to me" | `domain-legal/family-self-advocacy/legalprep_court_process_explainer.md` |
| "Prepare for mediation / settlement talks (my side)" | `domain-legal/family-self-advocacy/legalprep_mediation_preparation_organizer.md` |
| "Understand a mediation agreement before I sign" | `domain-legal/family-self-advocacy/legalprep_mediation_agreement_review_organizer.md` |
| "Capture what happened in a mediation session" | `domain-legal/family-self-advocacy/legalprep_post_mediation_follow_up_organizer.md` |
| "Questions to ask at my attorney consultation" | `domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md` |
| "Prepare for a custody evaluation / GAL interview" | `domain-legal/family-self-advocacy/legalprep_custody_evaluation_preparation_organizer.md` |
| "Map my facts to best-interests factor categories" | `domain-legal/family-self-advocacy/legalprep_best_interests_factor_self_map.md` |
| **Personal legal self-advocacy — NON-family (layperson; organize/prepare your own side — not legal advice)** | **Use `domain-legal/personal-self-advocacy/` — see [README](../domain-legal/personal-self-advocacy/README.md)** |
| "Which professional or authority do I even need?" | `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` |
| "Assemble a package for my attorney / the authority" | `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md` |
| "Preserve and inventory my (digital) evidence" | `domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md` |
| "Document a workplace concern (harassment/discrimination/retaliation)" | `domain-legal/personal-self-advocacy/workplace/legalprep_workplace_concern_documentation_organizer.md` |
| "Draft my own internal HR complaint" | `domain-legal/personal-self-advocacy/workplace/legalprep_hr_complaint_narrative_preparer.md` |
| "Organize facts for an EEOC / agency intake" | `domain-legal/personal-self-advocacy/workplace/legalprep_eeoc_agency_charge_preparation_organizer.md` |
| "Log harassment / stalking incidents (safety-forward)" | `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_harassment_stalking_incident_log.md` |
| "Organize my account for a protective-order request" | `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_protective_order_preparation_organizer.md` |
| "Prepare my own account for a police report" | `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_police_report_account_preparer.md` |
| "Draft my own cyberharassment report to a platform" | `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_cyberharassment_platform_report_preparer.md` |
| "Document a false statement made about me (defamation)" | `domain-legal/personal-self-advocacy/defamation-reputation/legalprep_defamation_concern_documentation_organizer.md` |
| "Draft my own correction / retraction request" | `domain-legal/personal-self-advocacy/defamation-reputation/legalprep_correction_retraction_request_preparer.md` |
| "Document my stolen / infringed work (IP)" | `domain-legal/personal-self-advocacy/ip-theft/legalprep_ip_infringement_documentation_organizer.md` |
| "Draft my own DMCA takedown notice (I sign it)" | `domain-legal/personal-self-advocacy/ip-theft/legalprep_dmca_takedown_notice_preparer.md` |
| "Report a scam / fraud (FTC / IC3 / bank)" | `domain-legal/personal-self-advocacy/consumer-scams/legalprep_scam_fraud_report_preparer.md` |
| "Document a tenant issue / draft a deposit-dispute letter" | `domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_security_deposit_dispute_preparer.md` |
| "Document identity theft + prepare my reports" | `domain-legal/personal-self-advocacy/identity-theft/legalprep_identity_theft_report_preparer.md` |
| "Draft my own debt-validation / dispute letter" | `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` |
| "Organize / prepare for my small-claims case" | `domain-legal/personal-self-advocacy/small-claims/legalprep_small_claims_case_preparation_organizer.md` |
| **Parenting (ages 4–8)** | **Use `domain-parenting/` — see README for full map** |
| "Tantrum / meltdown" | `domain-parenting/parenting_meltdown_response_script.md` |
| "Why is my kid doing this?" / behavior function | `domain-parenting/parenting_behavior_function_decoder.md` |
| "Is this normal for a 5-year-old?" | `domain-parenting/parenting_developmental_expectations_4_to_8.md` |
| "I lost it / yelled / need to repair" | `domain-parenting/parenting_repair_conversation_after_rupture.md` |
| "I'm about to lose it / flooded parent" | `domain-parenting/parenting_parent_coregulation_reset.md` |
| "Should I talk to the pediatrician?" | `domain-parenting/parenting_when_to_seek_professional_help.md` |
| "ADHD kid homework / executive function" | `domain-parenting/parenting_adhd_executive_function_scaffold.md` |
| "Strong-willed / power struggle / defiance" | `domain-parenting/parenting_strong_willed_power_struggle_defuser.md` |
| "Autistic / ASD / HFA social situation" | `domain-parenting/parenting_hfa_social_situation_decoder.md` |
| "Sensory overload / sensory-sensitive kid" | `domain-parenting/parenting_sensory_at_home_toolkit.md` |
| "Parenting style / am I too strict-soft" | `domain-parenting/parenting_parenting_style_self_assessment.md` |
| "Hard conversation with my kid (death / divorce / bodies)" | `domain-parenting/parenting_hard_topics_age_appropriate_scripts.md` |
| "Morning / bedtime / after-school routine" | `domain-parenting/parenting_daily_routine_designer.md` |
| "Transitions / warnings / first-then" | `domain-parenting/parenting_transitions_and_warnings_protocol.md` |
| "Rehearse / practice parenting conversation" | `domain-parenting/parenting_scenario_simulator.md` |
| "Sibling fighting / fairness / jealousy" | `domain-parenting/parenting_sibling_conflict_coach.md` |
| "Email the teacher" | `domain-parenting/parenting_teacher_partnership_email_composer.md` |
| "504 / IEP parent prep / school accommodations" | `domain-parenting/parenting_school_accommodation_conversation_prep.md` |
| "Sticker chart / allowance / behavior contract" | `domain-parenting/parenting_reward_system_premortem.md` |
| **Separation / Divorce / Custody / Co-Parenting** | **Use `domain-parenting/caregiver-facing/{divorce,custody,co-parenting}/` — see each subdir README** |
| "How do we tell the kids we're separating?" | `domain-parenting/caregiver-facing/divorce/parenting_divorce_telling_kids_script.md` |
| "Answering kids' hard divorce questions (whose fault, getting back together)" | `domain-parenting/caregiver-facing/divorce/parenting_divorce_hard_questions_answer_bank.md` |
| "Helping kids adjust to two homes / transitions" | `domain-parenting/caregiver-facing/divorce/parenting_divorce_two_homes_transition_support.md` |
| "Keep my own grief/anger off the kids; not using them as messengers" | `domain-parenting/caregiver-facing/divorce/parenting_divorce_parent_emotional_regulation.md` |
| "Is my child coping with the divorce or do they need a therapist?" | `domain-parenting/caregiver-facing/divorce/parenting_divorce_signs_child_needs_more_support.md` |
| "Build a parenting plan I can use and show in court (NOT legal advice)" | `domain-parenting/caregiver-facing/custody/parenting_custody_parenting_plan_builder.md` |
| "Design a custody / timesharing schedule by the child's age" | `domain-parenting/caregiver-facing/custody/parenting_custody_schedule_designer_by_age.md` |
| "Holiday / vacation / summer rotation schedule" | `domain-parenting/caregiver-facing/custody/parenting_custody_holiday_vacation_schedule_builder.md` |
| "Keep a factual co-parenting communication log for records" | `domain-parenting/caregiver-facing/custody/parenting_custody_communication_log_template.md` |
| "Track shared child expenses / reimbursements" | `domain-parenting/caregiver-facing/custody/parenting_custody_expense_and_logistics_tracker.md` |
| "Plain-language explainer of plan provisions (right of first refusal, relocation)" | `domain-parenting/caregiver-facing/custody/parenting_custody_common_plan_provisions_explainer.md` |
| "Special-needs parenting-plan addendum (meds/therapy/IEP across homes)" | `domain-parenting/caregiver-facing/custody/parenting_custody_special_needs_plan_addendum.md` |
| "Articulate a child-focused proposal for mediation" | `domain-parenting/caregiver-facing/custody/parenting_custody_child_focused_proposal_articulator.md` |
| "Rewrite a message to my co-parent (BIFF / de-escalate)" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_message_composer_biff.md` |
| "Dealing with a high-conflict co-parent / parallel parenting" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_high_conflict_response_strategy.md` |
| "Consistency across two homes (rules / routines)" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_consistency_across_homes.md` |
| "Make a joint decision with my co-parent / resolve an impasse" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_shared_decision_framework.md` |
| "Am I the problem? Co-parenting self-audit" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_self_audit.md` |
| "Co-parenting with an unsafe / absent / addicted / incarcerated parent" | `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_with_unsafe_or_absent_parent.md` |
| "Performance review / employee evaluation" | `domain-hr-management/performance-reviews/` |
| "Self-review / self-assessment" | `domain-hr-management/performance-reviews/hr_self_review_assessment.md` |
| "Peer / 360 feedback" | `domain-hr-management/performance-reviews/hr_peer_360_feedback.md` |
| "Calibration / norming session" | `domain-hr-management/performance-reviews/hr_calibration_facilitator.md` |
| "Role-tailored review scaffold (meta)" | `domain-hr-management/performance-reviews/hr_performance_review_meta_prompt.md` |
| **Psychology / Therapy / Behavioral Health** | **Use `domain-psychology/` — see [`PROMPT_INDEX.md`](../domain-psychology/PROMPT_INDEX.md)** |
| "SOAP / DAP / BIRP / GIRP / PIRP progress note" | `domain-psychology/documentation/psychology_soap_progress_note.md` (and siblings) |
| "Biopsychosocial intake (90791/90792)" | `domain-psychology/documentation/psychology_intake_assessment_note.md` |
| "Initial treatment plan with golden thread" | `domain-psychology/documentation/psychology_initial_treatment_plan.md` |
| "90-day treatment plan update" | `domain-psychology/documentation/psychology_treatment_plan_update.md` |
| "Discharge / termination summary" | `domain-psychology/documentation/psychology_discharge_summary.md` / `..._termination_summary.md` |
| "Group therapy note (90853 / 90849)" | `domain-psychology/documentation/psychology_group_therapy_note.md` |
| "Collateral contact note (with ROI)" | `domain-psychology/documentation/psychology_collateral_contact_note.md` |
| "Telehealth session note (POS 10/02 + modifier 95/93)" | `domain-psychology/documentation/psychology_telehealth_session_note.md` |
| "Clinical supervision note" | `domain-psychology/documentation/psychology_supervision_note.md` |
| "Columbia C-SSRS suicide risk assessment" | `domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md` |
| "Stanley-Brown safety plan" | `domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md` |
| "CALM lethal-means counseling" | `domain-psychology/risk-crisis/psychology_lethal_means_counseling_script.md` |
| "Homicidal ideation triage" | `domain-psychology/risk-crisis/psychology_homicidal_ideation_triage.md` |
| "NSSI four-function analysis & replacement-skill plan" | `domain-psychology/risk-crisis/psychology_self_harm_functional_assessment.md` |
| "Post-attempt re-engagement plan (90-day)" | `domain-psychology/risk-crisis/psychology_post_attempt_reengagement_plan.md` |
| "Mandated reporter (CPS/APS) decision" | `domain-psychology/risk-crisis/psychology_mandated_reporter_decision_walkthrough.md` |
| "Tarasoff / duty-to-protect analysis" | `domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md` |
| "Civil commitment / involuntary hold narrative" | `domain-psychology/risk-crisis/psychology_civil_commitment_narrative.md` |
| "In-session crisis de-escalation & disposition" | `domain-psychology/risk-crisis/psychology_crisis_de_escalation_session_plan.md` |
| **Psychology — Client / Patient-Side (self-use)** | **Use `domain-psychology/client-self-use/` (Wave 5, 30 prompts)** |
| "Pre-session agenda for therapy" | `domain-psychology/client-self-use/session-prep-integration/clientself_presession_agenda_drafter.md` |
| "Post-session reflection" | `domain-psychology/client-self-use/session-prep-integration/clientself_postsession_reflection_processor.md` |
| "Stuck on therapy homework" | `domain-psychology/client-self-use/session-prep-integration/clientself_between_session_homework_helper.md` |
| "Saying a hard thing to my therapist (rehearsal)" | `domain-psychology/client-self-use/session-prep-integration/clientself_saying_hard_things_to_therapist_rehearsal.md` |
| "Asking my therapist for a change in approach" | `domain-psychology/client-self-use/session-prep-integration/clientself_asking_therapist_for_change_in_approach.md` |
| "Planning the ending-therapy conversation" | `domain-psychology/client-self-use/session-prep-integration/clientself_ending_therapy_conversation_planner.md` |
| "Anxiety vs depression vs burnout — which is this?" | `domain-psychology/client-self-use/symptom-understanding/clientself_anxiety_depression_burnout_differentiator.md` |
| "Panic attack vs heart attack reasoning" | `domain-psychology/client-self-use/symptom-understanding/clientself_panic_attack_vs_heart_attack_reasoner.md` |
| "Are these intrusive thoughts OCD?" | `domain-psychology/client-self-use/symptom-understanding/clientself_intrusive_thoughts_vs_ocd_signal.md` |
| "Hypomania self-check" | `domain-psychology/client-self-use/symptom-understanding/clientself_hypomania_self_check.md` |
| "Trauma-response pattern recognizer" | `domain-psychology/client-self-use/symptom-understanding/clientself_trauma_response_pattern_recognizer.md` |
| "Interpreting a PHQ-9 / GAD-7 / PCL-5 / AUDIT / MDQ score" | `domain-psychology/client-self-use/symptom-understanding/clientself_symptom_severity_self_screen_interpreter.md` |
| "Anxiety grounding menu (context-matched)" | `domain-psychology/client-self-use/coping-by-concern/clientself_anxiety_grounding_menu_builder.md` |
| "Personal panic plan" | `domain-psychology/client-self-use/coping-by-concern/clientself_anxiety_panic_plan_builder.md` |
| "Worry postponement protocol (CBT-GAD)" | `domain-psychology/client-self-use/coping-by-concern/clientself_anxiety_worry_postponement_protocol.md` |
| "Self-designed exposure (with my therapist)" | `domain-psychology/client-self-use/coping-by-concern/clientself_anxiety_exposure_with_therapist.md` |
| "Behavioral activation scheduler" | `domain-psychology/client-self-use/coping-by-concern/clientself_depression_behavioral_activation_scheduler.md` |
| "Rumination interrupt protocol" | `domain-psychology/client-self-use/coping-by-concern/clientself_depression_rumination_interrupt_protocol.md` |
| "Anti-avoidance prompt" | `domain-psychology/client-self-use/coping-by-concern/clientself_depression_anti_avoidance_prompt.md` |
| "OCD ERP draft (with my therapist)" | `domain-psychology/client-self-use/coping-by-concern/clientself_ocd_erp_exercise_with_therapist.md` |
| "OCD family accommodation reduction" | `domain-psychology/client-self-use/coping-by-concern/clientself_ocd_family_accommodation_reduction_plan.md` |
| "Window of tolerance check" | `domain-psychology/client-self-use/coping-by-concern/clientself_trauma_window_of_tolerance_check.md` |
| "Flashback grounding script" | `domain-psychology/client-self-use/coping-by-concern/clientself_trauma_flashback_grounding_script.md` |
| "CBT-I sleep restriction calculator" | `domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md` |
| "ADHD external scaffold designer" | `domain-psychology/client-self-use/coping-by-concern/clientself_adhd_external_scaffold_designer.md` |
| "Anger time-out script (with return contract)" | `domain-psychology/client-self-use/coping-by-concern/clientself_anger_time_out_script_builder.md` |
| "Mood tracking summarizer" | `domain-psychology/client-self-use/mood-journaling/clientself_mood_tracking_summarizer.md` |
| "Weekly emotional pattern review" | `domain-psychology/client-self-use/mood-journaling/clientself_weekly_emotional_pattern_review.md` |
| "Anti-toxic-positivity journal prompts" | `domain-psychology/client-self-use/mood-journaling/clientself_journal_prompts_anti_toxic_positivity.md` |
| "Gratitude journal with calibration" | `domain-psychology/client-self-use/mood-journaling/clientself_gratitude_journal_with_calibration.md` |

---

## Summary

**Remember the core distinctions:**

**"Create/Build a NEW prompt for X"** → Determine category:
- **Image Generation (badge buddy, infographic, diagram, worksheet image):** Build using `domain-image-generation/IMAGE_GENERATION_GUIDE.md`
- **Coding/Technical:** Build using `AI_AGENT_QUICK_START.md`
- **Non-Coding (education, writing, healthcare, business, etc.):** Build using `NON_CODING_QUICK_START.md`

**"Create/Build a SKILL for X"** → Build using authoring/skill-patterns/README.md

**"Help me with X"** → Find existing skill (domain-agentic-resources/skills/) or prompt (domain-*/...)

**"How do I / What's the best way"** → Reference documentation (guides, techniques)

**When to create a SKILL vs a PROMPT:**

**Create a SKILL when:**
- Capability will be reused across multiple sessions
- Needs bundled resources (scripts, templates, references)
- Complex multi-step workflow requiring orchestration
- Requires external tool/API integration
- Benefits from progressive disclosure (metadata → instructions → resources)

**Create a PROMPT when:**
- One-time or ad-hoc task
- No external resources needed
- Simple, focused instruction set
- Task-specific rather than capability-focused

**Quick Actions:**

| Action | Go To |
|--------|-------|
| **USE** an existing skill | `domain-agentic-resources/skills/` |
| **USE** an existing agent | `domain-agentic-resources/agents/` |
| **USE** an existing command | `domain-agentic-resources/commands/` |
| **USE** an existing persona | `domain-agentic-resources/personas/` |
| **USE** a software engineering prompt | `domain-software-engineering/` |
| **USE** a business strategy prompt | `domain-business-strategy/` |
| **USE** an engineering workflow | `domain-engineering-workflows/` |
| **USE** a productivity prompt | `domain-productivity/` |
| **USE** an image generation prompt | `domain-image-generation/` |
| **CREATE** a new coding prompt | `AI_AGENT_QUICK_START.md` |
| **CREATE** a new non-coding prompt | `NON_CODING_QUICK_START.md` |
| **CREATE** a new image generation prompt | `domain-image-generation/IMAGE_GENERATION_GUIDE.md` |
| **CREATE** a new skill | `authoring/skill-patterns/README.md` |
| **CREATE** a new agent | `authoring/agent-patterns/AGENT_QUICK_START.md` |
| **CREATE** a new command | `authoring/command-patterns/COMMAND_QUICK_START.md` |
| **DESIGN** an agentic system (manual) | `authoring/system-patterns/README.md` |
| **PRODUCE** an agentic system from a use case (guided factory) | `agentic-system-factory/` |
| **LEARN** about image generation techniques | `domain-image-generation/IMAGE_GENERATION_GUIDE.md` |
| **LEARN** about skills | `authoring/skill-patterns/templates/GOLD_STANDARD_SKILL.md` |

**Remember:** `authoring/` = authoring system (how to build), `domain-agentic-resources/` = implementation library (what's built), `domain-*/` = organized prompts by domain

This approach maximizes the value of the existing registry (see the generated counts at the top of this file) while maintaining flexibility to build custom solutions when truly needed.

---

