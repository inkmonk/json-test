from jvalue import JList, JObject
import json

def check_json(json_string, json_structure):
    """
    json_string: String representing the json
    json_structure: A value representing JSON schema.
    """
    js = json.loads(json_string)
    # if ()

def check_json_object(json_obj, json_structure):
    """
    json_obj: Dictionary representing JSON
    json_structure: A value representing JSON schema
    """
    if (isinstance(json_structure, JObject)):
        keys = json_structure.get_keys()
        original_keys = json_obj.keys()
        print 'keys', keys, 'okeys', original_keys
        keys.sort()
        original_keys.sort()
        if (keys == original_keys):
            return True
        else:
            key_objs = filter(lambda x: isinstance(x, JObject), keys)
            key_lists = filter(lambda x: isinstance(x, JList), keys)
            parent_objs = map(lambda x: x.parent, key_objs)
            parent_list = map(lambda x: x.parent, key_lists)
            old_keys = filter(lambda x:  (not isinstance(x, JObject)) and (not isinstance(x, JList)), keys)
            base_keys = old_keys + parent_objs + parent_list
            original_keys.sort()
            base_keys.sort()
            if not (original_keys == base_keys):
                return False
            else:
                obj_eval = all(map(lambda x: check_json_object(json_obj[x.parent], x), key_objs))
                return obj_eval
    else:
        return False


# key2 = JObject({parent: 'key2', keys: ['key3']})
# key4 = JList({parent: 'key4', keys: None)
# key5 = JList({parent: 'key5', keys: ['key6', 'key7]})
# json_obj = JObject({parent: None, keys: ['key1', key2, key4, key5]})
