#!/usr/bin/env python3
"""
Generate comprehensive README.md for Claude Code commands based on analysis.
"""

import json
from pathlib import Path
from datetime import datetime

def format_command_entry(cmd):
    """Format a single command entry for the README."""
    lines = []

    # Command name as heading
    lines.append(f"### {cmd['name']}")
    lines.append("")

    # File path
    lines.append(f"**Path:** `{cmd['file_path']}`")
    lines.append("")

    # Syntax
    lines.append(f"**Syntax:** `{cmd['syntax']}`")
    lines.append("")

    # Description
    desc = cmd['description']
    if len(desc) > 300:
        desc = desc[:297] + "..."
    lines.append(f"**Description:** {desc}")
    lines.append("")

    # Orchestrated agents (if any)
    if cmd['agents']:
        lines.append(f"**Orchestrates:** {', '.join(f'`{agent}`' for agent in cmd['agents'][:10])}")
        if len(cmd['agents']) > 10:
            lines.append(f"  _(+ {len(cmd['agents']) - 10} more agents)_")
        lines.append("")

    # Related skills (if any)
    if cmd['skills']:
        lines.append(f"**Related Skills:** {', '.join(f'`{skill}`' for skill in cmd['skills'][:5])}")
        if len(cmd['skills']) > 5:
            lines.append(f"  _(+ {len(cmd['skills']) - 5} more skills)_")
        lines.append("")

    lines.append("---")
    lines.append("")

    return '\n'.join(lines)

def categorize_command(cmd):
    """Determine command complexity/type."""
    if 'orchestration' in cmd['category']:
        return 'Orchestration'
    elif len(cmd['agents']) >= 5:
        return 'Multi-Agent Workflow'
    elif len(cmd['agents']) >= 2:
        return 'Coordinated Workflow'
    elif cmd['agents']:
        return 'Single Agent'
    else:
        return 'Direct Execution'

