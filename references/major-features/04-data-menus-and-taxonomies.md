# Data, Menus, and Taxonomies

## Data Loading (`site.data`)

Supported data formats:
- YAML (`.yml`, `.yaml`)
- JSON (`.json`)
- TOML (`.toml`)

Place files in:
- `/.lunet/data/`

Example file:
- `/.lunet/data/project.yml`

Read from templates:

```scriban
{{ site.data.project.name }}
```

## Menu Basics

Top-level navigation in `menu.yml`:

```yaml
home:
  - { path: readme.md, title: "Home", self: true }
  - { path: docs/readme.md, title: "Docs", folder: true }
```

Use section `menu.yml` files for sidebars.

## Taxonomy Basics

Default taxonomies:
- `tags`
- `categories`

Define terms in page front matter:

```yaml
tags: ["lunet", "docs"]
categories: ["guides"]
```

## Common Pattern

1. Put structured facts in data files.
2. Keep menu structure explicit in yaml.
3. Use taxonomies for cross-cutting page grouping.

## Validation Checklist

- `site.data` keys match filenames.
- menus resolve to correct URLs.
- taxonomy term pages are generated.
- taxonomy pages exclude drafts/non-public content if required.
