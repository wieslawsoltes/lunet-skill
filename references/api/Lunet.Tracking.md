# Lunet.Tracking Public API

Assembly path: `src/Lunet.Tracking/bin/Release/net10.0/Lunet.Tracking.dll`

Exported types: **4**

## Types

### `Lunet.Tracking.AnalyticsObject`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Tracking.AnalyticsPlugin>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `AnalyticsObject(Lunet.Tracking.AnalyticsPlugin parent)`
### `Lunet.Tracking.AnalyticsPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `AnalyticsPlugin(Lunet.Core.SiteObject site)`
### `Lunet.Tracking.GoogleAnalytics`

- Kind: `class`
- Base: `Lunet.Core.DynamicObject<Lunet.Tracking.AnalyticsObject>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `GoogleAnalytics(Lunet.Tracking.AnalyticsObject parent)`
### `Lunet.Tracking.TrackingModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Tracking.AnalyticsPlugin>`

#### Constructors

- `TrackingModule()`
