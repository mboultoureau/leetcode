class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # SOLUTION 2
        n = len(grid)

        expected = (n * n) * (n * n + 1) // 2
        expected_square = (n * n) * (n * n + 1) * (2 * n * n + 1) // 6

        current = 0
        current_square = 0

        for r in range(n):
            for c in range(n):
                current += grid[r][c]
                current_square += grid[r][c] * grid[r][c]

        diff = current - expected
        diff_square = current_square - expected_square

        sum_a_b = diff_square // diff

        return [(sum_a_b + diff) // 2, (sum_a_b - diff) // 2]





        # SOLUTION 1: Memory exceeded
        # n = len(grid)
        # numbers = set([i for i in range(1, n ** n + 1)])
        # solution = [0, 0]

        # for r in range(n):
        #     for c in range(n):
        #         if grid[r][c] in numbers:
        #             numbers.remove(grid[r][c])
        #         else:
        #             solution[0] = grid[r][c]

        # solution[1] = numbers.pop()
        # return solution