class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0 for _ in range(length)]
        result[0] = 1

        for i in range(length - 1):
            result[i + 1] = result[i] * nums[i]

        suffix = 1
        for i in range(length - 1, 0, -1):
            result[i - 1] *= suffix * nums[i]
            suffix = suffix * nums[i]

        return result

        # Solution 1
        # length = len(nums)

        # prefix = [0 for _ in range(length)]
        # suffix = [0 for _ in range(length)]
        # result = [0 for _ in range(length)]

        # prefix[0] = 1
        # suffix[length - 1] = 1

        # for i in range(length - 1):
        #     prefix[i + 1] = prefix[i] * nums[i]

        # for i in range(length - 1, 0, -1):
        #     suffix[i - 1] = suffix[i] * nums[i]

        # for i in range(length):
        #     result[i] = prefix[i] * suffix[i]

        # return result