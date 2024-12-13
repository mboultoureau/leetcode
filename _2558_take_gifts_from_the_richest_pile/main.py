class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Solution 2
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        # If the max is 1, all elements are 1, so the result won't change
        maximum_value = float("inf")
        while k > 0 and maximum_value > 1:
            # Find the max
            maximum_value = -heapq.heappop(gifts)
            heapq.heappush(gifts, -isqrt(maximum_value))
            k -= 1

        return -sum(gifts)

        # Solution 1
        # for _ in range(k):
        #     # Find the max
        #     maximum_idx = 0
        #     maximum_value = 0

        #     for i in range(len(gifts)):
        #         if gifts[i] > maximum_value:
        #             maximum_idx = i
        #             maximum_value = gifts[i] 

        #     gifts[maximum_idx] = math.floor(math.sqrt(maximum_value))

        # return sum(gifts)