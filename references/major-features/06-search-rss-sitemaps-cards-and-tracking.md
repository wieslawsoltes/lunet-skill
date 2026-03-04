# Search, RSS, Sitemaps, Cards, and Tracking

## Search

Enable in config:

```scriban
with search
  enable = true
end
```

Produces client-side search artifacts used by frontend search UI.

## RSS

Create an rss page with `layout_type: rss`.

Typical `rss.xml` front matter:

```yaml
---
layout: "_default"
layout_type: "rss"
sitemap: false
---
```

## Sitemaps and Robots

Sitemaps module is enabled by default.
- auto-generates `/sitemap.xml`
- auto-generates `/robots.txt` when missing

## Social Cards

Configure OpenGraph and Twitter cards:

```scriban
with cards
  with twitter
    enable = true
    card = "summary_large_image"
  end
  with og
    enable = true
  end
end
```

## Tracking

Configure Google Analytics id:

```scriban
site.tracking.google.id = "G-XXXXXXXXXX"
```

Tracking should usually remain production-only behavior.

## Validation Checklist

- search index builds and queries return expected pages.
- rss feed has valid XML and recent entries.
- sitemap and robots are generated with canonical URLs.
- card tags render in page head.
- analytics script is absent in dev mode.
