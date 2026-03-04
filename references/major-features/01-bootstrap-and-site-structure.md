# Bootstrap and Site Structure

## Goal

Set up a Lunet site from scratch when no Lunet repository clone is available.

## Install and Initialize

```bash
dotnet tool install -g lunet
mkdir mysite
cd mysite
lunet init
```

## Build and Serve

```bash
lunet build
lunet serve
```

Default local URL:
- `http://localhost:4000`

Default output folder:
- `.lunet/build/www`

## Minimal Site Layout

Typical generated structure:

```text
mysite/
  config.scriban
  readme.md
  menu.yml
  docs/
    readme.md
    menu.yml
  .lunet/
    layouts/
    includes/
    data/
```

## What to Customize First

1. `config.scriban`
2. `readme.md`
3. `menu.yml`
4. `docs/readme.md`
5. theme/visual files under `.lunet/`

## Validation Checklist

- `lunet --help` works.
- `lunet build` creates `.lunet/build/www/index.html`.
- `lunet serve` opens site and live reload works.
- top navigation renders from `menu.yml`.
