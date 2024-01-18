class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            dividor = (columnNumber - 1) // 26
            remainder = (columnNumber - 1) % 26

            result = chr(remainder + ord('A')) + result
            columnNumber = dividor


        return result