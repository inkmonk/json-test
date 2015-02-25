from json_check import *
import unittest

class TestJsonCheck(unittest.TestCase):
    
    def test_simple(self):
        """Test a simple un-nested object"""
        samp1 = JObject(keys = ['status', 'result'])
        j = json.loads('{"status": "success", "result": "yes"}')
        self.assertTrue(check_json_object(j, samp1))

    def test_simplef(self):
        """Test a simple un-nested object"""
        samp1 = JObject(keys = ['status', 'result'])
        j = json.loads('{"status": "success", "resultd": "yes"}')
        self.assertFalse(check_json_object(j, samp1))

    def test_nested_obj(self):
        """Tests a nested json object"""
        jobj = JObject(keys = ['status', JObject(parent = 'nest', keys= ['a','b']), 
                               'result'])
        jdic = json.loads('{"status": "success", "result": "yes", "nest": {"a":1,"b":2}}')
        self.assertTrue(check_json_object(jdic, jobj))

    def test_nested_objf(self):
        """Tests a nested json object"""
        jobj = JObject(keys = ['status', JObject(parent = 'nest', keys= ['a','b']), 
                               'result'])
        jdic = json.loads('{"status": "success", "result": "yes", "nest": {"a":1,"bc":2}}')
        self.assertFalse(check_json_object(jdic, jobj))

    def test_list(self):
        """Tests a simple list"""
        jobj = JList(parent = 'some', keys = [])
        jdic = json.loads('[]')
        self.assertTrue(check_json_array(jdic, jobj))

    def test_listf(self):
        """Tests a simple list"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[]')
        self.assertFalse(check_json_array(jdic, jobj))

    def test_list_2(self):
        """Tests a list with object"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[{"test1":3, "test2":4}]')
        self.assertTrue(check_json_array(jdic, jobj))

    def test_list_2f(self):
        """Tests a list with object"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[{"test1":3, "test9":4}]')
        self.assertFalse(check_json_array(jdic, jobj))

    def test_list_3(self):
        """Tests a list with object"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[{"test1":3, "test2":4},{"test1":3, "test2":4}]')
        self.assertFalse(check_json_array(jdic, jobj))

    def test_list_4(self):
        """Tests a list with object"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2']),
                                              JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[{"test1":3, "test2":4},{"test1":3, "test2":4}]')
        self.assertTrue(check_json_array(jdic, jobj))

    def test_list_4f(self):
        """Tests a list with object"""
        jobj = JList(parent = 'some', keys = [JObject(parent = None, keys = ['test1', 'test2']),
                                              JObject(parent = None, keys = ['test1', 'test2'])])
        jdic = json.loads('[{"test1":3, "test2":4},{"test1":3, "test23":4}]')
        self.assertFalse(check_json_array(jdic, jobj))

if __name__ == '__main__':
    json_test = unittest.TestLoader().loadTestsFromTestCase(TestJsonCheck)
    testRunner = unittest.TextTestRunner()
    testRunner.run(json_test)




