class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0

        for i in range(1, n + 1):
            if self.partition(0, 0, i, str(i * i)):
                result += i * i

        return result

    def partition(self, i, current, target, string):
        if i == len(string) and current == target:
            return True

        for j in range(i, len(string)):
            if self.partition(j + 1, current + int(string[i:j+1]), target, string):
                return True

        return False