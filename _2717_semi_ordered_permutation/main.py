class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        first = nums.index(1)
        last = nums.index(n)

        if first > last:
            result -= 1

        result += first + (n - 1) - last

        return result