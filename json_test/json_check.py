from jvalue import JList, JObject
import json

def check_json(json_string, json_structure):
    """
    json_string: String representing the json
    json_structure: A value representing JSON schema.
    """
    js = json.loads(json_string)
    return check_json_object(js, json_structure)

def check_json_object(json_obj, json_structure):
    """
    json_obj: Dictionary representing JSON
    json_structure: (Type: JObject) A value representing JSON schema
    """
    if (isinstance(json_structure, JObject)):
        keys = json_structure.get_keys()
        original_keys = json_obj.keys()
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
                list_eval = all(map(lambda x: check_json_array(json_obj[x.parent], x), key_lists))
                return obj_eval and list_eval
    else:
        return False

def check_json_array(json_obj, json_structure):
    """
    json_obj: A list (which is a sub-part of JSON)
    json_structure: (Type JList) represents the sub part of the 
    JSON.
    """
    if (isinstance(json_structure, JList)):
        objs_stru = filter(lambda x: isinstance(x, JObject), json_structure.get_keys())
        objs_json = filter(lambda x: isinstance(x, dict), json_obj)
        if not (len(objs_stru) == len(objs_json)):
            return False
        else:
            zip_json = zip(objs_json, objs_stru)
            obj_eval = all(map(lambda x: check_json_object(x[0], x[1]), zip_json))
            return obj_eval
    else:
        return False
