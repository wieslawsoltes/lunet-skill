# Lunet.ApiExample Public API

Assembly path: `src/Lunet.ApiExample/bin/Release/net10.0/Lunet.ApiExample.dll`

Exported types: **34**

## Types

### `Lunet.ApiExample.Advanced.ApiUserExtensions`

- Kind: `static class`

#### Methods

- `System.Boolean static HasVisibleName(Lunet.ApiExample.ApiUser user)`
- `System.String static get_DisplayName(Lunet.ApiExample.ApiUser user)`
### `Lunet.ApiExample.Advanced.ApiUserExtensions.<G>$6D10AC436CD7C69B71D4067302DC985C`

- Kind: `class`

#### Methods

- `System.Boolean HasVisibleName()`

#### Properties

- `System.String DisplayName { get; }`
### `Lunet.ApiExample.Advanced.ApiUserExtensions.<G>$6D10AC436CD7C69B71D4067302DC985C.<M>$57EE207D97F7ADF79DC6AD24AA3C0B50`

- Kind: `static class`
### `Lunet.ApiExample.Advanced.BuildInfo`

- Kind: `class`
- Interfaces: `System.IEquatable<Lunet.ApiExample.Advanced.BuildInfo>`

#### Constructors

- `BuildInfo(System.String Version)`

#### Methods

- `Lunet.ApiExample.Advanced.BuildInfo <Clone>$()`
- `System.Boolean static op_Equality(Lunet.ApiExample.Advanced.BuildInfo left, Lunet.ApiExample.Advanced.BuildInfo right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.Advanced.BuildInfo left, Lunet.ApiExample.Advanced.BuildInfo right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.Advanced.BuildInfo other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.String Version)`

#### Properties

- `System.Collections.Generic.IReadOnlyList<System.String> Tags { get; set; }`
- `System.String Commit { get; set; }`
- `System.String Version { get; set; }`
### `Lunet.ApiExample.Advanced.CheckedInteger`

- Kind: `struct`
- Base: `System.ValueType`

#### Constructors

- `CheckedInteger(System.Int32 value)`

#### Methods

- `Lunet.ApiExample.Advanced.CheckedInteger static op_Addition(Lunet.ApiExample.Advanced.CheckedInteger left, Lunet.ApiExample.Advanced.CheckedInteger right)`
- `Lunet.ApiExample.Advanced.CheckedInteger static op_CheckedAddition(Lunet.ApiExample.Advanced.CheckedInteger left, Lunet.ApiExample.Advanced.CheckedInteger right)`
- `Lunet.ApiExample.Advanced.CheckedInteger static op_UnsignedRightShift(Lunet.ApiExample.Advanced.CheckedInteger value, System.Int32 count)`

#### Properties

- `System.Int32 Value { get; }`
### `Lunet.ApiExample.Advanced.DiagnosticSource`

- Kind: `class`
- Interfaces: `Lunet.ApiExample.Advanced.IWithDefaultDiagnostics`, `System.IDisposable`

#### Constructors

- `DiagnosticSource()`

#### Methods

- `System.Void virtual Dispose()`
### `Lunet.ApiExample.Advanced.FeatureFlag`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IEquatable<Lunet.ApiExample.Advanced.FeatureFlag>`

#### Constructors

- `FeatureFlag(System.String Name, System.Boolean Enabled)`

#### Methods

- `System.Boolean static op_Equality(Lunet.ApiExample.Advanced.FeatureFlag left, Lunet.ApiExample.Advanced.FeatureFlag right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.Advanced.FeatureFlag left, Lunet.ApiExample.Advanced.FeatureFlag right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.Advanced.FeatureFlag other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.String Name, out System.Boolean Enabled)`

#### Properties

- `System.Boolean Enabled { get; set; }`
- `System.String Name { get; set; }`
### `Lunet.ApiExample.Advanced.IBufferConsumer<TBuffer>`

