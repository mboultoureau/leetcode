class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 2
        return Counter(nums).most_common(1)[0][0]

        # Solution 1
        # numbers = Counter(nums)
        # target = len(nums) // 2 + 1

        # for k, v in numbers.items():
        #     if v >= target:
        #         return k