json-test
----------

A python library for assisting you in writing tests against a JSON
structure. The library concentrates on the shape of the JSON structure
rather than the actual content in it.

Pre-requisite
--------------

What you need to know for using the library?

There are two classes `JObject` and `JList` which are used to
represent Objects and list of JSON.

Let's assume you have a JSON object like this:

````
{
  "name" : "Joe",
  "age" : 12
}
````
You have to represent them using `JObject` like this:

````
person = JObject(keys=['name', 'age'])
````
Or
````
person = JObject(['name', 'age'])
````

Example for a Nested Object in JSON:
````
{
  "name" : "Joe",
  "age" : {
            "year" : 24,
            "days" : 174
          }
}
````
which will be represented like this:
````
age = JObject(parent = "age", keys=['year','days'])
person = JObject(keys = ['name', age])
````

Quick Start
------------
````
from json_test import *

json_string = """
{
  "name" : "Joe",
  "age" : 24
}
"""
json_obj = JObject(['name','age'])

check_json(json_string, json_obj) # This predicate will return True
````

For more working examples see `test.py`.
