class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @lru_cache(None)
        def dfs(index):
            if index >= len(arr):
                return 0

            max_sum = 0
            max_value = 0

            for i in range(index, min(index + k, len(arr))):
                max_value = max(max_value, arr[i])
                max_sum = max(
                    max_sum,
                    max_value * (i - index + 1) + dfs(i + 1)
                )

            return max_sum

        return dfs(0)