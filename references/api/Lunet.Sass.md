# Lunet.Sass Public API

Assembly path: `src/Lunet.Sass/bin/Release/net10.0/Lunet.Sass.dll`

Exported types: **13**

## Types

### `Lunet.Sass.DartSass.DartSassCompilationException`

- Kind: `class`
- Base: `Lunet.Sass.DartSass.DartSassException`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DartSassCompilationException(System.String message, System.Int32 exitCode, System.String standardError = optional, System.String standardOutput = optional)`

#### Properties

- `System.Int32 ExitCode { get; }`
- `System.String StandardError { get; }`
- `System.String StandardOutput { get; }`
### `Lunet.Sass.DartSass.DartSassCompiler`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `DartSassCompiler(System.String version = optional, System.String cacheDirectory = optional)`

#### Methods

- `Lunet.Sass.DartSass.DartSassResult CompileFile(System.String inputFile, System.String outputFile = optional, System.Action<Lunet.Sass.DartSass.DartSassOptions> configureOptions = optional, System.Threading.CancellationToken cancellationToken = optional)`
- `Lunet.Sass.DartSass.DartSassResult CompileString(System.String scss, System.Action<Lunet.Sass.DartSass.DartSassOptions> configureOptions = optional, System.Threading.CancellationToken cancellationToken = optional)`
- `System.Threading.Tasks.Task InitializeAsync(System.Threading.CancellationToken cancellationToken = optional)`
- `System.Threading.Tasks.Task<Lunet.Sass.DartSass.DartSassResult> CompileAsync(Lunet.Sass.DartSass.DartSassOptions options, System.Threading.CancellationToken cancellationToken = optional)`
- `System.Threading.Tasks.Task<Lunet.Sass.DartSass.DartSassResult> CompileFileAsync(System.String inputFile, System.String outputFile = optional, System.Action<Lunet.Sass.DartSass.DartSassOptions> configureOptions = optional, System.Threading.CancellationToken cancellationToken = optional)`
- `System.Threading.Tasks.Task<Lunet.Sass.DartSass.DartSassResult> CompileStringAsync(System.String scss, System.Action<Lunet.Sass.DartSass.DartSassOptions> configureOptions = optional, System.Threading.CancellationToken cancellationToken = optional)`
- `System.Threading.Tasks.Task<System.String> CompileToStringAsync(System.String scss, System.Action<Lunet.Sass.DartSass.DartSassOptions> configureOptions = optional, System.Threading.CancellationToken cancellationToken = optional)`
- `System.Void virtual Dispose()`

#### Properties

- `System.Boolean IsInitialized { get; }`
- `System.String CacheDirectory { get; }`
- `System.String Version { get; }`
### `Lunet.Sass.DartSass.DartSassDownloadException`

- Kind: `class`
- Base: `Lunet.Sass.DartSass.DartSassException`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DartSassDownloadException(System.String message, System.Exception innerException, System.String url = optional)`
- `DartSassDownloadException(System.String message, System.String url = optional)`

#### Properties

- `System.String Url { get; }`
### `Lunet.Sass.DartSass.DartSassException`

- Kind: `class`
- Base: `System.Exception`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DartSassException(System.String message)`
- `DartSassException(System.String message, System.Exception innerException)`
### `Lunet.Sass.DartSass.DartSassExtractionException`

- Kind: `class`
- Base: `Lunet.Sass.DartSass.DartSassException`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DartSassExtractionException(System.String message, System.Exception innerException, System.String archivePath = optional)`
- `DartSassExtractionException(System.String message, System.String archivePath = optional)`

#### Properties

- `System.String ArchivePath { get; }`
### `Lunet.Sass.DartSass.DartSassOptions`

- Kind: `class`

#### Constructors

- `DartSassOptions()`

#### Properties

- `Lunet.Sass.DartSass.OutputStyle Style { get; set; }`
- `System.Boolean Indented { get; set; }`
- `System.Boolean Interactive { get; set; }`
- `System.Boolean Update { get; set; }`
- `System.Boolean Version { get; set; }`
- `System.Boolean Watch { get; set; }`
- `System.Collections.Generic.List<System.String> CustomArguments { get; set; }`
- `System.Collections.Generic.List<System.String> FatalDeprecation { get; set; }`
- `System.Collections.Generic.List<System.String> FutureDeprecation { get; set; }`
- `System.Collections.Generic.List<System.String> LoadPaths { get; set; }`
- `System.Collections.Generic.List<System.String> SilenceDeprecation { get; set; }`
- `System.Nullable<Lunet.Sass.DartSass.PkgImporterType> PkgImporter { get; set; }`
- `System.Nullable<Lunet.Sass.DartSass.SourceMapUrls> SourceMapUrls { get; set; }`
- `System.Nullable<System.Boolean> Charset { get; set; }`
- `System.Nullable<System.Boolean> Color { get; set; }`
- `System.Nullable<System.Boolean> EmbedSourceMap { get; set; }`
- `System.Nullable<System.Boolean> EmbedSources { get; set; }`
- `System.Nullable<System.Boolean> ErrorCss { get; set; }`
- `System.Nullable<System.Boolean> Poll { get; set; }`
- `System.Nullable<System.Boolean> Quiet { get; set; }`
- `System.Nullable<System.Boolean> QuietDeps { get; set; }`
- `System.Nullable<System.Boolean> SourceMap { get; set; }`
- `System.Nullable<System.Boolean> StopOnError { get; set; }`
- `System.Nullable<System.Boolean> Trace { get; set; }`
- `System.Nullable<System.Boolean> Unicode { get; set; }`
- `System.Nullable<System.Boolean> Verbose { get; set; }`
- `System.String Input { get; set; }`
- `System.String Output { get; set; }`
- `System.String Stdin { get; set; }`
### `Lunet.Sass.DartSass.DartSassResult`

- Kind: `class`

#### Constructors

- `DartSassResult()`

#### Properties

- `System.Boolean Success { get; set; }`
- `System.Int32 ExitCode { get; set; }`
- `System.String Css { get; set; }`
- `System.String Stderr { get; set; }`
### `Lunet.Sass.DartSass.OutputStyle`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Sass.DartSass.OutputStyle Compressed`
- `const static Lunet.Sass.DartSass.OutputStyle Expanded`
### `Lunet.Sass.DartSass.PkgImporterType`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Sass.DartSass.PkgImporterType Node`
### `Lunet.Sass.DartSass.SourceMapUrls`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Sass.DartSass.SourceMapUrls Absolute`
- `const static Lunet.Sass.DartSass.SourceMapUrls Relative`
### `Lunet.Sass.DartSassTransform`

- Kind: `class`

#### Constructors

- `DartSassTransform()`

#### Methods

- `System.String static Minify(System.String content)`
- `System.Void static Convert(Lunet.Core.ContentObject file, System.Collections.Generic.List<Zio.DirectoryEntry> includePaths, Lunet.Core.SiteObject site)`
### `Lunet.Sass.SassModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Sass.SassPlugin>`

#### Constructors

- `SassModule()`
### `Lunet.Sass.SassPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Lunet.Layouts.ILayoutConverter`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SassPlugin(Lunet.Core.SiteObject site, Lunet.Layouts.LayoutPlugin layoutPlugin)`

#### Methods

- `System.Void virtual Convert(Lunet.Core.ContentObject file)`

#### Properties

- `Lunet.Core.PathCollection Includes { get; }`
- `System.Boolean ShouldConvertIfNoLayout { get; }`
- `System.String Name { get; }`

#### Fields

- `readonly static Lunet.Core.ContentType ScssType`
