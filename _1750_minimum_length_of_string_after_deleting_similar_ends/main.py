class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            # Advance left
            while left + 1 < right and s[left + 1] == s[right]:
                left += 1

            # Advance right
            while left < right - 1 and s[left] == s[right - 1]:
                right -= 1

            left += 1
            right -= 1

        return right - left + 1