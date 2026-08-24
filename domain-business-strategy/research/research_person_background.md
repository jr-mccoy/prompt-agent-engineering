---
title: "Person Background Research"
category: business-strategy/research
description: "Prepare a professional briefing on a person before a meeting, interview, or outreach — current role, career trajectory, public perspectives, and conversation starters — strictly limited to professional public information, fully sourced, with privacy boundaries enforced."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - QA-01
difficulty: beginner
tags:
  - research
  - person-research
  - meeting-prep
  - professional-briefing
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_company_deep_dive.md
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-business-strategy/research/research_industry_trends.md
---

# Person Background Research

**Objective:** Produce a concise, source-cited professional briefing on a person ahead of a meeting, interview, or outreach — their current role, career trajectory, public perspectives, and a few genuine conversation starters — using only professional, publicly available information and clearly separating fact from inference.

**When to use:**
- Pre-meeting, sales-call, or partnership-discussion preparation.
- Interview preparation (knowing your interviewer or candidate's public professional record).
- Networking-event or conference prep.

**When NOT to use:**
- The purpose is personal, not professional (this prompt excludes personal life by design).
- You need background-check-grade verification — that requires authorized, regulated services.
- The person has essentially no public professional footprint (the briefing would be padded or speculative).

**Audience:** Salespeople, founders, recruiters, BD/partnership leads, and professionals preparing for meetings.

---

## Inputs / Context

The user should supply (or the research should flag what is missing):

1. **Person's full name** and **current company** (to disambiguate).
2. **Context** of the meeting (sales, interview, partnership, networking) — focuses relevance.
3. **Available sources** the researcher can reach (LinkedIn, company bio, talks/podcasts, articles, reputable news).
4. **Recency window** for public activity (default: prefer the past 18 months).
5. Any **prior context** the user has, to avoid restating or guessing.

---

## Constraints

### Must
- Restrict strictly to **professional, publicly available information** relevant to the stated context.
- **Cite a source for every factual claim**; quotes must be **verbatim with attribution and link**.
- **Never invent** roles, employers, dates, quotes, accomplishments, or connections. If information is limited, say so rather than padding.
- Clearly **distinguish fact (what they've said/done) from inference (likely responsibilities)** and flag uncertain items with `[UNVERIFIED]`.
- Enforce **privacy boundaries**: no family, age, home location, personal social media, photos, or non-professional detail.
- If a primary source (e.g., LinkedIn) is unavailable, note it and state which alternates were used.

### Must Not
- Include or infer personal/private information.
- Fabricate a quote, a previous role, or a "mutual connection."
- Present an inferred responsibility as a confirmed fact.
- Pad a thin profile with generic filler.

---

## Instructions

1. **Confirm subject and context.** Disambiguate the person; note the meeting purpose and recency window.
2. **Current role.** Title, company, tenure, what the team does, and likely responsibilities (labeled as inference) — each sourced.
3. **Career trajectory.** Previous 3–4 roles with companies and approximate tenure; the pattern in their moves; notable prior employers — sourced.
4. **Public perspectives.** 2–3 topics they've spoken/written about, with verbatim quotes and links where available; positions on industry issues.
5. **Conversation starters.** 2–3 specific, genuine references (recent company news, a talk they gave, a shared professional interest if discoverable) — sourced.
6. **Compile source links.** LinkedIn URL, any talks/articles, company bio.
7. **Verify (verification step).** Re-read: any personal/private info that must be removed? Any unsourced fact or fabricated quote/connection? Are inferences labeled and uncertain items `[UNVERIFIED]`? Is thin information acknowledged rather than padded?

---

## False-Positive Prevention

❌ **DON'T:**
- Include the person's family, age, hometown, or personal social media.
- Invent a prior role, a quote, or a "mutual connection" to enrich the briefing.
- State an inferred responsibility ("they own the budget") as confirmed.
- Fill gaps with generic boilerplate about their title.
- Cite a paraphrase as if it were a verbatim quote.

✅ **DO:**
- Keep strictly to professional, public, context-relevant information.
- Source every fact; quote verbatim with a link.
- Label inference clearly and flag uncertainty with `[UNVERIFIED]`.
- Say "limited information found" when that's the truth.
- Note when a primary source was unavailable and what you used instead.

---

## Output Format

```
# Briefing: [Person Name] — [Company]
*Context: [meeting type] | Recency window: [...] | Research date: [...]*

## Current Role
- Title / company / tenure: [...] — [source]
- What their team does: [...] — [source]
- Likely responsibilities: [...] (inference)

## Career Trajectory
- [Role] @ [Company], ~[tenure] — [source]
- Pattern: [...] (inference, labeled)

## Public Perspectives
- Topic: [...]; "[verbatim quote]" — [source, date]
- Position on [issue]: [...] — [source]

## Conversation Starters
- [Specific reference + why it shows homework] — [source]

## Source Links
- LinkedIn: [URL or "not accessible — used [alternates]"]
- Talks / articles / bio: [...]

## Notes
- [UNVERIFIED] items: [...]
- Limited-information flags: [...]
```

---

## Example Output

```
# Briefing: Jordan Rivera (placeholder) — ExampleCo
*Context: partnership discussion | Recency window: 18 months | Research date: 2026-06-07*

## Current Role
- VP of Partnerships at ExampleCo, ~2 years — [LinkedIn profile, accessed 2026-06].
- Team runs channel and technology alliances — [ExampleCo team page, 2026-05].
- Likely responsibilities: owns partner revenue targets and co-marketing (inference from title + team scope; not stated).

## Career Trajectory
- Director, Business Development @ PriorCo (placeholder), ~3 years — [LinkedIn].
- Earlier: alliances roles at two enterprise-software firms — [LinkedIn].
- Pattern: a consistent partnerships/BD track in enterprise SaaS (inference).

## Public Perspectives
- Topic: ecosystem-led growth; "[verbatim quote on partner-sourced pipeline]" — [podcast episode, 2025-11].
- Position: advocates for tighter technical integration before co-selling — [conference talk, 2026-03].

## Conversation Starters
- ExampleCo's recently announced EU expansion — relevant to a cross-border partnership — [company blog, 2026-04].
- Their podcast point about partner-sourced pipeline — a credible, specific opener — [podcast, 2025-11].

## Source Links
- LinkedIn: [URL]
- Talks / articles: [podcast episode], [conference talk], [company blog]

## Notes
- [UNVERIFIED]: exact tenure at PriorCo (LinkedIn shows years only, not months).
- Limited-information: no recent written articles found; perspectives drawn from spoken sources.
```

---

## Verification

- [ ] Only professional, public, context-relevant information included.
- [ ] No personal/private data (family, age, home, personal social media, photos).
- [ ] Every factual claim sourced; quotes verbatim with links.
- [ ] No invented roles, dates, quotes, or connections.
- [ ] Inference labeled; uncertain items flagged `[UNVERIFIED]`.
- [ ] Thin information acknowledged rather than padded.
- [ ] Unavailable primary sources noted with alternates used.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a privacy-bounded, source-cited professional briefing.
- **RT-02 (Multi-Dimensional Analysis Framework):** Covers role, trajectory, perspectives, and conversation hooks.
- **DS-02 (Evidence-Based Decision Making):** Requires a source for every fact and verbatim, attributed quotes.
- **RT-05 (Evidence-Based Reasoning):** Inferred responsibilities follow from sourced facts and are labeled as inference.
- **QA-01 (Self-Critique Triggers):** Final verification audits for privacy leakage, fabrication, and unlabeled inference.

---

## Related Prompts

- `domain-business-strategy/research/research_company_deep_dive.md` — Research the person's company alongside the individual.
- `domain-business-strategy/research/research_competitive_landscape.md` — Understand the competitive context they operate in.
- `domain-business-strategy/research/research_industry_trends.md` — Brief yourself on the trends shaping their market.
