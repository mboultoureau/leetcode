class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        candidates = [0 for _ in range(26)]

        for c in reversed(s):
            index = ord(c) - ord('a')

            minimum = max(index - k, 0)
            maximum = min(index + k, 25)

            best = 0

            for i in range(minimum, maximum + 1):
                best = max(best, candidates[i])

            candidates[index] = best + 1

        return max(candidates)