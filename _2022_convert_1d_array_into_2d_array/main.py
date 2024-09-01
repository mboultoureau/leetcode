class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        result = [[0] * n for _ in range(m)]
        print(result)

        for r in range(m):
            for c in range(n):
                result[r][c] = original[r * n + c]

        return result