class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def dfs(row, column, moves):
            if row < 0 or row >= m or column < 0 or column >= n:
                return 1

            if moves <= 0:
                return 0

            return sum([
                dfs(row - 1, column, moves - 1),
                dfs(row + 1, column, moves - 1),
                dfs(row, column - 1, moves - 1),
                dfs(row, column + 1, moves - 1),
            ])
            
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)