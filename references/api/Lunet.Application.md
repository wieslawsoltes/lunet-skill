# Lunet.Application Public API

Assembly path: `src/Lunet.Application/bin/Release/net10.0/Lunet.Application.dll`

Exported types: **1**

## Types

### `Lunet.LunetApp`

- Kind: `class`

#### Constructors

- `LunetApp(Lunet.Core.SiteConfiguration config = optional)`

#### Methods

- `System.Threading.Tasks.Task<System.Int32> RunAsync(System.Threading.CancellationTokenSource cancellationTokenSource, params System.String[] args)`
- `System.Threading.Tasks.Task<System.Int32> RunAsync(params System.String[] args)`

#### Properties

- `Lunet.Core.SiteConfiguration Config { get; }`
- `Lunet.Helpers.OrderedList<Lunet.Core.SiteModule> Modules { get; }`
