---
name: uv-package-manager
description: Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when setting up Python projects, managing dependencies, or optimizing Python development workflows with uv.
metadata:
  tags:
    - manager
    - package
    - programming-languages
    - python
  updated: "2026-04-11"
---
# UV Package Manager

Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows.

## When to Use This Skill

- Setting up new Python projects quickly
- Managing Python dependencies faster than pip
- Creating and managing virtual environments
- Installing Python interpreters
- Resolving dependency conflicts efficiently
- Migrating from pip/pip-tools/poetry
- Speeding up CI/CD pipelines
- Managing monorepo Python projects
- Working with lockfiles for reproducible builds
- Optimizing Docker builds with Python dependencies

## Core Concepts

### 1. What is uv?
- **Ultra-fast package installer**: 10-100x faster than pip
- **Written in Rust**: Leverages Rust's performance
- **Drop-in pip replacement**: Compatible with pip workflows
- **Virtual environment manager**: Create and manage venvs
- **Python installer**: Download and manage Python versions
- **Resolver**: Advanced dependency resolution
- **Lockfile support**: Reproducible installations

### 2. Key Features
- Blazing fast installation speeds
- Disk space efficient with global cache
- Compatible with pip, pip-tools, poetry
- Comprehensive dependency resolution
- Cross-platform support (Linux, macOS, Windows)
- No Python required for installation
- Built-in virtual environment support

### 3. UV vs Traditional Tools
- **vs pip**: 10-100x faster, better resolver
- **vs pip-tools**: Faster, simpler, better UX
- **vs poetry**: Faster, less opinionated, lighter
- **vs conda**: Faster, Python-focused

## Installation

### Quick Install

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Using pip (if you already have Python)
pip install uv

# Using Homebrew (macOS)
brew install uv

# Using cargo (if you have Rust)
cargo install --git https://github.com/astral-sh/uv uv
```

### Verify Installation

```bash
uv --version
# uv 0.x.x
```

## Quick Start

### Create a New Project

```bash
# Create new project with virtual environment
uv init my-project
cd my-project

# Or create in current directory
uv init .

# Initialize creates:
# - .python-version (Python version)
# - pyproject.toml (project config)
# - README.md
# - .gitignore
```

### Install Dependencies

```bash
# Install packages (creates venv if needed)
uv add requests pandas

# Install dev dependencies
uv add --dev pytest black ruff

# Install from requirements.txt
uv pip install -r requirements.txt

# Install from pyproject.toml
uv sync
```

## Virtual Environment Management

### Pattern 1: Creating Virtual Environments

```bash
# Create virtual environment with uv
uv venv

# Create with specific Python version
uv venv --python 3.12

# Create with custom name
uv venv my-env

# Create with system site packages
uv venv --system-site-packages

# Specify location
uv venv /path/to/venv
```

### Pattern 2: Activating Virtual Environments

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Or use uv run (no activation needed)
uv run python script.py
uv run pytest
```

### Pattern 3: Using uv run

```bash
# Run Python script (auto-activates venv)
uv run python app.py

# Run installed CLI tool
uv run black .
uv run pytest

# Run with specific Python version
uv run --python 3.11 python script.py

# Pass arguments
uv run python script.py --arg value
```

## Package Management

### Pattern 4: Adding Dependencies

```bash
# Add package (adds to pyproject.toml)
uv add requests

# Add with version constraint
uv add "django>=4.0,<5.0"

# Add multiple packages
uv add numpy pandas matplotlib

# Add dev dependency
uv add --dev pytest pytest-cov

# Add optional dependency group
uv add --optional docs sphinx

# Add from git
uv add git+https://github.com/user/repo.git

# Add from git with specific ref
uv add git+https://github.com/user/repo.git@v1.0.0

# Add from local path
uv add ./local-package

# Add editable local package
uv add -e ./local-package
```

### Pattern 5: Removing Dependencies

```bash
# Remove package
uv remove requests

# Remove dev dependency
uv remove --dev pytest

# Remove multiple packages
uv remove numpy pandas matplotlib
```

### Pattern 6: Upgrading Dependencies

```bash
# Upgrade specific package
uv add --upgrade requests

# Upgrade all packages
uv sync --upgrade

# Upgrade package to latest
uv add --upgrade requests

# Show what would be upgraded
uv tree --outdated
```

### Pattern 7: Locking Dependencies

```bash
# Generate uv.lock file
uv lock

# Update lock file
uv lock --upgrade

# Lock without installing
uv lock --no-install

# Lock specific package
uv lock --upgrade-package requests
```

