class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = 0

        while i < len(nums):
            if nums[i] == n:
                return n

            if nums[i] == i + 1:
                i += 1
            else:
                next = nums[i]
                nums[i] = n
                n = next
                i = max(next - 1, 0)