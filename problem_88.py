class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            nums1[:] = nums1[:-n]
        nums1.extend(nums2)
        nums1.sort()
