class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):

            # Find a word valid
            for word in wordDict:
                length = len(word)
                if i + length > n or dp[i + length] == False:
                    continue

                valid = True
                for j in range(length):
                    if word[j] != s[i + j]:
                        valid = False
                        break

                if valid:
                    dp[i] = True

        return dp[0]