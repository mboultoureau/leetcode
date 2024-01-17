class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i in range(1, len(nums) + 1):
            if len(nums) % i == 0:
                sum += nums[i - 1] * nums[i - 1]

        return sum