- Kind: `interface`

#### Methods

- `System.Void abstract Consume(TBuffer buffer)`
### `Lunet.ApiExample.Advanced.IStaticFactory<TSelf>`

- Kind: `interface`

#### Methods

- `TSelf static abstract Create(System.Int32 value)`

#### Properties

- `TSelf Empty { get; }`
### `Lunet.ApiExample.Advanced.IWithDefaultDiagnostics`

- Kind: `interface`

#### Methods

- `System.String virtual GetLabel()`
### `Lunet.ApiExample.Advanced.NativeInteropSurface`

- Kind: `class`

#### Constructors

- `NativeInteropSurface()`

#### Properties

- ` Callback { get; set; }`
- `System.IntPtr Handle { get; set; }`
### `Lunet.ApiExample.Advanced.PipelineStep<TInput, TOutput>`

- Kind: `class`
- Base: `System.MulticastDelegate`
- Interfaces: `System.ICloneable`, `System.Runtime.Serialization.ISerializable`

#### Constructors

- `PipelineStep(System.Object object, System.IntPtr method)`

#### Methods

- `System.IAsyncResult virtual BeginInvoke(TInput input, System.AsyncCallback callback, System.Object object)`
- `TOutput virtual EndInvoke(System.IAsyncResult result)`
- `TOutput virtual Invoke(TInput input)`
### `Lunet.ApiExample.Advanced.PrimaryClient`

- Kind: `class`

#### Constructors

- `PrimaryClient(System.String name, System.Uri endpoint)`

#### Properties

- `System.String Name { get; }`
- `System.Uri Endpoint { get; }`
### `Lunet.ApiExample.Advanced.RefSemanticsSurface`

- Kind: `class`

#### Constructors

- `RefSemanticsSurface()`

#### Methods

- `System.Char ParseFirst(System.ReadOnlySpan<System.Char> value)`
- `System.Int32 Sum(System.ReadOnlySpan<System.Int32> values)`
- `System.Int32& RefReadonlyReturn(ref System.Int32 value)`
### `Lunet.ApiExample.Advanced.RetryOptions`

- Kind: `struct`
- Base: `System.ValueType`

#### Constructors

- `RetryOptions(System.Int32 retryCount, System.TimeSpan timeout)`

#### Properties

- `System.Int32 RetryCount { get; }`
- `System.TimeSpan Timeout { get; }`
### `Lunet.ApiExample.Advanced.TupleHelpers`

- Kind: `static class`

#### Methods

- `System.ValueTuple<System.Byte, System.Byte, System.Byte> static SplitRgb(System.Int32 rgb)`
- `System.ValueTuple<System.String, T> static CreatePair<T>(System.String name, T value)`
- `System.ValueTuple<TKey, TValue> static AsTuple<TKey, TValue>(System.Collections.Generic.KeyValuePair<TKey, TValue> pair)`
### `Lunet.ApiExample.ApiClient`

- Kind: `class`
- Interfaces: `Lunet.ApiExample.IStaticFactory<Lunet.ApiExample.ApiClient>`

#### Constructors

- `ApiClient(System.String name)`

#### Methods

- `Lunet.ApiExample.ApiClient static CreateDefault()`
- `System.Void AddTag(System.String tag)`
- `TResponse Execute<TRequest, TResponse>(TRequest request, System.Func<TRequest, TResponse> handler)`

#### Properties

- `System.Collections.Generic.IReadOnlyList<System.String> Tags { get; }`
- `System.String BaseAddress { get; set; }`
- `System.String Name { get; }`

#### Events

- `System.EventHandler<Lunet.ApiExample.Severity> SeverityChanged`
### `Lunet.ApiExample.ApiClientExtensions`

- Kind: `static class`

#### Methods

