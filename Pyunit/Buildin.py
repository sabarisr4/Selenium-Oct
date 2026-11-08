

"""
setupclass:only once before all the test cases started execution
tear down class:only once after all the test cases execution

setup:run before every test case
teardown:run after every test case

setupclass
  setup tc1 teardown
  setup tc2 teardown
  setup tc3 teardown
  setup tc4 teardown

tear down class

"""
import unittest

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("before all test cases")
    @classmethod
    def tearDownClass(self):
        print("after all test cases")


    def setUp(self):
        print("before each test case")

    def tearDown(self):
        print("after each test case")


    def test_1(self):
        print("test case 1")

    def test_2(self):
        print("test case 2")

if __name__ == '__main__':
    unittest.main()
