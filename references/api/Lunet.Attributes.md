# Lunet.Attributes Public API

Assembly path: `src/Lunet.Attributes/bin/Release/net10.0/Lunet.Attributes.dll`

Exported types: **4**

## Types

### `Lunet.Attributes.AttributesGlobber`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Attributes.AttributesObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `AttributesGlobber(Lunet.Attributes.AttributesObject parent, System.String pattern, System.Boolean match, Scriban.Runtime.ScriptObject setters)`

#### Properties

- `DotNet.Globbing.Glob Glob { get; set; }`
- `Scriban.Runtime.ScriptObject Setters { get; set; }`
- `System.Boolean Match { get; set; }`
- `System.String Pattern { get; set; }`
### `Lunet.Attributes.AttributesModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Attributes.AttributesPlugin>`

#### Constructors

- `AttributesModule()`
### `Lunet.Attributes.AttributesObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicCollection<Lunet.Attributes.AttributesGlobber, Lunet.Attributes.AttributesObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<Lunet.Attributes.AttributesGlobber>`, `System.Collections.Generic.IEnumerable<Lunet.Attributes.AttributesGlobber>`, `System.Collections.Generic.IList<Lunet.Attributes.AttributesGlobber>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `AttributesObject()`

#### Methods

- `Lunet.Attributes.AttributesGlobber Match(System.String pattern, Scriban.Runtime.ScriptObject setters)`
- `Lunet.Attributes.AttributesGlobber UnMatch(System.String pattern, Scriban.Runtime.ScriptObject setters)`
### `Lunet.Attributes.AttributesPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `AttributesPlugin(Lunet.Core.SiteObject site)`
