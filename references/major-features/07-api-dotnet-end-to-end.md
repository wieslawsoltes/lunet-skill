# API .NET End-to-End

## Core `api.dotnet` Configuration

```scriban
with api.dotnet
  title = "My API Reference"
  path = "/api"
  menu_name = "api"
  menu_title = "API"
  config = "Release"
  properties = { TargetFramework: "net10.0" }
  projects = [
    { name: "MyLib", path: "../src/MyLib/MyLib.csproj" }
  ]
end
```

## Multi-Project Pattern

```scriban
with api.dotnet
  projects = [
    { name: "Core", path: "../src/My.Core/My.Core.csproj" }
    { name: "Web", path: "../src/My.Web/My.Web.csproj" }
  ]
end
```

## External API Linking

Use `external_apis` for UIDs hosted elsewhere:

```scriban
with api.dotnet
  external_apis = [
    { assembly: "External.Lib", url: "https://example.com/api" }
  ]
end
```

## Extra Namespace/Type Docs

Add markdown docs under project `apidocs/` with `uid` front matter:

```markdown
---
uid: My.Namespace
---

# Summary
Namespace summary.

# Remarks
Additional notes.
```

## XRef in Content

```markdown
See [MyType](xref:My.Namespace.MyType).
```

## Validation Checklist

- `/api/` root page generated.
- namespace/type/member pages generated.
- api menu tree appears in navigation.
- xref links resolve to generated or external pages.
- long UIDs produce stable short slugs.
