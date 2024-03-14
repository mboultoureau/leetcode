class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = 0
        result = 0
        matches = defaultdict(int)
        matches[0] = 1

        for n in nums:
            total += n
            result += matches[total - goal]
            matches[total] += 1

        return result