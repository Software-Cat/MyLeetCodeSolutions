class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # Map stores the index of previously seen letters + 1, so that when the letter repeats,
        # the cached index is retrieved and set as the left bound (i) to ensure no repetition.
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        currentMax = 0
        for startingIndex, startingLetter in enumerate(s):
            seenLetters = [startingLetter]
            currentCounting = 1
            for extraLetter in s[startingIndex + 1:]:
                if not extraLetter in seenLetters:
                    seenLetters.append(extraLetter)
                    currentCounting += 1
                else:
                    break
            if currentCounting > currentMax:
                currentMax = currentCounting
        return currentMax
