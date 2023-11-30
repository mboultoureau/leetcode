class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = bin(n)[2:]
        nbOperations = 0

        for i in range(len(binary)):
            if binary[-i - 1] == '1':
                nbOperations = 2 ** (i + 1) - 1 - nbOperations

        return nbOperations