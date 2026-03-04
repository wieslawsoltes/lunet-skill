# Lunet.Core Public API

Assembly path: `src/Lunet.Core/bin/Release/net10.0/Lunet.Core.dll`

Exported types: **81**

## Types

### `Lunet.Core.BuiltinsObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Core.SiteObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `BuiltinsObject(Lunet.Core.SiteObject parent)`

#### Methods

- `System.Void Initialize()`

#### Properties

- `Lunet.Core.DynamicObject LogObject { get; }`
- `Lunet.Core.LunetObject LunetObject { get; }`
- `Lunet.Core.SiteObject Site { get; }`
- `System.Object Head { get; set; }`
- `System.String Name { get; }`
### `Lunet.Core.Commands.CleanCommandRunner`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteCommandRunner`

#### Constructors

- `CleanCommandRunner()`

#### Methods

- `System.Threading.Tasks.Task<Lunet.Core.RunnerResult> virtual RunAsync(Lunet.Core.SiteRunner runner, System.Threading.CancellationToken cancellationToken)`
### `Lunet.Core.Commands.InitCommandRunner`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteCommandRunner`

#### Constructors

- `InitCommandRunner()`

#### Methods

- `System.Threading.Tasks.Task<Lunet.Core.RunnerResult> virtual RunAsync(Lunet.Core.SiteRunner runner, System.Threading.CancellationToken cancellationToken)`

#### Properties

- `System.Boolean Force { get; set; }`
### `Lunet.Core.ContentDependency`

- Kind: `abstract class`
### `Lunet.Core.ContentLayoutTypes`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ContentLayoutTypes()`

#### Methods

- `System.Void AddListType(System.String type)`

#### Fields

- `const static System.Int32 ListWeight`
- `const static System.Int32 SingleWeight`
- `const static System.String List`
- `const static System.String Single`
### `Lunet.Core.ContentObject`

- Kind: `abstract class`
- Base: `Lunet.Core.TemplateObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Methods

- `System.String GetOrLoadContent()`
- `System.Void AddDefer(System.String textToReplace, Scriban.Syntax.ScriptExpression expression)`
- `System.Void ApplyDefer()`
- `System.Void ChangeContentType(Lunet.Core.ContentType newContentType)`
- `System.Void Initialize()`
- `Zio.UPath GetDestinationDirectory()`
- `Zio.UPath GetDestinationPath()`

#### Properties

- `Lunet.Core.ContentType ContentType { get; set; }`
- `System.Boolean Discard { get; set; }`
- `System.DateTime Date { get; set; }`
- `System.Int32 Weight { get; set; }`
- `System.String Content { get; set; }`
- `System.String Layout { get; set; }`
- `System.String LayoutType { get; set; }`
- `System.String Section { get; }`
- `System.String Slug { get; set; }`
- `System.String Summary { get; set; }`
- `System.String Title { get; set; }`
- `System.String Uid { get; set; }`
- `System.String Url { get; set; }`
- `System.String UrlWithoutBasePath { get; set; }`
- `Zio.UPath PathInSection { get; }`
### `Lunet.Core.ContentObjectType`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Core.ContentObjectType Dynamic`
- `const static Lunet.Core.ContentObjectType File`
### `Lunet.Core.ContentPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ContentPlugin(Lunet.Core.SiteObject site)`

#### Methods

- `System.Boolean TryCopyContentToOutput(Lunet.Core.ContentObject fromFile, Zio.UPath outputPath)`
- `System.Boolean static IsListLayout(System.String layoutType)`
- `System.Void CreateDirectory(Zio.DirectoryEntry directory)`
- `System.Void PreInitialize()`
- `System.Void ProcessPages(Lunet.Core.PageCollection pages, System.Boolean copyOutput)`
- `System.Void Run()`
- `System.Void TrackDestination(Zio.UPath outputFile, Zio.UPath sourceFile)`

#### Properties

- `Lunet.Core.ContentLayoutTypes LayoutTypes { get; }`
- `Lunet.Core.PageFinderProcessor Finder { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.IContentProcessor> AfterRunningProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.IContentProcessor> ContentProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISiteProcessor> AfterLoadingProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISiteProcessor> AfterProcessingProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISiteProcessor> BeforeInitializingProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISiteProcessor> BeforeLoadingProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISiteProcessor> BeforeProcessingProcessors { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.TryProcessPreContentDelegate> BeforeLoadingContentProcessors { get; }`
### `Lunet.Core.ContentProcessingStage`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Core.ContentProcessingStage Processing`
- `const static Lunet.Core.ContentProcessingStage Running`
### `Lunet.Core.ContentProcessor<TPlugin>`

- Kind: `abstract class`
- Base: `Lunet.Core.ProcessorBase<TPlugin>`
- Interfaces: `Lunet.Core.IContentProcessor`, `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Methods

- `Lunet.Core.ContentResult abstract TryProcessContent(Lunet.Core.ContentObject file, Lunet.Core.ContentProcessingStage stage)`
### `Lunet.Core.ContentResult`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Core.ContentResult Break`
- `const static Lunet.Core.ContentResult Continue`
- `const static Lunet.Core.ContentResult None`
### `Lunet.Core.ContentType`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IEquatable<Lunet.Core.ContentType>`

