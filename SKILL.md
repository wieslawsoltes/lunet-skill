---
name: lunet-static-site-docs-and-api-docs
description: Configure and troubleshoot Lunet static sites using docs-first workflows focused on `config.scriban`, content front matter, `menu.yml`, layouts/includes, full plugin configuration, deployment, and build/serve behavior. Use for Lunet site setup and maintenance; handle `api.dotnet` only when the user explicitly asks for API documentation features.
---

# Lunet Docs-First Site Configuration

Use this skill as a navigation layer to official Lunet documentation, not as a duplicate of the docs.

Core references:
- `references/lunet-docs-map.md`
- `references/major-feature-usage-playbooks.md`
- `references/config-menu-frontmatter-checklists.md`

## Working Principle

- Treat [lunet.io docs](https://lunet.io/docs/) as source of truth.
- Prefer linking users to the exact doc section over re-explaining large blocks of knowledge.
- Do not rely on local Lunet repository paths in guidance.

## Workflow

1. Classify the request by area, then pick one playbook from `references/major-feature-usage-playbooks.md`.
- `config.scriban`
- page/front matter/content
- `menu.yml` or navigation
- layouts/includes/themes
- plugin configuration (all modules listed in `references/lunet-docs-map.md`)
- CLI/build/serve/watch behavior
- deployment/CI (GitHub Actions)
- optional: `api.dotnet`

2. Open the matching official docs from `references/lunet-docs-map.md` before proposing changes.
- Use the smallest set of relevant pages.
- Quote configuration patterns minimally and adapt to the user’s files.
- For broad requests, first use the feature matrix in `references/lunet-docs-map.md` to confirm complete coverage.

3. Apply minimal, file-focused edits.
- Prioritize correctness of:
  - `config.scriban`
  - `menu.yml`
  - front matter blocks (`--- ... ---`)
  - layout/include paths

4. Validate behavior with Lunet commands.
- Typical checks:
  - `lunet build`
  - `lunet serve`
  - `lunet build --dev` (for environment-sensitive behavior)

5. Run the checklists in `references/config-menu-frontmatter-checklists.md` for touched surfaces.

6. Report outcome with doc anchors.
- Mention which doc pages were used.
- Summarize concrete file changes and how they map to docs guidance.

## Scope Guardrails

- Do not default to deep .NET API extraction/reference work.
- Use `api.dotnet` guidance only when user asks for API documentation generation.
- Prefer docs-first mapping for configuration and content tasks.
- Avoid duplicating full Lunet docs text in responses; point to exact pages and apply them.
