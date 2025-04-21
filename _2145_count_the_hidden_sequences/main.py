class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minimum = 0
        maximum = 0
        current = 0

        for diff in differences:
            current += diff
            minimum = min(minimum, current)
            maximum = max(maximum, current)

        return max(abs(upper - lower) - abs(maximum - minimum) + 1, 0)