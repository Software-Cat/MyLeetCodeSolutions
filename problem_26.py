class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = set(nums)
        nums[:] = sorted(list(unique))
        return len(nums)
