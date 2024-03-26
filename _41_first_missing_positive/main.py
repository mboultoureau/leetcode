class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index < 0 or index >= len(nums) or nums[index] < 0:
                continue

            if nums[index] == 0:
                nums[index] = -1 * (len(nums) + 1)
            else:
                nums[index] *= -1

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1