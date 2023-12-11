class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        previous = ''

        for c in arr:
            if previous == c:
                count += 1
            else:
                previous = c
                count = 0

            if count >= len(arr) // 4:
                return c