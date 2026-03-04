# Lunet.Datas Public API

Assembly path: `src/Lunet.Datas/bin/Release/net10.0/Lunet.Datas.dll`

Exported types: **6**

## Types

### `Lunet.Datas.DataFolderObject`

- Kind: `class`
- Base: `Lunet.Datas.DataObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DataFolderObject(Lunet.Datas.DatasPlugin parent, Zio.DirectoryEntry folder)`

#### Methods

- `System.String virtual ToString(System.String format, System.IFormatProvider formatProvider)`

#### Properties

- `Zio.DirectoryEntry Folder { get; }`
### `Lunet.Datas.DataObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Datas.DatasPlugin>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DataObject(Lunet.Datas.DatasPlugin parent)`
### `Lunet.Datas.DatasModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Datas.DatasPlugin>`

#### Constructors

- `DatasModule()`
### `Lunet.Datas.DatasPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DatasPlugin(Lunet.Core.SiteObject site)`

#### Properties

- `Lunet.Datas.DataObject RootDataObject { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Datas.IDataLoader> DataLoaders { get; }`
### `Lunet.Datas.DatasProcessor`

- Kind: `class`
- Base: `Lunet.Core.ProcessorBase<Lunet.Datas.DatasPlugin>`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DatasProcessor(Lunet.Datas.DatasPlugin plugin)`

#### Methods

- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Fields

- `const static System.String DataFolderName`
- `readonly static Zio.UPath DataFolder`
### `Lunet.Datas.IDataLoader`

- Kind: `interface`

#### Methods

- `System.Boolean abstract CanHandle(System.String fileExtension)`
- `System.Object abstract Load(Zio.FileEntry file)`
