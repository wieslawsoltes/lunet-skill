# Resources, Bundles, SCSS, and Minifier

## npm Resources

Download npm artifacts through Lunet:

```scriban
$bootstrap = resource "npm:bootstrap" "5.3.8"
$icons = resource "npm:bootstrap-icons"
```

## Bundle Configuration

Basic bundle setup:

```scriban
with bundle
  css "/css/main.scss"
  js "/js/main.js"
  concat = true
  minify = true
end
```

Bundle module handles concatenation and passes content to minifier when enabled.

## SCSS Compilation

SCSS files (`.scss`) compile via Dart Sass.

Common path:
- source: `/css/main.scss`
- output: `/css/main.css`

## Minifier

Minifier is applied through bundles (`minify = true`).

## Recommended Asset Pipeline

1. Fetch external libs using `resource`.
2. Feed css/js into `bundle`.
3. Keep `concat = true` for fewer requests.
4. Enable `minify = true` for production output.

## Validation Checklist

- all resource fetches resolve and are cached.
- generated CSS exists and includes compiled SCSS.
- final HTML includes expected `<link>` and `<script>` tags.
- minified output is valid and functional.
