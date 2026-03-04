# Lunet Feature Reference

Generated from repository sources on 2026-03-04T19:12:34.

## Product Features (readme.md)

- **Scriban templating** — full scripting language in your pages, layouts, and config (`config.scriban`)
- **Layouts & includes** — automatic layout resolution with section-aware search paths
- **Themes & extensions** — install themes/plugins directly from GitHub repos (`extend "owner/repo@tag"`)
- **npm resources** — fetch and cache npm packages (Bootstrap, Font Awesome…) without a separate `node_modules` workflow
- **Markdown** — [Markdig](https://github.com/xoofx/markdig)-based with cross-reference link support
- **SCSS / Dart Sass** — compile SCSS to CSS with the embedded Dart Sass compiler
- **Bundles** — declarative CSS/JS bundling with automatic minification
- **Taxonomies** — tags, categories, or any custom taxonomy with auto-generated term pages
- **RSS, sitemaps, search** — RSS feeds, `sitemap.xml`, and client-side search index generation
- **SEO & social cards** — OpenGraph / Twitter meta tags from page metadata
- **Data loading** — pull structured data from YAML, JSON, or TOML files into templates
- **Menus** — define navigation trees via simple `menu.yml` files
- **Live reload** — built-in dev server with file watcher and automatic browser refresh
- **Analytics** — Google Analytics injection (production builds only)
- **.NET API docs** — generate API reference pages from .NET projects/assemblies — unique to Lunet
- **URL patterns** — glob-based rules to apply metadata (URLs, layouts, etc.) across pages
- **Summarizer** — automatic page summaries for feeds and cards

## Plugin Registration Order (LunetApp.Modules)

| # | Module | Plugin | Project | Docs | Source |
|---|---|---|---|---|---|
| 1 | `ApiModule` | `ApiPlugin` | `Lunet.Api` | `site/docs/plugins/api.md` | `src/Lunet.Api/ApiPlugin.cs` |
| 2 | `BundleModule` | `BundlePlugin` | `Lunet.Bundles` | `site/docs/plugins/bundles.md` | `src/Lunet.Bundles/BundlePlugin.cs` |
| 3 | `ApiDotNetModule` | `ApiDotNetPlugin` | `Lunet.Api.DotNet` | `site/docs/plugins/api-dotnet.md` | `src/Lunet.Api.DotNet/ApiDotNetPlugin.cs` |
| 4 | `MenuModule` | `MenuPlugin` | `Lunet.Menus` | `site/docs/plugins/menus.md` | `src/Lunet.Menus/MenuPlugin.cs` |
| 5 | `ExtendsModule` | `ExtendsPlugin` | `Lunet.Extends` | `site/docs/plugins/extends.md` | `src/Lunet.Extends/ExtendsPlugin.cs` |
| 6 | `SummarizerModule` | `SummarizerPlugin` | `Lunet.Summarizer` | `site/docs/plugins/summarizer.md` | `src/Lunet.Summarizer/SummarizerPlugin.cs` |
| 7 | `MarkdownModule` | `MarkdownPlugin` | `Lunet.Markdown` | `site/docs/plugins/markdown.md` | `src/Lunet.Markdig/MarkdownPlugin.cs` |
| 8 | `LayoutModule` | `LayoutPlugin` | `Lunet.Layouts` | `site/docs/layouts-and-includes.md` | `src/Lunet.Layouts/LayoutPlugin.cs` |
| 9 | `ResourceModule` | `ResourcePlugin` | `Lunet.Resources` | `site/docs/plugins/resources.md` | `src/Lunet.Resources/ResourcePlugin.cs` |
| 10 | `DatasModule` | `DatasPlugin` | `Lunet.Datas` | `site/docs/plugins/datas.md` | `src/Lunet.Datas/DatasPlugin.cs` |
| 11 | `ServerModule` | `ServerPlugin` | `Lunet.Server` | `site/docs/plugins/server.md` | `src/Lunet.Server/ServerModule.cs` |
| 12 | `WatcherModule` | `-` | `Lunet.Watcher` | `site/docs/plugins/watcher.md` | `src/Lunet.Watcher/SiteWatcherService.cs` |
| 13 | `MinifierModule` | `MinifierPlugin` | `Lunet.Minifiers` | `site/docs/plugins/minifier.md` | `src/Lunet.NUglify/MinifierPlugin.cs` |
| 14 | `RssModule` | `RssPlugin` | `Lunet.Rss` | `site/docs/plugins/rss.md` | `src/Lunet.Rss/RssPlugin.cs` |
| 15 | `SassModule` | `SassPlugin` | `Lunet.Sass` | `site/docs/plugins/scss.md` | `src/Lunet.Sass/SassPlugin.cs` |
| 16 | `TaxonomyModule` | `TaxonomyPlugin` | `Lunet.Taxonomies` | `site/docs/plugins/taxonomies.md` | `src/Lunet.Taxonomies/TaxonomyPlugin.cs` |
| 17 | `CardsModule` | `CardsPlugin` | `Lunet.Cards` | `site/docs/plugins/cards.md` | `src/Lunet.Cards/CardsPlugin.cs` |
| 18 | `SearchModule` | `SearchPlugin` | `Lunet.Search` | `site/docs/plugins/search.md` | `src/Lunet.Search/SearchPlugin.cs` |
| 19 | `SitemapsModule` | `SitemapsPlugin` | `Lunet.Sitemaps` | `site/docs/plugins/sitemaps.md` | `src/Lunet.Sitemaps/SitemapsPlugin.cs` |
| 20 | `AttributesModule` | `AttributesPlugin` | `Lunet.Attributes` | `site/docs/plugins/attributes.md` | `src/Lunet.Attributes/AttributesPlugin.cs` |
| 21 | `YamlModule` | `YamlPlugin` | `Lunet.Yaml` | `site/docs/plugins/yaml.md` | `src/Lunet.Yaml/YamlPlugin.cs` |
| 22 | `JsonModule` | `JsonPlugin` | `Lunet.Json` | `site/docs/plugins/json.md` | `src/Lunet.Json/JsonPlugin.cs` |
| 23 | `TomlModule` | `TomlPlugin` | `Lunet.Toml` | `site/docs/plugins/toml.md` | `src/Lunet.Toml/TomlPlugin.cs` |
| 24 | `TrackingModule` | `AnalyticsPlugin` | `Lunet.Tracking` | `site/docs/plugins/tracking.md` | `src/Lunet.Tracking/TrackingPlugin.cs` |

## Documentation Pages

| Path | Title |
|---|---|
| `site/docs/cli.md` | CLI reference |
| `site/docs/configuration.md` | Configuration (config.scriban) |
| `site/docs/content-and-frontmatter.md` | Content & front matter |
| `site/docs/getting-started.md` | Getting started |
| `site/docs/github-actions.md` | Publishing with GitHub Actions |
| `site/docs/layouts-and-includes.md` | Layouts & includes |
| `site/docs/plugins/api-dotnet.md` | API module (.NET) |
| `site/docs/plugins/api.md` | API module |
| `site/docs/plugins/attributes.md` | Attributes module (URL patterns) |
| `site/docs/plugins/bundles.md` | Bundles module |
| `site/docs/plugins/cards.md` | Cards module (OpenGraph/Twitter) |
| `site/docs/plugins/data.md` | Data modules (site.data) |
| `site/docs/plugins/datas.md` | Datas module |
| `site/docs/plugins/extends.md` | Extends module (themes) |
| `site/docs/plugins/json.md` | JSON module |
| `site/docs/plugins/markdown.md` | Markdown module |
| `site/docs/plugins/menus.md` | Menus module |
| `site/docs/plugins/minifier.md` | Minifier module |
| `site/docs/plugins/readme.md` | Modules (plugins) |
| `site/docs/plugins/resources.md` | Resources module (npm) |
| `site/docs/plugins/rss.md` | RSS module |
| `site/docs/plugins/scss.md` | SCSS module (Dart Sass) |
| `site/docs/plugins/search.md` | Search module |
| `site/docs/plugins/server.md` | Server module (lunet serve) |
| `site/docs/plugins/sitemaps.md` | Sitemaps module |
| `site/docs/plugins/summarizer.md` | Summarizer module |
| `site/docs/plugins/taxonomies.md` | Taxonomies module |
| `site/docs/plugins/toml.md` | TOML module |
| `site/docs/plugins/tracking.md` | Tracking module (Google Analytics) |
| `site/docs/plugins/watcher.md` | Watcher module (--watch) |
| `site/docs/plugins/yaml.md` | YAML module |
| `site/docs/readme.md` | Lunet — User Guide |
| `site/docs/site-structure.md` | Site structure |
| `site/docs/themes-and-extends.md` | Themes & extensions (extend) |

## Project and Assembly Map

| Project | Assembly | TargetFramework | csproj |
|---|---|---|---|
| `Lunet` | `lunet` | `net10.0` | `src/Lunet/Lunet.csproj` |
| `Lunet.Api` | `Lunet.Api` | `net10.0` | `src/Lunet.Api/Lunet.Api.csproj` |
| `Lunet.Api.DotNet` | `Lunet.Api.DotNet` | `net10.0` | `src/Lunet.Api.DotNet/Lunet.Api.DotNet.csproj` |
| `Lunet.Api.DotNet.Extractor` | `Lunet.Api.DotNet.Extractor` | `netstandard2.0` | `src/Lunet.Api.DotNet.Extractor/Lunet.Api.DotNet.Extractor.csproj` |
| `Lunet.ApiExample` | `Lunet.ApiExample` | `net10.0` | `src/Lunet.ApiExample/Lunet.ApiExample.csproj` |
| `Lunet.Application` | `Lunet.Application` | `net10.0` | `src/Lunet.Application/Lunet.Application.csproj` |
| `Lunet.Attributes` | `Lunet.Attributes` | `net10.0` | `src/Lunet.Attributes/Lunet.Attributes.csproj` |
| `Lunet.Bundles` | `Lunet.Bundles` | `net10.0` | `src/Lunet.Bundles/Lunet.Bundles.csproj` |
| `Lunet.Cards` | `Lunet.Cards` | `net10.0` | `src/Lunet.Cards/Lunet.Cards.csproj` |
| `Lunet.Core` | `Lunet.Core` | `net10.0` | `src/Lunet.Core/Lunet.Core.csproj` |
| `Lunet.Datas` | `Lunet.Datas` | `net10.0` | `src/Lunet.Datas/Lunet.Datas.csproj` |
| `Lunet.Extends` | `Lunet.Extends` | `net10.0` | `src/Lunet.Extends/Lunet.Extends.csproj` |
| `Lunet.Json` | `Lunet.Json` | `net10.0` | `src/Lunet.Json/Lunet.Json.csproj` |
| `Lunet.Layouts` | `Lunet.Layouts` | `net10.0` | `src/Lunet.Layouts/Lunet.Layouts.csproj` |
| `Lunet.Markdown` | `Lunet.Markdown` | `net10.0` | `src/Lunet.Markdig/Lunet.Markdown.csproj` |
| `Lunet.Menus` | `Lunet.Menus` | `net10.0` | `src/Lunet.Menus/Lunet.Menus.csproj` |
| `Lunet.Minifiers` | `Lunet.Minifiers` | `net10.0` | `src/Lunet.NUglify/Lunet.Minifiers.csproj` |
| `Lunet.Resources` | `Lunet.Resources` | `net10.0` | `src/Lunet.Resources/Lunet.Resources.csproj` |
| `Lunet.Rss` | `Lunet.Rss` | `net10.0` | `src/Lunet.Rss/Lunet.Rss.csproj` |
| `Lunet.Sass` | `Lunet.Sass` | `net10.0` | `src/Lunet.Sass/Lunet.Sass.csproj` |
| `Lunet.Search` | `Lunet.Search` | `net10.0` | `src/Lunet.Search/Lunet.Search.csproj` |
| `Lunet.Server` | `Lunet.Server` | `net10.0` | `src/Lunet.Server/Lunet.Server.csproj` |
| `Lunet.Sitemaps` | `Lunet.Sitemaps` | `net10.0` | `src/Lunet.Sitemaps/Lunet.Sitemaps.csproj` |
| `Lunet.Summarizer` | `Lunet.Summarizer` | `net10.0` | `src/Lunet.Summarizer/Lunet.Summarizer.csproj` |
| `Lunet.Taxonomies` | `Lunet.Taxonomies` | `net10.0` | `src/Lunet.Taxonomies/Lunet.Taxonomies.csproj` |
| `Lunet.Toml` | `Lunet.Toml` | `net10.0` | `src/Lunet.Toml/Lunet.Toml.csproj` |
| `Lunet.Tracking` | `Lunet.Tracking` | `net10.0` | `src/Lunet.Tracking/Lunet.Tracking.csproj` |
| `Lunet.Watcher` | `Lunet.Watcher` | `net10.0` | `src/Lunet.Watcher/Lunet.Watcher.csproj` |
| `Lunet.Yaml` | `Lunet.Yaml` | `net10.0` | `src/Lunet.Yaml/Lunet.Yaml.csproj` |

