class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                flip += 1
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0

        return -1 if nums[len(nums) - 1] == 0 or nums[len(nums) - 2] == 0 else flip