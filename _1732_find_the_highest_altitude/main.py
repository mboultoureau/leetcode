class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        current = 0
        for g in gain:
            current += g
            result = max(result, current)

        return result