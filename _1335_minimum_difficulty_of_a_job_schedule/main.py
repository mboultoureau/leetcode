class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # With NeetCode video: https://www.youtube.com/watch?v=DAAULrZFeLI
        if d > len(jobDifficulty):
            return -1

        @lru_cache(None)
        def dfs(index, d, current_max):
            # End of jobs list
            if index == len(jobDifficulty):
                if d == 0:
                    return 0
                else:
                    return math.inf

            # No days left
            if d == 0:
                return math.inf

            current_max = max(current_max, jobDifficulty[index])
            # Two cases: continue, end day
            result = min(
                dfs(index + 1, d, current_max),
                current_max + dfs(index + 1, d - 1, -1)
            )
            return result

        return dfs(0, d, -1)