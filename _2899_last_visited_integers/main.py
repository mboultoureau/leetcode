class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []

        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                seen.append(nums[i])
                i += 1
                continue

            k = 0
            while i < len(nums) and nums[i] == -1:
                i += 1
                k += 1

                if k <= len(seen):
                    ans.append(seen[len(seen) - k])
                else:
                    ans.append(-1)

        return ans