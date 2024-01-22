class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        missing = 0
        double = 0

        for i in range(1, len(nums) + 1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                double = i

        return [double, missing]