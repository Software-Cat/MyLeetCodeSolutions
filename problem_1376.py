class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:

        subordinates: list[list[int]] = [[] for i in range(n)]
        for currentPerson, currentManager in enumerate(manager):
            if currentManager != -1:
                subordinates[currentManager].append(currentPerson)
        del manager

        print(subordinates)

        longest = 0

        def dfs(i: int, existingDelay: int):
            nonlocal longest
            longest = max(longest, existingDelay)
            for sub in subordinates[i]:
                dfs(sub, existingDelay + informTime[i])

        dfs(headID, 0)

        return longest


Solution().numOfMinutes(n=6, headID=2, manager=[
    2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0])
