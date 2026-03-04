# Lunet.Resources Public API

Assembly path: `src/Lunet.Resources/bin/Release/net10.0/Lunet.Resources.dll`

Exported types: **6**

## Types

### `Lunet.Resources.NpmResourceProvider`

- Kind: `class`
- Base: `Lunet.Resources.ResourceProvider`

#### Constructors

- `NpmResourceProvider(Lunet.Resources.ResourcePlugin plugin)`

#### Properties

- `System.String RegistryUrl { get; set; }`
### `Lunet.Resources.ResourceInstallFlags`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Resources.ResourceInstallFlags NoInstall`
- `const static Lunet.Resources.ResourceInstallFlags None`
- `const static Lunet.Resources.ResourceInstallFlags PreRelease`
- `const static Lunet.Resources.ResourceInstallFlags Private`
### `Lunet.Resources.ResourceModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Resources.ResourcePlugin>`

#### Constructors

- `ResourceModule()`
### `Lunet.Resources.ResourceObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ResourceObject(Lunet.Resources.ResourceProvider provider, System.String name, System.String version, Zio.DirectoryEntry absoluteDirectory)`

#### Properties

- `Lunet.Resources.ResourceProvider Provider { get; }`
- `System.String Name { get; }`
- `System.String Version { get; }`
- `Zio.DirectoryEntry AbsoluteDirectory { get; }`
- `Zio.UPath Path { get; }`
### `Lunet.Resources.ResourcePlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ResourcePlugin(Lunet.Core.SiteObject site)`

#### Methods

- `Lunet.Resources.ResourceObject TryLoadResource(System.String providerName, System.String packageName, System.String packageVersion = optional, Lunet.Resources.ResourceInstallFlags flags = optional)`

#### Properties

- `Lunet.Helpers.OrderedList<Lunet.Resources.ResourceProvider> Providers { get; }`

#### Fields

- `readonly static Zio.UPath ResourceFolder`
### `Lunet.Resources.ResourceProvider`

- Kind: `abstract class`

#### Methods

- `Lunet.Resources.ResourceObject Find(System.String resourceName, System.String resourceVersion)`
- `Lunet.Resources.ResourceObject GetOrInstall(System.String resourceName, System.String resourceVersion, Lunet.Resources.ResourceInstallFlags flags)`

#### Properties

- `Lunet.Resources.ResourcePlugin Plugin { get; }`
- `System.Collections.Generic.IEnumerable<Lunet.Resources.ResourceObject> ResourcesForScripting { get; }`
- `System.Collections.Generic.List<Lunet.Resources.ResourceObject> Resources { get; }`
- `System.String Name { get; }`
