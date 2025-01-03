class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        splits = 0

        for n in nums[:len(nums) - 1]:
            left += n
            right -= n
            if left >= right:
                splits += 1

        return splits