class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # With NeetCode video help: https://www.youtube.com/watch?v=etI6HqWVa8U

        count = defaultdict(int)
        right = 0
        far = 0
        near = 0
        result = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while len(count) > k:
                count[nums[near]] -= 1
                if count[nums[near]] == 0:
                    count.pop(nums[near])
                near += 1
                far = near

            while count[nums[near]] > 1:
                count[nums[near]] -= 1
                near += 1

            if len(count) == k:
                result += near - far + 1
        
        return result