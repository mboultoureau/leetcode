class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(i, current):
            if i >= len(nums):
                result.append(current.copy())
                return

            current.append(nums[i])
            backtracking(i + 1, current)
            current.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1, current)

        backtracking(0, [])

        return result