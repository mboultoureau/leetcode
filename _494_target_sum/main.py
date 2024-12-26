class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def combinaison(index, total):
            if index == len(nums):
                return 1 if total == target else 0

            return combinaison(index + 1, total - nums[index]) + combinaison(index + 1, total + nums[index])

        return combinaison(0, 0)