#### Constructors

- `ContentType(System.String name)`

#### Methods

- `System.Boolean IsHtmlLike()`
- `System.Boolean static op_Equality(Lunet.Core.ContentType left, Lunet.Core.ContentType right)`
- `System.Boolean static op_Inequality(Lunet.Core.ContentType left, Lunet.Core.ContentType right)`
- `System.Boolean virtual Equals(Lunet.Core.ContentType other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`

#### Properties

- `System.String Name { get; }`

#### Fields

- `readonly static Lunet.Core.ContentType Css`
- `readonly static Lunet.Core.ContentType Html`
- `readonly static Lunet.Core.ContentType Jpeg`
- `readonly static Lunet.Core.ContentType Js`
- `readonly static Lunet.Core.ContentType Markdown`
- `readonly static Lunet.Core.ContentType Txt`
- `readonly static Lunet.Core.ContentType Xml`
- `static Lunet.Core.ContentType Empty`
### `Lunet.Core.ContentTypeManager`

- Kind: `class`

#### Constructors

- `ContentTypeManager()`

#### Methods

- `Lunet.Core.ContentType GetContentType(System.String extension)`
- `System.Boolean IsHtmlContentType(Lunet.Core.ContentType contentType)`
- `System.Collections.Generic.HashSet<System.String> GetExtensionsByContentType(Lunet.Core.ContentType type)`
- `System.Void AddContentType(System.String extension, Lunet.Core.ContentType contentType)`
- `System.Void RegisterHtmlContentType(Lunet.Core.ContentType contentType)`
### `Lunet.Core.DefaultSiteOptions`

- Kind: `class`
- Base: `Lunet.Core.SiteOptions`

#### Constructors

- `DefaultSiteOptions(System.String rootDirectory = optional)`

#### Properties

- `Zio.IFileSystem BaseFileSystem { get; }`
- `Zio.IFileSystem OutputFileSystem { get; }`
- `Zio.IFileSystem TempFileSystem { get; }`

#### Fields

- `const static System.String DefaultOutputFolder`
- `const static System.String DefaultTempFolder`
### `Lunet.Core.DynamicCollection<T, TInstance>`

- Kind: `abstract class`
- Base: `Scriban.Runtime.ScriptArray<T>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<T>`, `System.Collections.Generic.IEnumerable<T>`, `System.Collections.Generic.IList<T>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Methods

- `System.Collections.Generic.IEnumerable<TInstance> virtual GroupBy(System.String key)`
- `System.Void SetValue(System.String name, System.Object value, System.Boolean isReadOnly = optional)`
- `TInstance Reverse()`
- `TItem GetSafeValue<TItem>(System.String name)`
### `Lunet.Core.DynamicContentObject`

- Kind: `class`
- Base: `Lunet.Core.ContentObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DynamicContentObject(Lunet.Core.SiteObject site, System.String url, System.String section = optional, System.Nullable<Zio.UPath> path = optional)`
### `Lunet.Core.DynamicObject`

- Kind: `class`
- Base: `Scriban.Runtime.ScriptObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DynamicObject()`
- `DynamicObject(System.Collections.Generic.IEqualityComparer<System.String> keyComparer)`

#### Methods

- `System.String virtual ToString(System.String format, System.IFormatProvider formatProvider)`
- `System.Void SetValue(System.String name, System.Object value)`
- `T GetSafeValue<T>(System.String name)`
### `Lunet.Core.DynamicObjectExtensions`

- Kind: `static class`

#### Methods

- `System.Void static CopyToWithReadOnly(Scriban.Runtime.ScriptObject from, Scriban.Runtime.ScriptObject to)`
- `T static GetSafeValue<T>(Scriban.Runtime.IScriptObject obj, System.String name)`
- `T static GetSafeValueFromPageOrSite<T>(Lunet.Core.TemplateObject obj, System.String name, T defaultValue = optional)`
### `Lunet.Core.DynamicObject<T>`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `DynamicObject(T parent)`
- `DynamicObject(T parent, System.Collections.Generic.IEqualityComparer<System.String> keyComparer)`

#### Properties

- `T Parent { get; }`
### `Lunet.Core.ExtraContent`

- Kind: `class`

#### Constructors

- `ExtraContent()`

#### Properties

- `System.Boolean IsExternal { get; set; }`
- `System.String DefinitionUid { get; set; }`
- `System.String FullName { get; set; }`
- `System.String Name { get; set; }`
- `System.String Uid { get; set; }`
### `Lunet.Core.FileContentDependency`

- Kind: `class`
- Base: `Lunet.Core.ContentDependency`

#### Constructors

- `FileContentDependency(Zio.FileEntry file)`

#### Properties

- `Zio.FileEntry File { get; }`
### `Lunet.Core.FileContentObject`

- Kind: `class`
- Base: `Lunet.Core.ContentObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `FileContentObject(Lunet.Core.SiteObject site, ref Zio.FileSystemItem sourceFileInfo, Lunet.Scripts.ScriptInstance scriptInstance = optional, System.Nullable<Zio.UPath> path = optional, Scriban.Runtime.ScriptObject preContent = optional, Lunet.Core.ContentObjectType objectType = optional)`
### `Lunet.Core.FileVariables`

- Kind: `class`

#### Fields

