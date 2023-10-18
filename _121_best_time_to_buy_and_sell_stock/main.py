class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0

        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])

            right += 1

        return profit