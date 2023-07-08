
class Solution:

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        safeNodes = set()
        N = len(graph)
        color = [0 for i in range(N)]

        def dfs(start: int) -> bool:
            if color[start] != 0:
                return color[start] == 1

            color[start] = 2
            for out in graph[start]:
                if not dfs(out):
                    return False
            color[start] = 1

            return True

        for i in range(N):
            if dfs(i):
                safeNodes.add(i)

        return sorted(safeNodes)


Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])
