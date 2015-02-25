class JList:
    """
    Represents JSON list
    """

    def __init__(self, keys, parent = None):
        self.parent = parent
        self.keys = keys

    def get_keys(self):
        return self.keys


class JObject:
    """
    Represents JSON Object
    """

    def __init__(self, keys, parent = None):
        self.parent = parent
        self.keys = keys

    def get_keys(self):
        return self.keys
    



