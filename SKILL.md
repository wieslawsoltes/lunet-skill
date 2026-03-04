---
name: lunet-static-site-docs-and-api-docs
description: Build and maintain Lunet static websites with first-class documentation and .NET API reference pages. Use when tasks involve `config.scriban`, plugin/module configuration, docs section authoring, menu/layout wiring, `api.dotnet` setup, `xref` linking, or Lunet feature/API lookup for either regular site projects or Lunet source contributions.
---

# Lunet Static Sites and API Docs

Use this skill to deliver Lunet documentation sites and API reference sections with practical, production-ready patterns.

Primary references:
- `references/major-features/README.md`
- `references/major-features/01-bootstrap-and-site-structure.md`
- `references/major-features/02-configuration-and-environments.md`
- `references/major-features/03-content-layouts-markdown-and-includes.md`
- `references/major-features/04-data-menus-and-taxonomies.md`
- `references/major-features/05-resources-bundles-scss-and-minifier.md`
- `references/major-features/06-search-rss-sitemaps-cards-and-tracking.md`
- `references/major-features/07-api-dotnet-end-to-end.md`
- `references/major-features/08-dev-workflow-ci-and-troubleshooting.md`

Source-level references (optional, only when Lunet source is available):
- `references/build-and-docs-workflow.md`
- `references/feature-map.md`
- `references/public-api-index.md`

## Operating Modes

1. Site Project Mode (default)
- Use this when the user does not have Lunet source cloned and only needs to build a site.
- Rely on `references/major-features/*.md`.
- Use `lunet` as an installed .NET tool.

2. Lunet Source Mode (optional)
- Use this when the user is modifying Lunet itself.
- Rely on `references/feature-map.md` and `references/public-api-index.md`.
- Use repository build/test workflow in `references/build-and-docs-workflow.md`.

## Workflow

1. Determine mode first.
- If task is about creating or editing a Lunet site, stay in Site Project Mode.
- If task explicitly targets Lunet internals/modules/source files, switch to Source Mode.

2. In Site Project Mode, implement by feature area.
- Bootstrap and structure: `references/major-features/01-bootstrap-and-site-structure.md`
- Config/environments: `references/major-features/02-configuration-and-environments.md`
- Content/layouts/markdown/includes: `references/major-features/03-content-layouts-markdown-and-includes.md`
- Data/navigation/taxonomies: `references/major-features/04-data-menus-and-taxonomies.md`
- Asset pipeline: `references/major-features/05-resources-bundles-scss-and-minifier.md`
- Discovery/SEO features: `references/major-features/06-search-rss-sitemaps-cards-and-tracking.md`
- .NET API docs: `references/major-features/07-api-dotnet-end-to-end.md`
- Dev loop/CI/troubleshooting: `references/major-features/08-dev-workflow-ci-and-troubleshooting.md`

3. In Source Mode, map behavior to modules and API.
- Read `references/feature-map.md` for module registration and docs mapping.
- Read `references/public-api-index.md` and assembly files under `references/api/*.md`.
- Use `references/build-and-docs-workflow.md` for build/test/site dogfooding commands.

4. Keep API docs deterministic.
- Configure `api.dotnet` with explicit `projects`, `path`, `menu_name`, and `config`.
- Use `apidocs/*.md` + `uid` for namespace/type/member supplemental docs when needed.
- Validate generated `/api` page tree and xref links.

5. Validate outputs and integration.
- Run build/serve/watch cycles and verify generated files, menus, links, and feeds.
- Check environment-specific behavior (dev vs prod) for tracking/minification and related features.

6. Regenerate references only when source/API mapping changed.
- Run:
```bash
python3 scripts/generate_lunet_references.py \
  --repo /path/to/lunet \
  --output references
```
- This refreshes:
  - `references/feature-map.md`
  - `references/public-api-index.md`
  - `references/api/*.md`
  - `references/api-summary.json`
  - `references/api/summary.json`

## API and Feature Lookup Patterns

- `rg -n "api\\.dotnet|xref|layout_type" .`
- `rg -n "bundle|scss|minify|resource" .`
- `rg -n "search|rss|sitemap|cards|tracking" .`
- `rg -n "SiteObject|SiteRunner|SiteApplication" references/api/*.md`
- `rg -n "class .*Module|class .*Plugin" src/Lunet.*/*.cs` (Source Mode)

## Execution Rules

- Do not assume a local Lunet source clone unless the task explicitly involves Lunet source code.
- Prefer Site Project Mode references first; switch to Source Mode only when needed.
- Keep changes minimal and feature-focused; avoid unrelated refactors.
- Add or update tests for behavior changes in Source Mode.
- Keep user-facing documentation in sync with behavior changes.
- Avoid machine-local paths in generated or committed reference files.
