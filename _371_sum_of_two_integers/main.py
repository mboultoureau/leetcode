class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) != 0:
            xor = a ^ b
            b = (a & b) << 1
            a = xor

        if b > 0:
            return a & mask
        else:
            return a