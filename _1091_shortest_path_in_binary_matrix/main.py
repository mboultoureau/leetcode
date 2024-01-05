class Cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)

        possibleMoves = [
            (-1,  0), # top
            (-1,  1), # top right
            ( 0,  1), # right
            ( 1,  1), # bottom right
            ( 1,  0), # bottom
            ( 1, -1), # bottom left
            ( 0, -1), # left
            (-1, -1)  # top left
        ]

        queue = [Cell(x = 0, y = 0, dist = 1)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True

        while len(queue) > 0:
            first = queue[0]
            queue.pop(0)

            if first.x == n - 1 and first.y == n - 1:
                return first.dist

            for possibleMove in possibleMoves:
                x = first.x + possibleMove[0]
                y = first.y + possibleMove[1]

                if x >= 0 and x < n and y >= 0 and y < n and not visited[x][y] and grid[x][y] == 0:
                    queue.append(Cell(x = x, y = y, dist = first.dist + 1))
                    visited[x][y] = True

        return -1