- `const static System.String Discard`
- `const static System.String Extension`
- `const static System.String Length`
- `const static System.String ModifiedTime`
- `const static System.String Path`
### `Lunet.Core.GlobCollection`

- Kind: `class`
- Base: `Scriban.Runtime.ScriptArray<DotNet.Globbing.Glob>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<DotNet.Globbing.Glob>`, `System.Collections.Generic.IEnumerable<DotNet.Globbing.Glob>`, `System.Collections.Generic.IList<DotNet.Globbing.Glob>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `GlobCollection()`

#### Methods

- `System.Boolean IsMatch(Zio.UPath path)`
- `System.Void Add(System.String glob)`
### `Lunet.Core.GlobalVariables`

- Kind: `static class`

#### Fields

- `const static System.String BundleFunction`
### `Lunet.Core.HtmlBody`

- Kind: `class`
- Base: `Lunet.Core.HtmlElement`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `HtmlBody(Scriban.Runtime.ScriptObject parent)`

#### Properties

- `Lunet.Core.ScriptCollection Includes { get; }`
### `Lunet.Core.HtmlElement`

- Kind: `abstract class`
- Base: `Lunet.Core.DynamicObject<Scriban.Runtime.ScriptObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`
### `Lunet.Core.HtmlHead`

- Kind: `class`
- Base: `Lunet.Core.HtmlElement`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `HtmlHead(Scriban.Runtime.ScriptObject parent)`

#### Properties

- `Lunet.Core.ScriptCollection Includes { get; }`
- `Lunet.Core.ScriptCollection Metas { get; }`
- `System.Object Title { get; set; }`
### `Lunet.Core.HtmlPage`

- Kind: `class`
- Base: `Lunet.Core.HtmlElement`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `HtmlPage(Scriban.Runtime.ScriptObject parent)`

#### Properties

- `Lunet.Core.HtmlBody Body { get; }`
- `Lunet.Core.HtmlHead Head { get; }`
### `Lunet.Core.IContentProcessor`

- Kind: `interface`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`

#### Methods

- `Lunet.Core.ContentResult abstract TryProcessContent(Lunet.Core.ContentObject file, Lunet.Core.ContentProcessingStage stage)`
### `Lunet.Core.IFrontMatter`

- Kind: `interface`

#### Methods

- `System.Void abstract Evaluate(Scriban.TemplateContext context)`
### `Lunet.Core.IFrontMatterParser`

- Kind: `interface`

#### Methods

- `Lunet.Core.IFrontMatter abstract TryParse(System.String text, System.String sourceFilePath, out Scriban.Parsing.TextPosition position)`
- `System.Boolean abstract CanHandle(System.ReadOnlySpan<System.Byte> header)`
- `System.Boolean abstract CanHandle(System.ReadOnlySpan<System.Char> header)`
### `Lunet.Core.IProfiler`

- Kind: `interface`

#### Methods

- `System.Void abstract BeginEvent(System.String name, System.String data, Lunet.Core.ProfilerColor color)`
- `System.Void abstract EndEvent()`
### `Lunet.Core.ISiteCommandRunner`

- Kind: `interface`

#### Methods

- `System.Threading.Tasks.Task<Lunet.Core.RunnerResult> abstract RunAsync(Lunet.Core.SiteRunner runner, System.Threading.CancellationToken cancellationToken)`
### `Lunet.Core.ISiteLoggerProvider`

- Kind: `interface`

#### Properties

- `Lunet.Core.SiteLogger Log { get; }`
- `Lunet.Core.SiteLoggerFactory LoggerFactory { get; }`
- `System.Boolean ShowStacktraceOnError { get; set; }`
- `System.Int32 LogEventId { get; set; }`
### `Lunet.Core.ISitePlugin`

- Kind: `interface`
- Interfaces: `Lunet.Core.ISitePluginCore`
### `Lunet.Core.ISitePluginCore`

- Kind: `interface`

#### Properties

- `Lunet.Core.SiteObject Site { get; }`
- `System.String Name { get; }`
### `Lunet.Core.ISiteProcessor`

- Kind: `interface`
- Interfaces: `Lunet.Core.ISitePluginCore`

#### Methods

- `System.Void abstract Process(Lunet.Core.ProcessingStage stage)`
### `Lunet.Core.ISiteService`

- Kind: `interface`
- Interfaces: `System.IDisposable`
### `Lunet.Core.LunetException`

- Kind: `class`
- Base: `System.Exception`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `LunetException(System.String message)`
- `LunetException(System.String message, System.Exception innerException)`
### `Lunet.Core.LunetObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Core.SiteObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `LunetObject(Lunet.Core.SiteObject site)`

#### Properties

- `System.String Version { get; }`
### `Lunet.Core.PageCollection`

