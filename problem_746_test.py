import unittest
from problem_746 import Solution


class SolutionTest(unittest.TestCase):
    def test_main(self):
        sol = Solution()
        self.assertEqual(6, sol.minCostClimbingStairs(
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
