from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        total = 0

        neighbors: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for c in connections:
            neighbors[c[0]].append((c[1], 1))
            neighbors[c[1]].append((c[0], 0))

        def dfs(curr: int, parent: int):
            nonlocal total
            if not curr in neighbors:
                return
            for nei in neighbors[curr]:
                if nei[0] != parent:
                    total += nei[1]
                    dfs(nei[0], curr)

        dfs(0, -1)
        return total


print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
