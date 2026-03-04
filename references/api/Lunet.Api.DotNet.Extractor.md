# Lunet.Api.DotNet.Extractor Public API

Assembly path: `src/Lunet.Api.DotNet.Extractor/bin/Release/netstandard2.0/Lunet.Api.DotNet.Extractor.dll`

Exported types: **165**

## Types

### `Lunet.Api.DotNet.Extractor.AssemblyViewModel`

- Kind: `class`

#### Constructors

- `AssemblyViewModel()`

#### Properties

- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.PageViewModel> Items { get; set; }`
- `System.String Name { get; set; }`
### `Lunet.Api.DotNet.Extractor.ExtractorAnalyzer`

- Kind: `class`
- Base: `Microsoft.CodeAnalysis.Diagnostics.DiagnosticAnalyzer`

#### Constructors

- `ExtractorAnalyzer()`

#### Methods

- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem> TryParseExtraDoc(Microsoft.CodeAnalysis.Diagnostics.CompilationAnalysisContext context, Microsoft.CodeAnalysis.AdditionalText file)`
- `System.Void virtual Initialize(Microsoft.CodeAnalysis.Diagnostics.AnalysisContext context)`

#### Properties

- `System.Collections.Immutable.ImmutableArray<Microsoft.CodeAnalysis.DiagnosticDescriptor> SupportedDiagnostics { get; }`
### `Lunet.Api.DotNet.Extractor.ExtractorHelper`

- Kind: `static class`

#### Methods

- `System.Collections.Generic.List<System.String> static FindResults(System.String text)`
- `System.String static FormatResult(System.String path)`
- `System.String static SelectBestResult(System.Collections.Generic.IReadOnlyList<System.String> results, System.String projectPath, System.String projectName, System.String targetFramework)`

#### Fields

- `const static System.String ResultId`
### `Lunet.Api.DotNet.Extractor.JsonSerializer`

- Kind: `class`

#### Constructors

- `JsonSerializer(System.IO.TextWriter writer)`

#### Methods

- `System.Void Write(System.Object value)`

#### Properties

- `System.Boolean PrettyOutput { get; set; }`
### `Microsoft.DocAsCode.Common.AggregatedLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `AggregatedLogListener(Microsoft.DocAsCode.Common.AggregatedLogListener other)`
- `AggregatedLogListener(Microsoft.DocAsCode.Common.LogLevel threshold = optional)`

#### Methods

- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.AggregatedPerformanceScope`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `AggregatedPerformanceScope(System.Nullable<Microsoft.DocAsCode.Common.LogLevel> logLevel = optional)`

#### Methods

- `System.Void Log(System.TimeSpan elapsedTime)`
- `System.Void virtual Dispose()`
### `Microsoft.DocAsCode.Common.AmbientContext`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IDisposable`

#### Methods

- `Microsoft.DocAsCode.Common.AmbientContext CreateBranch()`
- `Microsoft.DocAsCode.Common.AmbientContext static GetOrCreateAmbientContext()`
- `Microsoft.DocAsCode.Common.AmbientContext static InitializeAmbientContext(System.String id)`
- `System.String GenerateNextCorrelationId()`
- `System.Void virtual Dispose()`

#### Properties

- `System.Nullable<Microsoft.DocAsCode.Common.AmbientContext> CurrentContext { get; }`
- `System.String Id { get; }`
### `Microsoft.DocAsCode.Common.AsyncLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `AsyncLogListener()`
- `AsyncLogListener(Microsoft.DocAsCode.Common.CompositeLogListener compositeLogListener)`
- `AsyncLogListener(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Common.ILoggerListener> listeners)`

#### Methods

- `Microsoft.DocAsCode.Common.ILoggerListener FindListener(System.Predicate<Microsoft.DocAsCode.Common.ILoggerListener> predicate)`
- `System.Void AddListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void AddListeners(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Common.ILoggerListener> listeners)`
- `System.Void RemoveAllListeners()`
- `System.Void RemoveListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.CommandInfo`

- Kind: `class`

#### Constructors

- `CommandInfo()`

#### Properties

- `System.String Arguments { get; set; }`
- `System.String Name { get; set; }`
- `System.String WorkingDirectory { get; set; }`
### `Microsoft.DocAsCode.Common.CommandUtility`

- Kind: `static class`

#### Methods

- `System.Boolean static ExistCommand(System.String commandName, System.Action<System.String> processOutput = optional, System.Action<System.String> processError = optional)`
- `System.Int32 static RunCommand(Microsoft.DocAsCode.Common.CommandInfo commandInfo, System.IO.StreamWriter stdoutWriter = optional, System.IO.StreamWriter stderrWriter = optional, System.Int32 timeoutInMilliseconds = optional)`
### `Microsoft.DocAsCode.Common.CompositeDictionary`

- Kind: `class`
- Interfaces: `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.IEnumerable`

#### Constructors

- `CompositeDictionary()`

#### Methods

- `Microsoft.DocAsCode.Common.CompositeDictionary.Builder static CreateBuilder()`
- `System.Boolean virtual ContainsKey(System.String key)`
- `System.Boolean virtual Remove(System.String key)`
- `System.Boolean virtual TryGetValue(System.String key, out System.Object value)`
- `System.Collections.Generic.IEnumerator<System.Collections.Generic.KeyValuePair<System.String, System.Object>> virtual GetEnumerator()`
- `System.Void virtual Add(System.String key, System.Object value)`
- `System.Void virtual Clear()`

#### Properties

- `System.Boolean IsReadOnly { get; }`
- `System.Collections.Generic.ICollection<System.Object> Values { get; }`
- `System.Collections.Generic.ICollection<System.String> Keys { get; }`
- `System.Int32 Count { get; }`
- `System.Object Item[System.String key] { get; set; }`
### `Microsoft.DocAsCode.Common.CompositeDictionary.Builder`

- Kind: `class`

#### Methods

- `Microsoft.DocAsCode.Common.CompositeDictionary Create()`
- `Microsoft.DocAsCode.Common.CompositeDictionary.Builder Add<TValue>(System.String prefix, System.Collections.Generic.IDictionary<System.String, TValue> dict, System.Func<System.Object, TValue> valueConverter = optional)`
### `Microsoft.DocAsCode.Common.CompositeLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `CompositeLogListener()`
- `CompositeLogListener(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Common.ILoggerListener> listeners)`

#### Methods

- `Microsoft.DocAsCode.Common.ILoggerListener FindListener(System.Predicate<Microsoft.DocAsCode.Common.ILoggerListener> predicate)`
- `System.Void AddListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void AddListeners(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Common.ILoggerListener> listeners)`
- `System.Void RemoveAllListeners()`
- `System.Void RemoveListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`

#### Properties

- `System.Int32 Count { get; }`
### `Microsoft.DocAsCode.Common.ConsoleLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `ConsoleLogListener()`

#### Methods

- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.ConsoleUtility`

- Kind: `static class`

#### Methods

- `System.Void static Write(System.String message, System.ConsoleColor color)`
- `System.Void static WriteLine(System.String message, System.ConsoleColor color)`
### `Microsoft.DocAsCode.Common.CrossAppDomainListener`

- Kind: `class`
- Base: `System.MarshalByRefObject`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `CrossAppDomainListener()`

#### Methods

- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`

#### Properties

- `Microsoft.DocAsCode.Common.LogLevel LogLevelThreshold { get; set; }`
### `Microsoft.DocAsCode.Common.EntityMergers.MergeOption`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption Ignore`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption Merge`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption MergeKey`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption MergeNullOrDefault`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption Replace`
- `const static Microsoft.DocAsCode.Common.EntityMergers.MergeOption ReplaceNullOrDefault`
### `Microsoft.DocAsCode.Common.EntityMergers.MergeOptionAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `MergeOptionAttribute(Microsoft.DocAsCode.Common.EntityMergers.MergeOption option = optional)`

#### Properties

- `Microsoft.DocAsCode.Common.EntityMergers.MergeOption Option { get; }`
### `Microsoft.DocAsCode.Common.ErrorCodes`

- Kind: `static class`
### `Microsoft.DocAsCode.Common.ErrorCodes.Build`

- Kind: `static class`

#### Fields

- `const static System.String FatalError`
- `const static System.String FileNamesMaxLengthExceeded`
- `const static System.String InternalUidNotFound`
- `const static System.String InvalidHref`
- `const static System.String InvalidInputFile`
- `const static System.String InvalidMarkdown`
- `const static System.String InvalidPropertyFormat`
- `const static System.String InvalidRelativePath`
- `const static System.String InvalidYamlFile`
- `const static System.String TopicHrefNotset`
- `const static System.String UidFoundInMultipleArticles`
- `const static System.String UnsupportedTocHrefType`
- `const static System.String ViolateSchema`
### `Microsoft.DocAsCode.Common.ErrorCodes.Config`

- Kind: `static class`

#### Fields

- `const static System.String BuildConfigNotFound`
- `const static System.String MetadataConfigNotFound`
- `const static System.String PdfConfigNotFound`
### `Microsoft.DocAsCode.Common.ErrorCodes.Overwrite`

- Kind: `static class`

#### Fields

- `const static System.String InvalidOverwriteDocument`
- `const static System.String OverwriteDocumentMergeError`
### `Microsoft.DocAsCode.Common.ErrorCodes.Template`

- Kind: `static class`

#### Fields

- `const static System.String ApplyTemplatePreprocessorError`
- `const static System.String ApplyTemplateRendererError`
### `Microsoft.DocAsCode.Common.ErrorCodes.Toc`

