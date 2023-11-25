class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            current = nums[i]

            nums[i] = (i * current - leftSum) + (rightSum - (len(nums) - i) * current)

            rightSum -= current
            leftSum += current

        return nums