## Python Version Management

### Pattern 8: Installing Python Versions

```bash
# Install Python version
uv python install 3.12

# Install multiple versions
uv python install 3.11 3.12 3.13

# Install latest version
uv python install

# List installed versions
uv python list

# Find available versions
uv python list --all-versions
```

### Pattern 9: Setting Python Version

```bash
# Set Python version for project
uv python pin 3.12

# This creates/updates .python-version file

# Use specific Python version for command
uv --python 3.11 run python script.py

# Create venv with specific version
uv venv --python 3.12
```

## Project Configuration

### Pattern 10: pyproject.toml with uv

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
    "click>=8.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]
docs = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    # Additional dev dependencies managed by uv
]

[tool.uv.sources]
# Custom package sources
my-package = { git = "https://github.com/user/repo.git" }
```

### Pattern 11: Using uv with Existing Projects

```bash
# Migrate from requirements.txt
uv add -r requirements.txt

# Migrate from poetry
# Already have pyproject.toml, just use:
uv sync

# Export to requirements.txt
uv pip freeze > requirements.txt

# Export with hashes
uv pip freeze --require-hashes > requirements.txt
```

## CI/CD Integration

### Pattern 13: GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v2
        with:
          enable-cache: true

      - name: Set up Python
        run: uv python install 3.12

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Run tests
        run: uv run pytest

      - name: Run linting
        run: |
          uv run ruff check .
          uv run black --check .
```

## Advanced Workflows and Integrations

Monorepo workspace support, Docker multi-stage builds, lockfile management, performance optimization (global cache, parallel install, offline mode), tool integration (pre-commit hooks, VS Code settings), troubleshooting, migration from pip/poetry/pip-tools, and comparison with other tools.

See [references/advanced-workflows-and-integrations.md](references/advanced-workflows-and-integrations.md)

## Common Workflows

### Pattern 19: Starting a New Project

```bash
# Complete workflow
uv init my-project
cd my-project

# Set Python version
uv python pin 3.12

# Add dependencies
uv add fastapi uvicorn pydantic

# Add dev dependencies
uv add --dev pytest black ruff mypy

# Create structure
mkdir -p src/my_project tests

# Run tests
uv run pytest

# Format code
uv run black .
uv run ruff check .
```

### Pattern 20: Maintaining Existing Project

```bash
# Clone repository
git clone https://github.com/user/project.git
cd project

# Install dependencies (creates venv automatically)
uv sync

# Install with dev dependencies
uv sync --all-extras

# Update dependencies
uv lock --upgrade

# Run application
uv run python app.py

# Run tests
uv run pytest

# Add new dependency
uv add new-package

# Commit updated files
git add pyproject.toml uv.lock
git commit -m "Add new-package dependency"
```

## Command Reference

### Essential Commands

```bash
# Project management
uv init [PATH]              # Initialize project
uv add PACKAGE              # Add dependency
uv remove PACKAGE           # Remove dependency
uv sync                     # Install dependencies
uv lock                     # Create/update lockfile

# Virtual environments
uv venv [PATH]              # Create venv
uv run COMMAND              # Run in venv

# Python management
uv python install VERSION   # Install Python
uv python list              # List installed Pythons
uv python pin VERSION       # Pin Python version

# Package installation (pip-compatible)
uv pip install PACKAGE      # Install package
uv pip uninstall PACKAGE    # Uninstall package
uv pip freeze               # List installed
uv pip list                 # List packages

# Utility
uv cache clean              # Clear cache
uv cache dir                # Show cache location
uv --version                # Show version
```

## Resources

- **Official documentation**: https://docs.astral.sh/uv/
- **GitHub repository**: https://github.com/astral-sh/uv
- **Astral blog**: https://astral.sh/blog
- **Migration guides**: https://docs.astral.sh/uv/guides/
- **Comparison with other tools**: https://docs.astral.sh/uv/pip/compatibility/

## Best Practices Summary

1. **Use uv for all new projects** - Start with `uv init`
2. **Commit lockfiles** - Ensure reproducible builds
3. **Pin Python versions** - Use .python-version
4. **Use uv run** - Avoid manual venv activation
5. **Leverage caching** - Let uv manage global cache
6. **Use --frozen in CI** - Exact reproduction
7. **Keep uv updated** - Fast-moving project
8. **Use workspaces** - For monorepo projects
9. **Export for compatibility** - Generate requirements.txt when needed
10. **Read the docs** - uv is feature-rich and evolving
