class Solution:
    def findComplement(self, num: int) -> int:
        result = ""
        binString = str(bin(num))[2:]

        for c in binString:
            result += '0' if c == '1' else '1'

        return int(result, 2)