class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        NB_ROWS = len(grid1)
        NB_COLS = len(grid1[0]) 
        
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= NB_ROWS or col < 0 or col >= NB_COLS or (row, col) in visited or grid2[row][col] == 0:
                return True

            visited.add((row, col))
            valid = True

            if grid1[row][col] == 0:
                valid = False

            if not dfs(row - 1, col):
                valid = False

            if not dfs(row + 1, col):
                valid = False

            if not dfs(row, col - 1):
                valid = False

            if not dfs(row, col + 1):
                valid = False

            return valid

        count = 0

        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                if (row, col) not in visited and grid2[row][col] == 1 and dfs(row, col) == True:
                    count += 1

        return count