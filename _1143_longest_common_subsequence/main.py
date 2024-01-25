class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[-1][-1] = 1 if text1[-1] == text2[-1] else 0

        # Make last row
        for c in range(cols - 2, -1, -1):
            if text2[c] == text1[-1]:
                dp[-1][c] = 1
            else:
                dp[-1][c] = dp[-1][c + 1]

        # Make last column
        for r in range(rows - 2, -1, -1):
            if text1[r] == text2[-1]:
                dp[r][-1] = 1
            else:
                dp[r][-1] = dp[r + 1][-1]

        # Make the rest
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]