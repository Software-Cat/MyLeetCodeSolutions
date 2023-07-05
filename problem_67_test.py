import unittest
from problem_67 import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual("100", sol.addBinary("11", "1"))
