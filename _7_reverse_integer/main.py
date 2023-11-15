class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        if x < 0:
            r = -int(str(x)[:0:-1]) 
        else:
            r = int(str(x)[::-1])

        if r > 2**31 - 1 or r < -2**31:
            return 0

        return r