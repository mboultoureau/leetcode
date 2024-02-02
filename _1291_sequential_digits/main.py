class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []

        # Number of digits in the number
        for nbDigits in range(len(str(low)), len(str(high)) + 1):

            # First digit
            for startNumber in range(1, 10):
                
                if startNumber + nbDigits > 10:
                    break

                number = 0
                i = startNumber

                # Generate digit
                for digit in range(nbDigits - 1, -1, -1):
                    number += i * (10 ** digit)
                    i += 1

                if number >= low and number <= high:
                    results.append(number)

        return results