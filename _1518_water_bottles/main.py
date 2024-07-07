class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumedBottles = 0
        emptyBottles = 0

        while numBottles >= 1:
            # 1. Consume all bottles
            consumedBottles += numBottles
            emptyBottles += numBottles

            # 2. Exchange
            numBottles = emptyBottles // numExchange
            emptyBottles -= numBottles * numExchange

        return consumedBottles