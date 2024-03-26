class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        coordinates = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                coordinates.add((y, x))

        numberOfIslands = 0
        def dfs(y, x):
            if (y, x + 1) in coordinates and grid[y][x + 1] == "1":
                coordinates.remove((y, x + 1))
                dfs(y, x + 1)

            if (y, x - 1) in coordinates and grid[y][x - 1] == "1":
                coordinates.remove((y, x - 1))
                dfs(y, x - 1)

            if (y + 1, x) in coordinates and grid[y + 1][x] == "1":
                coordinates.remove((y + 1, x))
                dfs(y + 1, x)

            if (y - 1, x) in coordinates and grid[y - 1][x] == "1":
                coordinates.remove((y - 1, x))
                dfs(y - 1, x)

        while coordinates:
            y, x = coordinates.pop()
            if grid[y][x] == "1":
                dfs(y, x)
                numberOfIslands += 1

        return numberOfIslands