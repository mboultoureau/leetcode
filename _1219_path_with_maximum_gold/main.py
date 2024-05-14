class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0

        for r in range(m):
            for c in range(n):
                result = max(result, self.dfs(grid, r, c))

        return result

    def dfs(self, grid: List[List[int]], r, c):
        m = len(grid)
        n = len(grid[0])

        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0

        current = grid[r][c]
        gold = grid[r][c]
        grid[r][c] = 0

        directions = [
            [-1,  0],
            [ 1,  0],
            [ 0, -1],
            [ 0,  1]
        ]
        for d in directions:
            next = self.dfs(grid, r + d[0], c + d[1])
            gold = max(gold, current + next)

        grid[r][c] = current

        return gold
