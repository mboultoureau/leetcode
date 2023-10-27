class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        current = 0

        for n in nums:
            current += n
            maximum = max(current, maximum)
            if current < 0:
                current = 0

        return maximum