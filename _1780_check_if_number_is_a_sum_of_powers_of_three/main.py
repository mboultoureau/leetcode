class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(15, -1, -1):
            if 3**i <= n:
                n -= 3**i

        return n == 0