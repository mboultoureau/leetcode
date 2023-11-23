class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.check(nums[l[i]:r[i] + 1]))

        return result
        
    def check(self, nums) -> bool:
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i + 1] - nums[i] != diff:
                return False

        return True