from math import ceil


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        tot = ceil(diff / 2.0)
        if low % 2 == 1 and high % 2 == 1:
            tot += 1
        return tot
