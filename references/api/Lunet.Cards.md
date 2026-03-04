# Lunet.Cards Public API

Assembly path: `src/Lunet.Cards/bin/Release/net10.0/Lunet.Cards.dll`

Exported types: **5**

## Types

### `Lunet.Cards.CardsBase`

- Kind: `abstract class`
- Base: `Lunet.Core.DynamicObject<Lunet.Cards.CardsPlugin>`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Properties

- `System.Boolean Enable { get; set; }`
- `System.String Description { get; set; }`
- `System.String Image { get; set; }`
- `System.String ImageAlt { get; set; }`
- `System.String Title { get; set; }`
### `Lunet.Cards.CardsModule`

- Kind: `class`
- Base: `Lunet.Core.SiteModule<Lunet.Cards.CardsPlugin>`

#### Constructors

- `CardsModule()`
### `Lunet.Cards.CardsPlugin`

- Kind: `class`
- Base: `Lunet.Core.SitePlugin`
- Interfaces: `Lunet.Core.ISitePlugin`, `Lunet.Core.ISitePluginCore`, `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `CardsPlugin(Lunet.Core.SiteObject site)`

#### Properties

- `Lunet.Cards.OgCards Og { get; }`
- `Lunet.Cards.TwitterCards Twitter { get; }`
### `Lunet.Cards.OgCards`

- Kind: `class`
- Base: `Lunet.Cards.CardsBase`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `OgCards(Lunet.Cards.CardsPlugin parent)`

#### Properties

- `System.String Locale { get; set; }`
- `System.String Type { get; set; }`
- `System.String Url { get; set; }`
### `Lunet.Cards.TwitterCards`

- Kind: `class`
- Base: `Lunet.Cards.CardsBase`
- Interfaces: `Scriban.Runtime.IScriptObject`, `System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.Generic.IDictionary<System.String, System.Object>`, `System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<System.String, System.Object>>`, `System.Collections.ICollection`, `System.Collections.IDictionary`, `System.Collections.IEnumerable`, `System.IFormattable`

#### Constructors

- `TwitterCards(Lunet.Cards.CardsPlugin parent)`

#### Properties

- `System.String Card { get; set; }`
- `System.String User { get; set; }`
