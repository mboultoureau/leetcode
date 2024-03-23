class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        total = 0

        def backtracking(i):
            nonlocal total

            if total == target:
                result.append(current.copy())
                return

            if i >= len(candidates) or total > target:
                return

            print(current, total)

            current.append(candidates[i])
            total += candidates[i]
            backtracking(i)

            current.pop()
            total -= candidates[i]
            backtracking(i + 1)

        backtracking(0)

        return result