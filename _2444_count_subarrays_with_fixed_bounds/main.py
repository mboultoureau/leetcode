class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        left = -1
        right = -1
        bad = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                bad = i
            
            if nums[i] == minK:
                left = i
            
            if nums[i] == maxK:
                right = i

            result += max(0, min(left, right) - bad)

        return result