class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        @lru_cache(None)
        def dfs(row, robot1, robot2):
            if row == rows or robot1 == robot2 or min(robot1, robot2) < 0 or max(robot1, robot2) >= cols:
                return 0

            result = 0
            for c1 in [-1, 0, 1]:
                for c2 in [-1, 0, 1]:
                    result = max(
                        result,
                        dfs(row + 1, robot1 + c1, robot2 + c2)
                    )

            result += grid[row][robot1] + grid[row][robot2]
            return result

        return dfs(0, 0, cols - 1)