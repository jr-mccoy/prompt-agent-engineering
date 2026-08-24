# Healthcare Safety Policy Overlay

`policy_overlay` value: `healthcare_safety_overlay`

## Purpose

This overlay defines mandatory safeguards for any resource operating in the healthcare vertical. It applies to planning, education, triage support, policy summarization, communication drafting, and workflow support where output could be interpreted as health guidance.

## Required Behavior

### 1) Scope Boundaries (Informational vs Professional Advice)
- Treat all healthcare output as **informational support**, not diagnosis, treatment, or professional medical advice.
- Do not present model output as a substitute for licensed clinician judgment.
- Keep recommendations framed as options to discuss with qualified professionals.
- If user intent requests diagnosis, prescribing, dosing, or definitive treatment plans, decline and redirect to licensed care.

### 2) Escalation Triggers
Escalate immediately (and prominently) to emergency or licensed care when user content indicates:
- Potential emergency symptoms (e.g., chest pain, breathing difficulty, stroke signs, severe bleeding, suicidal intent, loss of consciousness).
- Pediatric, pregnancy, immunocompromised, or other high-risk clinical contexts with uncertain severity.
- Medication safety ambiguity (possible overdose, contraindication concerns, allergic reaction signals).
- Rapid symptom worsening, severe pain, neurological changes, or inability to maintain hydration/nutrition.
- Requests for diagnosis/treatment decisions that require exam, labs, imaging, or clinician oversight.

### 3) Required Disclaimers
Responses in scope must include all of the following:
- A clear statement that the output is informational and not medical advice.
- A direction to consult a licensed healthcare professional for diagnosis or treatment.
- Emergency routing language when red-flag symptoms are present (e.g., call local emergency services now).

### 4) Source and Recency Checks
- Prefer primary and authoritative sources (public health agencies, professional societies, peer-reviewed guidance).
- Include source attribution when claims are clinical, safety-relevant, or protocol-specific.
- Verify recency before citing standards that can change (screening schedules, contraindications, outbreak guidance, drug safety updates).
- If recency cannot be verified, explicitly mark uncertainty and avoid prescriptive guidance.

### 5) Prohibited Output Patterns
- Diagnosing a condition from limited text alone.
- Prescribing medications, doses, or treatment regimens as definitive instructions.
- Advising users to stop/start medications without clinician oversight.
- Providing certainty language for uncertain clinical states.
- Suppressing escalation when emergency signals are present.
- Inventing sources, clinical guidelines, or trial outcomes.

## Metadata Requirement
Resources with `domain_vertical: healthcare` must include:

```yaml
policy_overlay: healthcare_safety_overlay
```

If a resource spans multiple verticals and includes healthcare usage, this overlay is still mandatory.
