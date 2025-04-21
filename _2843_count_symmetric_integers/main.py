class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        n = low
        count = 0
        while n <= high:
            if n < 10:
                n = 10
                continue

            if n < 100:
                if n % 11 == 0:
                    count += 1
                
                n += 1
                continue


            if n < 1000:
                n = 1000
                continue

            if n // 1000 + n % 1000 // 100 == n % 100 // 10 + n % 10:
                count += 1
            
            n += 1

        return count