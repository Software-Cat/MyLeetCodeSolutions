class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # On each day, the price either goes up, down, or stays the same.
        # This creates a "mountain" shaped graph.
        # If we always buy at the valley of every mountain and sell at the peak of the next, profit is maximized
        profit = 0
        boughtAt = 0
        sellAt = 0
        i = 0
        l = len(prices) - 1

        while i < l:
            while i < l and prices[i + 1] <= prices[i]:
                # Descend down valley
                i += 1
            boughtAt = prices[i]

            while i < l and prices[i + 1] > prices[i]:
                # Travell up hill to top
                i += 1
            sellAt = prices[i]

            profit += sellAt - boughtAt
        return profit
