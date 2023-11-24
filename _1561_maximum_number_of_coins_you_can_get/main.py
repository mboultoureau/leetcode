class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Solution 2
        result = 0
        piles.sort()
        left = 0
        right = len(piles) - 1

        while left <= right:
            result += piles[right - 1]
            left += 1
            right -= 2

        return result

        # Solution 1
        # result = 0
        # piles.sort()

        # while len(piles) > 0:
        #     result += piles[-2]
        #     piles.pop(-1)
        #     piles.pop(-2)
        #     piles.pop(0)

        # return result
