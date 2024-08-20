class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        

        @lru_cache(None)
        def dfs(aliceTurn, i, M):
            if i == len(piles):
                return 0

            result = 0 if aliceTurn else float("inf")
            total = 0

            for j in range(1, 2 * M + 1):
                if i + j > len(piles):
                    break 
                
                total += piles[i + j - 1]
                if aliceTurn:
                    result = max(result, total + dfs(False, i + j, max(M, j)))
                else:
                    result = min(result, dfs(True, i + j, max(M, j)))

            return result

        return dfs(True, 0, 1)