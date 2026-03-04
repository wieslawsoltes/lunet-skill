# Lunet Prefetched Source Map

## Purpose

This map tracks local, prefetched documentation snapshots bundled with this skill so normal usage can avoid web requests.

## Default Behavior

- Read `references/upstream/` snapshots first.
- Repo snapshots are stored in `references/upstream/repos/` (sparse clones).
- Use canonical URLs from `references/lunet-docs-map.md` for citation and linking.
- Refresh snapshots only when content is missing or user asks for latest behavior.

## Refresh Command

```bash
bash scripts/sync-lunet-docs.sh
```

## Generated Snapshot Manifest

<!-- BEGIN GENERATED: DOC SYNC MANIFEST -->
_Last synced (UTC): 2026-03-04T21:16:23Z_

- Lunet repo commit: `39a59a58845506c90d84184022afe875c91e27db`
- Templates repo commit: `f876c2750684e383fe719697628580a08379c5c3`

| Category | Canonical URL | Source URL | Local path |
|---|---|---|---|
| Lunet docs | https://lunet.io/docs/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/readme.md | references/upstream/lunet-docs/readme.md |
| Lunet docs | https://lunet.io/docs/getting-started/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/getting-started.md | references/upstream/lunet-docs/getting-started.md |
| Lunet docs | https://lunet.io/docs/cli/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/cli.md | references/upstream/lunet-docs/cli.md |
| Lunet docs | https://lunet.io/docs/configuration/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/configuration.md | references/upstream/lunet-docs/configuration.md |
| Lunet docs | https://lunet.io/docs/content-and-frontmatter/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/content-and-frontmatter.md | references/upstream/lunet-docs/content-and-frontmatter.md |
| Lunet docs | https://lunet.io/docs/site-structure/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/site-structure.md | references/upstream/lunet-docs/site-structure.md |
| Lunet docs | https://lunet.io/docs/layouts-and-includes/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/layouts-and-includes.md | references/upstream/lunet-docs/layouts-and-includes.md |
| Lunet docs | https://lunet.io/docs/themes-and-extends/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/themes-and-extends.md | references/upstream/lunet-docs/themes-and-extends.md |
| Lunet docs | https://lunet.io/docs/github-actions/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/github-actions.md | references/upstream/lunet-docs/github-actions.md |
| Lunet docs | N/A (docs source only) | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/menu.yml | references/upstream/lunet-docs/menu.yml |
| Lunet docs | https://lunet.io/docs/plugins/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/readme.md | references/upstream/lunet-docs/plugins/readme.md |
| Lunet docs | https://lunet.io/docs/plugins/api-dotnet/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/api-dotnet.md | references/upstream/lunet-docs/plugins/api-dotnet.md |
| Lunet docs | https://lunet.io/docs/plugins/api/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/api.md | references/upstream/lunet-docs/plugins/api.md |
| Lunet docs | https://lunet.io/docs/plugins/attributes/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/attributes.md | references/upstream/lunet-docs/plugins/attributes.md |
| Lunet docs | https://lunet.io/docs/plugins/bundles/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/bundles.md | references/upstream/lunet-docs/plugins/bundles.md |
| Lunet docs | https://lunet.io/docs/plugins/cards/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/cards.md | references/upstream/lunet-docs/plugins/cards.md |
| Lunet docs | https://lunet.io/docs/plugins/data/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/data.md | references/upstream/lunet-docs/plugins/data.md |
| Lunet docs | https://lunet.io/docs/plugins/datas/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/datas.md | references/upstream/lunet-docs/plugins/datas.md |
| Lunet docs | https://lunet.io/docs/plugins/extends/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/extends.md | references/upstream/lunet-docs/plugins/extends.md |
| Lunet docs | https://lunet.io/docs/plugins/json/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/json.md | references/upstream/lunet-docs/plugins/json.md |
| Lunet docs | https://lunet.io/docs/plugins/markdown/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/markdown.md | references/upstream/lunet-docs/plugins/markdown.md |
| Lunet docs | https://lunet.io/docs/plugins/menus/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/menus.md | references/upstream/lunet-docs/plugins/menus.md |
| Lunet docs | N/A (docs source only) | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/menu.yml | references/upstream/lunet-docs/plugins/menu.yml |
| Lunet docs | https://lunet.io/docs/plugins/minifier/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/minifier.md | references/upstream/lunet-docs/plugins/minifier.md |
| Lunet docs | https://lunet.io/docs/plugins/resources/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/resources.md | references/upstream/lunet-docs/plugins/resources.md |
| Lunet docs | https://lunet.io/docs/plugins/rss/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/rss.md | references/upstream/lunet-docs/plugins/rss.md |
| Lunet docs | https://lunet.io/docs/plugins/scss/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/scss.md | references/upstream/lunet-docs/plugins/scss.md |
| Lunet docs | https://lunet.io/docs/plugins/search/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/search.md | references/upstream/lunet-docs/plugins/search.md |
| Lunet docs | https://lunet.io/docs/plugins/server/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/server.md | references/upstream/lunet-docs/plugins/server.md |
| Lunet docs | https://lunet.io/docs/plugins/sitemaps/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/sitemaps.md | references/upstream/lunet-docs/plugins/sitemaps.md |
| Lunet docs | https://lunet.io/docs/plugins/summarizer/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/summarizer.md | references/upstream/lunet-docs/plugins/summarizer.md |
| Lunet docs | https://lunet.io/docs/plugins/taxonomies/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/taxonomies.md | references/upstream/lunet-docs/plugins/taxonomies.md |
| Lunet docs | https://lunet.io/docs/plugins/toml/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/toml.md | references/upstream/lunet-docs/plugins/toml.md |
| Lunet docs | https://lunet.io/docs/plugins/tracking/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/tracking.md | references/upstream/lunet-docs/plugins/tracking.md |
| Lunet docs | https://lunet.io/docs/plugins/watcher/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/watcher.md | references/upstream/lunet-docs/plugins/watcher.md |
| Lunet docs | https://lunet.io/docs/plugins/yaml/ | https://github.com/lunet-io/lunet/blob/39a59a58845506c90d84184022afe875c91e27db/site/docs/plugins/yaml.md | references/upstream/lunet-docs/plugins/yaml.md |
| Templates | https://github.com/lunet-io/templates/blob/main/readme.md | https://github.com/lunet-io/templates/blob/f876c2750684e383fe719697628580a08379c5c3/readme.md | references/upstream/templates/readme.md |
| Templates | https://github.com/lunet-io/templates/blob/main/dist/readme.md | https://github.com/lunet-io/templates/blob/f876c2750684e383fe719697628580a08379c5c3/dist/readme.md | references/upstream/templates/dist/readme.md |
| Templates | https://github.com/lunet-io/templates/blob/main/dist/config.scriban | https://github.com/lunet-io/templates/blob/f876c2750684e383fe719697628580a08379c5c3/dist/config.scriban | references/upstream/templates/dist/config.scriban |
| Templates | https://github.com/lunet-io/templates/blob/main/dist/menu.yml | https://github.com/lunet-io/templates/blob/f876c2750684e383fe719697628580a08379c5c3/dist/menu.yml | references/upstream/templates/dist/menu.yml |
<!-- END GENERATED: DOC SYNC MANIFEST -->
