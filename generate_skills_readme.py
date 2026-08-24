#!/usr/bin/env python3
"""
Generate comprehensive README for Claude Code skills.
Uses analysis data from skills_analysis.json.
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import date

ROOT_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = ROOT_DIR / "domain-agentic-resources"
ANALYSIS_PATH = ROOT_DIR / "skills_analysis.json"

def load_analysis():
    """Load skills analysis data."""
    with open(ANALYSIS_PATH, 'r') as f:
        return json.load(f)

def generate_toc(skills_by_category):
    """Generate table of contents."""
    toc = []
    for category in sorted(skills_by_category.keys()):
        count = len(skills_by_category[category])
        # Convert category name to anchor
        anchor = category.lower().replace(' ', '-').replace('_', '-')
        # Format category name for display
        display_name = category.replace('-', ' ').title()
        toc.append(f"- [{display_name}](#{anchor}) ({count} skills)")
    return '\n'.join(toc)

def format_category_name(category):
    """Format category name for display."""
    return category.replace('-', ' ').title()

def format_bundled_resources(resources):
    """Format bundled resources for display."""
    parts = []
    if resources.get('scripts'):
        parts.append(f"{len(resources['scripts'])} scripts")
    if resources.get('references'):
        parts.append(f"{len(resources['references'])} references")
    if resources.get('assets'):
        parts.append(f"{len(resources['assets'])} assets")
    if resources.get('other'):
        parts.append(f"{len(resources['other'])} other files")

    return ', '.join(parts) if parts else 'SKILL.md only'

def extract_when_to_use(description):
    """Extract or infer 'when to use' from description."""
    # This is a simplified version - could be enhanced with NLP
    desc_lower = description.lower()

    if 'test' in desc_lower:
        return "Use when building or improving testing infrastructure"
    elif 'security' in desc_lower:
        return "Use when implementing security measures or auditing"
    elif 'deploy' in desc_lower or 'ci/cd' in desc_lower:
        return "Use when setting up deployment pipelines"
    elif 'api' in desc_lower:
        return "Use when designing or implementing APIs"
    elif 'pattern' in desc_lower:
        return "Use when applying design patterns or architectural patterns"
    else:
        return "Use when working in this domain"

def generate_skill_entry(skill, category):
    """Generate markdown entry for a single skill."""
    entry = [f"#### `{skill['name']}`\n"]
    entry.append(f"- **Path:** `skills/{category}/{skill['name']}/`")
    entry.append(f"- **Description:** {skill['description']}")

    # Bundled resources
    resources_summary = format_bundled_resources(skill['bundled_resources'])
    entry.append(f"- **Resources:** {resources_summary}")

    # Dependencies (if any)
    if skill['dependencies']:
        deps = ', '.join(skill['dependencies'][:5])
        if len(skill['dependencies']) > 5:
            deps += f" (+{len(skill['dependencies']) - 5} more)"
        entry.append(f"- **Dependencies:** {deps}")

    # When to use
    when_to_use = extract_when_to_use(skill['description'])
    entry.append(f"- **When to use:** {when_to_use}")

    entry.append("")  # Blank line
    return '\n'.join(entry)

def generate_readme(data):
    """Generate complete README content."""
    all_skills = data['all_skills']
    total = data['total_skills']
    total_categories = data['total_categories']

    # Organize skills by category
    skills_by_category = defaultdict(list)
    for skill in all_skills:
        skills_by_category[skill['category']].append(skill)

    # Count skills with bundled resources
    skills_with_resources = sum(1 for s in all_skills if s['has_bundled_resources'])

    # Generate README
    readme = []

    # Header
    readme.append("# Claude Code Skills Index")
    readme.append("")
    readme.append(f"**Comprehensive index of {total} Claude Code skills organized by domain.**")
    readme.append("")

    # Overview
    readme.append("## Overview")
    readme.append("")
    readme.append(f"This directory contains **{total} specialized skills** for Claude Code. Skills are modular knowledge packages that use progressive disclosure - loading detailed information only when needed to optimize context usage.")
    readme.append("")

    # Quick Stats
    readme.append("### Quick Stats")
    readme.append("")
    readme.append(f"- **Total Skills:** {total}")
    readme.append(f"- **Categories:** {total_categories}")
    readme.append(f"- **Skills with Bundled Resources:** {skills_with_resources} ({skills_with_resources*100//total}%)")
    readme.append("")

    # Progressive Disclosure explanation
    readme.append("### Progressive Disclosure Architecture")
    readme.append("")
    readme.append("Skills use a three-tier loading system for efficient context management:")
    readme.append("")
    readme.append("1. **Metadata** (name + description) - Always loaded (~100 words)")
    readme.append("2. **SKILL.md body** - Loaded when skill triggers (<5k words)")
    readme.append("3. **Bundled resources** - Loaded as needed by Claude (scripts, references, assets)")
    readme.append("")
    readme.append("This architecture minimizes context window usage while maximizing capability.")
    readme.append("")

    # Table of Contents
    readme.append("## Table of Contents")
    readme.append("")
    readme.append("**By Category:**")
    readme.append(generate_toc(skills_by_category))
    readme.append("")

    # Source attribution
    readme.append("## Source Attribution")
    readme.append("")
    readme.append("These skills are sourced from:")
    readme.append("- **[wshobson/agents](https://github.com/wshobson/agents)** - 107 skills (MIT License)")
    readme.append("- **[daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)** - 25 skills (MIT License)")
    readme.append("")

    # How to use
    readme.append("## How to Use This Index")
    readme.append("")
    readme.append("1. **Browse by category** to find skills for your domain")
    readme.append("2. **Check bundled resources** to see what tools/references are included")
    readme.append("3. **Review dependencies** to ensure you have required tools")
    readme.append("4. **Install skills** by copying to your Claude Code skills directory")
    readme.append("5. **Reference skills** in your prompts or let agents auto-invoke them")
    readme.append("")
    readme.append("---")
    readme.append("")

    # Skills by category
    readme.append("## Skills by Category")
    readme.append("")

    for category in sorted(skills_by_category.keys()):
        skills = sorted(skills_by_category[category], key=lambda s: s['name'])
        category_display = format_category_name(category)

        readme.append(f"### {category_display}")
        readme.append("")
        readme.append(f"**{len(skills)} skills in this category**")
        readme.append("")

        for skill in skills:
            readme.append(generate_skill_entry(skill, category))

    # Appendix: Skills with Bundled Resources
    readme.append("---")
    readme.append("")
    readme.append("## Appendix: Skills with Bundled Resources")
    readme.append("")
    readme.append("These skills include additional scripts, references, or assets beyond SKILL.md:")
    readme.append("")

    skills_with_resources = [s for s in all_skills if s['has_bundled_resources']]
    skills_with_resources.sort(key=lambda s: (s['category'], s['name']))

    for skill in skills_with_resources:
        readme.append(f"### {skill['name']}")
        readme.append(f"**Category:** {format_category_name(skill['category'])}")
        readme.append("")

        resources = skill['bundled_resources']
        for res_type in ['scripts', 'references', 'assets', 'other']:
            if resources.get(res_type):
                files = resources[res_type]
                readme.append(f"**{res_type.title()}:** ({len(files)} files)")
                for f in files[:10]:  # Limit to first 10
                    readme.append(f"- `{f}`")
                if len(files) > 10:
                    readme.append(f"- ...and {len(files) - 10} more")
                readme.append("")

    # Appendix: Dependency Matrix
    readme.append("---")
    readme.append("")
    readme.append("## Appendix: Common Dependencies")
    readme.append("")
    readme.append("Most frequently required tools and technologies:")
    readme.append("")

    # Count dependencies
    dep_count = defaultdict(int)
    for skill in all_skills:
        for dep in skill['dependencies']:
            dep_count[dep] += 1

    # Sort by frequency
    sorted_deps = sorted(dep_count.items(), key=lambda x: x[1], reverse=True)

    readme.append("| Dependency | Skills Using It |")
    readme.append("|------------|----------------|")
    for dep, count in sorted_deps[:30]:  # Top 30
        readme.append(f"| {dep} | {count} |")

    readme.append("")
    readme.append(f"*Last updated: {date.today().isoformat()}*")
    readme.append("")

    return '\n'.join(readme)

def main():
    """Main execution."""
    print("Loading skills analysis data...")
    data = load_analysis()

    print(f"Generating README for {data['total_skills']} skills...")
    readme_content = generate_readme(data)

    output_path = RESOURCES_DIR / 'skills/README.md'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        f.write(readme_content)

    print(f"\n✅ README generated successfully!")
    print(f"   Location: {output_path}")
    print(f"   Size: {len(readme_content)} characters")
    print(f"   Lines: {len(readme_content.splitlines())}")

if __name__ == '__main__':
    main()
