class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = 0

        for i in range(0, len(nums) // 2):
            if nums[i] + nums[len(nums) - 1 - i] > n:
                n = nums[i] + nums[len(nums) - 1 - i]

        return n