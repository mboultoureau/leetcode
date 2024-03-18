class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        NB_ROWS = len(matrix)
        NB_COLS = len(matrix[0])

        rows = [False for _ in range(NB_ROWS)]
        cols = [False for _ in range(NB_COLS)]

        for y in range(NB_ROWS):
            for x in range(NB_COLS):
                if matrix[y][x] == 0:
                    rows[y] = True
                    cols[x] = True


        for y in range(NB_ROWS):
            for x in range(NB_COLS):
                if rows[y] or cols[x]:
                    matrix[y][x] = 0