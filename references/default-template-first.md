# Default Template First (Major Rule)

Use the Lunet default template as the baseline before creating custom layout/navigation/theme infrastructure.

## Canonical Sources

- Template repo: https://github.com/lunet-io/templates
- Template overview/readme: https://github.com/lunet-io/templates/blob/main/readme.md
- Consumer quickstart/customization: https://github.com/lunet-io/templates/blob/main/dist/readme.md

Prefetched local snapshots:
- `references/upstream/templates/readme.md`
- `references/upstream/templates/dist/readme.md`
- `references/upstream/templates/dist/config.scriban`

## When To Apply

- New docs/static site setup.
- Existing site missing coherent layout/menu/search/theme structure.
- Requests mentioning custom layout, sidebar, syntax highlighting, or color/theme systems.

## What You Get By Default

- Shared layouts/includes and UI structure.
- Ready navbar + docs menu conventions.
- Search integration defaults.
- CSS theme variables and dark/light mode support.
- Syntax highlighting setup.

## Recommended Setup Pattern (`config.scriban`)

1. Extend the default template.
2. Set project-level `site_project_*` variables.
3. Call `site_project_init`.
4. Only then add project-specific overrides/plugins.

Minimal baseline:

```scriban
extend "lunet-io/templates"

site_project_name = "MyProject"
site_project_description = "Project docs."
site_project_github_user = "org"
site_project_github_repo = "myproject"
site_project_basepath = "/myproject"

site_project_init
```

Note:
- Prefer `extend "lunet-io/templates"` as the canonical repository reference.
- For reproducible production builds, pin a template tag when available:
  - `extend "lunet-io/templates@<tag>"`
- If you encounter older examples using a different template identifier, treat the repository URL above as the source of truth.

## Major Customization Knobs (Prefer These First)

- Theme mode/behavior:
  - `template_theme_default_mode`
  - `template_theme_storage_key`
- Site-owned style overrides loaded after template styles:
  - `template_theme_override_styles`
- Project branding and metadata:
  - `site_project_name`
  - `site_project_description`
  - `site_project_logo_path`
  - `site_project_social_banner_path`
  - `site_project_banner_background_path`
  - `site_project_favicon_path`
- Repository metadata:
  - `site_project_github_user`
  - `site_project_github_repo`
  - `site_project_basepath`

## Menu Conventions To Reuse

- Root navigation in `menu.yml`:
  - `home` for left/main nav
  - `home2` for right/utility nav
- Section navigation in `docs/menu.yml` (or section-local `menu.yml`) for docs sidebar structure.

## Upgrade-Safe Rule

- Prefer setting documented `site_project_*` and `template_*` variables.
- Prefer CSS variable overrides through `template_theme_override_styles`.
- Avoid copying template internals into the site unless explicitly required.

## Validation

```bash
lunet build
lunet serve
```

Confirm:
- Navbar and docs menu render as expected.
- Search works in generated output.
- Theme mode toggle and syntax highlighting are working.
