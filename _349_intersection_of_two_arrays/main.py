class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []

        for n in nums2:
            if n in nums1:
                result.append(n)

        return result