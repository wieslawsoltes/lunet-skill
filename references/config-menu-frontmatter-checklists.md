# Config, Menu, and Front Matter Checklists

Use this after opening the matching official docs pages.

## Required Docs Per Surface

- `config.scriban`: https://lunet.io/docs/configuration/
- Front matter/content: https://lunet.io/docs/content-and-frontmatter/
- Navigation menus: https://lunet.io/docs/plugins/menus/
- Layouts/includes: https://lunet.io/docs/layouts-and-includes/
- Themes/layering: https://lunet.io/docs/themes-and-extends/

## `config.scriban` Review Checklist

- Confirm core site identity values are intentional: `site.title`, `site.baseurl`, and `site.basepath`.
- Verify environment-sensitive behavior is explicit (`environment` checks for dev vs prod paths).
- Keep each feature setup in a focused `with ... end` block (no scattered partial config).
- Verify plugin options map to documented names/types on the plugin page.
- Confirm includes/excludes patterns are deliberate and not excluding needed content.
- Check `site.html.*` customizations do not duplicate built-in head includes unexpectedly.
- Prefer clear defaults with Scriban patterns (`??`, conditional expressions, helper funcs) over duplicated literal values.

## `menu.yml` Review Checklist

- Keep paths valid for existing pages and sections.
- Use `folder: true` only when the item should expose descendants.
- Keep menu root names stable so layout bindings (`site.menu.<name>`) remain valid.
- Confirm active-state logic and breadcrumb rendering for nested pages.
- For API docs sites, verify menu integration strategy (`menu.yml` link vs generated API menu).

## Front Matter Review Checklist

- Use valid YAML front matter delimiters (`---`) or valid Scriban front matter (`+++`) per docs.
- Set required per-page identity keys (`title`, optional `layout`) consistently.
- Keep taxonomy keys (`tags`, `categories`, custom taxonomies) as arrays of strings.
- Validate module-specific keys and types when used:
  - feed/sitemap/search/cards/tracking fields
  - URL overrides (`url`)
  - bundle selection (`bundle`)
- Prevent accidental type drift (string vs list vs object) across similar pages.

## Layouts and Includes Checklist

- Confirm layout filenames and resolution patterns match documented conventions.
- Verify include names are correct and exist in `/.lunet/includes/`.
- Ensure list vs single layout behavior is intentional for each content type.
- Validate rendered HTML output, not only template source.

## Feature-Specific Quick Checks

- Assets: resources + scss + bundle configuration align and output expected files.
- Discoverability: taxonomies/rss/sitemap/search generate expected pages/files.
- SEO/social: cards output expected head tags; summary fallback works.
- Analytics: tracking snippet appears only in production.
- API docs: only apply `api.dotnet` configuration when API docs are part of the request.

## Validation Commands

```bash
lunet build
lunet serve
lunet build --dev
```
