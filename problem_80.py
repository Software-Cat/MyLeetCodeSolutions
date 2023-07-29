from collections import Counter


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            c[k] = min(v, 2)
        nums[:] = [k for k, v in c.items() for i in range(v)]
        return len(nums)
