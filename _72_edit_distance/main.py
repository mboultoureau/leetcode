class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [
            [float("inf") for _ in range(len(word1) + 1)]
            for _ in range(len(word2) + 1)
        ]
        
        # Fill base case
        for i in range(len(word2) + 1):
            dp[i][len(word1)] = len(word2) - i
        
        for i in range(len(word1)):
            dp[len(word2)][i] = len(word1) - i


        # Bottom-up
        for r in range(len(word2) - 1, -1, -1):
            for c in range(len(word1) - 1, -1, -1):
                if word2[r] == word1[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]) + 1

        return dp[0][0]