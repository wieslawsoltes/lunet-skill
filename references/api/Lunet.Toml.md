# Lunet.Toml Public API

Assembly path: `src/Lunet.Toml/bin/Release/net10.0/Lunet.Toml.dll`

Exported types: **4**

## Types

### `Lunet.Toml.TomlDataLoader`

- Kind: `class`
- Interfaces: `Lunet.Datas.IDataLoader`

#### Constructors

- `TomlDataLoader()`

#### Methods

- `System.Boolean virtual CanHandle(System.String fileExtension)`
- `System.Object virtual Load(Zio.FileEntry file)`
### `Lunet.Toml.TomlModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Toml.TomlPlugin>`

#### Constructors

- `TomlModule()`
### `Lunet.Toml.TomlPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `TomlPlugin(Lunet.Core.SiteObject site, Lunet.Datas.DatasPlugin dataPlugin)`
### `Lunet.Toml.TomlUtil`

- Kind: `static class`

#### Methods

- `System.Object static FromText(System.String text, System.String tomlFile = optional)`
