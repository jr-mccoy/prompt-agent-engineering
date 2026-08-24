# Non-Coding Agent Template

Use this template when authoring a **non-coding agent**. Fill every bracketed field before publishing.

## 1) User Intent and Context Assumptions
- **Primary user intent:** [What outcome is the user trying to achieve?]
- **Secondary intents (optional):** [List adjacent goals.]
- **Context assumptions:**
  - [Assumption 1]
  - [Assumption 2]
  - [Assumption 3]
- **Unknowns to clarify early:**
  - [Question 1]
  - [Question 2]

## 2) Domain-Specific Role Framing
- **Agent role title:** [e.g., Healthcare Information Synthesizer]
- **Domain scope:** [What this agent covers]
- **Out-of-scope boundaries:** [What this agent must not do]
- **Decision posture:** [Conservative / exploratory / facilitative]
- **Required perspective(s):** [e.g., compliance, user outcomes, risk]

## 3) Input Schema
```yaml
input:
  user_goal: string            # Required
  audience: string             # Required (executive, practitioner, student, etc.)
  domain_context: string       # Required background/context
  constraints:                 # Optional
    - string
  source_materials:            # Optional references
    - type: string             # report | transcript | policy | notes
      location: string
  requested_output_format: string  # Optional; default: structured brief
  risk_tolerance: string       # Optional; low | medium | high
```

## 4) Output Contract (Measurable Criteria)
- **Output structure must include:**
  1. [Section A]
  2. [Section B]
  3. [Section C]
- **Measurable criteria:**
  - [ ] Contains at least **N** concrete recommendations.
  - [ ] Labels assumptions vs. verified facts.
  - [ ] Provides priority levels (e.g., High/Medium/Low) for each recommendation.
  - [ ] Uses language appropriate to the stated audience.
  - [ ] Includes an explicit “limitations” note.

## 5) Validation Stage
- **Validation checklist:**
  - [ ] Intent alignment check passed.
  - [ ] Domain boundary check passed (no out-of-scope guidance).
  - [ ] Evidence quality check passed (authoritative sources preferred).
  - [ ] Consistency check passed (no contradictions).
  - [ ] Readability check passed (target audience fit).
- **Validation output:** [Pass / Revise] with one-sentence rationale.

## 6) Safety Notes
- Do not present regulated advice (medical/legal/financial) as definitive instructions.
- Escalate high-risk decisions to qualified professionals.
- Call out uncertainty explicitly when source quality or recency is weak.
- Avoid discriminatory, stigmatizing, or culturally narrow framing.

## 7) Example Runs
### Example Run 1
- **Input summary:** [Brief user request + context]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Pass/Revise + why]

### Example Run 2
- **Input summary:** [Brief user request + context]
- **Expected output highlights:**
  - [Highlight 1]
  - [Highlight 2]
- **Validation result:** [Pass/Revise + why]
