import unittest
from validate_functions import checkVictAge, checkVictSex
from stats_function import calcMedian, calcMean

class TestFunctions(unittest.TestCase):
    def testCheckVictAge(self):
        self.assertIsInstance(checkVictAge(), bool)

    def testCheckVictSex(self):
        self.assertIsInstance(checkVictSex(), bool)

    def testCalcMean(self):
        result = calcMean()
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def testCalcMedian(self):
        result = calcMedian()
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
