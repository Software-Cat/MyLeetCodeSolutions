

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp: list[bool] = [False for i in s]

        for i in range(len(s)):
            for w in wordDict:
                if i < len(w) - 1:
                    continue

                if i == len(w) - 1 or dp[i - len(w)]:
                    if s[:i+1].endswith(w):
                        dp[i] = True
                        break

        return dp[-1]
