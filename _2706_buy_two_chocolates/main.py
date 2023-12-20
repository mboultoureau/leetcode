class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        r = prices[0] + prices[1]
        if r <= money:
            return money - r
        else:
            return money