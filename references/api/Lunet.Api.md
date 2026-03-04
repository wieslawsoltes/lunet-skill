# Lunet.Api Public API

Assembly path: `src/Lunet.Api/bin/Release/net10.0/Lunet.Api.dll`

Exported types: **3**

## Types

### `Lunet.Api.ApiConfig`

- Kind: `abstract class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`
### `Lunet.Api.ApiModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Api.ApiPlugin>`

#### Constructors

- `ApiModule()`
### `Lunet.Api.ApiPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ApiPlugin(Lunet.Core.SiteObject site)`

#### Methods

- `System.Void Register(System.String name, System.Func<Lunet.Api.ApiConfig> apiFunc)`
