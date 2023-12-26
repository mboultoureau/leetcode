class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.nbPossibilities(0, n, k, target) % (10 ** 9 + 7)

    @lru_cache(maxsize=None)
    def nbPossibilities(self, i: int, n: int, k: int, target: int) -> int:
        if target == 0 and i == n:
            return 1

        if target < 0 or i == n:
            return 0

        result = 0
        for x in range(1, k + 1):
            result += self.nbPossibilities(i + 1, n, k, target - x)

        return result