- Kind: `class`
- Base: `Lunet.Core.DynamicCollection<Lunet.Core.ContentObject, Lunet.Core.PageCollection>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<Lunet.Core.ContentObject>`, `System.Collections.Generic.IEnumerable<Lunet.Core.ContentObject>`, `System.Collections.Generic.IList<Lunet.Core.ContentObject>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `PageCollection()`
- `PageCollection(System.Collections.Generic.IEnumerable<Lunet.Core.ContentObject> values)`

#### Methods

- `Lunet.Core.PageCollection OrderByDate()`
- `Lunet.Core.PageCollection OrderByLength()`
- `Lunet.Core.PageCollection OrderByTitle()`
- `Lunet.Core.PageCollection OrderByWeight()`
- `System.Void Sort()`
### `Lunet.Core.PageContentDependency`

- Kind: `class`
- Base: `Lunet.Core.ContentDependency`

#### Constructors

- `PageContentDependency(Lunet.Core.ContentObject page)`

#### Properties

- `Lunet.Core.ContentObject Page { get; }`
### `Lunet.Core.PageFinderProcessor`

- Kind: `class`
- Base: `Lunet.Core.ProcessorBase<Lunet.Core.ContentPlugin>`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `PageFinderProcessor(Lunet.Core.ContentPlugin plugin)`

#### Methods

- `System.Boolean TryFindByPath(System.String path, out Lunet.Core.ContentObject content)`
- `System.Boolean TryFindByUid(System.String uid, out Lunet.Core.ContentObject content)`
- `System.Boolean TryGetExternalUid(System.String uid, out System.String name, out System.String fullname, out System.String url)`
- `System.Boolean TryGetTitleByUid(System.String uid, out System.String title)`
- `System.String UrlRef(Lunet.Core.ContentObject fromPage, System.String url)`
- `System.String UrlRelRef(Lunet.Core.ContentObject fromPage, System.String url)`
- `System.Void RegisterExtraContent(Lunet.Core.ExtraContent extraContent)`
- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`
### `Lunet.Core.PageVariables`

- Kind: `class`
- Base: `Lunet.Core.FileVariables`

#### Fields

- `const static System.String Content`
- `const static System.String ContentType`
- `const static System.String Date`
- `const static System.String Layout`
- `const static System.String LayoutContentType`
- `const static System.String LayoutType`
- `const static System.String Page`
- `const static System.String PathInSection`
- `const static System.String Section`
- `const static System.String Site`
- `const static System.String Slug`
- `const static System.String Summary`
- `const static System.String SummaryKeepFormatting`
- `const static System.String SummaryWordCount`
- `const static System.String Title`
- `const static System.String Uid`
- `const static System.String Url`
- `const static System.String UrlExplicit`
- `const static System.String UrlWithoutBasePath`
- `const static System.String Weight`
- `const static System.String XRefFullName`
- `const static System.String XRefName`
### `Lunet.Core.PathCollection`

- Kind: `class`
- Base: `Lunet.Core.ScriptCollection`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<System.Object>`, `System.Collections.Generic.IEnumerable<System.Object>`, `System.Collections.Generic.IList<System.Object>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `PathCollection()`
### `Lunet.Core.ProcessingStage`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Core.ProcessingStage AfterLoadingContent`
- `const static Lunet.Core.ProcessingStage AfterProcessingContent`
- `const static Lunet.Core.ProcessingStage BeforeInitializing`
- `const static Lunet.Core.ProcessingStage BeforeLoadingContent`
- `const static Lunet.Core.ProcessingStage BeforeProcessingContent`
### `Lunet.Core.ProcessorBase<TPlugin>`

- Kind: `abstract class`
- Base: `Lunet.Core.SitePluginCore`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Lunet.Core.ISiteProcessor`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Methods

- `System.Void virtual Process(Lunet.Core.ProcessingStage stage)`

#### Properties

- `TPlugin Plugin { get; }`
### `Lunet.Core.ProfilerColor`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IEquatable<Lunet.Core.ProfilerColor>`

#### Constructors

- `ProfilerColor(System.Byte r, System.Byte g, System.Byte b)`
- `ProfilerColor(System.UInt32 value)`

#### Methods

- `System.Boolean static op_Equality(Lunet.Core.ProfilerColor left, Lunet.Core.ProfilerColor right)`
- `System.Boolean static op_Inequality(Lunet.Core.ProfilerColor left, Lunet.Core.ProfilerColor right)`
- `System.Boolean virtual Equals(Lunet.Core.ProfilerColor other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`

#### Fields

- `readonly System.UInt32 Value`
- `readonly static Lunet.Core.ProfilerColor Default`
### `Lunet.Core.RunnerResult`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Core.RunnerResult Continue`
- `const static Lunet.Core.RunnerResult Exit`
- `const static Lunet.Core.RunnerResult ExitWithError`
### `Lunet.Core.ScriptCollection`

- Kind: `class`
- Base: `Scriban.Runtime.ScriptArray`
- Interfaces: `Scriban.Runtime.IScriptObject`, `Scriban.Runtime.IScriptTransformable`, `Scriban.Syntax.IScriptCustomBinaryOperation`, `System.Collections.Generic.ICollection<System.Object>`, `System.Collections.Generic.IEnumerable<System.Object>`, `System.Collections.Generic.IList<System.Object>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `ScriptCollection()`
### `Lunet.Core.SiteApplication`

- Kind: `class`

#### Constructors

- `SiteApplication(Lunet.Core.SiteConfiguration config = optional)`

#### Methods

- `Lunet.Core.SiteApplication Add(Lunet.Core.SiteModule module)`
- `System.Void Execute(params System.String[] args)`
- `TCommandRunner CreateCommandRunner<TCommandRunner>()`
- `XenoAtom.CommandLine.Command AddCommand(System.String name, System.String description, System.Action<XenoAtom.CommandLine.Command> configure)`

#### Properties

- `Lunet.Core.SiteConfiguration Config { get; }`
- `XenoAtom.CommandLine.Command CleanCommand { get; }`
- `XenoAtom.CommandLine.Command ConfigCommand { get; }`
- `XenoAtom.CommandLine.Command InitCommand { get; }`
- `XenoAtom.CommandLine.Command NewCommand { get; }`
- `XenoAtom.CommandLine.Command RunCommand { get; }`
### `Lunet.Core.SiteConfiguration`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteLoggerProvider`

