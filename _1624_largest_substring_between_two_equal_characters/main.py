class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = [[-1, -1] for i in range(26)]

        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')][0] == -1:
                count[ord(s[i]) - ord('a')][0] = i

        for i in range(len(s) - 1, -1, -1):
            if count[ord(s[i]) - ord('a')][1] == -1:
                count[ord(s[i]) - ord('a')][1] = i

        result = -1
        for i, j in count:
            if i != -1 and j != -1 and i != j:
                result = max(result, j - i - 1)

        return result