import unittest
from problem_3 import Solution


class SolutionTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))

    def test2(self):
        sol = Solution()
        self.assertEqual(1, sol.lengthOfLongestSubstring("bbbbb"))

    def test3(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))
