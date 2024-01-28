class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prefixSum = [[0] * cols for _ in range(rows)]

        # Top left
        prefixSum[0][0] = matrix[0][0]

        # First row
        for c in range(1, cols):
            prefixSum[0][c] = prefixSum[0][c - 1] + matrix[0][c]

        # First col
        for r in range(1, rows):
            prefixSum[r][0] = prefixSum[r - 1][0] + matrix[r][0]

        # The rest
        for r in range(1, rows):
            for c in range(1, cols):
                prefixSum[r][c] = matrix[r][c] + prefixSum[r - 1][c] + prefixSum[r][c - 1] - prefixSum[r - 1][c - 1]

        # Calculate number of targets
        result = 0
        for y1 in range(rows):
            for y2 in range(y1, rows):
                prefixCount = defaultdict(int)
                prefixCount[0] = 1
                for x2 in range(cols):
                    currentSum = prefixSum[y2][x2]
                    if y1 > 0:
                        currentSum -= prefixSum[y1 - 1][x2]

                    diff = currentSum - target
                    result += prefixCount[diff]
                    prefixCount[currentSum] += 1

        return result