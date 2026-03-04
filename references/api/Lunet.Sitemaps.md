# Lunet.Sitemaps Public API

Assembly path: `src/Lunet.Sitemaps/bin/Release/net10.0/Lunet.Sitemaps.dll`

Exported types: **5**

## Types

### `Lunet.Sitemaps.SitemapPageVariables`

- Kind: `static class`

#### Fields

- `const static System.String Sitemap`
- `const static System.String SitemapChangeFrequency`
- `const static System.String SitemapPriority`
### `Lunet.Sitemaps.SitemapUrl`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SitemapUrl()`
- `SitemapUrl(System.String url)`

#### Properties

- `System.Nullable<System.DateTime> LastModified { get; set; }`
- `System.Nullable<System.Single> Priority { get; set; }`
- `System.String ChangeFrequency { get; set; }`
- `System.String Url { get; set; }`
### `Lunet.Sitemaps.SitemapsModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Sitemaps.SitemapsPlugin>`

#### Constructors

- `SitemapsModule()`
### `Lunet.Sitemaps.SitemapsPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SitemapsPlugin(Lunet.Core.SiteObject site)`

#### Properties

- `System.Boolean Enable { get; set; }`
### `Lunet.Sitemaps.SitemapsProcessor`

- Kind: `class`
- Base: `Lunet.Core.ContentProcessor<Lunet.Sitemaps.SitemapsPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SitemapsProcessor(Lunet.Sitemaps.SitemapsPlugin plugin)`

#### Methods

- `Lunet.Core.ContentResult virtual TryProcessContent(Lunet.Core.ContentObject file, Lunet.Core.ContentProcessingStage stage)`
- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Fields

- `const static System.String DefaultUrl`
