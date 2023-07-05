from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Key: complement value wanted, Value: the index
        map = {}

        for i, n in enumerate(nums):
            if n in map:
                return [map[n], i]
            else:
                map[target - n] = i
        return []
