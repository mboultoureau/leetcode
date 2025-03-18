class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        longuest = 0
        curr = 0

        for right in range(len(nums)):
            while curr & nums[right] != 0:
                curr ^= nums[left]
                left += 1

            longuest = max(longuest, right - left + 1)
            curr |= nums[right]


        return longuest