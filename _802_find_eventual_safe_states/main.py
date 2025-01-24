class Solution:
    def dfs(self, node, graph, visited, path):
        if node in path:
            return True

        if node in visited:
            return False

        path.add(node)
        visited.add(node)

        for neighbor in graph[node]:
            if self.dfs(neighbor, graph, visited, path):
                return True

        path.remove(node)
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        visited = set()
        path = set()

        for i in range(N):
            self.dfs(i, graph, visited, path)

        safes = []
        for i in range(N):
            if i not in path:
                safes.append(i)

        return safes