# Domain: Professional Writing

**Purpose:** Prompts for domain-specific professional writing, business documents, and specialized communication.

---

## What This Domain Covers

Professional writing prompts for various fields:

1. **Business Writing** - Executive briefs, status reports, proposals, PRDs, post-mortems, SOPs, technical docs
2. **Content Quality** - 19 evaluators that score a finished draft by document type
3. **Content Production** - 8 generators for channel content (scripts, hooks, SEO, repurposing, voice bible, podcast outlines and host interview prep, video shot lists), paired with the evaluators above: generate here, score there
4. **Domain-Specific** - Client-facing documents by profession: CPAs, financial advisors, contractors and trades, real estate agents, engineers, founders, and more
5. **Writing** - Essays, narratives, structured documents, news articles, interview features
6. **Journalism** - The newsroom work around a story: editor's desk edit, source verification log, investigative project plan
7. **Translation** - Human translation craft: translator brief and glossary, MQM-style quality review, transcreation of creative copy

**Start with the [field guide](field_guide.md)** for the craft behind all of it:
what makes a business document work, how each type fails, a certainty framework
for business projections, and skeleton templates for the five recurring document
types (executive proposal, PRD, status report, competitive analysis, change
communication).

---

## Directory Structure

```
domain-professional-writing/
├── field_guide.md            # Craft reference + document templates (start here)
├── business-writing/         # Executive briefs, reports, proposals, PRDs, SOPs
├── content-production/       # Generators for channel content: scripts, hooks, SEO packaging, repurposing, voice bible, podcast, video shot lists
├── content-quality/          # Slop evaluators for finished drafts
├── domain-specific/          # Profession-specific writing prompts
├── journalism/               # Desk edit, source verification log, investigative plan
├── translation/              # Human translation: brief + glossary, MQM review, transcreation
├── writing/                  # General professional writing
└── README.md
```

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `domain-specific/` | 21 | Client- and stakeholder-facing documents by profession (`domain_writing_*`). Three stubs were merged into stronger neighbours in the 2026-10 quality backfill: attorney discovery responses → `domain-legal/discovery/legal_discovery_response_objections.md`, physician SOAP note → `domain-healthcare-clinical/prompts/workflow/medicine_clinical_documentation.md`, marketing campaign → `domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md` |
| `business-writing/` | 14 | Executive brief, status report, proposal (general, executive template, client engagement, investment example), PRD, post-mortem, SOP, technical doc, meeting notes, engagement case study, testimonial/referral request, nine principles |
| `content-quality/` | 19 | `quality_slop_*` evaluators by document type (moved here from `domain-productivity/validation/`) |
| `content-production/` | 8 | `content_*` generators for channel content: long-form script, short-form hook bank, SEO title/description, one-to-many repurposing, series/channel voice bible, podcast episode outline (rundown + show notes), podcast host interview prep, video shot list and pre-production |
| `writing/` | 12 | General writing prompts, including the newsletter issue writer, an inverted-pyramid news article writer, and an interview-transcript-to-feature writer with quote-fidelity rules |
| `journalism/` | 3 | `journalism_*`: editor's story desk edit (fairness table, legal-risk flags held for a media lawyer), source verification log (people, documents, images, sourcing terms, corrections trail), investigative project plan (hypothesis, kill signals, records/data plan, no-surprises letter) |
| `translation/` | 3 | `translation_*`, human translation (not software localization): project brief and glossary, MQM-style quality review with severity scoring, transcreation brief for slogans and campaign lines |
| **Total** | **80** | |

> `business-documents/` was removed: all nine files were a stale pre-frontmatter
> mirror of `business-writing/`, whose versions are roughly twice as long.

---

## Professional Fields Covered

The `domain-specific/` directory holds one prompt per profession and document:

- **Financial and insurance:** CPA year-end tax planning letter, financial advisor quarterly review, insurance policy comparison
- **Trades and home services:** contractor remodel estimate, electrical panel upgrade, HVAC estimate, plumbing repipe, landscape proposal
- **Healthcare-adjacent:** dental treatment plan letter, veterinary surgery recommendation
- **Technology and leadership:** CTO strategy memo, engineering design doc, RFC, sales strategy, founder investor update
- **Client services:** consultant executive summary, architect RFP proposal, wedding planner proposal
- **Listings and letters:** Amazon product listing, real estate listing, school counselor recommendation

Each one names its nearest neighbour elsewhere in the repository under "Not this prompt if".

---

## Key Patterns

### Professional Voice
Each profession requires:
- Appropriate terminology
- Industry conventions
- Regulatory awareness
- Client communication style

### Document Types
- Client proposals
- Expert reports
- Professional correspondence
- Compliance documentation

---

## When to Use This Domain

Use these prompts when you need to:
- Write documents for a specific profession
- Edit a reported story, verify its sources, or plan an investigation (`journalism/`)
- Brief a translator, review a translation's quality, or adapt a slogan for another market (`translation/`)
- Create business proposals or reports
- Draft professional correspondence
- Communicate in industry-appropriate style

**Do NOT use for:**
- Creative writing (use domain-creative-writing)
- Academic writing (use domain-research-academic)
- Marketing copy — landing pages, ads, email campaigns, sales collateral
  (use `domain-agentic-resources/skills/marketing/`: `copywriting`, `ad-creative`,
  `page-cro`, `email-sequence`, `sales-enablement`)
- Advertising **images** (use `domain-advertising`, which is an image-prompt set —
  it does not hold ad copy)
- Software localization — i18n architecture, string files, translation-management
  pipelines (use `domain-software-engineering/localization/`; human translation craft
  is in `translation/` here)

---

*Consolidated here from the retired pre-reorg `prompts/non-engineering/` tree (its `domain-specific/`, `business/` and `writing_*` files), which no longer exists; the current files are the subfolders listed above.*
