class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(0, n - 1):
            graph[i].append(i + 1)

        result = []

        for query in queries:
            c1, c2 = query
            graph[c1].append(c2)
            result.append(self.bfs(graph, n))

        return result


    def bfs(self, graph, n):
        distances = [float("inf") for _ in range(n)]
        distances[0] = 0

        heap = [(0, 0)]

        print(heap)


        while heap:
            distance, node = heapq.heappop(heap)

            for vertex in graph[node]:
                if distances[vertex] > distances[node] + 1:
                    distances[vertex] = distances[node] + 1
                    heapq.heappush(heap, (distances[vertex], vertex))


        return distances[n - 1]