- `System.Boolean static HasTag(Lunet.ApiExample.ApiClient client, System.String tag)`
- `System.String static ToDisplayName(Lunet.ApiExample.ApiUser user, Lunet.ApiExample.NameFormatter formatter)`
### `Lunet.ApiExample.ApiUser`

- Kind: `class`
- Interfaces: `System.IEquatable<Lunet.ApiExample.ApiUser>`

#### Constructors

- `ApiUser(System.String Id, System.String FirstName, System.String LastName)`

#### Methods

- `Lunet.ApiExample.ApiUser <Clone>$()`
- `System.Boolean static op_Equality(Lunet.ApiExample.ApiUser left, Lunet.ApiExample.ApiUser right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.ApiUser left, Lunet.ApiExample.ApiUser right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.ApiUser other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.String Id, out System.String FirstName, out System.String LastName)`

#### Properties

- `System.String FirstName { get; set; }`
- `System.String Id { get; set; }`
- `System.String LastName { get; set; }`
### `Lunet.ApiExample.ApiVersion`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IComparable<Lunet.ApiExample.ApiVersion>`, `System.IEquatable<Lunet.ApiExample.ApiVersion>`

#### Constructors

- `ApiVersion(System.Int32 major, System.Int32 minor)`

#### Methods

- `Lunet.ApiExample.ApiVersion static op_Addition(Lunet.ApiExample.ApiVersion left, Lunet.ApiExample.ApiVersion right)`
- `System.Boolean static op_GreaterThan(Lunet.ApiExample.ApiVersion left, Lunet.ApiExample.ApiVersion right)`
- `System.Boolean static op_LessThan(Lunet.ApiExample.ApiVersion left, Lunet.ApiExample.ApiVersion right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.ApiVersion other)`
- `System.Int32 virtual CompareTo(Lunet.ApiExample.ApiVersion other)`
- `System.String virtual ToString()`

#### Properties

- `System.Int32 Major { get; }`
- `System.Int32 Minor { get; }`
### `Lunet.ApiExample.DefaultImplementation`

- Kind: `class`
- Interfaces: `Lunet.ApiExample.IWithDefaultImplementation`

#### Constructors

- `DefaultImplementation()`
### `Lunet.ApiExample.Http.EndpointTimeout`

- Kind: `struct`
- Base: `System.ValueType`

#### Properties

- `System.Int32 ConnectTimeoutMilliseconds { get; set; }`
- `System.Int32 RequestTimeoutMilliseconds { get; set; }`
### `Lunet.ApiExample.Http.HttpEndpoint`

- Kind: `class`
- Interfaces: `Lunet.ApiExample.Http.IHttpEndpoint`

#### Constructors

- `HttpEndpoint(System.String route, Lunet.ApiExample.Http.HttpTransport transport)`

#### Methods

- `System.String virtual Invoke(Lunet.ApiExample.Http.HttpRequest request)`

#### Properties

- `Lunet.ApiExample.Http.EndpointTimeout Timeout { get; set; }`
- `Lunet.ApiExample.Http.HttpTransport Transport { get; }`
- `System.String Route { get; }`
### `Lunet.ApiExample.Http.HttpEndpointExtensions`

- Kind: `static class`

#### Methods

- `System.String static ToDisplayLabel(Lunet.ApiExample.Http.IHttpEndpoint endpoint)`
### `Lunet.ApiExample.Http.HttpRequest`

- Kind: `class`
- Interfaces: `System.IEquatable<Lunet.ApiExample.Http.HttpRequest>`

#### Constructors

- `HttpRequest(System.String Method, System.String Path)`

#### Methods

- `Lunet.ApiExample.Http.HttpRequest <Clone>$()`
- `System.Boolean static op_Equality(Lunet.ApiExample.Http.HttpRequest left, Lunet.ApiExample.Http.HttpRequest right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.Http.HttpRequest left, Lunet.ApiExample.Http.HttpRequest right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.Http.HttpRequest other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.String Method, out System.String Path)`

#### Properties

