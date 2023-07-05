from collections import Counter, defaultdict
from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        # Produces a dictionary counting the number of occurrences of each num
        buckets = Counter(nums)

        dp = defaultdict(int)

        for i in range(max(buckets.keys()) + 1):
            # We are up to the value i, we know the best solution when we take up to the i-1th bucket but also MUST take the i-1th bucket
            # We also know the best solution when we take up to the i-2th bucket and hence MUST NOT have taken the i-1th bucket

            if i in buckets.keys():
                # If the bucket with value i actually exists, we decide on it
                dp[i] = max(dp[i-2] + i * buckets[i], dp[i-1])
            else:
                # If the bucket doesn't exist, then we can't gain any value and it is just the previous
                dp[i] = dp[i-1]

        return dp[max(buckets.keys())]
