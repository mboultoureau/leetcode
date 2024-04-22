class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Solution 2
        score = 0

        for row in nums:
            row.sort(reverse=True)

        for col in range(len(nums[0])):
            maximum = 0
            for row in range(len(nums)):
                maximum = max(maximum, nums[row][col])

            score += maximum

        return score

        # Solution 1
        # heaps = []
        # score = 0

        # for row in nums:
        #     heap = []
        #     for cell in row:
        #         heapq.heappush(heap, -cell)
        #     heaps.append(heap)

        # for col in range(len(nums[0])):
        #     maximum = 0
        #     for row in range(len(nums)):
        #         maximum = max(maximum, -heapq.heappop(heaps[row]))

        #     score += maximum
            
        # return score