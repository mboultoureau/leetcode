class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Solution 1
        xor = k
        for n in nums:
            xor ^= n

        result = 0
        for i in range(32):
            result += (xor >> i) & 1

        return result

        # Solution 2
        # result = 32

        # for i in range(32):
        #     count = 0
        #     for n in nums:
        #         if n & (1 << i) != 0:
        #             count += 1

        #     if count % 2 == (k >> i) & 1:
        #         result -= 1

        # return result