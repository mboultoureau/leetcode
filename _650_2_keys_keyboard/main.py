class Solution:
    def minSteps(self, n: int) -> int:
        
        @lru_cache
        def dfs(length, clipboard):
            if length == n:
                return 0

            if length > n or clipboard > n:
                return float("inf")

            copy = float("inf")
            paste = float("inf")

            if length > clipboard:
                copy = dfs(length, length)

            if clipboard > 0:
                paste = dfs(length + clipboard, clipboard)

            return 1 + min(copy, paste)

        return dfs(1, 0)