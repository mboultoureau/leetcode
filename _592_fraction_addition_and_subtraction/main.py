class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        i = 0
        while i < len(expression):
            currentNumerator = ''
            currentDenominator = ''

            while expression[i] != '/':
                currentNumerator += expression[i]
                i += 1

            i += 1

            while i < len(expression) and expression[i] >= '0' and expression[i] <= '9':
                currentDenominator += expression[i]
                i += 1

            print(currentNumerator)
            print(currentDenominator)

            numerator = numerator * int(currentDenominator) + int(currentNumerator) * denominator
            denominator *= int(currentDenominator)

            divisor = math.gcd(numerator, denominator)

            numerator //= divisor
            denominator //= divisor

        return f"{numerator}/{denominator}"