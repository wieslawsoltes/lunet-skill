# Dev Workflow, CI, and Troubleshooting

## Local Development Loop

Primary loop:

```bash
lunet serve
```

Alternative loop:

```bash
lunet build --watch
```

Use `--no-threads` when debugging pipeline ordering or race-sensitive behavior.

## Build Modes

- dev mode: `lunet build --dev`
- prod mode: `lunet build`

## Common Troubleshooting

1. Missing layout output
- verify front matter `layout`
- verify layout file under `/.lunet/layouts`

2. Include resolution failure
- verify include path relative to `/.lunet/includes`

3. Missing data keys
- verify file path and extension under `/.lunet/data`
- verify filename without extension is the lookup key

4. Broken API pages
- verify `api.dotnet.projects` paths
- verify target framework/build configuration
- inspect generated API page paths under `/api`

5. Broken links in subpath hosting
- verify `baseurl` and `basepath`
- test with production-like path prefix

## CI and Deployment

Minimal pipeline pattern:
1. install .NET SDK
2. install or restore `lunet`
3. run `lunet build`
4. publish `.lunet/build/www`

GitHub Pages deployments should publish generated site output only.

## Quality Checklist

- run clean build from fresh checkout.
- verify no draft/internal pages leak to prod output.
- run link checks for docs + API pages.
- validate sitemap/rss/search artifacts in output.
