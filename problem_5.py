

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp: list[dict[tuple[int, int], str]] = [{} for i in range(len(s))]

        # Trivial palindromes
        for i, c in enumerate(s):
            dp[0][(i, i)] = c
        for i, cur, nxt in zip(range(len(s)), s, s[1:]):
            if cur == nxt:
                dp[1][(i, i+1)] = cur + nxt

        # Expand
        for i in range(2, len(s)):
            for k, v in dp[i-2].items():
                if k[0] > 0 and k[1] < len(s) - 1 and s[k[0] - 1] == s[k[1] + 1]:
                    dp[i][(k[0] - 1, k[1] + 1)] = s[k[0] - 1] + v + s[k[1] + 1]

        for item in reversed(dp):
            if item != {}:
                return list(item.values())[0]
        return ""
