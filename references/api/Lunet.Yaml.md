# Lunet.Yaml Public API

Assembly path: `src/Lunet.Yaml/bin/Release/net10.0/Lunet.Yaml.dll`

Exported types: **5**

## Types

### `Lunet.Yaml.YamlDataLoader`

- Kind: `class`
- Interfaces: `Lunet.Datas.IDataLoader`

#### Constructors

- `YamlDataLoader()`

#### Methods

- `System.Boolean virtual CanHandle(System.String fileExtension)`
- `System.Object virtual Load(Zio.FileEntry file)`
### `Lunet.Yaml.YamlFrontMatterParser`

- Kind: `class`
- Interfaces: `Lunet.Core.IFrontMatterParser`

#### Constructors

- `YamlFrontMatterParser()`

#### Methods

- `Lunet.Core.IFrontMatter virtual TryParse(System.String text, System.String sourceFilePath, out Scriban.Parsing.TextPosition position)`
- `System.Boolean virtual CanHandle(System.ReadOnlySpan<System.Byte> header)`
- `System.Boolean virtual CanHandle(System.ReadOnlySpan<System.Char> header)`
### `Lunet.Yaml.YamlModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Yaml.YamlPlugin>`

#### Constructors

- `YamlModule()`
### `Lunet.Yaml.YamlPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `YamlPlugin(Lunet.Core.SiteObject site, Lunet.Datas.DatasPlugin datasPlugin)`
### `Lunet.Yaml.YamlUtil`

- Kind: `static class`

#### Methods

- `System.Object static FromText(System.String yamlText, System.String yamlFile = optional)`
- `System.Object static FromYamlFrontMatter(System.String yamlText, out Scriban.Parsing.TextPosition position, System.String yamlFile = optional)`
