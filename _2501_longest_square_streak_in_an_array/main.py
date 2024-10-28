class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        result = 0
        numbers = set(nums)

        for num in nums:
            count = 0
            current = num

            while current in numbers:
                count += 1
                
                if current * current > 10**5:
                    break

                current *= current

            result = max(result, count)

        if result >= 2:
            return result
        else:
            return -1