class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-v for v in count.values()]
        heapq.heapify(heap)
        queue = deque([])
        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][1] <= time:
                value, _ = queue.popleft()
                heappush(heap, value)

            if heap:
                timeLeft = heappop(heap) + 1
                if timeLeft < 0:
                    queue.append((timeLeft, time + n + 1))

        return time