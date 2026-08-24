---
name: changelog-automation
description: Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizing commit conventions.
metadata:
  tags:
    - automation
    - changelog
  updated: "2026-04-11"
---
# Changelog Automation

Patterns and tools for automating changelog generation, release notes, and version management following industry standards.

## When to Use This Skill

- Setting up automated changelog generation
- Implementing Conventional Commits
- Creating release note workflows
- Standardizing commit message formats
- Generating GitHub/GitLab release notes
- Managing semantic versioning

## Core Concepts

### 1. Keep a Changelog Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature X

## [1.2.0] - 2024-01-15

### Added
- User profile avatars
- Dark mode support

### Changed
- Improved loading performance by 40%

### Deprecated
- Old authentication API (use v2)

### Removed
- Legacy payment gateway

### Fixed
- Login timeout issue (#123)

### Security
- Updated dependencies for CVE-2024-1234

[Unreleased]: https://github.com/user/repo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/user/repo/compare/v1.1.0...v1.2.0
```

### 2. Conventional Commits

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

| Type | Description | Changelog Section |
|------|-------------|-------------------|
| `feat` | New feature | Added |
| `fix` | Bug fix | Fixed |
| `docs` | Documentation | (usually excluded) |
| `style` | Formatting | (usually excluded) |
| `refactor` | Code restructure | Changed |
| `perf` | Performance | Changed |
| `test` | Tests | (usually excluded) |
| `chore` | Maintenance | (usually excluded) |
| `ci` | CI changes | (usually excluded) |
| `build` | Build system | (usually excluded) |
| `revert` | Revert commit | Removed |

### 3. Semantic Versioning

```
MAJOR.MINOR.PATCH

MAJOR: Breaking changes (feat! or BREAKING CHANGE)
MINOR: New features (feat)
PATCH: Bug fixes (fix)
```

## Implementation

### Method 1: Conventional Changelog (Node.js)

```bash
# Install tools
npm install -D @commitlint/cli @commitlint/config-conventional
npm install -D husky
npm install -D standard-version
# or
npm install -D semantic-release

# Setup commitlint
cat > commitlint.config.js << 'EOF'
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'chore',
        'ci',
        'build',
        'revert',
      ],
    ],
    'subject-case': [2, 'never', ['start-case', 'pascal-case', 'upper-case']],
    'subject-max-length': [2, 'always', 72],
  },
};
EOF

# Setup husky
npx husky init
echo "npx --no -- commitlint --edit \$1" > .husky/commit-msg
```

### Method 2: standard-version Configuration

```javascript
// .versionrc.js
module.exports = {
  types: [
    { type: 'feat', section: 'Features' },
    { type: 'fix', section: 'Bug Fixes' },
    { type: 'perf', section: 'Performance Improvements' },
    { type: 'revert', section: 'Reverts' },
    { type: 'docs', section: 'Documentation', hidden: true },
    { type: 'style', section: 'Styles', hidden: true },
    { type: 'chore', section: 'Miscellaneous', hidden: true },
    { type: 'refactor', section: 'Code Refactoring', hidden: true },
    { type: 'test', section: 'Tests', hidden: true },
    { type: 'build', section: 'Build System', hidden: true },
    { type: 'ci', section: 'CI/CD', hidden: true },
  ],
  commitUrlFormat: '{{host}}/{{owner}}/{{repository}}/commit/{{hash}}',
  compareUrlFormat: '{{host}}/{{owner}}/{{repository}}/compare/{{previousTag}}...{{currentTag}}',
  issueUrlFormat: '{{host}}/{{owner}}/{{repository}}/issues/{{id}}',
  userUrlFormat: '{{host}}/{{user}}',
  releaseCommitMessageFormat: 'chore(release): {{currentTag}}',
  scripts: {
    prebump: 'echo "Running prebump"',
    postbump: 'echo "Running postbump"',
    prechangelog: 'echo "Running prechangelog"',
    postchangelog: 'echo "Running postchangelog"',
  },
};
```

```json
// package.json scripts
{
  "scripts": {
    "release": "standard-version",
    "release:minor": "standard-version --release-as minor",
    "release:major": "standard-version --release-as major",
    "release:patch": "standard-version --release-as patch",
    "release:dry": "standard-version --dry-run"
  }
}
```

## Advanced Methods and Templates

Full configurations for semantic-release (multi-branch with alpha/beta + 6-plugin pipeline for commit analysis, release notes, changelog, npm publish, GitHub releases, and git commit-back), GitHub Actions release workflow (automatic on push to main + manual `workflow_dispatch` with release type selection), git-cliff (Rust-based fast generation with Tera templating and `cliff.toml`), Python commitizen (pyproject.toml config with custom schema + interactive `cz commit` workflow); plus GitHub Release Template (with contributor attribution) and Internal Release Notes Template (highlights, breaking changes, upgrade guide, dependencies table); and Commit Message Examples (feature with scope, fix with issue reference, breaking change with migration guide, multi-paragraph with review footer).

See [references/advanced-methods-and-templates.md](references/advanced-methods-and-templates.md)

## Best Practices

### Do's
- **Follow Conventional Commits** - Enables automation
- **Write clear messages** - Future you will thank you
- **Reference issues** - Link commits to tickets
- **Use scopes consistently** - Define team conventions
- **Automate releases** - Reduce manual errors

### Don'ts
- **Don't mix changes** - One logical change per commit
- **Don't skip validation** - Use commitlint
- **Don't manual edit** - Generated changelogs only
- **Don't forget breaking changes** - Mark with `!` or footer
- **Don't ignore CI** - Validate commits in pipeline

## Resources

- [Keep a Changelog](https://keepachangelog.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [semantic-release](https://semantic-release.gitbook.io/)
- [git-cliff](https://git-cliff.org/)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-methods-and-templates.md` | Methods 3–6 (semantic-release, GitHub Actions, git-cliff, commitizen), Release Notes Templates (GitHub + internal), and Commit Message Examples |
