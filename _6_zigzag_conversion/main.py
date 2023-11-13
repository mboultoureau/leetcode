class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Solution 2
        if numRows == 1:
            return s

        result = [""] * numRows
        i = 0
        direction = 1

        for c in s:
            result[i] += c
            if i == numRows - 1:
                direction = -1
            elif i == 0:
                direction = 1

            i += direction

        return "".join(result)

        # Solution 1
        # result = [""] * numRows
        # length = 0

        # while length < len(s):
        #     # Increasing
        #     for i in range(min(numRows, len(s) - length)):
        #         result[i] += s[length]
        #         length += 1

        #     # Decreasing
        #     for i in range(numRows - 2, numRows - 2 - min(numRows - 2, len(s) - length), -1):
        #         result[i] += s[length]
        #         length += 1

        # return "".join(result)