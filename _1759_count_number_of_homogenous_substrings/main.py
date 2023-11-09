class Solution:
    def countHomogenous(self, s: str) -> int:
        left = 0
        right = 1
        nb = 0

        while right < len(s) + 1:
            while right < len(s) and s[left] == s[right]:
                right += 1

            n = right - left
            nb += (n ** 2 + n) // 2
            left = right
            right += 1

        return nb % (10**9 + 7)