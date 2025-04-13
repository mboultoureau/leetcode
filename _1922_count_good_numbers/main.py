class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)
        even = pow(5, n // 2 + n % 2, mod)
        odd = pow(4, n // 2, mod)
        return (even * odd) % mod