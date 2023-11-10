class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        numsSumLeft = [0]
        for i in range(len(nums) -1):
            numsSumLeft.append(numsSumLeft[-1] + nums[i])

        numsSumRight = [0]
        for i in range(len(nums) -1, 0, -1):
            numsSumRight.insert(0, numsSumRight[0] + nums[i])

        for i in range(len(numsSumLeft)):
            if numsSumLeft[i] == numsSumRight[i]:
                return i

        return -1