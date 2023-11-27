class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        result = []
        for n in arr:
            result.append((str(bin(n))[2:].count('1'), n))

        result.sort()
        return [x[1] for x in result]