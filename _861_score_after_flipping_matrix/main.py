class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Change all rows begin with 0
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        # Change all columns with max 0
        for c in range(n):
            count = 0

            for r in range(m):
                count += grid[r][c]

            if count <= m // 2:
                for r in range(m):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        # Calculate sum
        total = 0
        for r in range(m):
            binary = 0
            for c in range(n):
                if grid[r][c] == 1:
                    binary |= (1 << (n - c - 1))

            total += binary
        
        return total