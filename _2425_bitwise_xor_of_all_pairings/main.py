class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums2) % 2 == 1:
            for num1 in nums1:
                res ^= num1

        if len(nums1) % 2 == 1:
            for num2 in nums2:
                res ^= num2

        return res
