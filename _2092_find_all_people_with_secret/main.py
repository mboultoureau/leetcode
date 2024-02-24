class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        times = defaultdict(lambda: defaultdict(list))
        result = set([0, firstPerson])

        for person1, person2, time in meetings:
            times[time][person1].append(person2)
            times[time][person2].append(person1)

        def dfs(person, links):
            if person in visited:
                return

            visited.add(person)
            result.add(person)

            for neighbord in links[person]:
                dfs(neighbord, links)

        for time in sorted(times.keys()):
            visited = set()
            for person1 in times[time]:
                if person1 in result:
                    dfs(person1, times[time])

        return result

    # TOO SLOW
    #     meetings = sorted(meetings, key=lambda meeting: meeting[2])
    #     result = set()
    #     result.add(0)
    #     result.add(firstPerson)

    #     queue = deque(meetings)
    #     while queue:
    #         person1, person2, time = queue.popleft()
    #         visited = set()
    #         graph = defaultdict(list)
    #         graph[person1].append(person2)
    #         graph[person2].append(person1)

    #         while queue and queue[0][2] == time:
    #             person1, person2, _ = queue.popleft()
    #             graph[person1].append(person2)
    #             graph[person2].append(person1)

    #         persons = result.copy()
    #         for person in persons:
    #             if person in visited:
    #                 continue

    #             if person in graph:
    #                 graph_queue = deque(graph[person])
    #                 while graph_queue:
    #                     person = graph_queue.popleft()
    #                     result.add(person)
    #                     if person in visited:
    #                         continue

    #                     visited.add(person)
    #                     graph_queue.extend(graph[person])

    #     return result