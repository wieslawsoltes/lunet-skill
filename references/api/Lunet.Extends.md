# Lunet.Extends Public API

Assembly path: `src/Lunet.Extends/bin/Release/net10.0/Lunet.Extends.dll`

Exported types: **3**

## Types

### `Lunet.Extends.ExtendObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Properties

- `Lunet.Core.SiteObject Site { get; }`
- `System.String Description { get; }`
- `System.String FullName { get; }`
- `System.String Name { get; }`
- `System.String Url { get; }`
- `System.String Version { get; }`
- `Zio.IFileSystem FileSystem { get; }`
### `Lunet.Extends.ExtendsModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Extends.ExtendsPlugin>`

#### Constructors

- `ExtendsModule()`
### `Lunet.Extends.ExtendsPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ExtendsPlugin(Lunet.Core.SiteObject site)`

#### Methods

- `Lunet.Extends.ExtendObject LoadExtend(System.String extendName, System.Boolean isPrivate)`
- `Lunet.Extends.ExtendObject TryInstall(System.String extendName, System.Boolean isPrivate = optional)`

#### Properties

- `System.Collections.Generic.List<Lunet.Extends.ExtendObject> CurrentList { get; }`
- `Zio.UPath ExtendsFolder { get; }`
- `Zio.UPath PrivateExtendsFolder { get; }`
