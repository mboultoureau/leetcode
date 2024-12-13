class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)

        while heap:
            value, index = heapq.heappop(heap)
            if nums[index] != -1:
                score += value
                nums[index] = -1
                if index > 0:
                    nums[index - 1] = -1
                if index + 1 < len(nums):
                    nums[index + 1] = -1

        return score