class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Solution 2
        N = len(grid)
        if N == 1:
            return grid[0][0]


        smallest1 = (0, -1)
        smallest2 = (0, -1)

        for row in range(N):
            candidates = []
            heapq.heapify(candidates)

            for col in range(N):
                if col == smallest1[1]:
                    heapq.heappush(candidates, (-grid[row][col] + smallest2[0], col))
                else:
                    heapq.heappush(candidates, (-grid[row][col] + smallest1[0], col))

                if len(candidates) > 2:
                    heapq.heappop(candidates)

            smallest2 = heapq.heappop(candidates)
            smallest1 = heapq.heappop(candidates)

        return -smallest1[0]

        # Solution 1
        # N = len(grid)
        # if N == 1:
        #     return grid[0][0]


        # dp = [[math.inf for _ in range(N)] for _ in range(N)]
        # dp[0] = grid[0]

        # for row in range(N - 1):
        #     for col in range(N):
        #         for nextCol in range(0, col):
        #             dp[row + 1][nextCol] = min(dp[row + 1][nextCol], grid[row + 1][nextCol] + dp[row][col])

        #         for nextCol in range(col + 1, N):
        #             dp[row + 1][nextCol] = min(dp[row + 1][nextCol], grid[row + 1][nextCol] + dp[row][col])

        # return min(dp[N - 1])