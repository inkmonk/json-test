class JsonTestException(ValueError):
    '''
    Custom class for exception
    '''

class JValue:

    def __init__(self, jvalue):
        self.jvalue = jvalue

    def get(self):
        return self.jvalue

class JList:

    def __init__(self, jlist):
        self.jlist = self.validate_jlist(jlist)

    def validate_jlist(self, data):
        keys = data.keys()
        if not ('parent' in keys and 'keys' in keys):
            raise JsonTestException('Invalid JList construction')
        else:
            return data
        
    def get(self):
        return self.jlist

class JObject:
    """
    JObject should be built using a dictionary with the parameter keys
    {parent: None, keys: []}. The keys parameter will contain the
    object keys in it. In case it is an nested object it will contain
    a new JObject inside it.
    """

    def __init__(self, jobject):
        self.jobject = jobject

    def get(self):
        return self.jobject


