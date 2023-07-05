import unittest
from problem_1523 import Solution


class SolutionTest(unittest.TestCase):
    def testOdd(self):
        sol = Solution()
        self.assertEqual(3, sol.countOdds(3, 7))

    def testEven(self):
        sol = Solution()
        self.assertEqual(1, sol.countOdds(8, 10))
