class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)

        for i in range(0, n + 1):
            arr[i] = Counter(bin(i))["1"]

        return arr