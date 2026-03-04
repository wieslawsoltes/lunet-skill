# Lunet.Taxonomies Public API

Assembly path: `src/Lunet.Taxonomies/bin/Release/net10.0/Lunet.Taxonomies.dll`

Exported types: **7**

## Types

### `Lunet.Taxonomies.Taxonomy`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Taxonomies.TaxonomyProcessor>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `Taxonomy(Lunet.Taxonomies.TaxonomyProcessor parent, System.String name, System.String single, System.String url, Scriban.Runtime.ScriptObject map)`

#### Methods

- `System.Void AddTerm(Lunet.Taxonomies.TaxonomyTerm term)`

#### Properties

- `Lunet.Core.DynamicObject Terms { get; }`
- `Lunet.Taxonomies.TaxonomyTermCollection ByCount { get; }`
- `Lunet.Taxonomies.TaxonomyTermCollection ByName { get; }`
- `Scriban.Runtime.ScriptObject Map { get; }`
- `System.String Name { get; }`
- `System.String Single { get; }`
- `System.String Url { get; }`
### `Lunet.Taxonomies.TaxonomyCollection`

- Kind: `class`
- Base: `Lunet.Core.DynamicCollection<Lunet.Taxonomies.Taxonomy, Lunet.Taxonomies.TaxonomyCollection>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<Lunet.Taxonomies.Taxonomy>`, `System.Collections.Generic.IEnumerable<Lunet.Taxonomies.Taxonomy>`, `System.Collections.Generic.IList<Lunet.Taxonomies.Taxonomy>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `TaxonomyCollection()`
### `Lunet.Taxonomies.TaxonomyModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Taxonomies.TaxonomyPlugin>`

#### Constructors

- `TaxonomyModule()`
### `Lunet.Taxonomies.TaxonomyPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `TaxonomyPlugin(Lunet.Core.SiteObject site, Lunet.Layouts.LayoutPlugin layoutPlugin)`
### `Lunet.Taxonomies.TaxonomyProcessor`

- Kind: `class`
- Base: `Lunet.Core.ProcessorBase<Lunet.Taxonomies.TaxonomyPlugin>`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `TaxonomyProcessor(Lunet.Taxonomies.TaxonomyPlugin plugin, Lunet.Layouts.LayoutPlugin layoutPlugin)`

#### Methods

- `Lunet.Taxonomies.Taxonomy Find(System.String name)`
- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `Lunet.Taxonomies.TaxonomyCollection List { get; }`
- `System.String Name { get; }`
### `Lunet.Taxonomies.TaxonomyTerm`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Taxonomies.Taxonomy>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `TaxonomyTerm(Lunet.Taxonomies.Taxonomy parent, System.String name)`

#### Properties

- `Lunet.Core.PageCollection Pages { get; }`
- `System.String Name { get; }`
- `System.String Url { get; }`
### `Lunet.Taxonomies.TaxonomyTermCollection`

- Kind: `class`
- Base: `Lunet.Core.DynamicCollection<Lunet.Taxonomies.TaxonomyTerm, Lunet.Taxonomies.TaxonomyTermCollection>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<Lunet.Taxonomies.TaxonomyTerm>`, `System.Collections.Generic.IEnumerable<Lunet.Taxonomies.TaxonomyTerm>`, `System.Collections.Generic.IList<Lunet.Taxonomies.TaxonomyTerm>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `TaxonomyTermCollection()`
- `TaxonomyTermCollection(System.Collections.Generic.IEnumerable<Lunet.Taxonomies.TaxonomyTerm> values)`
