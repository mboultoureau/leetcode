class Solution:
    def totalMoney(self, n: int) -> int:
        # Second solution
        divide = n // 7
        modulo = n % 7
        return 28 * divide + 7 * divide * (divide - 1) // 2 + ((divide + modulo + 1) * (divide + modulo) - divide * (divide + 1)) // 2

        # First solution
        # # 28 * (n // 7) --> each week add 28 days to make 1 + 2 + 3 + 4 + 5 + 6 + 7
        # # 7 * (n // 7) * (n // 7 - 1) // 2 --> each week add missing days, week 1: 0, week 2: 7, week 3: 14, etc
        # # ((n // 7 + n % 7 + 1) * (n // 7 + n % 7) - (n // 7) * (n // 7 + 1)) // 2 --> overflow day, ex: 4 --> 1 + 2 + 3 + 4, 10 --> 2 + 3 + 4
        # return 28 * (n // 7) + 7 * (n // 7) * (n // 7 - 1) // 2 + ((n // 7 + n % 7 + 1) * (n // 7 + n % 7) - (n // 7) * (n // 7 + 1)) // 2