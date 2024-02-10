class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            left = i
            right = i

            # Odd
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                result += 1

            # Even 
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                result += 1

        return result