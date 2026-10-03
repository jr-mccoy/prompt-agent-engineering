# Accessibility Prompts

**Category:** Frontend Development / Accessibility
**Prompts:** 5

---

## Overview

Production-grade prompts for web accessibility covering WCAG compliance audits, ARIA implementation patterns, and screen reader testing methodology — plus two prompts that go beyond components: the documents and slides an organisation publishes, and the organisation-wide accessibility program (policy, VPAT/ACR, cadence, procurement, training).

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_accessibility_wcag_audit.md](frontend_accessibility_wcag_audit.md) | Conduct comprehensive WCAG 2.1/2.2 compliance audits with remediation planning | Intermediate |
| [frontend_accessibility_aria_patterns.md](frontend_accessibility_aria_patterns.md) | Implement accessible ARIA patterns for custom UI components | Advanced |
| [frontend_accessibility_screen_reader.md](frontend_accessibility_screen_reader.md) | Test applications with screen readers (NVDA, VoiceOver, JAWS) | Intermediate |
| [frontend_accessibility_documents_slides.md](frontend_accessibility_documents_slides.md) | Triage and fix published PDFs, Word files, decks and recorded media: tagging, reading order, alt text, contrast, captions (WCAG2ICT, PDF/UA) | Intermediate |
| [frontend_accessibility_program_governance.md](frontend_accessibility_program_governance.md) | Organisation-wide program: maturity baseline, policy, evidence-backed VPAT/ACR, risk-tiered cadence, procurement gates, role-based training | Advanced |

## Usage Examples

### Full Accessibility Audit
Use `frontend_accessibility_wcag_audit.md` for:
- Pre-launch compliance assessment
- Legal requirement preparation (ADA, Section 508)
- Baseline measurement for improvements
- Phased remediation planning

### Building Accessible Components
Use `frontend_accessibility_aria_patterns.md` for:
- Modal dialogs
- Tab interfaces
- Accordion/disclosure widgets
- Combobox/autocomplete
- Menu buttons

### Validating with Assistive Technology
Use `frontend_accessibility_screen_reader.md` for:
- NVDA testing on Windows
- VoiceOver testing on macOS/iOS
- Documenting exact screen reader output
- Cross-AT compatibility testing

### Beyond Components
Use `frontend_accessibility_documents_slides.md` when the barrier is a published file —
an annual report PDF, a board deck, a fillable form, a recorded webinar. Use
`frontend_accessibility_program_governance.md` when a buyer asks for a VPAT/ACR, after a
complaint or new regulation, or when audits keep finding the same defects because nothing
upstream changes.

---

## Key Concepts

- **WCAG 2.1 AA**: Target conformance level for most applications
- **POUR Principles**: Perceivable, Operable, Understandable, Robust
- **Automated vs Manual**: Automated tools catch 30-40% of issues; manual testing required

---

## Related Prompts

- [../../domain-software-engineering/testing/testing_accessibility_wcag.md](../../domain-software-engineering/testing/testing_accessibility_wcag.md) - Testing strategy focus
