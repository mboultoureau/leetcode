class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        @lru_cache
        def dfs(i, previous_increasing, previous_decreasing):
            if i == len(nums):
                return 1

            total = 0
            for j in range(previous_increasing, nums[i] + 1):
                increasing = j
                decreasing = nums[i] - increasing
                if increasing >= previous_increasing and decreasing <= previous_decreasing:
                    total += dfs(i + 1, increasing, decreasing)

            return total

        total = dfs(i=0, previous_increasing=0, previous_decreasing=50)
        return total % (10**9 + 7)