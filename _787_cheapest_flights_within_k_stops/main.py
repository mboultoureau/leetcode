class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf for _ in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()
            for src, dest, cost in flights:
                if prices[src] == math.inf:
                    continue

                if prices[src] + cost < tempPrices[dest]:
                    tempPrices[dest] = prices[src] + cost

            prices = tempPrices

        return -1 if prices[dst] == math.inf else prices[dst] 