# Lunet.Layouts Public API

Assembly path: `src/Lunet.Layouts/bin/Release/net10.0/Lunet.Layouts.dll`

Exported types: **6**

## Types

### `Lunet.Layouts.ILayoutConverter`

- Kind: `interface`

#### Methods

- `System.Void abstract Convert(Lunet.Core.ContentObject page)`

#### Properties

- `System.Boolean ShouldConvertIfNoLayout { get; }`
### `Lunet.Layouts.LayoutContentObject`

- Kind: `class`
- Base: `Lunet.Core.TemplateObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `LayoutContentObject(Lunet.Core.SiteObject site, ref Zio.FileSystemItem sourceFileInfo, Lunet.Scripts.ScriptInstance scriptInstance)`
### `Lunet.Layouts.LayoutModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Layouts.LayoutPlugin>`

#### Constructors

- `LayoutModule()`
### `Lunet.Layouts.LayoutPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `LayoutPlugin(Lunet.Core.SiteObject site)`

#### Properties

- `Lunet.Layouts.LayoutProcessor Processor { get; }`
### `Lunet.Layouts.LayoutProcessor`

- Kind: `class`
- Base: `Lunet.Core.ContentProcessor<Lunet.Layouts.LayoutPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `LayoutProcessor(Lunet.Layouts.LayoutPlugin plugin)`

#### Methods

- `Lunet.Core.ContentResult virtual TryProcessContent(Lunet.Core.ContentObject page, Lunet.Core.ContentProcessingStage stage)`
- `System.Void RegisterConverter(Lunet.Core.ContentType contentType, Lunet.Layouts.ILayoutConverter converter)`
- `System.Void RegisterLayoutPathProvider(System.String layoutType, Lunet.Layouts.LayoutProcessor.GetLayoutPathsDelegate layoutPathsDelegate)`

#### Properties

- `System.String Name { get; }`

#### Fields

- `const static System.String DefaultLayoutName`
- `const static System.String LayoutFolderName`
- `readonly static Scriban.Syntax.ScriptVariableGlobal ContentVariable`
### `Lunet.Layouts.LayoutProcessor.GetLayoutPathsDelegate`

- Kind: `class`
- Base: `System.MulticastDelegate`
- Interfaces: `System.ICloneable`, `System.Runtime.Serialization.ISerializable`

#### Constructors

- `GetLayoutPathsDelegate(System.Object object, System.IntPtr method)`

#### Methods

- `System.Collections.Generic.IEnumerable<Zio.UPath> virtual EndInvoke(System.IAsyncResult result)`
- `System.Collections.Generic.IEnumerable<Zio.UPath> virtual Invoke(Lunet.Core.SiteObject site, System.String layoutName, System.String layoutType)`
- `System.IAsyncResult virtual BeginInvoke(Lunet.Core.SiteObject site, System.String layoutName, System.String layoutType, System.AsyncCallback callback, System.Object object)`
