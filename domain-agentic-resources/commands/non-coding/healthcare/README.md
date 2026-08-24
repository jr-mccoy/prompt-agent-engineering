# Healthcare

## Scope
This folder contains non-coding command resources for healthcare workflows.

## Inclusion criteria
- Focuses on domain-specific planning, analysis, communication, or execution tasks.
- Avoids code-generation-centric instructions unless incidental support is required.
- Uses patterns that can be applied repeatedly by practitioners in this domain.

## Examples
- Care pathway explainer.
- Clinical policy summarizer.
- Patient education material drafter.

## Quality gates checklist
Use the [Non-Coding Quality Gates Checklist Template](../../../documentation/templates/non_coding_quality_gates.md) before publishing or promoting any non-coding resource from this folder.

## Required policy overlay metadata
All healthcare resources in this folder must set:

```yaml
policy_overlay: healthcare_safety_overlay
```

See `documentation/policies/healthcare_safety_overlay.md` for mandatory behavior.
