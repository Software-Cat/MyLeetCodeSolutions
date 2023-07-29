class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxProf = 0

        while r < len(prices):
            curr = prices[r] - prices[l]
            if curr < 0:
                l = r
            else:
                maxProf = max(maxProf, curr)
            r += 1

        return maxProf
