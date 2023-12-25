class Solution:
    def numDecodings(self, s: str) -> int:
        # Check valid
        if s[0] == '0':
            return 0

        for i in range(0, len(s) - 1):
            if s[i] == '0' and s[i + 1] == '0':
                return 0

        # Count possibilities (fibonacci)
        arr = [0] * (len(s) + 1)
        arr[0] = 1
        arr[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                arr[i] += arr[i - 1]

            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] >= '0' and s[i - 1] <= '6'):
                arr[i] += arr[i - 2]


        return arr[-1]