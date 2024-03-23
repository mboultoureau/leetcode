class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtracking(i):
            if i >= len(nums):
                result.append(current.copy())
                return

            current.append(nums[i])
            backtracking(i + 1)
            current.pop()
            backtracking(i + 1)

        backtracking(0)

        return result