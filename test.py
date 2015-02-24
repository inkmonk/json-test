from json_check import *
import unittest

class TestJsonCheck(unittest.TestCase):
    
    def test_simple(self):
        """Test a simple un-nested object"""
        samp1 = JObject({'parent': None, 'keys': ['status', 'result']})
        j = json.loads('{"status": "success", "result": "yes"}')
        self.assertTrue(check_json_object(j, samp1))

    def test_simplef(self):
        """Test a simple un-nested object"""
        samp1 = JObject({'parent': None, 'keys': ['status', 'result']})
        j = json.loads('{"status": "success", "resultd": "yes"}')
        self.assertFalse(check_json_object(j, samp1))

    def test_nested_obj(self):
        """Tests a nested json object"""
        jobj = JObject({'parent': None, 'keys': ['status', JObject({'parent': 'nest', 'keys': ['a','b']}), 
                                                  'result']})
        jdic = json.loads('{"status": "success", "result": "yes", "nest": {"a":1,"b":2}}')
        self.assertTrue(check_json_object(jdic, jobj))

    def test_nested_objf(self):
        """Tests a nested json object"""
        jobj = JObject({'parent': None, 'keys': ['status', JObject({'parent': 'nest', 'keys': ['a','b']}), 
                                                  'result']})
        jdic = json.loads('{"status": "success", "result": "yes", "nest": {"a":1,"bc":2}}')
        self.assertFalse(check_json_object(jdic, jobj))

    def test_list(self):
        """Tests a simple list"""
        jobj = JList({'parent': 'some', 'keys': []})
        jdic = json.loads('[]')
        self.assertTrue(check_json_array(jdic, jobj))

if __name__ == '__main__':
    json_test = unittest.TestLoader().loadTestsFromTestCase(TestJsonCheck)
    testRunner = unittest.TextTestRunner()
    testRunner.run(json_test)




