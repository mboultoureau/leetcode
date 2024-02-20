class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums) * (len(nums) + 1) // 2
        for n in nums:
            result -= n

        return result
