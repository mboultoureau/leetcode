class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        NB_ROWS = len(grid)
        NB_COLS = len(grid[0])

        visited = set()
        maximum_fishes = 0

        def bfs(r, c):
            if r < 0 or r >= NB_ROWS or c < 0 or c >= NB_COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0

            fishes = grid[r][c]
            visited.add((r, c))
            movements = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in movements:
                fishes += bfs(nr, nc)

            return fishes

        for r in range(NB_ROWS):
            for c in range(NB_COLS):
                if (r, c) in visited or grid[r][c] == 0:
                    continue

                maximum_fishes = max(maximum_fishes, bfs(r, c))

        return maximum_fishes