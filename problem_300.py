class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Subproblem: what is the length of the longest subsequence formed between indices (i, j)
        # Also store min and max

        dp = [1 for i in nums]

        for j, _ in enumerate(nums):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
