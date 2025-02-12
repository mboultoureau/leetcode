class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = defaultdict(list)
        for n in nums:
            # Calculate sum of digit
            sum_of_digits = 0
            d = n
            while d > 0:
                sum_of_digits += d % 10
                d = d // 10

            heapq.heappush(digits[sum_of_digits], -n)


        maximum = -1
        for digit, l in digits.items():
            if len(l) >= 2:
                n1 = -heapq.heappop(l)
                n2 = -heapq.heappop(l)
                maximum = max(maximum, n1 + n2)

        return maximum