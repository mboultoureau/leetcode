class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        result = 0

        for i in range(1, len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                if diff in dp[i]:
                    dp[i][diff] += 1
                else:
                    dp[i][diff] = 1
                
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]

        return result
