json-test
----------

A python library for assisting you in writing tests against a JSON
structure.

Usage:
------

Let's assume you have a JSON response like this:

````
{
  key1 : value1,
  key2 : { key3: value3 },
  key4 : [1,2,3],
  key5 : [{key6: value6, key7: value7}]
}

````

You have to represent it like this for testing:

````
key2 = JObject({parent: 'key2', keys: ['key3']})
key4 = JList({parent: 'key4', keys: None)
key5 = JList({parent: 'key5', keys: ['key6', 'key7]})
json_obj = JObject({parent: None, keys: ['key1', key2, key4, key5]})
````

Assumption:
-----------

* Right now it assumes that if an list has JSON objects then it
  maintains the same structure.

