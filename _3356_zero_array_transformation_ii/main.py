class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)

        if not self.isSolution(nums, queries, right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2
            if self.isSolution(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left 


    def isSolution(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        total = 0
        diff = [0 for _ in range(len(nums) + 1)]

        for i in range(k):
            start, end, val = queries[i]
            diff[start] += val
            diff[end + 1] -= val

        for n in range(len(nums)):
            total += diff[n]
            if total < nums[n]:
                return False

        return True