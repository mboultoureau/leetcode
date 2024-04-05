class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        NB_ROWS = len(heights)
        NB_COLS = len(heights[0])

        pacific = set()
        atlantic = set()
        visited = set()

        queue = deque([(0, 0, heights[0][0])])

        # Left col
        for i in range(1, NB_ROWS):
            queue.append((i, 0, heights[i][0]))

        # Top col
        for i in range(1, NB_COLS):
            queue.append((0, i, heights[0][i]))

        while queue:
            (row, col, previous) = queue.popleft()

            if (row, col) in visited or row < 0 or col < 0 or row >= NB_ROWS or col >= NB_COLS or heights[row][col] < previous:
                continue

            visited.add((row, col))
            pacific.add((row, col))

            queue.append((row + 1, col, heights[row][col]))
            queue.append((row - 1, col, heights[row][col]))
            queue.append((row, col + 1, heights[row][col]))
            queue.append((row, col - 1, heights[row][col]))


        visited.clear()

        queue.append((NB_ROWS - 1, NB_COLS - 1, heights[NB_ROWS - 1][NB_COLS - 1]))

        # Right col
        for i in range(0, NB_ROWS - 1):
            queue.append((i, NB_COLS - 1, heights[i][NB_COLS - 1]))

        # Top col
        for i in range(0, NB_COLS - 1):
            queue.append((NB_ROWS - 1, i, heights[NB_ROWS - 1][i]))

        while queue:
            (row, col, previous) = queue.popleft()

            if (row, col) in visited or row < 0 or col < 0 or row >= NB_ROWS or col >= NB_COLS or heights[row][col] < previous:
                continue

            visited.add((row, col))
            atlantic.add((row, col))

            queue.append((row + 1, col, heights[row][col]))
            queue.append((row - 1, col, heights[row][col]))
            queue.append((row, col + 1, heights[row][col]))
            queue.append((row, col - 1, heights[row][col]))

        result = []

        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result