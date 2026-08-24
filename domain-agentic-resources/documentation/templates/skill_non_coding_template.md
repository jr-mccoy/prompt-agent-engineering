# Non-Coding Skill Template

Use this template when authoring a **non-coding skill** with reusable process knowledge, references, and assets.

## 1) User Intent and Context Assumptions
- **Target user jobs-to-be-done:**
  - [Job 1]
  - [Job 2]
- **Environment assumptions:** [Where this skill is expected to run and with what context]
- **Prerequisites assumed:** [Knowledge/tools/documents required]
- **Failure modes from missing context:** [Top risks]

## 2) Domain-Specific Role Framing
- **Skill role statement:** [One sentence describing capability]
- **Primary domain(s):** [e.g., research, policy analysis, education]
- **Boundary conditions:** [When this skill should not be used]
- **Escalation path:** [Where to route work when out of scope]

## 3) Input Schema
```yaml
input:
  task_type: string            # Required; classify the task
  objective: string            # Required
  context_bundle:              # Optional structured context
    stakeholder: string
    timeline: string
    constraints:
      - string
  evidence_sources:            # Optional
    - name: string
      trust_level: string      # high | medium | low
  deliverable_type: string     # Required; memo | brief | rubric | plan
  quality_threshold: string    # Optional; baseline | strict
```

## 4) Output Contract (Measurable Criteria)
- **Required outputs:**
  - [Artifact 1]
  - [Artifact 2]
- **Quality metrics:**
  - [ ] Includes a clear method section.
  - [ ] Includes explicit assumptions and dependency list.
  - [ ] Includes confidence labeling for major claims.
  - [ ] Includes actionable next steps with owners/timing.
  - [ ] Meets requested deliverable type exactly.

## 5) Validation Stage
- **Pre-delivery checks:**
  - [ ] Schema compliance (all required inputs handled).
  - [ ] Domain fit check (correct skill for the task).
  - [ ] Quality-threshold check (baseline/strict met).
  - [ ] Reuse check (references/assets used where appropriate).
- **Gate decision:** [Ship / Rework]

## 6) Safety Notes
- Identify and label uncertainty and unsupported claims.
- Avoid replacing licensed/professional judgment in regulated domains.
- Include provenance notes for key evidence inputs.
- Highlight potential stakeholder harm from recommendations.

## 7) Example Runs
### Example Run 1
- **Input summary:** [Task + objective + deliverable]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Ship/Rework + rationale]

### Example Run 2
- **Input summary:** [Task + objective + deliverable]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Ship/Rework + rationale]