#### Constructors

- `SiteConfiguration(Lunet.Core.SiteLoggerFactory loggerFactory = optional, Lunet.Core.SiteFileSystems fileSystems = optional)`

#### Methods

- `Lunet.Core.SiteConfiguration RegisterPlugin(System.Type pluginType)`
- `Lunet.Core.SiteConfiguration RegisterPlugin<TPlugin>()`
- `System.Collections.Generic.List<System.Type> PluginTypes()`

#### Properties

- `Lunet.Core.IProfiler Profiler { get; set; }`
- `Lunet.Core.SiteFileSystems FileSystems { get; }`
- `Lunet.Core.SiteLogger Log { get; }`
- `Lunet.Core.SiteLoggerFactory LoggerFactory { get; }`
- `System.Boolean ShouldRunGarbageCollectorOnReload { get; set; }`
- `System.Boolean ShowStacktraceOnError { get; set; }`
- `System.Boolean SingleThreaded { get; set; }`
- `System.Collections.Concurrent.ConcurrentDictionary<System.Object, System.Object> SharedCache { get; }`
- `System.Collections.Generic.List<Lunet.Core.ISiteCommandRunner> CommandRunners { get; }`
- `System.Collections.Generic.List<System.String> Defines { get; }`
- `System.Int32 LogEventId { get; set; }`
### `Lunet.Core.SiteFileSystems`

- Kind: `class`

#### Constructors

- `SiteFileSystems()`

#### Methods

- `System.Void AddContentFileSystem(Zio.IFileSystem fileSystem)`
- `System.Void ClearContentFileSystems()`
- `System.Void virtual Initialize(System.String inputDirectory = optional, System.String outputDirectory = optional)`

#### Properties

- `Zio.FileEntry ConfigFile { get; }`
- `Zio.FileSystems.FileSystem OutputFileSystem { get; set; }`
- `Zio.IFileSystem CacheMetaFileSystem { get; }`
- `Zio.IFileSystem CacheSiteFileSystem { get; }`
- `Zio.IFileSystem FileSystem { get; }`
- `Zio.IFileSystem InputFileSystem { get; set; }`
- `Zio.IFileSystem MetaFileSystem { get; }`
- `Zio.IFileSystem SharedFileSystem { get; }`
- `Zio.IFileSystem SharedMetaFileSystem { get; }`

#### Fields

- `const static System.String BuildFolderName`
- `const static System.String CacheSiteFolderName`
- `const static System.String DefaultConfigFileName`
- `const static System.String DefaultOutputFolderName`
- `const static System.String LunetFolderName`
- `const static System.String ModulesFolderName`
- `const static System.String SharedFolderName`
- `readonly static System.String LunetFolderWithSlash`
- `readonly static Zio.UPath BuildFolder`
- `readonly static Zio.UPath LunetFolder`
- `readonly static Zio.UPath SiteFolder`
- `readonly static Zio.UPath TempSiteFolder`
### `Lunet.Core.SiteLogger`

- Kind: `class`

#### Methods

- `System.Boolean IsEnabled(XenoAtom.Logging.LogLevel level)`
- `System.Void Log(XenoAtom.Logging.LogLevel level, XenoAtom.Logging.LogEventId eventId, System.String message)`

#### Properties

- `System.String Category { get; }`
### `Lunet.Core.SiteLoggerFactory`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `SiteLoggerFactory(System.Boolean defaultConsole = optional)`

#### Methods

- `Lunet.Core.SiteLogger CreateLogger(System.String categoryName)`
- `System.Void virtual Dispose()`

#### Properties

- `System.Boolean HasErrors { get; }`
- `System.Func<System.String, XenoAtom.Logging.LogLevel, System.Boolean> LogFilter { get; set; }`
### `Lunet.Core.SiteModule`

- Kind: `abstract class`
### `Lunet.Core.SiteModule<TPlugin>`

- Kind: `abstract class`
- Base: `Lunet.Core.SiteModule`
### `Lunet.Core.SiteObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Lunet.Core.ISiteLoggerProvider`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `SiteObject(Lunet.Core.SiteConfiguration configuration)`

#### Methods

- `Lunet.Core.SiteObject Clone()`
- `System.Boolean Initialize()`
- `System.Boolean IsHandlingPath(Zio.UPath path)`
- `System.Int32 Clean()`
- `System.Int32 Create(System.Boolean force)`
- `System.String GetSafeDefaultPageExtension()`
- `System.Void AddContentFileSystem(Zio.IFileSystem contentFileSystem)`
- `System.Void AddDefine(System.String defineStatement)`
- `System.Void Build()`

#### Properties

