class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cities = [0 for _ in range(n)]
        graph = defaultdict(set)

        for src, dst, length in edges:
            graph[src].add((dst, length))
            graph[dst].add((src, length))

        # Dijsktra on each node
        for src in range(n):
            visited = set()
            distances = [float("inf") for _ in range(n)]
            distances[src] = 0
            next_node = (src, 0)

            while next_node[0] != -1:
                src, length = next_node
                visited.add(src)

                # Update distances
                for dst, dst_length in graph[src]:
                    if length + dst_length <= distanceThreshold:
                        distances[dst] = min(distances[dst], length + dst_length)

                # Check next node
                next_node = (-1, float("inf"))
                for i in range(len(distances)):
                    if i in visited:
                        continue

                    if next_node[1] > distances[i]:
                        next_node = (i, distances[i])

            for i in range(len(distances)):
                if distances[i] != float('inf'):
                    cities[i] += 1

        index = -1
        minimum = float('inf')
        for i in range(len(cities)):
            if cities[i] <= minimum:
                index = i
                minimum = cities[i]

        return index


                    

