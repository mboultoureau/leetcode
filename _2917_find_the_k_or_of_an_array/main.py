class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0

        for i in range(32):
            total = 0
            for n in nums:
                total += (n >> i) & 1

            if total >= k:
                result |= (1 << i)

        return result