class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (n * 2 - 1)
        numbers = [False] * (n + 1)

        self.find_largest_sequence(0, result, numbers, n)

        return result

    def find_largest_sequence(self, index, result, numbers, n):
        if index == len(result):
            return True

        if result[index] != 0:
            return self.find_largest_sequence(index + 1, result, numbers, n)

        for num in range(n, 0, -1):
            if numbers[num]:
                continue

            numbers[num] = True
            result[index] = num

            if num == 1:
                if self.find_largest_sequence(index + 1, result, numbers, n):
                    return True
            elif index + num < len(result) and result[index + num] == 0:
                result[index + num] = num

                if self.find_largest_sequence(index + 1, result, numbers, n):
                    return True

                result[index + num] = 0

            result[index] = 0
            numbers[num] = False

        return False
