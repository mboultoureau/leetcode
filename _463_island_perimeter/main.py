class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        NB_ROWS = len(grid)
        NB_COLS = len(grid[0])
        perimeter = 0

        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                cell = grid[row][col]
                
                # Top
                if cell == 1 and (row == 0 or grid[row - 1][col] == 0):
                    perimeter += 1

                # Bottom
                if cell == 1 and (row == NB_ROWS - 1 or grid[row + 1][col] == 0):
                    perimeter += 1

                # Left
                if cell == 1 and (col == 0 or grid[row][col - 1] == 0):
                    perimeter += 1

                # Right
                if cell == 1 and (col == NB_COLS - 1 or grid[row][col + 1] == 0):
                    perimeter += 1

        return perimeter