class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 3
        return len(nums) != len(set(nums))

        # Solution 2
        # numbers = {}
        # for n in nums:
        #     if n in numbers:
        #         return True
        #     else:
        #         numbers[n] = 0

        # return False

        # Solution 1
        # numbers = Counter(nums)
        # for v in numbers.values():
        #     if v > 1:
        #         return True

        # return False