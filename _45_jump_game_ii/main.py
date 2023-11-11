class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = 0
        next = 0
        current = 0

        for i in range(len(nums) - 1):
            next = max(i + nums[i], next)
            if current == i:
                answer += 1
                current = next

        return answer

        # Solution 1: too slow
        # jumps = [math.inf] * len(nums)

        # def calculate_jump(current, n):
        #     if jumps[current] > n:
        #         jumps[current] = n
        #         for i in range(current + 1, min(current + nums[current] + 1, len(nums))):
        #             calculate_jump(i, n + 1)
    
        # calculate_jump(0, 0)
        # return jumps[len(nums) - 1]