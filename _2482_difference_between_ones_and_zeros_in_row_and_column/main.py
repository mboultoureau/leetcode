class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        onesRows = [0] * m
        onesCols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRows[i] += 1
                    onesCols[j] += 1

        for i in range(m):
            for j in range(n):
                grid[i][j] = onesRows[i] + onesCols[j] - (m - onesRows[i]) - (n - onesCols[j])

        return grid