

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N: int = len(isConnected)
        visited = [False] * N
        total = 0

        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j, isConnectedToJ in enumerate(isConnected[i]):
                if isConnectedToJ:
                    dfs(j)

        for i in range(N):
            if not visited[i]:
                dfs(i)
                total += 1

        return total


class SolutionSlow:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces = []
        N = len(isConnected[0])

        for i in range(N):
            if i in (c for p in provinces for c in p):
                continue

            currentProv = []
            todo = [i]
            while len(todo) > 0:
                currentTask = todo.pop()
                currentProv.append(currentTask)
                newCities = [j for j in range(
                    N) if isConnected[currentTask][j] and (not j in currentProv)]
                todo.extend(newCities)

            provinces.append(currentProv)

        return len(provinces)
