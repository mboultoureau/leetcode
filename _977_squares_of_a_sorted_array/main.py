class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 2
        nums = [n * n for n in nums]
        nums.sort()

        return nums

        # Solution 1
        # heap = []
        # for n in nums:
        #     heapq.heappush(heap, n * n)

        # return [heappop(heap) for i in range(len(heap))]