class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.rjust(32, '0')
        return int(binary[::-1], 2)