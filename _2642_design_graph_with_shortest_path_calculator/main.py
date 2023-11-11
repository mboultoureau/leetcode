class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))
    
    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, current = heapq.heappop(heap)

            if current in visited:
                continue

            if current == node2:
                return cost

            if current in self.graph:
                for neighbor, edge_cost in self.graph[current]:
                    heapq.heappush(heap, (cost + edge_cost, neighbor))

            visited.add(current)

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)