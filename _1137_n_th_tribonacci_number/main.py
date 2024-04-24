class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1

        for _ in range(n - 2):
            temp_t1 = t1
            temp_t2 = t2
            t2 = t0 + t1 + t2
            t0 = temp_t1
            t1 = temp_t2

        return t2