class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        best = -1


        for n in nums:
            if n > best and -n in nums:
                best = n

        return best