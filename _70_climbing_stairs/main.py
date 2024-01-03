class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution 4
        if n <= 2:
            return n

        previous_one = 1
        previous_two = 2

        for _ in range(2, n):
            current = previous_one + previous_two
            previous_one = previous_two
            previous_two = current

        return previous_two

        # Solution 3 : use less memory
        # if n <= 2:
        #     return n

        # prev = 2
        # curr = 3
        # for _ in range(n - 3):
        #     new = prev + curr
        #     prev = curr
        #     curr = new

        # return curr

        # Solution 2
        # numbers = [1, 2]

        # for i in range(2, n):
        #     numbers.append(numbers[i - 1] + numbers[i - 2])

        # return numbers[n - 1]



        # Solution 1 : Too slow
        # if n == 1 or n == 2:
        #     return n

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)