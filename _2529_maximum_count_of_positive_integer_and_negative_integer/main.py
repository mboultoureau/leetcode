class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        # Find the first positive number
        left = 0
        right = len(nums) - 1
        posLimit = len(nums)

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] <= 0:
                left = middle + 1
            else:
                right = middle - 1
                posLimit = middle

        # Find 0 (or the first positive number)
        left = 0
        right = len(nums) - 1
        negLimit = len(nums)

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] < 0:
                left = middle + 1
            else:
                right = middle - 1
                negLimit = middle

        return max(len(nums) - posLimit, negLimit)