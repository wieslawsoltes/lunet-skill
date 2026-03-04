# Lunet Official Docs Coverage Map

Use this map as a routing index to official docs only.

## Table of Contents

- [Entry Points](#entry-points)
- [Prefetch-First Routing](#prefetch-first-routing)
- [Default Template Baseline](#default-template-baseline)
- [Core Guides](#core-guides)
- [All Plugin Pages](#all-plugin-pages)
- [Feature Coverage Matrix](#feature-coverage-matrix)
- [Usage Rules](#usage-rules)

## Entry Points

| Topic | Official URL |
|---|---|
| Lunet docs home | https://lunet.io/docs/ |
| User guide landing | https://lunet.io/docs/ |
| Plugins index | https://lunet.io/docs/plugins/ |

## Prefetch-First Routing

- Snapshot index and canonical URL mapping:
  - `references/00-prefetch-source-map.md`
- Local snapshot roots:
  - `references/upstream/lunet-docs/`
  - `references/upstream/templates/`
  - `references/upstream/repos/` (sparse git snapshots used by sync script)
- Open local snapshots first; use canonical URLs in this map for citations.

## Default Template Baseline

| Topic | URL |
|---|---|
| Default template repository | https://github.com/lunet-io/templates |
| Template readme (overview + consumer contract) | https://github.com/lunet-io/templates/blob/main/readme.md |
| Template dist readme (consumer quickstart/customization) | https://github.com/lunet-io/templates/blob/main/dist/readme.md |

## Core Guides

| Topic | Official URL |
|---|---|
| Getting started | https://lunet.io/docs/getting-started/ |
| CLI reference | https://lunet.io/docs/cli/ |
| Configuration (`config.scriban`) | https://lunet.io/docs/configuration/ |
| Content and front matter | https://lunet.io/docs/content-and-frontmatter/ |
| Site structure | https://lunet.io/docs/site-structure/ |
| Layouts and includes | https://lunet.io/docs/layouts-and-includes/ |
| Themes and extensions | https://lunet.io/docs/themes-and-extends/ |
| GitHub Actions deployment | https://lunet.io/docs/github-actions/ |

## All Plugin Pages

| Plugin | Official URL |
|---|---|
| Extends (themes) | https://lunet.io/docs/plugins/extends/ |
| Resources (npm) | https://lunet.io/docs/plugins/resources/ |
| Bundles | https://lunet.io/docs/plugins/bundles/ |
| Markdown | https://lunet.io/docs/plugins/markdown/ |
| SCSS | https://lunet.io/docs/plugins/scss/ |
| Minifier | https://lunet.io/docs/plugins/minifier/ |
| Summarizer | https://lunet.io/docs/plugins/summarizer/ |
| Menus | https://lunet.io/docs/plugins/menus/ |
| Taxonomies | https://lunet.io/docs/plugins/taxonomies/ |
| RSS | https://lunet.io/docs/plugins/rss/ |
| Sitemaps | https://lunet.io/docs/plugins/sitemaps/ |
| Search | https://lunet.io/docs/plugins/search/ |
| Cards | https://lunet.io/docs/plugins/cards/ |
| Tracking | https://lunet.io/docs/plugins/tracking/ |
| Server (`lunet serve`) | https://lunet.io/docs/plugins/server/ |
| Watcher (`lunet build --watch`) | https://lunet.io/docs/plugins/watcher/ |
| Data modules overview | https://lunet.io/docs/plugins/data/ |
| Datas | https://lunet.io/docs/plugins/datas/ |
| YAML | https://lunet.io/docs/plugins/yaml/ |
| JSON | https://lunet.io/docs/plugins/json/ |
| TOML | https://lunet.io/docs/plugins/toml/ |
| Attributes (URL patterns) | https://lunet.io/docs/plugins/attributes/ |
| API registry | https://lunet.io/docs/plugins/api/ |
| API (.NET) | https://lunet.io/docs/plugins/api-dotnet/ |

## Feature Coverage Matrix

This matrix maps Lunet's public feature surface to docs and primary configuration files.

| Feature | Primary docs | Typical files touched |
|---|---|---|
| Default template baseline (recommended first step) | [templates repo](https://github.com/lunet-io/templates)<br>[template readme](https://github.com/lunet-io/templates/blob/main/readme.md)<br>[dist readme](https://github.com/lunet-io/templates/blob/main/dist/readme.md) | `config.scriban`, `menu.yml`, `docs/menu.yml`, site assets and theme override styles |
| Scriban templating in config/pages/layouts | [Configuration](https://lunet.io/docs/configuration/)<br>[Content & front matter](https://lunet.io/docs/content-and-frontmatter/)<br>[Layouts & includes](https://lunet.io/docs/layouts-and-includes/) | `config.scriban`, content `.md`/`.sbn-*`, `/.lunet/layouts/*`, `/.lunet/includes/*` |
| Layout resolution and include usage | [Layouts & includes](https://lunet.io/docs/layouts-and-includes/) | `/.lunet/layouts/*`, `/.lunet/includes/*`, front matter `layout` |
| Theme/extension layering from GitHub | [Themes & extensions](https://lunet.io/docs/themes-and-extends/)<br>[Extends module](https://lunet.io/docs/plugins/extends/) | `config.scriban`, overrides under `/.lunet/*` |
| npm resource download/cache | [Resources module](https://lunet.io/docs/plugins/resources/) | `config.scriban` |
| Markdown rendering and xref links | [Markdown module](https://lunet.io/docs/plugins/markdown/)<br>[Content & front matter](https://lunet.io/docs/content-and-frontmatter/) | content `.md`, `config.scriban` |
| SCSS compilation | [SCSS module](https://lunet.io/docs/plugins/scss/) | `config.scriban`, `.scss` assets |
| CSS/JS bundles and injected head links | [Bundles module](https://lunet.io/docs/plugins/bundles/) | `config.scriban`, front matter `bundle`, layout head includes |
| JS/CSS minification behavior | [Minifier module](https://lunet.io/docs/plugins/minifier/)<br>[Bundles module](https://lunet.io/docs/plugins/bundles/) | `config.scriban` |
| Taxonomies and generated term pages | [Taxonomies module](https://lunet.io/docs/plugins/taxonomies/)<br>[Content & front matter](https://lunet.io/docs/content-and-frontmatter/) | `config.scriban`, front matter taxonomies, taxonomy layouts |
| RSS generation | [RSS module](https://lunet.io/docs/plugins/rss/) | feed page front matter/content, feed layout, `config.scriban` |
| Sitemap and robots generation | [Sitemaps module](https://lunet.io/docs/plugins/sitemaps/) | optional front matter `sitemap*`, optional sitemap layout |
| Search index generation and client API | [Search module](https://lunet.io/docs/plugins/search/) | `config.scriban`, bundle/layout integration, optional excludes |
| Social/SEO card tags | [Cards module](https://lunet.io/docs/plugins/cards/) | `config.scriban`, per-page front matter overrides |
| Data loading into `site.data` | [Data overview](https://lunet.io/docs/plugins/data/)<br>[Datas module](https://lunet.io/docs/plugins/datas/)<br>[YAML module](https://lunet.io/docs/plugins/yaml/)<br>[JSON module](https://lunet.io/docs/plugins/json/)<br>[TOML module](https://lunet.io/docs/plugins/toml/) | `/.lunet/data/*`, `config.scriban`, layouts/templates |
| Menus and navigation trees | [Menus module](https://lunet.io/docs/plugins/menus/) | `menu.yml`, section `menu.yml`, layouts/includes |
| Live reload/dev server | [Server module](https://lunet.io/docs/plugins/server/)<br>[Watcher module](https://lunet.io/docs/plugins/watcher/)<br>[CLI reference](https://lunet.io/docs/cli/) | command usage, optional `site.livereload` and baseurl flags |
| Tracking/analytics in prod | [Tracking module](https://lunet.io/docs/plugins/tracking/)<br>[Configuration](https://lunet.io/docs/configuration/) | `config.scriban`, optional include override |
| .NET API docs generation | [API module](https://lunet.io/docs/plugins/api/)<br>[API (.NET) module](https://lunet.io/docs/plugins/api-dotnet/)<br>[Menus module](https://lunet.io/docs/plugins/menus/) | `config.scriban`, optional API menu integration |
| URL pattern rules by glob | [Attributes module](https://lunet.io/docs/plugins/attributes/)<br>[Content & front matter](https://lunet.io/docs/content-and-frontmatter/) | `config.scriban`, page front matter overrides |
| Page summaries for feeds/cards | [Summarizer module](https://lunet.io/docs/plugins/summarizer/)<br>[RSS module](https://lunet.io/docs/plugins/rss/)<br>[Cards module](https://lunet.io/docs/plugins/cards/) | page content markers, `config.scriban`, front matter overrides |
| CLI workflows (`init`, `build`, `serve`, `clean`) | [CLI reference](https://lunet.io/docs/cli/)<br>[Getting started](https://lunet.io/docs/getting-started/) | command line only, site folder structure |
| Site filesystem and layering model | [Site structure](https://lunet.io/docs/site-structure/)<br>[Themes & extensions](https://lunet.io/docs/themes-and-extends/) | `/.lunet/*`, content tree |
| GitHub Pages deployment | [GitHub Actions](https://lunet.io/docs/github-actions/) | `.github/workflows/*.yml`, optional CNAME/domain setup |

## Usage Rules

1. Open the smallest relevant set of local prefetched snapshots first (from `references/00-prefetch-source-map.md`).
2. Use official URLs for canonical linking/citation, and as fallback when snapshot content is missing/stale.
3. For new or heavily customized sites, evaluate `lunet-io/templates` first before custom layout/menu/theme implementation.
4. Prefer configuration/file fixes over long conceptual explanations.
5. Do not rely on local Lunet source checkout paths when giving guidance.
6. For deployment, prefer the documented GitHub Actions workflow page first: https://lunet.io/docs/github-actions/
7. Treat `api.dotnet` as opt-in: only deep-dive when the user asks for API docs work.
