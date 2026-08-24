#!/usr/bin/env python3
"""
Generate comprehensive README.md for Claude Code agents from analysis data.
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import date

ROOT_DIR = Path(__file__).resolve().parent
AGENTS_DIR = ROOT_DIR / "domain-agentic-resources" / "agents"

def generate_readme():
    """Generate the agents README.md file."""

    # Load analysis data
    with open(AGENTS_DIR / "agents_analysis.json", 'r') as f:
        data = json.load(f)

    categories = data['categories']
    model_counts = data['model_counts']
    total_agents = data['total_agents']

    # Start building README
    readme = []

    # Header
    readme.append("# Claude Code Agents Index")
    readme.append("")
    readme.append("**Comprehensive index of 128 specialized Claude Code agents organized by domain.**")
    readme.append("")
    readme.append("## Overview")
    readme.append("")
    readme.append(f"This directory contains **{total_agents} specialized AI agents** for Claude Code, each optimized for specific development tasks and domains. Agents are persistent identities with model assignments (Opus/Sonnet/Haiku) for optimal cost/performance balance.")
    readme.append("")

    # Quick Stats
    readme.append("### Quick Stats")
    readme.append("")
    readme.append(f"- **Total Agents:** {total_agents}")
    readme.append(f"- **Categories:** {len(categories)}")
    readme.append(f"- **Model Distribution:**")
    for model in sorted(model_counts.keys()):
        count = model_counts[model]
        percentage = (count / total_agents * 100) if total_agents > 0 else 0
        model_display = model.upper() if model != 'inherit' else 'Inherit (User Choice)'
        readme.append(f"  - **{model_display}:** {count} agents ({percentage:.1f}%)")
    readme.append("")

    # Table of Contents
    readme.append("## Table of Contents")
    readme.append("")
    readme.append("**By Category:**")
    for category in sorted(categories.keys()):
        count = len(categories[category])
        category_display = category.replace('-', ' ').title()
        anchor = category.lower().replace(' ', '-')
        readme.append(f"- [{category_display}](#{anchor}) ({count} agents)")
    readme.append("")

    # Model Assignment Guide
    readme.append("## Understanding Model Assignments")
    readme.append("")
    readme.append("Each agent is assigned a specific Claude model for optimal performance:")
    readme.append("")
    readme.append("- **Opus 4.5** - Critical architecture decisions, security audits, complex design")
    readme.append("- **Sonnet 4.5** - Balanced tasks requiring intelligence and speed")
    readme.append("- **Haiku 4.5** - Fast operational tasks, code generation, quick analyses")
    readme.append("- **Inherit** - User chooses model based on budget and performance needs")
    readme.append("")

    # How to Use
    readme.append("## How to Use This Index")
    readme.append("")
    readme.append("1. **Browse by category** to find agents for your domain")
    readme.append("2. **Check model assignment** to understand cost/performance")
    readme.append("3. **Review activation criteria** ('When to use') to know when to invoke")
    readme.append("4. **Look for related agents** for multi-agent workflows")
    readme.append("5. **Find related skills** for bundled knowledge packages")
    readme.append("")

    # Agents by Category
    readme.append("---")
    readme.append("")
    readme.append("## Agents by Category")
    readme.append("")

    # Sort categories for better organization
    category_order = [
        'architecture', 'backend', 'frontend-mobile', 'database',
        'cloud-infrastructure', 'devops', 'deployment',
        'code-quality', 'testing', 'security',
        'documentation', 'languages', 'ml-ai',
        'orchestration', 'business-operations', 'seo-marketing'
    ]

    # Put categories in preferred order, then alphabetically for any extras
    sorted_categories = [c for c in category_order if c in categories]
    sorted_categories += sorted([c for c in categories.keys() if c not in category_order])

    for category in sorted_categories:
        agents = sorted(categories[category], key=lambda x: x['name'])
        count = len(agents)
        category_display = category.replace('-', ' ').title()

        readme.append(f"### {category_display}")
        readme.append("")
        readme.append(f"**{count} agents in this category**")
        readme.append("")

        # Group by model for better organization
        agents_by_model = defaultdict(list)
        for agent in agents:
            agents_by_model[agent['model']].append(agent)

        # Show agents grouped by model priority (Opus first, then Sonnet, Haiku, Inherit)
        model_priority = ['opus', 'sonnet', 'haiku', 'inherit']

        for model in model_priority:
            if model not in agents_by_model:
                continue

            model_agents = sorted(agents_by_model[model], key=lambda x: x['name'])

            for agent in model_agents:
                readme.append(f"#### `{agent['name']}`")
                readme.append("")
                readme.append(f"- **Path:** `agents/{agent['relative_path']}`")
                readme.append(f"- **Model:** {agent['model'].upper()}")

                # Description
                desc = agent['description']
                # Split on "Use PROACTIVELY" or "Use when" to format better
                if "Use PROACTIVELY" in desc:
                    parts = desc.split("Use PROACTIVELY")
                    main_desc = parts[0].strip()
                    use_when = "Use PROACTIVELY " + parts[1].strip()
                elif "Use when" in desc:
                    parts = desc.split("Use when")
                    main_desc = parts[0].strip()
                    use_when = "Use when " + parts[1].strip()
                else:
                    main_desc = desc
                    use_when = None

                readme.append(f"- **Description:** {main_desc}")
                if use_when:
                    readme.append(f"- **When to use:** {use_when}")

                # Related agents (if any meaningful ones found)
                if agent['related_agents'] and any(len(a) > 5 for a in agent['related_agents']):
                    meaningful_agents = [a for a in agent['related_agents'] if len(a) > 5]
                    if meaningful_agents:
                        readme.append(f"- **Related agents:** {', '.join(meaningful_agents)}")

                # Related skills (if any meaningful ones found)
                if agent['related_skills'] and any(len(s) > 5 for s in agent['related_skills']):
                    meaningful_skills = [s for s in agent['related_skills'] if len(s) > 5]
                    if meaningful_skills:
                        readme.append(f"- **Related skills:** {', '.join(meaningful_skills)}")

                readme.append("")

        readme.append("---")
        readme.append("")

    # Quick Reference Tables
    readme.append("## Quick Reference")
    readme.append("")

    # By Model
    readme.append("### Agents by Model Assignment")
    readme.append("")
    for model in ['opus', 'sonnet', 'haiku', 'inherit']:
        model_display = model.upper() if model != 'inherit' else 'INHERIT (User Choice)'
        readme.append(f"**{model_display}** ({model_counts.get(model, 0)} agents)")
        readme.append("")

        # Find all agents with this model
        model_agents = []
        for category, agents in categories.items():
            for agent in agents:
                if agent['model'] == model:
                    model_agents.append((category, agent))

        # Sort by category then name
        model_agents.sort(key=lambda x: (x[0], x[1]['name']))

        # Show first 10 for each model
        for category, agent in model_agents[:10]:
            readme.append(f"- `{agent['name']}` ({category})")

        if len(model_agents) > 10:
            readme.append(f"- ... and {len(model_agents) - 10} more")

        readme.append("")

    # Footer
    readme.append("---")
    readme.append("")
    readme.append("## Additional Resources")
    readme.append("")
    readme.append("- [Skills Index](../skills/README.md) - 132 modular knowledge packages")
    readme.append("- [Commands Index](../commands/README.md) - 71 multi-agent orchestration workflows")
    readme.append("- [Integration Guide](../documentation/INTEGRATION_WITH_PROMPTS.md) - How agents relate to prompts")
    readme.append("- [Future Processing Instructions](../documentation/FUTURE_PROCESSING_INSTRUCTIONS.md) - Detailed analysis tasks")
    readme.append("")
    readme.append("## Contributing")
    readme.append("")
    readme.append("This index was automatically generated from agent file analysis. To update:")
    readme.append("")
    readme.append("1. Modify agent files in their respective category directories")
    readme.append("2. Run `python3 analyze_agents.py` to regenerate analysis")
    readme.append("3. Run `python3 generate_agent_readme.py` to update this README")
    readme.append("")
    readme.append("---")
    readme.append("")
    readme.append(f"*Last updated: {date.today().isoformat()}*")
    readme.append("")
    readme.append("**Source Repositories:**")
    readme.append("- [wshobson/agents](https://github.com/wshobson/agents) - MIT License")
    readme.append("")

    # Write to file
    output_file = AGENTS_DIR / "README.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme))

    print(f"\n{'='*80}")
    print(f"README.md generated successfully!")
    print(f"{'='*80}\n")
    print(f"Location: {output_file}")
    print(f"Total lines: {len(readme)}")
    print(f"Agents documented: {total_agents}")
    print(f"Categories: {len(categories)}")
    print(f"\n{'='*80}\n")

if __name__ == '__main__':
    generate_readme()
