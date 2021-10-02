## Why the name?
I really don't like naming my projects, so I just take the inspiration from my other library [ragdoll](https://github.com/rabbit-aaron/ragdoll). (I have 2 cats :D).

## Introduction
JSON processing is easy enough in python, but sometimes it is tedious to handle optional keys when accessing nested JSON like this one, assuming `settings.database.options` is optional.

```json
{
  "settings": {
    "database": {
      "type": "PostgreSQL",
      "options": {
        "arguments": {
          "user": "meow"
        }
      }
    }
  }
}
```
Without shorthair:
```python
try:
    user = obj["settings"]["database"]["options"]["arguments"]["user"]
except KeyError:
    user = _default_user
```

With shorthair:

```python
    # obj decoded using shorthair.json.load(s) or through shorthair.LookupProxy 
    user = obj["settings"]["database"]["options"]["arguments"]["user"]() or _default_user
```

## Usage

### Decoding json

Shorthair provides the `load` and `loads` shortcut functions to parse JSON and return the LookupProxy object.

```python
from shorthair import json

obj = json.loads("""{}""")

with open("myfile.json") as jsonfile:
    obj = json.load(jsonfile)
```

### Using the `LookupProxy`

If in your code you have a dictionary/list that's already decoded, you can wrap it with the LookupProxy

```python
from shorthair import LookupProxy

obj = LookupProxy({})
```

### Finalising the lookup

You need to either call (using `()`) the proxy or access its property `.value` to retrieve the value of the lookup, it will return the value or None if key doesn't exist.

```python
from shorthair import LookupProxy

obj = LookupProxy({
    "a": {
        "b": {
            "c": "d"
        }
    }
})

>>> obj["a"]["b"]["c"].value
'd'

# shortcut for `.value`
>>> obj["a"]["b"]["c"]()
'd'

>>> obj["x"]["y"][3][4]["z"].value is None
True

>>> obj["x"]["y"][3][4]["z"]() is None
True
```
