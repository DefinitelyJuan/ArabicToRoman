from arabictoroman import isInteger
import unittest


class intValTest (unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(isInteger(""),False)