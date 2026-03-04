---
name: lunet-static-site-docs-and-api-docs
description: Configure and troubleshoot Lunet static sites using docs-first workflows focused on `config.scriban`, content front matter, `menu.yml`, layouts/includes, full plugin configuration, GitHub Actions deployment, and build/serve behavior. Use for Lunet site setup and maintenance; handle `api.dotnet` only when the user explicitly asks for API documentation features.
---

# Lunet Docs-First Site Configuration

Use this skill as a navigation layer to official Lunet documentation, not as a duplicate of the docs.

Core references:
- `references/00-prefetch-source-map.md`
- `references/lunet-docs-map.md`
- `references/default-template-first.md`
- `references/major-feature-usage-playbooks.md`
- `references/config-menu-frontmatter-checklists.md`

## Working Principle

- Treat [lunet.io docs](https://lunet.io/docs/) as source of truth.
- Treat the default template repo ([lunet-io/templates](https://github.com/lunet-io/templates)) as first-choice baseline for layouts/navigation/styles.
- Use prefetched snapshots in `references/upstream/` first to avoid routine web requests.
- Only fetch web docs when snapshots are missing/stale, or when the user explicitly asks for latest upstream behavior.
- For deployment tasks, prefer the official [GitHub Actions guide](https://lunet.io/docs/github-actions/).
- Prefer linking users to the exact doc section over re-explaining large blocks of knowledge.
- Do not rely on local Lunet repository paths in guidance.

## Workflow

1. Start with template-first triage using `references/default-template-first.md`.
- If site is new or heavily customized, prefer adopting/extending `lunet-io/templates` first.
- Avoid rebuilding layout/search/menu/css/syntax-highlighting foundations from scratch unless explicitly requested.

2. Classify the request by area, then pick one playbook from `references/major-feature-usage-playbooks.md`.
- `config.scriban`
- page/front matter/content
- `menu.yml` or navigation
- layouts/includes/themes
- plugin configuration (all modules listed in `references/lunet-docs-map.md`)
- CLI/build/serve/watch behavior
- deployment/CI (prefer official GitHub Actions workflow)
- optional: `api.dotnet`

3. Load prefetched docs from `references/00-prefetch-source-map.md`.
- Start with local snapshots under `references/upstream/`.
- For broad requests, use `references/lunet-docs-map.md` feature matrix to confirm complete coverage.

4. Open official docs links only when needed.
- Use web fetches as fallback for missing/outdated snapshot content or explicit "latest" requests.
- Keep citations tied to the canonical URLs from `references/lunet-docs-map.md`.

5. Apply minimal, file-focused edits.
- Prioritize correctness of:
  - `config.scriban`
  - `menu.yml`
  - front matter blocks (`--- ... ---`)
  - layout/include paths

6. Validate behavior with Lunet commands.
- Typical checks:
  - `lunet build`
  - `lunet serve`
  - `lunet build --dev` (for environment-sensitive behavior)

7. Run the checklists in `references/config-menu-frontmatter-checklists.md` for touched surfaces.

8. Report outcome with doc anchors.
- Mention which doc pages were used.
- Summarize concrete file changes and how they map to docs guidance.

## Upstream Refresh

Refresh prefetched snapshots when needed:

```bash
bash scripts/sync-lunet-docs.sh
```

This updates `references/upstream/` and rewrites the generated manifest in `references/00-prefetch-source-map.md`.

## Scope Guardrails

- Do not skip template-first evaluation for greenfield docs sites.
- Do not default to deep .NET API extraction/reference work.
- Use `api.dotnet` guidance only when user asks for API documentation generation.
- For deployment, default to the documented GitHub Actions workflow unless user requests a different CI.
- Prefer docs-first mapping for configuration and content tasks.
- Avoid duplicating full Lunet docs text in responses; point to exact pages and apply them.
