class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maximum = [0 for _ in range(len(nums))]
        maximum[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            maximum[i] = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    maximum[i] = max(maximum[i], 1 + maximum[j])

        return max(maximum)