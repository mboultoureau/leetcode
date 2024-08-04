class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Improved
        heap = []
        for i in range(n):
            heapq.heappush(heap, (nums[i], i))


        result = 0
        for i in range(right):
            value, index = heapq.heappop(heap)
            if i >= left - 1:
                result += value

            if index < n - 1:
                heapq.heappush(heap, (value + nums[index + 1], index + 1))

        return result % (10**9 + 7)

        # Brute-force
        # subarraySums = []
        # for i in range(n):
        #     prefix = 0
        #     for j in range(i, n):
        #         subarraySums.append(prefix + nums[j])
        #         prefix += nums[j]

        # subarraySums.sort()
        # total = 0
        # for i in range(left - 1, right):
        #     total += subarraySums[i]

        # return total % (10**9 + 7)