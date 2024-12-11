class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        length = 0
        nums.sort()

        # Sliding window
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            length = max(length, right - left + 1)

        return length