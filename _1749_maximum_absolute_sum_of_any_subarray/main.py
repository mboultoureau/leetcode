class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maximum = 0
        positive = 0
        negative = 0

        for n in nums:
            positive = max(positive + n, 0)
            negative = max(negative - n, 0)
            maximum = max(maximum, positive)
            maximum = max(maximum, negative)

        return maximum
