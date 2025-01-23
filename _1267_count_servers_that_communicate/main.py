class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        NB_ROWS = len(grid)
        NB_COLS = len(grid[0])
        count = 0

        rows = [0 for _ in range(NB_COLS)]
        cols = [0 for _ in range(NB_ROWS)]

        for r in range(NB_ROWS):
            for c in range(NB_COLS):
                if grid[r][c] == 1:
                    rows[c] += 1
                    cols[r] += 1

        for r in range(NB_ROWS):
            for c in range(NB_COLS):
                if grid[r][c] == 1 and (rows[c] > 1 or cols[r] > 1):
                    count += 1

        return count 
