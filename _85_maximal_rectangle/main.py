class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        NB_ROWS = len(matrix)
        NB_COLS = len(matrix[0])

        result = 0
        heights = [0 for _ in range(NB_COLS)]

        for row in matrix:
            for x in range(len(row)):
                if row[x] == '1':
                    heights[x] = heights[x] + 1
                else:
                    heights[x] = 0

            # Recalculate maximum
            stack = deque()
            for y in range(len(heights) + 1):
                while stack and (y == len(heights) or heights[stack[-1]] > heights[y]):
                    h = heights[stack.pop()]
                    w = y
                    if stack:
                        w = y - stack[-1] - 1
                    result = max(result, h * w)
                stack.append(y)

        return result