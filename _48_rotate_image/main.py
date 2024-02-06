class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for y in range(n - 1):
            for x in range(y, n - 1 - y):
                row, col = y, x
                top_left = matrix[row][col]
                
                row, col = col, n - 1 - row
                top_right = matrix[row][col]
                matrix[row][col] = top_left

                row, col = col, n - 1 - row
                bottom_right = matrix[row][col]
                matrix[row][col] = top_right

                row, col = col, n - 1 - row
                bottom_left = matrix[row][col]
                matrix[row][col] = bottom_right

                row, col = col, n - 1 - row
                matrix[row][col] = bottom_left