class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # With Neetcode video: https://www.youtube.com/watch?v=wQGQnyv_9hI
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edges_count = {}
        leaves = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edges_count[src] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbor in adj[node]:
                    edges_count[neighbor] -= 1
                    if edges_count[neighbor] == 1:
                        leaves.append(neighbor)