- Kind: `static class`

#### Fields

- `const static System.String CircularTocInclusion`
- `const static System.String InvalidMarkdownToc`
- `const static System.String InvalidTocFile`
- `const static System.String InvalidTocLink`
### `Microsoft.DocAsCode.Common.FilePathComparer`

- Kind: `class`
- Interfaces: `System.Collections.Generic.IEqualityComparer<System.String>`

#### Constructors

- `FilePathComparer()`
- `FilePathComparer(System.Boolean ignoreToFullPath)`

#### Methods

- `System.Boolean virtual Equals(System.String x, System.String y)`
- `System.Int32 virtual GetHashCode(System.String obj)`

#### Fields

- `readonly static Microsoft.DocAsCode.Common.FilePathComparer OSPlatformSensitiveComparer`
- `readonly static Microsoft.DocAsCode.Common.FilePathComparer OSPlatformSensitiveRelativePathComparer`
- `readonly static System.StringComparer OSPlatformSensitiveStringComparer`
### `Microsoft.DocAsCode.Common.FilePathComparerWithEnvironmentVariable`

- Kind: `class`
- Interfaces: `System.Collections.Generic.IEqualityComparer<System.String>`

#### Constructors

- `FilePathComparerWithEnvironmentVariable(Microsoft.DocAsCode.Common.FilePathComparer inner)`

#### Methods

- `System.Boolean virtual Equals(System.String x, System.String y)`
- `System.Int32 virtual GetHashCode(System.String obj)`

#### Fields

- `readonly static Microsoft.DocAsCode.Common.FilePathComparerWithEnvironmentVariable OSPlatformSensitiveComparer`
- `readonly static Microsoft.DocAsCode.Common.FilePathComparerWithEnvironmentVariable OSPlatformSensitiveRelativePathComparer`
### `Microsoft.DocAsCode.Common.Git.GitDetail`

- Kind: `class`

#### Constructors

- `GitDetail()`

#### Methods

- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`

#### Properties

- `System.String RelativePath { get; set; }`
- `System.String RemoteBranch { get; set; }`
- `System.String RemoteRepositoryUrl { get; set; }`
### `Microsoft.DocAsCode.Common.Git.GitException`

- Kind: `class`
- Base: `System.Exception`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `GitException()`
- `GitException(System.String message)`
- `GitException(System.String message, System.Exception innerException)`
### `Microsoft.DocAsCode.Common.Git.GitRepoInfo`

- Kind: `class`

#### Constructors

- `GitRepoInfo()`

#### Properties

- `Microsoft.DocAsCode.Common.Git.RepoType RepoType { get; set; }`
- `System.String LocalBranch { get; set; }`
- `System.String LocalHeadCommitId { get; set; }`
- `System.String RemoteBranch { get; set; }`
- `System.String RemoteHeadCommitId { get; set; }`
- `System.String RemoteOriginUrl { get; set; }`
- `System.String RepoAccount { get; set; }`
- `System.String RepoName { get; set; }`
- `System.String RepoProject { get; set; }`
- `System.String RepoRootPath { get; set; }`
- `System.Uri NormalizedRepoUrl { get; set; }`
### `Microsoft.DocAsCode.Common.Git.GitUtility`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.Common.Git.GitDetail static TryGetFileDetail(System.String filePath)`
- `Microsoft.DocAsCode.Common.Git.GitRepoInfo static Parse(System.String repoUrl)`
- `System.Uri static CombineUrl(System.String normalizedRepoUrl, System.String refName, System.String relativePathToRepoRoot, Microsoft.DocAsCode.Common.Git.RepoType repoType)`
### `Microsoft.DocAsCode.Common.Git.RepoType`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Common.Git.RepoType GitHub`
- `const static Microsoft.DocAsCode.Common.Git.RepoType Unknown`
- `const static Microsoft.DocAsCode.Common.Git.RepoType Vso`
### `Microsoft.DocAsCode.Common.HtmlLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `HtmlLogListener(System.IO.StreamWriter writer)`
- `HtmlLogListener(System.String reportPath)`

#### Methods

- `System.String Escape(System.String html, System.Boolean encode = optional)`
- `System.String ReplaceRegex(System.String input, System.Text.RegularExpressions.Regex pattern, System.String replacement)`
- `System.Void WriteCommonHeader()`
- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Diagnostic`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Error`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Info`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Suggestion`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Verbose`
- `const static Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Warning`
### `Microsoft.DocAsCode.Common.HtmlLogListener.ReportItem`

- Kind: `class`

#### Constructors

- `ReportItem()`

#### Properties

- `Microsoft.DocAsCode.Common.HtmlLogListener.MessageSeverity Severity { get; set; }`
- `System.DateTime DateTime { get; set; }`
- `System.String File { get; set; }`
- `System.String Line { get; set; }`
- `System.String Message { get; set; }`
- `System.String Source { get; set; }`
### `Microsoft.DocAsCode.Common.ILogItem`

- Kind: `interface`

#### Properties

- `Microsoft.DocAsCode.Common.LogLevel LogLevel { get; }`
- `System.String Code { get; }`
- `System.String CorrelationId { get; }`
- `System.String File { get; }`
- `System.String Line { get; }`
- `System.String Message { get; }`
- `System.String Phase { get; }`
### `Microsoft.DocAsCode.Common.ILoggerListener`

- Kind: `interface`
- Interfaces: `System.IDisposable`

#### Methods

- `System.Void abstract Flush()`
- `System.Void abstract WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.InfoCodes`

- Kind: `static class`
### `Microsoft.DocAsCode.Common.InfoCodes.Build`

- Kind: `static class`

#### Fields

- `const static System.String IsFullBuild`
- `const static System.String IsIncrementalBuild`
- `const static System.String MarkdownEngineName`
### `Microsoft.DocAsCode.Common.InfoCodes.FullBuildReason`

- Kind: `static class`

#### Fields

- `const static System.String CommitShaMismatch`
- `const static System.String ConfigChanged`
- `const static System.String DocfxVersionChanged`
- `const static System.String ForceRebuild`
- `const static System.String NoAvailableBuildCache`
- `const static System.String NoAvailableGroupCache`
- `const static System.String PluginChanged`
### `Microsoft.DocAsCode.Common.InfoCodes.IncrementalBuildReason`

- Kind: `static class`

#### Fields

- `const static System.String TemplateChanged`
### `Microsoft.DocAsCode.Common.LogCodesLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `LogCodesLogListener()`

#### Methods

- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`

#### Properties

- `System.Collections.Concurrent.ConcurrentDictionary<System.String, System.Collections.Immutable.ImmutableHashSet<System.String>> Codes { get; }`
### `Microsoft.DocAsCode.Common.LogLevel`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Common.LogLevel Diagnostic`
- `const static Microsoft.DocAsCode.Common.LogLevel Error`
- `const static Microsoft.DocAsCode.Common.LogLevel Info`
- `const static Microsoft.DocAsCode.Common.LogLevel Suggestion`
- `const static Microsoft.DocAsCode.Common.LogLevel Verbose`
- `const static Microsoft.DocAsCode.Common.LogLevel Warning`
### `Microsoft.DocAsCode.Common.Logger`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.Common.ILogItem static GetLogItem(Microsoft.DocAsCode.Common.LogLevel level, System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `Microsoft.DocAsCode.Common.ILoggerListener static FindAsyncListener(System.Predicate<Microsoft.DocAsCode.Common.ILoggerListener> predicate)`
- `Microsoft.DocAsCode.Common.ILoggerListener static FindListener(System.Predicate<Microsoft.DocAsCode.Common.ILoggerListener> predicate)`
- `System.Void static Flush()`
- `System.Void static Log(Microsoft.DocAsCode.Common.ILogItem item)`
- `System.Void static Log(Microsoft.DocAsCode.Common.LogLevel level, System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static Log(Microsoft.DocAsCode.Common.LogLevel level, System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static Log(System.Object result)`
- `System.Void static LogDiagnostic(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogDiagnostic(System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static LogError(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogError(System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static LogInfo(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogInfo(System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static LogSuggestion(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogVerbose(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogVerbose(System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static LogWarning(System.String message, System.String phase = optional, System.String file = optional, System.String line = optional, System.String code = optional)`
- `System.Void static LogWarning(System.String message, System.String phase, System.String file, System.String line)`
- `System.Void static RegisterAsyncListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void static RegisterListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void static UnregisterAllListeners()`
- `System.Void static UnregisterAsyncListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void static UnregisterListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`

#### Properties

- `System.Boolean HasError { get; }`
- `System.Int32 WarningCount { get; }`

#### Fields

- `const static System.Int32 WarningThrottling`
- `static Microsoft.DocAsCode.Common.LogLevel LogLevelThreshold`
- `static System.Boolean WarningsAsErrors`
### `Microsoft.DocAsCode.Common.LoggerFileScope`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `LoggerFileScope(System.String fileName)`

#### Methods

- `Microsoft.DocAsCode.Common.LoggerFileScope static Restore(System.Object captured)`
- `System.Object static Capture()`
- `System.Void virtual Dispose()`
### `Microsoft.DocAsCode.Common.LoggerPhaseScope`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `LoggerPhaseScope(System.String phaseName)`
- `LoggerPhaseScope(System.String phaseName, Microsoft.DocAsCode.Common.LogLevel perfLogLevel)`
- `LoggerPhaseScope(System.String phaseName, Microsoft.DocAsCode.Common.LogLevel perfLogLevel, Microsoft.DocAsCode.Common.AggregatedPerformanceScope aggregatedPerformanceLogger)`