- `Lunet.Core.BuiltinsObject Builtins { get; }`
- `Lunet.Core.ContentPlugin Content { get; }`
- `Lunet.Core.ContentTypeManager ContentTypes { get; }`
- `Lunet.Core.GlobCollection Excludes { get; }`
- `Lunet.Core.GlobCollection ForceExcludes { get; }`
- `Lunet.Core.GlobCollection Includes { get; }`
- `Lunet.Core.HtmlPage Html { get; }`
- `Lunet.Core.PageCollection DynamicPages { get; }`
- `Lunet.Core.PageCollection Pages { get; }`
- `Lunet.Core.PageCollection StaticFiles { get; }`
- `Lunet.Core.SiteConfiguration Config { get; }`
- `Lunet.Core.SiteLogger Log { get; }`
- `Lunet.Core.SiteLoggerFactory LoggerFactory { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.ISitePlugin> Plugins { get; }`
- `Lunet.Scripts.ScriptingPlugin Scripts { get; }`
- `Lunet.Statistics.SiteStatistics Statistics { get; }`
- `System.Boolean BaseUrlForce { get; set; }`
- `System.Boolean HasErrors { get; set; }`
- `System.Boolean ReadmeAsIndex { get; set; }`
- `System.Boolean ShowStacktraceOnError { get; set; }`
- `System.Boolean UrlAsFile { get; set; }`
- `System.Int32 LogEventId { get; set; }`
- `System.String BasePath { get; set; }`
- `System.String BaseUrl { get; set; }`
- `System.String DefaultPageExtension { get; set; }`
- `System.String Environment { get; set; }`
- `System.String ErrorRedirect { get; set; }`
- `System.String Layout { get; set; }`
- `Zio.FileEntry ConfigFile { get; }`
- `Zio.IFileSystem CacheMetaFileSystem { get; }`
- `Zio.IFileSystem CacheSiteFileSystem { get; }`
- `Zio.IFileSystem FileSystem { get; }`
- `Zio.IFileSystem MetaFileSystem { get; }`
- `Zio.IFileSystem OutputFileSystem { get; }`
- `Zio.IFileSystem SharedFileSystem { get; }`
- `Zio.IFileSystem SharedMetaFileSystem { get; }`
- `Zio.IFileSystem SiteFileSystem { get; }`

#### Fields

- `const static System.String DefaultPageExtensionValue`
### `Lunet.Core.SiteObjectExtensions`

- Kind: `static class`

#### Methods

