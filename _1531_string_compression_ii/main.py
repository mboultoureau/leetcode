class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Solution 1: with NeetCode video: https://www.youtube.com/watch?v=ISIG3o-Xofg
        @lru_cache(None)
        def count(index, k, prev_char, prev_count):
            if k < 0:
                return math.inf
            
            if index == len(s):
                return 0

            if s[index] == prev_char:
                # Detect if number of characters increased (a --> a2, a9 --> a10, a99 --> a100)
                increment = 0
                if prev_count in [1, 9, 99]:
                    increment = 1
                result = increment + count(index + 1, k, prev_char, prev_count + 1)
            else:
                # Delete or don't delete?
                result = min(
                    count(index + 1, k - 1, prev_char, prev_count),
                    1 + count(index + 1, k, s[index], 1)
                )

            return result
                
        return count(0, k, "", 0)



        # Solution 2
        # if len(s) == k:
        #     return 0

        # @lru_cache(None)
        # def next(index, count, left, last):
        #     if index == len(s):
        #         return 0

        #     best = math.inf
        #     if last != -1 and s[index] == last:
        #         score = 0
        #         if count <= 1 or count == 9 or count == 99:
        #             score = 1

        #         best = min(best, next(index + 1, count + 1, left, last) + score)
        #         if left >= 1:
        #             best = min(best, next(index + 1, count, left - 1, last))

        #     else:
        #         best = min(best, next(index + 1, 1, left, s[index]) + 1)
        #         if left >= 1:
        #             best = min(best, next(index + 1, count, left - 1, last))

        #     return best

        # return next(0, 0, k, -1)