class Solution:
    def strangePrinter(self, s: str) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0

            result = 1 + dfs(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    result = min(result, dfs(i, k - 1) + dfs(k + 1, j))

            return result


        return dfs(0, len(s) - 1)