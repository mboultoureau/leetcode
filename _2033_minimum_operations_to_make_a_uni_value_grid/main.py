class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Check if all numbers have the same remainder
        target = grid[0][0] % x

        for row in grid:
            for cell in row:
                if cell % x != target:
                    return -1

        # Find the median
        nums = []

        for row in grid:
            for cell in row:
                nums.append(cell)

        nums.sort()
        common = nums[len(nums) // 2]

        # Calculate number of steps
        result = 0

        for cell in nums:
            result += abs(common - cell) // x

        return result