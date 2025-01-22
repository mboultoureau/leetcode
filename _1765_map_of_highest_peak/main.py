class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N = len(isWater)
        M = len(isWater[0])
        
        heightMap = [[-1 for _ in range(M)] for _ in range(N)]
        nextCells = deque([])
        height = 1

        # Fill with water positions
        for r in range(N):
            for c in range(M):
                if isWater[r][c] == 1:
                    heightMap[r][c] = 0
                    movements = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                    for mov in movements:
                        nextCells.append(mov)

        # BFS
        while nextCells:
            length = len(nextCells)
            for _ in range(length):
                (r, c) = nextCells.popleft()
                if r < 0 or r >= N or c < 0 or c >= M or heightMap[r][c] != -1:
                    continue

                heightMap[r][c] = height
                movements = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                for mov in movements:
                    nextCells.append(mov)


            height += 1

        return heightMap