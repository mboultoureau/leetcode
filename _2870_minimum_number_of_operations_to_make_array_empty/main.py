class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for v in count.values():
            if v == 1:
                return -1
            result += math.ceil(v / 3)

        return result