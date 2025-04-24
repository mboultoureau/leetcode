class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nb_distincts = len(set(nums))
        nb_subarrays = 0

        left = 0
        right = 0
        count = defaultdict(int)

        for left in range(len(nums)):
            if left > 0:
                count[nums[left - 1]] -= 1
                if count[nums[left - 1]] == 0:
                    count.pop(nums[left - 1])
            
            while right < len(nums) and len(count) < nb_distincts:
                count[nums[right]] += 1
                right += 1

            if len(count) == nb_distincts:
                nb_subarrays += len(nums) - right + 1

        return nb_subarrays