class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        nbFresh = 0
        queue = []

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    nbFresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        time = 0
        possibleMoves = [
            (-1,  0), # top
            ( 0,  1), # right
            ( 1,  0), # bottom
            ( 0, -1)  # left
        ]
        while nbFresh > 0 and len(queue) > 0:
            length = len(queue)
            
            for _ in range(length):
                first = queue[0]
                queue.pop(0)

                for possibleMove in possibleMoves:
                    row = first[0] + possibleMove[0]
                    col = first[1] + possibleMove[1]

                    if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1:
                        queue.append((row, col))
                        grid[row][col] = 2
                        nbFresh -= 1

            time += 1

        if nbFresh == 0:
            return time

        return -1