- `System.String Method { get; set; }`
- `System.String Path { get; set; }`
### `Lunet.ApiExample.Http.HttpTransport`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.ApiExample.Http.HttpTransport Http1`
- `const static Lunet.ApiExample.Http.HttpTransport Http2`
### `Lunet.ApiExample.Http.IHttpEndpoint`

- Kind: `interface`

#### Methods

- `System.String abstract Invoke(Lunet.ApiExample.Http.HttpRequest request)`

#### Properties

- `System.String Route { get; }`
### `Lunet.ApiExample.Http.RetrySettings`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IEquatable<Lunet.ApiExample.Http.RetrySettings>`

#### Constructors

- `RetrySettings(System.Int32 MaxAttempts, System.Int32 BackoffMilliseconds)`

#### Methods

- `System.Boolean static op_Equality(Lunet.ApiExample.Http.RetrySettings left, Lunet.ApiExample.Http.RetrySettings right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.Http.RetrySettings left, Lunet.ApiExample.Http.RetrySettings right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.Http.RetrySettings other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.Int32 MaxAttempts, out System.Int32 BackoffMilliseconds)`

#### Properties

- `System.Int32 BackoffMilliseconds { get; set; }`
- `System.Int32 MaxAttempts { get; set; }`
### `Lunet.ApiExample.IRepository<T>`

- Kind: `interface`

#### Methods

- `System.Collections.Generic.IEnumerable<T> abstract FindAll()`
- `T abstract FindById(System.String id)`
### `Lunet.ApiExample.IStaticFactory<TSelf>`

- Kind: `interface`

#### Methods

- `TSelf static abstract CreateDefault()`
### `Lunet.ApiExample.IWithDefaultImplementation`

- Kind: `interface`

#### Methods

- `System.String virtual Describe()`
### `Lunet.ApiExample.NameFormatter`

- Kind: `class`
- Base: `System.MulticastDelegate`
- Interfaces: `System.ICloneable`, `System.Runtime.Serialization.ISerializable`

#### Constructors

- `NameFormatter(System.Object object, System.IntPtr method)`

#### Methods

- `System.IAsyncResult virtual BeginInvoke(System.String firstName, System.String lastName, System.AsyncCallback callback, System.Object object)`
- `System.String virtual EndInvoke(System.IAsyncResult result)`
- `System.String virtual Invoke(System.String firstName, System.String lastName)`
### `Lunet.ApiExample.PageResult<T>`

- Kind: `struct`
- Base: `System.ValueType`
- Interfaces: `System.IEquatable<Lunet.ApiExample.PageResult<T>>`

#### Constructors

- `PageResult(System.Collections.Generic.IReadOnlyList<T> Items, System.Int32 TotalCount)`

#### Methods

- `System.Boolean static op_Equality(Lunet.ApiExample.PageResult<T> left, Lunet.ApiExample.PageResult<T> right)`
- `System.Boolean static op_Inequality(Lunet.ApiExample.PageResult<T> left, Lunet.ApiExample.PageResult<T> right)`
- `System.Boolean virtual Equals(Lunet.ApiExample.PageResult<T> other)`
- `System.Boolean virtual Equals(System.Object obj)`
- `System.Int32 virtual GetHashCode()`
- `System.String virtual ToString()`
- `System.Void Deconstruct(out System.Collections.Generic.IReadOnlyList<T> Items, out System.Int32 TotalCount)`

#### Properties

- `System.Collections.Generic.IReadOnlyList<T> Items { get; set; }`
- `System.Int32 TotalCount { get; set; }`
### `Lunet.ApiExample.Severity`

- Kind: `enum`
- Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`

#### Fields

- `System.Int32 value__`
- `const static Lunet.ApiExample.Severity Error`
- `const static Lunet.ApiExample.Severity Information`
- `const static Lunet.ApiExample.Severity Trace`
- `const static Lunet.ApiExample.Severity Warning`
