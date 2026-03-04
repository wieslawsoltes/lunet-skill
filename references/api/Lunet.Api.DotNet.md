# Lunet.Api.DotNet Public API

Assembly path: `src/Lunet.Api.DotNet/bin/Release/net10.0/Lunet.Api.DotNet.dll`

Exported types: **13**

## Types

### `Lunet.Api.DotNet.ApiDotNetConfig`

- Kind: `class`
- Base: `Lunet.Api.ApiConfig`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ApiDotNetConfig()`

#### Properties

- `Scriban.Runtime.ScriptArray Projects { get; set; }`
- `Scriban.Runtime.ScriptArray References { get; set; }`
- `Scriban.Runtime.ScriptObject KindIcons { get; set; }`
- `Scriban.Runtime.ScriptObject Properties { get; set; }`
- `System.Int32 MaxSlugLength { get; set; }`
- `System.Int32 MenuWidth { get; set; }`
- `System.Object ExternalApis { get; set; }`
- `System.String BasePath { get; set; }`
- `System.String IncludeHelper { get; set; }`
- `System.String Layout { get; set; }`
- `System.String MenuName { get; set; }`
- `System.String MenuTitle { get; set; }`
- `System.String SolutionConfiguration { get; set; }`
- `System.String Title { get; set; }`
### `Lunet.Api.DotNet.ApiDotNetModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Api.DotNet.ApiDotNetPlugin>`

#### Constructors

- `ApiDotNetModule()`
### `Lunet.Api.DotNet.ApiDotNetObject`

- Kind: `class`
- Base: `Scriban.Runtime.ScriptObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ApiDotNetObject()`

#### Methods

- `System.Void Clear()`

#### Properties

- `Scriban.Runtime.ScriptArray<Scriban.Runtime.ScriptObject> Namespaces { get; }`
- `Scriban.Runtime.ScriptObject Objects { get; }`
- `Scriban.Runtime.ScriptObject References { get; }`
### `Lunet.Api.DotNet.ApiDotNetPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ApiDotNetPlugin(Lunet.Core.SiteObject site, Lunet.Api.ApiPlugin api, Lunet.Bundles.BundlePlugin bundles = optional, Lunet.Menus.MenuPlugin menus = optional)`

#### Properties

- `Lunet.Api.ApiPlugin Api { get; }`
- `Lunet.Bundles.BundlePlugin Bundles { get; }`
- `Lunet.Menus.MenuPlugin Menus { get; }`
### `Lunet.Api.DotNet.ApiDotNetProcessor`

- Kind: `class`
- Base: `Lunet.Core.ProcessorBase<Lunet.Api.DotNet.ApiDotNetPlugin>`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ApiDotNetProcessor(Lunet.Api.DotNet.ApiDotNetPlugin plugin, Lunet.Api.DotNet.ApiDotNetConfig config)`

#### Methods

- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `Lunet.Api.DotNet.ApiDotNetConfig Config { get; }`
- `Lunet.Api.DotNet.ApiDotNetObject ApiDotNetObject { get; }`
- `System.Collections.Generic.List<Lunet.Api.DotNet.ApiDotNetProject> Projects { get; }`
### `Lunet.Api.DotNet.ApiDotNetProject`

- Kind: `class`

#### Constructors

- `ApiDotNetProject()`

#### Properties

- `Lunet.Api.DotNet.ApitDotNetCacheState CacheState { get; set; }`
- `Scriban.Runtime.ScriptObject Api { get; set; }`
- `Scriban.Runtime.ScriptObject Properties { get; set; }`
- `System.Collections.Generic.List<System.String> IncludedReferenceAssemblies { get; set; }`
- `System.String Name { get; set; }`
- `System.String Path { get; set; }`
- `Zio.UPath CachePath { get; set; }`
### `Lunet.Api.DotNet.ApiDotNetResultSelector`

- Kind: `static class`

#### Methods

- `System.String static SelectBestResult(System.Collections.Generic.IReadOnlyList<System.String> results, System.String projectPath, System.String projectName, System.String targetFramework)`
### `Lunet.Api.DotNet.ApiDotNetSlugGenerator`

- Kind: `static class`

#### Methods

- `System.Int32 static NormalizeMaxLength(System.Int32 requestedLength)`
- `System.String static BuildSlug(System.String uid, System.Int32 maxLength, System.Int32 disambiguator = optional)`

#### Fields

- `const static System.Int32 DefaultMaxLength`
- `const static System.Int32 MaxAllowedLength`
- `const static System.Int32 MinMaxLength`
### `Lunet.Api.DotNet.ApiDotNetSlugResolver`

- Kind: `class`

#### Constructors

- `ApiDotNetSlugResolver(System.Int32 maxLength)`

#### Methods

- `System.String GetSlug(System.String uid)`
### `Lunet.Api.DotNet.ApitDotNetCacheState`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Api.DotNet.ApitDotNetCacheState Found`
- `const static Lunet.Api.DotNet.ApitDotNetCacheState Invalid`
- `const static Lunet.Api.DotNet.ApitDotNetCacheState New`
- `const static Lunet.Api.DotNet.ApitDotNetCacheState NotFound`
### `Lunet.Api.DotNet.DotNetProgram`

- Kind: `class`

#### Constructors

- `DotNetProgram(System.String command)`

#### Methods

- `System.String Run()`
- `System.String static EscapePath(System.String path)`

#### Properties

- `System.Collections.Generic.Dictionary<System.String, System.Object> Properties { get; }`
- `System.Collections.Generic.List<System.String> Arguments { get; }`
- `System.String Command { get; }`
- `System.String WorkingDirectory { get; set; }`
### `Lunet.Api.DotNet.DotNetProgramException`

- Kind: `class`
- Base: `System.Exception`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DotNetProgramException(System.String message)`
- `DotNetProgramException(System.String message, System.Exception innerException)`
### `Lunet.Api.DotNet.Extractor.ExtractorHelper`

- Kind: `static class`

#### Methods

- `System.Collections.Generic.List<System.String> static FindResults(System.String text)`
- `System.String static FormatResult(System.String path)`
- `System.String static SelectBestResult(System.Collections.Generic.IReadOnlyList<System.String> results, System.String projectPath, System.String projectName, System.String targetFramework)`

#### Fields

- `const static System.String ResultId`
