class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        n1, n2 = 0, 0
        while n1 < len(nums1) or n2 < len(nums2):
            # End
            if n1 >= len(nums1):
                result.extend(nums2[n2:])
                break

            if n2 >= len(nums2):
                result.extend(nums1[n1:])
                break

            if nums1[n1][0] == nums2[n2][0]:
                result.append([nums1[n1][0], nums1[n1][1] + nums2[n2][1]])
                n1 += 1
                n2 += 1
                continue

            if nums1[n1][0] < nums2[n2][0]:
                result.append([nums1[n1][0], nums1[n1][1]])
                n1 += 1
            else:
                result.append([nums2[n2][0], nums2[n2][1]])
                n2 += 1

        return result