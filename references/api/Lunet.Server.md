# Lunet.Server Public API

Assembly path: `src/Lunet.Server/bin/Release/net10.0/Lunet.Server.dll`

Exported types: **5**

## Types

### `Lunet.Server.ServeCommandRunner`

- Kind: `class`
- Base: `Lunet.Watcher.BuildCommandRunner`
- Interfaces: `Lunet.Core.ISiteCommandRunner`

#### Constructors

- `ServeCommandRunner()`
### `Lunet.Server.ServerModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Server.ServerPlugin>`

#### Constructors

- `ServerModule()`

#### Properties

- `XenoAtom.CommandLine.Command ServerCommand { get; }`
### `Lunet.Server.ServerPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `ServerPlugin(Lunet.Core.SiteObject site)`
### `Lunet.Server.SiteObjectExtensions`

- Kind: `static class`

#### Methods

- `System.Boolean static GetLiveReload(Lunet.Core.SiteObject site)`
- `System.Void static SetLiveReload(Lunet.Core.SiteObject site, System.Boolean value)`
### `Lunet.Server.SiteServerService`

- Kind: `class`
- Interfaces: `Lunet.Core.ISiteService`, `System.IDisposable`

#### Constructors

- `SiteServerService(Lunet.Core.SiteConfiguration configuration)`

#### Methods

- `System.Boolean Update(Lunet.Core.SiteObject from)`
- `System.Threading.Tasks.Task NotifyReloadToClients()`
- `System.Threading.Tasks.Task StartOrUpdateAsync(System.Threading.CancellationToken token)`
- `System.Void ShutdownAndWaitForShutdown()`
- `System.Void static SetupLiveReloadClient(Lunet.Core.SiteObject site)`
- `System.Void virtual Dispose()`

#### Properties

- `System.Boolean LiveReload { get; set; }`
- `System.Boolean Logging { get; set; }`
- `System.String BasePath { get; set; }`
- `System.String BaseUrl { get; set; }`
- `System.String Environment { get; set; }`
- `System.String ErrorRedirect { get; set; }`

#### Fields

- `const static System.String DefaultBaseUrl`
- `const static System.String DefaultEnvironment`
- `const static System.String DefaultRedirect`
