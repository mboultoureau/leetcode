class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Optimization
        if source == target:
            return 0

        # Construct a graph with for each stop, a list of routeId
        graph = defaultdict(set)
        for routeIdx, route in enumerate(routes):
            for stop in route:
                graph[stop].add(routeIdx)


        cost = 0
        visited = set()
        queue = deque(graph[target])

        while queue:
            cost += 1

            for _ in range(len(queue)):
                busId = queue.popleft()
                visited.add(busId)

                if source in routes[busId]:
                    return cost

                for stop in routes[busId]:
                    for bus in graph[stop]:
                        if bus not in visited:
                            queue.append(bus)

        return -1