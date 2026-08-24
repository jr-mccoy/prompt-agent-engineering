---
title: "Route a Workflow Through the Right Visual Modality"
category: presentations/visual-planning
description: "Given a communication or thinking task, decide which visual modality actually serves it — table, chart, diagram, slide, infographic, dashboard, sketch, or no-visual-at-all. Produces a routed recommendation with reasoning, not a reflexive 'make a chart' answer."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - DS-25
  - QA-01
difficulty: intermediate
tags:
  - visual-planning
  - modality
  - chart-selection
  - communication
  - routing
updated: "2026-04-21"
related_prompts:
  - domain-presentations/visual-planning/visualplan_visual_qa_harness.md
  - domain-presentations/visual-planning/visualplan_capability_frontier_map.md
  - domain-presentations/visual-planning/visualplan_cascade_effects_scan.md
  - domain-presentations/powerpoint_board_deck_generator.md
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
---

# Route a Workflow Through the Right Visual Modality

**Objective:** Given a task — "communicate X to audience Y," "think through Z for myself," "persuade group W of decision V" — route to the visual modality that actually serves it: table, chart (of a named type), diagram, slide deck, infographic, dashboard, sketch, or text-only. Produces a routed recommendation with reasoning and the specific form the modality should take. Refuses reflexive "make a chart" or "put it in a deck" outputs.

**When to use:**
- The user has a communication or thinking task and is about to default to a familiar modality (usually slides, usually a chart).
- A team is deciding how to present something and wants a rigorous route, not a habit.
- A PM / analyst / writer is producing an artifact and wants to check that the modality fits before investing in production.
- A personal thinking task that may or may not benefit from a visual.

**Don't use when:** The modality is fixed by external constraint (the board template is fixed; the customer expects a PDF). Then the prompt is moot — use the fixed modality well.

**Audience:** Anyone producing visual or mixed-media artifacts. Output is a recommended modality + form + rationale, ready to hand to the producer.

---

## Inputs Required

1. **The task.** One sentence: what the user is trying to do. "Explain our Q3 miss to the board," "Think through whether to migrate to X for myself," "Convince engineering that option B is better," "Show parents how the fraction curriculum works."
2. **The audience.** Specific. Role, prior knowledge, attention budget, decision authority.
3. **The content.** What the user has: data? A comparison? A flow or process? A timeline? An argument? An identity or brand? A ranked list?
4. **The medium the artifact will live in.** Printed, shared screen, async Slack post, PDF, email body, live presentation, personal notes.
5. **Time and skill budget.** How much time and what production skill are available.
6. **Success criterion.** What happens if this artifact lands. A decision? A feeling? A learned concept?

---

## Instructions

### Step 1 — Classify the content shape

Every visual decision starts with what's actually being shown. Pick one primary content shape (secondary is allowed):

| Shape | Signals |
|-------|---------|
| **Comparison** | Multiple items evaluated against shared attributes. |
| **Composition** | Parts that sum to a whole; mix / share. |
| **Distribution** | How values are spread across a range. |
| **Change over time** | A trend across ordered intervals. |
| **Relationship** | Correlation, causation, or structural link between quantities. |
| **Ranking** | Ordered list by a single dimension. |
| **Flow / process** | Steps, states, or a directed graph with order. |
| **Structure / hierarchy** | Organizational, taxonomic, containment. |
| **Geography** | Spatial distribution on a real or abstract map. |
| **Narrative argument** | A sequence of claims with supporting evidence. |
| **Single fact / hero number** | One load-bearing number the audience must remember. |
| **Identity / brand** | A visual mark or scene representing a concept. |

If the content doesn't fit any shape, revisit — possibly the task isn't actually visual.

### Step 2 — Route by modality family

Using content shape (step 1) × medium (input 4) × audience (input 2), recommend a modality family:

