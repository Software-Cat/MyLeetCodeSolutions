class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        visited = [False for room in rooms]

        def dfs(n: int) -> None:
            if not visited[n]:
                visited[n] = True
                for nextR in rooms[n]:
                    dfs(nextR)

        dfs(0)

        return all(visited)
