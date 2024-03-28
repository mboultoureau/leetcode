class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        length = 0
        map = defaultdict(int)

        while left < len(nums):
            while right < len(nums) and map[nums[right]] + 1 <= k:
                map[nums[right]] += 1
                right += 1
                length = max(length, right - left)

            map[nums[left]] -= 1
            left += 1

        return length