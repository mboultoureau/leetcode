class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(2)]
        dp[0][0] = 1

        for row in range(1, n + 1):
            s = 0
            for col in range(k + 1):
                s += dp[0][col]
                if col >= row:
                    s -= dp[0][col - row]

                dp[1][col] = s

            # Move row
            dp[0] = dp[1]
            dp[1] = [0 for _ in range(k + 1)]

        return dp[0][k] % (10**9 + 7)