| Content shape | Preferred modality family | Notable alternatives |
|---------------|---------------------------|---------------------|
| Comparison | Table (detail) or bar chart (visual). | Matrix / RICE-style grid if both axes matter. |
| Composition | Stacked bar (multi-entity) or single 100% stacked bar (single entity). | Small pie ONLY if 2–3 slices with a hero share. |
| Distribution | Histogram / box plot / strip plot. | — |
| Change over time | Line chart. | Area chart if composition changes over time too; bar-in-time if few discrete intervals. |
| Relationship | Scatter plot. | Heatmap for many categorical pairs. |
| Ranking | Horizontal bar chart, sorted. | Dot plot for dense rankings. |
| Flow / process | Diagram (flowchart / sequence / state machine). | — |
| Structure / hierarchy | Tree / org chart / nested. | Sunburst / treemap for proportional structure. |
| Geography | Map (choropleth / dot / flow). | Cartogram for population-weighted. |
| Narrative argument | Slide deck or structured document. | Sometimes a single chart + caption beats a deck. |
| Single fact / hero number | Text callout, poster, single slide. | — |
| Identity / brand | Image (logo, infographic, scene). | — |

If the audience has a low attention budget (exec, parent group, customer) and the task is "understand," default to simpler modalities — tables over charts over dashboards. If the audience is analytical and needs to query (data analyst, investigator), default to denser modalities.

### Step 3 — Check "no visual at all"

Some tasks are worse with a visual. Check:

- **Is the content < 7 data points in comparison?** A sentence often beats a chart.
- **Is the audience reading this once in an email?** A deck is overkill.
- **Is the claim singular?** A callout or a number in text beats a chart.
- **Is the user's thinking task unresolved?** Sketch privately before producing a polished visual for others.

If any check fires, recommend text / callout / private sketch instead of a visual artifact. Name the specific minimalist form.

### Step 4 — Specify the exact form

Don't stop at family. Specify:

- Chart type (e.g., "horizontal bar, sorted descending, top 10, value labels on bars").
- Table columns and sort order.
- Diagram structure (flowchart with N nodes, sequence of swimlanes, state machine of M states).
- Deck length (3 slides, 15 slides) and slide roles (title / data / recommendation / appendix).
- Infographic layout (single scroll / multi-panel / fold).
- Dashboard tiles (which charts, priority order).

This is the form the producer will actually build.

### Step 5 — Match form to medium

Check the recommendation against input 4:

- Printed at 1-page: fits? readable?
- Shared-screen / zoomed: chart-on-a-chart?
- Async Slack: will the image render without context?
- Email body: inline image vs attachment?
- Live presentation: readable from the back?
- Personal notes: minimal-effort form, not polished?

If the form doesn't fit the medium, adjust or reroute.

### Step 6 — Match form to success criterion

From input 6:

- Decision: recommend a modality that surfaces a decision frame (often a comparison or matrix with a recommendation column).
- Feeling / persuasion: narrative deck or infographic with a hero callout.
- Learned concept: diagram or worked example; not a dashboard.
- Personal thinking: whatever the user can produce fastest for themselves.

Misaligned form + criterion = the visual will land but not work.

### Step 7 — Flag anti-patterns

For the recommended form, name the anti-patterns to avoid:

- Pie chart with > 5 slices.
- Stacked bar with > 5 categories.
- Line chart with a broken or truncated axis (unless explicitly signaled).
- Diagram with > 15 nodes in a single view.
- Deck with > 5 chart slides in a row with no narrative.
- Dashboard with > 7 tiles per view.
- Any chart without axis labels / units / source.
- Infographic with text-as-image that can't be searched or screen-read.

Anti-patterns specific to the shape also apply.

### Step 8 — Time budget check

Per input 5, does the recommended form fit the budget?

- Rough effort per modality: table (minutes), single chart (10–30 min), diagram (30–90 min), deck (hours to days), infographic (hours to a day of design), dashboard (day to weeks).

If the recommendation exceeds budget, either downgrade the form (simpler version of same modality) or reroute (table instead of infographic).

### Step 9 — Explain the routing decision

Three sentences. What was recommended, why this shape-medium-audience-criterion combination led there, what was rejected.

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Pick one primary content shape.
- Recommend a specific modality and specific form.
- Run the "no visual at all" check.
- Check form-medium and form-criterion fit.
- Flag anti-patterns specific to the recommendation.
- Check the time budget.

