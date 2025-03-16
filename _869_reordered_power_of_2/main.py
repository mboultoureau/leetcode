class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = self.decomposeNum(n)

        for p in range(32):
            target = self.decomposeNum(2**p)
            if target == nums:
                return True

        return False

    def decomposeNum(self, n: int) -> dict[int]:
        nums = defaultdict(int)
        while n != 0:
            nums[n % 10] += 1
            n //= 10

        return nums