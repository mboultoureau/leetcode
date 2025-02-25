class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        prefix = 0
        odd = 0
        even = 1

        for n in arr:
            prefix += n

            if prefix % 2 == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

            result = result % (10**9 + 7)

        return result