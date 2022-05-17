from arabictoroman import getRoman
import unittest


class conversionTest (unittest.TestCase):
    def testRange(self):
        self.assertEqual(getRoman(4000),"MMMM")
        self.assertEqual(getRoman(0),"")
    def testProperties(self):
        self.assertEqual(getRoman(4),"IV")
        self.assertEqual(getRoman(9),"IX")
        self.assertEqual(getRoman(12),"XII")
        self.assertEqual(getRoman(19),"XIX")
        self.assertEqual(getRoman(2356),"MMCCCLVI")

