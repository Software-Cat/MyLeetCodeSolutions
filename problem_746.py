from typing import Dict, List


class Solution:

    def __init__(self) -> None:
        self.dp: Dict[int, int]

    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n = len(costs)
        self.dp = {}
        return min(self.costToNRecursive(costs, n - 1), self.costToNRecursive(costs, n - 2))

    def costToNRecursive(self, costs: List[int], n) -> int:
        if n <= 1:
            return costs[n]
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = costs[n] + \
            min(self.costToNRecursive(costs, n-1),
                self.costToNRecursive(costs, n-2))
        return self.dp[n]
