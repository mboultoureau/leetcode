class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(lambda: 0)
        result = 0

        for num in nums:
            rev = int(str(num)[::-1])
            result += hashmap[num - rev]
            hashmap[num - rev] += 1

        return result % (10**9 + 7)