class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solution 2
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]

        return min(cost[-1], cost[-2])


        # Solution 1
        # @lru_cache(None)
        # def climb(i):
        #     # Last step
        #     if i >= len(cost):
        #         return 0

        #     return min(climb(i + 1), climb(i + 2)) + cost[i]


        # return min(climb(0), climb(1))