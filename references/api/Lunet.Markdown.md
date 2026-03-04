# Lunet.Markdown Public API

Assembly path: `src/Lunet.Markdig/bin/Release/net10.0/Lunet.Markdown.dll`

Exported types: **4**

## Types

### `Lunet.Markdown.Extensions.XRefMarkdownExtension`

- Kind: `class`
- Interfaces: `Markdig.IMarkdownExtension`

#### Constructors

- `XRefMarkdownExtension()`

#### Methods

- `System.Void virtual Setup(Markdig.MarkdownPipeline pipeline, Markdig.Renderers.IMarkdownRenderer renderer)`
- `System.Void virtual Setup(Markdig.MarkdownPipelineBuilder pipeline)`
### `Lunet.Markdown.MarkdownModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Markdown.MarkdownPlugin>`

#### Constructors

- `MarkdownModule()`
### `Lunet.Markdown.MarkdownOptions`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Markdown.MarkdownPlugin>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MarkdownOptions(Lunet.Markdown.MarkdownPlugin parent)`

#### Properties

- `System.String AutoIdKind { get; set; }`
- `System.String CssImageAttribute { get; set; }`
- `System.String Extensions { get; set; }`
### `Lunet.Markdown.MarkdownPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Lunet.Layouts.ILayoutConverter`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `MarkdownPlugin(Lunet.Core.SiteObject site, Lunet.Layouts.LayoutPlugin layoutPlugin)`

#### Methods

- `System.Void virtual Convert(Lunet.Core.ContentObject page)`

#### Properties

- `System.Boolean ShouldConvertIfNoLayout { get; }`
