class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = Counter(nums)
        target = len(nums) // 2 + 1

        for k, v in numbers.items():
            if v >= target:
                return k