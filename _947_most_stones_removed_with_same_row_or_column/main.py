class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adjacency = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency[i].append(j)
                    adjacency[j].append(i)

        result = 0
        visited = [False for _ in range(n)]

        def dfs(i):
            if visited[i]:
                return

            visited[i] = True
            for adjacent in adjacency[i]:
                dfs(adjacent)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1

        return n - result