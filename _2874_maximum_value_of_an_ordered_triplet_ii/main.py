class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxNum = 0
        maxDiff = 0
        maxResult = 0

        for k in nums:
            maxResult = max(maxResult, maxDiff * k)
            maxDiff = max(maxDiff, maxNum - k)
            maxNum = max(maxNum, k)

        return maxResult