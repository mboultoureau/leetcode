class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        power = 0
        while 2 ** power < n:
            power += 1

        return 2 ** power == n

        # Solution 1
        # return n >= 0 and Counter(bin(n))['1'] == 1