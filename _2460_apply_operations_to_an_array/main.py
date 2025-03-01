class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        numsOfZeros = 0
        i = 0
        j = 0

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1


        return nums