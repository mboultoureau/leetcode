class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        count = Counter(s)

        return '1' * (count['1'] - 1) + '0' * (length - count['1']) + '1'