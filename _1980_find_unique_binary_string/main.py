class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        maximum = int('1' * n, 2)
        numbers = set()

        for num in nums:
            numbers.add(int(num, 2))

        for i in range(maximum + 1):
            if i not in numbers:
                return bin(i)[2:].zfill(n)

        # Solution 1
        # for i in range(2**len(nums)):
        #     binary = format(i, 'b').rjust(len(nums[0]), '0')
        #     if binary not in nums:
        #         return binary