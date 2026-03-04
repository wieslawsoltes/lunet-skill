# Lunet.Menus Public API

Assembly path: `src/Lunet.Menus/bin/Release/net10.0/Lunet.Menus.dll`

Exported types: **5**

## Types

### `Lunet.Menus.MenuCollection`

- Kind: `class`
- Base: `Lunet.Core.DynamicCollection<Lunet.Menus.MenuObject, Lunet.Menus.MenuCollection>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<Lunet.Menus.MenuObject>`, `System.Collections.Generic.IEnumerable<Lunet.Menus.MenuObject>`, `System.Collections.Generic.IList<Lunet.Menus.MenuObject>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `MenuCollection()`
### `Lunet.Menus.MenuModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Menus.MenuPlugin>`

#### Constructors

- `MenuModule()`
### `Lunet.Menus.MenuObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MenuObject()`

#### Methods

- `System.Boolean HasChildren()`
- `System.String Render(Scriban.TemplateContext context, Scriban.Parsing.SourceSpan span, Scriban.Runtime.ScriptObject options = optional)`
- `System.String RenderBreadcrumb(Scriban.TemplateContext context, Scriban.Parsing.SourceSpan span, Scriban.Runtime.ScriptObject options = optional)`
- `System.String virtual ToString(System.String format, System.IFormatProvider formatProvider)`

#### Properties

- `Lunet.Core.ContentObject Page { get; set; }`
- `Lunet.Menus.MenuCollection Children { get; }`
- `Lunet.Menus.MenuObject Parent { get; set; }`
- `System.Boolean Folder { get; set; }`
- `System.Boolean Generated { get; set; }`
- `System.Boolean Separator { get; set; }`
- `System.Int32 Width { get; set; }`
- `System.String Name { get; set; }`
- `System.String Path { get; set; }`
- `System.String Post { get; set; }`
- `System.String Pre { get; set; }`
- `System.String Target { get; set; }`
- `System.String Title { get; set; }`
- `System.String Url { get; set; }`
### `Lunet.Menus.MenuPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MenuPlugin(Lunet.Core.SiteObject site, Lunet.Bundles.BundlePlugin bundlePlugin)`

#### Methods

- `System.Void RegisterMenu(System.String name, Lunet.Menus.MenuObject menu, System.Boolean overwrite = optional)`
- `System.Void SetPageMenu(Lunet.Core.ContentObject page, Lunet.Menus.MenuObject menu, System.Boolean force = optional)`

#### Properties

- `Lunet.Menus.MenuProcessor Processor { get; }`
- `System.Int32 AsyncLoadThreshold { get; set; }`
- `System.String AsyncPartialsFolder { get; set; }`
### `Lunet.Menus.MenuProcessor`

- Kind: `class`
- Base: `Lunet.Core.ContentProcessor<Lunet.Menus.MenuPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MenuProcessor(Lunet.Menus.MenuPlugin plugin)`

#### Methods

- `Lunet.Core.ContentResult virtual TryProcessContent(Lunet.Core.ContentObject page, Lunet.Core.ContentProcessingStage stage)`
- `System.Void SetPageMenu(Lunet.Core.ContentObject page, Lunet.Menus.MenuObject menu, System.Boolean force)`
- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `System.String Name { get; }`

#### Fields

- `const static System.String MenuFileName`
