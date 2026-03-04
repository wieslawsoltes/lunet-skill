# Configuration and Environments

## Core Model

`config.scriban` is executable Scriban code. Assignments in config set site-level values.

Example:

```scriban
title = "My Site"
baseurl = baseurl ?? "https://example.com"
basepath = "/"
```

## Environment Patterns

Production by default:
- `lunet build` => `environment = "prod"`

Development mode:
- `lunet build --dev`
- `lunet serve` (always dev)

Use environment switches for feature gating:

```scriban
if environment == "dev"
  log.info "Development mode"
end
```

## Reproducible Overrides

Use CLI defines for deploy-specific values:

```bash
lunet build -d "baseurl=https://staging.example.com" -d "environment='staging'"
```

Recommended config pattern:

```scriban
baseurl = baseurl ?? "https://example.com"
```

## Include/Exclude Rules

Tune handled files in config:

```scriban
excludes.add "**/*.psd"
includes.add "**/.well-known/**"
```

## Logging in Config

```scriban
log.info "Config loaded"
log.warn "Optional dependency not found"
builtins.log.level = "debug"
```

## Validation Checklist

- config values resolve without runtime exceptions.
- `--define` overrides behave as expected.
- dev/prod gates are deterministic.
- exclude/include changes affect intended files only.
