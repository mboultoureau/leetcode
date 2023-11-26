class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        result = 0
        m = len(matrix)
        n = len(matrix[0])

        for row in range(n):
            for column in range(1, m):
                if matrix[column][row] != 0:
                    matrix[column][row] = matrix[column - 1][row] + 1

        for column in range(m):
            sortedColumn = sorted(matrix[column], reverse=True)
            for row in range(n):
                result = max(result, sortedColumn[row] * (row + 1))

        return result