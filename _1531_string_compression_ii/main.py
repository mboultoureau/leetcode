class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) == k:
            return 0

        @lru_cache(None)
        def next(index, count, left, last):
            if index == len(s):
                return 0

            best = math.inf
            if last != -1 and s[index] == last:
                score = 0
                if count <= 1 or count == 9 or count == 99:
                    score = 1

                best = min(best, next(index + 1, count + 1, left, last) + score)
                if left >= 1:
                    best = min(best, next(index + 1, count, left - 1, last))

            else:
                best = min(best, next(index + 1, 1, left, s[index]) + 1)
                if left >= 1:
                    best = min(best, next(index + 1, count, left - 1, last))

            return best

        return next(0, 0, k, -1)