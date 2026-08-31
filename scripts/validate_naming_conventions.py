#!/usr/bin/env python3
"""
Naming Convention Validator for the Prompt & Agent Engineering repository

This script validates that markdown files follow the repository's naming conventions.

Conventions are resource-type aware:
- Prompts: snake_case, all-lowercase, no articles (e.g. security_vulnerability_analysis.md)
- Skill bundles (any path under skills/): kebab-case by design — snake_case/lowercase
  checks are skipped for them
- Guide / entry docs (UPPERCASE filenames, e.g. NEW_PROMPT_TEMPLATE.md): SHOUTING by
  design — snake_case/lowercase checks are skipped for them

Checks applied to EVERY file (any type):
1. Maximum filename length of 55 characters
2. No special characters (parentheses, quotes, etc.) or spaces
3. No numbered sequences (no1_, no2_, etc.)
4. No non-standard prefixes

Checks applied to PROMPTS only (skipped for skill bundles & UPPERCASE docs):
5. snake_case (no hyphens)
6. all-lowercase (no uppercase)
7. No articles in filenames (_a_, _the_, _an_)

Usage:
    python validate_naming_conventions.py [--fix] [--verbose] [--check-only PATH]

Options:
    --fix           Suggest fixes (does not rename, just shows what would change)
    --verbose       Show all files checked, not just violations
    --check-only    Only check a specific file or directory
    --ci            Exit with error code 1 if violations found (for CI)
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

# Maximum filename length (excluding .md extension)
MAX_FILENAME_LENGTH = 55

# Directories to check.
#
# Derived from the layout rather than hardcoded, so it cannot fall behind the
# repository the way the previous fixed list did: that list covered 23 of 55
# top-level directories, leaving naming unvalidated in domain-legal,
# domain-psychology, domain-medical-education, domain-science and 28 others, and
# still named a domain that had since been renamed.
def _check_directories():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bundle_suffixes = ('-toolkit', '-kit', '-studio', '-library', '-system', '-factory')
    always = {'techniques', 'authoring'}
    found = []
    for name in sorted(os.listdir(root)):
        if not os.path.isdir(os.path.join(root, name)) or name.startswith('.'):
            continue
        if name.startswith('domain-') or name.endswith(bundle_suffixes) or name in always:
            found.append(name)
    return found


CHECK_DIRECTORIES = _check_directories()

# Files to exclude from checks
EXCLUDED_FILES = {
    'README.md', 'readme.md', 'CLAUDE.md', 'CONTRIBUTING.md',
    'LICENSE.md', 'CHANGELOG.md', 'SKILL.md', 'AGENT.md', 'COMMAND.md',
    'IMAGE_GENERATION_GUIDE.md', 'QUICK_START.md', 'INDEX.md',
    'MASTER_TECHNIQUE_INDEX.md', 'USE_CASE_LOOKUP.md',
    'SKILL_PATTERN_INDEX.md', 'SKILL_USE_CASE_LOOKUP.md',
    'SKILL_QUALITY_RUBRIC.md', 'AGENT_SKILL_QUICK_START.md',
    'GOLD_STANDARD_SKILL.md', 'PROMPT_QUALITY_STANDARDS.md',
    'AI_AGENT_QUICK_START.md', 'NON_CODING_QUICK_START.md',
    'AGENT_QUICK_START.md', 'COMMAND_QUICK_START.md',
    # Intentionally kebab-case: these agents are referenced by their kebab
    # identity across CLAUDE.md, slash-command `agents_used:` fields, multiple
    # SKILL.md/README files, and a mirrored copy in financial-records-toolkit/.
    # Kebab is also a valid Claude Code agent convention. Renaming would churn a
    # self-contained toolkit for no functional gain, so they are exempt by name.
    'financial-records-orchestrator.md',
    'transaction-research-agent.md',
    'prompt-kit-ingestor.md',
    # Intentionally UPPERCASE-prefixed catalog docs: these are technique-catalog
    # provenance documents referenced by name from techniques/pending-additions/
    # STATUS.md and CANDIDATE_LEDGER.md, and follow the repo's UPPERCASE doc
    # convention with a lowercase topic suffix.
    'TECHNIQUE_CLUSTER_action_gating.md',
    'TECHNIQUE_FAMILY_inter_prompt_contracts.md',
    # Deliberate placeholder marker: the leading _PLANNED_ prefix signals an
    # unimplemented slot and is referenced as such from the evaluation README.
    '_PLANNED_stresstest_orchestrator.md',
    # The article here belongs to an established multi-word term, so the
    # no-articles rule would produce a worse, less recognizable name -- the same
    # reasoning that already exempts prepositions below. "Human in the loop",
    # "sum of the parts", "book of the Bible"; and "at the table" is the name of
    # domain-negotiation's own at-the-table/ subdirectory.
    'aiagent_human_in_the_loop_design.md',
    'finance_sum_of_the_parts_valuation.md',
    'biblical_learner_book_of_the_bible_deep_dive.md',
    'negotiation_emotional_flooding_at_the_table.md',
}

# Directory names to prune entirely (deprecated / not subject to conventions)
EXCLUDED_DIRS = {'_archive', '.git'}

# Standard category prefixes (lowercase)
STANDARD_PREFIXES = {
    # Software engineering prefixes
    'security', 'performance', 'quality', 'architecture', 'evolution',
    'testing', 'devops', 'cloud', 'api', 'mobile',
    # Frontend prefixes
    'frontend',
    # Business prefixes
    'strategy', 'research', 'organization', 'startup', 'analysis',
    # Engineering workflow prefixes
    'engineering', 'workflow', 'done_definition', 'improvement', 'task',
    # Productivity prefixes
    'automation', 'career', 'deep_work', 'prototyping', 'validation',
    # Other domain prefixes
    'image', 'presentation', 'prompt', 'decisioning', 'advertising',
    'writing', 'product', 'design', 'learning', 'medicine', 'education',
    # domain-education-teaching audience tracks: instructor/ program/ learner/
    'teaching', 'program', 'learn',
    'work_better', 'board', 'nano_banana', 'nursing', 'healthcare',
    # Agentic resource types
    'skill', 'agent', 'command', 'persona',
    # LLM-specific
    'llm',
}

# Prefixes that should be standardized
PREFIX_STANDARDIZATION = {
    'codex_': 'workflow_',
    'slop_evaluator_': 'quality_',
    'context_engineering_': 'architecture_context_',
}

# Articles that should be removed from filenames. Only true articles — NOT
# prepositions/conjunctions (_to_, _of_, _and_, _in_, _for_, _or_), which are
# frequently load-bearing in established prompt names (e.g. jobs_to_be_done,
# writing_theme_and_motif). Stripping those produces worse, less-readable names.
ARTICLES = ['_a_', '_an_', '_the_']

# Special characters not allowed
SPECIAL_CHARS = re.compile(r'[()"\'\[\]{}!@#$%^&*=+|\\:;<>?,]')

# Pattern for numbered sequences
NUMBERED_PATTERN = re.compile(r'_no\d+_')


class NamingViolation:
    """Represents a naming convention violation."""

    def __init__(self, filepath, violation_type, message, suggested_fix=None):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.violation_type = violation_type
        self.message = message
        self.suggested_fix = suggested_fix

    def __str__(self):
        base = f"[{self.violation_type}] {self.filepath}: {self.message}"
        if self.suggested_fix:
            base += f"\n  Suggested: {self.suggested_fix}"
        return base


def check_filename_length(filepath, filename):
    """Check if filename exceeds maximum length."""
    name_without_ext = filename[:-3] if filename.endswith('.md') else filename
    if len(name_without_ext) > MAX_FILENAME_LENGTH:
        return NamingViolation(
            filepath,
            'LENGTH',
            f"Filename is {len(name_without_ext)} chars (max {MAX_FILENAME_LENGTH})",
            shorten_filename(filename)
        )
    return None


def check_special_characters(filepath, filename):
    """Check for special characters in filename."""
    if SPECIAL_CHARS.search(filename):
        chars_found = SPECIAL_CHARS.findall(filename)
        return NamingViolation(
            filepath,
            'SPECIAL_CHAR',
            f"Contains special characters: {chars_found}",
            remove_special_chars(filename)
        )
    return None


def check_articles(filepath, filename):
    """Check for articles in filename."""
    filename_lower = filename.lower()
    found = [a for a in ARTICLES if a in filename_lower]
    if found:
        return NamingViolation(
            filepath,
            'ARTICLE',
            f"Contains articles/prepositions: {found}",
            remove_articles(filename)
        )
    return None


def check_numbered_sequence(filepath, filename):
    """Check for numbered sequences like _no1_, _no2_."""
    if NUMBERED_PATTERN.search(filename):
        return NamingViolation(
            filepath,
            'NUMBERED',
            "Contains numbered sequence pattern (_no1_, etc.)",
            remove_numbered_sequence(filename)
        )
    return None


def check_nonstandard_prefix(filepath, filename):
    """Check for non-standard prefixes that should be standardized."""
    filename_lower = filename.lower()
    for old_prefix, new_prefix in PREFIX_STANDARDIZATION.items():
        if filename_lower.startswith(old_prefix):
            return NamingViolation(
                filepath,
                'PREFIX',
                f"Non-standard prefix '{old_prefix}' should be '{new_prefix}'",
                filename.replace(old_prefix, new_prefix, 1)
            )
    return None


def check_hyphen_case(filepath, filename):
    """Check for hyphen-case that should be snake_case."""
    name = filename[:-3] if filename.endswith('.md') else filename
    if '-' in name:
        return NamingViolation(
            filepath,
            'HYPHEN',
            "Uses hyphen-case instead of snake_case",
            filename.replace('-', '_')
        )
    return None


def check_uppercase(filepath, filename):
    """Check for uppercase letters (except in excluded files)."""
    name = filename[:-3] if filename.endswith('.md') else filename
    if any(c.isupper() for c in name):
        return NamingViolation(
            filepath,
            'UPPERCASE',
            "Contains uppercase letters",
            filename.lower()
        )
    return None


def check_period_underscore(filepath, filename):
    """Check for period-underscore patterns like vs._"""
    if '._' in filename or '_.' in filename:
        return NamingViolation(
            filepath,
            'PERIOD',
            "Contains period-underscore pattern",
            filename.replace('._', '_').replace('_.', '_')
        )
    return None


def shorten_filename(filename):
    """Suggest a shortened filename."""
    name = filename[:-3] if filename.endswith('.md') else filename

    # Remove articles first
    for article in ARTICLES:
        name = name.replace(article, '_')

    # Remove numbered sequences
    name = NUMBERED_PATTERN.sub('_', name)

    # Remove duplicate underscores
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')

    # If still too long, truncate intelligently
    if len(name) > MAX_FILENAME_LENGTH:
        # Try to truncate at word boundary
        parts = name.split('_')
        while len('_'.join(parts)) > MAX_FILENAME_LENGTH and len(parts) > 2:
            parts.pop()
        name = '_'.join(parts)

    return name + '.md' if filename.endswith('.md') else name


def remove_special_chars(filename):
    """Remove special characters from filename."""
    name = filename[:-3] if filename.endswith('.md') else filename
    name = SPECIAL_CHARS.sub('', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name + '.md' if filename.endswith('.md') else name


def remove_articles(filename):
    """Remove articles from filename."""
    name = filename
    for article in ARTICLES:
        name = name.replace(article, '_')
    name = re.sub(r'_+', '_', name)
    if name.endswith('.md'):
        name = name[:-3].strip('_') + '.md'
    return name


def remove_numbered_sequence(filename):
    """Remove numbered sequences from filename."""
    name = NUMBERED_PATTERN.sub('_', filename)
    name = re.sub(r'_+', '_', name)
    if name.endswith('.md'):
        name = name[:-3].strip('_') + '.md'
    return name


def is_doc_filename(name_without_ext):
    """True for UPPERCASE guide/entry docs (e.g. NEW_PROMPT_TEMPLATE, REFLECTION-GUIDE).

    The repo convention is that entry/guide files use UPPERCASE_WITH_UNDERSCORES,
    so the snake_case/lowercase rules for prompts do not apply to them.
    """
    letters = [c for c in name_without_ext if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def in_skill_bundle(filepath):
    """
    True for files that follow kebab-case rather than the prompt convention.

    Skills, agents, and commands are addressed by a kebab-case identity in Claude
    Code -- `/author-agentic-system`, `agents_used: system-architect` -- and are
    referenced by that name from SKILL.md files, slash commands, and CLAUDE.md.
    Renaming them to snake_case would break those references for no gain, so the
    snake_case/lowercase rules do not apply inside those trees. Test fixtures are
    exempt for the same reason: their names are data their tests assert on.

    Genuine problems (illegal characters, spaces, over-length names) are still
    checked everywhere.
    """
    normalized = filepath.replace(os.sep, '/').lstrip('./')
    if any(seg in f'/{normalized}' for seg in ('/skills/', '/agents/', '/commands/', '/fixtures/')):
        return True
    # Self-contained bundles address their own files by kebab identity too --
    # `stage-4-gates.md`, `openai-agents-sdk.md` -- and their orchestrators and
    # pipeline docs reference those names. They are applications built from the
    # library, not entries in it, so the prompt naming convention is not theirs
    # to follow. `domain-*` remains fully checked.
    top = normalized.split('/')[0]
    return top.endswith(('-toolkit', '-kit', '-studio', '-library', '-system', '-factory'))


def validate_file(filepath):
    """Validate a single file against all naming conventions."""
    filename = os.path.basename(filepath)

    # Skip excluded files
    if filename in EXCLUDED_FILES:
        return []

    # Skip non-markdown files
    if not filename.endswith('.md'):
        return []

    name_without_ext = filename[:-3]

    # Determine which convention this file follows. Skill bundles are kebab-case
    # by design; UPPERCASE guide/entry docs are SHOUTING by design. For those,
    # skip the snake_case/lowercase checks but still catch genuine problems
    # (illegal characters, spaces/parens, over-length names).
    convention_exempt = in_skill_bundle(filepath) or is_doc_filename(name_without_ext)

    violations = []

    # Always-on checks (apply to every resource type)
    universal_checks = [
        check_special_characters,
        check_period_underscore,
        check_filename_length,
        check_numbered_sequence,
        check_nonstandard_prefix,
    ]
    # Prompt-convention checks (snake_case / all-lowercase / no articles)
    prompt_convention_checks = [
        check_hyphen_case,
        check_uppercase,
        check_articles,
    ]

    checks = list(universal_checks)
    if not convention_exempt:
        checks.extend(prompt_convention_checks)

    for check in checks:
        violation = check(filepath, filename)
        if violation:
            violations.append(violation)

    return violations


def find_all_files(base_path, directories=None):
    """Find all markdown files to check."""
    files = []
    dirs_to_check = directories or CHECK_DIRECTORIES

    for directory in dirs_to_check:
        dir_path = os.path.join(base_path, directory)
        if os.path.exists(dir_path):
            for root, dirnames, filenames in os.walk(dir_path):
                # Prune deprecated/archived trees in place
                dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
                for filename in filenames:
                    if filename.endswith('.md'):
                        files.append(os.path.join(root, filename))

    return sorted(files)


def generate_report(violations, verbose=False):
    """Generate a formatted report of violations."""
    if not violations:
        return "No naming convention violations found."

    # Group by violation type
    by_type = defaultdict(list)
    for v in violations:
        by_type[v.violation_type].append(v)

    report = []
    report.append(f"\n{'='*70}")
    report.append(f"NAMING CONVENTION VIOLATIONS REPORT")
    report.append(f"{'='*70}")
    report.append(f"Total violations: {len(violations)}")
    report.append("")

    type_labels = {
        'LENGTH': 'Filename Too Long (>55 chars)',
        'SPECIAL_CHAR': 'Special Characters',
        'ARTICLE': 'Contains Articles/Prepositions',
        'NUMBERED': 'Numbered Sequences',
        'PREFIX': 'Non-Standard Prefix',
        'HYPHEN': 'Hyphen-Case (should be snake_case)',
        'UPPERCASE': 'Contains Uppercase',
        'PERIOD': 'Period-Underscore Pattern',
    }

    for vtype, vlist in sorted(by_type.items()):
        report.append(f"\n## {type_labels.get(vtype, vtype)} ({len(vlist)} files)")
        report.append("-" * 50)
        for v in vlist:
            report.append(f"  {v.filename}")
            if v.suggested_fix:
                report.append(f"    -> {v.suggested_fix}")

    report.append("")
    report.append("="*70)

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description='Validate naming conventions')
    parser.add_argument('--fix', action='store_true',
                        help='Show suggested fixes')
    parser.add_argument('--verbose', action='store_true',
                        help='Show all files checked')
    parser.add_argument('--check-only', type=str, default=None,
                        help='Only check a specific path')
    parser.add_argument('--ci', action='store_true',
                        help='Exit with code 1 if violations found')
    parser.add_argument('--json', action='store_true',
                        help='Output results as JSON')
    args = parser.parse_args()

    # Change to repo root
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)

    # Find files to check
    if args.check_only:
        if os.path.isfile(args.check_only):
            files = [args.check_only]
        else:
            files = find_all_files('.', [args.check_only])
    else:
        files = find_all_files('.')

    if args.verbose:
        print(f"Checking {len(files)} files...")

    # Validate all files
    all_violations = []
    for filepath in files:
        violations = validate_file(filepath)
        all_violations.extend(violations)

    # Generate report
    if args.json:
        import json
        output = {
            'total_files': len(files),
            'total_violations': len(all_violations),
            'violations': [
                {
                    'file': v.filepath,
                    'type': v.violation_type,
                    'message': v.message,
                    'suggested_fix': v.suggested_fix
                }
                for v in all_violations
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        report = generate_report(all_violations, args.verbose)
        print(report)

    # Exit with appropriate code for CI
    if args.ci and all_violations:
        sys.exit(1)

    return len(all_violations)


if __name__ == '__main__':
    main()
