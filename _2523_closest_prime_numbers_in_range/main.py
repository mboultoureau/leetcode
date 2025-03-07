class Solution:
    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False

        if num == 2 or num == 3:
            return True

        if num % 2 == 0:
            return False

        p = 3
        while p * p <= num:
            if num % p == 0:
                return False

            p += 2

        return True
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev = -1
        solution = [0, 10**9]

        for num in range(left, right + 1):
            if not self.isPrime(num):
                continue

            if prev == -1:
                prev = num
                continue

            diff = num - prev
            if diff < solution[1] - solution[0]:
                solution = [prev, num]
            
            if solution[1] - solution[0] == 1 or solution[1] - solution[0] == 2:
                return [prev, num]

            prev = num
            

        return solution if solution[0] != 0 else [-1, -1]