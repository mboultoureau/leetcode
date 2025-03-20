class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Build graph
        graph = defaultdict(list)
        for src, dst, wgt in edges:
            graph[src].append((dst, wgt))
            graph[dst].append((src, wgt))

        # Explore groups
        visited = set()
        nodes = {} # each node has (group_id, cost)
        groupId = 0

        for i in range(n):
            if i in visited:
                continue

            nodesInGroup = set()
            cost = 2**32 - 1
            queue = deque([i])

            while len(queue) > 0:
                # Handle visited and dstFound
                start = queue.popleft()
                if start in nodesInGroup:
                    continue

                nodesInGroup.add(start)

                # Explore all weights
                for end, weight in graph[start]:
                    cost &= weight
                    queue.append(end)

            for node in nodesInGroup:
                visited.add(node)
                nodes[node] = (groupId, cost)

            groupId += 1

        # Calculate queries
        costs = []

        for src, dst in query:
            if nodes[src][0] != nodes[dst][0]:
                costs.append(-1)
            else:
                costs.append(nodes[src][1])

        return costs





    ## TOO SLOW
    # def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    #     # Build graph
    #     graph = defaultdict(list)
    #     for src, dst, wgt in edges:
    #         graph[src].append((dst, wgt))
    #         graph[dst].append((src, wgt))

    #     costs = []
    #     for src, dst in query:
    #         costs.append(self.queryCost(graph, src, dst))

    #     return costs

    # def queryCost(self, graph: dict[int], src: int, dst: int) -> int:
    #     visited = set()
    #     queue = deque([src])
    #     cost = 2**32 - 1
    #     dstFound = False

    #     while len(queue) > 0:
    #         # Handle visited and dstFound
    #         start = queue.popleft()
    #         if start in visited:
    #             continue

    #         if start == dst:
    #             dstFound = True

    #         visited.add(start)

    #         # Optimization
    #         if dstFound and cost == 0:
    #             return 0

    #         # Explore all weights
    #         for end, weight in graph[start]:
    #             cost &= weight
    #             queue.append(end)

    #     return cost if dstFound else -1