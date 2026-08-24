# Non-Coding Command Template

Use this template when authoring a **non-coding command** that orchestrates steps, agents, or skills.

## 1) User Intent and Context Assumptions
- **Primary command objective:** [What the command must accomplish]
- **Starting context assumptions:**
  - [Assumption 1]
  - [Assumption 2]
- **Inputs likely to be incomplete:** [What is often missing and must be requested]
- **Success definition from user perspective:** [What "done" looks like]

## 2) Domain-Specific Role Framing
- **Command role:** [Coordinator / analyst / reviewer / planner]
- **Domain focus:** [e.g., strategy, operations, healthcare education]
- **Execution mode:** [single-pass / staged / iterative]
- **Hard boundaries:** [Actions this command cannot take]

## 3) Input Schema
```yaml
input:
  objective: string            # Required
  scope: string                # Required
  stakeholders:                # Optional
    - role: string
      concerns:
        - string
  constraints:                 # Optional
    timeline: string
    compliance: string
    budget: string
  required_artifacts:          # Required
    - string
  optional_sources:
    - string
  output_style: string         # Optional; concise | detailed | executive
```

## 4) Output Contract (Measurable Criteria)
- **Command must return:**
  1. [Execution summary]
  2. [Structured artifact(s)]
  3. [Validation record]
- **Measurable criteria:**
  - [ ] Every required artifact is produced.
  - [ ] Each artifact includes acceptance criteria.
  - [ ] At least one risk register section is included.
  - [ ] Dependencies and blockers are explicitly listed.
  - [ ] Recommended next action is time-bound.

## 5) Validation Stage
- **Stage checks:**
  - [ ] Input completeness check.
  - [ ] Step-by-step consistency check.
  - [ ] Output contract compliance check.
  - [ ] Risk and boundary check.
  - [ ] Final reviewer sanity check.
- **Validation verdict:** [Pass / Needs Follow-up]

## 6) Safety Notes
- Treat sensitive domain guidance as informational, not prescriptive.
- Flag high-impact uncertainty and request expert review before execution.
- Avoid hidden assumptions in stakeholder-sensitive recommendations.
- Log known limitations and deferred decisions.

## 7) Example Runs
### Example Run 1
- **Input summary:** [Objective + scope + required artifacts]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Pass/Needs Follow-up + why]

### Example Run 2
- **Input summary:** [Objective + scope + required artifacts]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Pass/Needs Follow-up + why]
