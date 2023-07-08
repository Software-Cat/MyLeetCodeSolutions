from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:

        shortestRedLast = [-1 for i in range(n)]
        shortestBlueLast = [-1 for i in range(n)]

        todo: deque[tuple[int, int, bool]] = deque([
            (0, 0, False),
            (0, 0, True)
        ])

        # For breadth first serach, the first time visiting is always the shortest.
        while len(todo) > 0:
            current = todo.pop()
            i = current[0]
            depth = current[1]
            redLast = current[2]

            if redLast:
                if shortestRedLast[i] == -1:  # Unvisited
                    shortestRedLast[i] = depth
                    for edge in blueEdges:
                        if edge[0] == i:
                            todo.appendleft((edge[1], depth + 1, False))
                # Already visited from red, do nothing
            if not redLast:
                if shortestBlueLast[i] == -1:  # Unvisited
                    shortestBlueLast[i] = depth
                    for edge in redEdges:
                        if edge[0] == i:
                            todo.appendleft((edge[1], depth + 1, True))
                # Already visited from blue, do nothing

        return [min(shortestRedLast[i],
                    shortestBlueLast[i],
                    key=lambda x: x if x >= 0 else 10**10)
                for i in range(n)]
