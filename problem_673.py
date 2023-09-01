class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        N = len(nums)
        length: list[int] = [1] * N
        count: list[int] = [1] * N

        for currentLastInd in range(len(nums)):
            for beforeInd in range(currentLastInd):
                if nums[beforeInd] < nums[currentLastInd]:
                    # Found possible extension to subsequence
                    if length[beforeInd] + 1 > length[currentLastInd]:
                        # Found longer possibility, reject previous possibilities as too short
                        length[currentLastInd] = length[beforeInd] + 1
                        count[currentLastInd] = 0
                    elif length[beforeInd] + 1 == length[currentLastInd]:
                        # Found new possibility of same length, add to count
                        count[currentLastInd] += count[beforeInd]

        maxLen = max(length)
        total = 0
        for i, leng in enumerate(length):
            if leng == maxLen:
                total += count[i]

        return total


Solution().findNumberOfLIS(nums=[1, 3, 5, 4, 7])
