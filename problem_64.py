from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for s in range(m+n-1):
            for row in range(m):
                col = s - row
                if 0 <= col < n:
                    if row == 0 and col == 0:
                        dp[row][col] = grid[row][col]
                    elif row == 0 and col != 0:
                        dp[row][col] = grid[row][col] + dp[row][col-1]
                    elif row != 0 and col == 0:
                        dp[row][col] = grid[row][col] + dp[row-1][col]
                    else:
                        dp[row][col] = grid[row][col] + \
                            min(dp[row-1][col], dp[row][col-1])

        return dp[m-1][n-1]