#### Methods

- `Microsoft.DocAsCode.Common.LoggerPhaseScope static Restore(System.Object captured)`
- `Microsoft.DocAsCode.Common.LoggerPhaseScope static Restore(System.Object captured, Microsoft.DocAsCode.Common.LogLevel perfLogLevel)`
- `System.Object static Capture()`
- `System.Void virtual Dispose()`
- `T static WithScope<T>(System.String phaseName, Microsoft.DocAsCode.Common.LogLevel perfLogLevel, System.Func<T> func)`
- `T static WithScope<T>(System.String phaseName, System.Func<T> func)`
### `Microsoft.DocAsCode.Common.LogicalCallContext`

- Kind: `static class`

#### Methods

- `System.Object static GetData(System.String key)`
- `System.Void static FreeData(System.String key)`
- `System.Void static SetData(System.String key, System.Object data)`
### `Microsoft.DocAsCode.Common.PathUtility`

- Kind: `static class`

#### Methods

- `System.Boolean static IsDirectory(System.String path)`
- `System.Boolean static IsPathCaseInsensitive()`
- `System.Boolean static IsPathUnderSpecificFolder(System.String path, System.String folder)`
- `System.Boolean static IsRelativePath(System.String path)`
- `System.Boolean static IsVaildFilePath(System.String path)`
- `System.Collections.Generic.IEnumerable<System.String> static CopyFilesToFolder(System.Collections.Generic.IEnumerable<System.String> files, System.String sourceFolder, System.String destinationFolder, System.Boolean overwrite, System.Action<System.String> messageHandler, System.Func<System.String, System.Boolean> errorHandler)`
- `System.Collections.Generic.List<System.String> static GetFileListFromFile(System.String filePath)`
- `System.String static FormatPath(System.String path, System.UriKind kind, System.String basePath = optional)`
- `System.String static GetFullPath(System.String folder, System.String href)`
- `System.String static MakeRelativePath(System.String basePath, System.String absolutePath)`
- `System.String static NormalizePath(System.String path)`
- `System.String static ToCleanUrlFileName(System.String input, System.String replacement = optional)`
- `System.String static ToValidFilePath(System.String input, System.Char replacement = optional)`
- `System.Void static CopyFile(System.String path, System.String targetPath, System.Boolean overwrite = optional)`
- `System.Void static SaveFileListToFile(System.Collections.Generic.List<System.String> fileList, System.String filePath)`

#### Fields

- `const static System.String ListFileExtension`
- `readonly static System.Char[] InvalidFileNameChars`
- `readonly static System.Char[] InvalidPathChars`
### `Microsoft.DocAsCode.Common.PerformanceScope`

- Kind: `class`
- Interfaces: `System.IDisposable`

#### Constructors

- `PerformanceScope(System.Action<System.TimeSpan> logger = optional)`
- `PerformanceScope(System.String content)`
- `PerformanceScope(System.String content, Microsoft.DocAsCode.Common.LogLevel level)`
- `PerformanceScope(System.String content, Microsoft.DocAsCode.Common.LogLevel level, Microsoft.DocAsCode.Common.AggregatedPerformanceScope aggregatedPerformanceLogger)`

#### Methods

- `System.Void virtual Dispose()`
### `Microsoft.DocAsCode.Common.RelativePath`

- Kind: `class`
- Interfaces: `System.IEquatable<Microsoft.DocAsCode.Common.RelativePath>`

#### Methods

- `Microsoft.DocAsCode.Common.RelativePath BasedOn(Microsoft.DocAsCode.Common.RelativePath path)`
- `Microsoft.DocAsCode.Common.RelativePath ChangeFileName(System.String fileName)`
- `Microsoft.DocAsCode.Common.RelativePath GetDirectoryPath()`
- `Microsoft.DocAsCode.Common.RelativePath GetPathFromWorkingFolder()`
- `Microsoft.DocAsCode.Common.RelativePath MakeRelativeTo(Microsoft.DocAsCode.Common.RelativePath relativeTo)`
- `Microsoft.DocAsCode.Common.RelativePath Rebase(Microsoft.DocAsCode.Common.RelativePath from, Microsoft.DocAsCode.Common.RelativePath to)`
- `Microsoft.DocAsCode.Common.RelativePath RemoveWorkingFolder()`
- `Microsoft.DocAsCode.Common.RelativePath UrlDecode()`
- `Microsoft.DocAsCode.Common.RelativePath UrlDecodeUnsafe()`
- `Microsoft.DocAsCode.Common.RelativePath UrlEncode()`
- `Microsoft.DocAsCode.Common.RelativePath static FromUrl(System.String path)`
- `Microsoft.DocAsCode.Common.RelativePath static Parse(System.String path)`
- `Microsoft.DocAsCode.Common.RelativePath static TryParse(System.String path)`
- `Microsoft.DocAsCode.Common.RelativePath static op_Addition(Microsoft.DocAsCode.Common.RelativePath left, Microsoft.DocAsCode.Common.RelativePath right)`
- `Microsoft.DocAsCode.Common.RelativePath static op_Explicit(System.String path)`
- `Microsoft.DocAsCode.Common.RelativePath static op_Subtraction(Microsoft.DocAsCode.Common.RelativePath left, Microsoft.DocAsCode.Common.RelativePath right)`
- `System.Boolean InDirectory(Microsoft.DocAsCode.Common.RelativePath value)`
- `System.Boolean IsFromWorkingFolder()`
- `System.Boolean static IsPathFromWorkingFolder(System.String path)`
- `System.Boolean static IsRelativePath(System.String path)`
- `System.Boolean static TryGetPathWithoutWorkingFolderChar(System.String path, out System.String pathFromWorkingFolder)`
- `System.Boolean static op_Equality(Microsoft.DocAsCode.Common.RelativePath left, Microsoft.DocAsCode.Common.RelativePath right)`
- `System.Boolean static op_Inequality(Microsoft.DocAsCode.Common.RelativePath left, Microsoft.DocAsCode.Common.RelativePath right)`
- `System.Boolean virtual Equals(Microsoft.DocAsCode.Common.RelativePath other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String GetFileNameWithoutExtension()`
- `System.String static GetPathWithoutWorkingFolderChar(System.String path)`
- `System.String static op_Implicit(Microsoft.DocAsCode.Common.RelativePath path)`
- `System.String virtual ToString()`

#### Properties

- `System.Boolean IsEmpty { get; }`
- `System.Int32 ParentDirectoryCount { get; }`
- `System.Int32 SubdirectoryCount { get; }`
- `System.String FileName { get; }`

#### Fields

- `const static System.Char WorkingFolderChar`
- `const static System.String WorkingFolderString`
- `readonly static Microsoft.DocAsCode.Common.RelativePath Empty`
- `readonly static Microsoft.DocAsCode.Common.RelativePath WorkingFolder`
- `readonly static System.Char[] InvalidPartChars`
- `readonly static System.String AltWorkingFolder`
- `readonly static System.String NormalizedWorkingFolder`
### `Microsoft.DocAsCode.Common.ReplayLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `ReplayLogListener(Microsoft.DocAsCode.Common.LogLevel replayLevel = optional)`

#### Methods

- `System.Void AddListener(Microsoft.DocAsCode.Common.ILoggerListener listener)`
- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`

#### Properties

- `System.Boolean Replay { get; set; }`
### `Microsoft.DocAsCode.Common.ReportLogListener`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Common.ILoggerListener`, `System.IDisposable`

#### Constructors

- `ReportLogListener(System.IO.StreamWriter writer, System.String repoRoot, System.String root)`
- `ReportLogListener(System.String reportPath, System.String repoRoot, System.String root)`

#### Methods

- `System.Void virtual Dispose()`
- `System.Void virtual Flush()`
- `System.Void virtual WriteLine(Microsoft.DocAsCode.Common.ILogItem item)`
### `Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Diagnostic`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Error`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Info`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Suggestion`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Verbose`
- `const static Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Warning`
### `Microsoft.DocAsCode.Common.ReportLogListener.ReportItem`

- Kind: `class`

#### Constructors

- `ReportItem()`

#### Properties

- `Microsoft.DocAsCode.Common.ReportLogListener.MessageSeverity Severity { get; set; }`
- `System.DateTime DateTime { get; set; }`
- `System.String Code { get; set; }`
- `System.String CorrelationId { get; set; }`
- `System.String File { get; set; }`
- `System.String Line { get; set; }`
- `System.String Message { get; set; }`
- `System.String Source { get; set; }`
### `Microsoft.DocAsCode.Common.StringExtension`

- Kind: `static class`

#### Methods

- `System.Collections.Generic.IEnumerable<System.String> static GetNormalizedFullPathList(System.Collections.Generic.IEnumerable<System.String> paths)`
- `System.Collections.Generic.IEnumerable<System.String> static GetNormalizedPathList(System.Collections.Generic.IEnumerable<System.String> paths)`
- `System.String static BackSlashToForwardSlash(System.String input)`
- `System.String static ForwardSlashCombine(System.String baseAddress, System.String relativeAddress)`
- `System.String static GetMd5String(System.String content)`
- `System.String static GetNormalizedFullPathKey(System.Collections.Generic.IEnumerable<System.String> list)`
- `System.String static ToDelimitedString(System.Collections.Generic.IEnumerable<System.String> input, System.String delimiter = optional)`
- `System.String static ToDisplayPath(System.String path)`
- `System.String static ToNormalizedFullPath(System.String path)`
- `System.String static ToNormalizedPath(System.String path)`
- `System.String static TrimEnd(System.String input, System.String suffixToRemove)`
### `Microsoft.DocAsCode.Common.SuggestionCodes`

