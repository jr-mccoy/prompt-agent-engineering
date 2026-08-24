# Technical Documentation (User Guide / How-To)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Technical Documentation

## Prompt

```
You are writing technical documentation that enables someone to actually accomplish a task, not just understand a concept.

CONTEXT:
What this documents: [FEATURE/SYSTEM/TOOL NAME]
Who uses this: [USER ROLE/TECHNICAL LEVEL - e.g. "developers integrating our API" or "non-technical end users"]
Common use case: [THE PRIMARY TASK USERS ARE TRYING TO ACCOMPLISH]
Support context: [HOW THIS FITS IN SUPPORT - e.g. "referenced in 30% of support tickets"]

INPUT PROVIDED:
[PASTE YOUR TECHNICAL SPECS, API DETAILS, SYSTEM BEHAVIOR, ERROR CASES, EXAMPLES HERE]

YOUR TASK:
Create documentation that someone can follow step-by-step without prior knowledge. This will be used when things go wrong, so troubleshooting matters as much as happy path.

REQUIRED STRUCTURE:
1. **Prerequisites** (What user needs before starting - tools, access, knowledge)
2. **Overview** (What this does in 2-3 sentences - outcomes not features)
3. **Step-by-Step Instructions** (Numbered steps with expected result after each step)
4. **Code Examples** (Working examples they can copy-paste, with comments explaining key lines)
5. **Common Errors** (The 5 most common failures with exact error messages and fixes)
6. **Troubleshooting** (Decision tree: if X happens, check Y, try Z)
7. **Related Resources** (Links to related docs, API references, support)

CONSTRAINTS:
- Total length: 1000 words maximum
- Prerequisites: Must be exhaustive - include version numbers, permissions, dependencies from your inputs
- Overview: Must explain what user will accomplish, not what the system does
- Instructions: Each step must show expected result from the actual system
- Code examples: Must be complete and use actual syntax/endpoints from inputs (no placeholder code)
- Common errors: Must use exact error message text from inputs (this helps users search)
- Troubleshooting: Must be decision-tree format with specific checks from the actual system
- DO NOT assume: If a step requires knowledge, link to explanation or include it
- DO NOT skip: Error cases and edge cases are not optional (that's when docs get used)
- DO NOT invent: Use only actual error messages, endpoints, commands from inputs - no made-up examples

TONE:
- Imperative and specific ("Run `[actual command from inputs]`") not suggestive
- Include exact commands, file paths, environment variables from the real system
- Assume user is following instructions exactly (precision matters)
- Patient with errors (these docs are read when things are broken)

QUALITY CHECKS - Before outputting, verify:
- [ ] Prerequisites list includes actual version numbers from inputs
- [ ] Every instruction step shows actual expected output from the system
- [ ] All code examples use real endpoints/syntax from inputs (no fake URLs or placeholder values)
- [ ] Code examples include comments explaining key lines
- [ ] Every common error uses exact error text from inputs
- [ ] Troubleshooting section addresses actual failure modes from inputs
- [ ] No invented examples - everything comes from inputs provided
- [ ] File paths match actual system paths from inputs
- [ ] No step assumes knowledge not covered in prerequisites
- [ ] Every "if this fails" has a corresponding "try this" action from real troubleshooting
- [ ] Total word count is under 1000 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Technical docs exist to help users complete actions, not to explain how systems work. The structure forces action-oriented content.

**Customization Options:**
- Adjust for user technical level (non-technical, junior developers, senior developers, admins)
- Modify for documentation system (interactive docs, version tracking, video tutorials)
- Add sections for different content types (API, configuration, installation, integration, migration)

**Common Pitfalls:**
- Missing prerequisites (user can't start)
- Happy path only (breaks when errors occur)
- Placeholder code that doesn't work
- Invented error messages (user can't find them)
- No troubleshooting (user stuck when something fails)
- Mixing real and placeholder details
