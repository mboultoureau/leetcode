class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == "0" else 0
        right = Counter(s[1:])["1"]
        result = left + right

        for i in range(1, len(s) - 1):
            if s[i] == "1":
                right -= 1
            else:
                left += 1
            result = max(result, left + right)

        return result