- Kind: `static class`
### `Microsoft.DocAsCode.Common.SuggestionCodes.Build`

- Kind: `static class`

#### Fields

- `const static System.String EmptyInputContents`
- `const static System.String EmptyInputFiles`
### `Microsoft.DocAsCode.Common.TreeIterator`

- Kind: `static class`

#### Methods

- `System.Threading.Tasks.Task static PreorderAsync<T>(T current, T parent, System.Func<T, System.Collections.Generic.IEnumerable<T>> childrenGetter, System.Func<T, T, System.Threading.Tasks.Task<System.Boolean>> action)`
- `System.Void static Preorder<T>(T current, T parent, System.Func<T, System.Collections.Generic.IEnumerable<T>> childrenGetter, System.Func<T, T, System.Boolean> action)`
- `T static PreorderFirstOrDefault<T>(T current, System.Func<T, System.Collections.Generic.IEnumerable<T>> childrenGetter, System.Func<T, System.Boolean> predicate)`
### `Microsoft.DocAsCode.Common.WarningCodes`

- Kind: `static class`
### `Microsoft.DocAsCode.Common.WarningCodes.Build`

- Kind: `static class`

#### Fields

- `const static System.String DuplicateOutputFiles`
- `const static System.String DuplicateUids`
- `const static System.String EmptyTocItemName`
- `const static System.String EmptyTocItemNode`
- `const static System.String InvalidBookmark`
- `const static System.String InvalidFileLink`
- `const static System.String InvalidTagParametersConfig`
- `const static System.String InvalidTaggedPropertyType`
- `const static System.String InvalidTocInclude`
- `const static System.String ReferencedXrefPropertyNotString`
- `const static System.String TooManyWarnings`
- `const static System.String UidNotFound`
- `const static System.String UnknownContentType`
- `const static System.String UnknownContentTypeForTemplate`
- `const static System.String UnknownUriTemplatePipeline`
### `Microsoft.DocAsCode.Common.WarningCodes.Markdown`

- Kind: `static class`

#### Fields

- `const static System.String DifferentTabIdSet`
- `const static System.String DuplicateTabId`
- `const static System.String InvalidCodeSnippet`
- `const static System.String InvalidInclude`
- `const static System.String InvalidInlineCodeSnippet`
- `const static System.String InvalidTabGroup`
- `const static System.String InvalidYamlHeader`
- `const static System.String MissingNewLineBelowSectionHeader`
- `const static System.String NoVisibleTab`
### `Microsoft.DocAsCode.Common.WarningCodes.Metadata`

- Kind: `static class`
### `Microsoft.DocAsCode.Common.WarningCodes.Overwrite`

- Kind: `static class`

#### Fields

- `const static System.String DuplicateOPaths`
- `const static System.String InvalidMarkdownFragments`
- `const static System.String InvalidOPaths`
- `const static System.String InvalidYamlCodeBlockLanguage`
### `Microsoft.DocAsCode.Common.WarningCodes.Yaml`

- Kind: `static class`

#### Fields

- `const static System.String MissingYamlMime`
### `Microsoft.DocAsCode.Common.XHtmlWriter`

- Kind: `class`
- Base: `System.Xml.XmlWriter`
- Interfaces: `System.IAsyncDisposable`, `System.IDisposable`

#### Constructors

- `XHtmlWriter(System.IO.TextWriter writer)`

#### Methods

- `System.String virtual LookupPrefix(System.String ns)`
- `System.Void virtual Flush()`
- `System.Void virtual WriteBase64(System.Byte[] buffer, System.Int32 index, System.Int32 count)`
- `System.Void virtual WriteCData(System.String text)`
- `System.Void virtual WriteCharEntity(System.Char ch)`
- `System.Void virtual WriteChars(System.Char[] buffer, System.Int32 index, System.Int32 count)`
- `System.Void virtual WriteComment(System.String text)`
- `System.Void virtual WriteDocType(System.String name, System.String pubid, System.String sysid, System.String subset)`
- `System.Void virtual WriteEndAttribute()`
- `System.Void virtual WriteEndDocument()`
- `System.Void virtual WriteEndElement()`
- `System.Void virtual WriteEntityRef(System.String name)`
- `System.Void virtual WriteFullEndElement()`
- `System.Void virtual WriteProcessingInstruction(System.String name, System.String text)`
- `System.Void virtual WriteRaw(System.Char[] buffer, System.Int32 index, System.Int32 count)`
- `System.Void virtual WriteRaw(System.String data)`
- `System.Void virtual WriteStartAttribute(System.String prefix, System.String localName, System.String ns)`
- `System.Void virtual WriteStartDocument()`
- `System.Void virtual WriteStartDocument(System.Boolean standalone)`
- `System.Void virtual WriteStartElement(System.String prefix, System.String localName, System.String ns)`
- `System.Void virtual WriteString(System.String text)`
- `System.Void virtual WriteSurrogateCharEntity(System.Char lowChar, System.Char highChar)`
- `System.Void virtual WriteWhitespace(System.String ws)`

#### Properties

- `System.Xml.WriteState WriteState { get; }`
### `Microsoft.DocAsCode.DataContracts.Common.Constants`

- Kind: `static class`

#### Fields

- `const static System.String ContentPlaceholder`
- `const static System.String PrefixSeparator`
- `const static System.String TocYamlFileName`
- `const static System.String YamlExtension`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.DevLang`

- Kind: `static class`

#### Fields

- `const static System.String CSharp`
- `const static System.String VB`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.DocumentType`

- Kind: `static class`

#### Fields

- `const static System.String Toc`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.ExtensionMemberPrefix`

- Kind: `static class`

#### Fields

- `const static System.String Assemblies`
- `const static System.String Children`
- `const static System.String Content`
- `const static System.String DerivedClasses`
- `const static System.String Exceptions`
- `const static System.String ExtensionMethods`
- `const static System.String FullName`
- `const static System.String Implements`
- `const static System.String Inheritance`
- `const static System.String InheritedMembers`
- `const static System.String Modifiers`
- `const static System.String Name`
- `const static System.String NameWithType`
- `const static System.String Namespace`
- `const static System.String Overload`
- `const static System.String Overridden`
- `const static System.String Parent`
- `const static System.String Platform`
- `const static System.String Return`
- `const static System.String Source`
- `const static System.String Spec`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.MetadataName`

- Kind: `static class`

#### Fields

- `const static System.String Version`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.PropertyName`

- Kind: `static class`

#### Fields

- `const static System.String AdditionalNotes`
- `const static System.String Assemblies`
- `const static System.String Children`
- `const static System.String CommentId`
- `const static System.String Conceptual`
- `const static System.String Content`
- `const static System.String DerivedClasses`
- `const static System.String DisplayName`
- `const static System.String DocumentType`
- `const static System.String Documentation`
- `const static System.String Exceptions`
- `const static System.String ExtensionMethods`
- `const static System.String FullName`
- `const static System.String Href`
- `const static System.String Id`
- `const static System.String Implements`
- `const static System.String Inheritance`
- `const static System.String InheritedMembers`
- `const static System.String IsEii`
- `const static System.String Name`
- `const static System.String NameWithType`
- `const static System.String Namespace`
- `const static System.String OutputFileName`
- `const static System.String Overload`
- `const static System.String Overridden`
- `const static System.String Parent`
- `const static System.String Path`
- `const static System.String Platform`
- `const static System.String Return`
- `const static System.String SeeAlsoContent`
- `const static System.String Source`
- `const static System.String Summary`
- `const static System.String Syntax`
- `const static System.String SystemKeys`
- `const static System.String Title`
- `const static System.String TitleOverwriteH1`
- `const static System.String TocHref`
- `const static System.String TopicHref`
- `const static System.String TopicUid`
- `const static System.String Type`
- `const static System.String Uid`
### `Microsoft.DocAsCode.DataContracts.Common.Constants.TableOfContents`

- Kind: `static class`

#### Fields

- `const static System.String MarkdownTocFileName`
- `const static System.String YamlTocFileName`
### `Microsoft.DocAsCode.DataContracts.Common.IOverwriteDocumentViewModel`

- Kind: `interface`

#### Properties

- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Documentation { get; set; }`
- `System.String Conceptual { get; set; }`
- `System.String Uid { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.JTokenConverter`

- Kind: `static class`

#### Methods

- `T static Convert<T>(System.Object obj)`
### `Microsoft.DocAsCode.DataContracts.Common.MarkdownContentAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `MarkdownContentAttribute()`
### `Microsoft.DocAsCode.DataContracts.Common.MarkdownContentIgnoreAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `MarkdownContentIgnoreAttribute()`
### `Microsoft.DocAsCode.DataContracts.Common.ReferenceViewModel`

- Kind: `class`

#### Constructors

- `ReferenceViewModel()`

#### Methods

- `Microsoft.DocAsCode.DataContracts.Common.ReferenceViewModel Clone()`

#### Properties

