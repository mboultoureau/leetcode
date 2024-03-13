class Solution:
    def pivotInteger(self, n: int) -> int:
        # Solution 2
        x = sqrt(n * (n + 1) / 2)
        if x % 1 == 0:
            return int(x)

        return -1

        # Solution 1
        # total = n * (n + 1) / 2
        # for i in range(1, n + 1):
        #     totalFromX = i * (i + 1) / 2
        #     if totalFromX == total - totalFromX + i:
        #         return i 

        # return -1