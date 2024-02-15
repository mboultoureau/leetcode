class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxLength = -1
        sum = 0

        for num in nums:
            if sum > num:
                maxLength = sum + num
            sum += num

        return maxLength