- `System.Boolean static CanDebug(Lunet.Core.ISiteLoggerProvider site)`
- `System.Boolean static CanInfo(Lunet.Core.ISiteLoggerProvider site)`
- `System.Boolean static CanTrace(Lunet.Core.ISiteLoggerProvider site)`
- `System.Void static BeginEvent(Lunet.Core.SiteObject site, System.String name)`
- `System.Void static BeginEvent(Lunet.Core.SiteObject site, System.String name, Lunet.Core.ProfilerColor color)`
- `System.Void static Debug(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Debug(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
- `System.Void static EndEvent(Lunet.Core.SiteObject site)`
- `System.Void static Error(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Error(Lunet.Core.ISiteLoggerProvider site, System.Exception exception, System.String message, params System.Object[] args)`
- `System.Void static Error(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
- `System.Void static Fatal(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Fatal(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
- `System.Void static Info(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Info(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
- `System.Void static InsertBefore<T>(Lunet.Helpers.OrderedList<T> list, System.String name, T value)`
- `System.Void static Trace(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Trace(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
- `System.Void static Warning(Lunet.Core.ISiteLoggerProvider site, Scriban.Parsing.SourceSpan span, System.String message, params System.Object[] args)`
- `System.Void static Warning(Lunet.Core.ISiteLoggerProvider site, System.String message, params System.Object[] args)`
### `Lunet.Core.SiteOptions`

- Kind: `abstract class`

#### Properties

- `Zio.IFileSystem BaseFileSystem { get; }`
- `Zio.IFileSystem OutputFileSystem { get; }`
- `Zio.IFileSystem TempFileSystem { get; }`
### `Lunet.Core.SitePlugin`

- Kind: `abstract class`
- Base: `Lunet.Core.SitePluginCore`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`
### `Lunet.Core.SitePluginCore`

- Kind: `abstract class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Properties

- `Lunet.Core.SiteObject Site { get; }`
- `System.String Name { get; }`
### `Lunet.Core.SiteRunner`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `SiteRunner(Lunet.Core.SiteConfiguration config)`

#### Methods

- `System.Threading.Tasks.Task<System.Int32> RunAsync(System.Threading.CancellationTokenSource cancellationTokenSource = optional)`
- `System.Void RegisterService(Lunet.Core.ISiteService service)`
- `System.Void virtual Dispose()`
- `TService GetService<TService>()`

#### Properties

- `Lunet.Core.SiteConfiguration Config { get; }`
- `Lunet.Core.SiteObject CurrentSite { get; }`
- `System.Collections.Generic.IReadOnlyCollection<Lunet.Core.ISiteService> Services { get; }`
- `System.Collections.Generic.List<Lunet.Core.ISiteCommandRunner> CommandRunners { get; }`
### `Lunet.Core.SiteVariables`

- Kind: `static class`

#### Fields

- `const static System.String BasePath`
- `const static System.String BaseUrl`
- `const static System.String BaseUrlForce`
- `const static System.String Builtins`
- `const static System.String Bundles`
- `const static System.String DefaultPageExtension`
- `const static System.String Environment`
- `const static System.String ErrorRedirect`
- `const static System.String Excludes`
- `const static System.String ExtendFunction`
- `const static System.String Extends`
- `const static System.String ForceExcludes`
- `const static System.String Html`
- `const static System.String Includes`
- `const static System.String Layout`
- `const static System.String LayoutTypes`
- `const static System.String Pages`
- `const static System.String Plugins`
- `const static System.String ReadmeAsIndex`
- `const static System.String ResourceFunction`
- `const static System.String Resources`
- `const static System.String UrlAsFile`
### `Lunet.Core.TemplateObject`

- Kind: `abstract class`
- Base: `Lunet.Core.DynamicObject`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Properties

- `Lunet.Core.ContentObjectType ObjectType { get; }`
- `Lunet.Core.IFrontMatter FrontMatter { get; set; }`
- `Lunet.Core.SiteObject Site { get; }`
- `Scriban.Runtime.ScriptObject ScriptObjectLocal { get; set; }`
- `Scriban.Syntax.ScriptPage Script { get; }`
- `System.Boolean HasFrontMatter { get; }`
- `System.Collections.Generic.List<Lunet.Core.ContentDependency> Dependencies { get; }`
- `System.DateTimeOffset ModifiedTime { get; }`
- `System.Int64 Length { get; }`
- `System.String Extension { get; }`
- `Zio.UPath Path { get; }`

#### Fields

- `readonly Zio.FileSystemItem SourceFile`
### `Lunet.Core.TryProcessPreContentDelegate`

- Kind: `class`
- Base: `System.MulticastDelegate`
- Interfaces: `System.ICloneable`, `System.Runtime.Serialization.ISerializable`

#### Constructors

- `TryProcessPreContentDelegate(System.Object object, System.IntPtr method)`

#### Methods

- `System.IAsyncResult virtual BeginInvoke(Zio.UPath path, ref Scriban.Runtime.ScriptObject preContent, System.AsyncCallback callback, System.Object object)`
- `System.Void virtual EndInvoke(ref Scriban.Runtime.ScriptObject preContent, System.IAsyncResult result)`
- `System.Void virtual Invoke(Zio.UPath path, ref Scriban.Runtime.ScriptObject preContent)`
### `Lunet.Core.UidHelper`

- Kind: `static class`

#### Methods

- `System.String static Handleize(System.String uid)`
### `Lunet.Helpers.ExceptionUtil`

- Kind: `static class`

#### Methods

- `System.String static GetReason(System.Exception exception)`
### `Lunet.Helpers.HashUtil`

- Kind: `static class`

#### Methods

- `System.String static HashStringHex(System.String content)`
- `System.UInt128 static HashString(System.String content)`
### `Lunet.Helpers.OrderedList<T>`

- Kind: `class`
- Base: `System.Collections.ObjectModel.Collection<T>`
- Interfaces: `System.Collections.Generic.ICollection<T>`, `System.Collections.Generic.IEnumerable<T>`, `System.Collections.Generic.IList<T>`, `System.Collections.Generic.IReadOnlyCollection<T>`, `System.Collections.Generic.IReadOnlyList<T>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `OrderedList()`
- `OrderedList(System.Collections.Generic.IEnumerable<T> list)`

#### Methods

- `System.Boolean Contains<TElement>()`
- `System.Boolean InsertAfter<TElement>(T element)`
- `System.Boolean InsertBefore<TElement>(T element)`
- `System.Boolean ReplacyBy<TElement>(T element)`
- `System.Void AddIfNotAlready<TElement>()`
- `System.Void AddIfNotAlready<TElement>(TElement telement)`
- `System.Void AddRange<TList>(TList collection)`
- `TElement Find<TElement>()`
- `TElement FindExact<TElement>()`
### `Lunet.Helpers.PathUtil`

- Kind: `static class`

#### Methods

- `System.String static Normalize(System.String filePath)`
- `System.String static NormalizeExtension(System.String extension)`
- `System.String static NormalizeRelativePath(System.String filePath, System.Boolean isDirectory)`
- `System.String static NormalizeUrl(System.String filePath, System.Boolean isDirectory)`
- `T static Normalize<T>(T fileInfo)`
- `Zio.SearchPattern static SearchPattern(Zio.UPath path)`
### `Lunet.Helpers.TarUtil`

- Kind: `static class`

#### Methods

- `System.Void static UntarTo(System.IO.Stream stream, Zio.DirectoryEntry outputDirectory, System.String filterPath = optional)`
### `Lunet.Helpers.ZipUtil`

- Kind: `static class`

#### Methods

- `System.Void static ExtractToDirectory(System.IO.Compression.ZipArchive source, Zio.DirectoryEntry outputDirectory, System.String filterPath = optional)`
- `System.Void static ExtractToFile(System.IO.Compression.ZipArchiveEntry source, Zio.FileEntry destinationFile)`
- `System.Void static ExtractToFile(System.IO.Compression.ZipArchiveEntry source, Zio.FileEntry destinationFile, System.Boolean overwrite)`
### `Lunet.Scripts.LunetTemplateContext`

- Kind: `class`
- Base: `Scriban.TemplateContext`
- Interfaces: `System.IFormatProvider`

#### Constructors

- `LunetTemplateContext(Scriban.Runtime.ScriptObject builtin)`

#### Methods

- `System.Void virtual Reset()`

#### Properties

- `Lunet.Core.ContentObject Page { get; set; }`
### `Lunet.Scripts.ScriptFlags`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.Scripts.ScriptFlags AllowSiteFunctions`
- `const static Lunet.Scripts.ScriptFlags Expect`
- `const static Lunet.Scripts.ScriptFlags None`
### `Lunet.Scripts.ScriptInstance`

- Kind: `class`

#### Constructors

- `ScriptInstance(System.Boolean hasErrors, System.String sourceFilePath, Lunet.Core.IFrontMatter frontMatter, Scriban.Syntax.ScriptPage template)`

#### Fields

- `readonly Lunet.Core.IFrontMatter FrontMatter`
- `readonly Scriban.Syntax.ScriptPage Template`
- `readonly System.Boolean HasErrors`
- `readonly System.String SourceFilePath`
### `Lunet.Scripts.ScriptingPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Methods

- `Lunet.Scripts.ScriptInstance ParseScript(System.String scriptContent, Zio.UPath scriptPath, Scriban.Parsing.ScriptMode parsingMode)`
- `Scriban.Syntax.ScriptFunction CompileAnonymous(System.String expression)`
- `System.Boolean TryEvaluateExpression(Lunet.Core.ContentObject page, Scriban.Syntax.ScriptExpression expression, out System.String result)`
- `System.Boolean TryEvaluatePage(Lunet.Core.ContentObject page, Scriban.Syntax.ScriptPage script, Zio.UPath scriptPath, params Scriban.Runtime.ScriptObject[] contextObjects)`
- `System.Boolean TryImportInclude(Zio.UPath includePath, Scriban.Runtime.ScriptObject toObject)`
- `System.Boolean TryImportScript(System.String scriptText, Zio.UPath scriptPath, Scriban.Runtime.ScriptObject scriptObject, Lunet.Scripts.ScriptFlags flags, out System.Object result, Scriban.Parsing.ScriptMode scriptMode = optional)`
- `System.Boolean TryImportScriptFromFile(Zio.FileEntry scriptPath, Scriban.Runtime.ScriptObject scriptObject, Lunet.Scripts.ScriptFlags flags, out System.Object result, Scriban.Parsing.ScriptMode scriptMode = optional)`
- `System.Boolean TryImportScriptStatement(System.String scriptStatement, Scriban.Runtime.ScriptObject scriptObject, Lunet.Scripts.ScriptFlags flags, out System.Object result)`
- `System.Boolean TryRunFrontMatter(Lunet.Core.IFrontMatter frontMatter, Lunet.Core.TemplateObject obj, Scriban.Runtime.ScriptObject newGlobal = optional)`

#### Properties

- `Lunet.Helpers.OrderedList<Lunet.Core.IFrontMatterParser> FrontMatterParsers { get; }`
- `Scriban.Runtime.ScriptObject ScribanBuiltins { get; }`
### `Lunet.Statistics.ContentStat`

- Kind: `class`

#### Constructors

- `ContentStat(Lunet.Core.ContentObject contentObject)`

#### Properties

- `Lunet.Core.ContentObject ContentObject { get; }`
- `System.Boolean Static { get; set; }`
- `System.Int64 OutputBytes { get; set; }`
- `System.TimeSpan LoadingParsingTime { get; set; }`
- `System.TimeSpan LoadingTime { get; set; }`
- `System.TimeSpan OutputTime { get; set; }`
- `System.TimeSpan RunningTime { get; set; }`
- `System.TimeSpan SummaryTime { get; set; }`
### `Lunet.Statistics.PluginStat`

- Kind: `class`

#### Constructors

- `PluginStat(Lunet.Core.ISitePluginCore plugin)`

#### Properties

- `Lunet.Core.ISitePluginCore Plugin { get; }`
- `System.Int32 Order { get; set; }`
- `System.Int32 PageCount { get; set; }`
- `System.TimeSpan BeginProcessTime { get; set; }`
- `System.TimeSpan ContentProcessTime { get; set; }`
- `System.TimeSpan EndProcessTime { get; set; }`
- `System.TimeSpan InitializeTime { get; set; }`
### `Lunet.Statistics.SiteStatistics`

- Kind: `class`

#### Constructors

- `SiteStatistics()`

#### Methods

- `Lunet.Statistics.ContentStat GetContentStat(Lunet.Core.ContentObject page)`
- `Lunet.Statistics.PluginStat GetPluginStat(Lunet.Core.ISitePluginCore plugin)`
- `System.String GetSummary()`
- `System.Void Dump(System.Action<System.String> log)`
- `System.Void Reset()`

#### Properties

- `System.Collections.Generic.Dictionary<Lunet.Core.ContentObject, Lunet.Statistics.ContentStat> Content { get; }`
- `System.Collections.Generic.Dictionary<Lunet.Core.ISitePluginCore, Lunet.Statistics.PluginStat> Plugins { get; }`
- `System.TimeSpan TotalTime { get; set; }`
