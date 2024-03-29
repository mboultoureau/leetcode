class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(i, current, subset):
            nonlocal result

            if current == 0:
                result.append(subset.copy())
                return

            if i >= len(candidates) or current < 0:
                return

            subset.append(candidates[i])
            current -= candidates[i]
            backtracking(i + 1, current, subset)

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            subset.pop()
            current += candidates[i]
            backtracking(i + 1, current, subset)


        backtracking(0, target, [])

        return result