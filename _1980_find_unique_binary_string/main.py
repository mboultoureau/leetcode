class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(2**len(nums)):
            binary = format(i, 'b').rjust(len(nums[0]), '0')
            if binary not in nums:
                return binary