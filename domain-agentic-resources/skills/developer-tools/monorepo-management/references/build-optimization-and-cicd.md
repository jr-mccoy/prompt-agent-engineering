# Monorepo Management — Build Optimization, CI/CD, and Publishing

## Build Optimization

### Turborepo Caching

```json
// turbo.json
{
  "pipeline": {
    "build": {
      // Build depends on dependencies being built first
      "dependsOn": ["^build"],

      // Cache these outputs
      "outputs": ["dist/**", ".next/**"],

      // Cache based on these inputs (default: all files)
      "inputs": ["src/**/*.tsx", "src/**/*.ts", "package.json"]
    },
    "test": {
      // Run tests in parallel, don't depend on build
      "cache": true,
      "outputs": ["coverage/**"]
    }
  }
}
```

### Remote Caching

```bash
# Turborepo Remote Cache (Vercel)
npx turbo login
npx turbo link

# Custom remote cache
# turbo.json
{
  "remoteCache": {
    "signature": true,
    "enabled": true
  }
}
```

---

## CI/CD for Monorepos

### GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # For Nx affected commands

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Build
        run: pnpm turbo run build

      - name: Test
        run: pnpm turbo run test

      - name: Lint
        run: pnpm turbo run lint

      - name: Type check
        run: pnpm turbo run type-check
```

### Deploy Affected Only

```yaml
# Deploy only changed apps
- name: Deploy affected apps
  run: |
    if pnpm nx affected:apps --base=origin/main --head=HEAD | grep -q "web"; then
      echo "Deploying web app"
      pnpm --filter web deploy
    fi
```

---

## Best Practices

1. **Consistent Versioning**: Lock dependency versions across workspace
2. **Shared Configs**: Centralize ESLint, TypeScript, Prettier configs
3. **Dependency Graph**: Keep it acyclic, avoid circular dependencies
4. **Cache Effectively**: Configure inputs/outputs correctly
5. **Type Safety**: Share types between frontend/backend
6. **Testing Strategy**: Unit tests in packages, E2E in apps
7. **Documentation**: README in each package
8. **Release Strategy**: Use changesets for versioning

## Common Pitfalls

- **Circular Dependencies**: A depends on B, B depends on A
- **Phantom Dependencies**: Using deps not in package.json
- **Incorrect Cache Inputs**: Missing files in Turborepo inputs
- **Over-Sharing**: Sharing code that should be separate
- **Under-Sharing**: Duplicating code across packages
- **Large Monorepos**: Without proper tooling, builds slow down

---

## Publishing Packages

```bash
# Using Changesets
pnpm add -Dw @changesets/cli
pnpm changeset init

# Create changeset
pnpm changeset

# Version packages
pnpm changeset version

# Publish
pnpm changeset publish
```

```yaml
# .github/workflows/release.yml
- name: Create Release Pull Request or Publish
  uses: changesets/action@v1
  with:
    publish: pnpm release
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```
