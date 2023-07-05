from collections import defaultdict
from typing import Dict


class Solution:

    mem: Dict[int, int] = defaultdict()

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n in self.mem:
            return self.mem[n]
        res: int = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.mem[n] = res
        return res
