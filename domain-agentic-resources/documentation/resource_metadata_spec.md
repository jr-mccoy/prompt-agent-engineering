# Resource Metadata Specification (Canonical)

This document defines the required metadata contract for every resource file in `domain-agentic-resources`, including agents, skills, and commands.

## 1) Scope

This specification applies to:

- Agent resources
- Skill resources
- Command resources

If a file is treated as a reusable resource artifact, it **must** include a metadata block conforming to this spec.

---

## 2) Required Fields

Every resource metadata block **must** define all fields below.

| Field | Type | Required | Allowed Values / Shape | Purpose |
|---|---|---|---|---|
| `resource_type` | string | Yes | `agent` \| `skill` \| `command` | Identifies the resource category. |
| `domain_class` | string | Yes | `coding` \| `non-coding` \| `hybrid` | Indicates whether the resource is software-focused, non-software-focused, or mixed. |
| `domain_vertical` | string | Yes | One controlled vertical (see §3) | Primary application area for routing and discoverability. |
| `technique_tags` | array of strings | Yes | 1..20 tags; lowercase kebab-case recommended | Captures prompting/workflow techniques used by the resource. |
| `validation_mode` | array of strings | Yes | One or more checks from §4 | Defines validation gates that should pass before resource acceptance/use. |
| `output_contract` | object | Yes | Structured measurable outputs (see §5) | Defines what “done” looks like with measurable criteria. |
| `policy_overlay` | string | Conditional | Overlay id from §6 when vertical is high-stakes | Applies mandatory safety/compliance behavior for affected verticals. |

---

## 3) `domain_vertical` Controlled Vocabulary

Use one of the following values for `domain_vertical`:

- `education`
- `research`
- `writing`
- `healthcare`
- `business`
- `creative`
- `legal`
- `finance`
- `operations`
- `customer-support`
- `marketing`
- `product`
- `human-resources`
- `policy`
- `general`

If none fits cleanly, use `general` and document rationale in the resource body.

---

## 4) `validation_mode` Check Catalog

`validation_mode` is a list of validation checks required for that resource.

Recommended check names:

- `schema` — metadata schema completeness/type checks
- `safety` — policy/safety risk checks
- `quality` — rubric/readability/clarity checks
- `factuality` — evidence and claim-grounding checks (when applicable)
- `format` — output shape/format conformance checks
- `examples` — example presence and correctness checks
- `tests` — executable or deterministic test checks (when applicable)
- `lint` — style/lint checks for structured files/scripts
- `human-review` — mandatory human approval gate

At least one check is required; include all checks necessary for the resource’s risk profile.

---

## 5) `output_contract` Structure

`output_contract` must be measurable and machine-checkable where feasible.

### Required subfields

| Subfield | Type | Required | Description |
|---|---|---|---|
| `deliverables` | array of objects | Yes | Concrete outputs the resource must produce. |
| `acceptance_criteria` | array of strings | Yes | Objective criteria used to validate completion quality. |
| `constraints` | array of strings | Yes | Hard limits (style, safety, formatting, length, policy). |

### `deliverables` object shape

Each `deliverables` entry should include:

- `name` (string): output artifact name
- `format` (string): e.g., `markdown`, `json`, `table`, `plan`
- `min_items` (integer, optional)
- `max_items` (integer, optional)
- `required_sections` (array of strings, optional)

---

## 6) Policy Overlay Requirements

`policy_overlay` is required for high-stakes verticals and optional otherwise.

- `domain_vertical: healthcare` → `policy_overlay: healthcare_safety_overlay`
- `domain_vertical: legal` → `policy_overlay: regulated_business_overlay`
- `domain_vertical: finance` → `policy_overlay: regulated_business_overlay`
- `domain_vertical: policy` → `policy_overlay: regulated_business_overlay`
- `domain_vertical: business` → `policy_overlay: regulated_business_overlay` **when** the resource is regulated/compliance-sensitive

Overlay definitions live in:

- `documentation/policies/healthcare_safety_overlay.md`
- `documentation/policies/regulated_business_overlay.md`

---

## 7) Canonical Metadata Template

Use this template in resource files:

```yaml
resource_metadata:
  resource_type: skill
  domain_class: non-coding
  domain_vertical: education
  technique_tags:
    - scaffolded-explanation
    - socratic-questioning
    - misconception-detection
  validation_mode:
    - schema
    - quality
    - safety
    - format
  policy_overlay: healthcare_safety_overlay  # required for healthcare resources
  output_contract:
    deliverables:
      - name: lesson-plan
        format: markdown
        required_sections:
          - learning-objectives
          - activities
          - assessment
      - name: adaptation-notes
        format: bullet-list
        min_items: 3
    acceptance_criteria:
      - "Includes at least 3 measurable learning objectives."
      - "Maps activities to each objective."
      - "Contains an assessment rubric with 3 performance levels."
    constraints:
      - "Avoid medical, legal, or financial advice unless explicitly in scope."
      - "Use age-appropriate language for target learners."
```

---

## 8) Example A — Non-Coding Skill (Copy/Paste)

```yaml
resource_metadata:
  resource_type: skill
  domain_class: non-coding
  domain_vertical: writing
  technique_tags:
    - audience-adaptation
    - tone-calibration
    - outline-first
    - revision-loop
  validation_mode:
    - schema
    - quality
    - format
    - human-review
  output_contract:
    deliverables:
      - name: article-draft
        format: markdown
        required_sections:
          - title
          - executive-summary
          - main-body
          - next-steps
      - name: revision-checklist
        format: checklist
        min_items: 5
    acceptance_criteria:
      - "Draft includes all required sections in order."
      - "Executive summary is 60-120 words."
      - "Main body contains at least 3 clearly labeled subsections."
      - "Checklist has at least 5 actionable revision items."
    constraints:
      - "Do not fabricate quotes or citations."
      - "Keep language plain and audience-appropriate."
```

---

## 9) Example B — Non-Coding Command (Copy/Paste)

```yaml
resource_metadata:
  resource_type: command
  domain_class: non-coding
  domain_vertical: business
  technique_tags:
    - decision-matrix
    - risk-ranking
    - assumption-audit
  validation_mode:
    - schema
    - quality
    - format
    - safety
  policy_overlay: regulated_business_overlay
  output_contract:
    deliverables:
      - name: options-matrix
        format: table
        min_items: 3
      - name: recommendation
        format: markdown
        required_sections:
          - selected-option
          - rationale
          - risks
          - mitigation
    acceptance_criteria:
      - "Matrix compares at least 3 options across at least 4 criteria."
      - "Recommendation names exactly one selected option."
      - "At least 3 risks are listed with mitigation actions."
    constraints:
      - "State assumptions explicitly before final recommendation."
      - "Avoid domain-specific legal or medical claims."
```

---

## 10) Compliance Rules

1. All required top-level fields are mandatory; `policy_overlay` is mandatory when conditions in §6 apply.
2. `resource_type`, `domain_class`, and `domain_vertical` must use controlled values.
3. `technique_tags` cannot be empty.
4. `validation_mode` cannot be empty.
5. `output_contract.acceptance_criteria` must contain at least one measurable criterion.
6. For affected verticals, `policy_overlay` must match the required overlay in §6.
7. New resource submissions should be rejected if metadata is missing or invalid.

This file is the canonical source for resource metadata requirements.
