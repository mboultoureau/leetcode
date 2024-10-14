class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []

        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k):
            value = heapq.heappop(heap)
            score += -value
            heapq.heappush(heap, -math.ceil(-value / 3))

        return score