# Major Feature Usage Playbooks

Use these playbooks to select docs and edit points for common, high-value Lunet outcomes.

## Table of Contents

- [1. Basic Documentation Site](#1-basic-documentation-site)
- [2. Structured Navigation (Top Menu + Sidebar + Breadcrumbs)](#2-structured-navigation-top-menu--sidebar--breadcrumbs)
- [3. Blog with Clean URLs, Feeds, and Discoverability](#3-blog-with-clean-urls-feeds-and-discoverability)
- [4. Frontend Asset Pipeline (npm + SCSS + Bundles)](#4-frontend-asset-pipeline-npm--scss--bundles)
- [5. Content Metadata and Social/SEO Cards](#5-content-metadata-and-socialseo-cards)
- [6. Data-Driven Pages](#6-data-driven-pages)
- [7. .NET API Documentation Section](#7-net-api-documentation-section)
- [8. Local Dev and Deployment](#8-local-dev-and-deployment)

## 1. Basic Documentation Site

- Goal: start a docs site with reusable layouts and consistent front matter.
- Read:
  - https://lunet.io/docs/getting-started/
  - https://lunet.io/docs/configuration/
  - https://lunet.io/docs/content-and-frontmatter/
  - https://lunet.io/docs/layouts-and-includes/
- Edit:
  - `config.scriban`
  - docs pages (`*.md`)
  - `/.lunet/layouts/*`
  - `/.lunet/includes/*`
- Validate:
  - `lunet build`
  - `lunet serve`

## 2. Structured Navigation (Top Menu + Sidebar + Breadcrumbs)

- Goal: make docs navigation predictable and section-aware.
- Read:
  - https://lunet.io/docs/plugins/menus/
  - https://lunet.io/docs/content-and-frontmatter/
  - https://lunet.io/docs/layouts-and-includes/
- Edit:
  - root `menu.yml`
  - section-level `menu.yml`
  - navigation include/layout templates
- Validate:
  - all menu links resolve in built output
  - `page.menu_item` and breadcrumb rendering work on nested pages

## 3. Blog with Clean URLs, Feeds, and Discoverability

- Goal: blog-style docs/news pages with generated taxonomy, RSS, sitemap, and search.
- Read:
  - https://lunet.io/docs/plugins/attributes/
  - https://lunet.io/docs/plugins/taxonomies/
  - https://lunet.io/docs/plugins/rss/
  - https://lunet.io/docs/plugins/sitemaps/
  - https://lunet.io/docs/plugins/search/
  - https://lunet.io/docs/plugins/summarizer/
- Edit:
  - `config.scriban`
  - blog page front matter (`tags`, `categories`, `sitemap*`, summary controls)
  - taxonomy/feed layouts
- Validate:
  - dated URL rules are correct
  - taxonomy term/list pages are generated
  - RSS and sitemap outputs exist
  - search index is generated and queryable

## 4. Frontend Asset Pipeline (npm + SCSS + Bundles)

- Goal: reproducible CSS/JS pipeline without manual `node_modules` management.
- Read:
  - https://lunet.io/docs/plugins/resources/
  - https://lunet.io/docs/plugins/scss/
  - https://lunet.io/docs/plugins/bundles/
  - https://lunet.io/docs/plugins/minifier/
- Edit:
  - `config.scriban` (`resource`, `scss.includes`, `bundle`)
  - local `/css`, `/js`, and optional copied content targets
  - head include registration if theme does not include bundle output
- Validate:
  - generated CSS/JS paths exist
  - expected minified/concatenated behavior matches config

## 5. Content Metadata and Social/SEO Cards

- Goal: reliable sharing metadata for docs/blog pages.
- Read:
  - https://lunet.io/docs/plugins/cards/
  - https://lunet.io/docs/plugins/summarizer/
  - https://lunet.io/docs/plugins/tracking/
- Edit:
  - `config.scriban` (`cards.*`, `site.tracking.google.id`)
  - page front matter overrides (`twitter_*`, `og_*`)
  - optional summary markers in page content
- Validate:
  - meta tags render in page head
  - tracking appears only in prod environment

## 6. Data-Driven Pages

- Goal: generate docs pages from structured data files.
- Read:
  - https://lunet.io/docs/plugins/data/
  - https://lunet.io/docs/plugins/datas/
  - https://lunet.io/docs/plugins/yaml/
  - https://lunet.io/docs/plugins/json/
  - https://lunet.io/docs/plugins/toml/
- Edit:
  - `/.lunet/data/*.yml|*.yaml|*.json|*.toml`
  - templates/layouts that consume `site.data`
- Validate:
  - data files parse
  - expected `site.data.*` keys are present in rendered output

## 7. .NET API Documentation Section

- Goal: add API reference pages as part of the docs site.
- Read:
  - https://lunet.io/docs/plugins/api/
  - https://lunet.io/docs/plugins/api-dotnet/
  - https://lunet.io/docs/plugins/menus/
- Edit:
  - `config.scriban` (`with api.dotnet ...`)
  - optional menu entries linking API root
  - optional API layout overrides
- Validate:
  - API root and namespace/member pages are generated
  - `xref:` links resolve where expected

## 8. Local Dev and Deployment

- Goal: fast local iteration and deterministic publishing.
- Read:
  - https://lunet.io/docs/cli/
  - https://lunet.io/docs/plugins/server/
  - https://lunet.io/docs/plugins/watcher/
  - https://lunet.io/docs/github-actions/
- Edit:
  - commands/workflow usage
  - optional `.github/workflows/*` deployment file
- Validate:
  - `lunet serve` live reload behavior
  - production build output from `lunet build`
  - CI workflow uses intended build path/command
