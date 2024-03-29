class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(0, i - 1):
                row.append(result[-1][j] + result[-1][j + 1])

            row.append(1)
            result.append(row)

        return result