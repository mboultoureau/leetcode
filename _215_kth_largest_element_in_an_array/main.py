class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        return heap[0]


        # Solution 1
        # heapq.heapify(nums)
        # result = heapq.nlargest(k, nums)

        # return result[-1]