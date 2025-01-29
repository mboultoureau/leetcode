class Solution:
    def has_cycle(self, current, previous, graph, visited):
        # Check neighbor
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor != previous and (neighbor in visited or self.has_cycle(neighbor, current, graph, visited)) :
                return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

            if self.has_cycle(a, 0, graph, set()):
                return [a, b]