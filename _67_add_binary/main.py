class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
        
        # r = int('0b' + a, 2) + int('0b' + b, 2)
        # return "{0:b}".format(r)