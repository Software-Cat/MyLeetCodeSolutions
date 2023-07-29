class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [n for n in nums if n != val]
        return len(nums)
