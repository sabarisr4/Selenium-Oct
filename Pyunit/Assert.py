
import unittest

class Test(unittest.TestCase):

    def test_a(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(4, 1)
        self.assertTrue(3>1,"Error")
        self.assertFalse(3>4,"Error")

        self.assertIn(3,[1,2,3], "Error")
        self.assertNotIn(4,[1,2,3], "Error")
        a=4
        b=5
        self.assertIs(a,b)
        #self.assertIsNot(a,b,"Error are the same")

        self.assertListEqual([1,2,3],[1,2,3])
        self.assertTupleEqual((1,2,3),(1,2,3))
        self.assertSetEqual({1,2,3},{1,2,3})
        self.assertDictEqual({1:"one"},{1:"one"})


