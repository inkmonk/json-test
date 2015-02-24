from json_check import *
import unittest

class TestJsonCheck(unittest.TestCase):
    
    def setUp(self):
        print "Testing module json_check"

    def test_simple(self):
        """Test a simple un-nested object"""
        samp1 = JObject({'parent': None, 'keys': ['status', 'result']})
        j = json.loads('{"status": "success", "result": "yes"}')
        self.assertTrue(check_json_object(j, samp1))

if __name__ == '__main__':
    json_test = unittest.TestLoader().loadTestsFromTestCase(TestJsonCheck)
    testRunner = unittest.TextTestRunner()
    testRunner.run(json_test)




