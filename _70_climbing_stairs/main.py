class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution 3 : use less memory
        if n <= 2:
            return n

        prev = 2
        curr = 3
        for _ in range(n - 3):
            new = prev + curr
            prev = curr
            curr = new

        return curr

        # Solution 2
        # numbers = [1, 2]

        # for i in range(2, n):
        #     numbers.append(numbers[i - 1] + numbers[i - 2])

        # return numbers[n - 1]



        # Solution 1 : Too slow
        # if n == 1 or n == 2:
        #     return n

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)