def generate_readme(analysis_file, output_file):
    """Generate README.md from analysis JSON."""

    # Load analysis
    with open(analysis_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lines = []

    # Header
    lines.append("# Claude Code Commands Index")
    lines.append("")
    lines.append("**Total Commands:** 70 across 15 categories")
    lines.append("")
    lines.append(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of Contents
    lines.append("## Table of Contents")
    lines.append("")
    lines.append("- [Overview](#overview)")
    lines.append("- [What Are Commands?](#what-are-commands)")
    lines.append("- [Command Categories](#command-categories)")
    lines.append("- [Quick Reference by Category](#quick-reference-by-category)")

    # Add categories to TOC
    for category in sorted(data['categories']):
        category_name = category.replace('-', ' ').title()
        anchor = category.replace('_', '-').lower()
        count = len(data['commands_by_category'][category])
        lines.append(f"  - [{category_name} ({count})](#--{anchor})")

    lines.append("- [Command Types](#command-types)")
    lines.append("- [Usage Patterns](#usage-patterns)")
    lines.append("- [Integration Guide](#integration-guide)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Overview
    lines.append("## Overview")
    lines.append("")
    lines.append("Commands in Claude Code are **multi-agent orchestration workflows** that coordinate specialized agents to execute complex, multi-phase operations. Unlike simple prompts or single-purpose agents, commands represent entire development processes from architecture through deployment.")
    lines.append("")
    lines.append("**Key Characteristics:**")
    lines.append("- **Multi-phase workflows** with sequential agent coordination")
    lines.append("- **Output handoffs** where each agent consumes previous results")
    lines.append("- **Validation gates** ensuring quality at each phase")
    lines.append("- **Domain specialization** with expert agents for each task")
    lines.append("")

    # What Are Commands?
    lines.append("## What Are Commands?")
    lines.append("")
    lines.append("Commands are slash commands (e.g., `/full-stack-feature`, `/security-hardening`) that trigger comprehensive workflows. They differ from agents and skills:")
    lines.append("")
    lines.append("| Feature | Commands | Agents | Skills |")
    lines.append("|---------|----------|--------|--------|")
    lines.append("| **Purpose** | Multi-step orchestration | Specialized identity | Knowledge package |")
    lines.append("| **Scope** | End-to-end workflows | Single domain expertise | Progressive disclosure |")
    lines.append("| **Coordination** | Multiple agents | Single agent | Referenced by agents |")
    lines.append("| **Duration** | Long-running process | Per-task invocation | Always available |")
    lines.append("| **Example** | `/full-stack-feature` | `backend-architect` | `async-python-patterns` |")
    lines.append("")

    # Command Categories section
    lines.append("## Command Categories")
    lines.append("")
    lines.append("Commands are organized into 15 categories based on their primary domain:")
    lines.append("")

    # Create category statistics table
    lines.append("| Category | Count | Description |")
    lines.append("|----------|-------|-------------|")

    category_descriptions = {
        'orchestration': 'Multi-agent workflows for complex features',
        'security': 'Security scanning, hardening, and compliance',
        'testing': 'Test generation and TDD workflows',
        'devops': 'Infrastructure, CI/CD, and deployment',
        'troubleshooting': 'Debugging and incident response',
        'code-quality': 'Code review and refactoring',
        'performance': 'Performance analysis and optimization',
        'git-workflows': 'Git operations and PR management',
        'framework-migration': 'Framework upgrades and migrations',
        'other': 'Miscellaneous development commands',
        'accessibility': 'Accessibility compliance and testing',
        'architecture': 'Architecture design and documentation',
        'database': 'Database design and optimization',
        'deployment': 'Deployment and configuration',
        'documentation': 'Documentation generation',
    }

    for category in sorted(data['categories'], key=lambda c: len(data['commands_by_category'][c]), reverse=True):
        count = len(data['commands_by_category'][category])
        desc = category_descriptions.get(category, 'Various development commands')
        category_name = category.replace('-', ' ').title()
        lines.append(f"| {category_name} | {count} | {desc} |")

    lines.append("")

    # Quick Reference
    lines.append("## Quick Reference by Category")
    lines.append("")
    lines.append("Jump to any category:")
    lines.append("")

    for category in sorted(data['categories']):
        category_name = category.replace('-', ' ').title()
        anchor = category.replace('_', '-').lower()
        count = len(data['commands_by_category'][category])
        lines.append(f"- **[{category_name}](#--{anchor})** - {count} command{'s' if count != 1 else ''}")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Commands by category
    lines.append("## Commands by Category")
    lines.append("")

    # Sort categories with orchestration first, then by command count
    def category_sort_key(cat):
        if cat == 'orchestration':
            return (0, -len(data['commands_by_category'][cat]))
        elif cat == 'security':
            return (1, -len(data['commands_by_category'][cat]))
        elif cat == 'testing':
            return (2, -len(data['commands_by_category'][cat]))
        else:
            return (3, -len(data['commands_by_category'][cat]))

    sorted_categories = sorted(data['categories'], key=category_sort_key)

    for category in sorted_categories:
        commands = sorted(data['commands_by_category'][category], key=lambda c: c['name'])

        # Category header
        category_name = category.replace('-', ' ').title()
        lines.append(f"### 🔹 {category_name}")
        lines.append("")
        lines.append(f"**{len(commands)} command{'s' if len(commands) != 1 else ''}**")
        lines.append("")

        # Commands in this category
        for cmd in commands:
            lines.append(format_command_entry(cmd))

    # Command Types section
    lines.append("## Command Types")
    lines.append("")
    lines.append("Commands can be categorized by their coordination patterns:")
    lines.append("")

    # Categorize all commands
    orchestration_cmds = []
    multi_agent_cmds = []
    coordinated_cmds = []
    single_agent_cmds = []
    direct_cmds = []

    for category in data['categories']:
        for cmd in data['commands_by_category'][category]:
            cmd_type = categorize_command(cmd)
            if cmd_type == 'Orchestration':
                orchestration_cmds.append(cmd)
            elif cmd_type == 'Multi-Agent Workflow':
                multi_agent_cmds.append(cmd)
            elif cmd_type == 'Coordinated Workflow':
                coordinated_cmds.append(cmd)
            elif cmd_type == 'Single Agent':
                single_agent_cmds.append(cmd)
            else:
                direct_cmds.append(cmd)

    lines.append(f"### Orchestration Commands ({len(orchestration_cmds)})")
    lines.append("")
    lines.append("Complex multi-phase workflows coordinating 5+ specialized agents:")
    lines.append("")
    for cmd in sorted(orchestration_cmds, key=lambda c: c['name'])[:10]:
        lines.append(f"- `{cmd['syntax']}` - {len(cmd['agents'])} agents")
    if len(orchestration_cmds) > 10:
        lines.append(f"- _(+ {len(orchestration_cmds) - 10} more)_")
    lines.append("")

    lines.append(f"### Multi-Agent Workflows ({len(multi_agent_cmds)})")
    lines.append("")
    lines.append("Workflows coordinating 2-4 agents for focused tasks:")
    lines.append("")
    for cmd in sorted(multi_agent_cmds, key=lambda c: c['name'])[:10]:
        lines.append(f"- `{cmd['syntax']}` - {len(cmd['agents'])} agents")
    if len(multi_agent_cmds) > 10:
        lines.append(f"- _(+ {len(multi_agent_cmds) - 10} more)_")
    lines.append("")

    lines.append(f"### Single-Agent Commands ({len(single_agent_cmds)})")
    lines.append("")
    lines.append("Commands that invoke a single specialized agent:")
    lines.append("")
    for cmd in sorted(single_agent_cmds, key=lambda c: c['name'])[:10]:
        agent_info = f" - {cmd['agents'][0]}" if cmd['agents'] else ""
        lines.append(f"- `{cmd['syntax']}`{agent_info}")
    if len(single_agent_cmds) > 10:
        lines.append(f"- _(+ {len(single_agent_cmds) - 10} more)_")
    lines.append("")

    lines.append(f"### Direct Execution Commands ({len(direct_cmds)})")
    lines.append("")
    lines.append("Commands that execute without explicit agent coordination:")
    lines.append("")
    for cmd in sorted(direct_cmds, key=lambda c: c['name'])[:10]:
        lines.append(f"- `{cmd['syntax']}`")
    if len(direct_cmds) > 10:
        lines.append(f"- _(+ {len(direct_cmds) - 10} more)_")
    lines.append("")

    # Usage Patterns
    lines.append("## Usage Patterns")
    lines.append("")
    lines.append("### Basic Command Invocation")
    lines.append("")
    lines.append("```bash")
    lines.append("# Simple command")
    lines.append("/command-name")
    lines.append("")
    lines.append("# Command with arguments")
    lines.append("/command-name \"implement user authentication\"")
    lines.append("")
    lines.append("# Command with context")
    lines.append("/full-stack-feature \"add payment processing with Stripe\"")
    lines.append("```")
    lines.append("")

    lines.append("### Workflow Execution")
    lines.append("")
    lines.append("Commands execute in phases with validation gates:")
    lines.append("")
    lines.append("```")
    lines.append("Phase 1: Planning & Architecture")
    lines.append("  ↓ (validation gate)")
    lines.append("Phase 2: Implementation")
    lines.append("  ↓ (validation gate)")
    lines.append("Phase 3: Testing & Verification")
    lines.append("  ↓ (validation gate)")
    lines.append("Phase 4: Deployment & Monitoring")
    lines.append("```")
    lines.append("")

    # Integration Guide
    lines.append("## Integration Guide")
    lines.append("")
    lines.append("### When to Use Commands vs Agents vs Skills")
    lines.append("")
    lines.append("**Use Commands when:**")
    lines.append("- You need end-to-end feature development")
    lines.append("- Multiple specialized agents must coordinate")
    lines.append("- Workflow has distinct phases with validation")
    lines.append("- You want automated quality gates")
    lines.append("")
    lines.append("**Use Agents when:**")
    lines.append("- You need focused expertise in one domain")
    lines.append("- Task requires persistent identity/context")
    lines.append("- You're building a custom workflow")
    lines.append("")
    lines.append("**Use Skills when:**")
    lines.append("- You need reference knowledge on demand")
    lines.append("- Domain expertise requires bundled resources")
    lines.append("- You want progressive disclosure of information")
    lines.append("")

    lines.append("### Installation")
    lines.append("")
    lines.append("Commands are available in your Claude Code environment at:")
    lines.append("")
    lines.append("```")
    lines.append("claude-code-resources/commands/")
    lines.append("├── orchestration/")
    lines.append("├── security/")
    lines.append("├── testing/")
    lines.append("├── devops/")
    lines.append("└── [other categories]/")
    lines.append("```")
    lines.append("")

    lines.append("### Related Resources")
    lines.append("")
    lines.append("- **[Agents Index](../agents/README.md)** - 158 specialized agents")
    lines.append("- **[Skills Index](../skills/README.md)** - 132 knowledge packages")
    lines.append("- **[Integration Guide](../documentation/INTEGRATION_WITH_PROMPTS.md)** - How commands work with prompts")
    lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("Commands sourced from:")
    lines.append("- [wshobson/agents](https://github.com/wshobson/agents) - MIT License")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Write to file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"✅ Generated README with {len(lines)} lines")
    print(f"📄 Output: {output_path}")

    return len(lines)

def main():
    """Main generator function."""
    script_dir = Path(__file__).parent
    analysis_file = script_dir / 'commands_analysis.json'
    output_file = script_dir / 'README.md'

    if not analysis_file.exists():
        print(f"❌ Analysis file not found: {analysis_file}")
        print("   Run analyze_commands.py first")
        return 1

    print("Generating Commands Index README...")
    line_count = generate_readme(analysis_file, output_file)

    print(f"\n✅ Commands Index README generated successfully!")
    print(f"   Total lines: {line_count}")
    print(f"   Location: {output_file}")

    return 0

if __name__ == '__main__':
    exit(main())
