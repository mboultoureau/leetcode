class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count byte
        count = bin(num2).count('1')
        x = ['0' for _ in range(32)]

        for i in range(31, -1, -1):
            if num1 >= 2**i:
                count -= 1
                num1 -= 2**i
                x[31 - i] = '1'

            if count == 0:
                break

        for i in range(32):
            if count == 0:
                break

            if x[31 - i] == '0':
                x[31 - i] = '1'
                count -= 1

        return int(''.join(x), 2)