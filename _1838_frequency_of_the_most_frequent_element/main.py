class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        accumulator = 0
        result = 0

        while right < len(nums):
            accumulator += nums[right]

            # We compare the difference between (right - left + 1) equals numbers and the sum of (right - left + 1) numbers (which give us the number of operations)
            while (right - left + 1) * nums[right] - accumulator > k:
                accumulator -= nums[left]
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result