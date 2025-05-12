class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue

                    n = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if n % 2 == 0 and n >= 100:
                        nums.add(n)

        nums = list(nums)
        nums.sort()
        return nums