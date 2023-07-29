from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]
