class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True

            visited.add(n)
            sum = 0
            for digit in str(n):
                sum += int(digit) * int(digit)
            n = sum

        return False