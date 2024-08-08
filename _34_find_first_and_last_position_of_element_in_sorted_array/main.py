class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def dichotomous_search(nums, target, is_left):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                elif is_left:
                    index = middle
                    right = middle - 1
                else:
                    index = middle
                    left = middle + 1
            
            return index

        return [dichotomous_search(nums, target, True), dichotomous_search(nums, target, False)]