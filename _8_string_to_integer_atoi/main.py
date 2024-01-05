class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        number = ''
        positive = True

        # 1. Read in and ignore any leading whitespace.
        while left < len(s) and s[left] == ' ':
            left += 1

        if left == len(s):
            return 0

        # 2. Check if the next character (if not already at the end of the string)
        # is '-' or '+'. Read this character in if it is either. This
        # determines if the final result is negative or positive respectively.
        # Assume the result is positive if neither is present.
        if s[left] == '+':
            left += 1
        elif s[left] == '-':
            left += 1
            positive = False

        right = left

        # 3. Read in next the characters until the next non-digit character or the
        # end of the input is reached. The rest of the string is ignored.
        while right < len(s) and s[right] >= '0' and s[right] <= '9':
            number += s[right]
            right += 1

        if len(number) == 0:
            return 0

        # 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
        # If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        n = int(number)
        if not positive:
            n = -n

        # 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        # then clamp the integer so that it remains in the range. Specifically, integers
        # less than -231 should be clamped to -231, and integers greater than 231 - 1
        # should be clamped to 231 - 1.
        if n > 2**31 - 1:
            n = 2 ** 31 - 1
        elif n < -2**31:
            n = -2 ** 31

        # 6. Return the integer as the final result.
        return n