### Must Not
- Default to "make a deck" or "make a chart" without reasoning.
- Recommend a form the audience (input 2) can't consume.
- Recommend effort-heavy modalities (infographic, dashboard) without checking budget.
- Provide an ambiguous recommendation ("maybe a chart or a diagram").
- Ignore the content-shape classification and route by vibe.
- Let a "visual is always better" prior drive the routing.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Treat "executive audience" as "must have slides." Sometimes a 1-page table beats a 20-slide deck for execs.
- Route narrative arguments to a chart. Narrative is usually a deck or a structured document; a chart supports but doesn't argue.
- Recommend a dashboard for a one-shot decision. Dashboards are for recurring consumption, not one-time answers.
- Recommend a pie chart. Pie charts lose comparison accuracy past 2–3 slices; bar charts almost always win.
- Over-route to infographic for identity / brand tasks. An infographic is a narrative artifact with identity elements, not pure identity.

✅ **DO:**
- Downgrade modalities aggressively when the budget is tight. A rough table today beats a polished dashboard in two weeks.
- Route private thinking tasks to the simplest possible modality — a sketch, a bulleted list, a single napkin chart.
- When the content shape is Comparison with 2 items, recommend a table; Comparison with > 5 items, a sorted bar.
- For persuasion, privilege narrative structure over data density.
- Name the chart type (bar / line / scatter / etc.) specifically; don't leave "chart" abstract.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Routes a persuasion task to a dense dashboard; audience drowns; decision doesn't move. Or routes a quick thinking task to a polished deck; user spends days producing something that didn't need to be produced.

❌ **UNHELPFUL failure:** Hedges across three modalities without committing; user gets no clearer signal.

✅ **Quality check:** A senior communicator would, given the inputs, arrive at the same routing — or at least agree the recommendation is defensible.

---

## Output Format

```markdown
# Visual Modality Route — [Task]

## Inputs Summary
- Task: 
- Audience: 
- Medium: 
- Success criterion: 
- Time / skill budget: 

## Content Shape
- **Primary:** [from step 1 list]
- **Secondary (if any):** 

## Recommended Modality
- **Family:** [Table / Chart type / Diagram / Deck / Infographic / Dashboard / Sketch / Text only]
- **Specific form:** [exact form — e.g., "horizontal bar chart, sorted descending, top 7, value labels, ~400px wide for Slack embed"]

## Routing Rationale (3 sentences)
[What was chosen, why this shape × medium × audience × criterion led there, what was rejected.]

## Form-Medium Fit
- [Check per input 4; any adjustments.]

## Form-Criterion Fit
- [Check per input 6.]

## Anti-Patterns to Avoid
- [Specific to the recommended form.]

## Time Budget Check
- Estimated effort: 
- Fits budget: yes / downgrade to: [lighter form]

## No-Visual-Alternative
- [Was this considered? Is it actually a better choice? If borderline, note the text-only alternative.]
```

---

## Verification

- [ ] Exactly one primary content shape.
- [ ] One modality family and one specific form.
- [ ] No-visual-at-all check was run and noted.
- [ ] Form fits the medium and the success criterion.
- [ ] Anti-patterns listed.
- [ ] Time budget checked; downgrade or reroute if over.
- [ ] Rationale in three sentences; no hedged-across-three recommendation.
- [ ] No "make a deck" or "make a chart" without shape-driven justification.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a routed modality + form, not a menu.
- **ST-02 (Structured Sequential Instructions):** Ten steps from shape → route → no-visual check → form → medium fit → criterion fit → anti-patterns → budget → rationale → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids reflex routing ("make a deck") and ambiguous recommendations.
- **DS-01 (Framework Application):** Content-shape taxonomy × modality table is the framework.
- **DS-25 (Chart Selection Dictionary):** The shape-to-modality table is the chart-selection technique applied across all visual modalities, not only charts.
- **QA-01 (Self-Verification):** Verification checklist forces commitment and catches the reflex defaults.
