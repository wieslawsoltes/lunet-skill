# Lunet.Json Public API

Assembly path: `src/Lunet.Json/bin/Release/net10.0/Lunet.Json.dll`

Exported types: **4**

## Types

### `Lunet.Json.JsonDataLoader`

- Kind: `class`
- Interfaces: `Lunet.Datas.IDataLoader`

#### Constructors

- `JsonDataLoader()`

#### Methods

- `System.Boolean virtual CanHandle(System.String fileExtension)`
- `System.Object virtual Load(Zio.FileEntry file)`
### `Lunet.Json.JsonModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Json.JsonPlugin>`

#### Constructors

- `JsonModule()`
### `Lunet.Json.JsonPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `JsonPlugin(Lunet.Core.SiteObject site, Lunet.Datas.DatasPlugin dataPlugin)`
### `Lunet.Json.JsonUtil`

- Kind: `static class`

#### Methods

- `System.Object static FromStream(System.IO.Stream stream, System.String jsonFile = optional)`
- `System.Object static FromText(System.String text, System.String jsonFile = optional)`
