class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        binary = bin(n)[2:]
        return binary.count('1') == 1 and (len(binary) - binary.find('1')) % 2 == 1
