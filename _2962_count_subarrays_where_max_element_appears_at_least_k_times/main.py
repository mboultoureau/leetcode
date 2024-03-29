class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        left = 0
        result = 0
        nb = 0

        for right in range(len(nums)):
            if nums[right] == target:
                nb += 1

            while nb == k:
                if nums[left] == target:
                    nb -= 1
                left += 1

            result += left

        return result