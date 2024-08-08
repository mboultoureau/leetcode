class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        r = rStart
        c = cStart
        move = 1

        def addToResult(r, c):
            if c >= 0 and c < cols and r >= 0 and r < rows:
                result.append([r, c])
        

        while len(result) != rows * cols:

            # Move to right
            for i in range(move):
                addToResult(r, c)
                c += 1

            # Move to bottom
            for i in range(move):
                addToResult(r, c)
                r += 1

            move += 1
            # Move to left
            for i in range(move):
                addToResult(r, c)
                c -= 1

            # Move to up
            for i in range(move):
                addToResult(r, c)
                r -= 1

            move += 1

        return result