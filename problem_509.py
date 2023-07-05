from collections import defaultdict


class Solution:

    mem = defaultdict()

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        ret = self.fib(n-1) + self.fib(n-2)
        self.mem[n] = ret
        return ret
