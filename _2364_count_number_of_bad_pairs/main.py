class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badPairs = 0
        diff = defaultdict(int)

        for i in range(len(nums)):
            total = i - nums[i]
            badPairs += i - diff[total]
            diff[total] += 1

        return badPairs