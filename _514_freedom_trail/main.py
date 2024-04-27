class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        @lru_cache(None)
        def dfs(ring, keyI):
            if keyI == len(key):
                return 0

            result = math.inf

            for i in range(len(ring)):
                if ring[i] == key[keyI]:
                    rotations = min(i, len(ring) - i)
                    newRing = ring[i:] + ring[:i]
                    remaining = dfs(newRing, keyI + 1)
                    result = min(result, rotations + remaining + 1)

            return result

        return dfs(ring, 0)