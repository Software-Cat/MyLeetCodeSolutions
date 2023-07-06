

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        dp = [[0 for i in s] for i in s]

        for l in range(len(s)):
            for i, j in zip(range(len(s)), range(len(s))[l:]):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        for row in dp:
            print(row)

        return dp[0][len(s) - 1]


Solution().longestPalindromeSubseq("bbbab")
