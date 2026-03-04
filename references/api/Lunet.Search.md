# Lunet.Search Public API

Assembly path: `src/Lunet.Search/bin/Release/net10.0/Lunet.Search.dll`

Exported types: **4**

## Types

### `Lunet.Search.SearchEngine`

- Kind: `abstract class`
- Base: `Lunet.Core.ContentProcessor<Lunet.Search.SearchPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Methods

- `Lunet.Core.ContentResult virtual TryProcessContent(Lunet.Core.ContentObject file, Lunet.Core.ContentProcessingStage stage)`
- `System.Void abstract Initialize()`
- `System.Void abstract ProcessSearchContent(Lunet.Core.ContentObject file, System.String plainText)`
- `System.Void abstract Terminate()`
- `System.Void virtual PrepareBeforeProcessing()`
- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `System.String Name { get; }`
### `Lunet.Search.SearchModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Search.SearchPlugin>`

#### Constructors

- `SearchModule()`
### `Lunet.Search.SearchPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SearchPlugin(Lunet.Core.SiteObject site, Lunet.Bundles.BundlePlugin bundlePlugin, Lunet.Resources.ResourcePlugin resourcePlugin)`

#### Properties

- `Lunet.Core.PathCollection Excludes { get; }`
- `System.Boolean Enable { get; set; }`
- `System.Boolean Worker { get; set; }`
- `System.Collections.Generic.List<Lunet.Search.SearchEngine> SearchEngines { get; }`
- `System.String Engine { get; set; }`
- `System.String Url { get; set; }`

#### Fields

- `const static System.String DefaultKind`
- `readonly static Zio.UPath DefaultUrl`
### `Lunet.Search.SqliteSearchEngine`

- Kind: `class`
- Base: `Lunet.Search.SearchEngine`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SqliteSearchEngine(Lunet.Search.SearchPlugin plugin)`

#### Methods

- `System.Void virtual Initialize()`
- `System.Void virtual PrepareBeforeProcessing()`
- `System.Void virtual ProcessSearchContent(Lunet.Core.ContentObject file, System.String plainText)`
- `System.Void virtual Terminate()`

#### Fields

- `const static System.String EngineName`
