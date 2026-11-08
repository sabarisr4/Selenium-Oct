"""
create the class

create the test case

run only on the alphabetical order

call main method
"""

import unittest

class Test(unittest.TestCase):

    def test_a(self):
         print("test1")

    @unittest.skipIf(2 > 1, "skip")
    def test_b(self):
        print("test2")

    def test_d(self):
        print("test_2")

    @unittest.skip("skip")
    def test_z(self):
        print("test_3")

if __name__ == "__main__":
    unittest.main()
