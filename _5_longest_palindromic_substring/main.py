class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxLength = 0

        for middle in range(len(s)):
            # Odd
            left, right = middle, middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1
                if currentLength > maxLength:
                    result = s[left:right + 1]
                    maxLength = currentLength

                left -= 1
                right += 1

            # Even
            left, right = middle, middle + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1
                if currentLength > maxLength:
                    result = s[left:right + 1]
                    maxLength = currentLength

                left -= 1
                right += 1

        return result