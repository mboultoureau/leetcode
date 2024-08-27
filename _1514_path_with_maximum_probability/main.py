class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        newEdges = defaultdict(list)
        for i in range(len(edges)):
            start, end = edges[i]
            probability = succProb[i]

            newEdges[start].append((end, probability))
            newEdges[end].append((start, probability))

        visited = set()

        distances = [0 for _ in range(n)]
        distances[start_node] = 1
        
        heap = []
        heapq.heappush(heap, (-1, start_node))

        while heap:
            (distance, current) = heapq.heappop(heap)
            if current in visited:
                continue

            visited.add(current)

            for destination, probability in newEdges[current]:
                newDistance = probability * (-distance)
                if newDistance > distances[destination]:
                    distances[destination] = newDistance
                    heapq.heappush(heap, (-newDistance, destination))

        return distances[end_node]