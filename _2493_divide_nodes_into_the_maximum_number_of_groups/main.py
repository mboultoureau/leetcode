class Solution:

    def getLinkedNodes(self, graph: Dict[int, set[int]], nodes: set[int], source: int):
        nodes.add(source)
        for neighbor in graph[source]:
            if neighbor in nodes:
                continue

            nodes.union(self.getLinkedNodes(graph, nodes, neighbor))

        return nodes

    def bfs(self, graph: Dict[int, set[int]], source: int):
        # visited = set([])
        queue = deque([(source, 1)])
        distance = {
            source: 1
        }

        while queue:
            node, group = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in distance:
                    if distance[neighbor] == group:
                        return -1
                    continue

                queue.append((neighbor, group + 1))
                distance[neighbor] = group + 1

        return max(distance.values())


    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacent list
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Get linked nodes
        linked_nodes = []
        visited = set()
        for node in range(1, n + 1):
            if node in visited:
                continue

            linked = self.getLinkedNodes(graph, set(), node)
            linked_nodes.append(linked)
            visited = visited.union(linked)

        # Get max for each layer
        total = 0
        for link in linked_nodes:
            maximum = -1
            for node in link:
                maximum = max(maximum, self.bfs(graph, node))

            if maximum == -1:
                return -1

            total += maximum

        return total