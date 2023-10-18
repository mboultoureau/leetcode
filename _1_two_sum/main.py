class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, num in enumerate(nums):
            searchedNumber = target - num
            if searchedNumber in numbers:
                return [numbers[searchedNumber], i]
            numbers[num] = i
        
        return [0, 0]