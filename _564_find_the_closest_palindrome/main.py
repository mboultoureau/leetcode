class Solution:
    def nearestPalindromic(self, n: str) -> str:
        even = len(n) % 2 == 0
        middle = len(n) // 2 - 1 if len(n) % 2 == 0 else len(n) // 2
        left = int(n[:middle + 1])

        possibilities = [
            self.generate(left, even),
            self.generate(left - 1, even),
            self.generate(left + 1, even),
            10 ** (len(n) - 1) - 1,
            10 ** len(n) + 1,
        ]

        delta = float("inf")
        n = int(n)
        best = 0

        for possibility in possibilities:
            if possibility == n:
                continue
            
            if abs(possibility - n) < delta:
                best = possibility
                delta = abs(possibility - n)
            elif abs(possibility - n) == delta:
                best = min(best, possibility)

        return str(best)

    def generate(self, left, even):
        palindrome = left
        if not even:
            left //= 10
        
        while left > 0:
            palindrome = palindrome * 10 + left % 10
            left //= 10

        return palindrome