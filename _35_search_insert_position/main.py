class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        middle = 0

        if target > nums[-1]:
            return len(nums)

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return left
