from typing import Dict, List


class Solution:

    def __init__(self) -> None:
        self.dp = {}

    def rob(self, houses: List[int]) -> int:
        N = len(houses)
        return max(self.maxMoney(houses, N-1), self.maxMoney(houses, N-2))

    def maxMoney(self, houses: List[int], n: int) -> int:
        """
        Max money gainable when index n is the latest robbed house
        """
        if n < 0:
            return 0
        if n <= 1:
            return houses[n]
        if n in self.dp:
            return self.dp[n]

        self.dp[n] = houses[n] + max(
            self.maxMoney(houses, n-2),
            self.maxMoney(houses, n-3)
        )
        return self.dp[n]