- `Microsoft.DocAsCode.Common.CompositeDictionary AdditionalJson { get; }`
- `System.Collections.Generic.Dictionary<System.String, System.Object> Additional { get; }`
- `System.Collections.Generic.SortedList<System.String, System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.Common.SpecViewModel>> Specs { get; }`
- `System.Collections.Generic.SortedList<System.String, System.String> FullNameInDevLangs { get; }`
- `System.Collections.Generic.SortedList<System.String, System.String> NameInDevLangs { get; }`
- `System.Collections.Generic.SortedList<System.String, System.String> NameWithTypeInDevLangs { get; }`
- `System.Nullable<System.Boolean> IsExternal { get; set; }`
- `System.String CommentId { get; set; }`
- `System.String Definition { get; set; }`
- `System.String FullName { get; set; }`
- `System.String Href { get; set; }`
- `System.String Name { get; set; }`
- `System.String NameWithType { get; set; }`
- `System.String Parent { get; set; }`
- `System.String Uid { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.SourceDetail`

- Kind: `class`

#### Constructors

- `SourceDetail()`

#### Properties

- `Microsoft.DocAsCode.Common.Git.GitDetail Remote { get; set; }`
- `System.Boolean IsExternalPath { get; set; }`
- `System.Int32 EndLine { get; set; }`
- `System.Int32 StartLine { get; set; }`
- `System.String BasePath { get; set; }`
- `System.String Content { get; set; }`
- `System.String Href { get; set; }`
- `System.String Name { get; set; }`
- `System.String Path { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.SpecViewModel`

- Kind: `class`

#### Constructors

- `SpecViewModel()`

#### Properties

- `System.Boolean IsExternal { get; set; }`
- `System.String FullName { get; set; }`
- `System.String Href { get; set; }`
- `System.String Name { get; set; }`
- `System.String NameWithType { get; set; }`
- `System.String Uid { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel`

- Kind: `class`

#### Constructors

- `TocItemViewModel()`

#### Methods

- `Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel Clone()`
- `System.String virtual ToString()`

#### Properties

- `Microsoft.DocAsCode.Common.CompositeDictionary MetadataJson { get; }`
- `Microsoft.DocAsCode.DataContracts.Common.TocViewModel Items { get; set; }`
- `System.Boolean IsHrefUpdated { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, System.Object> Metadata { get; set; }`
- `System.Collections.Generic.SortedList<System.String, System.String> NameInDevLangs { get; }`
- `System.String AggregatedHref { get; set; }`
- `System.String AggregatedUid { get; set; }`
- `System.String DisplayName { get; set; }`
- `System.String Homepage { get; set; }`
- `System.String HomepageUid { get; set; }`
- `System.String Href { get; set; }`
- `System.String IncludedFrom { get; set; }`
- `System.String Name { get; set; }`
- `System.String NameForCSharp { get; set; }`
- `System.String NameForVB { get; set; }`
- `System.String OriginalHomepage { get; set; }`
- `System.String OriginalHref { get; set; }`
- `System.String OriginalTocHref { get; set; }`
- `System.String OriginalTopicHref { get; set; }`
- `System.String TocHref { get; set; }`
- `System.String TopicHref { get; set; }`
- `System.String TopicUid { get; set; }`
- `System.String Uid { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.TocRootViewModel`

- Kind: `class`

#### Constructors

- `TocRootViewModel()`

#### Properties

- `Microsoft.DocAsCode.DataContracts.Common.TocViewModel Items { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, System.Object> Metadata { get; set; }`
### `Microsoft.DocAsCode.DataContracts.Common.TocViewModel`

- Kind: `class`
- Base: `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`
- Interfaces: `System.Collections.Generic.ICollection<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`, `System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`, `System.Collections.Generic.IList<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`, `System.Collections.Generic.IReadOnlyCollection<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`, `System.Collections.Generic.IReadOnlyList<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel>`, `System.Collections.ICollection`, `System.Collections.IEnumerable`, `System.Collections.IList`

#### Constructors

- `TocViewModel()`
- `TocViewModel(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel> items)`

#### Methods

- `Microsoft.DocAsCode.DataContracts.Common.TocViewModel Clone()`
### `Microsoft.DocAsCode.DataContracts.Common.UniqueIdentityReferenceAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `UniqueIdentityReferenceAttribute()`
### `Microsoft.DocAsCode.DataContracts.Common.UniqueIdentityReferenceIgnoreAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `UniqueIdentityReferenceIgnoreAttribute()`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.AdditionalNotes`

- Kind: `class`

#### Constructors

- `AdditionalNotes()`

#### Properties

- `System.String Caller { get; set; }`
- `System.String Implementer { get; set; }`
- `System.String Inheritor { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter`

- Kind: `class`

#### Constructors

- `ApiParameter()`

#### Methods

- `System.Void CopyInheritedData(Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter src)`

#### Properties

- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.AttributeInfo> Attributes { get; set; }`
- `System.String Description { get; set; }`
- `System.String Name { get; set; }`
- `System.String Type { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.ArgumentInfo`

- Kind: `class`

#### Constructors

- `ArgumentInfo()`

#### Properties

- `System.Object Value { get; set; }`
- `System.String Type { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.AttributeInfo`

- Kind: `class`

#### Constructors

- `AttributeInfo()`

#### Properties

- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ArgumentInfo> Arguments { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.NamedArgumentInfo> NamedArguments { get; set; }`
- `System.String Constructor { get; set; }`
- `System.String Type { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.ExceptionInfo`

- Kind: `class`

#### Constructors

- `ExceptionInfo()`

#### Methods

- `Microsoft.DocAsCode.DataContracts.ManagedReference.ExceptionInfo Clone()`

#### Properties

- `System.String CommentId { get; set; }`
- `System.String Description { get; set; }`
- `System.String Type { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.ItemViewModel`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.DataContracts.Common.IOverwriteDocumentViewModel`

#### Constructors

- `ItemViewModel()`

#### Properties

- `Microsoft.DocAsCode.Common.CompositeDictionary ExtensionData { get; }`
- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Documentation { get; set; }`
- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Source { get; set; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.AdditionalNotes AdditionalNotes { get; set; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Type { get; set; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxDetailViewModel Syntax { get; set; }`
- `System.Boolean IsExplicitInterfaceImplementation { get; set; }`
- `System.Boolean IsExtensionMethod { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, System.Object> Metadata { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.AttributeInfo> Attributes { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ExceptionInfo> Exceptions { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> SeeAlsos { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> Sees { get; set; }`
- `System.Collections.Generic.List<System.String> AssemblyNameList { get; set; }`
- `System.Collections.Generic.List<System.String> Children { get; set; }`
- `System.Collections.Generic.List<System.String> DerivedClasses { get; set; }`
- `System.Collections.Generic.List<System.String> Examples { get; set; }`
- `System.Collections.Generic.List<System.String> ExtensionMethods { get; set; }`
- `System.Collections.Generic.List<System.String> Implements { get; set; }`
- `System.Collections.Generic.List<System.String> Inheritance { get; set; }`
- `System.Collections.Generic.List<System.String> InheritedMembers { get; set; }`
- `System.Collections.Generic.List<System.String> Platform { get; set; }`
- `System.Collections.Generic.List<System.String> SeeAlsosUidReference { get; }`
- `System.Collections.Generic.List<System.String> SeesUidReference { get; }`
- `System.Collections.Generic.SortedList<System.String, System.Collections.Generic.List<System.String>> Modifiers { get; set; }`
- `System.Collections.Generic.SortedList<System.String, System.String> FullNames { get; set; }`
- `System.Collections.Generic.SortedList<System.String, System.String> Names { get; set; }`
- `System.Collections.Generic.SortedList<System.String, System.String> NamesWithType { get; set; }`
- `System.String CommentId { get; set; }`
- `System.String Conceptual { get; set; }`
- `System.String FullName { get; set; }`
- `System.String FullNameForCSharp { get; set; }`
- `System.String FullNameForVB { get; set; }`
- `System.String Href { get; set; }`
- `System.String Id { get; set; }`
- `System.String Name { get; set; }`
- `System.String NameForCSharp { get; set; }`
- `System.String NameForVB { get; set; }`
- `System.String NameWithType { get; set; }`
- `System.String NameWithTypeForCSharp { get; set; }`
- `System.String NameWithTypeForVB { get; set; }`
- `System.String NamespaceName { get; set; }`
- `System.String Overload { get; set; }`
- `System.String Overridden { get; set; }`
- `System.String Parent { get; set; }`
- `System.String Remarks { get; set; }`
- `System.String Summary { get; set; }`
- `System.String Uid { get; set; }`
- `System.String[] SupportedLanguages { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo`

- Kind: `class`

#### Constructors

- `LinkInfo()`

#### Methods

- `Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo Clone()`

#### Properties

- `Microsoft.DocAsCode.DataContracts.ManagedReference.LinkType LinkType { get; set; }`
- `System.String AltText { get; set; }`
- `System.String CommentId { get; set; }`
- `System.String LinkId { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.LinkType`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.LinkType CRef`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.LinkType HRef`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Assembly`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType AttachedEvent`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType AttachedProperty`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Class`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Constructor`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Container`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Default`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Delegate`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Enum`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Event`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Field`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Interface`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Method`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Namespace`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Operator`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Property`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Struct`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Toc`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.NamedArgumentInfo`

- Kind: `class`

#### Constructors

- `NamedArgumentInfo()`

#### Properties

- `System.Object Value { get; set; }`
- `System.String Name { get; set; }`
- `System.String Type { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.PageViewModel`

- Kind: `class`

#### Constructors

- `PageViewModel()`

#### Properties

- `System.Collections.Generic.Dictionary<System.String, System.Object> Metadata { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.Common.ReferenceViewModel> References { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ItemViewModel> Items { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxDetailViewModel`

- Kind: `class`

#### Constructors

- `SyntaxDetailViewModel()`

#### Properties

- `Microsoft.DocAsCode.Common.CompositeDictionary ExtensionData { get; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter Return { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter> Parameters { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter> TypeParameters { get; set; }`
- `System.Collections.Generic.SortedList<System.String, System.String> Contents { get; set; }`
- `System.String Content { get; set; }`
- `System.String ContentForCSharp { get; set; }`
- `System.String ContentForVB { get; set; }`
### `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage CPlusPlus`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage CSharp`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage Default`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage FSharp`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage Javascript`
- `const static Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage VB`
### `Microsoft.DocAsCode.Exceptions.DocfxException`

- Kind: `class`
- Base: `System.Exception`
- Interfaces: `System.Runtime.Serialization.ISerializable`

#### Constructors

- `DocfxException()`
- `DocfxException(System.String message)`
- `DocfxException(System.String message, System.Exception innerException)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.AllMemberFilterVisitor`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

#### Constructors

- `AllMemberFilterVisitor()`

#### Methods

- `System.Boolean virtual CanVisitApi(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
- `System.Boolean virtual CanVisitAttribute(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.AttributeFilterData`

- Kind: `class`

#### Constructors

- `AttributeFilterData()`

#### Properties

- `System.Collections.Generic.IDictionary<System.String, System.String> ConstructorNamedArguments { get; set; }`
- `System.Collections.Generic.IEnumerable<System.String> ConstructorArguments { get; set; }`
- `System.String Id { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.AttributeFilterInfo`

- Kind: `class`

#### Constructors

- `AttributeFilterInfo()`

#### Methods

- `System.Boolean ContainedIn(Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData symbol)`

#### Properties

- `System.Collections.Generic.Dictionary<System.String, System.String> ConstructorNamedArguments { get; set; }`
- `System.Collections.Generic.List<System.String> ConstructorArguments { get; set; }`
- `System.String Uid { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.BuildInfo`

- Kind: `class`

#### Constructors

- `BuildInfo()`

#### Properties

- `Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions Options { get; set; }`
- `System.Collections.Generic.IDictionary<System.String, System.Collections.Generic.List<System.String>> ContainedFiles { get; set; }`
- `System.Collections.Generic.IEnumerable<System.String> RelativeOutputFiles { get; set; }`
- `System.DateTime CompleteUtcTime { get; set; }`
- `System.DateTime TriggeredUtcTime { get; set; }`
- `System.String BuildAssembly { get; set; }`
- `System.String CheckSum { get; set; }`
- `System.String InputFilesKey { get; set; }`
- `System.String OutputFolder { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.BuildMembers`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `BuildMembers()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.BuildToc`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `BuildToc()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CRefTarget`

- Kind: `class`

#### Constructors

- `CRefTarget()`

#### Properties

- `System.String CommentId { get; set; }`
- `System.String Id { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CSReferenceItemVisitor`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItemVisitor`

#### Constructors

- `CSReferenceItemVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem referenceItem, System.Boolean asOverload)`

#### Methods

- `System.Void virtual VisitArrayType(Microsoft.CodeAnalysis.IArrayTypeSymbol symbol)`
- `System.Void virtual VisitDynamicType(Microsoft.CodeAnalysis.IDynamicTypeSymbol symbol)`
- `System.Void virtual VisitEvent(Microsoft.CodeAnalysis.IEventSymbol symbol)`
- `System.Void virtual VisitField(Microsoft.CodeAnalysis.IFieldSymbol symbol)`
- `System.Void virtual VisitMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol)`
- `System.Void virtual VisitNamespace(Microsoft.CodeAnalysis.INamespaceSymbol symbol)`
- `System.Void virtual VisitPointerType(Microsoft.CodeAnalysis.IPointerTypeSymbol symbol)`
- `System.Void virtual VisitProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol)`
- `System.Void virtual VisitTypeParameter(Microsoft.CodeAnalysis.ITypeParameterSymbol symbol)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CSYamlModelGenerator`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator`

#### Constructors

- `CSYamlModelGenerator()`

#### Methods

- `Microsoft.CodeAnalysis.CSharp.Syntax.ExpressionSyntax static GetLiteralExpressionCore(System.Object value, Microsoft.CodeAnalysis.ITypeSymbol type)`
- `System.Void virtual DefaultVisit(Microsoft.CodeAnalysis.ISymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateEvent(Microsoft.CodeAnalysis.IEventSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateField(Microsoft.CodeAnalysis.IFieldSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CSharpNameVisitorCreator`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitorCreator`

#### Constructors

- `CSharpNameVisitorCreator(Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions options)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CacheBase`

- Kind: `abstract class`

#### Constructors

- `CacheBase(System.String path)`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.BuildInfo GetValidConfig(System.Collections.Generic.IEnumerable<System.String> inputProjects)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.BuildInfo GetValidConfig(System.String key)`
- `System.Void SaveToCache(System.Collections.Generic.IEnumerable<System.String> inputProjects, System.Collections.Generic.IDictionary<System.String, System.Collections.Generic.List<System.String>> containedFiles, System.DateTime triggeredTime, System.String outputFolder, System.Collections.Generic.IList<System.String> fileRelativePaths, Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions options)`
- `System.Void SaveToCache(System.String key, System.Collections.Generic.IDictionary<System.String, System.Collections.Generic.List<System.String>> containedFiles, System.DateTime triggeredTime, System.String outputFolder, System.Collections.Generic.IList<System.String> fileRelativePaths, Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions options)`
- `System.Void SaveToCache(System.String key, System.Collections.Generic.IEnumerable<System.String> containedFiles, System.DateTime triggeredTime, System.String outputFolder, System.Collections.Generic.IList<System.String> fileRelativePaths, Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions options)`

#### Fields

- `readonly static System.String AssemblyName`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CachedFilterVisitor`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.DelegatingFilterVisitor`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

#### Constructors

- `CachedFilterVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor inner)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CompositeYamlModelGenerator`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.YamlModelGenerator`

#### Constructors

- `CompositeYamlModelGenerator(System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator> generators)`
- `CompositeYamlModelGenerator(params Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator[] generators)`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.CompositeYamlModelGenerator static op_Addition(Microsoft.DocAsCode.Metadata.ManagedReference.CompositeYamlModelGenerator left, Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator right)`
- `System.Void virtual DefaultVisit(Microsoft.CodeAnalysis.ISymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateEvent(Microsoft.CodeAnalysis.IEventSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateField(Microsoft.CodeAnalysis.IFieldSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRule`

- Kind: `class`

#### Constructors

- `ConfigFilterRule()`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRule static Load(System.String configFile)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRule static LoadWithDefaults(System.String filterConfigFile)`
- `System.Boolean CanVisitApi(Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData symbol)`
- `System.Boolean CanVisitAttribute(Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData symbol)`

#### Properties

- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItemUnion> ApiRules { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItemUnion> AttributeRules { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleExcludeItem`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItem`

#### Constructors

- `ConfigFilterRuleExcludeItem()`

#### Properties

- `System.Boolean CanVisit { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleIncludeItem`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItem`

#### Constructors

- `ConfigFilterRuleIncludeItem()`

#### Properties

- `System.Boolean CanVisit { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItem`

- Kind: `abstract class`

#### Methods

- `System.Boolean IsMatch(Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData symbol)`

#### Properties

- `Microsoft.DocAsCode.Metadata.ManagedReference.AttributeFilterInfo Attribute { get; set; }`
- `System.Boolean CanVisit { get; }`
- `System.Nullable<Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind> Kind { get; set; }`
- `System.String UidRegex { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItemUnion`

- Kind: `class`

#### Constructors

- `ConfigFilterRuleItemUnion()`

#### Properties

- `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleExcludeItem Exclude { get; set; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleIncludeItem Include { get; set; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRuleItem Rule { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterVisitor`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.DelegatingFilterVisitor`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

#### Constructors

- `ConfigFilterVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor inner, Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRule rule)`
- `ConfigFilterVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor inner, System.String configFile)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.CopyInherited`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `CopyInherited()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.DefaultFilterVisitor`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

#### Constructors

- `DefaultFilterVisitor()`

#### Methods

- `System.Boolean virtual CanVisitApi(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
- `System.Boolean virtual CanVisitAttribute(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.DelegatingFilterVisitor`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

#### Constructors

- `DelegatingFilterVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor inner)`

#### Methods

- `System.Boolean virtual CanVisitApi(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
- `System.Boolean virtual CanVisitAttribute(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Assembly`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Class`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Delegate`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Enum`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Event`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Field`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Interface`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Member`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Method`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Namespace`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Property`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Struct`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind Type`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKindHelper`

- Kind: `static class`

#### Methods

- `System.Boolean static Contains(Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind kind, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData symbol)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions`

- Kind: `class`

#### Constructors

- `ExtractMetadataOptions()`

#### Properties

- `System.Boolean DisableDefaultFilter { get; set; }`
- `System.Boolean PreserveRawInlineComments { get; set; }`
- `System.Boolean ShouldSkipMarkup { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, System.String> MSBuildProperties { get; set; }`
- `System.Collections.Generic.IReadOnlyDictionary<Microsoft.CodeAnalysis.Compilation, System.Collections.Generic.IEnumerable<Microsoft.CodeAnalysis.IMethodSymbol>> RoslynExtensionMethods { get; set; }`
- `System.String CodeSourceBasePath { get; set; }`
- `System.String FilterConfigFile { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.FilterVisitorExtensions`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor static WithCache(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor fv)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor static WithConfig(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor fv, Microsoft.DocAsCode.Metadata.ManagedReference.ConfigFilterRule rule)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor static WithConfig(Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor fv, System.String configFile)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IBuildController`

- Kind: `interface`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem abstract ExtractMetadata(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters parameters)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IExtractor`

- Kind: `interface`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem abstract Extract(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor`

- Kind: `interface`

#### Methods

- `System.Boolean abstract CanVisitApi(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember = optional, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer = optional)`
- `System.Boolean abstract CanVisitAttribute(Microsoft.CodeAnalysis.ISymbol symbol, System.Boolean wantProtectedMember = optional, Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor outer = optional)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters`

- Kind: `interface`

#### Methods

- `System.Boolean abstract HasChanged(Microsoft.DocAsCode.Metadata.ManagedReference.BuildInfo buildInfo)`

#### Properties

- `Microsoft.DocAsCode.Metadata.ManagedReference.BuildInfo BuildInfo { get; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions Options { get; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ProjectLevelCache Cache { get; }`
- `System.Collections.Generic.IEnumerable<System.String> Files { get; }`
- `System.String Key { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

- Kind: `interface`

#### Methods

- `System.Void abstract Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.IRoslynBuildController`

- Kind: `interface`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IBuildController`

#### Methods

- `Microsoft.CodeAnalysis.Compilation abstract GetCompilation(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
- `Microsoft.CodeAnalysis.IAssemblySymbol abstract GetAssembly(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext`

- Kind: `interface`

#### Properties

- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Source { get; set; }`
- `System.Action<System.String, System.String> AddReferenceDelegate { get; set; }`
- `System.Boolean PreserveRawInlineComments { get; set; }`
- `System.Func<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.CRefTarget> ResolveCRef { get; }`
- `System.String CodeSourceBasePath { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.LayoutCheckAndCleanup`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `LayoutCheckAndCleanup()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem Exception`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem ExternalComments`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem Hierarchy`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem InlineComments`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem MemberTable`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem SeeAlso`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem Syntax`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem Title`
### `Microsoft.DocAsCode.Metadata.ManagedReference.LinkItem`

- Kind: `class`

#### Constructors

- `LinkItem()`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.LinkItem Clone()`

#### Properties

- `System.Boolean IsExternalPath { get; set; }`
- `System.String DisplayName { get; set; }`
- `System.String DisplayNamesWithType { get; set; }`
- `System.String DisplayQualifiedNames { get; set; }`
- `System.String Href { get; set; }`
- `System.String Name { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.MergeCommentsHelper`

- Kind: `static class`

#### Methods

- `System.Void static MergeComments(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, System.Collections.Generic.IEnumerable<System.String> commentFiles)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem`

- Kind: `class`
- Interfaces: `System.ICloneable`

#### Constructors

- `MetadataItem()`

#### Methods

- `System.Object virtual Clone()`
- `System.String virtual ToString()`
- `System.Void CopyInheritedData(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem src)`

#### Properties

- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Documentation { get; set; }`
- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Source { get; set; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType Type { get; set; }`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage Language { get; set; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem Parent { get; set; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.SyntaxDetail Syntax { get; set; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentModel CommentModel { get; set; }`
- `System.Boolean IsExplicitInterfaceImplementation { get; set; }`
- `System.Boolean IsExtensionMethod { get; set; }`
- `System.Boolean IsExtraDoc { get; set; }`
- `System.Boolean IsInvalid { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem> References { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.AttributeInfo> Attributes { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ExceptionInfo> Exceptions { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> SeeAlsos { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> Sees { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.LayoutItem> Layout { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem> Items { get; set; }`
- `System.Collections.Generic.List<System.String> AssemblyNameList { get; set; }`
- `System.Collections.Generic.List<System.String> DerivedClasses { get; set; }`
- `System.Collections.Generic.List<System.String> Examples { get; set; }`
- `System.Collections.Generic.List<System.String> ExtensionMethods { get; set; }`
- `System.Collections.Generic.List<System.String> Implements { get; set; }`
- `System.Collections.Generic.List<System.String> Inheritance { get; set; }`
- `System.Collections.Generic.List<System.String> InheritedMembers { get; set; }`
- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.Collections.Generic.List<System.String>> Modifiers { get; set; }`
- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.String> DisplayNames { get; set; }`
- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.String> DisplayNamesWithType { get; set; }`
- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.String> DisplayQualifiedNames { get; set; }`
- `System.String CommentId { get; set; }`
- `System.String ExtraDocFilePath { get; set; }`
- `System.String InheritDoc { get; set; }`
- `System.String Name { get; set; }`
- `System.String NamespaceName { get; set; }`
- `System.String Overload { get; set; }`
- `System.String Overridden { get; set; }`
- `System.String RawComment { get; set; }`
- `System.String Remarks { get; set; }`
- `System.String Summary { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel`

- Kind: `class`

#### Constructors

- `MetadataModel()`

#### Properties

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem TocYamlViewModel { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem> Members { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions All`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions None`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions Qualified`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions UseAlias`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithGenericParameter`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithMethodGenericParameter`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithNamespace`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithParameter`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithType`
- `const static Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions WithTypeGenericParameter`
### `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitor`

- Kind: `abstract class`
- Base: `Microsoft.CodeAnalysis.SymbolVisitor`
### `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitorCreator`

- Kind: `abstract class`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitorCreator static GetCSharp(Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions option)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitorCreator static GetVB(Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions option)`
- `System.String GetName(Microsoft.CodeAnalysis.ISymbol symbol)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.NormalizeSyntax`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `NormalizeSyntax()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ProjectLevelCache`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.CacheBase`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.ProjectLevelCache static Get(System.Collections.Generic.IEnumerable<System.String> files)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.ProjectLevelCache static Get(System.String firstFile)`

#### Fields

- `readonly System.String OutputFolder`
- `static System.Func<System.String, System.String> GetProjectLevelConfig`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem`

- Kind: `class`

#### Constructors

- `ReferenceItem()`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem Clone()`
- `System.Void Merge(Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem other)`

#### Properties

- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.Collections.Generic.List<Microsoft.DocAsCode.Metadata.ManagedReference.LinkItem>> Parts { get; set; }`
- `System.Nullable<System.Boolean> IsDefinition { get; set; }`
- `System.String CommentId { get; set; }`
- `System.String Definition { get; set; }`
- `System.String Parent { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItemVisitor`

- Kind: `abstract class`
- Base: `Microsoft.CodeAnalysis.SymbolVisitor`

#### Methods

- `System.Void virtual VisitNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol)`

#### Fields

- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat QualifiedFormat`
- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat QualifiedFormatWithoutGenericeParameter`
- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat ShortFormat`
- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat ShortFormatWithoutGenericeParameter`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ResolveReference`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `ResolveReference()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext`

- Kind: `class`

#### Constructors

- `ResolverContext()`

#### Properties

- `System.Boolean PreserveRawInlineComments { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem> Members { get; set; }`
- `System.Collections.Generic.Dictionary<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem> References { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.RoslynIntermediateMetadataExtractor`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IExtractor`

#### Constructors

- `RoslynIntermediateMetadataExtractor(Microsoft.DocAsCode.Metadata.ManagedReference.IRoslynBuildController controller)`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual Extract(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
- `System.Collections.Generic.IReadOnlyDictionary<Microsoft.CodeAnalysis.Compilation, System.Collections.Generic.IEnumerable<Microsoft.CodeAnalysis.IMethodSymbol>> static GetAllExtensionMethodsFromAssembly(Microsoft.CodeAnalysis.Compilation compilation, System.Collections.Generic.IEnumerable<Microsoft.CodeAnalysis.IAssemblySymbol> assemblies)`
- `System.Collections.Generic.IReadOnlyDictionary<Microsoft.CodeAnalysis.Compilation, System.Collections.Generic.IEnumerable<Microsoft.CodeAnalysis.IMethodSymbol>> static GetAllExtensionMethodsFromCompilation(System.Collections.Generic.IEnumerable<Microsoft.CodeAnalysis.Compilation> compilations)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.RoslynSourceFileBuildController`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IBuildController`, `Microsoft.DocAsCode.Metadata.ManagedReference.IRoslynBuildController`

#### Constructors

- `RoslynSourceFileBuildController(Microsoft.CodeAnalysis.Compilation compilation, Microsoft.CodeAnalysis.IAssemblySymbol assembly = optional)`

#### Methods

- `Microsoft.CodeAnalysis.Compilation virtual GetCompilation(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
- `Microsoft.CodeAnalysis.IAssemblySymbol virtual GetAssembly(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters key)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual ExtractMetadata(Microsoft.DocAsCode.Metadata.ManagedReference.IInputParameters parameters)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SetDerivedClass`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `SetDerivedClass()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SetParent`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.IResolverPipeline`

#### Constructors

- `SetParent()`

#### Methods

- `System.Void virtual Run(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel yaml, Microsoft.DocAsCode.Metadata.ManagedReference.ResolverContext context)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator`

- Kind: `abstract class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.YamlModelGenerator`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.CompositeYamlModelGenerator static op_Addition(Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator left, Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator right)`

#### Properties

- `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage Language { get; }`

#### Fields

- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat QualifiedFormat`
- `readonly static Microsoft.CodeAnalysis.SymbolDisplayFormat ShortFormat`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SymbolFilterData`

- Kind: `class`

#### Constructors

- `SymbolFilterData()`

#### Properties

- `System.Collections.Generic.IEnumerable<Microsoft.DocAsCode.Metadata.ManagedReference.AttributeFilterData> Attributes { get; set; }`
- `System.Nullable<Microsoft.DocAsCode.Metadata.ManagedReference.ExtendedSymbolKind> Kind { get; set; }`
- `System.String Id { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter`

- Kind: `class`
- Base: `Microsoft.CodeAnalysis.SymbolVisitor<Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem>`

#### Constructors

- `SymbolVisitorAdapter(Microsoft.DocAsCode.Metadata.ManagedReference.YamlModelGenerator generator, Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage language, Microsoft.CodeAnalysis.Compilation compilation, Microsoft.DocAsCode.Metadata.ManagedReference.ExtractMetadataOptions options)`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual DefaultVisit(Microsoft.CodeAnalysis.ISymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitAssembly(Microsoft.CodeAnalysis.IAssemblySymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitEvent(Microsoft.CodeAnalysis.IEventSymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitField(Microsoft.CodeAnalysis.IFieldSymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitNamespace(Microsoft.CodeAnalysis.INamespaceSymbol symbol)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem virtual VisitProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol)`
- `System.String AddOverloadReference(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String AddReference(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String AddReference(System.String id, System.String commentId)`
- `System.String AddSpecReference(Microsoft.CodeAnalysis.ISymbol symbol, System.Collections.Generic.IReadOnlyList<System.String> typeGenericParameters = optional, System.Collections.Generic.IReadOnlyList<System.String> methodGenericParameters = optional)`

#### Properties

- `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage Language { get; }`
- `Microsoft.DocAsCode.Metadata.ManagedReference.IFilterVisitor FilterVisitor { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.SyntaxDetail`

- Kind: `class`

#### Constructors

- `SyntaxDetail()`

#### Methods

- `System.Void CopyInheritedData(Microsoft.DocAsCode.Metadata.ManagedReference.SyntaxDetail src)`

#### Properties

- `Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter Return { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter> Parameters { get; set; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter> TypeParameters { get; set; }`
- `System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, System.String> Content { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentModel`

- Kind: `class`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentModel static CreateModel(System.String xml, Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage language, Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext context)`
- `System.String GetParameter(System.String name)`
- `System.String GetTypeParameter(System.String name)`
- `System.Void CopyInheritedData(Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentModel src)`

#### Properties

- `System.Collections.Generic.Dictionary<System.String, System.String> Parameters { get; }`
- `System.Collections.Generic.Dictionary<System.String, System.String> TypeParameters { get; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.ExceptionInfo> Exceptions { get; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> SeeAlsos { get; }`
- `System.Collections.Generic.List<Microsoft.DocAsCode.DataContracts.ManagedReference.LinkInfo> Sees { get; }`
- `System.Collections.Generic.List<System.String> Examples { get; }`
- `System.String InheritDoc { get; }`
- `System.String Remarks { get; }`
- `System.String Returns { get; }`
- `System.String Summary { get; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentParserContext`

- Kind: `class`
- Interfaces: `Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext`

#### Constructors

- `TripleSlashCommentParserContext()`

#### Properties

- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail Source { get; set; }`
- `System.Action<System.String, System.String> AddReferenceDelegate { get; set; }`
- `System.Boolean PreserveRawInlineComments { get; set; }`
- `System.Func<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.CRefTarget> ResolveCRef { get; set; }`
- `System.String CodeSourceBasePath { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.TripleSlashCommentTransformer`

- Kind: `static class`

#### Methods

- `System.Xml.Linq.XDocument static Transform(System.String xml, Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage language)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.VBNameVisitorCreator`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.NameVisitorCreator`

#### Constructors

- `VBNameVisitorCreator(Microsoft.DocAsCode.Metadata.ManagedReference.NameOptions options)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.VBReferenceItemVisitor`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItemVisitor`

#### Constructors

- `VBReferenceItemVisitor(Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem referenceItem, System.Boolean asOverload)`

#### Methods

- `System.Void virtual VisitArrayType(Microsoft.CodeAnalysis.IArrayTypeSymbol symbol)`
- `System.Void virtual VisitEvent(Microsoft.CodeAnalysis.IEventSymbol symbol)`
- `System.Void virtual VisitField(Microsoft.CodeAnalysis.IFieldSymbol symbol)`
- `System.Void virtual VisitMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol)`
- `System.Void virtual VisitNamespace(Microsoft.CodeAnalysis.INamespaceSymbol symbol)`
- `System.Void virtual VisitPointerType(Microsoft.CodeAnalysis.IPointerTypeSymbol symbol)`
- `System.Void virtual VisitProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol)`
- `System.Void virtual VisitTypeParameter(Microsoft.CodeAnalysis.ITypeParameterSymbol symbol)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.VBYamlModelGenerator`

- Kind: `class`
- Base: `Microsoft.DocAsCode.Metadata.ManagedReference.SimpleYamlModelGenerator`

#### Constructors

- `VBYamlModelGenerator()`

#### Methods

- `System.Void virtual DefaultVisit(Microsoft.CodeAnalysis.ISymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateEvent(Microsoft.CodeAnalysis.IEventSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateField(Microsoft.CodeAnalysis.IFieldSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.VisitorHelper`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.DataContracts.Common.SourceDetail static GetSourceDetail(Microsoft.CodeAnalysis.ISymbol symbol)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter static GetParameterDescription(Microsoft.CodeAnalysis.ISymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, System.String id, System.Boolean isReturn, Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext context)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.ApiParameter static GetTypeParameterDescription(Microsoft.CodeAnalysis.ITypeParameterSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext context)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType static GetMemberTypeFromTypeKind(Microsoft.CodeAnalysis.TypeKind typeKind)`
- `System.Boolean static InGlobalNamespace(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String static GetCommentId(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String static GetId(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String static GetOverloadId(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.String static GetOverloadIdBody(Microsoft.CodeAnalysis.ISymbol symbol)`
- `System.Void static FeedComments(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.ITripleSlashCommentParserContext context)`

#### Properties

- `System.String GlobalNamespaceId { get; set; }`
### `Microsoft.DocAsCode.Metadata.ManagedReference.YamlMetadataResolver`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataModel static ResolveMetadata(System.Collections.Generic.Dictionary<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem> allMembers, System.Collections.Generic.Dictionary<System.String, Microsoft.DocAsCode.Metadata.ManagedReference.ReferenceItem> allReferences, System.Boolean preserveRawInlineComments)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.YamlModelGenerator`

- Kind: `abstract class`

#### Methods

- `System.Void virtual DefaultVisit(Microsoft.CodeAnalysis.ISymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateEvent(Microsoft.CodeAnalysis.IEventSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateField(Microsoft.CodeAnalysis.IFieldSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateMethod(Microsoft.CodeAnalysis.IMethodSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateNamedType(Microsoft.CodeAnalysis.INamedTypeSymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
- `System.Void virtual GenerateProperty(Microsoft.CodeAnalysis.IPropertySymbol symbol, Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item, Microsoft.DocAsCode.Metadata.ManagedReference.SymbolVisitorAdapter adapter)`
### `Microsoft.DocAsCode.Metadata.ManagedReference.YamlViewModelExtensions`

- Kind: `static class`

#### Methods

- `Microsoft.DocAsCode.DataContracts.Common.SpecViewModel static ToSpecViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.LinkItem model)`
- `Microsoft.DocAsCode.DataContracts.Common.TocItemViewModel static ToTocItemViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item)`
- `Microsoft.DocAsCode.DataContracts.Common.TocViewModel static ToTocViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.ItemViewModel static ToItemViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem model)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.PageViewModel static ToPageViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem model)`
- `Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxDetailViewModel static ToSyntaxDetailViewModel(Microsoft.DocAsCode.Metadata.ManagedReference.SyntaxDetail model)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem static ShrinkToSimpleToc(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item)`
- `Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem static ShrinkToSimpleTocWithNamespaceNotEmpty(Microsoft.DocAsCode.Metadata.ManagedReference.MetadataItem item)`
- `System.Boolean static AllowMultipleItems(Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType type)`
- `System.Boolean static IsPageLevel(Microsoft.DocAsCode.DataContracts.ManagedReference.MemberType type)`
- `TValue static GetLanguageProperty<TValue>(System.Collections.Generic.SortedList<Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage, TValue> dict, Microsoft.DocAsCode.DataContracts.ManagedReference.SyntaxLanguage language, TValue defaultValue = optional)`
### `Microsoft.DocAsCode.Plugins.EnvironmentContext`

- Kind: `static class`

#### Methods

- `System.Void static SetBaseDirectory(System.String dir)`
- `System.Void static SetGitFeaturesDisabled(System.Boolean disabled)`
- `System.Void static SetOutputDirectory(System.String dir)`
- `System.Void static SetVersion(System.String version)`

#### Properties

- `System.Boolean GitFeaturesDisabled { get; }`
- `System.String BaseDirectory { get; }`
- `System.String OutputDirectory { get; }`
- `System.String Version { get; }`
### `Microsoft.DocAsCode.YamlSerialization.ExtensibleMemberAttribute`

- Kind: `class`
- Base: `System.Attribute`

#### Constructors

- `ExtensibleMemberAttribute()`
- `ExtensibleMemberAttribute(System.String prefix)`

#### Properties

- `System.String Prefix { get; }`
