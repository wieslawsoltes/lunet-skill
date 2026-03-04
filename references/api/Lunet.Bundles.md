# Lunet.Bundles Public API

Assembly path: `src/Lunet.Bundles/bin/Release/net10.0/Lunet.Bundles.dll`

Exported types: **13**

## Types

### `Lunet.Bundles.BundleLink`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Bundles.BundleObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `BundleLink(Lunet.Bundles.BundleObject parent, System.String type, System.String path, System.String url, System.String urlWithoutBasePath, System.String mode)`

#### Properties

- `Lunet.Core.ContentObject ContentObject { get; set; }`
- `System.String Content { get; set; }`
- `System.String Mode { get; set; }`
- `System.String Path { get; set; }`
- `System.String Type { get; set; }`
- `System.String Url { get; set; }`
- `System.String UrlWithoutBasePath { get; set; }`
### `Lunet.Bundles.BundleModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Bundles.BundlePlugin>`

#### Constructors

- `BundleModule()`
### `Lunet.Bundles.BundleObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Bundles.BundlePlugin>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `BundleObject(Lunet.Bundles.BundlePlugin plugin, System.String name)`

#### Methods

- `System.Void AddContent(System.Object resourceOrPath, System.String pathOrUrl, System.String url = optional)`
- `System.Void AddCss(System.Object resourceOrPath, System.String path = optional)`
- `System.Void AddJs(System.Object resourceOrPath, System.String path = optional, System.String mode = optional)`
- `System.Void AddLink(System.String type, System.String path, System.String url = optional, System.String mode = optional)`
- `System.Void InsertLink(System.Int32 index, System.String type, System.String path, System.String url = optional, System.String mode = optional)`

#### Properties

- `Scriban.Runtime.ScriptObject UrlDestination { get; }`
- `System.Boolean Concat { get; set; }`
- `System.Boolean Minify { get; set; }`
- `System.Collections.Generic.List<Lunet.Bundles.BundleLink> Links { get; }`
- `System.String Minifier { get; set; }`
- `System.String MinifyExtension { get; set; }`
- `System.String Name { get; }`
### `Lunet.Bundles.BundleObjectProperties`

- Kind: `static class`

#### Fields

- `const static System.String Concat`
- `const static System.String ContentType`
- `const static System.String CssType`
- `const static System.String JsType`
- `const static System.String Links`
- `const static System.String Minifier`
- `const static System.String Minify`
- `const static System.String MinifyExtension`
- `const static System.String Name`
- `const static System.String UrlDestination`
### `Lunet.Bundles.BundlePlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `BundlePlugin(Lunet.Core.SiteObject site)`

#### Methods

- `Lunet.Bundles.BundleObject FindBundle(System.String bundleName)`
- `Lunet.Bundles.BundleObject GetOrCreateBundle(System.String bundleName)`

#### Properties

- `Lunet.Bundles.BundleProcessor BundleProcessor { get; }`
- `System.Collections.Generic.List<Lunet.Bundles.BundleObject> List { get; }`

#### Fields

- `const static System.String DefaultBundleName`
### `Lunet.Bundles.BundleProcessor`

- Kind: `class`
- Base: `Lunet.Core.ProcessorBase<Lunet.Bundles.BundlePlugin>`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `BundleProcessor(Lunet.Bundles.BundlePlugin bundlePlugin)`

#### Methods

- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `Lunet.Helpers.OrderedList<Lunet.Bundles.IContentMinifier> Minifiers { get; }`
### `Lunet.Bundles.IContentMinifier`

- Kind: `interface`

#### Methods

- `System.String abstract Minify(System.String type, System.String content, System.String contentPath = optional)`

#### Properties

- `System.String Name { get; }`
### `Lunet.Bundles.SourceMaps.MappingEntry`

- Kind: `class`

#### Constructors

- `MappingEntry()`

#### Methods

- `Lunet.Bundles.SourceMaps.MappingEntry Clone()`
- `System.Boolean IsValueEqual(Lunet.Bundles.SourceMaps.MappingEntry anEntry)`

#### Fields

- `Lunet.Bundles.SourceMaps.SourcePosition GeneratedSourcePosition`
- `Lunet.Bundles.SourceMaps.SourcePosition OriginalSourcePosition`
- `System.String OriginalFileName`
- `System.String OriginalName`
### `Lunet.Bundles.SourceMaps.SourceMap`

- Kind: `class`

#### Constructors

- `SourceMap()`

#### Methods

- `Lunet.Bundles.SourceMaps.MappingEntry virtual GetMappingEntryForGeneratedSourcePosition(Lunet.Bundles.SourceMaps.SourcePosition generatedSourcePosition)`
- `Lunet.Bundles.SourceMaps.SourceMap ApplySourceMap(Lunet.Bundles.SourceMaps.SourceMap submap, System.String sourceFile = optional)`
- `Lunet.Bundles.SourceMaps.SourceMap Clone()`

#### Fields

- `System.Collections.Generic.List<Lunet.Bundles.SourceMaps.MappingEntry> ParsedMappings`
- `System.Collections.Generic.List<System.String> Names`
- `System.Collections.Generic.List<System.String> Sources`
- `System.Int32 Version`
- `System.String File`
- `System.String Mappings`
### `Lunet.Bundles.SourceMaps.SourceMapGenerator`

- Kind: `class`

#### Constructors

- `SourceMapGenerator()`

#### Methods

- `System.String GenerateSourceMapInlineComment(Lunet.Bundles.SourceMaps.SourceMap sourceMap, Newtonsoft.Json.JsonSerializerSettings jsonSerializerSettings = optional)`
- `System.String SerializeMapping(Lunet.Bundles.SourceMaps.SourceMap sourceMap, Newtonsoft.Json.JsonSerializerSettings jsonSerializerSettings = optional)`
### `Lunet.Bundles.SourceMaps.SourceMapParser`

- Kind: `class`

#### Constructors

- `SourceMapParser()`

#### Methods

- `Lunet.Bundles.SourceMaps.SourceMap ParseSourceMap(System.IO.StreamReader sourceMapStream)`
### `Lunet.Bundles.SourceMaps.SourceMapTransformer`

- Kind: `static class`

#### Methods

- `Lunet.Bundles.SourceMaps.SourceMap static Flatten(Lunet.Bundles.SourceMaps.SourceMap sourceMap)`
### `Lunet.Bundles.SourceMaps.SourcePosition`

- Kind: `class`
- Interfaces: `System.IComparable<Lunet.Bundles.SourceMaps.SourcePosition>`

#### Constructors

- `SourcePosition()`

#### Methods

- `Lunet.Bundles.SourceMaps.SourcePosition Clone()`
- `System.Boolean IsEqualish(Lunet.Bundles.SourceMaps.SourcePosition other)`
- `System.Boolean static op_GreaterThan(Lunet.Bundles.SourceMaps.SourcePosition x, Lunet.Bundles.SourceMaps.SourcePosition y)`
- `System.Boolean static op_LessThan(Lunet.Bundles.SourceMaps.SourcePosition x, Lunet.Bundles.SourceMaps.SourcePosition y)`
- `System.Int32 virtual CompareTo(Lunet.Bundles.SourceMaps.SourcePosition other)`

#### Fields

- `System.Int32 ZeroBasedColumnNumber`
- `System.Int32 ZeroBasedLineNumber`
