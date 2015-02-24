json-test
----------

A python library for assisting you in writing tests against a JSON
structure. The library concentrates on the shape of the JSON structure
rather than the actual content of it.

Usage:
------

Let's assume you have a JSON response like this:

````
{
  key2 : { key3: value3 },
  key4 : [1,2,3],
  key5 : [{key6: value6, key7: value7}]
}

````

Now before writing the test, you have to write a Schema for that JSON.
Each key can be represented like this:

````
key2 = JObject({parent: 'key2', keys: ['key3']})  # Note that we
ignore the value3 since we only concentrate on the shape of the JSON.
key4 = JList({parent: 'key4', keys: None) # keys is None here because
the List doesn't have objects here
key5 = JList({parent: 'key5', keys: ['key6', 'key7]})
````

And the complete object will be represented like this:

````
json_obj = JObject({parent: None, keys: ['key1', key2, key4, key5]})
````

Now, the file `json_check.py` will import the predicate functions
which will help you in running the tests:

````
from json_check import *

json_string = """
{
  key2 : { key3: value3 },
  key4 : [1,2,3],
  key5 : [{key6: value6, key7: value7}]
  }"""

check_json(json_string, json_obj) # This predicate will return True
````

Assumption:
-----------

* Right now it assumes that if an list has JSON objects then it
  maintains the same structure.

