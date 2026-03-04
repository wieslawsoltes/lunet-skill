# Lunet.Minifiers Public API

Assembly path: `src/Lunet.NUglify/bin/Release/net10.0/Lunet.Minifiers.dll`

Exported types: **2**

## Types

### `Lunet.Minifiers.MinifierModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Minifiers.MinifierPlugin>`

#### Constructors

- `MinifierModule()`
### `Lunet.Minifiers.MinifierPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Bundles.IContentMinifier`, `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MinifierPlugin(Lunet.Core.SiteObject site, Lunet.Bundles.BundlePlugin bundlePlugin)`

#### Methods

- `System.String virtual Minify(System.String type, System.String content, System.String contentPath)`
