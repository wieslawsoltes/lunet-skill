# Content, Layouts, Markdown, and Includes

## Front Matter Pattern

Markdown page with YAML front matter:

```markdown
---
title: "About"
layout: "_default"
---

# About
```

Files with front matter are pages. Files without front matter are static assets.

## Layout Resolution

Default lookup order is section-aware, then fallback layouts.

Use global fallback layout in config:

```scriban
layout = "_default"
```

Place layout files under:
- `/.lunet/layouts/`

## Includes

Reusable snippets live under:
- `/.lunet/includes/`

Use include in pages/layouts:

```scriban
{{ include "_partials/header.sbn-html" }}
```

## Markdown Module Patterns

Enable and configure markdown options in `config.scriban` via `with markdown`.

Convert markdown text in Scriban:

```scriban
{{ markdown.to_html some_markdown_text }}
```

## XRef Linking

Use `xref:` links in markdown when API UIDs are available:

```markdown
See [SiteObject](xref:Lunet.Core.SiteObject).
```

## Validation Checklist

- every page has intended layout.
- include paths resolve from `/.lunet/includes`.
- markdown renders consistently with expected pipeline options.
- xref links resolve or intentionally fail visibly.
