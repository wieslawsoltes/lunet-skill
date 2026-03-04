# Lunet.Summarizer Public API

Assembly path: `src/Lunet.Summarizer/bin/Release/net10.0/Lunet.Summarizer.dll`

Exported types: **4**

## Types

### `Lunet.Summarizer.SummarizerHelper`

- Kind: `static class`

#### Methods

- `System.Void static UpdateSummary(Lunet.Core.ContentObject page)`

#### Fields

- `const static System.Int32 DefaultSummaryWordCount`
### `Lunet.Summarizer.SummarizerModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Summarizer.SummarizerPlugin>`

#### Constructors

- `SummarizerModule()`
### `Lunet.Summarizer.SummarizerPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SummarizerPlugin(Lunet.Core.SiteObject site)`
### `Lunet.Summarizer.SummarizerProcessor`

- Kind: `class`
- Base: `Lunet.Core.ContentProcessor<Lunet.Summarizer.SummarizerPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SummarizerProcessor(Lunet.Summarizer.SummarizerPlugin plugin)`

#### Methods

- `Lunet.Core.ContentResult virtual TryProcessContent(Lunet.Core.ContentObject page, Lunet.Core.ContentProcessingStage stage)`
