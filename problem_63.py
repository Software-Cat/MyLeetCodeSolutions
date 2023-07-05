from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for item in row] for row in obstacleGrid]

        for i, row in enumerate(obstacleGrid):
            for j, col in enumerate(row):
                if obstacleGrid[i][j] == 1:  # Blocked
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[-1][-1]
