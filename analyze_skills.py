#!/usr/bin/env python3
"""
Analyze all skills in claude-code-resources/skills/ directory.
Extracts metadata from SKILL.md files and bundled resources.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"').strip("'")
    return frontmatter

def extract_description(content, frontmatter):
    """Extract description from frontmatter or content."""
    # Try frontmatter first
    if 'description' in frontmatter:
        return frontmatter['description']

    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    # Look for first substantial paragraph
    lines = content.strip().split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line and not line.startswith('#') and len(line) > 50:
            # Clean up markdown
            desc = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
            desc = re.sub(r'[*_`]', '', desc)
            return desc[:200] + ('...' if len(desc) > 200 else '')

    return "No description available"

def analyze_bundled_resources(skill_path):
    """Analyze what resources are bundled with the skill."""
    resources = {
        'scripts': [],
        'references': [],
        'assets': [],
        'other': []
    }

    # Check for common resource directories
    for subdir in ['scripts', 'references', 'assets', 'examples', 'templates']:
        subdir_path = skill_path / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            files = list(subdir_path.rglob('*'))
            files = [f for f in files if f.is_file()]
            if files:
                category = subdir if subdir in resources else 'other'
                resources[category] = [f.name for f in files]

    # Check for standalone files
    for item in skill_path.iterdir():
        if item.is_file() and item.name not in ['SKILL.md', '.gitkeep']:
            resources['other'].append(item.name)

    return resources

def extract_dependencies(content):
    """Extract dependencies mentioned in the skill."""
    dependencies = set()

    # Common dependency indicators
    patterns = [
        r'requires?\s+([a-zA-Z0-9\-_\.]+)',
        r'install\s+([a-zA-Z0-9\-_\.]+)',
        r'using\s+([a-zA-Z0-9\-_\.]+)',
        r'depends?\s+on\s+([a-zA-Z0-9\-_\.]+)',
    ]

    content_lower = content.lower()

    # Look for common tools
    common_tools = [
        'docker', 'kubernetes', 'terraform', 'aws', 'gcp', 'azure',
        'python', 'node', 'npm', 'yarn', 'pnpm', 'go', 'rust', 'java',
        'git', 'github', 'gitlab', 'gh cli', 'jest', 'pytest', 'vitest',
        'react', 'vue', 'angular', 'svelte', 'next.js', 'nuxt',
        'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch',
        'kafka', 'rabbitmq', 'grpc', 'graphql', 'rest',
    ]

    for tool in common_tools:
        if tool.lower() in content_lower:
            dependencies.add(tool)

    return sorted(list(dependencies))

def analyze_skill(skill_path, base_path):
    """Analyze a single skill directory."""
    skill_md = skill_path / 'SKILL.md'

    if not skill_md.exists():
        return None

    with open(skill_md, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    frontmatter = extract_frontmatter(content)
    description = extract_description(content, frontmatter)
    resources = analyze_bundled_resources(skill_path)
    dependencies = extract_dependencies(content)

    # Count total files
    has_resources = any(len(v) > 0 for v in resources.values())

    return {
        'name': skill_path.name,
        'path': str(skill_path.relative_to(base_path)),
        'description': description,
        'frontmatter': frontmatter,
        'bundled_resources': resources,
        'has_bundled_resources': has_resources,
        'dependencies': dependencies,
        'content_length': len(content),
    }

def main():
    base_path = Path.cwd()
    skills_dir = base_path / 'domain-agentic-resources/skills'

    if not skills_dir.exists():
        print(f"Error: {skills_dir} not found")
        return

    # Organize by category
    skills_by_category = defaultdict(list)
    all_skills = []

    # Find all skill directories (those containing SKILL.md)
    for category_dir in sorted(skills_dir.iterdir()):
        if not category_dir.is_dir():
            continue

        category_name = category_dir.name

        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir():
                continue

            skill_data = analyze_skill(skill_dir, base_path)
            if skill_data:
                skill_data['category'] = category_name
                skills_by_category[category_name].append(skill_data)
                all_skills.append(skill_data)

    # Generate statistics
    print("=" * 80)
    print("SKILLS ANALYSIS SUMMARY")
    print("=" * 80)
    print(f"\nTotal Skills: {len(all_skills)}")
    print(f"Total Categories: {len(skills_by_category)}")

    print("\n" + "=" * 80)
    print("SKILLS BY CATEGORY")
    print("=" * 80)
    for category, skills in sorted(skills_by_category.items()):
        print(f"\n{category}: {len(skills)} skills")
        for skill in skills:
            resources_indicator = " [+resources]" if skill['has_bundled_resources'] else ""
            print(f"  - {skill['name']}{resources_indicator}")

    print("\n" + "=" * 80)
    print("SKILLS WITH BUNDLED RESOURCES")
    print("=" * 80)
    skills_with_resources = [s for s in all_skills if s['has_bundled_resources']]
    print(f"\nTotal: {len(skills_with_resources)} skills")
    for skill in skills_with_resources:
        print(f"\n{skill['name']} ({skill['category']})")
        for res_type, files in skill['bundled_resources'].items():
            if files:
                print(f"  {res_type}: {len(files)} files - {', '.join(files[:3])}")

    print("\n" + "=" * 80)
    print("COMMON DEPENDENCIES")
    print("=" * 80)
    all_deps = defaultdict(int)
    for skill in all_skills:
        for dep in skill['dependencies']:
            all_deps[dep] += 1

    for dep, count in sorted(all_deps.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{dep}: {count} skills")

    # Save to JSON for further processing
    output_file = 'skills_analysis.json'
    with open(output_file, 'w') as f:
        json.dump({
            'total_skills': len(all_skills),
            'total_categories': len(skills_by_category),
            'skills_by_category': {k: [s['name'] for s in v] for k, v in skills_by_category.items()},
            'all_skills': all_skills
        }, f, indent=2)

    print(f"\n\nDetailed analysis saved to: {output_file}")
    print("=" * 80)

if __name__ == '__main__':
    main()
