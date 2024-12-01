class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = Counter(arr)
        for n in arr:
            if (n == 0 and numbers[0] > 1) or (n != 0 and numbers[n * 2] > 0):
                return True

        return False