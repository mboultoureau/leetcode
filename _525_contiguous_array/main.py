class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        total = 0
        diff = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total not in diff:
                diff[total] = i
            else:
                index = diff[total]
                result = max(result, i - index)


        return result