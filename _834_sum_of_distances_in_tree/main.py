class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # With solution help
        nodes = defaultdict(list)
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        count = [1 for _ in range(n)]
        result = [0 for _ in range(n)]

        def dfs(root, parent):
            for child in nodes[root]:
                if child != parent:
                    dfs(child, root)
                    count[root] += count[child]
                    result[root] += result[child] + count[child]


        def dfs2(root, parent):
            for child in nodes[root]:
                if child != parent:
                    result[child] = result[root] - count[child] + (n - count[child])
                    dfs2(child, root)

        dfs(0, -1)
        dfs2(0, -1)

        return result