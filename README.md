json-test
----------

A python library for assisting you in writing tests against a JSON
structure. The library concentrates on the shape of the JSON structure
rather than the actual content in it.

Pre-requisite
--------------

What you need to know for using the library?

There are two classes `JObject` and `JList` which are used to
represent Objects and list in JSON.

Let's assume you have a JSON object like this:

````
{
  "name" : "Joe",
  "age" : 12
}

````
You have to represent them using `JObject` like this:

````
person = JObject({parent = None, keys=['name', 'age']})
````

Note how the `parent` is `None` there. In case of a nested JSON, we
will use the `parent` key. Example:
````
{
  "name" : "Joe",
  "age" : {
            "year" : 24,
            "days" : 174
          }
}

````
will be represented like this:
````
age = JObject({parent = "age", keys=['year','days']})
person = JObject({parent = None, keys = ['name', age]})

````

Quick Start
------------
````
from json_check import *

json_string = """
{
  "name" : "Joe",
  "age" : 24
}
"""
json_obj = JObject({parent=None, keys=['name','age']})

check_json(json_string, json_obj) # This predicate will return True
````

