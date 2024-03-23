class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2= heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, stone1 - stone2)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]