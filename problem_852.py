class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        i, j = 0, len(arr) - 1
        while i < j:
            median = (i + j) // 2
            if arr[median] < arr[median + 1]:
                i = median + 1
            else:
                j = median
        return i
