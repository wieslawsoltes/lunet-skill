# Lunet.Watcher Public API

Assembly path: `src/Lunet.Watcher/bin/Release/net10.0/Lunet.Watcher.dll`

Exported types: **4**

## Types

### `Lunet.Watcher.BuildCommandRunner`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteCommandRunner`

#### Constructors

- `BuildCommandRunner()`

#### Methods

- `System.Threading.Tasks.Task<Lunet.Core.RunnerResult> virtual RunAsync(Lunet.Core.SiteRunner runner, System.Threading.CancellationToken cancellationToken)`

#### Properties

- `System.Boolean Development { get; set; }`
- `System.Boolean SingleThreaded { get; set; }`
- `System.Boolean Watch { get; set; }`
### `Lunet.Watcher.FileSystemEventBatchArgs`

- Kind: `class`
- Base: `System.EventArgs`

#### Constructors

- `FileSystemEventBatchArgs()`

#### Properties

- `System.Collections.Generic.List<Zio.FileChangedEventArgs> FileEvents { get; }`
### `Lunet.Watcher.SiteWatcherService`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteService`, `System.IDisposable`

#### Constructors

- `SiteWatcherService(Lunet.Core.SiteConfiguration siteConfig)`

#### Methods

- `System.Threading.Tasks.Task<Lunet.Core.RunnerResult> static RunAsync(Lunet.Core.SiteRunner runner, System.Threading.CancellationToken cancellationToken)`
- `System.Void Start()`
- `System.Void Stop()`
- `System.Void virtual Dispose()`

#### Properties

- `System.Collections.Concurrent.BlockingCollection<Lunet.Watcher.FileSystemEventBatchArgs> FileSystemEvents { get; }`

#### Fields

- `System.Func<Zio.UPath, System.Boolean> IsHandlingPath`
### `Lunet.Watcher.WatcherModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule`

#### Constructors

- `WatcherModule()`

#### Properties

- `XenoAtom.CommandLine.Command BuildAndWatchCommand { get; }`
